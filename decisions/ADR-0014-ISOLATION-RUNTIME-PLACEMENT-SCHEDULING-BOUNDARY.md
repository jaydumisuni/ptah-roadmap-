# ADR-0014 — Isolation Class, Runtime Provider, Placement, Lease and Scheduling Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Phase:** 0A / WP11 Strong Isolation and Distributed Placement/Scheduling closure

## Context

Ptah must run trusted and untrusted workloads across one local Node, future mini-PCs, remote Nodes, accelerators and distributed clusters without confusing runtime implementation, isolation strength, placement policy, caller reasoning, scheduling state or proof.

The inspected donors solve different layers:

- runc/containerd/OCI provide the baseline container contract already recovered in the Core runtime work;
- youki contributes a Rust low-level OCI runtime, rootless behavior and cross-runtime conformance evidence;
- crun contributes a low-memory C runtime, systemd/cgroup integration, `libcrun`, CRIU and alternative-handler lessons;
- gVisor contributes a userspace application kernel and a stronger-container class between ordinary OCI and VMs;
- Kata Containers contributes OCI/container lifecycle backed by a guest VM and guest kernel, with pluggable VMMs and confidential/GPU paths;
- Firecracker contributes a minimal standalone KVM microVM Provider, one-process/one-VM lifecycle, Jailer, rate limits and versioned snapshots;
- Ray contributes distributed Tasks, Actors, immutable runtime Objects, hard resource feasibility, gang reservations, locality and cluster workload execution;
- existing Ptah Node, Workspace, Activity, Event, Object, transfer, checkpoint, Device and Application contracts already provide the identities that donor runtimes lack;
- MiniRouter contributes later routing-policy evaluation only and remains study-only until its licence is resolved.

No donor defines Ptah's canonical Isolation Class, Runtime Provider, Node capability snapshot, Placement Request, Reservation, Lease, Fence, Workload Generation, secure credential delivery, checkpoint proof or distributed Activity semantics.

## Decision

Ptah will own backend-neutral contracts for:

1. Isolation Class;
2. Runtime Provider and Runtime Implementation;
3. Node Capability and Resource Snapshot;
4. Placement Request and hard constraints;
5. Placement Candidate, score and explanation;
6. Reservation and reserved-resource bundle;
7. Lease, generation and fencing token;
8. Workload Instance and Provider-local alias;
9. Network, Object mount, device and credential grants;
10. Checkpoint Bundle and restore compatibility;
11. interruption, eviction, migration and rescheduling policy;
12. distributed-compute Facility mappings;
13. runtime escalation and no-silent-weakening rules;
14. provider conformance, health, upgrade and rollback evidence.

No container ID, sandbox ID, VM ID, Ray Node/Task/Actor/ObjectRef, placement-group ID or CRIU/snapshot path becomes canonical Ptah identity.

---

# Isolation classes

Ptah distinguishes **isolation strength** from the runtime implementation used to provide it.

```text
L0 — host/native trusted
  direct process or application on an approved Node
  only for trusted code and explicit host authority

L1 — lightweight permission runtime
  Deno/WASM-style scoped tool execution
  useful for narrow scripts; not a kernel boundary

L2 — baseline OCI
  runc, crun, youki or equivalent
  host kernel shared; namespaces/cgroups/capabilities/seccomp/LSM

L3 — userspace-kernel sandbox
  gVisor/runsc
  compatible OCI workload sees a userspace Linux implementation

L4 — VM-backed container sandbox
  Kata Containers with approved VMM/guest stack
  guest kernel per sandbox/pod trust boundary

L5 — standalone microVM
  Firecracker or equivalent
  one controlled workload/Workspace generation per microVM

L6 — full VM / platform VM
  QEMU/libvirt, Hyper-V, macOS VM or equivalent
  broad compatibility and strongest ordinary platform separation
```

These levels are policy classes, not universal security scores. Device passthrough, shared filesystems, host networking, credentials, kernel/VMM versions and configuration can weaken any class.

The selected provider record includes:

```text
isolation_class
runtime_provider_id
implementation_name
implementation_version
build_digest
host_kernel_and_architecture
virtualization_mode
configuration_digest
network_mode
filesystem_mode
mount_grants
credential_grants
device_grants
security_profile
known_limitations
```

