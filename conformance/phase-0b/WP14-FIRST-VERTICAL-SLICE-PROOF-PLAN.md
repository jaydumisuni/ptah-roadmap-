# WP14 first vertical-slice proof plan

Status: candidate freeze

The Phase 0C implementation decision may select backends, but it may not weaken these proofs.

## Required slice

- one Linux Node and exact Node generation;
- one persistent Workspace with detach/reconnect;
- Object registration and immutable Revision identity;
- at least ten concurrent Activities with independent cancellation/failure;
- multiple terminals and streamed output;
- upload plus resumable download with digest verification;
- Git clone or mirror as a receipted Activity;
- one isolated container path;
- one persistent Browser path;
- one decomposition adapter;
- Artifact registration and exact provenance;
- checkpoint, restart and verified recovery;
- one backend-replacement run preserving stable Ptah identity;
- one offline run with no network schema resolution.

## Mandatory negative proofs

The implementation must reject stale Provider generations, stale fences, reused Attempts, raw secrets, ACK-as-success, incomplete citations, expired Accepted Risk, same-environment reproduction, path traversal, partial transfer overclaim, stale semantic UI targets and recovery without new-generation verification.

## Acceptance

All required structural and semantic cases must pass at the exact implementation commit. Reports, Receipts, Artifacts, logs and limitations must be retained. A green CI summary without the immutable reports is insufficient.
