# Phase 0B WP08 — Final Consistency Review 0.1.2

**Status:** PASSED FOR CANDIDATE CONTRACT USE  
**Date:** 2026-07-19  
**Reviewed catalog:** `urn:ptah:schema-catalog:domain:0.1.2`

## Review purpose

Re-open only the identity/lifecycle closure gap found after WP08 catalog `0.1.1` acceptance. This review does not reconsider the accepted WP08 Domain/Firmware/Disk/Filesystem/Device architecture and does not authorize implementation.

## Finding

Catalog `0.1.1` correctly selected exact Provider/connection/generation schemas and strong mutation/mount/recovery boundaries, but it did not activate two entity kinds already registered for WP08 and did not provide a lifecycle projection for Device Operation Recovery:

- `firmware.compatibility_claim`;
- `device.protocol_operation`;
- `device.operation_recovery` lifecycle/generation correction.

Treating `0.1.1` as final would force implementation teams either to invent these semantics or collapse them into neighbouring records.

## Corrective inventory

Catalog `0.1.2` contains:

- **47 schema entries**;
- **47 unique absolute schema URNs**;
- **15 lifecycle entries**;
- **15 unique namespaced lifecycle names**;
- seven exact dependency catalogs;
- no network resolution requirement;
- explicit supersession of Device Operation Recovery `0.1.0`.

Added records:

1. `firmware.compatibility_claim` `0.1.0`;
2. `device.protocol_operation` `0.1.0`;
3. `device.operation_recovery` `0.1.1`.

Added lifecycle machines:

1. `device.protocol_operation.lifecycle` `0.1.0`;
2. `device.operation_recovery.lifecycle` `0.1.0`.

## Non-regression review

Every selected `0.1.1` correction remains unchanged, including:

- exact Provider revision/instance/generation and truthful locality;
- Domain Run Dispatch Eligibility and capability evidence;
- exact firmware Compatibility Result context;
- transport authorization and cleanup protocol stages;
- immutable Firmware Operation Plan;
- firmware Operation/Verification exact Plan, Profile, Interface, Connection and Provider bindings;
- writable-copy/overlay filesystem rules and mount cleanup quarantine;
- Device Profile, Session, capability snapshot, Stream, Stream Observation, Screen Context and Backup exact connection bindings;
- Device Session cleanup-failure quarantine;
- explicit Recovery before uncertain firmware work resumes.

## Identity review

Passed boundaries:

- Compatibility Claim is immutable evidence and cannot become exact Compatibility Result or authority.
- Device Protocol Operation projects one Device protocol interaction while WP02 Operation/Attempt remain canonical execution identity.
- Firmware Operation remains the specialist mutation aggregate with Plan/Authorization/backup/Verification.
- Device Operation Recovery remains a new reconciliation record and cannot rewrite the original uncertain Operation.
- `runtime.lease` remains canonical Device ownership/fencing authority; no `device.lease` exists.
- `object.decomposition_run` remains canonical decomposition identity; no duplicate Domain decomposition identity exists.
- WP03 Content/Object Revision remains canonical byte identity for firmware, disks and backups.

## Lifecycle review

Passed boundaries:

- ACK and verified completion are distinct terminal claims.
- `uncertain` is non-terminal and requires reconciliation.
- protocol retries require new WP02 Attempts.
- Recovery reacquisition cannot reuse stale Session, Connection epoch, Provider generation, Lease or fence.
- Recovery may conclude verified, limited, safe-to-resume, safe-to-retry-new-attempt, manual intervention, unrecoverable, inconclusive or blocked.
- safe retry explicitly requires a new Attempt.
- unknown states are rejected and breaking changes require migration mapping/manual review.

## Migration review

Passed directional rules:

- legacy vendor/tool compatibility information maps to Claims, not Results;
- legacy protocol logs map to Device Protocol Operation only with exact execution/context correlation;
- absent correlation preserves logs as observations/Receipts/Artifacts;
- Recovery `0.1.0` upgrades only with lifecycle and prior/new generation evidence;
- missing evidence remains legacy/manual-review/inconclusive;
- no acknowledgement, unknown or inconclusive result migrates to verified success.

## Conformance review

The correction adds 22 cross-record scenarios with expected result codes covering:

- Claim/Result/authority separation;
- contradictory Claims;
- protocol projection and WP02 identity;
- firmware/protocol cross-linking without collapse;
- ACK versus verification;
- Attempt reuse and stale context;
- Recovery migration, stale authority, reconciliation and immutable history;
- catalog count, active-kind coverage and duplicate-family prevention.

Executable harness proof remains deferred to WP13, consistent with every Phase 0B candidate package.

## Decision

The correction is internally consistent and required for implementation-ready roadmap closure.

Recommended active WP08 catalog:

```text
urn:ptah:schema-catalog:domain:0.1.2
```

WP08 remains **CANDIDATE COMPLETE** after this correction. Runtime implementation, dependency selection and live Device mutation remain unauthorized until Phase 0C.
