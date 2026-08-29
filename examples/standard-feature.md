# Example: standard feature

Prompt:

```text
Use $cadence to add a visible count of unread notifications to the header.
```

Cadence should first inspect the header, notification query/state, and existing UI tests. A compact plan could be:

| Slice | Seam | Proof |
| --- | --- | --- |
| Calculate unread count | notification query or view model | focused query/unit test |
| Render an accessible badge | header component | component test or browser observation |
| Preserve zero state | header component | test: badge hidden or correctly labelled at zero |

This is normally Standard: it changes behaviour and crosses a data-to-UI seam, but it does not automatically require a worktree, ADR, or traceability manifest.
