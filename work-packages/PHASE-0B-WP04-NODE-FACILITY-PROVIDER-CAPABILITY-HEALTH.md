# Phase 0B WP04 — Node, Facility, Provider, Capability and Health

**Status:** CANDIDATE COMPLETE — DOWNSTREAM CONTRACT USE APPROVED; IMPLEMENTATION FREEZE DEFERRED  
**Date:** 2026-07-19  
**Runtime implementation:** NOT STARTED  
**Dependency/backend selection:** NOT STARTED

## Purpose

Turn the frozen Node Protocol, Facility/Provider, observability, isolation and placement architecture into exact candidate identities, schemas, lifecycle machines, migration rules and conformance expectations.

WP04 closes the contract boundary required to represent a Node or remote service honestly, expose a neutral Facility independently from its implementation, bind Provider revisions/instances/generations, retain capability evidence and decide whether one exact operation is currently eligible for dispatch.

## Normative records

- `contracts/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-CONVENTIONS.md`
- `contracts/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-CONVENTIONS.v0.1.1.md`
- `contracts/PHASE-0B-WP04-ENTITY-KIND-SUPPLEMENT.md`
- `migrations/phase-0b/WP04-NODE-FACILITY-PROVIDER-MIGRATION-COMPATIBILITY.md`
- `conformance/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-SAFETY-NET.md`
- `conformance/PHASE-0B-WP04-NODE-FACILITY-PROVIDER-SAFETY-NET.v0.1.1.md`
- `conformance/fixtures/phase-0b/wp04/node-facility-provider-cases.v0.1.0.json`
- `schemas/phase-0b/runtime/schema-catalog.v0.1.0.json`

The `0.1.1` correction records supersede only the named clauses of the original candidate drafts. They preserve candidate history while making the accepted package internally consistent.

## Candidate schema set

The runtime catalog contains 19 active schemas:

1. shared runtime definitions;
2. Node;
3. Node Enrollment;
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
16. Provider Instance;
17. Provider Observation;
18. Provider Capability Snapshot;
19. Dispatch Eligibility.

Dependencies:

- `ptah.common` `0.1.0`;
- `ptah.activity` `0.1.1`;
- `ptah.object` `0.1.0`.

## Lifecycle machines

Six namespaced lifecycle machines are included:

- `node.enrollment.lifecycle`;
- `node.lifecycle`;
- `facility.lifecycle`;
- `facility.instance.lifecycle`;
- `provider.lifecycle`;
- `provider.instance.lifecycle`.

Reachability, readiness, health, capability verification, capability availability and resource pressure are independent observations/projections rather than lifecycle aliases.

## Accepted boundaries

### Node

1. `core.node` is stable physical/virtual machine identity.
2. hostname, IP, MAC, cloud instance ID, boot ID, agent ID, key fingerprint and connection ID remain Aliases/evidence.
3. Node Enrollment is separate from Node lifecycle.
4. a Node becomes lifecycle `active` only after approved enrollment/trust evidence.
5. canonical Node lifecycle is `active`, `draining`, `quarantined`, `suspended`, `revoked`, `retired`.
6. Node generation fences prior runtime authority; connection epoch fences prior connection-scoped messages.
7. reconnect may advance only connection epoch; reinstall/restore/replacement may advance Node generation.
8. reachability and health remain independent observations.

### Capabilities and resources

1. Capability Definition, Claim, Verification and Availability remain separate.
2. manifest declaration, installed binary and provider self-report remain Claims.
3. Verification requires a frozen protocol and exact subject revision/generation.
4. Availability is current, time-bounded and policy-derived; it never rewrites verification history.
5. Node capability/resource snapshots are immutable, generation/epoch bound and expiring.
6. total, allocatable, reserved, consumed, currently available, quarantined, overcommit and pressure remain separate resource dimensions.
7. expired, partial or inconsistent snapshots cannot authorize dispatch beyond their proven scope.

### Facility

1. Facility is the stable neutral caller-facing operation contract.
2. Facility Revision is immutable operation/schema/capability/permission/dependency/proof contract.
3. Facility Instance is a scoped logical exposure/binding.
4. Facility identity never becomes an implementation/package/process/endpoint name.
5. Provider replacement does not change Facility identity.

