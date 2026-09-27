#!/usr/bin/env bash
# Installs every plugin in the marketplace into a throwaway Claude Code config
# (fetching each from its pinned upstream commit) and fails if any plugin
# does not install or registers no components at all.
#
# Usage: ./scripts/smoke-test-plugins.sh [plugin-name ...]   (default: all)
# Requires: jq and the Claude Code CLI (override the binary with $CLAUDE).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CLAUDE="${CLAUDE:-claude}"
MANIFEST="$ROOT/.claude-plugin/marketplace.json"
MARKETPLACE_NAME="$(jq -r .name "$MANIFEST")"

CLAUDE_CONFIG_DIR="$(mktemp -d)"
export CLAUDE_CONFIG_DIR
export CLAUDE_CODE_PLUGIN_CACHE_DIR="$CLAUDE_CONFIG_DIR/cache"
trap 'rm -rf "$CLAUDE_CONFIG_DIR"' EXIT

$CLAUDE plugin marketplace add "$ROOT/" >/dev/null

if (( $# > 0 )); then
  plugins=("$@")
else
  mapfile -t plugins < <(jq -r '.plugins[].name' "$MANIFEST")
fi

errors=0
for plugin in "${plugins[@]}"; do
  if ! $CLAUDE plugin install "$plugin@$MARKETPLACE_NAME" >/dev/null 2>"$CLAUDE_CONFIG_DIR/err"; then
    echo "FAIL $plugin: install failed: $(tail -1 "$CLAUDE_CONFIG_DIR/err")" >&2
    errors=$((errors + 1))
    continue
  fi
  details="$($CLAUDE plugin details "$plugin")"
  # Sum every "<Kind> (N)" count in the component inventory.
  counts="$(echo "$details" | sed -nE 's/^[[:space:]]*(Skills|Agents|Commands|Hooks|MCP servers|LSP servers) \(([0-9]+)\).*/\1=\2/p' | paste -sd' ' -)"
  total="$(echo "$counts" | grep -oE '[0-9]+' | awk '{ s += $1 } END { print s + 0 }')"
  if (( ${total:-0} > 0 )); then
    echo "OK   $plugin: $counts"
  else
    echo "FAIL $plugin: installed but registered no components ($counts)" >&2
    errors=$((errors + 1))
  fi
done

if (( errors > 0 )); then
  echo "Smoke test failed for $errors of ${#plugins[@]} plugin(s)." >&2
  exit 1
fi
echo "All ${#plugins[@]} plugins installed and registered components."
