# Example: brownfield feature and improvement

Prompt:

```text
Use $cadence to add invoice-payment retry notifications to this existing billing service and identify the smallest architecture improvement needed to make retries reliable.
```

Cadence should select Brownfield and Assured. Before editing, it should inspect the payment workflow, retry scheduler, notification integration, state transitions, tests, configuration, and deployment/runbook context. It should map the change surface: invoice/payment states, idempotency key, retry ownership, outbound side effects, customer preferences, and failure/rollback behaviour.

A good incremental plan might add characterization coverage for existing retry rules, put retry policy behind the coherent billing owner, use an outbox or adapter only if the current coupling makes delivery unreliable, and verify duplicate suppression plus a partial-failure recovery path. It should not rewrite the billing service merely because the current design is awkward.
