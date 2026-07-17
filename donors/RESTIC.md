# Donor Record — restic

**Phase:** 0A / WP04  
**Status:** FIRST-PASS COMPLETE — ENCRYPTED BACKUP AND RESTORE DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/restic/restic
- Default branch: `master`
- Pinned commit: `d4088aa09ba78d3c93d81505bfab9cacf13f5168`
- Licence: BSD-2-Clause
- Activity: Active
- Classification: Encrypted, deduplicated snapshot backup, repository verification and restore donor
- Ptah targets: recoverable backups, encrypted repositories, content deduplication, snapshots, retention, repository checking, restore and backend portability

## Files/components inspected

- `README.md`
- `doc/design.rst`
- snapshot/repository/check/forget/prune source locations
- scripting/JSON status source locations
- supported backend and rclone-backend relationships

## Verified capabilities and patterns

- Runs on Linux, macOS, Windows and BSD variants.
- Creates encrypted backup repositories on local, SFTP, REST, S3-compatible and several cloud backends, with further providers through rclone.
- Backups create snapshots that represent file/directory content and metadata at a point in time.
- Restore and FUSE browse/mount operations are supported.
- Repository data is designed for confidentiality and integrity even when the storage backend is untrusted.
- Backup data is deduplicated so additional snapshots store only new content.
- Restore is treated as more important than merely producing backups, and repository/data verification is supported.
- Repository storage IDs are SHA-256 hashes of stored content.
- Stored repository files are immutable after write; writes should be atomic and multiple clients may access/write concurrently.
- Data and tree blobs are independently encrypted/authenticated and packed for efficient storage/indexing.
- Repository config has versioning and a unique repository ID independent of storage backend location.
- Index files can reconstruct local indexes if local cache is lost.
- Snapshot, index, key, lock and data structures are distinct.
- Only prune removes otherwise immutable repository data.
- Restic releases are themselves reproducibly built.

## What restic completes

- A dedicated backup/restore system rather than confusing synchronization with backup.
- Encrypted and authenticated storage on untrusted backends.
- Incremental content deduplication and immutable snapshots.
- Repository checking and restore verification.
- Backend independence, including S3-compatible and rclone-backed repositories.
- A content-addressed repository design with atomic immutable records.
- Snapshot browsing and selective restore.

## Important limitations for Ptah

- restic snapshots are backup objects, not live Ptah Workspaces, Sessions or provider snapshots.
- Repository passwords/keys are critical: losing them permanently loses access.
- Restic does not merge mutable online/local state or resolve conflicts.
- Backup success does not prove a running application/database was quiesced consistently.
- FUSE browsing/mounting is for restore/access, not the active build/database/container filesystem.
- Retention/forget/prune can permanently remove historical data and must be explicit, reviewed and evidenced.
- Repository locks and multi-client operation do not replace Ptah Activity/lease/fencing semantics.
- Restic storage IDs identify encrypted repository objects, not necessarily the same identity as plaintext Ptah Objects.
- Restore must map content into a selected destination without overwriting current Workspace state silently.
- Backup metadata may contain paths/hostnames/tags requiring privacy classification.
- rclone backend chaining adds another credential/configuration dependency.
- A snapshot may include inconsistent files if applications are writing during backup.

## Must not be inherited

- restic repository/snapshot IDs used as canonical Ptah Object or Session identity.
- Backup mounted as live Workspace storage.
- Synchronization or provider snapshots treated as equivalent to encrypted backup.
- Password/key material stored in roadmap, public config, logs or ordinary Session exports.
- Automatic forget/prune without retained plan, policy reference and receipt.
- Backup completion interpreted as verified restore.
- Restore overwriting current data without a new revision/checkpoint and explicit target.
- Application-consistency claims without quiesce/snapshot proof.

## Integration decision

**WRAP RESTIC AS THE PRIMARY ENCRYPTED BACKUP/RESTORE BACKEND CANDIDATE.**

Ptah owns backup policy references, Activity identity, source revision/checkpoint, repository connection/key references, snapshot relationship, retention receipts and restore verification.

Restic is suitable for:

- Node/Workspace backup sets;
- selected Object/Artifact and configuration backup;
- encrypted off-machine backups to R2/S3/SFTP/local/other providers;
- recovery of local catalogue/export bundles;
- periodic full restore drills.

It is not the primary Object store or synchronization engine.

## Native Ptah gap

Ptah must define:

- Backup Recipe and source selection by Object/revision/path;
- quiesce/provider snapshot/checkpoint references;
- repository connection and encryption-key references;
- restic snapshot mapping to Ptah backup Artifact/Session relationships;
- tags/retention policy and explicit prune plan;
- Activity/operation/attempt receipts;
- backup verification and restore-drill results;
- alternate destination/merge-safe restore behavior;
- privacy classification of paths/host metadata;
- backend health and redundant-copy strategy;
- distinction between bytes backed up and logical Session recoverability.

## Exit strategy

Ptah backup records remain backend-neutral. Another content-addressed encrypted backup system can replace restic while Ptah retains source revision, backup Artifact, retention and restore-proof records.

## Validation required

1. Back up one Workspace/Object set twice and prove deduplication of unchanged content.
2. Store the repository on S3-compatible/R2 and restore after deleting the local source.
3. Run repository check and a full restore drill; retain separate backup and restore-verification receipts.
4. Lose local index/cache and reconstruct from repository data.
5. Quiesce a database/service or use a provider snapshot, then prove application-consistent restore.
6. Reject restore into an existing mutable Workspace without an explicit new revision/target.
7. Simulate lost/incorrect key and prove Ptah reports unrecoverable-key state honestly without leaking the key.
8. Generate a retention/prune plan, review it, execute and retain removed-snapshot/content evidence.
9. Replace the storage backend or restore through another Node without changing Ptah backup identity.
10. Prove synchronization deletion does not remove restic history until retention policy explicitly permits it.
