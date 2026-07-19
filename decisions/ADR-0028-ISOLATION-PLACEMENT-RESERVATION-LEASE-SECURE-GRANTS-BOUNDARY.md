# ADR-0028 — Isolation, Placement, Reservation, Lease and Secure Grants Boundary

**Status:** ACCEPTED

## Decision

Ptah will represent isolation policy, runtime realization, placement, admission, resource reservation/consumption, preemption/eviction, migration, Lease/fencing and secure access as separate typed records with namespaced lifecycle machines.

Canonical `runtime.lease` remains the authority identity. WP11 adds typed projections and fence observations; it does not create a competing lock system.

Secure Grants contain scope, expiry, revocation, generation and fence context only. Raw secrets never enter canonical records. Secret delivery and cleanup verification remain distinct Activities/Operations/Attempts.

Network, Device and filesystem access require explicit, bounded, expiring grants. Checkpoint evidence cannot become recovered-runtime proof. Migration requires new target generations, Attempts, Leases/fences and target verification before cutover.

## Consequences

- container, VM, process, emulator, remote sandbox and future backends remain replaceable;
- stale capacity, generations, Leases, fences and grants are rejectable by contract;
- silent isolation downgrade, hidden overcommit and split-brain ownership are prohibited;
- backend acknowledgement cannot become cleanup, isolation, migration or recovery success;
- implementation can proceed later without inventing authority and failure semantics.

## Deferred

Exact backends, schedulers, secret brokers and runtime dependencies remain Phase 0C decisions. Executable conformance remains WP13.
