# ADR-0030 — Executable Conformance and Exact-Head Proof

**Status:** ACCEPTED SUBJECT TO PR-HEAD WORKFLOW

## Context

Phase 0B candidate contracts cannot be frozen on prose review alone. Schema catalogs, lifecycle machines, migrations and fixtures require deterministic offline validation bound to the exact repository state being accepted.

## Decision

Ptah adopts a repository-local, backend-neutral conformance harness that:

1. validates JSON and JSON Schema 2020-12 structure;
2. enforces unique versioned schema URNs and local Ptah references;
3. validates catalog file and schema identity integrity;
4. validates lifecycle transitions and reachability;
5. validates fixture suite structure and stable expected failure codes;
6. executes versioned semantic rules and fixtures;
7. records typed Conformance Runs, Check Results and Reports;
8. binds reports to exact commit, catalog set, harness version and fixture set;
9. preserves failed, negative, skipped and inconclusive evidence;
10. blocks Phase 0B freeze when any required check is absent or failing.

## Consequences

- Contract defects become executable failures before implementation.
- CI provider status alone is not proof; uploaded typed reports are the evidence.
- Structural validity and semantic correctness remain separate.
- The harness may be replaced later if the typed records and exact-head proof semantics remain stable.
- WP14 owns the frozen golden and negative corpus; WP13 owns its execution mechanism.
