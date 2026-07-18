# Phase 0A — WP11 Strong Isolation and Distributed Placement/Scheduling Composition

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Runtime code:** NOT STARTED

## Purpose

Close the remaining v1 architecture gap between:

- an ordinary local/OCI Workspace;
- permission-scoped lightweight Tool execution;
- stronger syscall isolation;
- VM-backed container isolation;
- standalone microVM/full-VM isolation;
- one-Node execution;
- secure multi-Node placement;
- distributed Python/AI workloads;
- interruption, rescheduling and checkpoint recovery.

WP11 does not select one universal runtime or one universal scheduler. It defines the Ptah-owned contracts that allow several runtimes and placement backends to coexist without changing Workspace, Activity, Object, Package or caller identity.

## Evidence recovered

### Existing Ptah foundations

- `decisions/ADR-0001-NODE-WORKSPACE-BOUNDARY.md`
- `decisions/ADR-0003-ACTIVITY-EVENT-OBSERVABILITY-BOUNDARY.md`
- `decisions/ADR-0004-OPERATION-RECEIPTS-PROOF-LEVELS.md`
- `decisions/ADR-0006-STORAGE-TRANSFER-SYNC-BOUNDARY.md`
- `decisions/ADR-0009-DEVICE-SESSION-DISPLAY-INPUT-SEMANTIC-UI-BOUNDARY.md`
- `work-packages/PHASE-0A-WP02A-WORKSPACE-EXECUTION-COMPOSITION.md`
- `work-packages/PHASE-0A-WP02C-INTERNAL-CORE-RUNTIME-RECOVERY.md`
- `donors/CONTAINERD-OCI.md`

These foundations already establish:

- Node identity is separate from connection identity and connection epoch;
- a Node can expose several Workspace Providers and Facilities;
- Workspace identity survives Provider replacement;
- Provider operations are durable Activities;
- Activity, operation, attempt, nonce, Event, telemetry, Receipt and proof remain separate;
- side-effect retries require idempotency/fencing evidence;
- Object transfer and large streams remain outside ordinary control messages;
- provider snapshots/checkpoints are runtime references, not universal Session truth;
- physical Devices and other scarce resources use leases and fencing;
- offline Nodes retain local journals and reconcile on reconnect.

### External donor records

- `donors/GVISOR.md`
- `donors/KATA-CONTAINERS.md`
- `donors/FIRECRACKER.md`
- `donors/YOUKI.md`
- `donors/CRUN.md`
- `donors/RAY.md`
- `donors/MINIROUTER.md`

### Internal THETECHGUY completion evidence

- `internal/THETECHGUY-NODE-WORKER-RESOURCE-PLACEMENT.md`
- `internal/TECHGUY-RELAY.md`
- `internal/SOFTWARE-BUILDER.md`
- `internal/HUNTER-RUNTIME-SYNC.md`
- `internal/HUNTER-AGENTOPS.md`
- `internal/MIBU.md`

## Composite result

```text
Ptah-owned identities and contracts
  Node / Node connection epoch / capability snapshot
  Workspace / Workspace Provider / Provider profile
  Isolation Class / threat profile / escalation decision
  Activity / operation / attempt / Receipt
  Resource Request / Reservation / Lease / Fence
  Placement Request / Candidate / Decision / Run
  Object locality / transfer / mount / credential grant
  Checkpoint / snapshot bundle / restore attempt
  scheduler policy reference / caller policy reference

Baseline execution machinery
  containerd + OCI
    image, content, bundle, container, Task and snapshot substrate

Low-level baseline OCI implementations
  runc / crun / youki
    replaceable implementations beneath one baseline OCI Provider contract

Permission-scoped lightweight Tools
  Deno
    explicit filesystem/network/environment/run permissions for compatible scripts

Stronger-container isolation
  gVisor / runsc
    userspace application kernel between ordinary OCI and VM-backed isolation

VM-backed container isolation
  Kata Containers
    dedicated guest kernel/VM while retaining container/Pod operational model

Standalone microVM isolation
  Firecracker
    one-process/one-microVM high-isolation Provider with Ptah-owned guest lifecycle

Full VM and specialist Providers
  QEMU/libvirt/platform-native/remote managed Providers
    broader compatibility, OS and device classes where needed

Distributed computation and placement backend
  Ray
    optional Python/AI Task, Actor, logical-resource and Placement Group Facility

Durable orchestration and event machinery
  Temporal + NATS/JetStream + local Node journal
    Activity recovery, live events and intermittent-Node reconciliation

Optional routing/evaluation workload
  MiniRouter
    study-only workload; not Ptah scheduler or reasoning authority
```

