# ADR-0006 — Storage Classes, Object Transfer, Synchronization and Backup Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Phase:** 0A storage/transfer/synchronization closure

## Context

Ptah must move and preserve many kinds of data without turning every backend into one ambiguous filesystem.

The inspected sources solve different problems:

- Lumi DM provides a substantial multi-protocol product/engine prototype.
- aria2 provides mature segmented, multi-source and torrent/Metalink downloading.
- tus/tusd provides resumable upload protocol and backend abstractions.
- rclone provides cloud/provider movement, copy/check/sync/bisync and optional encryption/chunking.
- Syncthing provides direct Node-to-Node block replication, device identity and version-vector conflict detection.
- restic provides encrypted deduplicated backups, immutable snapshots, verification and restore.
- Hunter internal architecture separates tracked source, local runtime bytes, durable metadata and R2 attachment bytes.
- JuiceFS and SeaweedFS can provide shared distributed filesystems later, but are not required for Ptah v1.

The risks of collapsing these concerns are severe:

- sync deletion mistaken for backup retention;
- cloud mount treated like local build storage;
- transfer completion treated as Object verification;
- remote provider path/tag treated as immutable identity;
- folder replication used as conflict authority;
- cache used as source truth;
- backup snapshot used as a live Session;
- one vendor's IDs becoming Ptah identity.

## Decision

Ptah will own a backend-neutral **Storage Fabric** with explicit storage classes, content identities, revisions, locations, transfer Activities, synchronization records and backup records.

The following concepts remain separate:

1. hot active Workspace storage;
2. immutable Objects;
3. mutable Workspace revisions;
4. promoted Artifacts;
5. caches;
6. provider volumes/snapshots;
7. transfer landing/partial data;
8. synchronization replicas;
9. encrypted backups;
10. exports/recovery bundles.

No storage provider, transfer engine, sync engine or backup repository is canonical identity by itself.

---

# Storage classes

## 1. Hot Workspace storage

Used for:

- active source/worktrees;
- build outputs before promotion;
- package/tool caches;
- container layers and writable volumes;
- browser profiles;
- media intermediates;
- mounted filesystems;
- emulators/VM disks;
- active databases and services.

Rules:

- fast local SSD/NVMe is the default;
- provider volumes may implement this class;
- cloud/object mounts are convenience/adapters, not the default active Build/DB filesystem;
- mutable bytes are not durable Objects until checkpointed/registered;
- pressure, health and available capacity are reported by the Node/Provider;
- caches and temporary files are explicitly disposable.

## 2. Immutable Object storage

An Object is identified by content digest and type/version metadata, independent of filename or storage location.

Initial durable locations may include:

- local content-addressed storage;
- R2/S3-compatible Object Storage;
- OCI registry/layout through ORAS for suitable Artifacts;
- later replicated/self-hosted locations.

Each location has independent availability and verification state.

## 3. Mutable Workspace revisions

Mutable files/directories are represented through revisions/checkpoints, not by changing immutable Object identity.

A revision records:

```text
revision_id
workspace_id
base_revision_id
parent_revision_ids
writer_node_id
writer_activity_id
created_at
file_or_tree_object_id
tombstones
conflict_state
```

Concurrent edits from the same base create divergent revisions. They are preserved as conflicts until a caller/human/authorized merge operation resolves them.

## 4. Artifacts

Artifacts are promoted Objects with durable purpose, provenance, retention and verification relationships as defined by ADR-0005.

## 5. Cache

Cache is derived reusable state.

It may be deleted/rebuilt and cannot be the only copy of source, Object, Artifact, receipt or Session truth.

## 6. Provider volume/snapshot

A provider volume or VM/container snapshot is runtime storage state. It may be referenced by a Session/checkpoint but does not replace Ptah Object/revision records.

## 7. Landing/partial data

Incomplete upload/download bytes live in an explicit landing class with:

- transfer identity;
- current offset/chunks;
- source validators;
- expected size/digest;
- backend/session references;
- retention/cleanup state.

Partial data is not a completed Object.

## 8. Backup

Backups are encrypted recoverable copies/snapshots, initially with restic as the primary backend candidate.

They are separate from synchronization, live storage and provider snapshots.

## 9. Export/recovery bundle

Human-readable or portable exports may target Google Drive or another provider.

Exports contain manifests and selected source/Artifact/Session data. They are not active Workspace storage.

---

# Object identity and content addressing

## Digest identity

Ptah Object identity uses an algorithm-qualified digest:

```text
algorithm:digest
```

Phase 0B selects required algorithms and migration rules. SHA-256 is the initial interoperability baseline; faster local/chunk hashes may be added without changing the qualified identity model.

## Object record

At minimum:

```text
object_id
object_type
size
content_digests
created_at
source
producer_activity_id
parent_or_subject_ids
storage_locations
verification_state
retention_class
visibility
```

