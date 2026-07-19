# ADR-0025 — Domain Pack, Firmware, Disk, Filesystem and Device Operation Boundary

**Status:** ACCEPTED FOR PHASE 0B DOWNSTREAM CONTRACT DESIGN  
**Date:** 2026-07-19  
**Phase:** 0B-WP08  
**Implementation authorization:** NONE

## Context

Ptah must support many specialist formats, firmware families, disk/filesystem structures and physical/virtual Devices without allowing one parser, file extension, USB mode, backend session, loader, tool exit, protocol acknowledgement or screenshot to become universal truth or physical-operation authority.

The frozen architecture established Domain Packs, immutable Objects, plural detector claims, bounded decomposition, firmware/disk/device separation, stable Device identity, leased Sessions and read-back proof. WP08 converts that architecture into candidate contracts.

## Decision

Ptah owns separate canonical records for:

1. Domain Pack and immutable Pack Revision;
2. Pack Compatibility;
3. Detector Observation and Classification Decision;
4. Domain Operation Request, Run and Coverage;
5. Inventory, Validation, Compare and Rebuild Runs;
6. Firmware Package, Manifest and Component;
7. executable loader/programmer/DA/FDL/payload asset;
8. Firmware/Device Compatibility Result;
9. Mutation Authorization;
10. Firmware Operation Plan;
11. Protocol Stage Observation;
12. physical Firmware Operation and Operation Verification;
13. Disk Image Revision and Extent Map;
14. Partition Table and Partition;
15. Filesystem Observation, Filesystem identity, Mount Session and Inspection Result;
16. Device, Profile Revision, Interface, Connection and Connection Observation;
17. Device Session and Session Capability Snapshot;
18. Device Stream, Stream Observation and Screen Context;
19. verified Device Backup and Mutation Exception;
20. Device Operation Recovery;
21. WP02 Activity/Operation/Attempt/Receipt and existing Object/Provider/Workspace/Transfer/Build/proof records.

Backend/device IDs, paths, serials, VID/PID, COM ports, IPs, process/service IDs, tool stage names and filenames remain aliases or observations.

## Domain Pack boundary

A Pack is a stable specialist capability family, not one binary/library/container, MIME type, parser version or run.

Pack Revision is immutable and declares detector claims, operation capabilities, dependencies, resources, network/credential/isolation requirements, outputs, proof capabilities, licence/provenance and limitations.

Compatibility is directional and operation-specific. A Pack may be compatible for inventory while incompatible for rebuild, execution or physical mutation.

Detector observations remain plural. Classification is separate and retains ambiguity, conflicts, polyglots, unknown/opaque/encrypted/malformed/truncated/unsupported states.

Recursive operations are budgeted. Valid partial output survives; Coverage records missing scope and budget exhaustion. Descendants inherit remaining budget.

## Derived output boundary

Inventory, Decomposition, Validation, Compare and Rebuild remain separate from source Object truth.

Children, Views and Relationships retain exact source locators and parser/Pack provenance. Parser replacement creates new results without replacing originals or deleting disagreement.

Rebuild uses immutable Recipe/materials and produces new Objects. Hash, reopen/parse, semantic comparison, execution, independent review and authoritative result remain different proof domains.

## Firmware boundary

Firmware Package is a role over exact immutable bytes. Manifest and Components remain derived, versioned and parser-bound.

Filename, model, build and chipset strings are claims only.

Loader/programmer/DA/FDL/preloader/ramdisk/payload assets are first-class Objects with exact digest, source/licence/provenance, role, target/mode/configuration claims, capability and verification.

Asset selection and write compatibility require exact evidence; family resemblance is insufficient.

`.P5C` remains unsupported/opaque until a lawful sample, specification or parser exists.

## Disk/filesystem boundary

Encoded image bytes, expanded logical content, sparse/backing extents and backing Objects remain separate.

Untrusted backing references require explicit Object allowlists.

Partition tables/partitions retain exact geometry, copies/checks, bounds, overlaps and provenance. Names/GUIDs/labels are metadata, not byte identity.

Filesystem observations remain plural before canonical selection. Untrusted filesystem access uses isolated Providers/appliances. Read-only cannot silently become writable; writable overlay changes remain separate Artifacts.

Host mount/open paths remain aliases.

## Device identity and continuity boundary

Device identity is stable across transport, USB topology, serial, VID/PID, IP, mode, Interface, Connection, Provider and Session changes.

Cross-mode correlation requires multiple evidence sources or explicit operator review.

Every transport/mode incarnation is a Device Interface. Every continuity period is a Device Connection with a monotonic epoch. Reconnect, re-enumeration, unproven mode transition, re-pair, Provider restart/fencing or continuity loss advances epoch.

Old epoch/generation/Lease/fence evidence cannot authorize or complete current operations.

Presence/reachability is not protocol readiness. Protocol handshake is not loaded service. Loaded service is not successful write or read-back.

## Session, Stream and Screen Context boundary

Device Session binds exact Workspace, Device/Profile, typed Device Lease/fencing token, Provider generation, current connections and expiring capability snapshot.

Session availability may be partial/recovering without altering Device identity.

Video, audio, control, clipboard, log, shell, file and semantic streams remain separate records with current epoch/generation and privacy.

Screen Context is one captured observation with screenshot/coverage/redaction/limitations. It does not grant input authority or prove action outcome. WP09 owns semantic target/action and Shell contracts.

## Backup and mutation boundary

