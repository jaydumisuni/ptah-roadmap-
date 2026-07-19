# Phase 0B WP04 — Node, Facility, Provider, Capability and Health Safety Net

**Status:** CANDIDATE SPECIFICATION  
**Executable harness:** deferred to WP13/WP14  
**Fixture suite:** `conformance/fixtures/phase-0b/wp04/node-facility-provider-cases.v0.1.0.json`

## Purpose

Define one consolidated conformance boundary for stable Node identity, enrollment/trust, generation/epoch fencing, Facility/Provider separation, capability evidence, resource truth, readiness/health observations, local/remote Provider operation and time-bounded dispatch eligibility.

Structural JSON Schema validation is necessary but insufficient. The harness must load the common, activity, object and runtime catalogs, entity-kind registry, state-machine definitions and cross-record history.

## Required catalog inputs

- `schemas/phase-0b/common/schema-catalog.v0.1.0.json`
- `schemas/phase-0b/activity/schema-catalog.v0.1.1.json`
- `schemas/phase-0b/object/schema-catalog.v0.1.0.json`
- `schemas/phase-0b/runtime/schema-catalog.v0.1.0.json`

## Validation layers

### L1 — Structural

- valid JSON and JSON Schema 2020-12;
- resolvable absolute Ptah URNs through local catalogs;
- required fields and enums;
- canonical Entity Envelope and `entity_kind`;
- UUIDv7/reference format;
- state-machine projection shape;
- timestamp, version and extension shape.

### L2 — Typed reference

Enforce at minimum:

- `node_ref` → `core.node`;
- enrollment/snapshot/observation references → exact WP04 kinds;
- Facility/Revision/Instance references → exact Facility kinds;
- Provider/Revision/Instance references → exact Provider kinds;
- capability claim/verification/availability references → exact capability kinds;
- Activity/Operation/Attempt/Receipt references → WP02 canonical kinds;
- policy/authorization/review references → allowed authority/proof kinds.

### L3 — Identity and history

- Node identity cannot be hostname/IP/MAC/cloud ID/boot ID/agent ID/key fingerprint alone;
- backend process/container/VM/service/endpoint IDs remain aliases;
- immutable Capability/Facility/Provider revisions and observations cannot be rewritten;
- lifecycle projections advance through registered state machines only;
- supersession/replacement preserves prior revisions and observations;
- migration never merges Nodes or Facility/Provider identities from aliases alone.

### L4 — Generation and connection fencing

- Node generation is monotonic within one Node;
- Provider generation is monotonic within one Provider Instance;
- connection epoch is monotonic within the relevant connection scope;
- reboot, agent replacement and Provider restart advance the appropriate generation/epoch;
- Attempts, Receipts, observations and eligibility decisions bind exact generations/epoch;
- late/stale evidence is retained but cannot prove current-generation work;
- eligibility becomes invalid after generation/epoch mismatch.

### L5 — Enrollment, trust and authorization

- reachability never grants enrollment, trust or dispatch authority;
- enrollment approval/revocation/expiry retains named authority, scope, policy and evidence;
- revoked/expired/rejected enrollment blocks new work;
- Node lifecycle `draining`, `quarantined`, `suspended`, `revoked` or `retired` blocks ordinary new work;
- maintenance/recovery exceptions require explicit narrow authorization;
- credential/certificate possession alone cannot restore revoked authority.

### L6 — Capability truth chain

The harness must preserve:

```text
Capability Definition
  what the capability means

Capability Claim
  what one subject says it supports

Capability Verification
  what a frozen protocol observed

Capability Availability
  whether the exact subject generation can provide it now

Provider Capability Snapshot
  current bounded operation/dependency projection
```

Rules:

- Claim never becomes Verification automatically;
- Verification never means current Availability;
- Availability expires and is generation-bound;
- dependency/device/network/resource loss can degrade or block Availability while historical Verification remains;
- unsupported/failed/inconclusive/stale outcomes remain visible;
- Provider/Node names and labels are not capability proof.

### L7 — Resource truth

For every resource quantity:

```text
observed total
administratively allocatable
reserved
consumed
currently available
unavailable/quarantined
overcommit policy/limit
pressure
```

Rules:

- dimensions cannot be collapsed;
- units must be compatible before comparison;
- historical snapshots are immutable;
- pressure observations do not rewrite capacity;
- reservations/consumption cannot be ignored when authorizing dispatch;
- expired/partial snapshots cannot support constraints they did not observe;
- logical scheduler labels are not physical/exclusive capacity proof.

### L8 — Facility and Provider separation

- Facility is the neutral stable operation contract;
- Facility Revision is immutable operation/capability/permission/proof definition;
- Facility Instance is a scoped exposure/binding;
- Provider is stable implementation-family identity;
- Provider Revision is exact implementation/build/configuration compatibility;
- Provider Instance is one materialized local or remote incarnation/generation;
- package/executable/plugin/backend name cannot replace Facility identity;
- replacing Provider implementation preserves Facility/caller contract identity;
- dispatch operation key must exist in the exact Facility Revision and be supported by the exact Provider Revision/snapshot.

### L9 — Lifecycle versus observations

Node and Provider lifecycle are not reachability/readiness/health.

Valid examples:

