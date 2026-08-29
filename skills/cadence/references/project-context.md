# Project-context routes

Choose this route after initial orientation. A **greenfield** project has no meaningful production code or established technical constraints. A **brownfield** project has code, users, data, integrations, deployment history, or local conventions that the change must preserve. A new module inside an existing system is brownfield at the system boundary and may use a greenfield approach inside the module.

## Greenfield: establish a safe starting shape

The goal is not to design the whole future system. Establish enough shared understanding and engineering feedback to ship the first thin, production-worthy slice.

1. **Frame the product.** Confirm primary users, the problem and outcome, first success measure, non-goals, and constraints such as compliance, budget, team capability, deadline, hosting, or integrations.
2. **Map the first slice.** Identify the smallest user journey that proves value end-to-end. Prefer a walking skeleton through UI/API/domain/persistence only where those layers are actually needed.
3. **Set architectural guardrails.** Name the initial module boundaries, ownership, dependency direction, data ownership, public contracts, and the quality attributes that matter now. Record an ADR only for a decision expensive to reverse.
4. **Create the feedback baseline.** Choose the runtime/dev command, test strategy appropriate to the first slice, formatting/type/lint checks, configuration/secrets approach, error handling and observability baseline, and CI check. Do not claim production readiness without a deploy/rollback path appropriate to the product.
5. **Deliver then evolve.** Implement the walking skeleton, verify it, and use the next concrete capability to decide whether another boundary or abstraction is justified.

Useful Greenfield outputs are a short outcome/constraints note, a first-slice plan, an architecture sketch or ADR only when consequential, and a runnable feedback loop. Avoid large backlogs, exhaustive domain models, microservices, or speculative schemas before evidence requires them.

## Brownfield: learn before changing

The goal is to preserve valuable, often undocumented behaviour while making the requested change safer and easier to evolve.

1. **Inventory the reality.** Read repository instructions, status, dependency/build files, top-level structure, relevant code and tests, CI, configuration, and the closest completed feature. Inspect history or issue context when it explains a non-obvious constraint.
2. **Map the change surface.** Trace callers, consumers, data flow, contracts, permissions, side effects, runtime configuration, and deployment/migration impact. State uncertainties rather than filling gaps with generic architecture.
3. **Protect current behaviour.** Run the existing focused checks before editing. Add a characterization or regression test when the affected behaviour is important but unprotected. Distinguish a pre-existing failure from one introduced by the change.
4. **Choose the smallest safe seam.** Extend a coherent owner when possible. If the architecture needs improvement, propose an incremental extraction, adapter, migration, or strangler step with compatibility and rollback evidence; do not combine an unrelated rewrite with a feature by default.
5. **Verify integration.** Test the new behaviour and affected contracts, then inspect the final diff for coupling, duplicated policy, hidden configuration, data/migration issues, and rollout risk.

Useful Brownfield outputs are a concise change-surface map, acceptance criteria, targeted regression evidence, and a migration/rollback note when the change is not trivially reversible.

## Route selection examples

| Situation | Route |
| --- | --- |
| New SaaS product with no code | Greenfield |
| Adding the first billing module to an existing app | Brownfield for the app; Greenfield inside the new module as needed |
| Replacing a legacy queue consumer | Brownfield |
| Prototype that will be discarded | Greenfield + Quick or Standard, with the disposable boundary stated explicitly |

## Shared completion standard

Both routes still require an observable outcome, proportionate verification, an honest final report, and architecture appropriate to the risk. The route controls the order of discovery and design—not permission to skip verification.
