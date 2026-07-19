# ADR-0021 — Node, Facility, Provider, Capability and Health Boundary

**Status:** ACCEPTED FOR PHASE 0B DOWNSTREAM CONTRACT DESIGN  
**Date:** 2026-07-19  
**Phase:** 0B-WP04  
**Implementation authorization:** NONE

## Context

Ptah must describe machines, external services, neutral Facilities and their implementations without turning hostnames, endpoints, heartbeats, manifests or process starts into identity, trust, readiness, capability or proof.

The frozen Phase 0A architecture established:

- stable Node identity and Node Protocol;
- Facility contracts independent of implementation;
- Provider workers and generations;
- Node capability/resource snapshots;
- lifecycle, readiness, health and observability separation;
- placement hard constraints and stale-generation fencing;
- local one-Node and later distributed operation under the same identities.

WP01–WP03 supplied common identity/versioning, Activity/Attempt/Receipt proof and Object/Artifact/storage contracts. WP04 must bind these layers before Workspace, Session, transfer, Build and placement schemas can safely reference them.

## Decision

Ptah owns distinct canonical records for:

1. Node;
2. Node Enrollment;
3. Node Generation and connection epoch;
4. Node Observation;
5. Node Capability Snapshot;
6. Node Resource Snapshot;
7. Capability Definition;
8. Capability Claim;
9. Capability Verification;
10. Capability Availability;
11. Facility;
12. Facility Revision;
13. Facility Instance;
14. Provider;
15. Provider Revision;
16. Provider Instance and Provider Generation;
17. Provider Observation;
18. Provider Capability Snapshot;
19. Dispatch Eligibility.

Backend identifiers, endpoints, hostnames, processes, containers, VMs, package names and service accounts remain aliases/evidence.

## Node boundary

`core.node` is stable identity for one physical or virtual machine boundary.

Enrollment is separate from Node lifecycle. A Node ID may be reserved during enrollment, but dispatch-eligible lifecycle begins only after approved enrollment/trust evidence.

Canonical Node lifecycle:

```text
active
draining
quarantined
suspended
revoked
retired
```

Node reachability and health are independent observations. A Node may be `active`, `offline` and health `unknown` without contradiction.

Node generation fences prior machine/agent runtime authority. Connection epoch fences connection-scoped messages. Ordinary reconnect may advance only epoch; reinstall, restore, forced fencing or identity-preserving replacement may advance generation.

## Capability boundary

Capability truth is a chain rather than one flag:

```text
Capability Definition
Capability Claim
Capability Verification
Capability Availability
Capability Snapshot
```

- Definition states what a capability means.
- Claim states what one subject declares.
- Verification states what a frozen protocol observed over one exact revision/generation.
- Availability states whether it can be used now under current policy/dependency/resource evidence.
- Snapshot groups bounded current observations.

Manifest declarations, installed binaries and provider self-reports never become verified capability automatically.

## Resource boundary

Resource snapshots retain separately:

```text
observed_total
administratively_allocatable
reserved
consumed
currently_available
unavailable_or_quarantined
overcommit_policy_and_limit
pressure
```

Snapshots are immutable, time-bounded and generation/epoch bound. Total capacity cannot be used as available capacity, and stale/partial snapshots cannot satisfy constraints they did not observe.

## Facility boundary

Facility is the stable neutral caller-facing operation contract.

- Facility Revision is immutable operation/schema/capability/permission/dependency/proof definition.
- Facility Instance is one scoped exposure/binding.
- Provider is an implementation-family identity, not Facility identity.
- Provider replacement cannot change caller-facing Facility identity.

## Provider boundary

Provider, Provider Revision and Provider Instance remain separate.

Provider Revision retains exact implementation/build/configuration, compatibility, capabilities, dependencies, requirements, provenance and limitations.

Provider Instance is one local or remote incarnation with monotonic Provider generation and connection epoch.

Canonical Provider Instance lifecycle:

```text
declared
starting
running
draining
stopping
stopped
failed
quarantined
retired
```

Reachability, readiness and health remain independent observations.

- `running` proves only that a local process/service or approved remote binding exists.
- readiness states whether current dispatch preconditions pass.
- health assesses current condition.
- transient `unhealthy` does not automatically create lifecycle `failed`.
- lifecycle `failed` requires exact-generation correlated evidence and reconciliation.
- quarantine blocks ordinary dispatch even when reachable/ready.

## Local and remote locality

Provider records use exactly one locality form.

### Local

Binds exact Node and Node generation plus current Node capability/resource evidence.

### Remote service

Binds approved remote-service identity/authority and current Provider evidence. It does not fabricate a Ptah Node, Node generation or Node snapshots.

Moving between locality modes normally creates a new Provider Instance. Any explicit identity-preserving migration advances generation, fences old work and re-verifies capability/readiness.

## Heartbeat and observation boundary

A heartbeat proves only that an authenticated producer emitted one time/sequence/generation-bound observation.

It does not prove:

