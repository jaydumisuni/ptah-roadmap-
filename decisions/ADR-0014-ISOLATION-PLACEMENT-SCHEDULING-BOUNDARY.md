# ADR-0014 — Isolation, Placement and Scheduling Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Phase:** 0A / WP11 closure

## Context

Ptah must execute work across:

- trusted local processes;
- permission-scoped scripts;
- ordinary OCI containers;
- stronger userspace-kernel sandboxes;
- VM-backed container sandboxes;
- standalone microVMs and full VMs;
- physical/specialist Devices;
- one local Node;
- several Nodes and accelerators;
- optional distributed compute frameworks.

These concerns are often collapsed into one runtime or scheduler. That would create false guarantees:

- a fast OCI runtime being described as strong isolation;
- a logical CPU label being described as a hard quota;
- a Ray retry being described as safe durable recovery;
- a container/VM snapshot being described as a portable Session;
- a Registry trust label being allowed to weaken sandbox policy;
- a missing runtime silently falling back to host execution;
- a model router or cluster scheduler deciding caller priority, spending or acceptance.

Existing Ptah decisions already separate Node, Workspace Provider, Activity, operation/attempt, Object transfer, Device leases and proof. WP11 extends those contracts rather than replacing them.

## Decision

Ptah will own separate versioned contracts for:

1. **Isolation Class and Threat Profile**;
2. **Runtime/Workspace Provider Profile**;
3. **Node Capability and Resource Snapshots**;
4. **Placement Request, Candidate and Decision**;
5. **Resource Reservation**;
6. **Lease, Generation and Fencing Token**;
7. **Worker Claim and Activity Attempt**;
8. **Network Policy and Credential Grant**;
9. **Object/Data Locality and Transfer Plan**;
10. **Checkpoint Capability, Checkpoint and Restore Attempt**;
11. **Scheduler/Distributed Facility Adapters**;
12. **Placement, resource and recovery Receipts**.

No runtime, scheduler, Node daemon, cluster, queue or donor-specific ID becomes canonical Ptah identity.

Full composition and proof plan: `work-packages/PHASE-0A-WP11-STRONG-ISOLATION-DISTRIBUTED-PLACEMENT.md`.

---

# Isolation classes

The neutral family must represent at least:

```text
trusted_host_process
permission_scoped_script
baseline_oci
userspace_kernel_oci
vm_backed_container
standalone_microvm
full_virtual_machine
specialist_remote_provider
physical_device_provider
```

The family is not one perfectly linear security score. Compatibility, host surface, startup cost, device access, checkpoint behavior and threat model remain explicit.

## Initial donor placement

- **Deno** — permission-scoped lightweight JavaScript/TypeScript Tool runtime.
- **containerd/OCI** — baseline image/content/container/Task substrate.
- **runc, crun, youki** — replaceable baseline OCI runtime implementations, not separate strong-isolation classes.
- **gVisor/runsc** — primary userspace-application-kernel OCI candidate.
- **Kata Containers** — primary VM-backed container/Workspace candidate.
- **Firecracker** — primary standalone microVM candidate and optional Kata VMM.
- **QEMU/libvirt/platform VMs** — broader full-VM/application compatibility.
- **physical/specialist Providers** — anchored resources with explicit lease and non-migratable state.

Every runtime profile pins its implementation, version, component set, platform mode, guest/kernel image, filesystem/network/device configuration, checkpoint capabilities and limitations.

## No silent downgrade

When a selected runtime is unavailable or incompatible:

1. Ptah reports the exact failure;
2. an equal or stronger caller-approved alternative may be evaluated;
3. weaker isolation requires explicit policy and a durable decision Receipt;
4. Ptah never silently falls back from gVisor, Kata, microVM or VM to ordinary OCI or host process;
5. unsupported GPU, device, confidential-computing or checkpoint paths remain unsupported.

Registry presence, publisher trust, official labels or clean scans do not authorize weaker isolation.

---

# Node capability and resource truth

A stable Node is separate from:

```text
node_instance_id
connection_id
connection_epoch
provider_worker_generation
capability_snapshot_id
resource_snapshot_id
```

Capability Snapshots record observed/versioned facts such as:

- OS, kernel and architecture;
- CPU topology/features;
- KVM/virtualization/nested support;
- cgroup, namespace, seccomp, LSM and IOMMU support;
- runtime/provider profiles;
- storage/network classes;
- accelerators, Devices and drivers;
- guest/VMM/confidential-computing support;
- toolchains and Facilities;
- checkpoint/restore compatibility;
- patch/advisory state and limitations.

