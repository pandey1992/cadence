# Cadence

Cadence is a risk-adaptive engineering skill for building production-quality software with an AI coding agent. It provides fast feedback for small changes and evidence, isolation, and review for consequential ones.

It combines three ideas without making every change pay for all of them:

- a compact shared domain vocabulary and durable decisions;
- a visible path from intended outcome to verification; and
- tight implementation feedback: tests where behaviour changes, repository checks, review, and ongoing architecture care.

## Why Cadence

AI can create code faster than a team can validate assumptions. Cadence asks: **what is the cheapest process that gives us sufficient confidence for this change?**

| Lane | Use it for | What Cadence requires |
| --- | --- | --- |
| Quick | Copy, styling, isolated configuration, or a safe one-file fix | Inspect, make the smallest change, run the closest check |
| Standard | Ordinary features, bug fixes, and refactors | Confirm outcome and constraints, plan vertical slices, verify changed behaviour, review the diff |
| Assured | Security, money, permissions, migrations, public APIs, regulated work, or high blast radius | Explicit decisions and acceptance criteria, traceability, focused tests, architecture review, and independent review |

The user can select a lane. Cadence escalates when uncertainty or consequences justify it, and de-escalates when evidence shows the work is simple.

## Architecture is a continuous loop

Cadence makes architecture visible at three moments:

1. **Design:** identify the module boundary, public contract, ownership, dependencies, and non-functional constraints before a change crosses a meaningful seam.
2. **Change review:** inspect whether the final diff deepens an existing module or leaks new coupling, policy, data access, or infrastructure concerns across layers.
3. **Improvement:** periodically survey for high-leverage simplifications and produce candidates with evidence—never a speculative rewrite plan.

This is deliberately not an architecture-astronaut exercise. Cadence prefers a small interface with coherent behaviour behind it, explicit dependency direction, and a safe evolution path over diagrams or patterns for their own sake.

## What it borrows—and changes

Cadence is original work informed by:

- [Matt Pocock's skills](https://github.com/mattpocock/skills): shared language, architecture records, and composable engineering practices.
- [Superpowers](https://github.com/obra/superpowers): design before implementation, honest red-green-refactor feedback, isolation where it helps, and review before completion.
- [AWS sample AI-DLC decisions-driven skill](https://github.com/aws-samples/sample-aidlc-decisions-driven-skill): decision gates, scope-aware workflows, and requirements-to-verification traceability.

Cadence is a single, portable, risk-adaptive skill—not a mandatory always-on pipeline. A worktree, detailed traceability, TDD, subagents, or architecture artifacts are selected by risk and project conventions rather than ritual.

## Install

### Codex

Copy `skills/cadence` into a discoverable skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/cadence ~/.codex/skills/cadence
```

Restart or refresh the session if it does not discover the skill immediately, then use:

```text
Use $cadence to add audit logging to account changes.
```

### Claude Code

Cadence is published as a Claude Code marketplace plugin. In Claude Code, add the marketplace and install it:

```text
/plugin marketplace add pandey1992/cadence
/plugin install cadence@cadence-marketplace
```

Choose the preferred installation scope when prompted, then run `/reload-plugins` if Claude Code requests it. Invoke the skill with:

```text
/cadence:cadence add audit logging to account changes
```

For local development without installation, start Claude Code from this repository with:

```bash
claude --plugin-dir ./plugins/claude-cadence
```

Plugin skills are namespaced, so the local development invocation is `/cadence:cadence`.

### Other agents

The core skill is plain Markdown. Copy `skills/cadence` to the location your agent uses for skills and invoke `cadence` with that agent’s convention. `agents/openai.yaml` is optional Codex UI metadata.

## What the skill does

Cadence inspects the repository, selects a risk lane, aligns on outcome and constraints, works in verifiable slices, and finishes with honest evidence. It uses project vocabulary and ADRs only when ambiguity or a lasting decision merits them. For changes at a meaningful seam it also designs and reviews the architecture; for established systems it can survey improvement opportunities before proposing a refactor.

Read the [workflow reference](skills/cadence/references/workflow.md) for lane selection, lightweight artifacts, and architecture guidance. The [Cadence architecture](docs/ARCHITECTURE.md) explains the product’s own design choices.

## Greenfield and brownfield

Cadence does not use one flow for every repository:

| Context | First priority | Architecture posture |
| --- | --- | --- |
| Greenfield | Prove the smallest valuable end-to-end journey | Create a minimal, reversible baseline and walking skeleton |
| Brownfield | Learn and preserve the system’s real behaviour | Map the change surface, add characterization evidence, then change the smallest safe seam |

A new module inside an existing system uses both: Brownfield at the integration boundary and Greenfield within the new module. See the full [project-context guide](skills/cadence/references/project-context.md), plus [greenfield](examples/greenfield-saas.md) and [brownfield](examples/brownfield-feature.md) examples.

## Examples

- [Standard feature](examples/standard-feature.md)
- [Assured migration](examples/assured-migration.md)
- [Greenfield SaaS first release](examples/greenfield-saas.md)
- [Brownfield feature and architectural improvement](examples/brownfield-feature.md)

## Design principles

- Evidence over ceremony.
- Progressive rigor: add process only when risk, a decision, or a handoff needs it.
- Existing repository conventions outweigh generic rules.
- No hidden writes: branches, worktrees, tickets, pull requests, deploys, and persistent docs need appropriate authorization.
- Never claim a check, review, merge, or deployment that did not occur.

## Repository layout

```text
skills/cadence/
├── SKILL.md                    # Agent entry point
├── agents/openai.yaml          # Optional Codex UI metadata
└── references/workflow.md      # Lanes, architecture, gates, and templates

plugins/
├── cadence/                     # Codex plugin distribution
└── claude-cadence/              # Claude Code plugin distribution
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The best contributions are real examples where Cadence added friction or missed an important quality signal.

## License and attribution

Cadence is released under the [MIT License](LICENSE). It is independently written; it does not copy instructions or implementation from its inspirations.
