# Cadence for Claude Code

This is Cadence’s self-contained Claude Code plugin distribution. It contributes the namespaced `/cadence:cadence` skill for risk-adaptive planning, architecture, implementation, verification, and review.

## Install from GitHub

In Claude Code:

```text
/plugin marketplace add pandey1992/cadence
/plugin install cadence@cadence-marketplace
```

Choose an installation scope, then run `/reload-plugins` if prompted. Use `/cadence:cadence` followed by your request.

## Develop locally

From the repository root:

```bash
claude plugin validate ./plugins/claude-cadence
claude plugin validate .
claude --plugin-dir ./plugins/claude-cadence
```

The second validation command checks the repository marketplace. Claude Code is not bundled with Cadence; install it separately before running these commands.

See the repository [README](../../README.md) for usage examples and the full project rationale.
