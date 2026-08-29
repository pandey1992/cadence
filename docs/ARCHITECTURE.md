# Cadence architecture

Cadence has a deliberately small core and optional delivery integrations.

```text
User request
    │
    ▼
Cadence skill ──► risk lane ──► alignment / architecture / implementation
    │                                      │
    │                                      ▼
    └──────────────────────────────► verification and honest handoff

Optional delivery support: Codex plugin • Git whitespace hook • CI structural validation
```

## Core: portable skill

`skills/cadence` is the source-oriented distribution. It is plain Markdown so it can be adopted by any agent harness. Its entry point contains the universally relevant decisions; conditional details live in small references:

- `workflow.md` supplies lane selection, planning, traceability, and verification guidance.
- `architecture.md` supplies design, review, and improvement prompts for meaningful seams.
- `project-context.md` separates Greenfield bootstrapping from Brownfield discovery and safe evolution.

This separation keeps routine invocation small while allowing a deeper architecture pass when the task calls for one.

## Distribution: Codex plugin

`plugins/cadence` is self-contained for Codex plugin installation. It includes a distribution copy of the skill, a valid plugin manifest, optional Git tooling, and no required external service or MCP dependency. The plugin manifest intentionally does not declare hooks because the Codex manifest schema does not support hook registration; the Git hook is an explicit, user-installed integration.

The standalone and plugin variants share the same principles. Changes that affect agent behaviour should be made to both distributions in the same pull request and checked with their respective validators.

## Optional Git hygiene

The Git pre-commit hook runs only `git diff --cached --check`. It catches whitespace errors cheaply without assuming language, package manager, test command, or deployment policy. Cadence itself discovers and runs repository-specific checks after inspecting the project; it never turns a guessed command into a universal blocking hook.

## Architectural invariants

- Lane selection is based on evidence and risk, not the project’s label or size.
- Persistent artifacts exist only when they support a future decision, handoff, or audit.
- Architecture review evaluates ownership, contracts, dependency direction, and failure behaviour—not pattern conformance.
- Integrations are opt-in and must not create hidden state or destroy existing user configuration.
- Completion claims require observed evidence, with limitations reported plainly.

## Evolution

Cadence should evolve from demonstrated prompts and outcomes. Add a rule only when it changes an agent decision in a repeatable way. New integrations should remain optional unless a reliable cross-harness capability makes them safe and useful by default.

The `tests/` directory validates deterministic repository behaviour: structural validation, the opt-in Git hook’s whitespace detection, and the presence of the project-context route in both supported distributions. It intentionally does not attempt to unit-test model reasoning; examples and real-user feedback are the behavioral evaluation loop for that.
