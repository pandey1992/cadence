#!/usr/bin/env bash
set -euo pipefail

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Cadence check must run inside a Git worktree." >&2
  exit 2
fi

git diff --cached --check

if [[ "${1:-}" == "--" ]]; then
  shift
  if [[ "$#" -eq 0 ]]; then
    echo "Expected a check command after --." >&2
    exit 2
  fi
  "$@"
fi