No donor is Ptah's universal execution or scheduling truth.

---

# 1. Mandatory separation of layers

WP11 closes five frequently collapsed layers as separate contracts.

## 1.1 Runtime implementation

Examples:

- runc;
- crun;
- youki;
- runsc;
- Kata runtime plus selected VMM;
- standalone Firecracker;
- QEMU/libvirt;
- Deno.

A binary/runtime implementation is replaceable adapter metadata.

## 1.2 Isolation Class

An Isolation Class describes the security and compatibility guarantees required by a workload. It is not a runtime name.

## 1.3 Workspace/Execution Provider

The Provider owns lifecycle operations on one Node using one runtime/component profile.

## 1.4 Placement and reservation

Placement decides where an Activity attempt may run and reserves the required resources. It does not execute the workload or prove its result.

## 1.5 Caller policy and reasoning

The caller supplies intent, priorities, budget, privacy, allowed regions/Nodes, minimum isolation, acceptance and trade-offs. Ptah mechanically evaluates and enforces these declared constraints.

Ptah does not invent company priority, select a preferred model for Hunter, waive isolation, spend money or accept a result without caller policy.

---

# 2. Isolation Class model

## 2.1 Class family

Phase 0B must support a neutral family capable of representing at least:

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

The family is not a claim that every class forms one perfectly linear security scale. Each class has different compatibility, host-surface, startup, checkpoint and device characteristics.

## 2.2 Initial implementation direction

### `trusted_host_process`

- native/local process Provider;
- only for trusted platform-controlled code;
- ordinary host permissions, namespaces and process controls apply;
- never used for unknown third-party code merely for speed.

### `permission_scoped_script`

- Deno is the primary lightweight candidate;
- suitable for approved JavaScript/TypeScript without native/FFI/broad subprocess requirements;
- explicit filesystem, network, environment and process permissions;
- permission prompts or flags are not hostile-code containment against runtime/compiler/kernel compromise.

### `baseline_oci`

- containerd/OCI is the substrate direction;
- runc, crun and youki are replaceable low-level implementations;
- shares the host kernel;
- rootless is a privilege mode, not a stronger Isolation Class;
- suited to trusted or policy-approved container workloads.

### `userspace_kernel_oci`

- gVisor/runsc is the primary candidate;
- Systrap and KVM are separate Provider profiles;
- reduces direct exposure to host Linux syscalls;
- compatibility/performance gaps are expected and explicit;
- host cgroups, network policy, mounts, credentials and data scope remain external controls.

### `vm_backed_container`

- Kata Containers is the primary candidate;
- each mutually untrusted tenant/workload receives a separate VM sandbox unless shared trust is explicit;
- Dragonball integrated mode and QEMU/Cloud Hypervisor/Firecracker external modes are distinct profiles;
- guest kernel/image/agent/VMM/shared-filesystem/network/device component set is pinned.

### `standalone_microvm`

- Firecracker is the primary candidate;
- intended for one-workload-per-microVM, function-like, disposable or specially controlled high-risk work;
- requires Ptah-owned guest image, bootstrap/agent, TAP/network policy, block storage, Jailer and result/Receipt handling;
- snapshots remain operator-managed compatibility-sensitive Artifacts.

### `full_virtual_machine`

- broad OS/device/application compatibility;
- QEMU/libvirt and platform-specific VM Providers remain candidates from application-runtime work;
- higher overhead, broader virtual hardware and stronger compatibility than minimal microVMs;
- required where Windows/macOS/legacy kernel/device behavior or full-machine state is needed.

