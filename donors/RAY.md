# Donor Record — Ray

**Phase:** 0A / WP11  
**Status:** FIRST-PASS COMPLETE — PRIMARY DISTRIBUTED TASK/ACTOR AND PLACEMENT WORKLOAD DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/ray-project/ray
- Owner/organisation: `ray-project`
- Default branch: `master`
- Pinned commit: `bed46a1379d13830b314ec7ef0a924d9b42093a7`
- Licence: Apache-2.0
- Activity: Active
- Primary language/runtime: Python-facing distributed framework with native runtime components
- Classification: distributed task, actor, immutable-object, gang-placement, autoscaling and AI-compute workload donor
- Ptah targets: `DIST-001`, distributed execution Facilities, resource-aware placement, gang reservations, locality, retries, cancellation, state/attempt visibility and cluster workload composition

## Files/components inspected

- `README.rst`
- `LICENSE`
- `doc/source/ray-core/scheduling/index.rst`
- `doc/source/ray-core/scheduling/placement-group.rst`
- `doc/source/ray-core/fault_tolerance/tasks.rst`
- `doc/source/ray-core/fault_tolerance/actors.rst`
- `doc/source/ray-core/fault_tolerance/objects.rst`
- `doc/source/ray-core/fault_tolerance/gcs.rst`
- `doc/source/ray-core/handling-dependencies.rst`
- `doc/source/ray-security/index.md`
- current repository/commit activity

## Verified capabilities and patterns

### Distributed execution model

- Ray Core exposes stateless Tasks, stateful Actors and immutable distributed Objects.
- The same application can run on one machine or a multi-node cluster.
- Tasks and actors declare logical CPU, GPU, memory and custom-resource requirements.
- A node is feasible only when it has every hard required resource; unavailable feasible nodes wait, while fully infeasible work requires new capacity or fails under the selected strategy.
- Default scheduling combines locality and load balancing; large task arguments can favor nodes holding the most local Object bytes.
- SPREAD, placement-group and node-affinity strategies provide explicit alternatives.
- Labels are a beta scheduling mechanism; custom numeric resources remain relevant for counted capacity.

### Reservations and gang placement

- Placement groups atomically reserve one or more resource bundles across Nodes.
- PACK and SPREAD-style strategies support locality, failure-domain and distributed-training choices.
- If every bundle cannot be placed, no partial resources are reserved.
- Bundles must each fit on one Node.
- Placement-group creation is asynchronous and exposes pending/created state.
- Reserved resources are consumed only by tasks/actors explicitly scheduled into that placement group.
- Placement groups are useful evidence for all-or-nothing reservations, but Ray placement-group IDs and state are not Ptah reservation identity.

### Retry, cancellation and execution semantics

- System-level Task failure can trigger automatic retries; defaults and limits are configurable.
- Application exceptions are not retried by default but can be selected for retry.
- Cancellation can interrupt or force-terminate workers, and cancelled tasks are not automatically retried.
- Actor processes can restart, but actor state is reconstructed only by rerunning the constructor unless the application manages checkpoints.
- Actor methods default to at-most-once semantics, but an error may occur even after a side effect actually executed.
- Configured actor-task retries provide at-least-once semantics and therefore require idempotent application behavior.
- Unavailable actor responses explicitly carry ambiguity about whether the method ran.
- Ray task/actor retries are workload behavior, not Ptah operation nonces, attempt receipts or side-effect proof.

### Objects and lineage

- Ray Objects have data in distributed Object Stores and metadata retained by the creating owner process.
- Lost data may be reconstructed from another copy or by rerunning the producing Task and recursively reconstructing its arguments.
- Lineage reconstruction assumes deterministic/idempotent production and is bounded by retry policy and retained lineage.
- Objects created through `ray.put` are not reconstructable through task lineage.
- Ray does not recover Objects after owner-process failure; remaining copies are cleaned and readers receive an owner-death error.
- Ray ObjectRefs, owners and Object Store entries are ephemeral workload/runtime identities rather than canonical Ptah Objects or durable Artifacts.

### Cluster control and fault tolerance

