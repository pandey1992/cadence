# Greenfield and Brownfield routes

A greenfield project has no meaningful production code or established technical constraints. A brownfield project has code, users, data, integrations, deployment history, or local conventions that the change must preserve. A new module inside an existing system is brownfield at the system boundary and can be greenfield internally.

## Greenfield

Confirm users, problem, outcome, success measure, non-goals, and material constraints. Plan the smallest end-to-end walking skeleton. Define only the initial module boundaries, ownership, dependency direction, data ownership, public contracts, and quality attributes needed for that slice. Establish runnable development, proportionate tests/checks, configuration/secrets handling, observability, CI, and a deploy/rollback path appropriate to the product. Evolve further architecture from the next concrete capability, not speculation.

## Brownfield

Inspect instructions, status, structure, dependencies, relevant code/tests, CI, configuration, and the closest feature. Map callers, consumers, data flow, contracts, permissions, side effects, runtime configuration, and migration impact. Run focused existing checks; add characterization coverage for important unprotected behaviour. Extend the smallest coherent owner, or propose an incremental extraction/adapter/migration with compatibility and rollback proof. Do not combine an unrelated rewrite with a feature by default.

Both routes require observable outcomes, proportionate verification, and an honest final report. The route changes discovery order, not the quality standard.
