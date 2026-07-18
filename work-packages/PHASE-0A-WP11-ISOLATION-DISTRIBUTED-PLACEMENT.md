# Phase 0A — WP11 Strong Isolation and Distributed Placement/Scheduling

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Runtime code:** NOT STARTED

## Purpose

Close Ptah's isolation-class, runtime-provider, Node-capability, placement, reservation, lease, fencing, secure-materialization, interruption, checkpoint and distributed-compute boundaries without turning one container runtime, VMM, cluster framework or learned router into Ptah Core.

## Sources inspected and saved

### Stronger-container isolation

- gVisor.

Saved record:

- `donors/GVISOR.md`

### VM-backed container isolation

- Kata Containers.

Saved record:

- `donors/KATA-CONTAINERS.md`

### Standalone microVM

- Firecracker.

Saved record:

- `donors/FIRECRACKER.md`

### Baseline OCI implementations

- youki;
- crun;
- existing runc/containerd/OCI evidence from WP01–WP02.

Saved records:

- `donors/YOUKI.md`
- `donors/CRUN.md`

### Distributed compute and placement workload

- Ray.

Saved record:

- `donors/RAY.md`

### Routing/evaluation boundary

- MiniRouter, retained only as an optional later evaluation workload.

Saved record:

- `donors/MINIROUTER.md`

### Existing Ptah foundations reused

- Node Protocol and capability publication;
- Workspace Provider and runtime composition;
- Activity, operation, attempt, nonce, Receipt and proof levels;
- Object, storage, transfer and checkpoint foundations;
- Device/Application/Browser Provider generations and fencing;
- Plugin runtime classes and Deno/OCI/VM escalation from WP10;
- Event, observability and resource-accounting direction.

## Canonical pins

- gVisor: `eb7b0b4c1a84b7e48e97d606e6a5e79e3eddbf01`
- Kata Containers: `a2fbc64e27ecd3fc1b5992cf9a5fabba586c7911`
- Firecracker: `5ac3f5ffdcd7a9660778df8b4c33fcad811d8fe2`
- youki: `8ed71767216cebb9436fba1da94785f1ddbe4d4d`
- crun: `fb54bc00bf4a9139e74ba68e00da22b424b90912`
- Ray: `bed46a1379d13830b314ec7ef0a924d9b42093a7`
- MiniRouter active organization lineage: `520982b737f4fb78e855d042e85cd1e6c23fd75c`; earlier recovered lineage retained in its donor record

## Licence findings

- gVisor: Apache-2.0.
- Kata Containers: Apache-2.0.
- Firecracker: Apache-2.0.
- youki: Apache-2.0.
- crun: mixed component boundary — root program GPL-2.0; inspected `libcrun` source LGPL-2.1-or-later.
- Ray: Apache-2.0.
- MiniRouter: no explicit repository licence recovered; study-only.
- Guest kernels/images, VMMs, CRIU, drivers, GPU stacks, Redis/KubeRay and packaged dependencies require separate review.

## Composite result

```text
Ptah Isolation Class
  policy-level trust/containment requirement

Ptah Runtime Provider
  Node Facility that can materialize an Isolation Class

Baseline OCI Provider
  runc | crun | youki

Stronger-container Provider
  gVisor systrap | gVisor KVM

VM-backed container Provider
  Kata + approved VMM/guest stack

Standalone microVM Provider
  Firecracker + Ptah guest bootstrap/agent

Full VM Provider
  QEMU/libvirt/platform VM paths from WP07

Ptah Node Capability Snapshot
  observed kernel/architecture/resources/providers/devices/health

Ptah Placement Request
  hard constraints plus permitted optimization preferences

Placement Candidate and Decision
  feasibility rejection reasons and score explanation

Ptah Reservation / Lease / Generation / Fence
  capacity promise and stale-worker prevention

Secure Materialization
  exact network, Object mount, device and credential grants

Checkpoint Bundle
  provider state plus compatibility, integrity and application proof

Ray
  optional trusted distributed Task/Actor/gang-scheduling Facility

MiniRouter
  optional later routing/evaluation workload, not Ptah policy
```

