# Phase 0B WP08 — Domain Pack, Firmware, Disk, Filesystem and Device

**Status:** CANDIDATE PACKAGE — FINAL CATALOG/CONSISTENCY REVIEW REQUIRED  
**Date:** 2026-07-19  
**Contract families:** `ptah.domain`, `ptah.firmware`, `ptah.disk`, `ptah.device` `0.1.0`  
**Implementation authorization:** NONE

## Objective

Turn the frozen Object decomposition, Domain Pack, firmware/disk/filesystem and Device architecture into exact backend-neutral contracts that an implementation team can build without inventing identity, mutation-safety, recovery or proof semantics.

## Candidate boundary

1. Domain Pack identity survives implementation, Provider and backend replacement; immutable Pack Revisions declare capabilities, requirements and limitations.
2. Detector observations remain plural evidence. Classification is a separate decision retaining conflicts, ambiguity, polyglot, malformed, encrypted, unsupported and unknown outcomes.
3. Domain Request, Run, Inventory, Coverage, decomposition, Validation, Compare and Rebuild remain separate from source Object truth and from one another.
4. Progressive/budgeted decomposition retains valid partial outputs and explicit unknown, skipped and exhausted scope.
5. Firmware Package, Manifest Revision, Component, executable asset, compatibility claim and reviewed exact-context compatibility result remain separate.
6. Static analysis/read/rebuild compatibility cannot authorize physical mutation.
7. Disk/Image identity remains WP03 Object identity; Image Revision, Extent Map, Partition Table, Partition, Filesystem observation/identity and Mount/Inspection Session are interpreted, range-bound records.
8. Read-only inspection cannot silently become writable; untrusted content uses an isolated Provider and explicit cleanup.
9. Device identity survives transient Interface, transport, mode, Connection epoch, Provider and Session changes.
10. Device Session, capability snapshot, Streams, stream observations and Screen Context remain independently fresh and generation-bound.
11. Physical mutation uses current Lease/fence, exact Device/Profile/Session/Connection/Provider context, immutable Plan, reviewed Compatibility Result, Mutation Authorization, backup policy and verification strategy.
12. Every physical retry creates a new WP02 Attempt/nonce and binds the exact current generation/epoch.
13. Protocol presence, handshake, loader/service readiness, write acknowledgement and post-condition read-back remain distinct evidence.
14. Destructive work is blocked without verified immutable backup unless a narrow, expiring and reviewed Mutation Exception records compensating controls.
15. Disconnect or ambiguity during non-idempotent mutation creates uncertain outcome and explicit Device Operation Recovery; blind retry is prohibited.
16. Partial, unsupported, negative, conflicting and inconclusive results remain immutable evidence.
17. Sensitive Device identifiers, credentials, keys, calibration/NV data, logs and screen content follow explicit audience/privacy/redaction/retention rules.

## Required canonical outputs

- WP08 normative conventions;
- entity-kind supplement and any reviewed correction;
- domain schema definitions and all candidate record schemas;
- local offline schema catalog;
- namespaced lifecycle state machines;
- cross-machine invariants;
- migration and compatibility record;
- positive, negative and adversarial fixture manifest;
- consolidated safety net;
- ADR-0025;
- final catalog/identity/transition consistency review.

## Minimum closure proofs

WP08 cannot close unless review confirms:

- all registered WP08 kinds have exactly one canonical schema or an explicit reused family;
- every lifecycle projection references an existing namespaced/versioned machine;
- every catalog URN resolves offline and no duplicate `$id` exists;
- all schema/entity-kind names agree, including reused WP03/WP04/WP05/WP07 families;
- range arithmetic, coverage, generation/epoch, Lease/fence, backup and read-back invariants are represented;
- stale and contradictory evidence cannot overwrite current truth;
- no raw-secret or private-identifier field leaks into ordinary/public records;
- the fixture manifest covers detector conflict, bounded decomposition, disk/filesystem safety, exact firmware compatibility, destructive backup policy, stale fencing, acknowledgement/read-back separation, disconnect recovery and backend replacement;
- migration preserves stable Object/Pack/Device identity and all negative/uncertain history;
- ADR-0025 is accepted before the package is marked candidate-complete.

## Deferred implementation choices

This package does not select:

- file-type detector or parser libraries;
- archive/document/media/executable/domain implementations;
- disk/filesystem mount engines;
- firmware flasher, loader/programmer or vendor protocol stack;
- ADB, Fastboot, MTP, META, DIAG, download-mode, Appium or display/input backend;
- container/VM isolation backend;
- production Device inventory or worker topology.

Those choices occur only after Phase 0C approval and must conform to this boundary.

## Build-readiness consequence

Once accepted, an implementation team can build adapters by mapping backend identifiers to scoped Aliases, emitting exact Ptah records/Receipts and satisfying the fixed proof gates. It must not redesign Device identity, mutation safety, recovery, decomposition coverage or physical success semantics during implementation.