### specialist/physical Providers

- remote managed sandboxes, Android/iOS Devices, emulators, attached repair hardware and future accelerators remain separate Provider classes;
- they use the same Activity, lease, placement and evidence contracts but declare non-migratable or externally authoritative state explicitly.

## 2.3 Runtime profile

Each usable Provider profile records at minimum:

```text
provider_profile_id
provider_family
isolation_class
runtime_implementation
runtime_version
runtime_build_digest
component_set_id
host_platform_constraints
guest_platform_constraints
architecture_constraints
kernel_or_guest_image_references
vmm_or_platform_mode
rootless_or_privilege_mode
filesystem_mode
network_mode
seccomp_lsm_policy_reference
device_and_accelerator_policy
checkpoint_capabilities
known_compatibility_profile
known_limitations
security_advisory_state
health_check_recipe
conformance_suite_revision
```

The profile is versioned. A runtime upgrade or VMM/guest-image change creates a new profile revision.

## 2.4 Isolation request

A caller/Package/Facility may declare:

```text
minimum_isolation_class
allowed_isolation_classes
forbidden_runtime_features
requires_native_or_ffi
requires_kernel_features
requires_device_or_gpu
requires_network
requires_credentials
requires_mutable_mounts
requires_checkpoint
performance_or_latency_class
break_glass_policy_reference
```

## 2.5 No silent downgrade

When the preferred runtime is unavailable or incompatible:

1. the current class fails with an exact reason;
2. Ptah may evaluate an equal or stronger approved alternative;
3. any weaker alternative requires explicit caller/deployment policy and a receipted decision;
4. Ptah never silently falls back from gVisor/Kata/microVM to baseline OCI or host process;
5. unsupported GPU, device, checkpoint or confidential-computing paths remain unsupported rather than simulated through labels.

## 2.6 Risk inputs

Isolation selection considers declared and observed evidence including:

- source and publisher trust;
- executes-code status;
- native binary/FFI/JIT/compiler behavior;
- subprocess/shell use;
- filesystem write scope;
- credential access;
- network/open-world access;
- untrusted web/email/message input;
- device/USB/GPU/VFIO access;
- kernel/syscall/ioctl requirements;
- cross-tenant data exposure;
- persistence and service lifetime;
- destructive or physical side effects;
- vulnerability/scan/provenance evidence;
- required startup/latency/cost;
- compatibility and checkpoint requirements.

Registry trust or a clean scan is one evidence input, not a permission to select a weak class.

---

# 3. Node capability and resource snapshots

## 3.1 Stable Node versus observed instance

Ptah retains:

```text
node_id
node_instance_id
connection_id
connection_epoch
provider_worker_generation
```

- `node_id` is stable identity;
- instance and connection records describe current runtime presence;
- connection epochs reject stale commands/events/Receipts;
- worker generation rejects output from superseded Provider processes.

## 3.2 Capability Snapshot

A versioned immutable snapshot records observed facts at one time:

```text
capability_snapshot_id
node_id
node_instance_id
captured_at
source_and_attestation
os_distribution_and_version
kernel_version
architecture
cpu_model_features_and_topology
virtualization_kvm_and_nested_support
cgroup_version_and_controllers
namespaces_seccomp_lsm_iommu
installed_runtime_profiles
filesystem_snapshotters
network_providers_and_interfaces
storage_classes_and_mount_health
accelerators_devices_and_drivers
confidential_compute_features
attached_physical_devices
available_facilities_and_toolchains
checkpoint_restore_profiles
security_patch_and_advisory_state
limitations
expires_or_refresh_after
```

Capabilities are observations/claims with time/source, not timeless truth.

## 3.3 Resource Snapshot

Capacity and pressure remain separate from compatibility:

```text
resource_snapshot_id
node_id
captured_at
configured_capacity
hard_capacity
allocatable_capacity
reserved_capacity
leased_capacity
observed_usage
pressure_and_health
overcommit_policy
hard_enforcement_mechanism
accounting_source
```

