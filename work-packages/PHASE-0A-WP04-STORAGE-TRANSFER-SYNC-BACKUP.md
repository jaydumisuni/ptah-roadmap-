# Phase 0A — WP04 Storage, Transfer, Synchronization and Backup Composition

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Runtime code:** NOT STARTED

## Purpose

Close Ptah's active-storage, immutable-Object, transfer, cloud/provider movement, direct Node replication, backup, export and mutable-revision/conflict requirements without collapsing them into one filesystem or vendor.

## Sources inspected and saved

### Internal

- Lumi Download Manager
- Hunter storage authority, source/local sync, D1 outbox and R2 lifecycle
- Software Builder shared-cache/clean-Project rules

### External/upstream

- aria2
- tus/tusd
- rclone
- Syncthing
- restic
- JuiceFS
- SeaweedFS
- OCI/ORAS storage relationships from WP03

Saved records:

- `internal/LUMI-DM.md`
- `internal/STORAGE-AUTHORITY.md`
- `internal/HUNTER-RUNTIME-SYNC.md`
- `internal/SOFTWARE-BUILDER.md`
- `donors/ARIA2.md`
- `donors/TUSD.md`
- `donors/RCLONE.md`
- `donors/SYNCTHING.md`
- `donors/RESTIC.md`
- `donors/FUTURE-SHARED-FILESYSTEMS.md`

## Composite result

```text
Hot Workspace Storage
  local SSD/NVMe and provider volumes for active mutable work

Ptah Local Content-Addressed Store
  immutable verified Objects on each Node

Ptah Metadata Catalogue
  SQLite local + backend-neutral shared SQL

R2/S3-Compatible Object Storage
  durable remote Object/Artifact locations

Lumi + aria2
  product requirements and segmented/multi-source download backend

tus/tusd
  resumable upload protocol and landing storage

rclone
  cloud/Object provider transport, Drive and R2 movement

Syncthing
  optional direct Node folder/block replication and version-vector donor

restic
  encrypted deduplicated backup, retention and restore

ORAS/OCI
  suitable Artifact distribution and subject/referrer relationships

Google Drive
  readable export/recovery destination

JuiceFS/SeaweedFS
  parked distributed/shared-filesystem candidates for Phase 12
```

## Accepted architecture

Saved as `decisions/ADR-0006-STORAGE-TRANSFER-SYNC-BOUNDARY.md`.

Key decisions:

1. Hot Workspace bytes, immutable Objects, mutable revisions, Artifacts, caches, provider volumes, partial landing data, sync replicas, backups and exports are separate storage classes.
2. Active builds, databases, container layers, browser profiles and VM/emulator disks default to local fast storage.
3. Object identity is algorithm-qualified content digest plus type/version metadata, independent of path, tag or provider location.
4. Storage locations have independent availability, verification and health state.
5. Mutable Workspace data uses revisions; concurrent offline edits create preserved conflicts rather than silent last-write-wins.
6. Transfer completion and Object verification/finalization are separate states.
7. aria2 is the primary segmented/multi-source download backend candidate; Lumi remains the internal product/reference.
8. tus/tusd is the primary resumable-upload candidate.
9. rclone is the primary broad cloud/provider transport candidate.
10. Syncthing is an optional direct Node-sync backend; Ptah retains revision/conflict authority.
11. restic is the primary encrypted backup/restore candidate.
12. Synchronization is not backup. Provider snapshots are not backups. Cloud mounts are not active Build filesystems.
13. Google Drive is export/recovery, not live Workspace truth.
14. Local CAS + SQLite/shared SQL + R2/S3 is the initial Storage Fabric direction.
15. JuiceFS and SeaweedFS are evaluated and deliberately parked until measured multi-Node shared-POSIX need.

## Requirement closure verdict

Closed for Phase 0B contract design:

- `STORE-001` Hot local Workspace storage classes
- `STORE-002` Durable Object/Artifact storage abstraction
- `STORE-003` Metadata catalogue direction
- `STORE-004` content hashing, deduplication and location verification
- `STORE-005` Drive export/recovery boundary
- `XFER-001` resumable upload
- `XFER-002` fast resumable/multi-source download
- `XFER-003` cloud and Node transport
- `SYNC-001` mutable revision/conflict model
- remaining storage/sync portions of `SESSION-001`
- storage/transfer portions of `OFFLINE-001`
- storage-location portions of `CORE-003`

Still dependent on later groups:

- full Object relationship/decomposition model;
- filesystem/domain-pack handling;
- browser intake and download interception;
- device/platform-specific storage;
- distributed scheduler/network identity;
- actual multi-Node shared filesystem, currently parked.

## Phase 0B contracts required

1. Storage class and backend capability schema.
2. Object identity, qualified digest and type/version schema.
3. Storage location and health/verification schema.
4. Mutable revision, parent, tombstone and conflict schema.
5. Transfer request, source validator, mirror and state schema.
6. Partial/landing Object and chunk/resume metadata.
7. Upload/tus resource adapter record.
8. aria2/rclone/Syncthing backend reference and attempt record.
9. Synchronization scope, authority, revision and resolution contract.
10. Backup Recipe, repository/key reference and restore-proof schema.
11. Drive/export bundle manifest.
12. Local CAS layout, atomic finalization and garbage-collection rules.
13. Local SQLite/shared SQL catalogue and migration rules.
14. Credential/proxy/certificate/cookie references.
15. SSRF/path/root and operation-scope rules.
16. Storage health, replication and repair Activities.
17. Shared-filesystem reopening criteria.

## Validation set

- interrupted/restarted tus upload;
- aria2 multi-source resume and changed-source rejection;
- one Object stored locally, in R2/S3, Drive export and OCI with stable identity;
- missing/corrupt replica repair;
- concurrent offline revisions and explicit merge conflict;
- transport engines cannot decide conflict or delete backup history;
- restic application-consistent backup and full restore drill;
- reviewed retention/prune plan;
- local catalogue loss/recovery;
- cloud provider outage while local work continues;
- backend replacement without identity changes;
- no cloud/Drive mount used as active Build/DB/container storage.

## Next Phase 0A group

Proceed with the **universal Object and decomposition cluster**:

- internal App Recover;
- internal APK Extractor;
- internal Creative Studio/media asset handling;
- internal Document Generator/rendering;
- libarchive;
- Apache Tika;
- Unstructured;
- LIEF;
- Binwalk;
- JADX;
- Apktool;
- libvips;
- FFmpeg/ffprobe;
- optional Tree-sitter/source-code structure donors where required.

This group must close progressive detection, recursive Object graphs, derivatives, views and domain-pack boundaries before firmware-specific work begins.
