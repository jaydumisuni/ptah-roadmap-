# Phase 0B WP08 — Domain, Firmware, Disk and Device Migration Compatibility 0.1.1 Corrections

**Status:** CANDIDATE CORRECTION  
**Date:** 2026-07-19  
**Parent:** `WP08-DOMAIN-FIRMWARE-DISK-DEVICE-MIGRATION-COMPATIBILITY.md`  
**Authoritative catalog:** `urn:ptah:schema-catalog:domain:0.1.1`

## Purpose

Preserve the base migration record while making its active schema/lifecycle references and final review invariants match catalog `0.1.1`.

## Active catalog and corrected records

Migration targets catalog:

- `schemas/phase-0b/domain/schema-catalog.v0.1.1.json`.

The following `0.1.0` records are superseded candidate history and must migrate to their `0.1.1` replacements where active interpretation/execution authority is required:

- Domain Pack Compatibility;
- Domain Operation Run;
- Firmware Compatibility Result;
- Firmware Protocol Stage Observation;
- Firmware Operation;
- Firmware Operation Verification;
- Filesystem Mount Session;
- Device Profile Revision;
- Device Session;
- Device Session Capability Snapshot;
- Device Stream;
- Device Stream Observation;
- Device Screen Context;
- Device Backup;
- Device Session lifecycle;
- Firmware Operation lifecycle.

Migration also recognizes the added active records:

- stable `disk.image` root;
- `firmware.operation_plan`.

## Exact execution-context migration

Legacy Domain Runs, Device Sessions, Streams, Profiles, Backups and physical Operations are current-authority records only when they can bind exact:

```text
Provider Revision
Provider Instance
Provider generation
connection epoch
Interface/Connection where Device-bound
Workspace Materialization generation where Workspace-bound
Node generation and current snapshots for Node-local execution
or approved remote-service identity for remote execution
Dispatch Eligibility/capability evidence where applicable
```

Missing context produces historical/partial evidence, not current execution authority.

Remote records do not invent Ptah Nodes. Local and remote locality fields are mutually exclusive.

## Operation Plan migration

Legacy parsed scatter/rawprogram/patch/PIT/payload instructions may become plan inputs, but physical work receives a `firmware.operation_plan` only when exact package/component/source bytes, Device/Profile/layout, target ranges, tools/assets, authority, Lease/fence, backup/exception, retry policy and read-back Protocol are recovered.

A legacy tool invocation cannot serve simultaneously as Plan, Authorization, Operation and Verification.

Changing source, target, layout, Profile, epoch, Provider generation, selected tool/asset, authority or verification method invalidates the imported Plan.

## Backup compatibility migration

Legacy `can read` or `read supported` flags do not become `compatible_for_backup`.

Backup compatibility requires recovered evidence for:

- exact ranges and expected size;
- digest/verification method;
- durable Location capability;
- privacy/retention policy;
- restoration Recipe and compatibility limits.

Write compatibility remains separate and still requires backup/read-back capability or an exact reviewed exception.

## Writable mount migration

Legacy writable direct mounts against the original source cannot become approved WP08 writable Sessions.

Migration options are:

- retain as historical unsafe/unknown-effect evidence;
- create a new `writable_copy` Session over a copied Object Revision;
- create a new `writable_overlay` Session over an explicit overlay/change Artifact.

The original source Object Revision remains immutable.

## Device Session and cleanup migration

A legacy Device Session with several transports/providers must decompose into per-binding records containing exact Interface, Connection epoch and Provider revision/generation.

Session close becomes `closed` only when required cleanup/revocation is verified. If cleanup cannot be proven:

- migrate to `cleanup_failed` or manual review;
- record/require Device quarantine;
- block ordinary reassignment;
- preserve the failure after later remediation.

Provider disconnect, process exit or lease expiry is not cleanup proof.

## Uncertain-operation migration

A legacy uncertain non-idempotent Operation cannot transition directly back to preparation/execution.

Migration requires:

- Device Operation Recovery record;
- authoritative rediscovery/read-back/current Profile and layout;
- current Plan, Compatibility, Session, Lease/fence and Provider/Connection context;
- explicit resume/recovery authority;
- new WP02 Attempt/nonce.

Otherwise retain `uncertain` and block replay.

## Stream, Screen Context and Profile freshness

Legacy Profile, Stream, Stream Observation and Screen Context records without exact Interface, Connection epoch, Provider revision/generation and freshness deadline remain historical observations only.

They cannot authorize input, mutation, compatibility or current Session capability.

## Parked formats and driver/admin changes

`.P5C` remains extension-only/opaque/unsupported and cannot be migrated as PAC semantics without an accepted reopening decision and authoritative evidence.

Driver/package/host-admin changes become separate authorized Activities with before/after inventory and rollback evidence. Driver installation success cannot become Interface or protocol readiness.

## Additional negative migration cases

Reject or require manual review when migration attempts to:

- select catalog `0.1.0` context-light schemas as active authority;
- invent Node fields for remote Domain/Device Providers;
- merge several Device connections under one Provider generation;
- treat a legacy invocation as Plan plus Authorization plus Verification;
- map read support directly to backup compatibility;
- import direct writable source mutation as an approved Mount Session;
- mark Session closed when cleanup is unverified;
- resume uncertain firmware work without Recovery and a new Attempt;
- use stale Screen Context/Profile/Stream evidence after epoch/generation change;
- infer `.P5C` semantics from extension or PAC resemblance;
- infer Device readiness from successful driver installation.

## Do-not-break rule

> Migration may preserve incomplete legacy evidence, but it may never manufacture exact context, planning, backup safety, cleanup, continuity, compatibility or read-back proof that the source records did not establish.
