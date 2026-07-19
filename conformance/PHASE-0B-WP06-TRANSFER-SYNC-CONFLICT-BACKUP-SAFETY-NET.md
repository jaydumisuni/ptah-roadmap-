# Phase 0B WP06 — Transfer, Sync, Conflict and Backup Safety Net

**Status:** CANDIDATE SPECIFICATION  
**Date:** 2026-07-19  
**Executable harness:** DEFERRED TO WP13  
**Fixture suite:** `conformance/fixtures/phase-0b/wp06/transfer-sync-backup-cases.v0.1.0.json`

## Purpose

Define structural, cross-record, temporal, generation, digest, range, cursor, conflict, retention, privacy and proof invariants that every WP06 implementation/migration must satisfy.

## A. Transfer identity and retries

1. Transfer Request, Run, Operation and physical Attempts remain distinct.
2. provider/job/multipart/resume IDs are scoped aliases only.
3. one logical Run preserves idempotency key while every physical Attempt gets new ID/nonce/generation/epoch.
4. duplicate callbacks cannot double-finalize a Run or create duplicate accepted Locations.
5. non-idempotent uncertain finalize/commit/delete cannot auto-retry.
6. stale Provider/connection/workload generation evidence cannot prove current transfer.

## B. Source/destination and resume

1. source descriptor resolves exact Content/Revision/Location or mutable remote/stream evidence.
2. resume requires matching source validators/identity, destination intent/alias, protocol, chunk/range/checksum, encryption/compression, idempotency and current authority.
3. source drift invalidates old partial state and prevents mixed bytes.
4. destination replacement/generation change invalidates incompatible partial state.
5. unknown-size stream is accepted only after finalization, digest and atomic registration.
6. partial bytes are isolated/non-executable and never surfaced as final Object bytes.

## C. Progress and acceptance

1. Progress Snapshot/Event is observation, not durable completion.
2. `bytes_received_unverified`, provider-acknowledged and `bytes_verified` remain distinct and arithmetically valid.
3. transport checksum is not canonical Content digest unless explicitly same algorithm/domain over exact canonical bytes.
4. provider success/HTTP success/multipart completion does not prove destination read-back.
5. verified Location/Object acceptance requires applicable byte count, Content digest, read-back, atomic promotion and Receipts.
6. digest mismatch/corruption leaves quarantined/partial state and no verified Location.
7. acceptance references require matching Transfer Verification domains.

## D. Sync relationships/cursors/runs

1. Sync Relationship is policy, not current equality.
2. Cursor is scoped to exact relationship/endpoint/protocol/provider generation and expires.
3. stale/lost/incompatible cursor triggers rescan/reconciliation, never skipped changes.
4. Run freezes start cursors and endpoint snapshots.
5. cursor advances only after accepted destination verification for represented scope.
6. partial/failure/conflict cannot advance cursor past unaccepted changes unless protocol explicitly records per-item safe cursor semantics.
7. sync completion is bounded by included scopes/frozen endpoints/cursors/time.
8. sync success never implies backup coverage/recoverability.

## E. Identity, rename and delete

1. rename/move changes aliases/Locations/relationships, not Object identity when logical identity is preserved.
2. concurrent rename/content changes may create Conflict.
3. delete/tombstone propagation, Location deletion and Content-byte deletion remain separate.
4. tombstone cannot bypass retention/legal hold/reference/verified-replica requirements.
5. unknown identity mapping becomes Conflict/manual review rather than merge.

## F. Conflict and resolution

1. every conflict retains competing revisions/tombstones/aliases/policies and base/clock evidence.
2. last-write-wins is not default authority.
3. resolution is separate, named and policy-bound.
4. merge creates a new Revision with explicit parents/provenance.
5. choosing one side preserves competing history.
6. delete-modify, privacy/permission and identity ambiguity require stronger authority/manual review unless policy is explicitly proven.
7. resolved conflict requires follow-up destination verification.

## G. Backup policy/snapshot

