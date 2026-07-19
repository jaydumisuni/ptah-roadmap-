# Phase 0B WP04 — Entity Kind Supplement

**Status:** CANDIDATE DRAFT  
**Parent registry:** `ptah.entity-kind` `0.1.0`  
**Date:** 2026-07-19

## Purpose

Add the independently referenced identities required by the Node, Facility, Provider, capability and health contract set without repurposing backend aliases or observational states as entity kinds.

## New entity kinds

| Entity kind | Canonical role | Mutability rule |
|---|---|---|
| `core.node_enrollment` | explicit request/approval/trust record for one Node | versioned lifecycle projection; decisions/history retained |
| `core.node_capability_snapshot` | immutable observed capability inventory for one Node generation/epoch | immutable |
| `core.node_resource_snapshot` | immutable total/allocatable/reserved/consumed/pressure observation | immutable |
| `core.node_observation` | one reachability/health/heartbeat observation | immutable |
| `core.capability_claim` | one subject's declaration of capability support | immutable assertion; replacement supersedes |
| `core.capability_verification` | frozen-protocol verification over one exact capability subject | immutable |
| `core.capability_availability` | time-bounded derived availability projection | immutable observation/projection revision |
| `core.facility_revision` | immutable Facility contract/operation revision | immutable |
| `core.facility_instance` | one scoped logical exposure/binding of a Facility Revision | mutable lifecycle/projection with retained history |
| `runtime.provider_instance` | one deployed/running materialization of a Provider Revision | mutable lifecycle/projection with monotonic generation |
| `runtime.provider_observation` | one reachability/readiness/health/heartbeat observation | immutable |
| `runtime.provider_capability_snapshot` | immutable Provider Instance capability/dependency projection | immutable |
| `runtime.dispatch_eligibility` | one operation-specific eligibility decision for an exact Node/Provider state | immutable decision |

## Existing kinds reused

- `core.node` — stable physical/virtual machine identity.
- `core.facility` — stable neutral Facility contract root.
- `core.capability` — versioned capability definition.
- `runtime.provider` — stable Provider definition root.
- `runtime.provider_revision` — immutable Provider implementation/configuration revision.
- `runtime.process` — supervised process identity.
- `runtime.service` — supervised service/endpoint registration.
- `runtime.reservation` — resource reservation.
- `runtime.lease` — scoped time-bounded execution authority.
- `runtime.placement_request`, `runtime.placement_candidate`, `runtime.placement_decision` — later placement contracts.
- `runtime.secure_grant` — later exact Object/network/device/credential grant.
- `proof.receipt`, `proof.evidence`, `proof.review`, `proof.verdict` — proof/review records.

## Typed-family values

### Provider kinds

Existing provider-kind values remain canonical, including:

```text
workspace
process
oci_runtime
isolation_runtime
storage
transfer
build
browser
application
device
display
semantic_ui
knowledge
data
plugin_runtime
scheduler
security_scanner
reproduction
```

WP04 adds no donor/backend names as provider kinds. Specific implementations remain Provider Revisions and Aliases.

### Capability subject kinds

```text
node
facility_revision
facility_instance
provider_revision
provider_instance
```

### Observation dimensions

These are fields/registries, not entity kinds:

```text
node_reachability
node_health
provider_reachability
provider_readiness
provider_health
capability_verification_state
capability_availability_state
resource_pressure_state
```

## Required typed-reference rules

- `node_ref` requires `core.node`.
- `enrollment_ref` requires `core.node_enrollment`.
- `node_capability_snapshot_ref` requires `core.node_capability_snapshot`.
- `node_resource_snapshot_ref` requires `core.node_resource_snapshot`.
- `facility_ref` requires `core.facility`.
- `facility_revision_ref` requires `core.facility_revision`.
- `facility_instance_ref` requires `core.facility_instance`.
- `capability_ref` requires `core.capability`.
- `provider_ref` requires `runtime.provider`.
- `provider_revision_ref` requires `runtime.provider_revision`.
- `provider_instance_ref` requires `runtime.provider_instance`.
- `provider_capability_snapshot_ref` requires `runtime.provider_capability_snapshot`.
- `dispatch_eligibility_ref` requires `runtime.dispatch_eligibility`.

Structural JSON Schema cannot enforce every cross-document kind and generation constraint. The executable conformance harness must use the entity registry, schema catalog and generation/freshness rules.

## Identity prohibitions

The following cannot become canonical entity IDs:

- hostname, IP address or MAC address;
- cloud instance/VM identifier;
- boot ID, agent installation ID or connection/session ID;
- certificate subject or public key fingerprint alone;
- process ID, socket, port, URL or endpoint;
- container, sandbox, VM or service backend ID;
- package name/version alone;
- provider plugin/module name;
- heartbeat sequence;
- capability label in an unversioned manifest;
- GPU/device label or scheduler resource tag;
- health/readiness/liveness status string.

## Classification rules

1. Node Enrollment is not Node identity.
2. Node Generation and connection epoch are monotonic fields bound to observations/work; they are not backend IDs.
3. Capability Definition, Claim, Verification and Availability are separate records.
4. Facility, Facility Revision and Facility Instance are separate.
5. Provider, Provider Revision and Provider Instance are separate.
6. Provider Generation belongs to one Provider Instance incarnation and fences stale work/evidence.
7. reachability, readiness and health are observations/projections, not lifecycle entity kinds.
8. Dispatch Eligibility is operation-specific and time-bounded, not a permanent capability.
9. backend aliases remain scoped `core.alias` records where durable referencing is required.
10. registration does not authorize implementation or deployment.
