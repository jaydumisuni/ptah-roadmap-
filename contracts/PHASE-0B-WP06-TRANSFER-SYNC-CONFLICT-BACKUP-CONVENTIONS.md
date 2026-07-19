# Phase 0B WP06 — Transfer, Synchronization, Conflict and Backup Conventions

**Status:** CANDIDATE DRAFT  
**Date:** 2026-07-19  
**Contract family target:** `ptah.transfer` / `ptah.sync` / `ptah.backup` `0.1.0`  
**Implementation authorization:** NONE

## Purpose

Define exact contracts for moving bytes, resuming interrupted transfers, reconciling revisions between locations/nodes/services, preserving conflicts, creating encrypted/versioned backups and proving storage-level restore without confusing any of those operations with Object acceptance, Workspace checkpointing, runtime recovery or export.

This package composes WP01 identity/versioning, WP02 Activity/Attempt/Receipt proof, WP03 Content/Object/Revision/Location, WP04 Node/Provider/capability and WP05 Workspace/checkpoint/recovery contracts.

---

# 1. Required separation

Ptah keeps the following distinct:

```text
Transfer Request
Transfer Run
Transfer Attempt
Transfer Manifest
Transfer Progress Snapshot
Transfer Verification

Sync Relationship
Sync Cursor
Sync Run
Conflict
Conflict Resolution

Backup Policy
Backup Snapshot
Backup Verification
Backup Prune Decision
Backup Restore Decision
Backup Restore Run

Replica Reconciliation

Content / Object / Object Revision / Storage Location
Activity / Operation / Attempt / Receipt
Workspace Checkpoint / Runtime Restore / Recovery Verification
Workspace Export / Import
```

No generic `transfer_status`, `sync_status`, `backup_status` or `success` field may collapse these truth classes.

---

# 2. Transfer identity and intent

## 2.1 Transfer Request

A Transfer Request states an intended byte movement or copy under exact authority and policy.

It binds:

- requestor and Workspace/organization scope;
- source Content/Object Revision/Location or remote source descriptor;
- destination Storage Location intent;
- transfer direction and mode;
- expected Content identity/digests/size where known;
- resumability/idempotency policy;
- network, credential and secure-grant references;
- privacy, audience, retention and legal/location policy;
- resource/time/cost budgets;
- required verification and acceptance behavior.

Request acceptance creates distinct Activity/Operation/Transfer Run records. The Request never mutates into the Run or final Object/Location.

## 2.2 Transfer Run

A Transfer Run is one logical transfer effect across one or more physical Attempts.

It binds:

```text
transfer_run_id
request_ref
activity_ref
operation_ref
source_descriptor
source_content_or_revision_ref
source_location_or_provider
expected_content_identity
destination_intent
transfer_mode
idempotency_key
attempt_refs
manifest/progress/verification refs
lifecycle
```

The Operation persists across retries. Every physical network/process try is a new WP02 Attempt with a new nonce and exact Node/Provider/workload generations/connection epoch.

## 2.3 Transfer modes

```text
upload
download
provider_to_provider
node_to_node
location_to_location
streaming_ingest
streaming_export
local_copy
replica_copy
```

Mode does not define proof or storage acceptance.

---

# 3. Source and destination truth

## 3.1 Source

A source may be:

- exact `object.content`;
- exact `object.revision` plus Content;
- verified `storage.location`;
- remote URL/API/object reference with captured metadata;
- stream whose Content identity is unknown until completion.

Mutable URLs, tags, cloud keys and provider IDs remain aliases/descriptors. If source bytes can change, Transfer Manifest retains validators such as ETag/version/last-modified only as observations—not canonical identity.

A resumed transfer must prove the source is still the same byte sequence under the resume protocol. Otherwise the old partial state is invalidated/quarantined and a new Run/Attempt begins.

## 3.2 Destination intent

Destination intent states provider/backend, namespace, storage class, encryption/retention policy and whether the operation is:

```text
create_new_location
replace_location_generation
repair_location
create_replica
stage_for_object_acceptance
export_only
```

A provider upload/object key is not a canonical Ptah Location until finalization registers it.

## 3.3 Acceptance boundary

Bytes received or provider acknowledgement do not create accepted Content/Object/Location truth.

Final acceptance requires the applicable sequence:

1. transport completed;
2. staged bytes closed/flushed;
3. full expected byte count or explicit unknown-size completion;
4. cryptographic Content digest computed/read back;
5. expected digest/size compared where declared;
6. destination provider read-back or equivalent verification;
7. immutable Content/Object Revision relationship established or imported under policy;
8. Storage Location registered with exact provider alias/version and verification state;
9. atomic promotion from partial/staging state;
10. Receipts retained.

Failure before atomic promotion leaves partial/quarantined state and cannot surface as accepted Object bytes.

---

# 4. Transfer manifest, partial state and resumption

## 4.1 Transfer Manifest

An immutable manifest records:

- source/destination descriptors and identities;
- expected/observed size and qualified digests;
- selected transport/provider/protocol revisions;
- chunk/range/checksum scheme;
- encryption/compression settings;
- idempotency key and correlation nonce;
- Attempt and Receipt references;
- policy, credentials/grants by opaque references;
- limitations.

## 4.2 Progress Snapshot

Transfer Progress is an immutable observation/projection, not durable operation truth.

It may contain:

- bytes/ranges/chunks completed;
- acknowledged versus locally buffered bytes;
- throughput/ETA observation;
- retry/backoff state;
- partial destination alias;
- source validator observation;
- latest Attempt/generation/epoch;
- freshness/valid-until.

Progress Events/telemetry may be sampled or lost. Final transfer truth comes from the Run, Attempts, Manifest, Verification, destination read-back and Receipts.

## 4.3 Resume token/state

Resume is valid only when all required dimensions match:

```text
transfer_run_id
source identity/validators
source expected size/digest where known
destination intent/partial alias
transport/provider protocol revision
chunk/range/checksum scheme
encryption/compression parameters
idempotency key
current authority and policy
```

A resume token is not canonical transfer identity and cannot outlive revocation, generation change, source drift, destination replacement or policy expiry.

## 4.4 Retry safety

- read-only/repeatable range fetches may retry within policy;
- destination writes use idempotency/conditional-create/offset proof where available;
- uncertain non-idempotent finalize/commit/delete operations do not retry automatically;
- provider acknowledgement without read-back may leave Operation `uncertain`;
- duplicate completion callbacks are deduplicated by Operation/Attempt/idempotency correlation while original evidence is retained.

---

# 5. Transfer verification

Transfer Verification is immutable evidence over one Run and destination.

Verification domains remain separate:

```text
transport_completed
byte_count_matched
transport_checksums_matched
content_digest_matched
destination_readback_matched
location_registered
object_acceptance_completed
external_delivery_confirmed
```

Transport checksum may detect chunk corruption but does not replace canonical Content digest. Provider `200 OK`, multipart completion or upload receipt does not automatically prove destination read-back or Object acceptance.

A Run may complete transport but fail Content verification. Such bytes remain quarantined/partial and are not promoted.

---

# 6. Synchronization model

## 6.1 Sync Relationship

A Sync Relationship is a durable policy/relationship between two or more versioned endpoints.

It records:

- endpoint identities and locality/provider;
- direction: one-way, bidirectional or publish/subscribe;
- included/excluded namespaces/Objects;
- revision and deletion semantics;
- cursor/vector/journal strategy;
- conflict policy;
- rename/move and metadata policy;
- permissions/credentials/network;
- offline and retry policy;
- retention/tombstone behavior;
- lifecycle and limitations.

A Sync Relationship is not a running Sync Run and does not imply endpoints are current/equal.

## 6.2 Sync Cursor

A Cursor is immutable endpoint-specific progress evidence under one relationship and protocol revision.

It may retain:

- journal/event sequence;
- vector clock/version vector;
- provider change token;
- last accepted Object Revision/location generation;
- endpoint/provider generation and epoch;
- observation time and expiry.

A cursor is not source truth. Lost/stale/incompatible cursor causes rescan/reconciliation; it never authorizes skipping unseen changes.

## 6.3 Sync Run

A Sync Run:

1. freezes start cursors/snapshots;
2. discovers changes;
3. resolves identities/renames/deletions;
4. creates Transfer Runs for byte movement;
5. creates new Object Revisions/Locations/relationships under policy;
6. records conflicts rather than overwriting;
7. verifies destination state;
8. advances cursors only after accepted results;
9. retains partial/failed items and limitations.

Sync Run success is scoped to its frozen endpoints/cursors and included namespace. It never proves global equality or backup recoverability.

## 6.4 Rename/move

A rename/move changes aliases/Locations or path relationships; it does not create a new Object when byte/logical identity is preserved. Competing rename/content changes can create a Conflict.

## 6.5 Deletion/tombstone propagation

Deletion has distinct records:

- source tombstone/revocation;
- sync propagation decision;
- destination tombstone;
- Location deletion;
- shared Content-byte physical deletion.

A delete marker never automatically authorizes physical byte deletion. Retention/legal hold/reference and verified-replica rules from WP03 remain mandatory.

---

# 7. Conflict model

A Conflict is a first-class immutable incident/root representing incompatible concurrent or uncertain changes.

Conflict kinds include:

```text
content_divergence
rename_divergence
delete_modify
metadata_divergence
permission_or_policy_divergence
identity_ambiguity
source_drift_during_transfer
cursor_gap
provider_generation_change
unsupported_semantic_merge
```

Conflict retains:

- relationship/run/endpoints;
- common ancestor/base where known;
- competing Object Revisions/aliases/tombstones/policies;
- clocks/cursors/evidence;
- detection protocol and time;
- affected audience/privacy;
- limitations.

## 7.1 Conflict Resolution

Resolution is a separate authorized decision and may:

```text
choose_revision
keep_both
create_merged_revision
apply_rename_mapping
apply_tombstone
ignore_for_scope
postpone
reject_automatic_resolution
```

Resolution never mutates frozen revisions. Merge creates a new Revision with explicit parents and provenance. Choosing one side does not delete the competing history.

Automatic resolution is allowed only under a versioned policy for conflict classes proven safe. Ambiguous identity, delete-modify, permission/privacy and non-mergeable binary conflicts require stronger review/manual authority.

---

# 8. Backup model

## 8.1 Backup versus other mechanisms

Backup is not:

- live synchronization;
- a replica alone;
- Workspace checkpoint;
- Workspace Export;
- source-control history;
- archive state;
- application/runtime recovery proof.

A backup preserves selected historical Content/Object/metadata under retention and encryption policy so storage-level restoration can be attempted and verified later.

## 8.2 Backup Policy

A versioned Policy defines:

- protected scopes/Objects/Locations/metadata;
- schedule/trigger and consistency target;
- inclusion/exclusion;
- full/incremental/deduplicated strategy;
- encryption/key reference;
- repository/provider requirements;
- retention, pruning and legal hold;
- geographic/audience/licence constraints;
- verification/scrub/restore-test frequency;
- failure/alert behavior;
- required independent copies/failure domains.

Policy activation does not prove any backup exists.

## 8.3 Backup Snapshot

A Backup Snapshot is an immutable manifest over protected source revisions and stored backup objects/chunks.

It records:

- Policy Revision;
- frozen source scope/cursors/time;
- included Object/Content/metadata references;
- excluded/failed/unknown items;
- full/incremental parent snapshot(s);
- repository/provider revision and location;
- encryption/compression/dedup configuration;
- manifest/chunk digests;
- consistency and completeness;
- Activity/Attempts/Receipts;
- limitations.

Snapshot creation proves only that the backup producer recorded/stored the declared data. Verification and restore proof remain separate.

## 8.4 Backup Verification

Verification may include:

```text
manifest_valid
repository_index_valid
chunk_digest_valid
sampled_readback
full_readback
decryption_test
metadata_relationship_validation
retention_policy_validation
independent_copy_present
```

Verification is time-bounded. A previously verified snapshot may later become stale/corrupt/missing.

## 8.5 Pruning

Prune Decision is separate from deletion execution.

It requires:

- retention/legal hold evaluation;
- dependency graph for incremental snapshots/chunks;
- minimum independent copies/failure domains;
- protected restore points;
- repository health/current verification;
- authorized scope;
- dry-run impact manifest;
- deletion Receipts and post-prune verification.

No snapshot/chunk is deleted merely because it is old or duplicated.

---

# 9. Backup restore

Backup Restore is storage-level recovery of selected Objects/metadata/Locations. It is not WP05 runtime/application recovery.

## 9.1 Restore Decision

Target-specific decision evaluates:

- Snapshot verification/freshness;
- requested scope and dependencies;
- destination capacity/provider compatibility;
- encryption key/credential availability;
- privacy/audience/location/licence policy;
- conflict/overwrite/fork behavior;
- expected Content/Object identities;
- conversion/migration needs.

Decisions:

```text
restorable
restorable_with_conversion
partially_restorable
not_restorable
unknown
```

## 9.2 Restore Run

A Restore Run is a new Activity/Operations/Attempts and may create Transfer Runs.

It retains per-item outcomes, created/repaired Locations, new Object/Revision records where required, conflicts, read-back verification and limitations.