Resource dimensions include:

- CPU quantity/topology/affinity;
- RAM and swap;
- local storage by class, free space, IOPS and bandwidth;
- network bandwidth/latency/egress class;
- GPU/accelerator quantity, model, memory and driver/runtime;
- attached Devices/ports/interfaces;
- runtime slots or concurrency limits;
- energy/cost/region/failure-domain metadata where applicable.

## 3.4 Logical versus enforced resources

- Ray/queue logical resource labels express scheduling demand;
- Provider/cgroup/VM/device controls enforce hard limits;
- configured capacity is not current availability;
- reservation is not observed usage;
- observed usage does not prove a hard limit exists;
- GPU visibility variables are not complete device isolation;
- every Placement Receipt states which resources were logically reserved and which were physically enforced.

---

# 4. Placement, reservation, lease and fencing model

## 4.1 Placement Request

Every placed Activity attempt references a versioned request:

```text
placement_request_id
activity_id
operation_id
workspace_id
caller_policy_reference
requested_provider_family
minimum_isolation_class
resource_bundle
platform_and_architecture_constraints
required_facilities_and_tools
required_objects_and_data_locality
required_devices_or_accelerators
credential_and_network_requirements
failure_domain_and_locality_rules
latency_deadline_and_duration
cost_or_budget_constraints
checkpoint_preemption_and_retry_policy
allowed_nodes_or_regions
forbidden_nodes_or_regions
created_at
```

## 4.2 Candidate evaluation

Each candidate Node/Provider produces an immutable evaluation:

```text
placement_candidate_id
placement_request_id
node_id
capability_snapshot_id
resource_snapshot_id
provider_profile_id
compatible
hard_rejection_reasons
missing_capabilities
transfer_requirements
credential_delivery_possible
network_policy_possible
estimated_start_and_transfer_cost
resource_and_failure_domain_score
limitations
```

Rejected candidates remain evidence. A score never overrides a hard constraint.

## 4.3 Placement Decision

```text
placement_decision_id
placement_request_id
selected_candidate_id
decision_engine_and_version
caller_policy_reference
constraints_satisfied
tradeoffs_applied
fallback_or_escalation_reference
decided_at
expires_at
```

The decision explains the mechanical match. Business priority, acceptance and spend authority remain caller-owned.

## 4.4 Resource Reservation

A reservation is an expiring claim on a resource bundle before execution:

```text
reservation_id
placement_decision_id
node_id
provider_profile_id
resource_bundle
holder_activity_and_attempt
issued_at
expires_at
generation
state
release_receipt
```

States include:

```text
requested
pending
reserved
partially_reserved
infeasible
expired
consumed
releasing
released
failed
```

Partial reservation is not gang success.

## 4.5 Lease and fencing

A lease grants time-bounded authority to mutate or exclusively control a resource:

```text
lease_id
resource_identity
holder_activity_attempt
capability_scope
mode
issued_at
expires_at
lease_generation
fencing_token
renewal_state
cleanup_recipe_reference
state
```

Every mutating Provider, Device, cache-writer, volume-writer or singleton-service operation presents the current fencing token.

A stale worker may continue computing, but cannot commit authoritative state after its lease is superseded.

## 4.6 Worker Claim

Dispatch creates a worker claim linked to one attempt:

```text
worker_claim_id
activity_id
operation_id
attempt_id
node_id
provider_worker_generation
reservation_ids
lease_ids
claim_time
heartbeat_deadline
fencing_tokens
state
```

Loss of heartbeat makes the claim suspect/expired; it does not prove the operation did or did not take effect.

## 4.7 Gang and topology scheduling

Distributed workloads may request multiple bundles with:

- all-or-nothing reservation;
- PACK, SPREAD or strict locality/failure-domain rules;
- accelerator topology;
- same-Node/shared-memory constraints;
- anti-affinity;
- data-shard locality;
- minimum/maximum worker count for elastic workloads.

