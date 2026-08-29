# Architecture guidance

Use this reference only when designing across a meaningful seam, reviewing architecture, or seeking improvement candidates.

## Design a change at a seam

Start from the behaviour and map its boundary:

| Question | Evidence to seek |
| --- | --- |
| Who owns this rule? | The module/service that can enforce it without reaching through another abstraction |
| What is the contract? | Inputs, outputs, errors, invariants, compatibility promises, and callers |
| Which direction may dependencies flow? | Existing layer/module rules and the smallest new dependency needed |
| What fails or rolls back? | Timeout, partial failure, retry/idempotency, migration, and recovery behaviour |
| What quality attribute matters? | Security, latency, availability, cost, accessibility, operability, or evolvability |

Explain the selected seam and one credible alternative when the choice is consequential. Prefer extending an existing coherent module over creating a new abstraction. Create a new boundary when it gives one owner a stable interface and removes—not merely relocates—coupling.

## Review a change

Review the final diff with these questions:

- Does one module own each business rule, or is it duplicated across handlers, UI, jobs, and persistence?
- Did a transport, framework, database, or vendor detail escape into domain-facing code without a reason?
- Is a new public contract versioned, validated, observable, and compatible with its consumers?
- Does the dependency direction still allow the higher-level policy to be tested independently?
- Are failure modes explicit, including partial completion and retries where relevant?
- Does the change make the next likely feature easier, or introduce a temporary shortcut without an exit path?

Report findings by consequence. A clear, evidenced concern is more useful than a catalog of stylistic preferences.

## Improve an existing architecture

Survey before proposing a refactor. Build candidates from evidence such as high change coupling, repeated policy branches, fragile integration seams, unclear ownership, test pain, recurring defects, or an expensive deployment/recovery path.

For each candidate, provide:

```text
Candidate: [short name]
Evidence: [files, dependencies, tests, incidents, or repeated change pattern]
Benefit: [specific capability or risk reduction]
Smallest safe step: [incremental, reversible move]
Proof: [how to show behaviour and architecture remain sound]
Cost/risk: [migration, compatibility, and rollout concern]
```

Do not recommend a rewrite merely because the current architecture is unfamiliar. Prioritize candidates with a concrete next change, a bounded migration, and observable benefit.

## Durable architecture decisions

Record an ADR when the decision has broad impact, meaningful alternatives, or a future reader would otherwise reverse it accidentally. Keep it concise: context, decision, consequences, migration/rollback, and verification impact. Use the project’s ADR convention; do not create a parallel directory without a reason.
