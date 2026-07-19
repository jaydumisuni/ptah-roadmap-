# Phase 0B WP14 — Golden/Negative Corpus and Proof-Plan Freeze

**Status:** CANDIDATE BLUEPRINT
**Implementation authorization:** NONE

## Objective

Freeze the lawful, reproducible corpus and exact proof plan that Phase 0C will use to select and authorize the first vertical slice.

## Corpus classes

- canonical positive records for every active schema and state machine;
- malformed and structurally invalid records;
- semantically invalid but structurally valid records;
- stale generation/epoch/Lease/fence evidence;
- duplicate, late and contradictory Events/Receipts;
- partial/corrupt archives, documents, media, executables, firmware and disks;
- unsupported and opaque formats with bounded negative capability evidence;
- interrupted transfers and uncertain finalize/commit/delete cases;
- workspace/checkpoint/restore and unresolved external-effect cases;
- cache poisoning, volatile-input and secret-leakage cases;
- device disconnect/re-enumeration/partial-write cases;
- stale browser/UI snapshots and ambiguous-action cases;
- Plugin incompatibility/revocation/rollback cases;
- security disagreement, false-positive and failed-reproduction cases;
- backend replacement and migration cases.

## Fixture law

Every fixture has immutable bytes/digest, licence/source permission, audience, expected validation result, expected semantic-rule result, exact expected Receipts/Evidence, supported platforms and retention policy. Private THETECHGUY evidence may inform private fixtures but cannot be published without explicit authorization and redaction review.

## Proof-plan freeze

The frozen plan must name exact:

1. catalogs and schema versions;
2. state machines and transitions;
3. harness revision and environment;
4. Nodes/Providers/Facilities or simulation boundaries;
5. Activities, Operations, Attempts and required Receipts;
6. positive success criteria and negative rejection criteria;
7. concurrency, recovery, migration and backend-replacement scenarios;
8. privacy/redaction and secret-leakage checks;
9. performance/resource measurements;
10. artifact/proof-bundle outputs and reviewer authority.

## Phase 0B exit gate

- corpus manifest complete and hashes pinned;
- licence/audience review complete;
- WP13 harness passes the full corpus;
- no unresolved identity, migration, authority or proof ambiguity blocks the first slice;
- cross-package review accepts Phase 0B freeze;
- Phase 0C readiness decision records remaining implementation choices without reopening contract identity.

## Outputs

Corpus policy, manifest schemas, fixture tree, proof-plan template, frozen proof plan, cross-package review, Phase 0B freeze ADR and Phase 0C readiness record.