- The Global Control Service manages cluster metadata, actor/placement-group operations and Node management.
- Without external persistence, GCS failure causes cluster failure.
- HA Redis can support GCS state reload, but several creation, resource and registration operations remain unavailable during recovery.
- Running tasks/actors and existing objects may remain alive while the control service recovers.
- Official support for some GCS fault-tolerance paths is deployment-specific, particularly KubeRay/Serve.
- Ray control-plane recovery does not replace Ptah Activity history, placement leases, Node generations or independent reconciliation.

### Runtime environments and dependency distribution

- Runtime environments can install packages, files and environment variables per Job, Task or Actor and cache them on cluster Nodes.
- Production guidance favors prepared container images for stable environments.
- Dynamic runtime environments can download and install packages at execution time.
- Conflicting runtime environments can cause serialization and compatibility failures.
- Working directories and local files can be pushed to the cluster.
- Runtime environments are dependency convenience, not an isolation boundary or trusted Package/Build system.

### Security boundary

- Ray executes arbitrary code and its Dashboard, Jobs and Client services can provide complete cluster/compute access.
- Ray explicitly expects trusted code and a controlled network.
- Pickle/cloudpickle use creates arbitrary-code deserialization risk.
- Isolation must be enforced outside the Ray cluster.
- Workloads needing isolation from one another should use separate isolated Ray clusters.
- Built-in token authentication is defense in depth, not a replacement for network and runtime isolation.
- Ray does not provide per-developer or per-workload multi-tenant containment inside one cluster.

## What Ray contributes

- Mature distributed Task and Actor execution.
- Hard resource feasibility and configurable placement strategies.
- Data-locality-aware scheduling.
- Atomic multi-Node resource reservations and gang scheduling.
- Actor and Task state, attempts, retries, cancellation and observability patterns.
- Distributed immutable Object/cache machinery and lineage-reconstruction lessons.
- Autoscaling and KubeRay integration paths.
- Runtime-environment and container-image workload preparation patterns.
- A strong optional Facility for distributed Python, ML, data, simulation and evaluation workloads.
- A useful workload for MiniRouter, model evaluation, parallel research and future Ptah distributed Activities.

## Important limitations for Ptah

- Ray is a trusted-code distributed compute framework, not a secure multi-tenant substrate.
- Tasks, Actors, Jobs, Objects, ObjectRefs, placement groups, Nodes and attempts are Ray-local identities.
- Task retry can duplicate side effects; actor at-most-once errors can remain uncertain after execution.
- Ray lacks Ptah operation nonces, authoritative Receipts, external-side-effect proof and caller acceptance.
- Actor restart does not automatically restore application state.
- Object reconstruction assumes deterministic/idempotent lineage and cannot recover owner failure.
- GCS recovery depends on external Redis and still has control-plane interruption/availability boundaries.
- Runtime environments can install arbitrary supply-chain code and do not prove reproducibility, provenance or isolation.
- Ray's logical resources are scheduling quantities, not measured or fenced physical reservations by themselves.
- Labels are beta and placement choices can change across versions.
- Node affinity uses runtime Node IDs and can prevent scheduler/autoscaler optimization.
- Cluster services expose arbitrary code execution and must never be directly public.
- Separate Ray Jobs in one cluster are not isolated from each other.
- Ray's Object Store is not Ptah CAS, durable Object storage or canonical provenance.
- Python/cloudpickle and package/runtime compatibility can create security and reproducibility risk.
- Ray does not own Ptah Workspace, Node, Provider, Object, Activity, credential, network, checkpoint or proof contracts.

## Must not be inherited

- Ray Job, Task, Actor, ObjectRef, placement-group or Node IDs as canonical Ptah identities;
- Ray task completion or returned Object treated as verified operation success;
- automatic retries enabled for side-effecting work without nonce/idempotency policy;
- actor method error interpreted as proof that no side effect occurred;
- Ray Object Store used as durable canonical Object storage;
- owner-based object lifetime used as Ptah retention policy;
- runtime environments used as a Package trust, Build provenance or isolation system;
- one Ray cluster shared between mutually untrusted Workspaces;
- Dashboard, Jobs, Client, GCS or worker ports exposed to untrusted networks;
- cloudpickle data accepted from untrusted callers;
- token authentication described as complete isolation;
- placement-group reservation described as a durable Ptah lease without fencing and reconciliation;
- Node-affinity or scheduling policy embedded as caller reasoning authority;
- Ray made mandatory for single-Node or non-Python Workspaces.

