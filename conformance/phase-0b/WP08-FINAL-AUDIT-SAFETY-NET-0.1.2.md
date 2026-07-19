# WP08 Final Audit Safety Net — 0.1.2

**Status:** CANDIDATE CORRECTION TEST PLAN  
**Catalog:** `urn:ptah:schema-catalog:domain:0.1.2`

This safety net is additive to the accepted WP08 conformance suite. It covers the identity and lifecycle gaps found after catalog `0.1.1` acceptance.

## Structural gates

- Catalog `0.1.2` parses and resolves without network access.
- Exactly 47 schema entries have unique absolute URNs and repository paths.
- Exactly 15 lifecycle entries have unique names and repository paths.
- `firmware.compatibility_claim`, `device.protocol_operation` and `device.operation_recovery` resolve to their active schemas.
- `device.operation_recovery` resolves to version `0.1.1`; candidate `0.1.0` remains superseded evidence.
- Device Protocol Operation and Recovery schemas contain valid state projections whose names resolve to cataloged machines.
- All `0.1.1` selected schema and lifecycle versions remain unchanged.

## Semantic gates

1. Firmware Compatibility Claim never grants exact Compatibility Result, Mutation Authorization or physical execution authority.
2. Claims and reviewed Results retain distinct identity, source, context, authority and expiry.
3. Device Protocol Operation references canonical WP02 Activity/Operation/Attempt identity.
4. Firmware Operation and Device Protocol Operation can cross-link but cannot collapse.
5. Every protocol retry creates a new Attempt and nonce.
6. Current Interface, Connection epoch, Provider revision/instance/generation and Lease/fence are required where the operation can mutate or control state.
7. Acknowledgement cannot transition to `completed_verified` without separate verification evidence.
8. Interrupted non-idempotent protocol work transitions to `uncertain`, not automatic retry.
9. Device Operation Recovery binds exact prior Session/Connection epoch/Provider generation and new context when reacquired.
10. Recovery cannot declare resume/retry safe without reconciliation evidence.
11. Safe retry always means a new WP02 Attempt under current authority.
12. Recovery cannot rewrite the original uncertain Operation or Receipts.
13. No Device-specific Lease or second decomposition identity is introduced.

## Migration gates

- Legacy support matrices and tool claims become Claims, never Results.
- Legacy protocol logs become Device Protocol Operations only when exact execution/context correlation exists; otherwise they remain observations/Receipts/Artifacts.
- Recovery `0.1.0` migrates to `0.1.1` only with lifecycle and prior/new generation evidence.
- Missing evidence results in manual review, inconclusive or preserved-without-interpretation—not inferred success.

## Fixtures

Execute every case in:

- `conformance/fixtures/phase-0b/wp08/final-audit-correction-cases.v0.1.2.json`;
- the accepted WP08 Domain/Firmware/Disk/Device fixture suite;
- WP02 retry/Attempt fixtures;
- WP04 Provider generation, connection epoch, Dispatch Eligibility and Lease/fencing fixtures;
- WP07 compatibility, proof and partial-state fixtures where referenced.

## Proof output

The WP13 harness must produce an immutable report containing:

- exact catalog and schema digests;
- lifecycle-machine digests;
- dependency-catalog versions;
- positive/negative case outcomes and expected codes;
- migration-case outcomes;
- duplicate/collision scan;
- unresolved-reference scan;
- secret/privacy scan;
- exact harness/tool/environment revisions and Receipts.

A failure in this correction suite blocks WP08 freeze claims but does not delete or rewrite the previously accepted WP08 evidence.
