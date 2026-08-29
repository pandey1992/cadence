---
name: cadence
description: "Plan and implement production software changes with risk-adaptive alignment, architecture care, verification, and review. Use for features, bugs, refactors, migrations, or AI-assisted implementation where confidence, traceability, or scope control matters; not for purely informational questions."
---

# Cadence

Use Cadence to produce a working, evidenced change without imposing enterprise ceremony on low-risk work. Match the process to the consequences of being wrong.

## Orient before proposing implementation

Inspect repository instructions, current status, relevant code, tests, checks, and the closest existing implementation. Establish the observable outcome, material constraints, existing conventions, and the risk lane. Ask a concise question only when a missing decision would materially change delivered behaviour; otherwise state a reversible assumption and proceed.

## Choose the lightest suitable lane

| Lane | Indicators | Minimum evidence |
| --- | --- | --- |
| **Quick** | Narrow, reversible, well-understood change without contract risk | Inspect target and run the closest practical check |
| **Standard** | Normal feature, bug fix, or refactor with meaningful behaviour | Acceptance criteria, small verifiable plan, relevant verification, diff review |
| **Assured** | Security, authorization, money, sensitive data, migration, public contract, production reliability, compliance, or high blast radius | Durable decisions where needed, criterion-to-verification mapping, focused regression coverage, architecture review, independent review when available |

Let the user select a lane. Escalate only the concern that needs it; a simple UI change in a payments product is not automatically Assured. Read [the workflow reference](references/workflow.md) after selecting a lane, and only the sections relevant to the work.

## Work in verifiable slices

For Standard and Assured work, give a concise plan before broad implementation. Each slice names one observable behaviour, its likely seam, and proof it works. Prefer a failing test before a behaviour change when the repository supports it and the boundary is stable; use the strongest meaningful feedback for visual or exploratory work. Never report a test as red or green unless observed.

Use a separate branch or Git worktree when parallel changes, experiments, or a dirty workspace make isolation valuable. Creating a branch, worktree, ticket, pull request, deployment, or persistent artifact changes state: obtain the required authorization and preserve existing user work.

## Design, review, and improve architecture

When a change crosses a meaningful module, data, or integration boundary, identify the owning module, public contract, dependency direction, failure/rollback path, and relevant quality attributes before implementing. Favor a small coherent interface over adding a layer or pattern by default.

Review the final diff for new coupling, leaking infrastructure or policy concerns, duplicate rules, unclear ownership, and contract breaks. For Assured work, request an independent architecture/spec review when tools and authorization permit. For a requested architectural improvement, survey first and present evidence-backed candidates; do not begin a broad rewrite without an agreed target and incremental migration path. See [architecture guidance](references/architecture.md).

## Preserve useful context, not paperwork

Update a project glossary or `CONTEXT.md` when a non-obvious recurring term would otherwise be ambiguous. Record an ADR only for consequential, durable, or disputed choices. For Assured work, maintain a compact criterion-to-verification mapping using the project’s existing documentation convention.

## Finish honestly

Inspect the final diff, run the strongest relevant feasible checks, and compare each acceptance criterion with observed evidence. State checks that could not run and why. Report outcome first, then changed areas, verification, and residual risks. Do not claim a review, merge, deployment, or validation that did not occur.
