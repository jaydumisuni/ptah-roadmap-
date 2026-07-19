# Phase 0B WP06 — Transfer, Synchronization, Conflict and Backup

**Status:** CANDIDATE COMPLETE — DOWNSTREAM CONTRACT USE APPROVED; IMPLEMENTATION FREEZE DEFERRED  
**Date:** 2026-07-19  
**Runtime implementation:** NOT STARTED  
**Dependency/backend selection:** NOT STARTED

## Purpose

Turn the frozen transfer, synchronization, revision/conflict, storage-replica and backup architecture into exact candidate identities, schemas, lifecycles, migration rules and conformance expectations.

WP06 closes the contract boundary needed to move and verify bytes, resume safely, reconcile revisions without data loss, preserve recoverable history, prune safely and perform storage-level restore without confusing any of those operations with Object acceptance, Workspace checkpointing, export or application recovery.

## Normative records

- `contracts/PHASE-0B-WP06-TRANSFER-SYNC-CONFLICT-BACKUP-CONVENTIONS.md`
- `contracts/PHASE-0B-WP06-ENTITY-KIND-SUPPLEMENT.md`
- `schemas/phase-0b/transfer/schema-catalog.v0.1.0.json`
- `migrations/phase-0b/WP06-TRANSFER-SYNC-CONFLICT-BACKUP-MIGRATION-COMPATIBILITY.md`
- `conformance/PHASE-0B-WP06-TRANSFER-SYNC-CONFLICT-BACKUP-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp06/transfer-sync-backup-cases.v0.1.0.json`

## Candidate schema set

The Transfer catalog contains 18 active schemas:

1. shared definitions;
2. Transfer Request;
3. Transfer Run;
4. Transfer Manifest;
5. Transfer Progress Snapshot;
6. Transfer Verification;
7. Sync Relationship;
8. Sync Cursor;
9. Sync Run;
10. Sync Conflict;
11. Sync Conflict Resolution;
12. Backup Policy;
13. Backup Snapshot;
14. Backup Verification;
15. Backup Prune Decision;
16. Backup Restore Decision;
17. Backup Restore Run;
18. Replica Reconciliation.

Dependencies:

- `ptah.common` `0.1.0`;
- `ptah.activity` `0.1.1`;
- `ptah.object` `0.1.0`;
- `ptah.runtime` `0.1.2`;
- `ptah.workspace` `0.1.0`.

## Lifecycle machines

Seven namespaced lifecycles are included:

- `transfer.request.lifecycle`;
- `transfer.run.lifecycle`;
- `sync.relationship.lifecycle`;
- `sync.run.lifecycle`;
- `sync.conflict.lifecycle`;
- `backup.policy.lifecycle`;
- `backup.restore_run.lifecycle`.

Progress, verification, cursor freshness, snapshot completeness/consistency, restoreability and replica observations remain separate from lifecycle.

## Accepted boundaries

### Transfer

1. Transfer Request, logical Run, physical Attempt, Manifest, Progress and Verification remain separate.
2. source/destination provider/task/resume IDs are aliases only.
3. logical Operation persists across retries; every physical Attempt gets new identity/nonce/generations/epoch.
4. Resume is valid only when source identity/validators, destination partial state, protocol, range/checksum scheme, encryption/compression, idempotency and authority match.
5. source/destination/provider/policy drift invalidates incompatible resume state.
6. Progress Events/Snapshots are observations, not durable completion.
7. bytes received, provider acknowledged, transport verified, canonical Content digest verified, destination read-back, Location registration and Object acceptance remain separate.
8. provider/HTTP/multipart success cannot create verified Location/Object truth.
9. digest mismatch leaves partial/quarantined state and prevents atomic promotion.
10. unsafe non-idempotent finalize/commit/delete outcomes become `uncertain`, not automatic retries.

### Synchronization

1. Sync Relationship is durable policy, not proof endpoints are equal/current.
2. Cursor is endpoint/relationship/protocol/provider-generation scoped and expiring.
3. stale/lost/incompatible Cursor triggers rescan/reconciliation.
4. Sync Run freezes start cursors/endpoints, discovers/reconciles changes, executes Transfer Runs, records conflicts, verifies destination and advances cursors only after accepted state.
5. completion is bounded by frozen endpoints/cursors/included scope/time.
6. rename/move preserves Object identity when evidence supports it.
7. deletion/tombstone propagation, Location deletion and shared Content-byte deletion remain separate.
8. sync success never implies backup recoverability.

### Conflict

