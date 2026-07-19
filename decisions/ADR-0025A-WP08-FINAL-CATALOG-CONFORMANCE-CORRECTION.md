# ADR-0025A — WP08 Final Catalog and Conformance Correction

**Status:** ACCEPTED CORRECTION TO ADR-0025  
**Date:** 2026-07-19  
**Implementation authorization:** NONE

## Context

ADR-0025 accepted the WP08 Domain Pack, Firmware, Disk, Filesystem and Device architecture against catalog `0.1.0` with 44 active schemas.

A final consistency review preserved that architecture but found machine-readable precision gaps:

1. stable `disk.image` identity was omitted from the active catalog;
2. current Pack Compatibility and Domain Runs lacked complete Provider revision/generation/epoch, capability, Dispatch Eligibility and locality evidence;
3. Firmware physical execution needed an independently addressable immutable Operation Plan;
4. Firmware Compatibility needed backup-specific authority distinct from read/write;
5. Protocol Stage Observation omitted transport authorization and cleanup verification;
6. Firmware Operation applied mutation authority too broadly and did not require the Plan;
7. Firmware Verification, Device Profile, Session, Streams, Screen Context and Backup lacked complete exact Interface/Connection/Provider context;
8. writable Mount Session could be interpreted as direct source mutation;
9. Device Session closure did not require verified cleanup/quarantine on failure;
10. uncertain Firmware Operation could resume without an explicit Recovery decision and new Attempt.

No accepted WP08 architectural boundary changed.

## Decision

The authoritative WP08 candidate catalog is:

- `schemas/phase-0b/domain/schema-catalog.v0.1.1.json`.

It contains **45 active schemas** and supersedes catalog `0.1.0`.

The final active schema selection includes:

- Domain Pack Compatibility `0.1.1`;
- Domain Operation Run `0.1.1`;
- Firmware Compatibility Result `0.1.1`;
- Firmware Protocol Stage Observation `0.1.1`;
- Firmware Operation Plan `0.1.0`;
- Firmware Operation `0.1.1`;
- Firmware Operation Verification `0.1.1`;
- stable Disk Image `0.1.0`;
- Filesystem Mount Session `0.1.1`;
- Device Profile Revision `0.1.1`;
- Device Session `0.1.1`;
- Device Session Capability Snapshot `0.1.1`;
- Device Stream `0.1.1`;
- Device Stream Observation `0.1.1`;
- Device Screen Context `0.1.1`;
- Device Backup `0.1.1`;
- all remaining active schemas at the versions listed in catalog `0.1.1`.

The final active lifecycle selection is:

- Device Session lifecycle `0.1.1`;
- Firmware Operation lifecycle `0.1.1`;
- the other eleven WP08 lifecycle machines at `0.1.0`.

Every superseded record remains retained as candidate history and is not selected downstream.

## Normative correction

The active convention set is:

- `contracts/phase-0b/domain/DOMAIN-FIRMWARE-DISK-DEVICE-CONVENTIONS.md`;
- `contracts/phase-0b/domain/DOMAIN-FIRMWARE-DISK-DEVICE-CONVENTIONS.v0.1.1.md`.

The correction adds final precision for:

- `compatible_for_backup`;
- immutable Firmware Operation Plan;
- `transport_authorized` and `cleanup_verified` protocol stages;
- cleanup failure requiring quarantine;
- public Device-data export redaction/remapping;
- parked `.P5C` status;
- separate driver/host-admin Activities.

The entity-kind correction remains:

- `contracts/phase-0b/common/ENTITY-KIND-REGISTRY-WP08-CORRECTION-0.1.1.md`.

## Migration and conformance correction

The active migration set is:

- `migrations/phase-0b/WP08-DOMAIN-FIRMWARE-DISK-DEVICE-MIGRATION-COMPATIBILITY.md`;
- `migrations/phase-0b/WP08-DOMAIN-FIRMWARE-DISK-DEVICE-MIGRATION-COMPATIBILITY.v0.1.1.md`.

The active safety net is:

- `conformance/PHASE-0B-WP08-DOMAIN-FIRMWARE-DISK-DEVICE-SAFETY-NET.md`;
- `conformance/PHASE-0B-WP08-DOMAIN-FIRMWARE-DISK-DEVICE-SAFETY-NET.v0.1.1.md`.

The active fixture corpus is:

- base `domain-firmware-disk-device-cases.v0.1.0.json`;
- correction `domain-firmware-disk-device-cases.v0.1.1.json`.

The correction corpus adds mandatory proof for:

- exact Node-local and remote Domain execution;
- no fictional Nodes;
- Operation Plan presence/freshness;
- read versus backup versus write compatibility;
- writable copy/overlay targets;
- per-binding Device Session contexts;
- stale Profile/Stream/Screen Context rejection;
- cleanup failure quarantine;
- Recovery-gated uncertain resume;
- sensitive public export restrictions;
- driver installation versus Interface readiness;
- parked `.P5C` behavior.

## Effect on ADR-0025 and WP08

Where ADR-0025 or the original WP08 work package points to catalog `0.1.0`, 44 schemas or the original context-light records as active, interpret the active package through:

- catalog `0.1.1`;
- `work-packages/PHASE-0B-WP08-DOMAIN-FIRMWARE-DISK-DEVICE.v0.1.1.md`;
- this ADR correction.

WP08 remains candidate-complete for downstream Phase 0B contract design.

No parser, filesystem appliance, driver, USB/runtime service, Device Provider, loader/programmer, firmware flasher, display/input backend, physical test hardware or deployment is authorized.

## Do-not-break rule

> Final WP08 authority requires exact context, immutable planning, bounded physical authorization, verified backup/read-back, explicit writable targets, cleanup quarantine and Recovery-gated retry. Correcting the catalog does not authorize implementation.
