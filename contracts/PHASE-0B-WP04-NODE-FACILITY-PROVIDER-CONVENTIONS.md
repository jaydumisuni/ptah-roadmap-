# Phase 0B WP04 — Node, Facility, Provider, Capability and Health Conventions

**Status:** CANDIDATE DRAFT  
**Date:** 2026-07-19  
**Contract family target:** `ptah.runtime` / `ptah.facility` `0.1.0`  
**Implementation authorization:** NONE

## Purpose

Define the exact identities and truth boundaries required to register Nodes, publish Facilities, bind Provider implementations, observe resources/capabilities and decide whether one exact Provider Instance on one exact Node generation may receive work.

This record composes the frozen Node Protocol, Activity/Receipt, Object/storage and isolation/placement decisions without selecting a runtime, message bus, database, scheduler, container engine or deployment topology.

---

# 1. Required separation

Ptah keeps the following distinct:

```text
Node
Node Enrollment
Node Generation
Node Connection Epoch
Node Reachability Observation
Node Health Observation
Node Capability Snapshot
Node Resource Snapshot

Capability Definition
Capability Claim
Capability Verification
Capability Availability Projection

Facility
Facility Revision
Facility Instance

Provider
Provider Revision
Provider Instance
Provider Generation
Provider Reachability Observation
Provider Readiness Observation
Provider Health Observation
Provider Capability Snapshot

backend alias / endpoint / process ID / container ID
Activity / Operation / Attempt / Receipt
```

None of these records may be collapsed into one generic `status` or one mutable backend row.

---

# 2. Node identity and authority

## 2.1 Stable Node identity

`core.node` is the stable identity of one physical or virtual machine boundary contributing capabilities to Ptah.

A Node identity is not:

- hostname;
- IP address;
- MAC address;
- cloud instance ID;
- device serial alone;
- agent installation ID;
- connection/session ID;
- boot ID;
- certificate subject alone.

These remain scoped Aliases or evidence.

## 2.2 Enrollment

A Node becomes eligible only through an explicit enrollment record retaining:

```text
enrollment_id
node_ref
requestor_and_approver
organization_or_owner_scope
identity_evidence
attestation_or_key_refs
requested_roles
approved_roles
policy_revision
enrolled_at
expires_or_review_at
limitations
```

Reachability never implies enrollment, trust or authorization.

Enrollment states and Node lifecycle are separate. A rejected enrollment request does not create an active Node.

## 2.3 Node generation

`node_generation` is a monotonic incarnation counter under one stable Node identity.

It advances when the control/worker authority must fence prior execution context, including:

- agent reinstall or identity-key replacement;
- operating-system/runtime substrate replacement where prior authority is unsafe;
- restored machine image that could replay stale state;
- administrative forced fencing;
- machine replacement intentionally retaining the logical Node identity under approved migration.

Ordinary network reconnect does not necessarily advance Node generation.

## 2.4 Connection epoch

`connection_epoch` is a monotonic connection/reconciliation epoch for one Node generation.

It advances on reconnect or transport/session replacement and is used to reject late connection-scoped messages. It does not replace Node generation or Provider generation.

## 2.5 Lifecycle, reachability and health

Node lifecycle is durable administrative state:

```text
pending_enrollment
active
draining
suspended
retired
revoked
```

Node reachability is an observed projection:

```text
unknown
online
offline
stale
```

Node health is an observed assessment:

```text
unknown
healthy
degraded
unhealthy
```

A Node may be lifecycle `active`, reachability `offline`, and health `unknown` simultaneously. These facts are not contradictory and must not overwrite one another.

---

# 3. Capability truth

## 3.1 Capability Definition

`core.capability` defines one versioned capability vocabulary item and its evidence/conformance requirements.

Examples:

```text
process.execute
oci.run
browser.chromium.persistent_context
device.android.adb
storage.object.read
build.buildkit.solve
runtime.kvm
accelerator.cuda
```

A Capability Definition includes:

