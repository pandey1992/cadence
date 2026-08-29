# Architecture guidance

Use this reference for a meaningful seam, architecture review, or improvement request.

## Design

Identify the owning module, public contract (including errors and invariants), permitted dependency direction, failure/rollback behaviour, and the relevant quality attribute: security, latency, availability, cost, accessibility, operability, or evolvability. Prefer extending a coherent module; create a boundary only when it creates a stable owner and removes coupling.

## Review

Ask whether business rules have one owner, infrastructure details leak into policy code, public contracts are compatible and observable, dependencies still support independent testing, failure modes are explicit, and the next likely change becomes easier rather than relying on an unbounded shortcut.

## Improve

Survey before proposing a refactor. Use evidence such as repeated change coupling, duplicated policy, fragile integration seams, unclear ownership, test pain, recurring defects, or expensive deployment/recovery. For each candidate state the evidence, concrete benefit, smallest reversible step, proof, and migration risk. Do not recommend a rewrite solely because the current architecture is unfamiliar.