## No silent weakening

When a requested class is unavailable or incompatible:

1. Ptah may select an equal or stronger approved class;
2. Ptah may return `unsatisfied` or `blocked`;
3. Ptah must not silently fall back to a weaker class;
4. break-glass weakening requires explicit authorized policy, reason, expiry and Receipt;
5. UI and APIs must show the actual provider and limitations.

Compatibility failure and security policy are separate. A workload incompatible with gVisor may escalate to Kata/Firecracker/VM; this does not prove the stronger provider will support it.

---

# Runtime Provider and implementation

A Runtime Provider is a Ptah Facility capable of materializing and supervising one isolation class on one or more Nodes.

```text
runtime_provider_id
provider_type
isolation_classes
implementation_variants
node_requirements
supported_architectures
supported_workload_types
checkpoint_capabilities
network_capabilities
storage_capabilities
device_capabilities
health_state
version_and_build
```

Runtime implementations remain replaceable:

```text
OCI Provider
  runc | crun | youki

gVisor Provider
  runsc systrap | runsc KVM

Kata Provider
  Dragonball | QEMU | Cloud Hypervisor | Firecracker | approved variant

MicroVM Provider
  Firecracker | future equivalent

Distributed Compute Facility
  Ray | future backend
```

Rootless is a privilege/configuration mode, not a separate strong Isolation Class.

A memory-safe implementation is useful evidence but does not increase the isolation class by itself.

---

# Node capability and resource truth

Placement uses current, receipted Node observations rather than names or static claims.

A Node Capability Snapshot includes:

```text
node_id
node_generation
observed_at
agent_version
os_and_kernel
architecture
virtualization_and_nested_virtualization
KVM_or_platform_hypervisor
cgroup_mode
namespaces
LSM_and_seccomp
CPU_topology_and_features
RAM_total_available_pressure
local_storage_capacity_and_pressure
network_interfaces_and_reachability
GPU_accelerator_model_driver_memory
runtime_provider_inventory
checkpoint_compatibility_groups
cost_and_location_metadata
health_and_drain_state
snapshot_expiry
```

Capacity has separate values for:

- physical/observed total;
- administratively allocatable;
- currently reserved;
- currently consumed;
- pressure/health headroom;
- overcommit policy.

Logical resource labels are scheduling inputs, not proof of physical capacity or exclusive reservation.

---

# Placement Request and decision

A Placement Request belongs to a Ptah Activity or Workload generation.

```text
placement_request_id
activity_id
workspace_id
caller_reference
workload_revision
required_isolation_class
allowed_provider_classes
hard_resource_requirements
architecture_and_OS_constraints
accelerator_constraints
network_and_credential_constraints
source_Object_and_data_location_constraints
checkpoint_or_restore_constraints
fault_domain_constraints
locality_preferences
cost_budget
latency_or_deadline
interruption_policy
created_at
```

Placement happens in two phases.

## Hard feasibility

A Node/Provider candidate is rejected when any required condition fails:

- trust/isolation class;
- runtime/provider compatibility;
- architecture, OS or virtualization;
- CPU, RAM, disk, GPU/device capacity;
- required image/kernel/checkpoint compatibility;
- network route or data access;
- credential delivery policy;
- Workspace/caller visibility;
- health, drain or maintenance state;
- legal/location/licence restrictions;
- resource reservation capability.

## Optimization score

Only feasible candidates are scored. Scoring may consider:

- current utilization and pressure;
- Object/data locality and transfer cost;
- startup/cold-cache cost;
- accelerator fit and fragmentation;
- network latency/bandwidth;
- monetary cost;
- energy/thermal policy where measured;
- failure-domain spread or pack preference;
- checkpoint locality and restore time;
- Workspace affinity;
- interruption/preemption risk.

Every decision retains candidate rejection reasons, score components, selected candidate and policy revision.

Scheduler policy is operational policy, not caller reasoning. Callers may supply constraints/preferences but do not silently control Node authority.

---

# Reservation, lease, generation and fencing

Placement selection alone does not reserve capacity or authorize execution.

```text
Reservation
  resource bundle promised on one or more Nodes

Lease
  time-bounded authority to use the reservation/provider

Generation
  monotonic incarnation of the workload/provider instance

Fence token
  proof carried by workers and side-effecting operations to reject stale generations
```

