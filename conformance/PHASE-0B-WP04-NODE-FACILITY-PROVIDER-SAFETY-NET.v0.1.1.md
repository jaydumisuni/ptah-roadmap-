# Phase 0B WP04 — Node, Facility, Provider, Capability and Health Safety Net 0.1.1

**Status:** CANDIDATE CORRECTION  
**Date:** 2026-07-19  
**Extends:** `PHASE-0B-WP04-NODE-FACILITY-PROVIDER-SAFETY-NET.md`  
**Fixture suite:** `conformance/fixtures/phase-0b/wp04/node-facility-provider-cases.v0.1.0.json`

## Purpose

Add the lifecycle and locality invariants discovered during WP04 package review. All original safety-net requirements remain active unless replaced below.

## S1 — Node Enrollment versus Node lifecycle

The harness must enforce:

1. enrollment lifecycle and Node lifecycle are different state machines;
2. `pending_enrollment` is rejected as a Node lifecycle state;
3. Node lifecycle `active` requires current approved enrollment/trust evidence;
4. rejected, expired or revoked enrollment cannot authorize dispatch;
5. Node lifecycle `quarantined` may coexist with reachability `online` and health `healthy`, while ordinary dispatch remains blocked;
6. heartbeat/reachability cannot create or reactivate enrollment.

## S2 — Provider Instance lifecycle versus health

Canonical Provider Instance lifecycle states are:

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

The harness must prove:

1. `running` does not imply `ready` or `healthy`;
2. health `unhealthy` does not automatically transition lifecycle to `failed`;
3. lifecycle `failed` requires exact-generation failure evidence and reconciliation of uncertain work;
4. lifecycle `quarantined` blocks ordinary dispatch even when reachable/ready/capable;
5. restart from `stopped` or `failed` uses a new Provider generation;
6. health/readiness observations remain immutable evidence beneath lifecycle decisions.

## S3 — Local versus remote Provider locality

Exactly one Provider locality form is valid.

### Local

Requires:

- `node_ref`;
- `node_generation`;
- current Node Capability Snapshot;
- current Node Resource Snapshot;
- enrollment/trust/lifecycle eligibility;
- Provider Instance/generation/epoch and current Provider evidence.

### Remote service

Requires:

- `remote_service_ref`;
- approved remote-service identity/authority;
- Provider Instance/generation/epoch;
- current Provider capability/readiness evidence;
- network, credential, audience, location, licence and policy evidence.

It forbids:

- `node_ref`;
- `node_generation`;
- Node Capability Snapshot;
- Node Resource Snapshot.

The harness must reject mixed local/remote fields and any fabricated Node created solely for an external service.

## S4 — Dispatch eligibility replacement

The original L11 wording requiring an exact Node for every eligible decision is replaced by:

An `eligible` decision always requires:

- exact Activity and Operation;
- exact Facility Revision and operation key;
- exact Provider Instance/generation;
- non-expired Provider Capability Snapshot and relevant observations;
- current authority and policy;
- all applicable hard constraints satisfied;
- exact evaluation and expiry times;
- no lifecycle, capability or isolation weakening.

A **local** eligible decision additionally requires exact Node/generation plus current Node capability/resource snapshots.

A **remote** eligible decision instead requires an approved remote-service reference/authority and must not contain Node fields/snapshots.

## S5 — Replacement and migration

The harness must prove:

1. Facility identity survives local-to-local, remote-to-remote and local-to-remote Provider replacement;
2. locality change normally creates a new Provider Instance;
3. an explicitly identity-preserving locality migration advances Provider generation and fences prior work;
4. capability/readiness verification is rerun after locality/backend change;
5. old Attempts, Receipts, observations and failures remain historical;
6. no dispatch eligibility survives generation, locality, authority or snapshot change.

## Additional mandatory positive cases

- Node quarantined but online;
- Provider unhealthy without automatic lifecycle failure;
- Provider lifecycle running/readiness not-ready/health degraded;
- valid remote Provider observation without Node fields;
- valid remote dispatch eligibility without Node snapshots;
- Facility retains identity after local-to-remote Provider replacement.

## Additional mandatory negative cases

- `pending_enrollment` used as Node lifecycle;
- Node active without approved enrollment;
- mixed local and remote Provider locality fields;
- remote Provider carrying fabricated Node snapshots;
- local Provider eligibility without Node snapshots;
- transient unhealthy observation promoted to lifecycle failed;
- ordinary dispatch to quarantined Provider;
- stale Provider generation accepted after local or remote restart/rebinding.

## Property additions for WP13

- locality XOR invariant for Provider Instance, Observation, Capability Snapshot and Dispatch Eligibility;
- local eligibility implies Node snapshot generations equal decision Node generation;
- remote eligibility implies absence of every Node-specific field;
- Node lifecycle state belongs to `node.lifecycle`, never enrollment lifecycle;
- Provider `failed` lifecycle transition references exact-generation failure evidence;
- quarantine blocks ordinary operation keys regardless of reachability/readiness projection.

## Exit condition

WP04 cannot be accepted until its ADR/work package reference:

- conventions correction `0.1.1`;
- corrected Provider Instance lifecycle;
- corrected migration record;
- extended fixture suite;
- this safety-net correction.