### Provider

1. Provider is stable implementation-family identity.
2. Provider Revision is immutable build/configuration/compatibility/provenance.
3. Provider Instance is one local or remote incarnation.
4. Provider generation fences prior attempts/evidence; connection epoch fences prior transport/binding observations.
5. Provider lifecycle, reachability, readiness and health remain separate.
6. Provider Instance lifecycle is `declared`, `starting`, `running`, `draining`, `stopping`, `stopped`, `failed`, `quarantined`, `retired`.
7. lifecycle `failed` requires exact-generation correlated failure evidence; transient health `unhealthy` does not automatically create failure lifecycle.
8. lifecycle `running` proves only local process/service existence or approved remote binding—not readiness.
9. optional dependency failure degrades only affected capabilities/operations and remains visible.

### Local and remote Provider locality

Exactly one locality form is valid.

Local Providers bind:

- Node identity/generation;
- current Node capability/resource snapshots;
- Provider Instance/generation/epoch;
- Node enrollment/trust/lifecycle evidence.

Remote Providers bind:

- approved remote-service identity/authority;
- Provider Instance/generation/epoch;
- current Provider capability/readiness observations;
- external network/credential/audience/location/licence/policy evidence.

Remote Providers do not fabricate a Ptah Node or Node snapshots. Mixed locality is invalid.

### Dispatch eligibility

Dispatch Eligibility is one immutable, operation-specific, time-bounded decision. It is not Capability, Placement, Reservation, Lease, Attempt or proof of execution.

Every eligible decision requires:

- exact Activity and Operation;
- exact Facility Revision and operation key;
- exact Provider Instance/generation;
- current Provider capability/readiness evidence;
- authorization, policy and all hard constraints;
- evaluation and expiry times;
- no lifecycle, isolation or capability weakening.

Local eligibility adds current Node/generation/capability/resource evidence. Remote eligibility uses approved remote-service evidence and excludes Node fields.

## Migration closure

The migration record forbids:

- alias-derived Node identity;
- reachability-derived trust;
- global status collapse;
- capability claim promoted to verification;
- resource dimensions collapsed;
- stale snapshot/generation eligibility;
- Facility/Provider identity merge;
- generation reuse;
- fictional Node creation for remote services;
- mixed local/remote locality;
- historical evidence deletion.

Provider/backend/locality replacement preserves Facility identity, creates/selects compatible Provider revisions/instances, advances or replaces generation appropriately, re-verifies capabilities/readiness and fences all stale eligibility/evidence.

## Conformance closure

The consolidated safety net and fixture suite cover:

- Node reconnect, reboot, reinstall and stale evidence;
- enrollment approval/rejection/revocation and Node lifecycle separation;
- quarantined-but-online Node behavior;
- capability claim/verification/availability chain;
- resource arithmetic/freshness/pressure;
- Facility/Provider replacement;
- running-but-not-ready and ready-but-degraded Providers;
- receipted Provider failure versus transient health;
- local/remote locality XOR;
- remote dispatch without fictional Node snapshots;
- draining/quarantine dispatch blocking;
- eligibility expiry and generation fencing;
- migration from collapsed legacy status.

Structural validation is insufficient. WP13 must execute typed-reference, history, time, generation, arithmetic, locality, transition, policy and cross-record invariants.

## Candidate-completion verdict

**WP04 is candidate-complete for downstream Phase 0B use.**

It does not prove that any Node agent, Provider, runtime, scheduler, health system, capability probe, remote service, transport or backend exists or works.

## Deferred work

- Workspace/Session/checkpoint/recovery — WP05;
- transfer/sync/backup — WP06;
- Build/provenance — WP07;
- Domain/Device and UI contracts — later WPs;
- isolation/placement/reservation/lease/secure grants — WP11;
- executable harness and golden corpus — WP13/WP14;
- runtime and dependency selection — Phase 0C only.

## Acceptance decision

- `decisions/ADR-0021-NODE-FACILITY-PROVIDER-CAPABILITY-HEALTH-BOUNDARY.md`

## Do-not-build rule

> Candidate-complete contracts authorize downstream schema design only. They do not authorize installing, deploying or selecting a Node agent, Provider implementation, health checker, scheduler, message bus, database, container runtime or remote service.