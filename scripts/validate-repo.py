#!/usr/bin/env python3
"""Portable structural checks used locally and by CI."""

from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "docs/ARCHITECTURE.md",
    "skills/cadence/SKILL.md",
    "skills/cadence/references/workflow.md",
    "skills/cadence/references/architecture.md",
    "plugins/cadence/.codex-plugin/plugin.json",
    "plugins/cadence/skills/cadence/SKILL.md",
    "plugins/cadence/hooks/pre-commit",
    "plugins/cadence/scripts/cadence-check.sh",
    "plugins/cadence/scripts/install-git-hook.sh",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


for relative_path in REQUIRED:
    if not (ROOT / relative_path).is_file():
        fail(f"missing required file: {relative_path}")

placeholder = "[TODO" + ":"
for path in ROOT.rglob("*"):
    if path.is_file() and placeholder in path.read_text(errors="ignore"):
        fail(f"unfinished placeholder: {path.relative_to(ROOT)}")

manifest_path = ROOT / "plugins/cadence/.codex-plugin/plugin.json"
manifest = json.loads(manifest_path.read_text())
if manifest.get("name") != "cadence" or manifest.get("version") != "0.1.0":
    fail("plugin manifest must identify cadence at version 0.1.0")
if manifest.get("skills") != "./skills/":
    fail("plugin manifest must expose ./skills/")

print("Cadence repository structure is valid.")