`restored_storage` proves selected bytes/metadata were restored and verified. It does not prove a Workspace Materialization, Session, service or application recovered. Runtime recovery must use WP05 Restore/Recovery Verification and may consume restored Objects/Locations/checkpoints.

---

# 10. Replica reconciliation

Replica Reconciliation compares expected Content/Location relationships with current backend observations.

It may classify Locations:

```text
present_verified
present_unverified
stale
missing
corrupt
inaccessible
unknown
```

It may propose/carry out repair only through explicit Transfer/repair Activities and Receipts.

A healthy replica does not become backup unless it is retained/versioned under a Backup Policy. A backup copy does not become a live replica unless registered as a current Location under policy.

---

# 11. Credentials, network and security

- manifests contain opaque credential/grant references, never raw secrets;
- transfer/sync/backup credentials are scoped to exact Provider, endpoint, operation, object namespace and lifetime;
- remote URLs/content are untrusted inputs and require SSRF/path/redirect/protocol controls;
- partial files/archives are non-executable and isolated;
- archive/path extraction safety follows WP03 Domain rules;
- encryption keys are separate and rotation/revocation is explicit;
- logs/Events/Receipts redact tokens, signed URLs and sensitive paths;
- cross-Workspace deduplication/equality disclosure follows WP03 privacy scope;
- provider/server-side encryption claims remain evidence, not proof of readable recovery.

---

# 12. Provider/backend replacement

Replacing transfer/sync/backup machinery:

1. preserves Transfer/Sync/Backup canonical identities and source records;
2. creates/selects compatible Provider Revisions/Instances;
3. invalidates incompatible resume tokens/cursors;
4. advances/fences Provider/connection/workload generations;
5. re-verifies existing Locations/snapshots where semantics differ;
6. converts manifests/cursors only through explicit migration;
7. preserves old Attempts/Receipts/conflicts/verification history;
8. does not claim equivalent deduplication, encryption, consistency or restore behavior without conformance proof.

---

# 13. Migration rules

Migration must not:

- equate a download/upload record with accepted Object/Location;
- promote provider acknowledgement to Content verification;
- resume after source/destination/protocol drift;
- merge Transfer Run and physical Attempt;
- treat progress Event as durable completed range truth;
- equate Sync with Backup or Replica with Backup;
- silently resolve divergent revisions/deletes/permissions;
- advance cursor before accepted destination verification;
- delete source/destination bytes from a tombstone alone;
- claim backup complete with missing/failed/unknown required items;
- claim encrypted backup restorable without key/decryption evidence;
- treat backup verification as runtime recovery;
- prune without dependency/retention/legal-hold analysis;
- reactivate expired credentials;
- discard conflicts, partial outcomes, negative verification or failed restore evidence.

---

# 14. Required conformance cases

1. interrupted transfer resumes only when source/destination/protocol/idempotency dimensions match.
2. source drift invalidates partial state and prevents mixed bytes.
3. provider upload acknowledgement without full digest/read-back does not register verified Location.
4. transport completed but digest mismatch remains quarantined/failed.
5. duplicate callback/Attempt cannot double-finalize one logical transfer.
6. unknown-size stream becomes Content only after final digest/atomic acceptance.
7. stale Sync Cursor triggers rescan rather than skipped changes.
8. concurrent divergent edits create Conflict and retain both Revisions.
9. rename preserves Object identity; delete-modify conflict is not auto-overwritten.
10. cursor advances only after accepted destination state.
11. tombstone propagation does not physically delete shared Content bytes.
12. sync success does not claim backup coverage.
13. Backup Snapshot with missing required item is partial/failed.
14. verified manifest with missing/corrupt chunk fails later read-back honestly.
15. encrypted snapshot without usable key is not restorable.
16. prune dry-run preserves dependent incremental snapshots/chunks/legal holds.
17. storage restore creates verified Locations/Objects but does not claim runtime/application recovery.
18. provider/backend replacement preserves identities and invalidates incompatible cursors/resume tokens.
19. local and remote Providers use the same canonical records with truthful locality evidence.
20. one failed transfer/sync/backup does not block unrelated Workspace Activities.

---

# Do-not-break rule

> Never collapse byte movement, accepted Content, synchronization, conflict resolution, replica health, backup preservation, checkpoint capture, export packaging, storage restore or runtime recovery into one operation or one status. Provider acknowledgement, cursor advancement, snapshot creation and manifest verification are all weaker facts than verified destination bytes or successful application recovery.