1. active Policy does not prove any Snapshot exists.
2. Snapshot freezes source scope/time/cursors and records every included/excluded/failed/unknown required item.
3. required missing/failed/unknown item prevents complete-for-declared-scope.
4. incremental/deduplicated Snapshot retains parent/chunk dependency graph.
5. manifest creation/provider acknowledgement does not prove stored chunks readable.
6. backup, sync, replica, checkpoint and export remain distinct.
7. encryption key is separate and policy-bound.
8. sensitive/prohibited items are omitted/encrypted/restricted with declared recovery impact.

## H. Backup verification

1. verification domains remain separate: manifest, index, chunk digest, sampled/full read-back, decryption, metadata, retention and independent copy.
2. verification is time-bounded; stale verification cannot prove current readability.
3. sampled read-back never becomes full read-back.
4. manifest/hash signature proves integrity/identity only under its trust chain.
5. missing/revoked key makes encrypted Snapshot not restorable even when ciphertext digests pass.
6. copy/failure-domain claims require distinct observed locations/domains, not aliases of one backend.

## I. Prune

1. Prune Decision precedes deletion Activity.
2. dependency graph, retention, legal hold, protected points, copy/failure-domain, repository health and dry-run impact must be evaluated.
3. unknown/failed required check blocks or narrows prune.
4. incremental parent/chunk dependency cannot be removed while retained restore points depend on it.
5. deletion Receipts and post-prune verification are mandatory.
6. age or duplicate digest alone never authorizes prune.

## J. Backup restore

1. Restore Decision is target-specific and expiring.
2. missing key/dependency/policy/capacity/provider compatibility blocks or narrows restore.
3. partial restorable scope requires explicit approval.
4. Restore Run uses new Activity/Attempts and may create Transfer Runs.
5. restored-unverified bytes do not become verified Location.
6. storage restore may create/repair Content/Object/Location but cannot claim Workspace/runtime/application recovery.
7. runtime recovery consumes restored state only through WP05 Restore/Recovery Verification.
8. conflicts/overwrite/fork behavior is explicit before mutation.

## K. Replica reconciliation

1. expected and observed Locations remain distinct.
2. present-unverified is not healthy/verified.
3. repair is explicit Activity/Transfer with verification.
4. replica does not become backup without Backup Policy/Snapshot history.
5. backup copy does not become live replica without Location registration/current policy.

## L. Security and privacy

1. credentials/keys/signed URLs are opaque refs and redacted from Events/logs/Receipts.
2. remote source protocols enforce scheme/redirect/SSRF/path controls.
3. cross-Workspace dedup/equality disclosure follows WP03 privacy scope.
4. encryption/provider claims remain evidence until read-back/decryption verification.
5. export/backup audience/location/licence rules apply before transfer.

## M. Provider replacement

1. canonical identities/history remain stable across provider replacement.
2. generation/epoch changes fence old evidence.
3. incompatible resume tokens/cursors are invalidated.
4. manifest/cursor conversion is explicit and non-lossless limitations retained.
5. changed encryption/dedup/consistency semantics require re-verification.
6. old Attempts/Receipts/conflicts/verifications remain historical.

## N. Property-based invariants for WP13

- verified bytes <= received bytes <= expected bytes when size known;
- verified ranges do not overlap inconsistently and remain within expected size;
- completed Transfer Run implies all required verification domains passed;
- accepted Location/Content references match verified digest/size;
- cursor valid_until > observed_at and endpoint/provider generation matches Run;
- Conflict resolution merge has at least two parents;
- complete Backup Snapshot has no required failed/missing/unknown entry;
- prune-approved set excludes every retained dependency/legal hold/protected point;
- restored_storage requires required item results restored_verified;
- no storage restore record implies WP05 recovered outcome.

## Exit condition

WP06 is candidate-complete only when:

1. all 18 schemas resolve through one catalog;
2. seven lifecycles use registered proof/state vocabulary;
3. fixtures cover every mandatory case;
4. migration preserves identity/history/conflicts/privacy;
5. work package and ADR reference this safety net;
6. implementation/provider selection remains blocked until Phase 0C.