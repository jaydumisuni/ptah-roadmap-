# Phase 0B WP13 — Cross-Contract Migrations and Executable Conformance

**Status:** CANDIDATE BLUEPRINT
**Implementation authorization:** CONFORMANCE HARNESS ONLY AFTER PACKAGE APPROVAL

## Objective

Prove that Phase 0B contracts are mutually coherent and executable as schemas/state machines without selecting production runtime backends.

## Harness requirements

1. Load every active local schema catalog with network access disabled.
2. Validate JSON Schema 2020-12 syntax, unique absolute URNs and collision-free entity kinds.
3. Validate namespaced state-machine definitions, transition reachability and terminal-state consistency.
4. Validate positive fixtures and prove every negative fixture fails for the intended reason.
5. Execute semantic invariants that JSON Schema cannot express.
6. Test directional migrations, unknown-field preservation, tombstones, supersession and referential integrity.
7. Test stale generation, stale connection epoch, stale Lease/fence and duplicate/late evidence rejection.
8. Test public/private audience, redaction, retention and secret-field prohibitions.
9. Test backend replacement while preserving stable public identities.
10. Produce immutable receipted reports binding harness revision, catalogs, fixtures, environment and results.

## Cross-contract scenarios

- Workspace restore creates new runtime generations while preserving Objects and uncertain external effects;
- resumable transfer produces accepted Content/Object only after verification;
- Build outputs bind exact Attempts and later survive Provider replacement;
- Device disconnect during write becomes uncertain and blocks blind retry;
- browser semantic action rejects stale Screen Context;
- Plugin revocation removes capability without rewriting historical outputs;
- isolation fence prevents old Provider generation from committing;
- security Finding and reproduction evidence remain distinct from release approval.

## Migration matrix

Every active schema requires: source version, target version, direction, loss classification, authority, rollback policy, compatibility window, fixture and expected evidence. Breaking migrations require explicit ADR and cannot silently reinterpret old records.

## Exit gate

WP13 closes only when the harness runs deterministically in CI and locally, all active catalogs pass, intended negatives fail, semantic invariants pass and the proof report is retained as an Artifact/Evidence record.

## Outputs

Harness specification, migration matrix, fixture manifest, semantic-rule registry, report schema, safety net, package record and ADR-0030.
