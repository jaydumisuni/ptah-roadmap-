# ADR-0021 Correction 001 — Runtime Catalog 0.1.2

**Status:** ACCEPTED CORRECTION  
**Date:** 2026-07-19  
**Parent decision:** `ADR-0021-NODE-FACILITY-PROVIDER-CAPABILITY-HEALTH-BOUNDARY.md`  
**Implementation authorization:** NONE

## Purpose

Preserve ADR-0021 as accepted decision history while correcting the candidate-catalog reference after proof-vocabulary and local/remote lifecycle review.

## Correction

The ADR-0021 section **Schema and conformance decision** is interpreted as:

- 19 runtime record schemas in `schemas/phase-0b/runtime/schema-catalog.v0.1.2.json`;
- six namespaced lifecycle machines selected by that catalog;
- conventions and `0.1.1` corrections;
- migration/compatibility record;
- extended positive/negative fixtures;
- consolidated safety net and `0.1.1` corrections.

The ADR-0021 related-record reference:

```text
schemas/phase-0b/runtime/schema-catalog.v0.1.0.json
```

is superseded by:

```text
schemas/phase-0b/runtime/schema-catalog.v0.1.2.json
```

## Authoritative lifecycle selection

Runtime catalog `0.1.2` selects:

- `node.enrollment.lifecycle` `0.1.1`;
- `node.lifecycle` `0.1.0`;
- `facility.lifecycle` `0.1.0`;
- `facility.instance.lifecycle` `0.1.1`;
- `provider.lifecycle` `0.1.0`;
- `provider.instance.lifecycle` `0.1.2`.

Provider Instance lifecycle `0.1.2` supersedes `0.1.1` because it:

1. uses exact local-Node versus remote-service locality;
2. forbids fictional Node evidence for remote Providers;
3. requires exact-generation correlated evidence for lifecycle `failed`;
4. keeps transient health `unhealthy` separate from durable lifecycle failure;
5. retains only registered WP02 proof vocabulary.

## No architectural change

This correction does not reverse ADR-0021. It makes the accepted decision's machine-readable references match the already accepted Node/Facility/Provider boundary.

No runtime, dependency or backend selection is authorized.