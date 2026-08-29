# Cadence lanes

## Quick

State the outcome; inspect the target and immediate callers; make the smallest compatible change; run the closest focused check (test, type check, lint, build, preview, or explicit manual observation); and inspect the diff. Move to Standard if unclear behaviour, multiple components, or a user-facing contract appears.

## Standard

Capture an outcome, acceptance criteria, material constraints, and reversible assumptions in the conversation or the project’s existing task format. Plan vertical slices:

```text
Slice: [behaviour]
Seam/files: [likely boundary]
Proof: [test, check, or manual observation]
```

Implement one slice at a time; verify relevant behaviour and inspect the final diff against the criteria.

## Assured

Resolve material choices before implementation. If the choice is durable, record context, decision, consequences, rollback/migration, and verification impact using the repository’s ADR convention. If approval is outside the agent’s authority, request it instead of guessing.

Maintain a compact mapping where the project already tracks work:

| Acceptance criterion | Slice / change | Verification | Status |
| --- | --- | --- | --- |
| [criterion] | [implementation seam] | [test/check/observation] | planned / evidenced |

Use isolation when it genuinely reduces risk. Request independent spec and code-quality review when available and authorized.

## Verification hierarchy

Prefer a focused automated regression test, then relevant static/build/contract/integration checks, then a controlled runtime observation. Clearly report a limitation when no meaningful check can run. Separate pre-existing failures from new ones.