Ray Placement Groups may implement selected Python/AI reservations, but Ptah retains Reservation identity, deadline, permissions and release proof.

---

# 5. Scheduler boundary

## 5.1 Ptah placement engine

Ptah requires a backend-neutral placement engine that:

- filters hard incompatibilities;
- evaluates current snapshots;
- accounts for reservations/leases;
- plans required Object transfer and credential/network setup;
- emits candidate rejection and selected-decision evidence;
- supports local one-Node operation;
- can delegate selected workloads to Ray or future schedulers.

The first implementation may be a small SQL-backed scheduler. It must preserve the final contracts and migration path.

## 5.2 What Ray may own

- Python Tasks and Actors;
- logical resource requests;
- Placement Groups and distributed worker launch;
- distributed immutable-object transport/cache;
- workload retries/reconstruction where permitted;
- Ray-level state and metrics.

## 5.3 What Ray does not own

- canonical Ptah Activity/attempt identity;
- hard resource isolation;
- mutually untrusted tenant boundaries;
- caller priority or spend policy;
- credential/Object permissions;
- external side-effect idempotency;
- durable cross-backend Activity truth;
- Node admission and security posture;
- acceptance or proof.

## 5.4 MiniRouter boundary

MiniRouter is an optional future model-routing/evaluation workload. It may produce Routing Policy and Evaluation Artifacts under exact model/provider/benchmark revisions.

It is not:

- the Ptah scheduler;
- the Node placement engine;
- Hunter's reasoning authority;
- a licensed source dependency at the inspected repository state.

---

# 6. Data locality, transfer and mounts

## 6.1 Locality inputs

Placement evaluates:

- immutable required Objects already verified on a Node;
- mutable Workspace revision ownership;
- package/toolchain/model/cache locations;
- database/service endpoints;
- attached physical Devices;
- volume/snapshot location;
- region/privacy constraints;
- transfer size, bandwidth and time;
- object-replica health.

## 6.2 Transfer Plan

When data is absent, Ptah creates explicit Transfer Activities before execution. The Placement does not assume bytes appeared merely because metadata references them.

A transfer plan records:

```text
required_object_or_revision
source_location
destination_location
transfer_activity_id
expected_digest
mount_or_copy_mode
read_only_or_mutable
verification_required
cleanup_or_cache_policy
```

## 6.3 Mutable Workspace placement

- one online writer lease can reduce conflicts;
- offline divergence remains possible and creates revisions/conflicts;
- moving a mutable Workspace requires a frozen revision, provider snapshot or explicit reconciliation plan;
- no important mutable tree is moved through silent last-write-wins;
- Provider volumes remain runtime state until represented by revisions/checkpoints.

## 6.4 Cache locality

Shared caches/toolchains can influence placement, but:

- cache is derived and replaceable;
- cache integrity and writer ownership are explicit;
- a cache hit does not become source or Artifact proof;
- mutually untrusted Workspaces do not receive uncontrolled shared writable caches.

## 6.5 Device locality

A physical Device is anchored to the Node/Provider currently exposing its valid interface. Work requiring that Device moves to that Node or is rejected; the scheduler does not pretend the Device is migratable.

---

# 7. Secure network and credential placement

## 7.1 Network Policy

Each attempt receives a referenced policy defining:

- network namespace/provider;
- allowed ingress and exposed services;
- allowed egress destinations/ports/protocols;
- DNS and private-network rules;
- proxy/tunnel requirements;
- metadata-service access;
- bandwidth/rate limits;
- public-address disclosure policy;
- audit/evidence requirements.

Runtime availability does not imply open network authority.

## 7.2 Node connection security

- temporary pairing is only bootstrap;
- stable cryptographic Node identity and revocable credentials are required;
- secure tunnels or authenticated connections replace public host/port disclosure;
- connection epoch and replay cursors reject stale traffic;
- capability reports and Receipts identify producer version/instance.

## 7.3 Credential Grant

Credentials remain opaque references. Placement creates a short-lived grant:

