# Phase 0B WP04 — Node, Facility, Provider, Capability and Health Conventions 0.1.1 Corrections

**Status:** CANDIDATE CORRECTION  
**Date:** 2026-07-19  
**Supersedes:** specific clauses in `PHASE-0B-WP04-NODE-FACILITY-PROVIDER-CONVENTIONS.md`  
**Implementation authorization:** NONE

## Purpose

Preserve the original WP04 draft as candidate history while correcting review findings before package acceptance.

All clauses in the original conventions remain active except where explicitly replaced below.

---

# C-001 — Node Enrollment and Node lifecycle remain separate

The original section 2.5 lifecycle list is replaced by:

```text
active
draining
quarantined
suspended
revoked
retired
```

Rules:

1. `core.node_enrollment` owns submitted, under-review, approved, rejected, revoked and expired enrollment decisions.
2. A Node ID may be reserved during enrollment, but canonical dispatch-eligible Node state begins only after approved enrollment.
3. A rejected enrollment never produces lifecycle `active`.
4. `pending_enrollment` is not a Node lifecycle state.
5. `quarantined` is a Node lifecycle state distinct from health `unhealthy` and reachability `offline`.
6. Node lifecycle initial state is `active` only when approved enrollment/trust evidence exists.
7. Node reachability and health remain independent projections.

Canonical lifecycle machine:

- `state-machines/phase-0b/node-lifecycle.v0.1.0.json`

Canonical enrollment lifecycle machine:

- `state-machines/phase-0b/node-enrollment-lifecycle.v0.1.0.json`

---

# C-002 — Local and remote Provider locality are explicit alternatives

Provider Instance, Provider Observation, Provider Capability Snapshot and Dispatch Eligibility use exactly one locality form.

## Local Provider

```text
node_ref
node_generation
provider_instance_ref
provider_generation
connection_epoch
```

Local dispatch also requires current:

- Node Capability Snapshot;
- Node Resource Snapshot;
- Node enrollment/trust/lifecycle eligibility;
- Provider Capability Snapshot and readiness evidence.

## Remote-service Provider

```text
remote_service_ref
provider_instance_ref
provider_generation
connection_epoch
```

Remote-service Providers do not fabricate a Ptah Node, Node generation, Node capability snapshot or Node resource snapshot merely to satisfy a local schema shape.

Remote dispatch instead requires:

- approved remote-service identity and authority;
- current Provider Capability Snapshot;
- current Provider observations/readiness;
- network, credential, audience, location, licence and policy checks;
- exact external-service limitations and proof boundary.

## Rules

1. exactly one locality form is valid;
2. moving a Provider between local and remote locality creates a new Provider Instance unless an explicit migration preserves identity and advances generation;
3. Facility identity remains unchanged;
4. remote-service liveness/readiness remains Provider evidence, not Node truth;
5. external service account, endpoint, region or deployment ID remains an Alias/reference rather than canonical Provider identity;
6. remote Provider operation results still require WP02 correlation and authoritative external evidence where applicable.

Corrected schemas:

- `schemas/phase-0b/runtime/provider-observation.v0.1.0.schema.json`
- `schemas/phase-0b/runtime/provider-capability-snapshot.v0.1.0.schema.json`
- `schemas/phase-0b/runtime/dispatch-eligibility.v0.1.0.schema.json`

---

# C-003 — Dispatch wording

The original dispatch rule "Node lifecycle/trust/authorization are eligible" applies only to local Providers.

For remote-service Providers, the equivalent hard check is:

> Remote service identity, authority, Provider generation, readiness, capability evidence, policy, network, credential, audience, location and licence constraints are current and satisfied.

All remaining dispatch rules continue to apply where meaningful.

---

# C-004 — Provider Instance lifecycle includes receipted failure and quarantine

The original Provider Instance lifecycle list is replaced by:

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

Rules:

1. `failed` is a durable lifecycle state only after a correlated failure transition records the exact Provider generation and uncertain work.
2. transient health `unhealthy` does not automatically move lifecycle to `failed`.
3. lifecycle `failed` does not replace health, readiness, reachability or Activity/Operation reconciliation.
4. `quarantined` is an administrative lifecycle state that blocks dispatch while preserving the Provider Instance and evidence.
5. `running` proves only that a local process/service or approved remote binding exists; readiness remains separate.
6. local startup binds current Node generation; remote startup binds approved remote-service authority.
7. a new start from `stopped` or `failed` requires a new monotonic Provider generation.

Canonical machine:

- `state-machines/phase-0b/provider-instance-lifecycle.v0.1.0.json`

---

# Conformance additions

1. reject Node lifecycle `pending_enrollment`;
2. reject Node `active` without approved/current enrollment evidence;
3. permit Node `quarantined` with reachability `online` while blocking ordinary dispatch;
4. permit local Provider Observation only with Node reference and generation;
5. permit remote Provider Observation only with remote service reference and no Node fields;
6. reject mixed local/remote locality fields;
7. reject remote dispatch requiring or inventing Node snapshots;
8. reject local dispatch without current Node capability/resource snapshots;
9. preserve Facility identity when local and remote Provider implementations are swapped;
10. fence stale Provider generations in both locality modes;
11. reject transient health `unhealthy` used as an automatic Provider lifecycle transition;
12. require correlated failure evidence before lifecycle `failed`;
13. permit lifecycle `running`, readiness `not_ready`, and health `degraded` simultaneously;
14. reject ordinary dispatch to lifecycle `quarantined` even when reachable.

## Do-not-break rule

> Enrollment does not become Node lifecycle, quarantine does not become health, transient unhealthiness does not become receipted failure, and a remote Provider does not become a fictional Node. Local and remote Providers share Facility/Provider contracts while retaining truthful locality-specific evidence.