- stable capability key and version;
- input/output contract references;
- required operations;
- security/permission class;
- evidence requirements;
- compatibility dimensions;
- limitations and deprecation state.

Registration does not prove any Node or Provider supports the capability.

## 3.2 Capability Claim

A Capability Claim is one producer's assertion that a Node, Facility, Provider Revision or Provider Instance supports a capability under stated conditions.

Claims retain source, version range, configuration, limitations, evidence references and expiry.

Manifest declaration, installed binary presence and provider self-report are Claims—not verification.

## 3.3 Capability Verification

A Capability Verification is an immutable result under one frozen protocol over an exact subject revision/generation.

Verification states:

```text
unverified
verified
failed
inconclusive
stale
```

Verification must retain:

- exact subject and generations;
- Capability Definition/version;
- protocol/tool/build/configuration;
- Activity/Operation/Attempt/Receipts;
- observations and produced evidence;
- scope, limitations and expiry.

## 3.4 Capability availability

Current availability is a projection derived from:

- current Node/Provider lifecycle;
- reachability/readiness/health;
- current verified or policy-accepted capability evidence;
- resource availability and pressure;
- dependencies and grants;
- snapshot freshness;
- placement/organization policy.

Availability states:

```text
unknown
available
degraded
unavailable
blocked
```

Availability is not a durable capability claim and cannot rewrite historical verification.

---

# 4. Capability and resource snapshots

## 4.1 Node Capability Snapshot

A Node Capability Snapshot is immutable and binds to:

```text
node_ref
node_generation
connection_epoch
agent_revision
observed_at
valid_until
observation_and_receipt_refs
```

It may include:

- OS/kernel/architecture;
- virtualization and hypervisor support;
- cgroup, namespace, LSM and seccomp modes;
- CPU topology/features;
- memory/storage/network inventory;
- GPU/accelerator/device inventory;
- installed/eligible Provider Revisions;
- checkpoint compatibility groups;
- location/cost/failure-domain metadata;
- claimed and verified capability references;
- explicit unavailable/unsupported capabilities;
- limitations and observation errors.

Expired or stale snapshots cannot authorize new placement or dispatch.

## 4.2 Resource Snapshot

Resource truth keeps these dimensions separate:

```text
observed_total
administratively_allocatable
reserved
consumed
currently_available
pressure_or_headroom
overcommit_limit_and_policy
unavailable_or_quarantined
```

`currently_available` is derived and must not be accepted when arithmetic, freshness or reservation state is inconsistent.

Logical labels are scheduling Claims, not proof of physical capacity or exclusive reservation.

---

# 5. Facility contracts

## 5.1 Facility

`core.facility` is a stable neutral capability/service contract exposed to callers.

Examples:

- Process Facility;
- OCI Runtime Facility;
- Browser Facility;
- Storage Facility;
- Build Facility;
- Device Facility;
- Knowledge Facility.

Facility identity does not identify one implementation, plugin, process, Node or endpoint.

## 5.2 Facility Revision

An immutable Facility Revision retains:

```text
facility_ref
facility_contract_version
operation_definitions
input_output_schema_refs
capability_requirements
permission_classes
resource_budget_classes
network_credential_device_object_requirements
required_receipt_and_proof_domains
compatibility_ranges
deprecation_and_replacement
```

Breaking contract changes create a new Facility Revision/version and migration/compatibility record.

## 5.3 Facility Instance

A Facility Instance is one logical exposed binding of a Facility Revision in a scope.

It may be backed by one Provider Instance, several Provider Instances, a remote service or a routing adapter.

A Facility Instance retains:

- Facility Revision;
- Workspace/organization/global scope;
- Provider Instance bindings;
- routing/failover policy revision;
- permission/credential/network policy references;
- lifecycle and availability projection;
- endpoints as Aliases only.

Facility Instance is not Provider Instance and does not own provider process lifecycle.

---

# 6. Provider contracts

## 6.1 Provider