Destructive or uncertain mutation requires verified operation-specific immutable backup unless an exact reviewed exception records impossibility, consequences, compensating controls and expiry.

Backup file presence or tool log is not proof. Verification requires expected/actual ranges and sizes, Content/Object/digests, Locations and restoration recipe/limits.

Compatibility, Mutation Authorization, Operation Plan, WP02 Operation/Attempts, protocol stages, acknowledgement and Operation Verification remain separate.

Plan grants no authority and performs no mutation.

Mutation requires current Session, Lease/fence, connection epoch, Provider generation, compatibility, authorization, exact target/source ranges, assets, backup/read-back policy and new Attempt.

## Physical proof and recovery boundary

Protocol ACK/process exit is intermediate evidence only.

`completed_verified` requires correlated read-back or authoritative external evidence under the exact current context.

When read-back is unavailable, outcome remains acknowledged-with-limitations, uncertain or manual/external verification; it is never silently verified.

Write/erase/repartition/security/NV/payload operations default to no automatic retry or retry only after authoritative read-back/manual resume.

Disconnect/provider restart/Lease expiry during a non-idempotent operation produces uncertain state and fences stale work. Recovery creates new context/Attempts, explicitly reconciles whether the effect occurred and never rewrites history.

## Privacy/security boundary

Sensitive identifiers, keys, serials, IMEI, hardware hashes, NV/calibration/RPMB/eFuse data, partition contents, backups, screenshots/logs and operator actions are restricted by default.

Raw credentials never enter ordinary/public records.

Untrusted parsers/images/packages execute under bounded isolation. Extracted content is non-executable by default. Device-side executable assets require exact provenance/licence/trust/compatibility.

## Entity-kind correction

Accepted correction `0.1.1` adds `firmware.operation_plan` and preserves its separation from compatibility, authority, execution and verification.

## Schema and conformance decision

Accepted candidate package:

- 44 active schemas in `schemas/phase-0b/domain/schema-catalog.v0.1.0.json`;
- 13 namespaced lifecycle machines;
- normative conventions and entity-kind supplement/correction;
- migration/compatibility rules;
- positive/negative fixture corpus;
- consolidated safety net.

Structural JSON Schema validation is insufficient. WP13 must enforce typed references, range/bounds/overlap arithmetic, monotonic epochs, exact generation/fence correlation, budget inheritance, lineage, compatibility freshness, backup coverage, ACK/read-back separation, retry policy and privacy.

## Consequences

### Positive

- specialist tools remain replaceable;
- parser disagreement and partial evidence survive;
- firmware/disk/device identities remain stable and exact;
- static capability cannot mutate physical state;
- Device continuity and stale-control risks are explicit;
- backups and physical proof are operation-specific;
- unsafe automatic retry is blocked;
- Device UI/semantic work can build on honest Session/Stream/Screen Context foundations.

### Costs

- many records and exact range/generation correlations;
- verified backup/read-back can be slow or unavailable;
- Device identity correlation may require operator review;
- legacy logs frequently remain partial evidence;
- physical fixtures/hardware are required later for executable proof.

## Rejected alternatives

- one universal parser/firmware/device tool identity;
- extension/parser exit as authoritative type;
- successful parse as write compatibility;
- chipset-family/filename loader selection;
- `.P5C` inferred from `.PAC`;
- host direct writable mount of untrusted images;
- serial/VID/PID/IP as Device identity;
- USB/device listing as protocol readiness;
- Stream/screenshot as Session/mutation authority;
- backup file existence as verified backup;
- Operation Plan as Mutation Authorization;
- protocol ACK/process exit as verified physical state;
- blind retry after uncertain mutation;
- Provider replacement rewriting old outcomes.

## Downstream requirements

WP09 and later packages must preserve:

- Pack/Revision/Compatibility/Request/Run/Coverage separation;
- source Object/derived result lineage;
- Device/Profile/Interface/Connection/Session/Stream/Screen Context separation;
- current Lease/fence/epoch/generation correlation;
- static versus physical mutation authority;
- backup/exception/authorization/plan/operation/ACK/verification/recovery separation;
- privacy restrictions and negative evidence;
- WP02 retry/Receipt rules;
- WP03 Object/Relationship/Artifact/Location identity;
- WP04 Provider/generation/capability freshness;
- WP05 Workspace/Session/checkpoint boundaries;
- WP06 backup/restore/transfer boundaries;
- WP07 Recipe/Build/provenance/trust rules.

No parser, filesystem, firmware, USB/runtime, Device Provider, loader/programmer, flasher, display/input backend or Device UI implementation is authorized by this ADR.

## Related records

- `work-packages/PHASE-0B-WP08-DOMAIN-FIRMWARE-DISK-DEVICE.md`
- `contracts/phase-0b/domain/DOMAIN-FIRMWARE-DISK-DEVICE-CONVENTIONS.md`
- `contracts/phase-0b/common/ENTITY-KIND-REGISTRY-WP08-SUPPLEMENT.md`
- `contracts/phase-0b/common/ENTITY-KIND-REGISTRY-WP08-CORRECTION-0.1.1.md`
- `schemas/phase-0b/domain/schema-catalog.v0.1.0.json`
- `migrations/phase-0b/WP08-DOMAIN-FIRMWARE-DISK-DEVICE-MIGRATION-COMPATIBILITY.md`
- `conformance/PHASE-0B-WP08-DOMAIN-FIRMWARE-DISK-DEVICE-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp08/domain-firmware-disk-device-cases.v0.1.0.json`