```text
credential_grant_id
credential_reference
workspace_id
activity_id
attempt_id
node_id
provider_id
facility_id
allowed_use
issued_at
expires_at
revocation_state
materialization_method
redaction_and_audit_class
```

- grants are least privilege and attempt-scoped;
- placement verifies the selected Node/Provider can deliver them safely;
- ambient host credentials are not inherited by default;
- expiration/revocation follows attempt completion or cancellation;
- secrets never enter capability snapshots, logs or ordinary Receipts.

## 7.4 High-risk interfaces

VFIO, GPU, USB, raw sockets, host networking, host PID namespace, broad host mounts, directfs, FFI and privileged containers require distinct capability/permission records and normally trigger a stronger class or explicit exception.

---

# 8. Interruption, retry, checkpoint, rescheduling and migration

## 8.1 Separate recovery mechanisms

Ptah distinguishes:

- retry from original inputs;
- Activity-level logical checkpoint;
- application checkpoint;
- filesystem/Workspace revision;
- container/VM/provider snapshot;
- process-memory checkpoint;
- Session archive/export;
- replica transfer;
- migration to another Node.

No one mechanism implies the others.

## 8.2 Checkpoint Capability

Provider profiles declare exact support:

```text
none
application_only
filesystem_revision
container_criu
provider_snapshot
microvm_full_snapshot
microvm_differential_snapshot
vm_snapshot
custom_device_checkpoint
```

Capability includes compatible runtime/profile/component/hardware ranges and known unsupported state.

## 8.3 Checkpoint record

```text
checkpoint_id
workspace_id
activity_id
operation_and_attempt
provider_profile_id
node_and_capability_snapshot
checkpoint_kind
source_revision_ids
memory_state_artifact
machine_or_process_state_artifact
volume_or_disk_artifacts
network_and_external_state
credential_and_secret_class
created_at
integrity_and_encryption
application_quiesce_receipts
compatibility_profile
limitations
restore_test_state
```

A checkpoint command completing proves only checkpoint creation at its stated level.

## 8.4 Restore attempt

- restore is a new Activity attempt and Provider generation;
- compatibility is checked before placement;
- restored process/VM start is not application readiness;
- external sockets, leases, credentials, identity, entropy and network state may require renewal;
- application/read-back proof is required before the restored attempt becomes ready;
- stale prior workers remain fenced.

## 8.5 Retry and side effects

- pure/idempotent work may restart from source or checkpoint;
- retry-safe classification is explicit;
- external/physical/destructive side effects require operation-level idempotency or proof the previous attempt did not apply;
- a lost Node creates `unknown`/`recovering` state until authoritative reconciliation;
- duplicate results are retained and one accepted result is selected through caller policy/proof, not silently overwritten.

## 8.6 Preemption

An Activity is preemptible only when its policy declares a safe path:

- restart from original inputs;
- resume from a validated checkpoint;
- compensate a prior side effect;
- pause at an application-defined boundary.

Otherwise resource pressure may reject new placement but does not kill non-preemptible work without a caller/emergency policy.

## 8.7 Migration

Migration is not universal. It requires:

- compatible target Node/Provider profile;
- transferred/verified Objects and mutable revision state;
- checkpoint compatibility;
- renewed network/credential/device leases;
- a new attempt/generation;
- source shutdown/fencing;
- target readiness/read-back proof;
- explicit partial/failed migration state.

Physical Devices and some provider/service states remain non-migratable.

---

# 9. One-Node and multi-Node operation

## 9.1 One-Node is complete

A single Linux Node must support the first vertical slice using the same contracts:

- local placement engine;
- local SQL catalogue/Activity Ledger;
- local OCI Provider;
- local Object store/cache;
- local journal/outbox;
- no Ray or distributed scheduler required.

The absence of multiple Nodes is not an error or unsupported architecture.

## 9.2 Multi-Node extension

Adding Nodes introduces:

- capability/resource snapshots;
- Placement Requests/Candidates/Decisions;
- reservations and leases;
- secure Node identity/networking;
- Object/data transfer and locality;
- failure domains;
- drain/reschedule behavior;
- optional Ray/distributed Facilities.