Isolation class, runtime implementation, placement, reservation, execution generation and proof retain separate identities.

## Isolation ladder

Closed direction:

```text
L0 host/native trusted
L1 lightweight permission runtime (Deno/WASM)
L2 baseline OCI (runc/crun/youki)
L3 userspace-kernel sandbox (gVisor)
L4 VM-backed container sandbox (Kata)
L5 standalone microVM (Firecracker)
L6 full VM/platform VM
```

This ladder is not a marketing score. Actual strength depends on exact mounts, shared filesystems, networking, devices, credentials, host/kernel/VMM versions and configuration.

Rules:

1. rootless is a privilege mode, not a new isolation class;
2. implementation language does not define containment strength;
3. incompatibility can escalate to an equal/stronger class or block;
4. fallback to weaker isolation is never silent;
5. break-glass weakening requires authorization, reason, expiry and Receipt;
6. the actual Provider and limitations are visible in UI/API evidence.

## Baseline OCI closure

runc, crun and youki remain replaceable implementations below one Ptah OCI Provider contract.

Ptah must retain:

- exact runtime binary/library version, build, signature, SBOM and licence;
- Node kernel, cgroup, namespace, seccomp and LSM capabilities;
- generated OCI config and permission snapshot;
- rootful/rootless mode;
- hooks, FDs, devices and extensions;
- runtime lifecycle mapped to Activity attempts and Receipts;
- golden cross-runtime behavior tests;
- upgrade/rollback and active-workload policy.

crun's `libcrun`, seccomp plugins, krun/WASM handlers and GPL/LGPL boundary require separate review. youki's Rust implementation is useful but remains ordinary OCI isolation.

## gVisor closure

gVisor is the primary stronger-container candidate between ordinary OCI and VMs.

Closed direction:

- use OCI-compatible `runsc` through a dedicated Provider;
- record systrap/KVM platform explicitly;
- keep cgroups, network policy, mounts, credentials and devices under Ptah authority;
- separate mutually untrusted workloads into separate sandboxes;
- fail or escalate unsupported syscalls/ioctls rather than silently weaken;
- treat checkpoint and GPU support as exact version/platform/driver capability, not generic promises.

## Kata closure

Kata is the primary VM-backed container/sandbox candidate.

Closed direction:

- guest VM and guest kernel form the additional sandbox boundary;
- containerd shim, runtime, VMM, guest agent, kernel, image, shared filesystem and devices are one versioned component set;
- Dragonball, QEMU, Cloud Hypervisor and Firecracker are explicit VMM variants rather than equivalent aliases;
- QEMU remains the broad GPU/confidential-computing path in the inspected donor;
- virtiofs, vhost, vsock, TAP, VFIO and ACPI alter threat and compatibility surfaces;
- one VM-backed sandbox does not permit mutually untrusted tenants inside the same guest;
- attestation/confidential paths require their own evidence and do not replace Ptah authorization or proof.

## Firecracker closure

Firecracker is the primary standalone microVM candidate.

Closed direction:

- one Firecracker process owns one microVM;
- production starts through Jailer-equivalent constraints;
- each instance receives unique UID/GID, jail, namespace, cgroup, network and API-socket identity;
- Ptah supplies signed kernel/rootfs, guest bootstrap/agent, Object mounting, process execution and result collection;
- host firewall supplies network filtering;
- snapshot memory/state/disk files are encrypted, authenticated, content-addressed and lifecycle-managed by Ptah;
- restore creates a new generation and requires application-level read-back;
- standalone Firecracker and Kata-Firecracker remain separate Provider compositions.

## Node capability and placement closure

A Node Capability Snapshot is observed, time-bounded truth.

