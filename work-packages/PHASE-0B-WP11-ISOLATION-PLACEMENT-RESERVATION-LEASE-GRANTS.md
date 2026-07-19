# Phase 0B WP11 — Isolation, Placement, Reservation, Lease and Secure Grants

**Status:** CANDIDATE BLUEPRINT
**Implementation authorization:** NONE

## Required entities

- Isolation Profile and immutable Profile Revision;
- Placement Request, Candidate, Decision and rejection evidence;
- Resource Requirement, Capacity Snapshot, Reservation and Consumption Observation;
- Lease, Fence, Renewal, Revocation and expiry;
- Secure Grant, Credential Reference, Delivery, Use, Cleanup and leakage evidence;
- Network/port exposure grant;
- Provider/Node affinity, anti-affinity, locality and failure-domain constraints;
- admission, preemption, eviction and migration decisions.

## Core laws

1. Requested isolation, available isolation and proven effective isolation remain separate.
2. Container, VM, process, emulator and physical-device boundaries are typed, not one security level.
3. Placement is operation-specific and exact-generation-bound.
4. Reservation is not consumption; capacity observation is not guaranteed availability.
5. Every state-changing holder must present a current Lease and Fence.
6. Expired/revoked grants cannot authorize new access.
7. Raw secrets never enter ordinary records, logs, snapshots or public bundles.
8. Preemption and eviction preserve Activity/Attempt and partial-output truth.
9. Stronger isolation backends may replace weaker providers without changing Facility identity.

## Proof cases

- stale fence cannot commit work after reassignment;
- oversubscribed capacity is rejected or explicitly degraded;
- reservation expiry releases capacity without deleting history;
- secret delivery is scoped to one Attempt and cleanup is independently verified;
- leakage detection produces a retained Finding and blocks publication where policy requires;
- Provider crash fences old generation before replacement dispatch;
- migration changes placement/attempt generation but preserves Activity identity;
- unsupported isolation requirement fails closed.

## Outputs

Conventions, entity kinds, schemas/catalog, lifecycle machines, migration, fixtures, safety net, package record and ADR-0028.
