# ADR-0025A — WP08 Final Identity and Lifecycle Correction

**Status:** ACCEPTED  
**Date:** 2026-07-19  
**Corrects:** ADR-0025 without replacing its accepted boundary

## Context

ADR-0025 and WP08 catalog `0.1.1` established the accepted Domain Pack, firmware, disk/filesystem and Device boundary. A final registry-to-catalog audit found three active-contract omissions:

1. `firmware.compatibility_claim` was registered but had no active schema;
2. `device.protocol_operation` was registered but had no active schema or lifecycle;
3. `device.operation_recovery` `0.1.0` had no namespaced lifecycle projection and did not require explicit prior/new Provider-generation evidence.

Leaving these gaps would force implementation teams to invent semantics or collapse source compatibility assertions, generic Device protocol work and uncertain-operation recovery into neighbouring records.

## Decision

Adopt catalog `urn:ptah:schema-catalog:domain:0.1.2` and the following corrections:

- activate immutable `firmware.compatibility_claim` `0.1.0` as evidence only;
- retain exact live-context `firmware.compatibility_result` as the reviewed compatibility decision;
- activate `device.protocol_operation` `0.1.0` as a Device-domain projection over canonical WP02 Activity/Operation/Attempt identity;
- preserve `firmware.operation` as the specialist physical firmware mutation aggregate;
- activate `device.protocol_operation.lifecycle` `0.1.0` with acknowledgement, verification and uncertainty separation;
- supersede Device Operation Recovery candidate `0.1.0` with lifecycle-bearing `0.1.1`;
- activate `device.operation_recovery.lifecycle` `0.1.0` with explicit reacquisition, reconciliation and bounded recovery decisions;
- require prior/new Connection epoch and Provider-generation evidence where applicable;
- require every retry after recovery to use a new WP02 Attempt and current authority.

## Identity ownership

- WP02 Operation/Attempt remain canonical execution identity.
- Device Protocol Operation is a typed projection, never a replacement.
- Firmware Operation is a specialist aggregate with Plan, Authorization, backup and Verification.
- Compatibility Claim is evidence; Compatibility Result is reviewed exact-context decision.
- Recovery is append-only reconciliation and cannot rewrite the original uncertain Operation.
- Device ownership/fencing continues to reuse `runtime.lease`.
- Decomposition continues to reuse `object.decomposition_run`.
- Exact bytes continue to use WP03 Content/Object Revision identity.

## Consequences

### Positive

- Adapter implementers no longer need to invent a generic Device operation model.
- Vendor/tool support information can be represented honestly without becoming authority.
- ADB/Fastboot/MTP/META/DIAG and similar protocols map to one neutral contract while specialist firmware safety remains intact.
- Recovery semantics are build-ready and explicitly generation-fenced.
- The active catalog becomes registry-complete for these WP08 kinds.

### Cost

- Two additional active schemas and two lifecycle machines must be supported by conformance tooling.
- Legacy protocol/recovery records without exact correlation may remain observation-only or inconclusive.
- Catalog consumers must move from `0.1.1` to `0.1.2`.

## Rejected alternatives

1. **Remove the registered tokens** — loses useful distinctions already required by the Device architecture.
2. **Treat Compatibility Claim as Compatibility Result** — collapses evidence into authority.
3. **Use only Firmware Operation for every Device protocol action** — wrongly imposes firmware-mutation semantics on shell, package, display, control and transfer operations.
4. **Use only Device Protocol Operation for firmware mutation** — loses immutable Plan, Authorization, backup and read-back requirements.
5. **Leave Recovery as a result-only record** — implementation would lack explicit recovery progression and fencing.
6. **Infer missing generation evidence during migration** — creates false continuity and unsafe retry authority.

## Acceptance evidence

- final consistency review records 47 unique schema URNs and 15 unique lifecycle names;
- all accepted `0.1.1` selections remain unchanged;
- migration rules preserve history and reject unsupported upgrades;
- 22 targeted positive/negative fixtures cover the correction;
- correction safety net defines structural, semantic and migration gates.

## Constraint

This decision authorizes candidate contract use only. It does not authorize dependency selection, runtime implementation or live Device mutation. Executable conformance remains a WP13 requirement.
