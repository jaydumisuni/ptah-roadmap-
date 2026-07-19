# WP08 Catalog Migration — 0.1.1 to 0.1.2

**Status:** CANDIDATE  
**Date:** 2026-07-19  
**Source catalog:** `urn:ptah:schema-catalog:domain:0.1.1`  
**Target catalog:** `urn:ptah:schema-catalog:domain:0.1.2`

## Purpose

Catalog `0.1.2` is a non-breaking identity/lifecycle completion over accepted WP08 `0.1.1`. All selected `0.1.1` schemas and lifecycle machines remain active unchanged except candidate Device Operation Recovery `0.1.0`, which is superseded by `0.1.1`.

## Added active records

### Firmware Compatibility Claim

Legacy vendor matrices, manifest declarations, tool-support tables, package metadata, model/chipset lists and operator assertions may migrate to `firmware.compatibility_claim` only when:

- the exact source Object/record and claimant are retained;
- claim scope and target claims are explicit;
- claimed operation classes are bounded;
- evidence, confidence, issue time and limitations are preserved.

They do not migrate to `firmware.compatibility_result`, Mutation Authorization or execution authority. Exact live-context review remains required.

### Device Protocol Operation

Legacy ADB, Fastboot, MTP, USB serial, vendor-download, META, DIAG, Appium, accessibility, display/input, shell, package-management or file-transfer records may migrate to `device.protocol_operation` only when exact correlation exists for:

- stable Device and Profile Revision;
- Device Session and Interface;
- Connection record and epoch;
- Provider revision/instance/generation;
- WP02 Activity, Operation and Attempt identities;
- protocol class and bounded operation/mutation class;
- timestamps, outcome, Receipts and evidence.

Backend job/session IDs remain scoped Aliases. If exact correlation is unavailable, preserve the legacy record as an Observation, Receipt, Artifact or restricted source record; do not manufacture canonical execution identity.

When a legacy record represents a specialist firmware mutation, it may additionally map to `firmware.operation`. The Device protocol projection and firmware aggregate remain separate and cross-linked.

## Device Operation Recovery correction

Candidate `device.operation_recovery` `0.1.0` may migrate to `0.1.1` only when the migration can supply:

- a valid `device.operation_recovery.lifecycle` projection;
- exact previous Session and Connection references;
- previous Connection epoch and Provider generation;
- recovery Activity, Operations and new Attempts;
- reconciliation questions/results and evidence;
- new Session/Connection epoch/Provider generation when reacquisition occurred;
- bounded recovery decision and Receipts.

If those facts cannot be reconstructed:

- retain the `0.1.0` record as superseded candidate/legacy evidence;
- classify the migration as `manual_review`, `inconclusive` or `preserve_without_interpretation`;
- do not infer recovered, safe-to-resume or safe-to-retry state.

## Lifecycle migration

- `device.protocol_operation` begins in `prepared` only after exact current context and a new WP02 Attempt exist.
- Legacy “success” based only on backend return or acknowledgement migrates no higher than `acknowledged`/`completed_acknowledged` with explicit authority and limitations.
- Legacy interrupted non-idempotent work migrates to `uncertain`, followed by a separate Recovery record.
- Recovery cannot transition to safe retry unless reconciliation proves duplicate/partial effects are resolved and a new Attempt will be used.

## Non-regression requirements

Migration must preserve every `0.1.1` correction, including:

- exact Provider revision/instance/generation and truthful locality;
- Dispatch Eligibility and capability evidence;
- immutable Firmware Operation Plan;
- transport authorization and cleanup stages;
- writable-copy/overlay filesystem rules;
- Device Profile, Session, capability, Stream, Screen Context and Backup exact connection bindings;
- Device Session quarantine on cleanup failure;
- explicit Recovery before uncertain firmware resume.

## History and proof

- No source record is modified in place.
- Old schema IDs, backend IDs, aliases, negative outcomes and limitations remain retained.
- Migration produces a new Migration Run and immutable mapping evidence.
- Contradictory Claims and Results remain plural.
- No migration converts acknowledgement, unknown or inconclusive state into verified success.