- enrollment or trust;
- readiness;
- capability conformance;
- free capacity;
- successful operation;
- truth beyond its freshness deadline.

Missing/late heartbeat changes reachability/projection freshness; it does not fabricate Node/Provider/Activity failure.

## Dependency and degradation boundary

Dependencies are classified as required, optional, operation-specific or proof-only.

- required failure blocks affected readiness;
- optional failure degrades only affected capability;
- operation-specific failure leaves unrelated operations available;
- proof-only failure may permit execution while blocking stronger proof/acceptance.

Reduced capability and limitations must be visible.

## Dispatch eligibility

Dispatch Eligibility is an immutable, operation-specific and expiring decision. It is not Capability, Placement, Reservation, Lease, Attempt or execution proof.

Every eligible decision requires:

- exact Activity and Operation;
- exact Facility Revision and operation key;
- exact Provider Instance/generation;
- current Provider capability/readiness evidence;
- current authority and policy;
- all applicable hard constraints;
- no blocking lifecycle state;
- exact evaluation and expiry times;
- no silent isolation/capability weakening.

Local eligibility adds exact Node/generation and current Node capability/resource snapshots. Remote eligibility instead uses approved remote-service evidence and excludes Node fields.

## Migration and replacement

Migration must preserve:

- stable identities and aliases;
- generation/epoch boundaries;
- lifecycle versus observations;
- capability claim/verification/availability separation;
- resource dimensions;
- Facility/Provider separation;
- local/remote locality;
- historical failures, revocations and stale evidence.

Backend replacement preserves Facility identity, creates/selects compatible Provider revisions/instances, advances/replaces generation, invalidates stale eligibility, re-verifies capability/readiness and never rewrites historical Attempts/Receipts.

## Schema and conformance decision

Accepted candidate package:

- 19 runtime schemas in `schemas/phase-0b/runtime/schema-catalog.v0.1.0.json`;
- six namespaced lifecycle machines;
- conventions and `0.1.1` corrections;
- migration/compatibility record;
- extended positive/negative fixtures;
- consolidated safety net and `0.1.1` corrections.

Structural JSON Schema validation is not sufficient. WP13 must enforce typed references, monotonic generations/epochs, time/freshness, resource arithmetic, locality XOR, lifecycle transitions, authorization, compatibility and cross-record evidence.

## Consequences

### Positive

- Nodes and Providers survive endpoint/process/backend replacement without identity loss.
- external services are represented honestly without fake Nodes.
- capability declarations cannot masquerade as conformance proof.
- heartbeat, readiness, health and operation proof remain distinct.
- stale-generation work and evidence can be fenced.
- resource truth supports later placement without collapsing capacity.
- Facility callers remain independent from implementation choice.
- local and remote Providers share one neutral contract family.

### Costs

- more records and state dimensions than a single worker/status table;
- explicit enrollment, observations, snapshots and verification are required;
- compatibility and availability become operation-specific and time-bounded;
- migration from simple worker registries needs manual review where evidence is weak.

## Rejected alternatives

### Hostname/IP/cloud ID as Node identity

Rejected because aliases change, collide and can be reassigned.

### Heartbeat means healthy and ready

Rejected because contact does not prove dependencies, capabilities, capacity or operation support.

### One global status

Rejected because lifecycle, reachability, readiness, health, capability and pressure answer different questions.

### Facility equals implementation/plugin

Rejected because it prevents replacement and leaks backend identity into caller contracts.

### Installed binary means verified capability

Rejected because presence does not prove configuration, dependency or operation behavior.

### Every Provider must belong to a Ptah Node

Rejected because remote services are real Providers but are not Ptah-controlled machine boundaries.

### Failed health automatically changes lifecycle

Rejected because transient observation and durable receipted failure are different facts.

### Dispatch eligibility stored permanently

Rejected because it expires when snapshots, generations, policy, authority or locality change.

## Downstream requirements

WP05 and later packages may reference WP04 candidates, but must preserve:

- Node/Provider generations and connection epochs;
- local/remote locality;
- lifecycle versus readiness/health;
- capability and resource snapshot freshness;
- Facility versus Provider identity;
- dispatch eligibility as expiring evidence;
- WP02 Activity/Attempt/Receipt correlation.

No runtime, Node agent, health checker, scheduler, Provider implementation, database, message bus or deployment is authorized by this ADR.

## Related records

- `work-packages/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-CAPABILITY-HEALTH.md`
- `contracts/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-CONVENTIONS.md`
- `contracts/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-CONVENTIONS.v0.1.1.md`
- `contracts/PHASE-0B-WP04-ENTITY-KIND-SUPPLEMENT.md`
- `schemas/phase-0b/runtime/schema-catalog.v0.1.0.json`
- `migrations/phase-0b/WP04-NODE-FACILITY-PROVIDER-MIGRATION-COMPATIBILITY.md`
- `conformance/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-SAFETY-NET.md`
- `conformance/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-SAFETY-NET.v0.1.1.md`
- `conformance/fixtures/phase-0b/wp04/node-facility-provider-cases.v0.1.0.json`