A reservation may contain multiple atomic bundles for gang workloads.

```text
reservation_id
placement_request_id
bundle_definitions
node_and_provider_assignments
resource_quantities
created_at
expires_at
state
```

States include:

```text
proposed
reserving
reserved
partially_failed
active
releasing
released
expired
lost
reconciled
```

Partial gang reservation is never reported as ready. Resources are rolled back or the state remains explicit for reconciliation.

A workload attempt binds to:

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

Stale workers, delayed Events and external side effects with old fencing tokens are rejected where the target supports fencing. Where external systems cannot fence, Ptah requires operation nonces, idempotency keys or read-back reconciliation.

---

# Secure materialization

Isolation is incomplete without controlled network, data, devices and credentials.

## Objects and storage

- Workloads receive exact Object/View revisions, not arbitrary host paths.
- Mounts declare read-only/read-write, source digest/revision, destination, propagation, retention and cleanup.
- Host paths and runtime state directories remain Provider-private.
- Shared filesystems, virtiofs, directfs, block devices and Object copies are separate grant types.
- Device passthrough and GPU access require exact device, driver, ABI, IOMMU/capability and revocation records.

## Network

- every workload has an explicit network mode and identity;
- ingress, egress, DNS, proxy, service and metadata access are policy-controlled;
- gVisor/Kata/Firecracker/Ray do not replace host/network policy;
- control-plane ports remain private;
- trust domains use separate networks or equivalent enforced segmentation.

## Credentials

- credentials are references, not embedded environment truth;
- delivery is scoped to exact workload generation, Facility, destination and lifetime;
- short-lived credentials are preferred;
- credential revocation occurs on lease loss, stop, rollback, quarantine or removal;
- snapshots/checkpoints containing credentials are classified and protected.

---

# Checkpoint, interruption and migration

Checkpoint capability is Provider-specific.

Checkpoint types include:

```text
process_checkpoint      CRIU/runtime-sensitive
container_checkpoint    runtime/kernel/LSM-sensitive
sandbox_checkpoint      gVisor/platform-sensitive
microVM_snapshot        VMM/CPU/device-sensitive
full_VM_checkpoint      hypervisor/device-sensitive
application_checkpoint  application-defined durable state
```

A Checkpoint Bundle records:

```text
checkpoint_id
workspace_or_activity_reference
provider_and_runtime_revision
source_node_and_generation
component_digests
memory_state
machine_or_process_state
disk_or_Object_revisions
network_and_vsock_state
credential_and_secret_classification
compatibility_requirements
integrity_signature_and_encryption
application_consistency_state
created_activity_and_receipts
```

Checkpoint creation proves only that files/state were produced. Recovery requires:

1. compatible target feasibility;
2. new Reservation, Lease and generation;
3. restore attempt;
4. provider readiness;
5. application/read-back proof;
6. explicit handling of lost connections, identities, entropy and credentials.

Interruption policies include:

```text
non_interruptible
checkpoint_then_interrupt
restart_from_source
restart_from_latest_approved_checkpoint
migrate_if_compatible
best_effort_preemptible
```

A rescheduled attempt is a new attempt and generation. It does not rewrite earlier evidence.

---

# Ray and distributed execution

Ray is an optional distributed Compute Facility, not Ptah's global scheduler.

Ptah owns:

- trust-domain cluster creation;
- Node and Provider selection;
- isolation around the Ray cluster;
- credentials and network exposure;
- durable Activity/attempt identity;
- operation nonces and side-effect receipts;
- durable Object/Artifact promotion;
- acceptance and proof.

Ray may own inside the approved cluster:

- Task/Actor dispatch;
- logical resource scheduling;
- placement groups/gang reservations as an adapter implementation;
- Object-store caching;
- workload retries and actor restart;
- ML/data/serve libraries.

Rules:

1. mutually untrusted Workspaces use separate isolated Ray clusters;
2. Dashboard, Jobs, Client, GCS and worker ports are not public;
3. runtime environments are restricted dependency features, not isolation or provenance;
4. Ray retries of side-effecting work require Ptah operation nonce/idempotency policy;
5. Ray ObjectRefs are transient and promote to Ptah Objects only through explicit hashed persistence;
6. Ray placement-group IDs remain adapter metadata under Ptah Reservations/Leases;
7. GCS recovery does not replace Ptah reconciliation;
8. Ray can be removed without changing Ptah Activity or Object identity.

