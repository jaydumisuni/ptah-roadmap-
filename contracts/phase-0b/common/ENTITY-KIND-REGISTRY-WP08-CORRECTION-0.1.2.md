# WP08 Entity-Kind Registry Correction 0.1.2

**Status:** CANDIDATE CORRECTION  
**Date:** 2026-07-19  
**Applies to:** `ptah.entity-kind`, WP08 Domain/Firmware/Disk/Device contracts

This correction activates and disambiguates three WP08 kinds already present in the broad Phase 0B registry. It does not repurpose any frozen token and does not authorize implementation.

## Active kinds corrected

### `firmware.compatibility_claim`

An immutable source, vendor, package, tool, detector or operator assertion about possible firmware/target compatibility.

Rules:

1. A Claim is evidence, never execution or mutation authority.
2. A Claim may be broad, stale, incomplete, contradictory or wrong.
3. Exact physical compatibility remains `firmware.compatibility_result`, bound to the current Device Profile Revision, Interface, Connection epoch, Provider revision/instance/generation, requested operation, target ranges, assets, backup/read-back capability and evidence.
4. A filename, model name, chipset string or vendor matrix may support a Claim but cannot become a Compatibility Result by itself.
5. New evidence creates a new Claim or reviewed Result; historical Claims are not rewritten.

### `device.protocol_operation`

A Device-domain projection over one protocol interaction, bound to exact Device/Session/Interface/Connection/Provider context and canonical WP02 execution identity.

Rules:

1. WP02 `core.operation` and `core.attempt` remain the canonical logical and physical execution identities.
2. `device.protocol_operation` never replaces or duplicates WP02 Operation/Attempt identity; it references them.
3. Every physical retry uses a new WP02 Attempt and nonce.
4. A specialist firmware mutation may additionally reference `firmware.operation`; the two records express different scopes:
   - `device.protocol_operation`: one Device protocol/control projection;
   - `firmware.operation`: one specialist physical firmware mutation aggregate with Plan, Authorization, backup and Verification.
5. ADB, Fastboot, MTP, USB serial, vendor download, META, DIAG, Appium, accessibility, display/input, shell, package-management and file-transfer backends map to this neutral projection without becoming canonical identity.
6. Protocol acknowledgement remains distinct from verified post-condition state.

### `device.operation_recovery`

A lifecycle-bearing reconciliation record for one uncertain physical Device or firmware operation.

Rules:

1. Version `0.1.1` supersedes candidate schema `0.1.0`.
2. Recovery binds exact prior Session, Connection epoch, Provider generation and Attempts.
3. Reacquisition creates or references a new current Session/Connection epoch/Provider generation; stale authority is never continued silently.
4. Recovery may conclude verified, limited, safe-to-resume, safe-to-retry-new-attempt, manual-intervention-required, unrecoverable, inconclusive or blocked.
5. `safe_to_retry_new_attempt` never permits Attempt reuse.
6. Recovery evidence cannot rewrite the original uncertain Operation or its Receipts.

## Explicit non-duplication rules

- No `device.lease` entity kind is introduced. Device ownership and fencing reuse canonical `runtime.lease` with the registered Device lease kind/scope.
- No second decomposition-run identity is introduced. Progressive decomposition reuses `object.decomposition_run` and WP08 Domain Run/Coverage records.
- No second byte/content identity is introduced for disks, firmware or backups. WP03 Content/Object Revision remains canonical exact-byte identity.
- No backend session, USB path, ADB serial, VID/PID, process ID, flasher job ID or parser result ID becomes canonical Ptah identity.
- `firmware.compatibility_claim`, `firmware.compatibility_result`, `firmware.operation_plan`, `firmware.mutation_authorization`, `device.protocol_operation`, `firmware.operation`, `firmware.operation_verification` and `device.operation_recovery` remain separately addressable.

## Catalog effect

Active catalog `urn:ptah:schema-catalog:domain:0.1.2` contains:

- 47 unique schema URNs;
- 15 unique namespaced lifecycle machines;
- all selected `0.1.1` corrections unchanged;
- `firmware.compatibility_claim` `0.1.0`;
- `device.protocol_operation` `0.1.0`;
- `device.operation_recovery` `0.1.1`;
- Device Protocol Operation and Device Operation Recovery lifecycle machines.

## Conformance blockers

Reject:

- a Compatibility Claim used directly as physical mutation authority;
- a Device Protocol Operation lacking exact WP02 Operation/Attempt references;
- firmware and Device protocol records collapsed into one generic operation identity;
- protocol acknowledgement promoted to verified success;
- recovery using stale Session, Connection epoch, Provider generation, Lease or fence;
- retry after recovery reusing an Attempt identity;
- migration of a legacy recovery record to `0.1.1` without lifecycle and generation evidence.