## Storage location record

```text
location_id
object_id
backend_type
connection_reference
provider_object_key_or_path
provider_version_or_etag
stored_size
stored_digest_claims
verified_at
health_state
replica_role
encryption_or_wrapper_reference
```

Provider paths, tags, ETags and repository IDs are location metadata, not Object identity.

## Health states

```text
pending
available
verified
degraded
missing
corrupt
repairing
retiring
deleted
```

Metadata must never claim durable availability until bytes are confirmed at the selected location.

---

# Transfer Activity boundary

Uploads, downloads, cloud copies and Node transfers are Ptah Activities with stable operation/attempt identities.

## Transfer states

```text
requested
staged
probing
awaiting_confirmation
queued
transferring
paused
resuming
verifying
finalizing
completed
verification_failed
finalization_failed
cancelled
failed
cleanup_pending
cleanup_failed
```

`completed` transport and `verified` Object readiness remain separate.

## Source identity and validators

A remote source may retain:

- URL/provider reference;
- mirror list;
- expected size;
- ETag/version/generation;
- Last-Modified;
- expected whole digest;
- chunk/piece hashes;
- authentication/credential reference;
- redirect/final source record.

Unsafe resume is rejected when the remote identity changed and the partial bytes cannot be proven compatible.

## Upload direction

- tus/tusd is the primary resumable-upload candidate.
- Ptah maps tus resource IDs to stable Activity/operation/Object landing records.
- Whole-object hash is computed during or immediately after intake.
- completion, hash verification, registration and post-upload decomposition are separate states.

## Download direction

- aria2 is the primary segmented/multi-source backend candidate.
- Lumi DM supplies internal product requirements and fallback/native-engine patterns.
- JSON-RPC/service control is preferred over parsing human console output.
- aria2 GID/session IDs remain adapter references.

## Cloud/provider transport

- rclone is the primary broad provider-transport candidate.
- immutable copy/check is preferred over blind directory sync.
- sync/bisync/delete operations require explicit plan, dry run where supported, conflict/delete list and caller approval when the caller demands it.

## Node-to-Node transport

- Syncthing may provide optional continuous folder/block replication.
- dedicated Ptah Object streams may transfer selected immutable Objects directly.
- transport does not own revision or conflict authority.

---

# Synchronization boundary

Synchronization is the reconciliation of replicas/revisions, not merely copying bytes.

## Immutable Objects

- identical content digests deduplicate safely;
- adding a new storage location creates a replica, not a conflict;
- missing/corrupt replicas can be repaired from verified copies;
- deletion follows retention/tombstone policy, not simple last-writer deletion.

## Mutable Workspace data

- every mutable update is based on a known revision;
- one online writer lease may reduce conflicts but does not erase offline divergence;
- independent changes from one base produce concurrent revisions;
- conflicts preserve both/all versions and their writers/Activities;
- merge/resolution creates a new revision with both parents;
- sync engines transport revisions and bytes; Ptah decides authority/conflict state;
- no silent last-write-wins default for important data.

## Version vectors

Syncthing's version-vector model is a strong donor for causal comparison. Phase 0B may adopt a compatible causal-clock representation, but Ptah revision IDs and conflict records remain canonical.

## Tombstones and deletion

Deletion creates a tombstone/revision. Retention and backup policies determine when physical bytes/replicas may be removed.

Synchronization deletion never automatically deletes backup history.

## Source Git synchronization

Git/source updates retain their own fast-forward/merge semantics. Git is not the generic sync engine for binary Objects or runtime state.

---

# Backup boundary

restic is the primary encrypted backup/restore backend candidate.

## Backup record

```text
backup_id
backup_recipe_id
source_revision_or_checkpoint
source_object_ids
source_paths
quiesce_or_provider_snapshot_reference
repository_connection_reference
encryption_key_reference
backend_snapshot_reference
created_at
verification_state
restore_test_state
retention_policy_reference
```

## Rules

- key/password material remains an opaque credential reference;
- backup completion and restore verification are separate;
- application-consistent backup requires quiesce/provider snapshot evidence;
- retention/forget/prune is explicit, planned and receipted;
- restore creates or targets an explicit revision/location and never silently overwrites current mutable state;
- at least one periodic full restore drill is part of proof;
- synchronization is not backup.

---

# Google Drive boundary

Google Drive is an export and readable recovery destination.

Suitable content:

- Session export bundles;
- documents/media selected by users;
- source/release bundles;
- readable reports/manifests;
- recovery copies.

Unsuitable live use:

- Git worktrees;
- build directories;
- container layers;
- databases;
- active browser profiles;
- VM/emulator disks;
- high-churn caches.

rclone or a provider-native adapter may implement Drive transport. Ptah owns the export/import manifest and verification.

---

# Metadata catalogue

## Local catalogue