It includes:

- Node generation and agent version;
- OS, kernel and architecture;
- virtualization/KVM/nested support;
- cgroup, namespace, seccomp and LSM capability;
- CPU topology/features and pressure;
- RAM, storage and network capacity/pressure;
- GPU/accelerator model, driver, memory and capability;
- installed Runtime Providers and variants;
- checkpoint compatibility groups;
- cost, location, health, drain and maintenance state;
- observation time and expiry.

Placement first filters hard feasibility:

- isolation/trust class;
- provider/runtime compatibility;
- resource capacity;
- OS/architecture/virtualization;
- device/accelerator requirements;
- network, credential and Object access;
- checkpoint/restore compatibility;
- health/drain/failure-domain/legal constraints.

Only feasible candidates are scored for:

- utilization/pressure;
- Object/data locality;
- transfer/startup cost;
- accelerator fit/fragmentation;
- network latency/bandwidth;
- monetary cost;
- failure-domain pack/spread;
- checkpoint locality;
- Workspace affinity;
- interruption risk.

Every rejection and score component is retained.

## Reservation, lease and fencing closure

Selection does not authorize work.

Ptah owns:

- atomic Reservations, including multi-Node gang bundles;
- time-bounded Leases;
- monotonic workload/provider generations;
- fencing tokens for workers and side effects;
- resource release and reconciliation.

Partial gang reservation is not `ready`.

Every provider attempt binds:

```text
activity_id
operation_id
attempt_id
reservation_id
lease_id
node_id
node_generation
runtime_provider_id
workload_generation
fence_token
```

Stale generations are rejected. External systems without fencing use nonces/idempotency/read-back reconciliation.

## Secure materialization closure

Isolation requires separate grants for:

- exact Object/View revisions;
- read-only/read-write mount or block-image access;
- shared filesystem/directfs/virtiofs/device path;
- ingress, egress, DNS, proxy and metadata access;
- device/GPU passthrough and driver ABI;
- short-lived credential references;
- cleanup, revocation and retained state.

Host paths, control sockets and runtime state remain Provider-private.

## Checkpoint and interruption closure

Checkpoint classes remain distinct:

- application checkpoint;
- CRIU/process/container checkpoint;
- gVisor sandbox checkpoint;
- microVM snapshot;
- full VM checkpoint.

Checkpoint creation is not recovery proof.

Restore requires:

1. target feasibility and compatibility;
2. new Reservation, Lease and generation;
3. provider restore attempt;
4. runtime readiness;
5. application/read-back proof;
6. renewed identity, entropy, credentials and network state where needed.

Interruption policies include non-interruptible, checkpoint-then-interrupt, restart-from-source, restart-from-approved-checkpoint, migrate-if-compatible and best-effort preemptible.

## Ray closure

Ray is an optional distributed Compute Facility, not Ptah's global scheduler or Activity Ledger.

Ptah owns:

- trust-domain cluster isolation;
- Node/Provider placement;
- credentials/network;
- durable Activity and attempt identity;
- side-effect nonce/Receipt policy;
- durable Object/Artifact promotion;
- acceptance and proof.

Ray may provide:

- Tasks, Actors and worker execution;
- logical resources and locality;
- placement groups/gang scheduling;
- transient Object-store caching;
- workload retry/actor restart;
- distributed Python/ML/data libraries.

Rules:

1. mutually untrusted Workspaces use separate Ray clusters;
2. Dashboard, Jobs, Client, GCS and worker surfaces remain private;
3. token auth is defense in depth, not isolation;
4. runtime environments are restricted dependency distribution, not provenance or containment;
5. Task/Actor retry ambiguity is guarded by Ptah operation nonces and Receipts;
6. Ray ObjectRefs never become canonical Ptah Objects;
7. placement-group IDs remain adapter metadata beneath Ptah Reservations;
8. GCS/owner recovery limitations are reconciled through Ptah records;
9. Ray remains optional and replaceable.

