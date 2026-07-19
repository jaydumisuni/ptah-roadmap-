# Phase 0B WP06 — Entity Kind Supplement

**Status:** CANDIDATE DRAFT  
**Parent registry:** `ptah.entity-kind` `0.1.0`  
**Date:** 2026-07-19

## New entity kinds

| Entity kind | Canonical role | Mutability rule |
|---|---|---|
| `transfer.request` | requested byte movement/copy intent | lifecycle projection; acceptance creates Activity/Run |
| `transfer.run` | one logical transfer effect across physical Attempts | lifecycle projection; history retained |
| `transfer.manifest` | immutable source/destination/protocol/chunk/digest/idempotency manifest | immutable |
| `transfer.progress_snapshot` | immutable progress/range/partial-state observation | immutable |
| `transfer.verification` | immutable transport/content/read-back/Location acceptance verification | immutable |
| `sync.relationship` | durable endpoint/direction/policy/conflict relationship | lifecycle projection; revisions/history retained |
| `sync.cursor` | immutable endpoint/protocol/journal/vector progress evidence | immutable |
| `sync.run` | one frozen-cursor reconciliation execution | immutable result/lifecycle projection root |
| `sync.conflict` | durable incompatible concurrent/uncertain change root | lifecycle projection; evidence retained |
| `sync.conflict_resolution` | immutable authorized resolution decision | immutable |
| `backup.policy` | versioned protected-scope/schedule/encryption/retention/verification policy | lifecycle projection; revisions/history retained |
| `backup.snapshot` | immutable backup manifest/restore point | immutable |
| `backup.verification` | immutable manifest/chunk/read-back/decryption/relationship verification | immutable |
| `backup.prune_decision` | immutable retention/dependency/legal-hold deletion decision | immutable |
| `backup.restore_decision` | immutable target-specific storage restore decision | immutable |
| `backup.restore_run` | one storage-level restore execution result root | immutable result/lifecycle projection root |
| `storage.replica_reconciliation` | immutable expected-versus-observed Location/replica reconciliation result | immutable |

## Existing kinds reused

- `core.activity`, `core.operation`, `core.attempt` — logical work and physical execution.
- `proof.receipt`, `proof.evidence`, `proof.review`, `proof.external_result` — evidence and authority.
- `object.content`, `object.object`, `object.revision`, `object.artifact` — source and destination identity.
- `storage.location`, `storage.location_observation`, `storage.verification`, `storage.repair`, `storage.deletion_decision` — WP03 physical storage records.
- `runtime.provider`, `runtime.provider_revision`, `runtime.provider_instance`, `runtime.dispatch_eligibility` — WP04 machinery and current eligibility.
- `core.workspace`, `core.workspace_revision`, `runtime.checkpoint_bundle`, `runtime.restore_run`, `runtime.recovery_verification`, `object.workspace_export` — WP05 records that must remain distinct from transfer/sync/backup.
- `event.cursor` — generic replay cursor where applicable; `sync.cursor` is the sync-protocol-specific progress record.

## Typed-reference rules

- `transfer_request_ref` requires `transfer.request`.
- `transfer_run_ref` requires `transfer.run`.
- `transfer_manifest_ref` requires `transfer.manifest`.
- `transfer_progress_snapshot_ref` requires `transfer.progress_snapshot`.
- `transfer_verification_ref` requires `transfer.verification`.
- `sync_relationship_ref` requires `sync.relationship`.
- `sync_cursor_ref` requires `sync.cursor`.
- `sync_run_ref` requires `sync.run`.
- `conflict_ref` requires `sync.conflict`.
- `conflict_resolution_ref` requires `sync.conflict_resolution`.
- `backup_policy_ref` requires `backup.policy`.
- `backup_snapshot_ref` requires `backup.snapshot`.
- `backup_verification_ref` requires `backup.verification`.
- `backup_restore_decision_ref` requires `backup.restore_decision`.
- `backup_restore_run_ref` requires `backup.restore_run`.

Cross-record kind, digest, range, cursor, revision graph, retention, expiry, locality, authority and proof constraints are enforced by the executable harness rather than JSON Schema alone.

## Identity prohibitions

The following cannot become canonical Transfer/Sync/Backup identities:

- URL, cloud object key, local path or temporary filename;
- upload/download ID, multipart ID, tus URL or aria2 GID;
- ETag, Last-Modified, provider object version or generation;
- process ID, connection/socket ID or progress Event sequence;
- resumable token;
- Syncthing device/file version or rclone/restic backend ID alone;
- backup repository path, snapshot display name or archive filename;
- checksum without algorithm/domain;
- provider acknowledgement/status string;
- cursor token without relationship/endpoint/protocol scope.

## Classification rules

1. Transfer Request, Run, physical Attempt, Manifest, Progress and Verification remain separate.
2. transport completion and Object/Location acceptance remain separate.
3. Sync Relationship, Cursor, Run, Conflict and Resolution remain separate.
4. Backup Policy, Snapshot, Verification, Prune Decision and Restore remain separate.
5. `backup.restore_run` is storage-level and never replaces WP05 `runtime.restore_run` or Recovery Verification.
6. replica health, sync currency and backup recoverability remain separate.
7. aliases/tokens/checksums remain scoped evidence.
8. registration does not authorize implementation or Provider selection.
