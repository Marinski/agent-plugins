# Agent Plugins

One plugin marketplace that brings together plugins from several repositories. Add it once and you get every plugin below. Each plugin is fetched straight from its own repository at an exact, reviewed commit.

```bash
# Claude Code
/plugin marketplace add Marinski/agent-plugins
/plugin install code-quality-skills@marinski-plugins

# GitHub Copilot CLI
copilot plugin marketplace add Marinski/agent-plugins
```

```jsonc
// VS Code settings.json (GitHub Copilot agent plugins)
"chat.plugins.marketplaces": ["Marinski/agent-plugins"]
```

## What's included

| Source | Tracks | Plugins |
|--------|--------|---------|
| [Marinski/ClaudeSkills](https://github.com/Marinski/ClaudeSkills) | `master` | document-skills, development-skills, database-skills, devops-skills, code-quality-skills, communication-skills |
| [Marinski/ai-enablement-prompts](https://github.com/Marinski/ai-enablement-prompts) | `main` | creating-prompts, figma-from-code, implement-workflow, code, react, react-mock, figma-react, playwright, trpc-prisma |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | `plugins` | *disabled until that repo publishes its marketplace branch* |

The exact commit of each source is in [`sources.lock.json`](./sources.lock.json).

## How it works

Nothing is copied or vendored, and there are no submodules. The repo holds three files that matter:

| File | Edited by | Purpose |
|------|-----------|---------|
| `sources.json` | you | Which repos to include, which branch or tag each one tracks, and optional filters |
| `sources.lock.json` | the update workflow | The exact commit each source is pinned to |
| `.claude-plugin/marketplace.json` | generated | One entry per upstream plugin, whose `source` points at the upstream repo at the pinned commit (`github` / `git-subdir` source with `sha`) |

`scripts/build_marketplace.py` reads each upstream's own `.claude-plugin/marketplace.json` at the pinned commit and rewrites every plugin's relative source into a pinned remote source. New plugins that appear upstream are picked up automatically at the next pin update. `.github/plugin/marketplace.json` is a symlink to the same file, for Copilot tools.

## Keeping it up to date

- **`update-pins.yml`** runs daily and on demand. It moves each pin to the tip of its tracked ref, regenerates the manifest, validates it, installs every plugin from its new pin, and then opens (or refreshes) **one PR** listing what moved, with a compare link per upstream. Merging that PR publishes the update; until then, users keep getting the old pins.
- **`check.yml`** runs on every PR and push. It fails if the manifest isn't exactly what the sources and pins generate, if Claude Code's validator rejects it, or if any plugin fails to install or registers nothing.

**Setup for the update workflow:**
- Turn on *Settings → Actions → General → Allow GitHub Actions to create and approve pull requests*.
- Optionally add a `PIN_UPDATE_TOKEN` secret (a fine-grained PAT or GitHub App token with contents and pull-requests write on this repo). This lets `check.yml` also run on the bump PRs, since PRs opened with the default token don't trigger workflows. The update workflow runs the same checks itself either way.

## Adding or changing a source

Edit `sources.json`:

```jsonc
{
  "id": "my-repo",                                  // unique short name
  "repo": "https://github.com/owner/my-repo.git",   // any git URL
  "ref": "main",                                    // branch or tag to track
  "prefix": "my-",                                  // optional: prefix plugin names to avoid clashes
  "include": ["plugin-a"],                          // optional: only these plugins
  "exclude": ["plugin-b"],                          // optional: skip these plugins
  "manifest": ".claude-plugin/marketplace.json",    // optional: upstream manifest path
  "enabled": false                                  // optional: keep but skip
}
```

The source repo must have its own plugin marketplace manifest. Then pin it, regenerate, and check:

```bash
python3 scripts/build_marketplace.py --update   # pin every source to its ref's tip + regenerate
python3 scripts/build_marketplace.py            # regenerate from the current pins only
claude plugin validate ./
./scripts/smoke-test-plugins.sh                 # or pass plugin names to test a subset
```

Two sources can't publish the same plugin name; the build stops and asks for a `prefix`.

## Compatibility

Pinned remote sources (`github`, `url`, and `git-subdir` with `sha`) are tested with Claude Code: CI installs every plugin this way. VS Code and Copilot CLI read the same manifest format, but check that your version supports `git-subdir` sources before relying on it there.
