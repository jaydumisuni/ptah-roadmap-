# Donor Record — containerd and OCI Specifications

**Phase:** 0A  
**Status:** FIRST-PASS COMPLETE — OWNED EXECUTION FOUNDATION CANDIDATE  
**Inspected:** 2026-07-17

## Identity

### containerd

- Canonical URL: https://github.com/containerd/containerd
- Pinned commit: `cb23630be7e6473870431eb9eeb84d27abc768b2`
- Licence: Apache-2.0 for code; CC-BY-4.0 for README/docs
- Activity: Active CNCF graduated project

### OCI Runtime Specification

- Canonical URL: https://github.com/opencontainers/runtime-spec
- Pinned commit: `6999a89a76a0329f440d5740497bedb9dd431297`
- Licence: Apache-2.0

### OCI Image Specification

- Canonical URL: https://github.com/opencontainers/image-spec
- Pinned commit: `af26a05fba5ee648512f4ea3c9fda1fcc1b6d6dc`
- Licence: Apache-2.0

### OCI Distribution Specification

- Canonical URL: https://github.com/opencontainers/distribution-spec
- Pinned commit: `967efdc079b91785ad18c77cc4f8991a47feefbf`
- Licence: Apache-2.0

- Classification: Mature upstream machinery and execution substrate candidate
- Ptah targets: container lifecycle, images, content store, snapshots, tasks, runtimes and registry interoperability

## Files/components inspected

- containerd `README.md`
- containerd `docs/features.md`
- OCI Runtime Spec `README.md`
- OCI Image Spec `README.md`
- OCI Distribution Spec `spec.md`

## Verified capabilities and patterns

- containerd is explicitly designed to be embedded into larger systems.
- Linux and Windows daemon support.
- Complete host container lifecycle: image transfer/storage, execution/supervision, snapshots and network/storage attachment.
- Namespaces allow multiple consumers to share content while separating container and image identities.
- Containers are metadata objects; runnable processes are separate Tasks.
- OCI runtime specifications connect images/root filesystems to low-level runtime implementations.
- Built-in overlayfs and btrfs snapshot support plus external snapshotter plug-ins.
- Optional CRIU-backed checkpoint and restore, including registry transport of checkpoints.
- OCI Image Spec defines portable image manifests, layers, configuration, descriptors and validation types.
- OCI Distribution Spec is content-type agnostic and defines digest-addressed push, pull, discovery, management, resumable transfer, range requests, deduplication and referrer relationships.

## What this completes beyond workspace platforms

- An owned, vendor-neutral container substrate rather than dependence on Coder, Daytona or E2B control planes.
- Stable standards between images, bundles, runtimes and registries.
- A clean separation between container metadata and running process/task.
- Content-addressed distribution and snapshot foundations.
- A path to alternate OCI runtimes and snapshotters.

## Important limitations

- containerd is not a user-facing workspace manager.
- It does not supply Ptah workspaces, objects, activities, sessions, UI, scheduling or durable workflow history.
- Networking, port exposure and higher-level environment configuration require additional machinery.
- Checkpoint/restore depends on CRIU and is not portable or universally supported.
- OCI bundles may require host-specific adjustment.
- Container isolation is not enough for every multi-tenant or hostile workload.
- Containerd APIs and implementation complexity are larger than directly shelling out to Docker for an early proof.

## Must not be inherited

- container, Task, Ptah Activity and Ptah Workspace collapsed into one record.
- checkpoint/restore advertised as universal.
- direct exposure of low-level containerd APIs as Ptah's public workspace API.
- container-only assumptions for native, VM, device or application providers.
- registry content identity confused with Ptah's richer object/provenance graph.

## Integration decision

**CANDIDATE MATURE UPSTREAM FOUNDATION — ADOPT STANDARDS, WRAP RUNTIME.**

Ptah should adopt OCI compatibility and own a container Workspace Provider over mature OCI machinery. The exact v1 implementation may begin through a narrower adapter while preserving a direct containerd path.

## Native Ptah gap

- Workspace Provider and Activity mappings;
- Node capability and health integration;
- typed create/start/stop/pause/snapshot operations;
- object, artifact and session registration;
- port/service registry;
- provider conformance and error mapping;
- image/build provenance and policy supplied by callers;
- optional stronger isolation backends;
- lifecycle recovery independent of containerd process state.

## Exit strategy

The Ptah provider speaks OCI concepts through its own contract. Backends may include containerd, Docker/Moby, CRI-O or other conforming runtimes. Ptah schemas do not depend on one daemon implementation.

## Validation required

- Create two isolated Ptah workspaces using separate containerd namespaces or equivalent provider separation.
- Reuse a shared image/content store without identity collision.
- Map container metadata and Tasks to separate Ptah Workspace and Activity records.
- Stop, restart and recover provider state.
- Prove unsupported checkpoint operations are explicit.
- Pull and push content by digest and verify resumable transfer/deduplication behavior.
- Run the same provider conformance suite against at least one alternative OCI path.
