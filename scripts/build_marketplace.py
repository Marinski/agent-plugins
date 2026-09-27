#!/usr/bin/env python3
"""Build .claude-plugin/marketplace.json from sources.json + sources.lock.json.

Each source is another git repo that already has its own plugin marketplace.
For every plugin in that upstream manifest, this emits an entry whose `source`
points back at the upstream repo, pinned to the commit recorded in
sources.lock.json. Nothing is copied or vendored: tools fetch each plugin
straight from its upstream at that exact commit.

Usage:
  build_marketplace.py            rebuild the manifest from the current pins
  build_marketplace.py --check    fail if the committed manifest is out of date
  build_marketplace.py --update   move every pin to the tip of its tracked ref,
                                  then rebuild (optionally --summary FILE writes
                                  a Markdown changelog of what moved)

Per-source options in sources.json:
  id          short unique name (required)
  repo        git URL (required)
  ref         branch or tag to track (required)
  manifest    path to the upstream manifest (default .claude-plugin/marketplace.json)
  prefix      prepended to every plugin name from this source, to avoid clashes
  include     only take these upstream plugin names
  exclude     skip these upstream plugin names
  enabled     false to keep the entry without building it
"""

from __future__ import annotations

import argparse
import copy
import json
import posixpath
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources.json"
LOCK = ROOT / "sources.lock.json"
MANIFEST = ROOT / ".claude-plugin" / "marketplace.json"
DEFAULT_UPSTREAM_MANIFEST = ".claude-plugin/marketplace.json"
GITHUB_RE = re.compile(r"^https://github\.com/([^/]+/[^/]+?)(?:\.git)?/?$")


def git(*args: str, cwd: Path | None = None) -> str:
    result = subprocess.run(["git", *args], cwd=cwd, check=True, text=True, capture_output=True)
    return result.stdout


def resolve_ref(repo: str, ref: str) -> str:
    out = git("ls-remote", repo, f"refs/heads/{ref}", f"refs/tags/{ref}", f"refs/tags/{ref}^{{}}")
    lines = [line.split("\t") for line in out.splitlines() if line]
    if not lines:
        sys.exit(f"ERROR: ref '{ref}' not found in {repo}")
    # A peeled annotated tag (^{}) points at the commit; prefer it when present.
    peeled = [sha for sha, name in lines if name.endswith("^{}")]
    return peeled[0] if peeled else lines[0][0]


def read_upstream_manifest(repo: str, sha: str, path: str, cache: Path) -> dict:
    work = cache / sha
    if not work.exists():
        work.mkdir(parents=True)
        git("init", "-q", cwd=work)
        git("fetch", "-q", "--depth", "1", repo, sha, cwd=work)
    try:
        return json.loads(git("show", f"FETCH_HEAD:{path}", cwd=work))
    except subprocess.CalledProcessError:
        sys.exit(f"ERROR: {repo}@{sha[:7]} has no {path}")


def pinned_source(repo: str, sha: str, path: str) -> dict:
    """A plugin source pointing at `path` inside `repo`, pinned to `sha`."""
    if path in ("", "."):
        # Use the plain https URL rather than the `github` source type: on a
        # GitHub Actions runner `github` sources failed to clone while https
        # `url` / `git-subdir` sources installed fine.
        return {"source": "url", "url": repo, "sha": sha}
    return {"source": "git-subdir", "url": repo, "path": path, "sha": sha}


def plugin_path(source: str, plugin_root: str | None) -> str:
    path = source
    if plugin_root and not source.startswith("./"):
        path = posixpath.join(plugin_root, source)
    path = posixpath.normpath(path.lstrip("/"))
    if path.startswith(".."):
        raise ValueError(f"plugin source {source!r} points outside its repo")
    return "" if path == "." else path


