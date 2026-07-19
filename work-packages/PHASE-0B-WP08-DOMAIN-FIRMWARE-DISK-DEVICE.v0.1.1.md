# Phase 0B WP08 — Final Catalog and Conformance Correction 0.1.1

**Status:** CANDIDATE COMPLETE CORRECTION  
**Date:** 2026-07-19  
**Parent package:** `PHASE-0B-WP08-DOMAIN-FIRMWARE-DISK-DEVICE.md`  
**Implementation authorization:** NONE

## Purpose

Preserve the accepted WP08 package while correcting its machine-readable catalog, lifecycle, migration and conformance references after the final consistency review.

All architectural boundaries in the parent package remain accepted.

## Authoritative package selection

The active catalog is:

- `schemas/phase-0b/domain/schema-catalog.v0.1.1.json`.

It supersedes catalog `0.1.0` and contains **45 active schemas**, adding/selecting:

- stable `disk.image` root;
- `firmware.operation_plan`;
- exact-context Pack Compatibility and Domain Operation Run `0.1.1`;
- backup-aware Firmware Compatibility Result `0.1.1`;
- corrected Protocol Stage Observation, Firmware Operation and Verification `0.1.1`;
- corrected Filesystem Mount Session `0.1.1`;
- exact-context Device Profile, Session, Capability Snapshot, Stream, Stream Observation, Screen Context and Backup `0.1.1`.

The active lifecycle set remains 13 machines, selecting:

- `device.session.lifecycle` `0.1.1`;
- `firmware.operation.lifecycle` `0.1.1`;
- the other eleven lifecycles at `0.1.0`.

Every superseded `0.1.0` record is retained as candidate history and listed in catalog `0.1.1`.

## Active normative records

The active convention set is:

- `contracts/phase-0b/domain/DOMAIN-FIRMWARE-DISK-DEVICE-CONVENTIONS.md`;
- `contracts/phase-0b/domain/DOMAIN-FIRMWARE-DISK-DEVICE-CONVENTIONS.v0.1.1.md`.

The active entity-kind set is:

- `contracts/phase-0b/common/ENTITY-KIND-REGISTRY-WP08-SUPPLEMENT.md`;
- `contracts/phase-0b/common/ENTITY-KIND-REGISTRY-WP08-CORRECTION-0.1.1.md`.

The correction adds `firmware.operation_plan` and final rules for backup compatibility, transport authorization, cleanup verification/quarantine, sensitive public export, parked `.P5C` behavior and separate driver/host-admin Activities.

## Active migration and conformance records

Migration:

- `migrations/phase-0b/WP08-DOMAIN-FIRMWARE-DISK-DEVICE-MIGRATION-COMPATIBILITY.md`;
- `migrations/phase-0b/WP08-DOMAIN-FIRMWARE-DISK-DEVICE-MIGRATION-COMPATIBILITY.v0.1.1.md`.

Safety net:

- `conformance/PHASE-0B-WP08-DOMAIN-FIRMWARE-DISK-DEVICE-SAFETY-NET.md`;
- `conformance/PHASE-0B-WP08-DOMAIN-FIRMWARE-DISK-DEVICE-SAFETY-NET.v0.1.1.md`.

Fixtures:

- `conformance/fixtures/phase-0b/wp08/domain-firmware-disk-device-cases.v0.1.0.json`;
- `conformance/fixtures/phase-0b/wp08/domain-firmware-disk-device-cases.v0.1.1.json`.

The correction corpus adds exact Node-local/remote Domain execution, Plan freshness, read-versus-backup compatibility, explicit writable copies/overlays, per-binding Device Session contexts, cleanup quarantine, recovery-gated uncertain resume, public redaction, driver/readiness separation and parked `.P5C` cases.

## Final accepted precision

WP08 downstream users must preserve:

1. exact Provider revision, generation and connection epoch for current Domain/Device evidence;
2. truthful local versus remote execution without fictional Nodes;
3. immutable Firmware Operation Plan before physical execution;
4. general physical authority for every Device Operation and separate Mutation Authorization for destructive classes;
5. operation-specific backup compatibility and verified Backup or exact exception before destructive mutation;
6. writable filesystem inspection only through explicit copy/overlay targets;
7. Device Session capabilities mapped to exact Interface/Connection/Provider bindings;
8. stale Profile/Stream/Screen Context evidence rejected after epoch/generation change;
9. ordinary Session closure only after verified cleanup; cleanup failure requires Device quarantine;
10. uncertain firmware work resumed only through explicit Recovery, rediscovery, current authority and a new Attempt;
11. `.P5C` remains parked/unsupported;
12. driver installation remains separate from Device Interface/readiness proof.

## Acceptance decision

- `decisions/ADR-0025-DOMAIN-PACK-FIRMWARE-DISK-DEVICE-OPERATION-BOUNDARY.md`;
- `decisions/ADR-0025A-WP08-FINAL-CATALOG-CONFORMANCE-CORRECTION.md`.

## Do-not-build rule

> This correction finalizes candidate contracts only. It does not authorize parser, filesystem appliance, driver, Device Provider, loader/programmer, flashing, display/input, physical-hardware testing or deployment.
