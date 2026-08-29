# Cadence Codex plugin

This is the installable Codex distribution of Cadence. Its core skill selects proportionate engineering rigor for a feature, fix, refactor, migration, design review, or architecture improvement.

For the full rationale, lanes, examples, and contributor guidance, see the repository [README](../../README.md). The distributable skill is intentionally self-contained inside `skills/cadence`.

## Local development

Validate the plugin from the repository root:

```bash
python3 /home/suraj/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/cadence
python3 /home/suraj/.codex/skills/.system/skill-creator/scripts/quick_validate.py plugins/cadence/skills/cadence
```

The optional Git hook is not installed automatically. See [hooks/README.md](hooks/README.md).
