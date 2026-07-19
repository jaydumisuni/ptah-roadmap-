# Phase 0B WP06 — Transfer, Sync, Conflict and Backup Migration Compatibility

**Status:** CANDIDATE  
**Contract catalogs:** common 0.1.0, activity 0.1.1, object 0.1.0, runtime 0.1.2, workspace 0.1.0, transfer 0.1.0  
**Date:** 2026-07-19

## Purpose

Define how legacy download/upload jobs, partial files, replication tools, sync folders, conflict copies, backup repositories and restore logs enter Ptah without fabricating Content acceptance, current synchronization, backup completeness, restoreability or runtime recovery.

## Non-negotiable preservation rules

1. Transfer Request, logical Run, physical Attempt, Manifest, Progress and Verification remain separate.
2. provider/task/download/upload IDs remain Aliases, not canonical IDs.
3. progress, provider acknowledgement and transport completion do not become Content/Object/Location acceptance.
4. source drift, destination drift, protocol change, policy expiry and generation change invalidate incompatible resume state.
5. Sync Relationship, Cursor, Run, Conflict and Resolution remain separate.
6. conflicts, divergent revisions, deletes, renames and policy disagreements are retained.
7. cursor advancement follows accepted destination verification only.
8. sync, replica, backup, checkpoint and export remain different mechanisms.
9. Backup Policy, Snapshot, Verification, Prune Decision and Restore remain separate.
10. storage-level restore does not become Workspace/application recovery.
11. retention/legal hold/dependency/copy rules precede deletion or pruning.
12. credentials/keys are re-authorized and never inferred from stored bytes.
13. negative, partial, stale, corrupt and failed evidence remains historical.

## Legacy transfer import

A legacy transfer record may produce:

- `transfer.request` if original intent/authority is known;
- one `transfer.run` for the logical effect;
- WP02 Attempts for physical retries;
- immutable Manifest and Progress observations;
- Verification only for checks actually performed;
- partial/quarantined Location aliases and evidence.

Legacy `completed` maps only to transport/provider completion unless full byte/digest/read-back/acceptance evidence is recovered. It cannot create verified Content/Location automatically.

Missing idempotency/generation/source validators become limitations and may force a new Run rather than resumed continuation.

## Partial/resume migration

A partial file, multipart upload or resume token is imported only with:

- source descriptor/validators;
- destination alias/intent;
- protocol/provider revision;
- range/chunk scheme;
- encryption/compression settings;
- observed ranges/checksums;
- current authority.

When those dimensions are incomplete or mismatched, retain the bytes as unverified/quarantined partial state and start a new transfer rather than appending blindly.

## Legacy sync import

A sync-folder/tool configuration becomes `sync.relationship` only when endpoints, direction, filters, cursor strategy, conflict/deletion/rename policy and authority can be identified.

Provider change tokens/device versions/file indexes become `sync.cursor` scoped to exact relationship/endpoint/protocol/provider generation.

A historical `in sync` flag becomes a bounded observation/Run result with time/scope/limitations—not relationship truth.

Conflict-copy filenames and last-write-wins overwrites are imported as conflict evidence where possible. Missing competing bytes/history are recorded as lost/unknown evidence; they are not reconstructed from current state.

## Revision and deletion migration

Legacy paths/renames map to aliases/Location relationships while stable Object identity is preserved when evidence supports it.

Delete markers/tombstones remain separate from Location deletion and Content-byte deletion. Unknown deletion propagation state requires reconciliation/manual review.

## Backup import

Legacy schedules/settings become `backup.policy` only with protected scope, repository, encryption, retention and verification behavior.

Legacy backup points become `backup.snapshot` only when manifest/scope/source time/provider/encryption/dependency information is available. Missing required items make completeness partial/unknown.

Repository snapshots without source scope or dependency graph may be imported reference-only and are not automatically prunable/restorable.

Hashes/signatures map to the exact verification domains they prove. Snapshot display name or timestamp is not canonical identity.

## Backup verification migration

Legacy `healthy`, `verified` or `OK` flags are split into available domains: manifest, index, chunk digest, sampled/full read-back, decryption, metadata relationship and copy/failure-domain checks.

Unknown tool/database/key/provider versions remain limitations. A prior successful verification is time-bounded and cannot prove current readability.

## Restore migration

Legacy restore logs become `backup.restore_run` only when Snapshot, target, decision, Activity/Attempts, outputs and verification can be correlated.

A copied file without Content digest/Location registration remains restored-unverified.

A successful storage restore never maps to WP05 `runtime.restore_run` or `recovered`. Runtime/application recovery requires separate WP05 records and postconditions.

## Prune migration

Legacy retention/prune logs become decisions only when dependency graph, legal hold, retention, protected restore points, copy/failure-domain and dry-run impact can be recovered.

Otherwise deletion events remain historical destructive evidence and the repository requires reconciliation before future prune.

## State migration

Legacy global statuses are split into:

- Transfer Request lifecycle;
- Transfer Run lifecycle;
- Sync Relationship lifecycle;
- Sync Run lifecycle;
- Conflict lifecycle;
- Backup Policy lifecycle;
- Backup Restore Run lifecycle;
- Progress/verification/cursor freshness;
- Snapshot completeness/consistency;
- Restoreability decision;
- replica observation.

Ambiguous values become partial/unknown/manual review. They are never guessed into verified, synchronized, complete, restorable or restored.

## Backend replacement

Replacing transfer/sync/backup machinery:

1. preserves canonical records and histories;
2. creates/selects new Provider revisions/instances;
3. advances/fences generations/epochs;
4. invalidates incompatible resume tokens/cursors;
5. migrates manifests/cursors only through explicit conversion;
6. re-verifies Locations/snapshots where semantics differ;
7. preserves old Attempts/Receipts/conflicts/verification;
8. does not claim equivalent encryption/dedup/consistency/restore behavior without conformance proof.

## Breaking changes

Require versioned migration when changing:

- transfer identity/idempotency/resume semantics;
- source/destination/digest/range meanings;
- cursor/conflict/deletion behavior;
- backup strategy/dependency/encryption/retention semantics;
- restore/prune authorization/proof;
- lifecycle transition authority.

## Negative migration cases

Reject or require manual review when migration attempts to:

- use provider transfer ID as canonical identity;
- promote progress/provider acknowledgement to verified Content/Location;
- resume after source/destination/protocol/policy drift;
- collapse retries into one Attempt;
- treat `in sync` as permanent relationship truth;
- silently discard conflicts/divergent revisions;
- advance cursor before verified destination state;
- treat sync/replica as backup;
- claim backup complete with unknown/missing required items;
- claim restorable without key/decryption/dependency evidence;
- prune without dependency/retention/legal-hold/copy checks;
- treat storage restore as application recovery;
- discard corrupt/failed/partial evidence.

WP13/WP14 must execute legacy-to-candidate fixtures, round trips, provider replacement and negative cases. Structural validation alone is insufficient.