def build(sources: dict, lock: dict, cache: Path) -> dict:
    out = copy.deepcopy(sources["marketplace"])
    out["plugins"] = []
    owners: dict[str, str] = {}

    for src in sources["sources"]:
        if src.get("enabled", True) is False:
            continue
        sid, repo = src["id"], src["repo"]
        pin = lock.get(sid)
        if not pin or pin.get("repo") != repo or pin.get("ref") != src["ref"]:
            sys.exit(f"ERROR: source '{sid}' has no matching pin in {LOCK.name}; run with --update")
        sha = pin["sha"]
        upstream = read_upstream_manifest(repo, sha, src.get("manifest", DEFAULT_UPSTREAM_MANIFEST), cache)
        plugin_root = (upstream.get("metadata") or {}).get("pluginRoot")
        include, exclude = src.get("include"), set(src.get("exclude", []))

        taken = 0
        for plugin in upstream.get("plugins", []):
            name = plugin["name"]
            if (include is not None and name not in include) or name in exclude:
                continue
            entry = copy.deepcopy(plugin)
            entry["name"] = src.get("prefix", "") + name
            if isinstance(plugin["source"], str):
                entry["source"] = pinned_source(repo, sha, plugin_path(plugin["source"], plugin_root))
            # Object sources already point at a remote; keep the upstream's own pin.
            if entry["name"] in owners:
                sys.exit(f"ERROR: plugin name '{entry['name']}' comes from both '{owners[entry['name']]}' "
                         f"and '{sid}'; set a \"prefix\" on one of them in {SOURCES.name}")
            owners[entry["name"]] = sid
            out["plugins"].append(entry)
            taken += 1

        missing = set(include or []) - {p["name"] for p in upstream.get("plugins", [])}
        if missing:
            sys.exit(f"ERROR: source '{sid}' includes unknown plugins: {', '.join(sorted(missing))}")
        if taken == 0:
            sys.exit(f"ERROR: source '{sid}' contributed no plugins")
    return out


def dump(data: dict) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def compare_link(repo: str, old: str | None, new: str) -> str:
    match = GITHUB_RE.match(repo)
    if not match:
        return f"`{(old or '')[:7]}` → `{new[:7]}`"
    base = f"https://github.com/{match.group(1)}"
    if not old:
        return f"new pin [`{new[:7]}`]({base}/commit/{new})"
    return f"[`{old[:7]}...{new[:7]}`]({base}/compare/{old}...{new})"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="fail if the committed manifest is stale")
    mode.add_argument("--update", action="store_true", help="move pins to the tip of each tracked ref")
    parser.add_argument("--summary", type=Path, help="with --update: write a Markdown changelog here")
    args = parser.parse_args()

    sources = json.loads(SOURCES.read_text())
    ids = [s["id"] for s in sources["sources"]]
    if len(ids) != len(set(ids)):
        sys.exit(f"ERROR: duplicate source ids in {SOURCES.name}")
    lock = json.loads(LOCK.read_text()) if LOCK.exists() else {}

    if args.update:
        changes = []
        new_lock = {}
        for src in sources["sources"]:
            if src.get("enabled", True) is False:
                continue
            sid = src["id"]
            sha = resolve_ref(src["repo"], src["ref"])
            old = lock.get(sid, {})
            old_sha = old.get("sha") if old.get("repo") == src["repo"] else None
            if old_sha != sha:
                changes.append(f"- **{sid}** (`{src['ref']}`): {compare_link(src['repo'], old_sha, sha)}")
            new_lock[sid] = {"repo": src["repo"], "ref": src["ref"], "sha": sha}
        dropped = sorted(set(lock) - set(new_lock))
        changes += [f"- **{sid}**: removed" for sid in dropped]
        lock = new_lock
        LOCK.write_text(dump(lock))
        if args.summary:
            args.summary.write_text("\n".join(changes) + "\n" if changes else "")
        print("\n".join(changes) if changes else "All pins already at the tip of their refs.")

    with tempfile.TemporaryDirectory() as tmp:
        manifest = dump(build(sources, lock, Path(tmp)))

    if args.check:
        current = MANIFEST.read_text() if MANIFEST.exists() else ""
        if current != manifest:
            sys.exit(f"ERROR: {MANIFEST.relative_to(ROOT)} is out of date; "
                     "run scripts/build_marketplace.py and commit the result")
        print(f"{MANIFEST.relative_to(ROOT)} is up to date "
              f"({len(json.loads(manifest)['plugins'])} plugins).")
        return

    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(manifest)
    print(f"Wrote {MANIFEST.relative_to(ROOT)} ({len(json.loads(manifest)['plugins'])} plugins).")


if __name__ == "__main__":
    main()