`runtime.provider` is the stable definition root for one Provider family/implementation line that can satisfy one or more Facility Revisions.

Examples include a Playwright Provider, containerd OCI Provider, local process Provider, R2 storage Provider or ADB Device Provider.

Provider identity survives running-instance replacement and endpoint movement.

## 6.2 Provider Revision

`runtime.provider_revision` is immutable and retains:

```text
provider_ref
provider_kind
implementation_name_and_version
binary_image_package_or_source_digest
build_and_configuration_digest
supported_facility_revisions
supported_capabilities
node_and_architecture_requirements
security_and_isolation_requirements
network_device_object_and_credential_requirements
checkpoint_or_recovery_capabilities
known_limitations
licence_and_provenance_refs
```

A Provider Revision may claim support; conformance verification remains separate.

## 6.3 Provider Instance

A Provider Instance is one deployed/running materialization of one Provider Revision on one exact Node generation or approved remote-service boundary.

It retains:

```text
provider_instance_id
provider_revision_ref
node_ref_or_remote_service_ref
node_generation
provider_generation
connection_epoch
process_service_or_workload_refs
endpoint_aliases
started_at
lifecycle
current_readiness_projection
current_health_projection
capability_snapshot_refs
```

## 6.4 Provider generation

`provider_generation` is monotonic under one Provider Instance identity and advances whenever prior execution authority, endpoints, workers or state must be fenced.

Restart, replacement, restore or forced reconciliation may advance Provider generation. A health probe does not.

Attempts and Receipts bind exact Provider generation. Late evidence from a stale generation is rejected or reconciled explicitly under WP02.

## 6.5 Provider lifecycle

Durable Provider Instance lifecycle:

```text
declared
starting
running
draining
stopping
stopped
retired
```

`failed` is an outcome/health observation, not an automatic replacement for lifecycle history. A failed start may remain lifecycle `stopped` with a failed Attempt and unhealthy observation.

## 6.6 Readiness, reachability and health

Provider reachability:

```text
unknown
reachable
unreachable
stale
```

Provider readiness:

```text
unknown
not_ready
ready
```

Provider health:

```text
unknown
healthy
degraded
unhealthy
```

Rules:

1. lifecycle `running` does not imply readiness;
2. heartbeat/reachability does not imply readiness;
3. readiness means declared dispatch preconditions currently pass under one readiness protocol;
4. readiness does not prove every advertised operation succeeds;
5. optional dependency failure may yield health `degraded` with a reduced capability snapshot;
6. draining prevents new ordinary assignments but permits bounded existing work, checkpointing and cleanup;
7. stale observations do not rewrite durable lifecycle or Activity truth.

---

# 7. Heartbeats and observations

Heartbeats are append-only or stream observations carrying:

- Node/Provider Instance references;
- Node/Provider generations and connection epoch;
- sequence and timestamps;
- reported lifecycle/readiness/health summaries;
- capability/resource snapshot references;
- producer identity and signature/attestation references.

A heartbeat proves only that an authenticated producer emitted the recorded observation. It does not prove:

- Node enrollment/trust;
- Provider readiness;
- capability conformance;
- free capacity;
- successful operation;
- current truth after its freshness deadline.

Projection freshness policy converts missing/late heartbeats to `stale` or `offline`; it does not fabricate provider failure or Activity failure.

---

# 8. Compatibility and dispatch eligibility

A Provider Instance may receive an Operation Attempt only when all required checks pass:

1. Node lifecycle/trust/authorization are eligible;
2. Node and Provider generation/connection epoch are current;
3. required Capability Snapshot and Verification are current;
4. Provider lifecycle is `running` and readiness is `ready`;
5. health/degradation policy allows the exact operation;
6. Facility Revision and Provider Revision compatibility range matches;
7. resource/reservation requirements pass;
8. isolation, network, Object, device and credential requirements pass;
9. Node/Provider is not draining, suspended, retired or revoked;
10. policy/audience/location/licence restrictions pass.

