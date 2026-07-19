# ADR-0023 — Transfer, Synchronization, Conflict, Backup and Storage-Restore Boundary

**Status:** ACCEPTED FOR PHASE 0B DOWNSTREAM CONTRACT DESIGN  
**Date:** 2026-07-19  
**Phase:** 0B-WP06  
**Implementation authorization:** NONE

## Context

Ptah must move and preserve bytes across local storage, Nodes, remote services and backup repositories while retaining immutable Content/Object identity, resumability, conflicts, retention, privacy and proof.

The frozen architecture and donors established mature mechanisms for resumable upload/download, concurrent transfer, cloud copy, revision vectors, encrypted backup and restore. No donor defines canonical Ptah Transfer, Sync, Conflict or Backup truth, and none may turn a progress signal/provider acknowledgement/sync flag/snapshot name into accepted Content or recovery proof.

## Decision

Ptah owns separate canonical records for:

1. Transfer Request;
2. Transfer Run;
3. Transfer Manifest;
4. Transfer Progress Snapshot;
5. Transfer Verification;
6. Sync Relationship;
7. Sync Cursor;
8. Sync Run;
9. Sync Conflict;
10. Conflict Resolution;
11. Backup Policy;
12. Backup Snapshot;
13. Backup Verification;
14. Backup Prune Decision;
15. Backup Restore Decision;
16. Backup Restore Run;
17. Replica Reconciliation.

Provider/task/multipart/resume IDs, URLs, paths, cloud keys, ETags, provider versions, process IDs, cursor tokens and snapshot display names remain scoped aliases/evidence.

## Transfer boundary

Transfer Request, logical Run, WP02 Operation, physical Attempts, immutable Manifest, Progress observations and final Verification remain separate.

One logical Run persists across retries. Each physical Attempt receives new identity, nonce and exact Node/Provider/workload generations/connection epoch.

Resume is valid only when source identity/validators, destination partial state, protocol/chunk/range/checksum scheme, encryption/compression, idempotency and current authority match. Drift invalidates the partial state.

Provider acknowledgement, HTTP success, range completion or bytes received do not create accepted Content/Object/Location truth. Applicable byte count, canonical digest, destination read-back, Location registration and atomic promotion must pass.

Unsafe non-idempotent finalize/commit/delete outcomes become `uncertain`; they are not retried automatically.

## Synchronization boundary

Sync Relationship is policy/endpoint relationship, not permanent equality.

Cursor is immutable, endpoint/relationship/protocol/provider-generation scoped and expiring. Missing/stale/incompatible Cursor causes rescan/reconciliation, not skipped changes.

Sync Run freezes start cursors/endpoints, discovers and classifies changes, executes Transfer Runs, records conflicts, verifies destination and advances cursors only after accepted state.

Rename/move may preserve Object identity. Tombstone propagation, Location deletion and shared Content-byte deletion remain separate.

Sync completion is bounded by included scope/frozen endpoints/cursors/time and never implies backup coverage.

## Conflict boundary

Conflict is first-class and retains every competing Revision/tombstone/alias/policy/base/clock/evidence.

Resolution is separate, named and policy-bound. Merge creates a new Revision with explicit parents/provenance. Choosing one side preserves competing history. Delete-modify, privacy/permission and identity ambiguity require stronger review unless a versioned policy has proven safe behavior.

## Backup boundary

Backup is separate from live sync, replica, Workspace checkpoint, export, source control and archive.

Backup Policy defines protected scope, strategy, encryption, repository, retention, verification and failure-domain requirements. Activation does not prove a Snapshot exists.

Backup Snapshot is immutable and records included, reused, excluded, missing, failed and unknown items plus parent/chunk dependencies, repository/provider, encryption, consistency and completeness.

Snapshot creation/provider acknowledgement does not prove readability.

Backup Verification domains remain separate: manifest, repository index, chunk digest, sampled/full read-back, decryption, metadata relationship, retention and independent copy. Verification is time-bounded; sampled is not full.

## Prune boundary

Prune Decision precedes deletion and requires dependency graph, retention, legal hold, protected restore points, copies/failure domains, repository health, authorization and dry-run impact. Unknown/failed required checks block or narrow prune. Deletion Receipts and post-prune verification are mandatory.