MiniRouter may run later as an evaluation workload using Ray or another backend. It does not own model, caller or placement policy and remains study-only until licensed.

## Accepted architecture

Saved as `decisions/ADR-0014-ISOLATION-RUNTIME-PLACEMENT-SCHEDULING-BOUNDARY.md`.

Key decisions:

1. Isolation Class and runtime implementation remain separate.
2. Baseline OCI, gVisor, Kata, Firecracker and full VM have distinct roles.
3. Rootless and memory-safe implementation are useful properties, not stronger containment classes.
4. No workload silently falls back to weaker isolation.
5. Node placement uses fresh capability/resource snapshots.
6. Hard feasibility precedes optimization scoring.
7. Candidate rejections and score components are retained.
8. Placement selection, Reservation, Lease, Generation and Fence remain separate.
9. Network, Objects, devices and credentials require explicit grants.
10. Checkpoint production, restore and application recovery are separate proof levels.
11. Ray is an optional trusted distributed workload Facility, not Ptah Core.
12. Distributed and local one-Node operation use the same Ptah identities.
13. Scheduler policy is operational policy rather than caller reasoning.
14. MiniRouter remains an optional evaluation workload and not a routing authority.

## Requirement closure verdict

Closed for Phase 0B contract design:

- `ISOLATION-001` runtime isolation-class selection and escalation;
- `DIST-001` Node capability, placement, reservation, lease, fencing and distributed execution;
- strong-isolation completion portions of `EXEC-002`, `CORE-005`, `PLUGIN-001` and external caller workloads;
- distributed checkpoint/interruption portions of `SESSION-001`;
- distributed resource/placement portions of `OBS-001`;
- provider/runtime/attempt evidence portions of `PROV-001` and `OFFLINE-001`.

Still open elsewhere:

- security/reproduction workload composition;
- Linux AT-SPI semantic completion;
- research/documentation-source cleanup;
- final Phase 0A cross-requirement review and freeze.

## Phase 0B contracts required

1. Isolation Class.
2. Runtime Provider and Implementation Variant.
3. Node Capability and Resource Snapshot.
4. Placement Request, Candidate and Decision.
5. Reservation and gang bundles.
6. Lease, Generation and Fence.
7. Workload Instance/provider alias.
8. network, Object mount, device and credential grants.
9. Checkpoint Bundle and restore compatibility.
10. interruption, eviction, migration and rescheduling.
11. distributed/Ray Facility adapter.
12. resource accounting, pressure and cost conventions.
13. runtime health, vulnerability, upgrade and rollback.
14. cross-provider golden workload/conformance corpus.

## Validation set

- runc/crun/youki golden OCI conformance;
- rootless versus strong-isolation proof;
- gVisor systrap/KVM compatibility and no-silent-fallback;
- Kata VMM/component-set comparison;
- Firecracker Jailer/network/storage/snapshot proof;
- Node capability expiry and stale-snapshot rejection;
- hard infeasibility and explained candidate scoring;
- atomic gang reservation rollback;
- stale-worker fencing;
- credential/network/Object grant revocation;
- checkpoint compatibility and application read-back;
- interruption/reschedule as new attempt/generation;
- Ray retry/actor ambiguity without duplicate protected side effect;
- Ray Object-to-Ptah Object promotion;
- GCS/owner loss reconciliation;
- separate Ray clusters for distinct trust domains;
- local one-Node operation without Ray;
- replacement of every donor runtime/backend without Ptah identity loss.

## Next Phase 0A group

Proceed with the remaining completion work:

1. Linux AT-SPI semantic automation donor pass;
2. reproduction/security workloads and scanners;
3. research/documentation-source and unresolved-profile cleanup;
4. full Phase 0A review, freeze and readiness decision for Phase 0B.

No runtime implementation is approved yet.
