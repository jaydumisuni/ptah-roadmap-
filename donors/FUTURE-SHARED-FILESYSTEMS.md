# Donor Record — Future Shared Filesystem Candidates

**Phase:** 0A / WP04  
**Status:** EVALUATED — PARKED UNTIL DISTRIBUTED PTAH REQUIREMENT  
**Inspected:** 2026-07-17

## Candidates

### JuiceFS

- Canonical URL: https://github.com/juicedata/juicefs
- Pinned commit: `a84508bffa2403fd192939be0e8438fe4f709ddd`
- Licence: Apache-2.0
- Classification: POSIX filesystem over Object Storage plus metadata engine

### SeaweedFS

- Canonical URL: https://github.com/seaweedfs/seaweedfs
- Pinned commit: `6f14be1138302ae1306c4a26f858f6d0b59a5b89`
- Licence: Apache-2.0
- Classification: scalable blob/file/S3 system with filer, replication and tiering

## Files/components inspected

- JuiceFS `README.md`
- SeaweedFS `README.md`
- documented architecture, metadata, Object Storage, POSIX, FUSE, S3, replication and tiering boundaries

## Verified JuiceFS capabilities/patterns

- POSIX-compatible filesystem backed by Object Storage and a separate metadata engine.
- Metadata engines include Redis, MySQL, SQLite, TiKV and others.
- Files are divided into chunks, slices and blocks before storage in Object Storage.
- Strong consistency, global file locks, atomic metadata operations and close-to-open behavior are documented.
- Supports FUSE/local access, S3 gateway, Hadoop and Kubernetes CSI.
- Shared read/write access from many clients.
- Data encryption, compression and local caching are available.
- Supports S3-compatible stores, including a path compatible with R2-like backends.

## Verified SeaweedFS capabilities/patterns

- Distributed blob store designed for large file counts and fast access.
- Volume servers distribute file data/metadata load; optional Filer provides directories/POSIX attributes.
- Supports single-node `weed mini` through large multi-server deployments.
- Provides S3, WebDAV, FUSE, replication, tiered storage, cloud backup/integration and erasure coding.
- Filer metadata backends include SQL, Redis, MongoDB, RocksDB, SQLite and others.
- Supports active-active replication and asynchronous cloud integration.
- Can provide local hot storage with cloud-backed warm capacity.

## What these systems could complete later

- Shared POSIX-like storage across several Ptah Nodes.
- High-volume self-hosted Object/file storage.
- Kubernetes/cluster persistent volumes.
- Hot-local plus cloud-tiered storage.
- Cross-cluster replication and large-scale capacity growth.
- A shared environment for workloads that genuinely require concurrent POSIX access.

## Why they are not selected for Ptah v1

Ptah v1 can meet its requirements more simply with:

- local SSD/NVMe for active Workspaces, caches and volumes;
- content-addressed local Object storage;
- R2/S3 for durable remote Objects/Artifacts;
- SQLite locally and shared SQL for metadata;
- aria2/tus/rclone/Syncthing for transfer paths;
- restic for encrypted backup.

Adding a distributed filesystem now would introduce:

- another metadata/control plane;
- FUSE/kernel/platform complexity;
- Object Storage layout hidden behind filesystem-specific block formats;
- operational backup/repair requirements;
- consistency/locking semantics that Ptah would still need to map to Objects, Workspaces and Activities;
- a risk of treating remote shared storage as a substitute for fast local active storage;
- unnecessary coupling before multiple always-on Nodes and shared-write workloads exist.

## Important limitations and boundaries

- Neither system replaces Ptah Object, revision, Activity, Session or Artifact identity.
- Filesystem consistency does not provide semantic conflict resolution or application-consistent snapshots by itself.
- Underlying Object Storage layout is implementation-specific and not directly human-readable.
- FUSE/shared POSIX does not make cloud/object latency suitable for every build, database, container or emulator workload.
- Metadata engine availability becomes critical infrastructure.
- Backup and disaster recovery remain separate requirements.
- Cross-platform behavior and Windows/macOS support need proof for the actual Ptah topology.
- A shared filesystem can spread corruption/deletion just as efficiently as valid writes.

## Integration decision

**PARK FOR PHASE 12 DISTRIBUTED PTAH.**

Do not add JuiceFS or SeaweedFS to the first online vertical slice.

Re-open evaluation only when measured requirements show one or more of:

1. several always-on Nodes require concurrent POSIX access to the same mutable data;
2. local storage plus Object transfer cannot meet latency/throughput targets;
3. Kubernetes/cluster volumes become an approved deployment path;
4. self-hosted storage scale or small-file count exceeds the simple local+S3 architecture;
5. tiered hot/warm storage materially reduces cost/latency;
6. the mini-PC/workstation topology requires a shared volume rather than Object/revision movement.

## Future comparison criteria

When reopened, compare:

- consistency and locking;
- metadata availability and recovery;
- single-node and multi-node performance;
- R2/S3 compatibility and egress patterns;
- local cache behavior;
- snapshot/backup integration;
- encryption and key management;
- Windows/macOS/Linux access;
- Kubernetes requirements;
- repair/scrub and disaster recovery;
- operational complexity;
- ability to preserve Ptah Object and revision identities;
- clean exit/migration path.

## Exit strategy

Ptah storage classes and Object catalogue remain independent. Either filesystem can be introduced as a Workspace/Volume backend later or removed without changing public Ptah Object, Artifact or Session contracts.

## Validation required before future adoption

- benchmark actual Ptah workloads against local storage plus Object transfer;
- simulate metadata-engine loss and restore;
- prove consistent concurrent writes and explicit application snapshots;
- verify backup/restore independently;
- test Node/network partition behavior;
- measure FUSE/cache behavior and platform compatibility;
- migrate data out without losing Ptah identities/provenance.
