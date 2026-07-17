# Donor Record — Syncthing

**Phase:** 0A / WP04  
**Status:** FIRST-PASS COMPLETE — DIRECT NODE SYNCHRONIZATION DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/syncthing/syncthing
- Default branch: `main`
- Pinned commit: `a0171e3a9b34cff897800e76fba3f8c529c7e5e8`
- Licence: MPL-2.0
- Activity: Active
- Classification: Continuous peer-to-peer file synchronization, block exchange and version-vector donor
- Ptah targets: direct Node-to-Node synchronization, block reuse, device identity, intermittent connectivity, folder indexes, conflict detection and cross-platform background operation

## Files/components inspected

- `README.md`
- `lib/protocol/vector.go`
- `man/syncthing-bep.7`
- conflict-handling source/test locations
- Block Exchange Protocol device, folder, index, block and authentication model

## Verified capabilities and patterns

- Continuously synchronizes folders among two or more computers.
- Prioritizes data safety and encrypted/authenticated communication.
- Runs on common desktop/server platforms and has background-service/GUI integrations.
- Block Exchange Protocol exchanges local file models and block hashes; devices request only missing/outdated blocks.
- File blocks range from 128 KiB to 16 MiB and can be reused across transfers.
- TLS 1.3-or-newer transport is required by the current BEP specification.
- Device authentication is certificate based; the reference implementation uses certificate fingerprints as Device IDs.
- Devices exchange implementation/version metadata and folder/device configuration.
- Version vectors represent revision causality and distinguish equal, greater, lesser and concurrent versions.
- Concurrent version vectors expose true divergence rather than silently imposing one causal order.
- Folder/index updates, block requests/responses, download progress and ping/close messages are separate protocol classes.
- Conflict copies and conflict tests exist for concurrent changes.
- Signed releases and update verification are part of the project distribution process.

## What Syncthing completes

- Efficient direct peer-to-peer block transfer between Nodes.
- Durable device identity based on certificates rather than temporary connection codes.
- Continuous operation during intermittent connectivity.
- Causal revision comparison through version vectors.
- Explicit concurrent-change/conflict handling.
- Cross-platform folder synchronization with automatic discovery/connection machinery.
- A strong donor for local-first Node replication where cloud staging is undesirable.

## Important limitations for Ptah

- Syncthing synchronizes directory trees; it does not own Ptah Object, Workspace, Activity, Session or Artifact authority.
- Folder-global model selection and conflict-copy behavior may not match Ptah's revision/ownership rules.
- Continuous mirroring can propagate deletion, corruption or unwanted changes quickly; it is not backup.
- Device IDs/certificates are Syncthing identities, not automatically Ptah Node identities or workload attestations.
- File paths, platform metadata, permissions, symlinks and case sensitivity vary across operating systems.
- Version vectors identify causality, not semantic merge correctness.
- Syncthing is not a cloud-object-storage adapter and does not replace R2/S3/Drive transport.
- MPL-2.0 creates file-level source-modification obligations; protocol/adapter study is safer than embedding modified code into Ptah Core.
- Folder-wide synchronization is too broad for some Ptah Object or Artifact transfers.
- Conflict filenames are a preservation mechanism, not a complete user/caller conflict-resolution workflow.
- Encrypted/untrusted folders and discovery/NAT behavior require deployment-specific review.

## Must not be inherited

- Syncthing folder ID or Device ID as canonical Ptah Workspace/Object/Node identity.
- Continuous two-way sync enabled by default for mutable Workspaces.
- Conflict copies treated as resolved conflicts.
- Deletion propagation treated as backup retention.
- Folder-global state used as the universal source of truth.
- Syncthing's certificates used as all-purpose Ptah workload authorization without identity mapping/attestation.
- MPL-covered source copied into native Ptah files without licence review.
- All Workspace files shared when only selected Objects/paths are required.

## Integration decision

**ADAPT VERSION-VECTOR/BLOCK-EXCHANGE PATTERNS AND SUPPORT SYNCTHING AS AN OPTIONAL NODE-SYNC BACKEND.**

Ptah should own revision identity, authority, conflict records and selected synchronization scope. Syncthing may transport approved folder/object subsets between trusted Nodes.

Recommended initial role:

- optional replication of selected local Workspace/Object directories;
- direct mini-PC/workstation synchronization;
- offline-friendly background transport;
- not the authoritative metadata or automatic merge engine.

## Native Ptah gap

Ptah must define:

- stable Ptah Node identity mapped to transport certificate/device identities;
- Object/revision IDs and version-vector or equivalent causal metadata;
- synchronization scope and path/Object allowlists;
- authoritative writer/owner for mutable Workspace state;
- delete/tombstone and retention policy;
- explicit conflict records and caller resolution;
- immutable Object dedupe versus mutable revision synchronization;
- Activity/operation/attempt receipts for scan, transfer and apply;
- content/hash verification and storage-location updates;
- encrypted/secret data classes and credential references;
- pause/quiesce/checkpoint integration for active processes/databases;
- fallback transport and exit strategy.

## Exit strategy

Ptah's synchronization contract remains independent. Syncthing, direct Ptah block transfer, rsync-like tools or cloud-mediated transport may implement it. Ptah revision/conflict records remain canonical.

## Validation required

1. Synchronize immutable Objects directly between two Nodes and reuse existing blocks.
2. Disconnect both Nodes, edit the same mutable file independently and preserve an explicit concurrent conflict.
3. Demonstrate caller-selected resolution without silently deleting either version.
4. Propagate a deletion only according to the configured tombstone/retention policy.
5. Map Syncthing certificate identity to a Ptah Node and reject an unapproved device.
6. Synchronize only an approved Object/path subset rather than the full Workspace.
7. Verify file content hashes and platform metadata differences after transfer.
8. Prove synchronization is not treated as backup by restoring an older version from the backup system.
9. Replace Syncthing with another Node transport without changing Ptah Object/revision identity.
10. Complete MPL integration/licence review before bundling or modifying Syncthing code.