## Storage restore boundary

Backup Restore Decision is target-specific and expiring. Missing keys/dependencies/policy/capacity/provider compatibility block or narrow restore. Partial restorable scope requires explicit approval.

Backup Restore Run is a new Activity/Attempts and may create Transfer Runs, conflicts, Objects/Revisions and Locations.

`restored_storage` means selected bytes/metadata were restored and verified. It never means Workspace/runtime/application recovery; that requires WP05 Restore/Recovery Verification.

## Replica boundary

Replica Reconciliation compares expected versus observed Locations. Present-unverified is not verified. Repair is explicit Activity/Transfer plus Verification.

A current replica is not a backup without Backup Policy/Snapshot history. A backup copy is not a live replica without current Location registration/policy.

## Security and privacy

Credentials, keys and signed URLs are opaque references and redacted. Remote inputs require protocol/redirect/SSRF/path controls. Partial bytes remain isolated/non-executable. Cross-Workspace equality/deduplication follows WP03 privacy scope. Encryption/provider claims remain evidence until read-back/decryption verification.

## Schema and conformance decision

Accepted candidate package:

- 18 schemas in `schemas/phase-0b/transfer/schema-catalog.v0.1.0.json`;
- seven namespaced lifecycle machines;
- conventions and entity-kind supplement;
- migration/compatibility record;
- positive/negative fixture corpus;
- consolidated safety net.

Structural JSON Schema validation is insufficient. WP13 must enforce typed references, range arithmetic, digest domains, idempotency, generation/epoch, cursor freshness, revision/conflict graphs, retention/legal hold, locality, authority, privacy and proof.

## Consequences

### Positive

- byte movement cannot masquerade as accepted Content;
- resume/retry behavior is explicit and safe;
- conflicts and deletes are retained rather than overwritten;
- sync currency and backup recoverability remain honest;
- backup dependency/encryption/readability/prune evidence is explicit;
- storage restore cannot masquerade as application recovery;
- Provider replacement preserves canonical histories.

### Costs

- richer records than one transfer/sync/backup job table;
- full verification and safe pruning require extra read-back/storage;
- conflicts require policy/human review;
- legacy tool migrations frequently remain partial/manual-review.

## Rejected alternatives

- provider job ID as canonical Transfer identity;
- progress/provider acknowledgement as completion proof;
- last-write-wins conflict deletion;
- cursor advance before destination acceptance;
- sync or replica treated as backup;
- manifest/signature treated as readable backup;
- encrypted backup treated as restorable without key/decryption proof;
- age/dedup alone authorizing prune;
- storage restore treated as runtime/application recovery.

## Downstream requirements

WP07 and later packages must preserve:

- Transfer/Attempt/Verification separation;
- Content/Object/Location acceptance boundaries;
- Sync Relationship/Cursor/Run/Conflict separation;
- Backup Policy/Snapshot/Verification/Prune/Restore separation;
- storage restore versus WP05 runtime recovery;
- WP02 Receipt correlation;
- WP03 retention/deletion rules;
- WP04 Provider/generation/freshness;
- WP05 Workspace/checkpoint/export boundaries.

No transfer engine, sync service, backup repository, encryption backend, cloud provider, pruning or restore implementation is authorized by this ADR.

## Related records

- `work-packages/PHASE-0B-WP06-TRANSFER-SYNC-CONFLICT-BACKUP.md`
- `contracts/PHASE-0B-WP06-TRANSFER-SYNC-CONFLICT-BACKUP-CONVENTIONS.md`
- `contracts/PHASE-0B-WP06-ENTITY-KIND-SUPPLEMENT.md`
- `schemas/phase-0b/transfer/schema-catalog.v0.1.0.json`
- `migrations/phase-0b/WP06-TRANSFER-SYNC-CONFLICT-BACKUP-MIGRATION-COMPATIBILITY.md`
- `conformance/PHASE-0B-WP06-TRANSFER-SYNC-CONFLICT-BACKUP-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp06/transfer-sync-backup-cases.v0.1.0.json`
