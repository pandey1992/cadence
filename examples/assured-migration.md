# Example: assured migration

Prompt:

```text
Use $cadence to migrate customer email addresses to encrypted storage without breaking login or account recovery.
```

Cadence should choose Assured because the work changes sensitive data, authentication-adjacent behaviour, and rollback risk. Expected outputs before broad implementation include:

- acceptance criteria for existing and new records, login, recovery, encryption-key access, and rollback;
- a durable decision for encryption approach and migration/rollback strategy;
- an incremental plan (schema compatibility, dual-read/write if needed, backfill, validation, cutover, cleanup);
- a criterion-to-verification map; and
- a focused independent review covering authorization, exposure in logs/errors, partial migration, idempotency, and recovery.

Cadence should not silently create a worktree, run the migration, or deploy it. Those need explicit authorization.