Resource Snapshots distinguish:

- configured capacity;
- hard capacity;
- allocatable capacity;
- reservations and leases;
- observed usage/pressure;
- overcommit policy;
- hard enforcement mechanism.

Logical scheduler resources are not hard enforcement. Ray CPU/GPU/custom labels provide admission and placement inputs; cgroups, VM boundaries, device/IOMMU policy and Provider controls enforce actual limits.

---

# Placement boundary

## Placement Request

A request carries caller policy plus exact requirements for:

- Provider family and minimum isolation;
- CPU/RAM/storage/network/accelerator bundle;
- OS/architecture/kernel/tool compatibility;
- required Objects, models, caches, volumes and data locality;
- required physical Devices;
- credential and network scope;
- privacy, region and failure-domain constraints;
- deadline, duration, preemption/checkpoint and retry class;
- budget/cost references;
- allowed/forbidden Nodes or regions.

## Candidate and Decision

Every candidate is retained with:

- exact capability/resource snapshot;
- compatible/incompatible result;
- hard rejection reasons;
- missing capabilities;
- required transfers/grants;
- estimated resource/start/transfer cost;
- limitations.

Hard constraints are filtered before scoring. A score never overrides isolation, privacy, Device, credential or compatibility requirements.

The Placement Decision explains the selected mechanical match and references caller policy. Ptah does not invent company priority, waive restrictions, authorize spending or accept outputs.

---

# Reservation, lease and fencing

## Reservation

A Resource Reservation is an expiring claim on a declared bundle. It records Node, Provider profile, holder Activity/attempt, generation, expiry, state and release Receipt.

Gang/multi-bundle reservations are all-or-nothing unless the workload explicitly supports elastic partial execution.

## Lease

A Lease grants temporary authority over a scarce or mutable resource, including:

- Provider worker ownership;
- writable Workspace/volume/cache ownership;
- Device control;
- singleton service ownership;
- reserved accelerator or port use.

Every mutating operation presents the current fencing token. A stale worker may continue computing, but cannot commit authoritative state after supersession.

## Worker Claim

Dispatch binds one Activity attempt to:

- Node and Provider generation;
- reservations and leases;
- fencing tokens;
- heartbeat deadline;
- operation/attempt identity.

Heartbeat loss makes the claim suspect/expired. It does not prove whether an external side effect occurred.

---

# Scheduler and distributed framework boundary

Ptah owns the backend-neutral placement/Reservation contracts and may begin with a small SQL-backed implementation preserving migration/conformance paths.

## Ray

Ray may implement selected distributed Python/AI workloads through Tasks, Actors, Objects, logical resources and Placement Groups.

Ray does not own:

- canonical Activity/attempt identity;
- hard resource isolation;
- mutually untrusted tenant boundaries;
- caller priority/spend/acceptance;
- credential or Object permissions;
- external side-effect idempotency;
- durable cross-backend truth;
- Node admission/security posture;
- proof.

Mutually untrusted Ray workloads require separate clusters inside separately isolated Ptah Workspaces/Providers.

## MiniRouter

MiniRouter is an optional future routing/evaluation workload. It is not the Ptah scheduler, Node placement engine or reasoning authority. Source reuse remains blocked until its licence is resolved.

---

# Network, credential and data placement

- Node pairing is only bootstrap; stable cryptographic identity and revocable credentials are required.
- public host/port disclosure is not a secure Node protocol.
- each attempt receives an explicit Network Policy and short-lived Credential Grant.
- ambient host credentials are not inherited by default.
- secrets never enter capability snapshots, ordinary logs or status Receipts.
- placement verifies that selected Nodes/Providers can enforce egress, ingress, private-network, metadata-service and tunnel requirements.
- required Objects must be transferred and digest-verified before execution.
- mutable Workspaces move only through revisions, snapshots/checkpoints and reconciliation plans.
- cache locality may influence placement but cache never becomes source truth.
- physical Devices are anchored to current Provider Nodes and are not treated as migratable.

---

# Recovery, checkpoint and migration

Ptah distinguishes:

- retry from inputs;
- Activity/application checkpoint;
- Workspace/filesystem revision;
- container/VM/provider snapshot;
- process-memory checkpoint;
- Session archive/export;
- migration to another Node.

Checkpoint capability is Provider-profile-specific. Snapshot/checkpoint creation is not proof of portability, application consistency or successful restore.

Restore:

- creates a new Activity attempt and Provider generation;
- checks exact runtime/component/hardware compatibility;
- renews identity, entropy, credentials, network and leases where required;
- keeps source workers fenced;
- requires application/read-back proof before readiness.

