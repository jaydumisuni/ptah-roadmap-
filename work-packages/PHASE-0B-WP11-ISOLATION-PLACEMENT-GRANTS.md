# Phase 0B WP11 — Isolation, Placement, Reservation, Lease and Secure Grants

**Status:** CANDIDATE COMPLETE ON BRANCH

## Accepted candidate inventory

- catalog `urn:ptah:schema-catalog:isolation:0.1.0`;
- 28 schemas including shared definitions;
- seven lifecycle machines;
- 24 cross-machine invariants;
- directional migration and backend-replacement record;
- 36 positive/negative/adversarial conformance scenarios;
- consolidated safety net;
- final consistency review;
- ADR-0028.

## Boundary

WP11 defines policy and proof for process/container/VM/emulator/device-backed isolation, placement, capacity, reservation, consumption, admission, preemption, eviction, migration, Lease/fencing, secure grants, secret delivery/cleanup, network/device/filesystem exposure and runtime checkpoint/recovery.

It does not choose containerd, Docker, gVisor, Kata, Firecracker, E2B, Daytona, Coder or any production scheduler. Those remain candidate implementations for Phase 0C selection.

## Closure claims

Builders no longer need to invent how isolation downgrade, stale capacity, overcommit, split-brain ownership, secret injection, public exposure, Device epoch changes or migration uncertainty are represented. Each has explicit identity, lifecycle, evidence and negative proof cases.