1. Conflict is first-class and retains competing revisions/tombstones/aliases/policies/base/clocks/evidence.
2. last-write-wins is not default authority.
3. Resolution is separate, named and policy-bound.
4. merge creates a new Revision with explicit parents/provenance.
5. choosing one side never deletes competing history.
6. delete-modify, permission/privacy and identity ambiguity require stronger review unless an explicit proven policy applies.
7. resolution requires follow-up destination verification.

### Backup

1. Backup Policy activation does not prove a backup exists.
2. Backup Snapshot is immutable and records included, reused, excluded, missing, failed and unknown entries.
3. required missing/failed/unknown item prevents complete-for-declared-scope.
4. incremental/deduplicated Snapshots retain parent/chunk dependency graphs.
5. Snapshot creation/provider acknowledgement does not prove repository readability.
6. Verification domains remain separate: manifest, index, chunk digest, sampled/full read-back, decryption, metadata, retention and independent copy.
7. Verification is time-bounded and sampled is not full.
8. encryption key remains separate; unavailable/revoked key can make ciphertext non-restorable.
9. backup, sync, replica, checkpoint and export remain distinct mechanisms.

### Prune

1. Prune Decision is separate from deletion execution.
2. retention, legal hold, dependency graph, protected restore points, copy/failure-domain, repository health, authorization and dry-run impact are mandatory.
3. unknown/failed required check blocks or narrows prune.
4. deletion Receipts and post-prune verification are mandatory.
5. age or duplicate digest alone never authorizes deletion.

### Storage restore

1. Backup Restore Decision is target-specific and expiring.
2. missing key/dependency/policy/capacity/provider compatibility blocks or narrows restore.
3. partial restorable scope requires explicit approval.
4. Restore Run is new Activity/Attempts and may create Transfer Runs/conflicts/Locations/Object revisions.
5. restored-unverified bytes do not become verified Location.
6. `restored_storage` proves selected bytes/metadata restored and verified only.
7. Workspace/runtime/application recovery requires WP05 Restore/Recovery Verification and is never implied.

### Replica reconciliation

1. expected and observed Locations remain separate.
2. present-unverified is not present-verified.
3. repair is explicit Transfer/repair Activity with verification.
4. replica is not backup without retained Backup Policy/Snapshot history.
5. backup copy is not live replica without Location registration/current policy.

## Migration closure

The migration record forbids:

- provider/task ID as canonical identity;
- progress/provider acknowledgement promoted to accepted Content/Location;
- resume after source/destination/protocol/policy drift;
- retry Attempts collapsed;
- `in sync` promoted to permanent equality;
- conflict/revision/deletion evidence discarded;
- cursor advanced before verified destination state;
- sync/replica promoted to backup;
- incomplete Snapshot promoted to complete;
- encrypted Snapshot declared restorable without key/decryption evidence;
- unsafe prune without dependency/retention/hold/copy checks;
- storage restore promoted to application recovery;
- negative/partial/corrupt/failed evidence deletion.

## Conformance closure

The safety net and fixtures cover:

- interrupted resume and source/destination drift;
- duplicate finalization and uncertain provider commit;
- unknown-size streaming acceptance;
- provider acknowledgement/digest/read-back boundaries;
- stale Cursor, premature advancement and rescan;
- divergent revisions, rename and delete-modify conflicts;
- tombstone versus physical deletion;
- backup completeness/dependency/readability/key boundaries;
- sampled versus full verification;
- prune dependency/legal-hold/post-verification;
- storage restore versus runtime recovery;
- replica repair versus backup;
- Provider replacement and failure isolation.

Structural validation is insufficient. WP13 must execute typed-reference, arithmetic/range, digest-domain, idempotency, generation/epoch, cursor, revision-graph, conflict, retention, legal-hold, privacy, authority and proof invariants.

## Candidate-completion verdict

**WP06 is candidate-complete for downstream Phase 0B use.**

It does not prove any transfer engine, sync daemon, backup repository, encryption backend, cloud provider, pruning system or restore path exists or works.

## Deferred work

- Build/provenance — WP07;
- domain/device/application/browser/shell subtype contracts — later WPs;
- isolation/placement/reservation/Lease/secure grants — WP11;
- security/reproduction — WP12;
- executable harness and golden corpus — WP13/WP14;
- dependency/provider/backend selection — Phase 0C only.

## Acceptance decision

- `decisions/ADR-0023-TRANSFER-SYNC-CONFLICT-BACKUP-RESTORE-BOUNDARY.md`

## Do-not-build rule

> Candidate-complete contracts authorize downstream schema design only. They do not authorize selecting or deploying aria2, tusd, rclone, Syncthing, restic, cloud storage, databases, encryption systems, transfer daemons, backup repositories or restore services.