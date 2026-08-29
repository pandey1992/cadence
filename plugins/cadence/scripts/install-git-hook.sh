#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
hook_target="$repo_root/.git/hooks/pre-commit"
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
hook_source="$script_dir/../hooks/pre-commit"

if [[ ! -d "$repo_root/.git/hooks" ]]; then
  echo "No writable .git/hooks directory found." >&2
  exit 2
fi

if [[ -e "$hook_target" ]]; then
  echo "Refusing to overwrite existing hook: $hook_target" >&2
  echo "Merge the command from plugins/cadence/hooks/pre-commit into it manually." >&2
  exit 1
fi

cp "$hook_source" "$hook_target"
chmod +x "$hook_target"
echo "Installed Cadence pre-commit hook."
