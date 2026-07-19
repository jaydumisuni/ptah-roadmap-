# Phase 0B WP08 — Final Audit Correction

**Status:** CANDIDATE COMPLETE CORRECTION  
**Date:** 2026-07-19  
**Active catalog:** `urn:ptah:schema-catalog:domain:0.1.2`  
**Implementation authorization:** NONE

## Scope

This is a narrow post-acceptance correction to the completed WP08 package. It does not redesign the Domain Pack, firmware, disk/filesystem or Device architecture.

## Audit gap closed

The accepted `0.1.1` catalog omitted active contracts for two already registered entity kinds and left Device Operation Recovery without its own namespaced lifecycle:

- `firmware.compatibility_claim`;
- `device.protocol_operation`;
- `device.operation_recovery` lifecycle and prior/new generation evidence.

These omissions would otherwise force implementation-time invention or identity collapse.

## Corrective outputs

- Firmware Compatibility Claim schema `0.1.0`;
- Device Protocol Operation schema `0.1.0`;
- Device Operation Recovery schema `0.1.1`;
- Device Protocol Operation lifecycle `0.1.0`;
- Device Operation Recovery lifecycle `0.1.0`;
- Domain catalog `0.1.2` with 47 schemas and 15 lifecycle machines;
- entity-kind ownership correction;
- migration `0.1.1` → `0.1.2`;
- 22 targeted cross-record fixtures;
- additive correction safety net;
- final consistency review;
- ADR-0025A.

## Implementation-ready boundaries added

1. Source/vendor/tool compatibility assertions are represented without being mistaken for exact live compatibility or authority.
2. Generic Device protocol interactions have a neutral record usable by ADB, Fastboot, MTP, serial, vendor download, META, DIAG, Appium, accessibility, display/input, shell and file-transfer adapters.
3. WP02 Activity/Operation/Attempt remain canonical; Device and Firmware records are typed projections/aggregates.
4. Protocol acknowledgement remains separate from verified post-condition state.
5. Uncertain physical effects require a lifecycle-bearing Recovery record.
6. Recovery binds old and new generations and cannot reuse stale authority.
7. Retry after recovery always creates a new WP02 Attempt.

## Non-regression

All selected `0.1.1` records and accepted ADR-0025 boundaries remain unchanged. The correction only fills missing active identity/lifecycle contracts and supersedes Recovery candidate `0.1.0`.

## Completion statement

After acceptance of ADR-0025A and catalog `0.1.2`, WP08 is detailed enough for later adapter implementation without inventing compatibility-claim, protocol-operation or recovery semantics.

Executable conformance remains deferred to WP13, and implementation remains prohibited until Phase 0C authorization.
