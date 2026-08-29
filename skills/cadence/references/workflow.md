# Cadence workflow reference

The lane is a confidence budget, not a checklist to complete mechanically.

Choose the project-context route in [project-context.md](project-context.md) before applying a lane. Project maturity changes what must be discovered, not the risk standard for a change.

## Quick lane

State the outcome; inspect the target and immediate callers; make the smallest compatible change; run the closest focused check (test, type check, lint, build, preview, or explicit manual observation); and inspect the diff. Move to Standard when unclear behaviour, multiple components, or a user-facing contract appears.

## Standard lane

Capture this in the conversation or the repository’s existing task format:

```text
Outcome: [observable result]
Acceptance criteria:
- [condition and expected result]
Constraints: [material constraints only]
Assumptions: [reversible assumptions, if any]
```

Plan vertical slices:

```text
Slice: [behaviour]
Seam/files: [likely boundary]
Proof: [test, check, or manual observation]
```

Implement one slice at a time. After the change, run relevant checks and inspect the diff against the criteria.

## Assured lane

Resolve material choices before implementation. Keep a decision note only if it will matter after the task:

```markdown
# Decision: [short title]

**Status:** accepted | proposed
**Context:** [risk and constraints]
**Decision:** [choice]
**Consequences:** [benefits, costs, rollback or migration]
**Verification impact:** [what must prove this safe]
```

If the decision needs product, legal, security, or another owner’s approval, request that decision rather than guessing.

Maintain this compact mapping in the existing issue, spec, or appropriate project document:

| Acceptance criterion | Slice / change | Verification | Status |
| --- | --- | --- | --- |
| [criterion] | [implementation seam] | [test/check/observation] | planned / evidenced |

Use a separate branch or worktree only when it reduces collision or protects valuable work. Ask an independent reviewer, when available and authorized, to assess both criterion compliance and code/architecture quality.

## Risk signals

Select Assured for authentication, authorization, tenancy, secrets, encryption, payments, sensitive data, destructive operations, schema migrations, external contracts, production reliability, compliance, or audit/sign-off needs. Select Standard for meaningful behaviour changes without those signals. Select Quick only when evidence supports its narrow scope.

## Verification hierarchy

Prefer the strongest practical evidence closest to the changed behaviour:

1. Focused automated regression test.
2. Type, lint, build, contract, integration, or migration check.
3. Controlled runtime observation or manual acceptance check with conditions stated.
4. A clearly reported limitation if none can run.

Run broader checks when repository rules or risk warrant them. Separate pre-existing failures from new ones; do not silently ignore either.
