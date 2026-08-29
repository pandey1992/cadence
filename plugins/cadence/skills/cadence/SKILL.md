---
name: cadence
description: Plan and implement production software changes with risk-adaptive alignment, architecture care, verification, and review. Use for features, bugs, refactors, migrations, design reviews, or AI-assisted implementation where confidence, traceability, or scope control matters; not for purely informational questions.
---

# Cadence

Use Cadence to deliver a working, evidenced change without imposing enterprise ceremony on low-risk work. Match the process to the consequences of being wrong.

## Orient and choose a lane

Inspect repository instructions, current status, relevant code, tests, checks, and the closest existing implementation. Establish the observable outcome, material constraints, existing conventions, and risk. Ask only when an unresolved decision materially changes behaviour; otherwise state a reversible assumption and proceed.

| Lane | Indicators | Minimum evidence |
| --- | --- | --- |
| **Quick** | Narrow, reversible, well-understood change without contract risk | Inspect target and run the closest practical check |
| **Standard** | Normal feature, bug fix, or refactor with meaningful behaviour | Acceptance criteria, small verifiable plan, relevant verification, diff review |
| **Assured** | Security, authorization, money, sensitive data, migration, public contract, production reliability, compliance, or high blast radius | Durable decisions where needed, criterion-to-verification mapping, focused regression coverage, architecture review, independent review when available |

Let the user select a lane. Escalate only the affected concern. For detailed lane guidance, read [workflow.md](references/workflow.md).

## Implement in verifiable slices

For Standard and Assured work, give a concise plan before broad implementation. Each slice has one observable behaviour, a likely seam, and proof it works. Prefer a failing test before a stable behaviour boundary when the repository supports it; use the strongest meaningful feedback for visual or exploratory work. Never report a test as red or green unless observed.

Use a branch or Git worktree when it reduces collisions or protects valuable work. Creating a branch, worktree, ticket, pull request, deployment, or persistent artifact changes state: obtain appropriate authorization and preserve existing user work.

## Design, review, and improve architecture

At a meaningful module, data, or integration boundary, identify ownership, public contract, dependency direction, failure/rollback path, and relevant quality attributes before implementation. Favor a small coherent interface over an additional pattern or layer by default.

Review the final diff for new coupling, leaking infrastructure or policy concerns, duplicate rules, unclear ownership, and contract breaks. For an improvement request, survey first and give evidence-backed, incremental candidates instead of proposing a broad rewrite. Read [architecture.md](references/architecture.md) for design and review prompts.

## Finish honestly

Inspect the final diff, run the strongest relevant feasible checks, and compare acceptance criteria with observed evidence. State unrun checks and why. Report the outcome first, then changed areas, verification, residual risks, and follow-ups. Never claim a review, merge, deployment, or validation that did not occur.