Automatic retry is allowed only under the Activity's retry class. Lost Nodes performing external/physical/destructive side effects remain `unknown` or `recovering` until authoritative reconciliation.

Preemption is permitted only when restart, checkpoint, compensation or application pause is explicitly safe.

Migration is never implied universally and requires verified data/checkpoint transfer, target compatibility, renewed grants/leases, source fencing and target read-back proof.

---

# One-Node and multi-Node rule

A single Linux Node remains a complete supported Ptah deployment using the same contracts:

- local placement;
- local SQL Activity/catalogue state;
- local OCI Provider;
- local Object store/cache;
- local journal/outbox;
- no Ray or cluster scheduler requirement.

Adding Nodes extends placement, locality, reservations, failure domains and optional distributed Facilities without changing Workspace, Activity, Object, Package or Session identity.

A disconnected Node may perform explicitly permitted local work and reconcile later. Distributed-backend failure may degrade compatible work to local execution, but isolation, Device, data and credential constraints never silently weaken.

---

# Donor decisions

## gVisor

- primary stronger-container/userspace-kernel candidate;
- separate Systrap/KVM profiles;
- compatibility and performance failures are explicit;
- host cgroups/network/mount/credential policy remains Ptah-owned.

## Kata Containers

- primary VM-backed container/Workspace candidate;
- separate mutually untrusted workloads receive separate VMs;
- VMM/guest/component profile is explicit;
- GPU/confidential paths require exact hardware/driver/attestation evidence.

## Firecracker

- primary standalone microVM candidate;
- Jailer-equivalent containment and host networking/storage policy required;
- snapshot memory/state/disk bundle, integrity, encryption and application consistency are Ptah responsibilities.

## youki and crun

- optional baseline OCI implementations for conformance and Node-specific performance/footprint;
- neither is a stronger isolation class;
- crun process wrapping is preferred until `libcrun` licence/failure-boundary review approves embedding.

## Ray

- optional distributed Python/AI execution and gang-placement Facility;
- logical resources and retries remain subordinate to Ptah hard limits, attempts and fencing.

---

# Consequences

## Positive

- Ptah can match isolation to workload risk without one universal runtime.
- ordinary trusted work avoids unnecessary VM overhead.
- untrusted Plugins and workloads can escalate without changing identities.
- placement becomes explainable and auditable.
- logical scheduling and hard resource enforcement cannot be confused.
- stale workers/Devices are fenced.
- one-Node operation remains first-class.
- Ray and future schedulers remain replaceable.
- checkpoint/restore claims remain honest and profile-specific.
- caller reasoning and approval remain outside Ptah.

## Costs

- several schemas, profiles and conformance suites are required;
- runtime/component compatibility matrices must be maintained;
- secure Node identity, network and credential delivery require substantial work;
- data locality and transfer planning add scheduling complexity;
- checkpoint compatibility and migration require expensive proof;
- multi-Node deployments need durable reservations, leases, drain and reconciliation.

## Do-not-break rules

> Never describe a runtime implementation, rootless mode, logical scheduler resource, Registry trust label, clean scan, snapshot command or retry mechanism as a stronger guarantee than it actually provides.

> Never silently weaken isolation, move mutable data, transfer Device control, expose credentials or repeat side effects because a preferred Node/runtime is unavailable.

> Never let Ray, MiniRouter, a Provider, model, router or cluster scheduler become Ptah's reasoning, priority, spend or acceptance authority.

---

# Required proof before freeze

1. Same workload runs under baseline OCI, gVisor and VM/microVM profiles with stable Ptah identity.
2. Unsupported compatibility does not trigger silent isolation downgrade.
3. runc/crun/youki conformance differences are measured.
4. stale Node snapshots/connection epochs and Provider generations are rejected.
5. logical reservations and physical resource limits are proven separately.
6. expired worker lease/fencing prevents stale commit.
7. gang reservation exposes pending/infeasible/deadline states.
8. Object and Device locality produce explicit placement/transfer decisions.
9. attempt-scoped credentials and network policy are enforced/revoked.
10. retry-safe Node failure does not duplicate side effects.
11. ambiguous external side effect remains unresolved until authoritative evidence.
12. checkpoint restore requires exact compatibility and application readiness proof.
13. Node drain handles restartable, checkpointable and non-preemptible work separately.
14. Ray execution remains subordinate to Ptah Activities, isolation and hard limits.
15. distributed placement can disappear while compatible work continues on one Node.
16. runtime and scheduler implementations can be replaced without changing public identities.