It does not change canonical Workspace, Activity, Object, Package or Session identities.

## 9.3 Intermittent Nodes

A Node may be:

```text
online
suspect
disconnected
offline_permitted
draining
maintenance
quarantined
retired
```

Local permitted work journals state and reconciles later. Placement never dispatches new remote work to a disconnected/suspect Node without an explicit offline plan.

## 9.4 Degraded fallback

When the preferred distributed path is unavailable:

- independent compatible Activities may run locally;
- gang/distributed work remains pending, rejects or uses an approved smaller mode;
- isolation cannot silently weaken;
- required data/Device/credential constraints remain enforced;
- the degraded decision and lost capabilities are explicit.

---

# 10. Failure domains and lifecycle

## 10.1 Distinct failures

```text
node_connection_failure
node_host_failure
provider_runtime_failure
worker_failure
reservation_failure
lease_expired
fence_rejected
resource_pressure
network_policy_failure
credential_delivery_failure
object_transfer_failure
checkpoint_failure
restore_incompatible
restore_runtime_failure
scheduler_backend_failure
ray_cluster_failure
control_plane_failure
```

Each maps to an Activity/Placement state without collapsing unrelated work.

## 10.2 Node drain

Drain is an Activity that:

1. stops new placements;
2. inventories active reservations/leases/attempts;
3. classifies restart/checkpoint/non-preemptible state;
4. moves or completes work according to policy;
5. transfers required Objects/checkpoints;
6. verifies destination readiness;
7. releases resources and revokes credentials;
8. records unresolved/stranded work;
9. changes Node lifecycle only after Receipts.

## 10.3 Provider/runtime upgrade

- new runtime/component profile is staged beside the old profile;
- golden conformance and security tests run;
- active Workspaces are not silently migrated;
- checkpoint compatibility is tested explicitly;
- rollback remains available while retained state depends on the old profile;
- vulnerability urgency can quarantine new placement while preserving honest active-work status.

---

# 11. Observability, accounting and proof

Every placement/run correlates:

- Activity/operation/attempt;
- Node and connection epoch;
- capability/resource snapshots;
- Provider/runtime profile;
- Placement Request/Candidate/Decision;
- reservations, leases and fencing tokens;
- Object transfers/mounts;
- credential/network grants;
- resource accounting;
- checkpoint/restore references;
- output Objects/Artifacts;
- limitations and rejected candidates.

Operational telemetry may be sampled. Placement, lease, fence, side-effect and proof-critical Receipts remain durable and unsampled.

Cost/accounting may record:

- requested/reserved/used CPU time;
- RAM/time;
- local/object storage;
- network transfer;
- accelerator time;
- provider/API cost;
- energy class where available;
- wasted/retried/preempted work.

Cost evidence does not authorize spending; caller policy does.

---

# 12. Requirement closure verdict

## `ISOLATION-001` — CLOSED FOR PHASE 0B CONTRACT DESIGN

Closed direction:

- isolation is a Ptah class/profile contract, not a runtime name;
- baseline OCI remains host-kernel isolation with runc/crun/youki alternatives;
- gVisor is the primary stronger-container candidate;
- Kata is the primary VM-backed container candidate;
- Firecracker is the primary standalone microVM candidate;
- full VM/specialist Providers remain available for broader compatibility;
- no silent isolation downgrade;
- network, credentials, mounts, devices, cgroups and data permissions remain separate controls;
- checkpoint support is profile-specific and proof-dependent.

## `DIST-001` — CLOSED FOR PHASE 0B CONTRACT DESIGN

Closed direction:

- stable Node identity, connection epochs, capability snapshots and Provider generations;
- explicit Placement Request, Candidate, Decision, Resource Reservation, Lease, Fence and Worker Claim;
- hard constraints precede scoring;
- logical scheduler resources remain separate from physical enforcement;
- locality, transfer, Devices, credentials, privacy, cost and failure domains are placement inputs;
- one-Node execution is complete and uses the same contracts;
- Ray is an optional distributed Python/AI Facility, not the universal scheduler or trust boundary;
- caller policy owns priority, spend and acceptance;
- Activity retry/checkpoint/reschedule preserves attempts and side-effect fencing;
- backend/runtime replacement preserves canonical identities.

