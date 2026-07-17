# Donor Record — rclone

**Phase:** 0A / WP04  
**Status:** FIRST-PASS COMPLETE — CLOUD/OBJECT TRANSPORT DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/rclone/rclone
- Default branch: `master`
- Pinned commit: `fb25801f3548478dd4e8ff9e86ed430c6fdada5a`
- Licence: MIT
- Activity: Active
- Classification: Multi-provider file/object transport, sync, mount and cloud-adapter donor
- Ptah targets: Cloudflare R2/S3, Google Drive, local/SFTP/SMB/WebDAV and other storage movement, integrity checking, encryption/chunking wrappers and backend-neutral transport

## Files/components inspected

- `README.md`
- `COPYING`
- `docs/content/rc.md`
- `fs/rc/jobs/job.go`
- provider and virtual-backend catalogue
- copy/sync/bisync/check/mount/chunker/crypt/hasher behavior documented by the project

## Verified capabilities and patterns

- Supports a very large provider set, including Cloudflare R2/S3-compatible storage, Google Drive, local filesystems, SFTP, SMB, WebDAV and many cloud services.
- Copy performs one-way changed/new file movement; sync can make destination match source; bisync provides bidirectional directory synchronization.
- Integrity checks use provider-supported hashes such as MD5/SHA-1 and timestamp/size behavior.
- Network-to-network transfers are supported.
- Multi-threaded downloads to local disk are available.
- Virtual backends provide chunking, encryption, additional hashing, compression, union/combine and aliases.
- FUSE mounting and several serving protocols are available.
- Remote Control API can run rclone as a service and launch asynchronous jobs.
- RC jobs retain process execution ID, job ID, accounting group, start/end time, error, success, duration and output.
- Async jobs can be cancelled through context cancellation and expose status.
- Metrics can be exposed in OpenMetrics/Prometheus format.
- The RC API can use loopback, Unix sockets, TLS and authentication.
- The project explicitly warns that RC access is equivalent to shell access because it can execute commands, read/write local files and expose configured credentials.

## What rclone completes

- A broad cloud/provider adapter layer that Ptah should not recreate.
- Direct support for both R2 and Google Drive.
- Copy/check/sync/bisync distinctions.
- Network-to-network movement without always staging through the client.
- Optional encryption, chunking and extra hash wrappers.
- A service/API mode with async jobs and accounting groups.
- An exit path across many storage vendors.

## Important limitations for Ptah

- rclone moves directory/file views; it does not own Ptah Object, revision, Activity, Session or conflict truth.
- `sync` may delete destination content to match source and must never run implicitly.
- `bisync` has its own listing/state/conflict behavior; Ptah must not delegate canonical conflict resolution blindly.
- Provider hashes differ in availability/semantics and may not represent a trusted whole-content digest.
- RC jobs are process-local and expire; their IDs are not durable Ptah Activity IDs.
- RC has all-or-nothing authority and no per-endpoint capability scopes at the inspected version.
- RC compromise can expose every configured cloud credential and arbitrary local files.
- Mounting cloud storage does not provide local-disk latency, consistency or durability suitable for active builds/databases/containers.
- Crypt/chunker wrappers change remote names/layout and require durable configuration/key recovery.
- A successful copy/sync does not independently prove the intended Object/revision or restore correctness.
- Provider-specific metadata, eventual consistency, rate limits and timestamp behavior vary.
- Backup retention/versioning is not the same as sync.

## Must not be inherited

- RC exposed broadly or directly to untrusted clients.
- rclone configuration files as public Ptah credential contracts.
- rclone job IDs as canonical Activity identity.
- destructive sync/bisync launched without a reviewed plan, dry-run and receipt.
- cloud mount used as the live Build, container-layer or database filesystem.
- provider MD5/SHA-1 treated as universal Ptah content identity.
- synchronization treated as backup or revision authority.
- crypt keys/configuration stored only on one machine without recovery references.
- command output used as the sole transfer proof.

## Integration decision

**WRAP RCLONE AS THE PRIMARY CLOUD/PROVIDER TRANSPORT BACKEND CANDIDATE.**

Ptah owns transfer Activities, source/destination Object identities, expected revisions, conflict policy, dry-run plan, receipts and verification. rclone performs suitable provider-specific movement/checking behind a tightly scoped local adapter.

Preferred control direction:

- local Unix socket or loopback-only RC;
- Ptah-owned scoped adapter rather than exposing RC to callers;
- credential references resolved only for the selected backend/operation;
- immutable Object copies preferred over blind directory sync;
- sync/bisync treated as explicit high-impact recipes.

## Native Ptah gap

Ptah must define:

- storage connection references and per-operation scopes;
- source/destination storage locations and Object/revision IDs;
- immutable copy versus mirror/sync/bisync operation classes;
- dry-run plan and delete/conflict list;
- streaming/whole-content verification and provider-hash interpretation;
- Activity/operation/attempt mapping to rclone jobs;
- retry/resume, rate limit and partial-failure receipts;
- encryption/chunker/hasher configuration identity and recovery;
- local cache/staging rules;
- revision/conflict authority above transport;
- backup/export distinction;
- backend health, replication and repair state.

## Exit strategy

Ptah's storage/transfer contract remains backend-neutral. Provider-native SDKs, S3 clients, Drive API, rsync/SFTP or another engine can replace rclone without changing Object or Activity identity.

## Validation required

1. Copy the same immutable Object among local, R2/S3 and Drive and retain one content identity with several locations.
2. Use `check` plus Ptah whole-content digest verification.
3. Run RC through a Unix socket/scoped adapter and prove callers cannot dump all credentials or access arbitrary local paths.
4. Generate and review a destructive sync plan before execution; retain delete/conflict receipts.
5. Simulate partial provider failure/rate limiting and resume/reconcile without duplicate Objects.
6. Encrypt/chunk one Object and restore it using recovered configuration references.
7. Move data network-to-network while progress remains linked to the Ptah Activity.
8. Demonstrate that cloud mount latency/failure does not affect active local Workspace storage.
9. Replace rclone with a provider-native copy for one Object without identity changes.
10. Prove sync, backup and export remain distinct operations and states.
