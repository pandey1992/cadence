# Example: greenfield product

Prompt:

```text
Use $cadence to build the first release of a team stand-up app where a manager creates a team, members submit an update, and the manager sees a daily summary.
```

Cadence should select the Greenfield route, then normally Standard (or Assured if authentication, tenant isolation, or sensitive employee data changes the risk). It should establish:

- the first user journey: create team → invite/join → submit update → view summary;
- initial ownership and contracts, for example `teams`, `memberships`, and `updates`, without prematurely splitting services;
- a walking skeleton with one end-to-end verified path;
- a minimal feedback baseline: local run, tests for the business rule and permissions, type/lint/build checks, configuration/secrets handling, CI, and an appropriate deploy/rollback story; and
- only durable ADRs, such as tenancy/data isolation, when that decision is difficult to reverse.

It should not produce a complete multi-quarter roadmap, a microservice topology, or every future database table before the first journey works.