MiniRouter may later run as a Ray or other distributed evaluation workload. It does not select Ptah's global reasoning or scheduling policy.

---

# Single-Node and multi-Node behavior

Ptah remains useful on one Node.

- Placement uses the same request/candidate/reservation/lease contracts even when only one candidate exists.
- Local operation does not require Ray, Kubernetes or a distributed control plane.
- Multi-Node scheduling is an extension of the same contracts, not a separate product identity.
- If remote Nodes are unavailable, Ptah may run locally only when local feasibility and policy pass.
- Reduced distribution, capacity or isolation is reported honestly as degraded/unsatisfied; it is not silently equivalent.

---

# Consequences

## Positive

- Isolation strength is visible and policy-controlled.
- OCI implementations remain replaceable.
- gVisor, Kata and Firecracker have distinct roles instead of one vague sandbox label.
- Placement decisions are explainable and based on observed Node truth.
- Reservations and execution authority are fenced against stale workers.
- Distributed Ray workloads do not redefine Ptah Activities or Objects.
- Ptah works from one Node to future multi-Node deployments.
- Checkpoint and migration claims require compatibility and application proof.

## Costs

- More records and conformance tests are required.
- Stronger isolation increases startup, memory and operational complexity.
- Node capability snapshots must remain fresh.
- Secure networking, credentials and storage grants require dedicated infrastructure.
- Checkpoint portability will be limited and provider-specific.
- Cross-runtime behavior must be tested rather than assumed from OCI compatibility.

## Risks retained

- host kernel, hypervisor, firmware and hardware vulnerabilities;
- denial-of-service and noisy-neighbour behavior;
- device passthrough and shared-filesystem attack surfaces;
- misconfigured network or credential policy;
- runtime/guest/VMM supply-chain vulnerabilities;
- uncertain external side effects during crashes;
- distributed partitions and stale observations;
- incomplete checkpoint/application recovery.

These are explicit risk records, not hidden by a generic `sandboxed` label.

---

# Rejected alternatives

## One runtime for every workload

Rejected. Compatibility, risk, devices, performance and host support differ materially.

## Ray as the Ptah global scheduler and Activity runtime

Rejected. Ray assumes trusted code, has workload-local retry/object semantics and lacks Ptah proof, permission and durable identity boundaries.

## Rootless OCI as strong multi-tenant isolation

Rejected. It reduces privilege but shares the host kernel.

## gVisor as a universal replacement for OCI and VMs

Rejected. Compatibility and performance gaps require multiple classes.

## Kata or Firecracker made mandatory

Rejected. KVM/virtualization is not universal and their lifecycle/overhead is unnecessary for trusted lightweight work.

## Silent fallback to runc/native on failure

Rejected. This breaks the requested trust boundary.

## Checkpoint creation equals recovery

Rejected. Restore compatibility and application correctness require separate proof.

---

# Phase 0B requirements

Phase 0B must define schemas and conformance for:

1. Isolation Class and Runtime Provider;
2. Runtime Implementation/Variant;
3. Node Capability/Resource Snapshot;
4. Placement Request/Candidate/Decision;
5. Reservation and gang bundle;
6. Lease, generation and fence token;
7. Workload Instance and provider alias;
8. network, mount, credential and device grants;
9. Checkpoint Bundle and restore compatibility;
10. interruption, eviction, migration and rescheduling;
11. Ray/distributed Facility adapter;
12. runtime escalation/no-silent-weakening;
13. resource accounting and pressure;
14. health, vulnerability, upgrade and rollback;
15. golden cross-provider workload corpus.

No implementation is authorized by this ADR.

## Related evidence

- `donors/GVISOR.md`
- `donors/KATA-CONTAINERS.md`
- `donors/FIRECRACKER.md`
- `donors/YOUKI.md`
- `donors/CRUN.md`
- `donors/RAY.md`
- existing containerd/OCI, Node, Workspace, Activity, Object and checkpoint records
- `donors/MINIROUTER.md`
- `work-packages/PHASE-0A-WP11-ISOLATION-DISTRIBUTED-PLACEMENT.md`