## Related foundations extended

- `CORE-005` Node capability reporting;
- `CORE-001` Workspace Provider selection;
- `CORE-002` Activity attempts/recovery;
- `EXEC-002` OCI Provider;
- `SESSION-001` checkpoint/restore compatibility;
- `STORE/XFER/SYNC` locality and migration;
- `DEVICE-001/002` anchored resources and leases;
- `PLUGIN-001` risk-based runtime activation;
- `OBS-001` resource/placement accounting;
- `OFFLINE-001` local one-Node and intermittent operation.

No runtime, scheduler, placement engine or distributed cluster implementation is authorized by this closure.

---

# 13. Phase 0B contracts required

1. Isolation Class and threat-profile schema.
2. Runtime/Provider Profile and component-set schema.
3. Node Instance, connection epoch and Capability Snapshot schema.
4. Resource Snapshot and hard-enforcement evidence schema.
5. Placement Request, Candidate and Decision schema.
6. Resource Reservation, Lease, Fence and Worker Claim schema.
7. network policy, service endpoint and secure Node connection schema.
8. Credential Grant/materialization/revocation schema.
9. Object locality, transfer and mount plan schema.
10. Checkpoint Capability, Checkpoint and Restore Attempt schema.
11. preemption, drain, migration and degraded-fallback state families.
12. Ray/other scheduler adapter contract.
13. resource/cost/accounting semantic conventions.
14. runtime/scheduler conformance and replacement corpus.

---

# 14. Required proof before freeze

1. Run one workload under baseline OCI, gVisor and Kata/Firecracker profiles without changing Workspace/Activity/Object identity.
2. Attempt an unsupported feature and prove there is no silent downgrade.
3. Compare runc, crun and youki lifecycle, resource, signal, seccomp and state behavior.
4. Reject a Node lacking required KVM, architecture, driver, tool or runtime capability.
5. Generate capability/resource snapshots and invalidate stale snapshots after Node/runtime change.
6. Reserve CPU/RAM/storage/GPU bundles and prove hard limits independently from logical scheduler labels.
7. Expire a worker lease, issue a new fencing token and reject the stale worker's output.
8. Create all-or-nothing gang reservations and expose pending/infeasible/deadline states.
9. Place one Activity by data locality and another by attached Device locality.
10. Transfer and verify required Objects before execution; never run from metadata-only presence.
11. Deliver an attempt-scoped credential and revoke it after completion/cancellation.
12. Enforce egress/private-network/metadata-service policy independently of runtime networking.
13. Kill a Node during retry-safe work and resume with a new attempt without duplicate side effects.
14. Lose a Node during an ambiguous external side effect and retain `unknown/recovering` until authoritative reconciliation.
15. Create and restore profile-specific checkpoints and reject incompatible targets.
16. Prove restored process/VM start remains separate from application-ready/read-back proof.
17. Drain a Node containing restartable, checkpointable and non-preemptible work and retain each outcome.
18. Run a distributed Ray workload while Ptah remains canonical for Activities, permissions and hard limits.
19. Isolate mutually untrusted Ray workloads in separate clusters/Workspace Providers.
20. Disable Ray/distributed placement and complete compatible work on one local Node with unchanged identities.
21. Replace one OCI runtime and one scheduler backend through golden conformance without changing public identities.
22. Retain rejected placement candidates, limitations, resource usage and proof-critical Receipts.

## Closure conclusion

Ptah now has a complete design direction from lightweight trusted execution through strong VM-backed isolation and from one-Node operation through secure multi-Node placement. Runtime strength, compatibility, hard resource controls, placement, caller policy and proof remain distinct. The next phase may design exact schemas and conformance tests; implementation remains prohibited until Phase 0C approves the first vertical slice.