Dispatch eligibility is a decision/result record or Receipt-backed projection. It is not stored as a permanent capability.

---

# 9. Dependencies and degraded operation

Facility/Provider manifests classify dependencies:

```text
required
optional
operation_specific
proof_only
```

Each dependency records capability/version, endpoint/Provider reference, credentials/network needs and failure behavior.

Rules:

- required dependency failure makes affected operations not ready;
- optional dependency failure removes or degrades only the dependent capability;
- operation-specific dependency failure does not make unrelated operations unavailable;
- proof-only dependency failure may allow execution but blocks the stronger proof/acceptance level;
- UI/API must expose the reduced capability and limitation;
- no dependency failure may be hidden behind generic `healthy`.

---

# 10. Credentials, network, devices and Objects

Manifests contain requirements and opaque references—not credential values or arbitrary host paths.

Runtime delivery is scoped to exact:

- Facility/Provider Instance;
- Node/Provider/workload generation;
- Activity/Operation/Attempt;
- destination and operation;
- lifetime/lease;
- audience and policy.

Revocation occurs on expiry, lease loss, suspension, stop, retirement, replacement or policy action.

Provider-private host paths, sockets and control-plane endpoints remain backend details and never become public canonical identity.

---

# 11. Replacement, failover and reconciliation

Provider/backend replacement:

1. preserves Facility and caller contract identity;
2. creates or selects a compatible Provider Revision/Instance;
3. advances Provider generation where the same Instance identity is retained;
4. receives a new connection epoch/endpoints;
5. fences stale Attempts and Receipts;
6. re-runs readiness/capability verification;
7. preserves earlier lifecycle/health/failure evidence;
8. does not claim state/checkpoint portability without explicit compatibility proof.

Node replacement retaining logical Node identity requires explicit migration authority and advances Node generation. Otherwise a new Node identity is created.

---

# 12. Migration and compatibility rules

Migration must not:

- treat hostname/IP/cloud instance ID as Node identity;
- mark reachable Nodes enrolled/trusted;
- carry stale capability snapshots into a new Node or Provider generation;
- collapse total/allocatable/reserved/available resources;
- turn installed-binary claims into verified capabilities;
- merge Facility and Provider identity;
- turn heartbeat into readiness or operation proof;
- reuse Provider generation after restart/replacement;
- hide optional dependency loss;
- embed raw secrets or backend-private paths/endpoints;
- silently weaken isolation/security requirements.

Compatibility is directional and operation-specific. A Provider supporting Facility revision `A` does not automatically support later revision `B`.

---

# 13. Required conformance cases

1. Node reconnect keeps Node identity and generation but advances connection epoch.
2. Node authority replacement advances Node generation and rejects stale worker evidence.
3. reachable unapproved Node remains ineligible.
4. expired Capability Snapshot cannot authorize placement/dispatch.
5. declared GPU/device/runtime capability remains unverified until protocol evidence exists.
6. total, allocatable, reserved, consumed and available resources remain arithmetically consistent.
7. Facility identity survives Provider implementation replacement.
8. Provider restart advances Provider generation and fences stale Attempts/Receipts.
9. lifecycle `running` with readiness `not_ready` remains valid and ineligible.
10. heartbeat/reachability cannot satisfy readiness or operation proof.
11. optional dependency outage yields explicit degraded/reduced capability.
12. draining rejects new work while permitting bounded cleanup/checkpoint actions.
13. Node/Provider stale/offline observation does not fabricate Activity failure.
14. secret values and backend-private paths are absent from public manifests/records.
15. local and remote Providers implement the same canonical Facility/Provider contracts.

---

# Do-not-break rule

> Never collapse stable Node/Facility/Provider identity, generation/connection epoch, lifecycle, reachability, readiness, health, capability evidence, resource truth or backend alias into one record or one status. A heartbeat, installed binary, manifest claim or successful process start never proves readiness, capability conformance, free capacity or successful operation.