SQLite is the initial local Node catalogue candidate because it is transactional, embedded and recoverable.

## Shared catalogue

A SQL backend such as PostgreSQL or deployment-specific D1 may implement shared metadata. Public schemas remain backend-neutral.

## Requirements

- migrations/versioning;
- atomic state changes;
- idempotency constraints;
- Activity/outbox attempts;
- Object/location/revision relationships;
- local Node journal and synchronization cursors;
- append-only receipt history;
- backup/export of metadata;
- rebuild/projection from retained canonical records where possible.

Direct JSON files may remain export/debug formats, not multi-Node authoritative state.

---

# Local content-addressed store

The first Node should use a simple local content-addressed Object store rather than a distributed filesystem.

Direction:

```text
objects/<algorithm>/<digest-prefix>/<digest>
```

with metadata in the catalogue and temporary/landing/cache directories stored separately.

Requirements:

- atomic finalize/rename;
- verified digest before promotion;
- deduplication by qualified digest;
- read-only immutable Object bytes;
- garbage collection only after reference/retention analysis;
- repair from another verified location;
- optional chunk index later;
- no user filename used as physical identity.

---

# Shared filesystem decision

JuiceFS and SeaweedFS are parked until Phase 12 Distributed Ptah.

They may be reopened when measured multi-Node shared-POSIX or storage-scale requirements exceed local storage plus Object transfer.

Ptah v1 does not depend on either.

---

# Security boundaries

## Paths

- all local targets resolve through approved Workspace/storage roots;
- no path traversal or arbitrary host-path access;
- filenames/metadata are sanitized separately from Object identity.

## Network intake

Online deployments require explicit SSRF/private-network/redirect/DNS-rebinding protections according to deployment/caller configuration.

These protections preserve host/world integrity; they are not Ptah making business decisions.

## Credentials

- provider, proxy, cookie, certificate, repository and encryption-key references are opaque;
- adapters receive only operation-scoped access;
- rclone RC/aria2 RPC/tusd endpoints are local/private/scoped, never directly exposed as the public API;
- raw secrets stay out of logs, telemetry, receipts, exports and roadmaps.

---

# Donor decisions

- **Lumi DM:** internal requirements and implementation source; product remains separate; durable Ptah core rebuilt.
- **aria2:** primary segmented/multi-source download backend through JSON-RPC; GPL packaging reviewed separately.
- **tus/tusd:** primary resumable-upload protocol/backend candidate.
- **rclone:** primary cloud/provider transport adapter.
- **Syncthing:** optional direct Node-sync backend and version-vector donor.
- **restic:** primary encrypted backup/restore backend candidate.
- **JuiceFS/SeaweedFS:** evaluated and parked until measured distributed-storage need.
- **local CAS + SQLite/shared SQL + S3-compatible storage:** initial Storage Fabric direction.

All remain behind Ptah-owned contracts and exit strategies.

---

# Consequences

## Positive

- Active work remains fast and local.
- Object identity survives movement among storage providers.
- Sync cannot silently erase conflicts or substitute for backup.
- Transfer completion cannot masquerade as verified Object readiness.
- Drive remains useful without becoming a broken live filesystem.
- Backends can be replaced without changing Objects, revisions or Sessions.
- The first vertical slice stays simpler than a distributed filesystem deployment.

## Costs

- Ptah must maintain Object, location, revision, conflict, transfer and backup schemas.
- Local CAS and metadata migrations require careful garbage collection and recovery.
- Several adapters and credential types are needed.
- Correct offline reconciliation is more complex than last-write-wins.
- Backup/restore drills consume time and storage.
- Some provider hashes/metadata need normalization and independent verification.

## Do-not-break rule

> Never treat transfer, synchronization, cloud mount, provider path, backup snapshot, mutable tag, cache or export as universal Ptah truth. Immutable Object identity, mutable revisions, storage locations, backups and live Workspace state have different guarantees and must remain explicit.

---

# Required proof before freeze

1. Upload a large Object through tus, interrupt/restart and finalize with verified digest.
2. Download one Object through aria2 from multiple sources, resume safely and reject changed remote identity.
3. Store the same Object locally, in R2/S3, Drive export and OCI without identity change.
4. Delete one replica and repair it from another verified location.
5. Create concurrent offline revisions and preserve an explicit conflict; merge into a new two-parent revision.
6. Prove Syncthing/rclone transport does not make conflict decisions or delete backup history.
7. Back up an application-consistent checkpoint with restic, delete local data and perform verified restore.
8. Run an explicit retention/prune plan and retain deletion receipts.
9. Lose/rebuild the local metadata projection from backup/canonical records where supported.
10. Fail one cloud provider while local work and other storage locations remain operational.
11. Prove cloud/Drive mounts are not used for active Build/database/container state.
12. Replace one transfer/storage backend without changing Object, revision, Activity or Session identities.
