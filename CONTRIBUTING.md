# Contributing to Cadence

Cadence should make an agent more reliable without turning ordinary work into paperwork.

## Before proposing a change

- Begin with a real task or failure mode.
- State what decision the new guidance changes.
- Keep `SKILL.md` concise; put reused, conditional detail in `references/`.
- Do not make worktrees, TDD, subagents, tickets, documentation, or architecture diagrams universal mandates without a concrete risk boundary.

## Pull requests

Include a representative prompt, the intended before/after behaviour, and validation performed. Run:

```bash
python3 /home/suraj/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/cadence
```

If that absolute path is unavailable, use the validator bundled with your installed Skill Creator skill.

Write constraints that alter an agent’s behaviour. Prefer decision criteria over a rigid sequence, distinguish required safeguards from recommendations, and do not include credentials, customer data, or proprietary source code.
