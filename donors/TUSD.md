# Donor Record — tusd / tus Protocol

**Phase:** 0A / WP04  
**Status:** FIRST-PASS COMPLETE — RESUMABLE UPLOAD PROTOCOL DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/tus/tusd
- Default branch: `main`
- Pinned commit: `ad7fb31344e0629cb8a5af67bb1e630f90507890`
- Protocol version: tus 1.0.0
- Repository branch: tusd v2
- Licence: MIT
- Activity: Active reference implementation
- Classification: Standard resumable upload protocol and server/storage abstraction donor
- Ptah targets: interruption-safe uploads, offsets, partial concatenation, deferred size, termination, locking and local/S3-compatible landing

## Files/components inspected

- `README.md`
- `pkg/handler/datastore.go`
- DataStore, Upload, Locker, termination, concatenation, deferred-length and content-serving interfaces

## Verified capabilities and patterns

- tus is an HTTP protocol for upload pause/resume without retransmitting completed bytes.
- tusd is the official reference implementation.
- Arbitrary-size uploads can land on local disk, Google Cloud Storage, AWS S3 or compatible backends.
- Upload resources retain ID, total size, deferred-size state, current offset, metadata, partial/final status, constituent partial uploads and backend storage metadata.
- `WriteChunk` receives an explicit offset; the handler validates offset and size boundaries.
- Upload resources can expose readers before completion when the backend supports it.
- Finish hooks allow a store to complete provider-specific cleanup/finalization.
- Termination can make a resource non-resumable and remove it.
- Concatenation allows ordered partial uploads to form a final upload.
- Deferred-length uploads support sources whose final size is not initially known.
- Pluggable locks protect offsets/chunk order across multiple processes and can use disk, memory or external coordination.
- Storage implementations are modular and can delegate conditional/range content serving.
- Pre-create hooks can control upload IDs and sanitize/replace metadata.

## What tusd completes

- A standard client/server resume contract rather than a custom upload endpoint.
- Correct offset-based continuation and concurrency locking.
- Backend-neutral upload storage interfaces.
- Partial upload/parallel concatenation support.
- Deferred-size and termination semantics.
- A clean hook point to assign Ptah IDs and sanitized metadata before bytes arrive.
- Direct S3-compatible storage paths useful for R2-backed online intake.

## Important limitations for Ptah

- Upload resource IDs/offset state are tus implementation state, not Ptah Object/Activity identity.
- tus guarantees byte continuation, not expected content identity or malware/safety/format validation.
- User-supplied metadata must be filtered; it may contain untrusted filenames or sensitive values.
- S3 multipart/partial storage and final Object registration need transactional coordination with Ptah metadata.
- Concatenating completed partial uploads does not automatically verify the final content digest.
- Backend locks/offsets do not replace the Ptah Activity Ledger or Node journal.
- tusd does not provide download, sync, backup or conflict semantics.
- Upload endpoints require authentication, authorization, rate/size limits and deployment-specific network policy.
- An upload may complete at the protocol layer while Object hashing, scanning, decomposition or storage finalization later fails.
- Cleanup/termination behavior differs by DataStore and requires explicit receipts.

## Must not be inherited

- tus upload ID as canonical Ptah Object identity.
- Raw client metadata stored without filtering and normalization.
- Upload-complete event promoted to verified Object-ready state.
- Public unauthenticated unlimited upload endpoints.
- Offset/lock state treated as durable multi-Node Activity truth.
- S3/backend storage metadata exposed as public Ptah contracts.
- Partial uploads retained forever without lifecycle/cleanup states.

## Integration decision

**ADOPT TUS PROTOCOL COMPATIBILITY AND WRAP/EMBED TUSD AS THE PRIMARY RESUMABLE-UPLOAD CANDIDATE.**

Ptah should assign or map stable Object/Activity/operation IDs through hooks, stream hash the incoming bytes, retain a landing Object state and promote to durable Object only after finalization/verification.

Potential deployment paths:

- direct tusd service to local landing storage;
- tusd S3-compatible store for R2/S3;
- Ptah-native tus-compatible handler backed by its storage abstraction later.

## Native Ptah gap

Ptah must define:

- Upload Activity and operation/attempt IDs;
- tus resource mapping and idempotent create behavior;
- caller/Workspace/storage-class/target references;
- sanitized filename and metadata schema;
- streaming whole-object and optional chunk hashes;
- expected digest/size and final verification;
- landing, finalizing, verified, failed and cleanup states;
- Object catalogue transaction linking bytes and metadata;
- backend/lock/lease identity and stale recovery;
- authentication, quotas and explicit deployment network restrictions;
- post-upload decomposition/scan Activities;
- partial-upload retention and garbage collection;
- independent backend exit/migration path.

## Exit strategy

Ptah's Upload contract remains protocol-neutral and may be exposed through tus, multipart, signed direct-object-store upload or Node-to-Node streams. tus IDs and storage metadata remain adapter references.

## Validation required

1. Interrupt and resume an upload after client, server and network failure.
2. Reject a PATCH with an incorrect offset without corrupting stored bytes.
3. Run concurrent writers and prove locking preserves correct offset/order.
4. Assemble ordered partial uploads and independently verify the final digest.
5. Upload with unknown size and declare the final length safely.
6. Stream bytes directly to an S3-compatible backend and recover after restart.
7. Sanitize hostile metadata/filenames and reject path/control-data abuse.
8. Complete tus transport while deliberately failing final hash/registration; preserve honest `finalization_failed` state.
9. Terminate and clean a partial upload with durable cleanup receipts.
10. Switch storage backend without changing Ptah Object/Activity identity.
