# Phase 0B WP08 — Closure Gates

**Status:** ACTIVE CLOSURE PLAN
**Implementation authorization:** NONE

WP08 closes only when the canonical Domain Pack, firmware, disk/filesystem and Device contracts satisfy all gates below.

## Required contract groups

1. Domain Pack, immutable Pack Revision, capability declaration and directional compatibility.
2. Detector Observation, accepted classification, confidence, disagreement and bounded coverage.
3. Inventory, Decomposition, Validation, Compare, Rebuild and Execute request/run/result separation.
4. Progressive decomposition budgets, retained unknown gaps and immutable source Object identity.
5. Firmware Package, Manifest, Component, target compatibility, loader/programmer/toolchain evidence.
6. Disk image, partition table, partition, filesystem, range/offset and mount/inspection Session identity.
7. Read-only inspection, static transformation and state-changing physical mutation authority separation.
8. Device, Interface incarnation, Connection epoch, Session, Stream and Screen Context identity.
9. Lease/fence, exact Provider generation, protocol stage and physical Operation/Attempt correlation.
10. Immutable backup and explicit approval before destructive operations.
11. Protocol acknowledgement separated from write completion and post-operation read-back verification.
12. Disconnect, partial write, unsupported family and uncertain physical outcomes retained honestly.

## Mandatory proof cases

- conflicting detectors coexist without overwriting evidence;
- bounded decomposition yields useful partial output plus explicit gaps;
- parser replacement preserves source identity and produces new derived revisions;
- partition ranges are exact and overlap-checked;
- read-only sessions cannot silently become writable;
- stale Lease, fence, generation or connection evidence cannot mutate a Device;
- destructive work is blocked without backup and approval;
- acknowledgement without read-back cannot become verified success;
- disconnect during non-idempotent write becomes uncertain and requires reconciliation;
- backend replacement preserves canonical Object and Device history.

## Required package outputs

- normative conventions;
- entity-kind registry supplement;
- versioned schemas and local catalog;
- namespaced lifecycle machines;
- migration/compatibility record;
- lawful positive and negative fixtures;
- consolidated safety net;
- WP08 package record;
- ADR-0025 after consistency review.