- Node lifecycle `active`, reachability `offline`;
- Provider Instance lifecycle `running`, readiness `not_ready`, health `healthy`;
- Provider Instance lifecycle `running`, readiness `ready`, health `degraded` for a bounded operation subset;
- Provider lifecycle `deprecated` while an existing Instance remains active under policy.

Invalid examples:

- heartbeat loss changes Node lifecycle to failed/revoked;
- running process implies ready;
- ready implies healthy;
- healthy implies capable/authorized/resourced;
- one optional dependency outage becomes universal unavailable or is hidden behind full ready.

### L10 — Local and remote Provider hosting

- Node-local Provider Instances bind an exact Node generation and Provider generation;
- remotely hosted/external Provider Instances declare hosting/control mode, endpoint aliases, authorization and external health evidence without inventing a local Node;
- endpoint URL/socket/service name remains alias;
- remote reachability is not external service correctness or authority;
- dispatch eligibility must apply the correct local/remote constraints and current evidence.

### L11 — Dispatch eligibility

An `eligible` decision requires all of:

- exact Activity and Operation;
- exact Facility Revision and operation key;
- exact Node/Provider Instance and current generations;
- non-expired Node capability and resource snapshots;
- non-expired Provider capability snapshot and relevant observations;
- enrollment/trust and caller/Workspace authorization;
- Node/Provider lifecycle not blocking new work;
- hard constraints satisfied;
- required resources, network, credentials, devices and Object access permitted;
- policy revision and evaluation/expiry times;
- no silent isolation/capability weakening.

Eligibility is not a Reservation, Lease, Attempt, Receipt or proof that execution succeeded. It expires before dispatch if unused and is invalidated by relevant generation, authorization, lifecycle or evidence changes.

### L12 — Event, heartbeat and projection loss

- heartbeat/Event delivery updates projections but does not replace durable observations/history;
- missing heartbeat marks projection stale/offline after policy threshold;
- missing Event cannot erase Node/Provider/Activity truth;
- reconnect requires reconciliation and fresh evidence;
- duplicate/out-of-order observations are retained/dispositioned by sequence/generation/time rules;
- current projections must identify their source observations.

### L13 — Migration and backend replacement

The harness must prove:

- legacy global status splits into namespaced dimensions;
- ambiguous status maps to unknown/manual review, never guessed ready/healthy/verified;
- legacy capability labels become Claims;
- missing generations/epochs are bounded migration assignments, not reconstructed history;
- Provider replacement creates new Revisions/Instances/generations;
- Facility and caller contract identity remains stable;
- old dispatch decisions and Receipts cannot authorize/prove new generations;
- all historical failures/revocations/observations remain retained.

## Mandatory positive cases

1. reconnect preserves Node ID and advances connection epoch;
2. reboot/agent replacement preserves Node ID and advances generation/epoch as applicable;
3. verified capability temporarily unavailable due to dependency/device loss;
4. optional dependency degrades only affected operations;
5. running Provider not ready;
6. ready Provider degraded for a bounded subset;
7. Provider implementation replacement preserves Facility identity;
8. remote Provider represented without fake local Node;
9. eligibility passes under exact current evidence and later expires;
10. pressure/resource history retained across immutable snapshots.

## Mandatory negative cases

1. alias used as Node/Provider/Facility identity;
2. reachable but unauthorized/revoked Node receives work;
3. stale/expired capability or resource snapshot authorizes dispatch;
4. declared capability promoted to verified;
5. total capacity treated as available capacity;
6. Provider generation reused after restart;
7. old-generation Receipt proves new-generation work;
8. running implies ready/healthy;
9. operation absent from Facility Revision is dispatched;
10. global status collapses lifecycle/reachability/readiness/health;
11. draining/quarantined/suspended/revoked/retired Node receives ordinary work;
12. backend replacement rewrites historical identity/evidence.

## Property/invariant tests for WP13

- generation and epoch monotonicity;
- no eligibility after `valid_until`;
- any referenced snapshot generation equals the decision subject generation;
- `eligible` implies every required hard constraint result is `satisfied`;
- `eligible` cannot reference blocked/unavailable required capability;
- `eligible` cannot reference rejected/revoked/expired enrollment;
- Facility operation key uniqueness within one Revision;
- Provider Instance generation change invalidates prior current projection;
- immutable observation/revision content hash remains stable;
- lifecycle transition authority/preconditions/Receipts satisfy registered state machine;
- backend aliases never equal canonical Entity IDs.

## Proof expectations

Candidate contract proof consists of:

- catalog/schema validation;
- typed-reference and history checks;
- state-machine transition checks;
- generation/freshness fencing;
- migration scenarios;
- backend replacement scenarios;
- retained positive and negative fixtures.

It does **not** prove any real Node, Provider, runtime, scheduler or backend is implemented, deployed, secure, healthy or performant.

## Exit criteria for WP04 candidate completion

- normative conventions and entity supplement committed;
- 19 active schemas cataloged;
- six lifecycle machines committed;
- migration/compatibility rules committed;
- fixture suite committed;
- this consolidated safety net committed;
- ADR/work-package review accepts the boundary;
- all global ledgers synchronized;
- runtime/dependency selection remains blocked.