## Integration decision

**ADOPT RAY AS AN OPTIONAL DISTRIBUTED COMPUTE AND GANG-SCHEDULING FACILITY BEHIND PTAH ACTIVITIES, PLACEMENT, ISOLATION AND OBJECT CONTRACTS; DO NOT USE IT AS PTAH CORE OR THE GLOBAL SCHEDULER.**

Recommended Ptah role:

1. Ptah decides the Workspace, Node, Isolation Class, credential, network and source/data policy before starting a Ray cluster or Job;
2. each trust domain receives a separate isolated Ray cluster or equivalent strong boundary;
3. Ray Tasks/Actors become provider-local executions under a durable Ptah Activity and attempt;
4. Ptah operation nonces and receipts guard side-effecting tasks against Ray retries/ambiguity;
5. Ray placement groups can implement an approved Ptah Reservation, but the Ptah lease/generation/fence remains authoritative;
6. Ray logical resources are mapped to measured Node capability and reserved capacity snapshots;
7. Ray Objects remain transient caches/results and are promoted to Ptah Objects/Artifacts only through explicit hashed persistence;
8. stable workload environments use signed container/Workspace images; dynamic runtime environments remain restricted development capability;
9. GCS, head Nodes and Ray services stay inside controlled networks with external authentication and process/container/VM isolation;
10. local one-Node operation remains possible without Ray;
11. Ray can be replaced by another distributed backend without changing Ptah Activity, Object, Reservation or caller identity.

## Licence decision

Apache-2.0 is compatible with architecture study, wrapping and optional dependency use. Ray wheels/images, bundled native components, Python packages, KubeRay, Redis, ML libraries and workload dependencies require independent licence, SBOM and provenance review.

## Native Ptah gap

Ptah must define:

- distributed Compute Facility and provider identity;
- trust-domain/cluster identity and isolation class;
- Node capability, observed load, reservation and availability snapshots;
- Placement Request, candidate decision, Reservation, Lease, Generation and Fence identities;
- CPU, RAM, disk, GPU/accelerator, network, cost, locality and data-gravity policy;
- mapping from Ray Job/Task/Actor/attempt to Ptah Activity/operation/attempt identities;
- operation nonce, retry, idempotency and side-effect Receipt policy;
- ObjectRef/result promotion to durable hashed Objects/Artifacts;
- actor/application checkpoint and recovery contracts;
- GCS/head-node loss and cluster-reconciliation policy;
- cluster/network/credential isolation and service exposure controls;
- signed/prepared workload environment and dynamic-package restrictions;
- observability and resource-accounting normalization;
- backend replacement and local fallback tests.

## Exit strategy

Ptah's distributed-placement and Activity contracts remain independent. Distributed work may use Ray, Kubernetes Jobs, Temporal workers, batch systems, direct Node workers or future schedulers without changing Workspace, Activity, Object, Reservation or caller identity.

## Validation required

1. Run the same pure computation locally and through Ray while preserving one Ptah Activity identity and distinct provider attempts.
2. Map hard resource requirements to measured Node capacity and reject infeasible placement honestly.
3. Reserve a multi-Node placement group atomically and retain Ptah lease/generation/fencing evidence.
4. Kill a worker/Node and prove retries create new attempts without duplicating protected external side effects.
5. Trigger actor-unavailable ambiguity and prove Ptah does not claim whether the side effect ran without a receipt/read-back.
6. Persist a Ray result into a hashed Ptah Object and lose every Ray Object copy without losing canonical data.
7. Kill an Object owner and prove Ptah identity/retention does not depend on Ray ownership.
8. Lose/restart GCS and reconcile Ptah Activities, Reservations and Nodes without trusting Ray recovery alone.
9. Deny untrusted access to Dashboard, Jobs, Client, GCS and worker services.
10. Run mutually untrusted workloads in separate Ray clusters and separate strong isolation Providers.
11. Reject unapproved dynamic runtime-environment packages and use signed prepared images for frozen workloads.
12. Compare locality, pack, spread, accelerator and cost-aware placement against a golden workload corpus.
13. Scale down/interruption-test a cluster and retain exact lost/retried/completed attempt evidence.
14. Replace Ray with another distributed backend without changing Ptah identities.
