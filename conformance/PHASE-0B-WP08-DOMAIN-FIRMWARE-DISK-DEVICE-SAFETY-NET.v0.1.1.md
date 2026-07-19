# Phase 0B WP08 — Domain, Firmware, Disk and Device Safety Net 0.1.1 Corrections

**Status:** CANDIDATE CORRECTION  
**Date:** 2026-07-19  
**Parent:** `PHASE-0B-WP08-DOMAIN-FIRMWARE-DISK-DEVICE-SAFETY-NET.md`  
**Authoritative catalog:** `schemas/phase-0b/domain/schema-catalog.v0.1.1.json`  
**Fixture correction:** `conformance/fixtures/phase-0b/wp08/domain-firmware-disk-device-cases.v0.1.1.json`

## Purpose

Preserve the base WP08 safety net while aligning its exit criteria and invariants with the final 45-schema catalog and corrected lifecycle/context records.

All base invariants remain active except where explicitly replaced or extended below.

---

# C-001 — Active package count and selection

The base exit condition is replaced by:

1. all **45 active schemas** resolve through catalog `0.1.1`;
2. all **13 lifecycle machines** resolve, selecting Device Session lifecycle `0.1.1` and Firmware Operation lifecycle `0.1.1`;
3. the active convention set includes `DOMAIN-FIRMWARE-DISK-DEVICE-CONVENTIONS.v0.1.1.md`;
4. the active entity-kind set includes `ENTITY-KIND-REGISTRY-WP08-CORRECTION-0.1.1.md`;
5. migration uses the base record plus migration correction `0.1.1`;
6. fixtures use the base corpus plus correction corpus `0.1.1`;
7. implementation/backend selection remains blocked.

Catalog `0.1.0` and every superseded schema/lifecycle remain candidate history only.

---

# C-002 — Exact Domain execution context

Every current Pack Compatibility and Domain Operation Run must bind:

- Pack Revision and requested operation/scope;
- Provider Revision, Instance, generation and connection epoch;
- current Provider Capability Snapshot;
- current Dispatch Eligibility for a Run;
- Workspace Revision and Materialization generation for a Run;
- exactly one locality form.

Node-local execution additionally requires exact Node generation and current Node capability/resource snapshots.

Remote-service execution requires approved remote-service identity/authority and must not fabricate Node evidence.

Mixed locality, stale compatibility or generation mismatch is invalid.

---

# C-003 — Firmware planning, authority and physical proof

The harness must preserve:

```text
parsed package operation graph
Firmware Operation Plan
physical authority
Mutation Authorization where destructive
verified Device Backup or exact exception where required
WP02 Operation and Attempt
protocol-stage observations
Firmware Operation
Operation Verification
Recovery/cleanup
```

Rules:

- parsed scatter/rawprogram/patch/PIT/payload instructions cannot execute directly;
- a Plan cannot authorize or prove execution;
- target/source/Profile/layout/epoch/Provider/tool/authority change invalidates the Plan;
- general physical authority applies to every connected-device Operation;
- Mutation Authorization applies only to destructive/high-risk classes;
- read compatibility is not backup compatibility;
- backup compatibility is not write compatibility;
- process exit or ACK is not verified physical state;
- `completed_verified` requires matching Operation Verification under exact current context.

---

# C-004 — Device observation and Session binding

Device Profile Revision, Session, capability snapshot, Stream, Stream Observation, Screen Context, Backup and Firmware Verification must bind exact Interface, Connection epoch and Provider revision/instance/generation.

A Device Session with several transports/providers retains per-binding contexts and capability scopes under one Lease/fence.

Rules:

- loss of one binding cannot imply universal Session failure;
- stale Profile/Stream/Screen Context cannot authorize current input, compatibility or mutation;
- old-epoch Receipts remain historical only;
- Device identity remains stable while Interfaces/Connections/Providers change.

---

# C-005 — Writable filesystem inspection

Every writable Mount Session uses exactly one explicit mutation target:

```text
writable_copy
or
writable_overlay
```

It requires:

- write authority;
- a distinct writable target Object Revision;
- copy/overlay Artifact;
- exact Provider revision/generation/epoch and Dispatch Eligibility;
- truthful local/remote locality;
- cleanup/unmount evidence.

The original untrusted source Object Revision is never directly writable.

---

# C-006 — Session cleanup and Device quarantine

Ordinary Device Session `closed` requires verified cleanup/revocation for the applicable:

- Streams and forwarding;
- helper binaries/services;
- credentials and grants;
- accounts/data created by the Session;
- clipboard/input/display/control paths;
- Lease/fence authority;
- temporary files and host/device changes.

If cleanup cannot be proven:

- lifecycle becomes terminal `cleanup_failed`;
- Device quarantine is required;
- ordinary reassignment is blocked;
- Provider disconnect/Session close cannot fabricate cleanup success;
- quarantine release requires authorized remediation and verification while preserving history.

---

# C-007 — Uncertain physical-operation recovery

A non-idempotent Firmware Operation in `uncertain` cannot return to preparation/execution automatically.

Resume requires:

- Device Operation Recovery record;
- authoritative current Profile/layout/read-back or bounded state discovery;
- current Plan and Compatibility;
- current Session/Lease/fence/Connection/Provider context;
- explicit recovery/resume authority;
- new WP02 Attempt/nonce.

Without these, the Operation remains uncertain and the target may remain quarantined.

---

# C-008 — Backup, privacy, parked formats and drivers

- `compatible_for_backup` requires exact range, digest, durable Location, privacy/retention and restoration-compatibility evidence.
- Device Backup requires actual ranges/sizes, immutable Objects/digests, Locations and verification.
- public exports use allowlisted/remapped/redacted Device/Profile/Backup/Screen evidence.
- `.P5C` remains parked; extension-only routing to PAC semantics or physical execution is rejected.
- driver/host-admin changes are separate Activities; successful installation does not prove Interface enumeration, handshake, Provider readiness or mutation compatibility.

---

# Additional WP13 property invariants

- active catalog contains 45 unique schema IDs/paths;
- every corrected `0.1.1` record is selected and its superseded `0.1.0` is not active;
- Domain local/remote locality is XOR and all referenced generations match;
- every physical Firmware Operation references one current immutable Operation Plan;
- every destructive Operation references current Mutation Authorization and verified Backup or exact exception;
- `compatible_for_backup` has backup capability plus restoration constraint evidence;
- every writable Mount Session target differs from the immutable source revision;
- each Device Session capability maps to one or more exact connection-binding keys;
- every Stream Observation and Screen Context matches parent Stream/Session Interface epoch and Provider generation;
- Session `closed` has cleanup verification; `cleanup_failed` has quarantine decision;
- uncertain Firmware Operation cannot transition to preparing except through `resume_after_reconciliation` with Recovery evidence;
- public fixture/export bytes contain no raw sensitive Device identifiers or protected content;
- `.P5C` never appears as accepted parser/mutation capability absent a future reopening migration.

## Do-not-break rule

> Final conformance must prove exact context, immutable planning, bounded authority, safe backup, truthful writable targets, verified cleanup and recovery-gated physical mutation. Structural validity alone is insufficient.
