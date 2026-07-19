# Phase 0B WP08 — Domain Pack, Firmware, Disk, Filesystem and Device Contracts

**Status:** CANDIDATE COMPLETE — DOWNSTREAM CONTRACT USE APPROVED; IMPLEMENTATION FREEZE DEFERRED  
**Date:** 2026-07-19  
**Runtime implementation:** NOT STARTED  
**Dependency/backend selection:** NOT STARTED

## Purpose

Turn the frozen Domain Pack, firmware/disk/filesystem and Device architecture into exact candidate identities, schemas, lifecycles, migration rules and conformance expectations without selecting parser, filesystem appliance, USB/runtime, ADB/Fastboot, vendor-protocol, loader/programmer, flasher, display or input backends.

## Normative records

- `contracts/phase-0b/domain/DOMAIN-FIRMWARE-DISK-DEVICE-CONVENTIONS.md`
- `contracts/phase-0b/common/ENTITY-KIND-REGISTRY-WP08-SUPPLEMENT.md`
- `contracts/phase-0b/common/ENTITY-KIND-REGISTRY-WP08-CORRECTION-0.1.1.md`
- `schemas/phase-0b/domain/schema-catalog.v0.1.0.json`
- `migrations/phase-0b/WP08-DOMAIN-FIRMWARE-DISK-DEVICE-MIGRATION-COMPATIBILITY.md`
- `conformance/PHASE-0B-WP08-DOMAIN-FIRMWARE-DISK-DEVICE-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp08/domain-firmware-disk-device-cases.v0.1.0.json`

## Candidate schema set

The Domain catalog contains 44 active schemas:

### Generic Domain Pack

1. shared definitions;
2. Domain Pack;
3. immutable Pack Revision;
4. exact-context Pack Compatibility;
5. Detector Observation;
6. Classification Decision;
7. Domain Operation Request;
8. Coverage;
9. Domain Operation Run;
10. Inventory;
11. Validation Run;
12. Compare Run;
13. Rebuild Run.

### Firmware and physical operations

14. Firmware Package;
15. Firmware Manifest;
16. Firmware Component;
17. executable loader/programmer/FDL asset;
18. Firmware/Device Compatibility Result;
19. Mutation Authorization;
20. Protocol Stage Observation;
21. Firmware Operation Plan;
22. physical Firmware Operation;
23. Operation Verification.

### Disk and filesystem

24. Disk Image Revision;
25. Extent Map;
26. Partition Table;
27. Partition;
28. Filesystem Observation;
29. Filesystem identity;
30. Mount/Inspection Session;
31. Filesystem Inspection Result.

### Device

32. Device;
33. Device Profile Revision;
34. Interface incarnation;
35. Connection epoch;
36. Connection Observation;
37. Device Session;
38. Session Capability Snapshot;
39. Device Stream;
40. Stream Observation;
41. Screen Context;
42. verified Device Backup;
43. Mutation Exception;
44. Operation Recovery.

Dependencies:

- common `0.1.0`;
- activity `0.1.1`;
- object `0.1.0`;
- runtime `0.1.2`;
- workspace `0.1.0`;
- transfer `0.1.0`;
- build/provenance `0.1.1`.

## Lifecycle machines

Thirteen namespaced lifecycles are included:

- Domain Pack;
- Domain Operation Request;
- shared Domain Run;
- Filesystem;
- Filesystem Mount Session;
- Device;
- Device Interface;
- Device Connection;
- Device Session;
- Device Stream;
- Device Backup;
- Firmware Mutation Authorization;
- Firmware Operation.

Detector/classification, compatibility, coverage, protocol stages and verification remain immutable evidence/decision records rather than lifecycle shortcuts.

## Accepted boundaries

### Domain Pack

1. Pack, immutable Revision, Compatibility, Request, Run and Coverage remain separate.
2. operation capabilities are explicit; static analysis cannot grant physical mutation.
3. detector observations remain plural; classification retains conflict/ambiguity/polyglot/unknown states.
4. recursive work is budgeted; partial valid outputs survive and incomplete coverage remains visible.
5. Inventories, Validation, Compare and Rebuild remain separate result classes.
6. Pack replacement preserves source Object identity and creates new evidence/results.

### Firmware

1. Package, Manifest, Component and executable assets remain separate roles over exact Objects.
2. filename/model/build/chip claims are never compatibility authority.
3. Manifest retains components, operations, ranges/digests, ordering and source requirements.
4. loaders/programmers/DA/FDLs are first-class Objects with source/licence/trust/target evidence.
5. Compatibility is operation-specific and binds exact Device Profile, layout, connection epoch, tools/assets and Provider generation.
6. analyzable/readable never implies writable.
7. `.P5C` remains unsupported/opaque until lawful authoritative evidence exists.

### Disk/filesystem

1. encoded bytes, expanded logical content, sparse/backing extents and backing Objects remain separate.
2. untrusted backing paths require approved Object allowlists.
3. Partition tables/partitions retain exact geometry, copies/checks, bounds, overlaps and provenance.
4. Filesystem Observations remain plural before identity selection.
5. untrusted filesystem access occurs through isolated Providers.
6. read-only mode cannot silently become writable; overlay changes remain separate Artifacts.
7. host mount/open paths remain aliases.

### Device identity/session

1. stable Device identity remains independent of serial, VID/PID, USB path, IP, mode, Interface, Connection, Provider and Session.
2. cross-mode correlation requires multiple evidence sources or explicit operator review.
3. every transport/mode incarnation is an Interface; every continuity period is a Connection epoch.
4. reconnect/re-enumeration/provider restart/fence advances epoch and invalidates stale evidence.
5. Device Session binds Workspace, Device/Profile, typed Device Lease/fence, Provider generation, current Connections and expiring capability snapshot.
6. Session/Stream partial availability does not alter Device identity or imply mutation authority.
7. Screen Context is a captured observation; WP09 owns semantic targets/actions and Shell behavior.

### Backup and physical mutation

1. destructive/uncertain mutation requires verified operation-specific backup unless an exact reviewed exception exists.
2. backup file existence or tool log is not backup proof.
3. Compatibility, Mutation Authorization, Operation Plan, WP02 Operation/Attempts, protocol stages, ACK and Operation Verification remain separate.
4. Plan grants no authority and performs no mutation.
5. stale Lease/fence/epoch/generation/authorization blocks before execution.
6. protocol ACK/process exit supports acknowledged evidence only.
7. verified completion requires correlated read-back or authoritative external evidence.
8. read-back unavailable remains acknowledged-with-limitations/uncertain/manual verification.
9. disconnect during non-idempotent mutation becomes uncertain; blind retry is forbidden.
10. recovery creates new context/Attempts and never rewrites history.

### Privacy/security

1. protected identifiers, keys, NV/RPMB/eFuse, backups, partition data, screenshots/logs and operator actions are restricted by default.
2. raw credentials never enter canonical/public records.
3. untrusted parsers/images/packages run under bounded isolation.
4. extracted bytes are non-executable by default.
5. Device-side executable assets require exact provenance/licence/trust/compatibility.

## Migration closure

The migration record forbids:

- extension/parser exit becoming authoritative classification;
- detector disagreement deletion;
- complete decomposition without budget/coverage evidence;
- derived parser bytes replacing originals;
- `.P5C` structure or loader compatibility guessed by analogy;
- arbitrary backing-path resolution;
- direct writable untrusted filesystem mount without authority;
- Device merge from one serial/VID/PID/IP;
- stale epoch/generation/Lease/Receipt reuse;
- interface presence treated as protocol readiness;
- ACK/process exit treated as verified physical success;
- backup file presence treated as verified backup;
- uncertain mutation automatically retried;
- sensitive Device evidence made public by default;
- Pack/Provider replacement rewriting historical results.

## Conformance closure

The fixtures and safety net cover:

- detector disagreement and ambiguous/polyglot classification;
- budget inheritance, partial outputs and unknown gaps;
- parser/Pack replacement;
- firmware manifest/delta source requirements;
- parked `.P5C` behavior;
- executable asset compatibility;
- disk sparse/backing/partition geometry;
- isolated read-only and overlay filesystem access;
- Device identity across ADB/Fastboot/mode transitions;
- new connection epoch and stale fence rejection;
- protocol presence versus service readiness;
- partial Sessions/Streams/Screen Context;
- verified backup versus file presence;
- backup exceptions;
- ACK versus read-back verification;
- disconnect/uncertain/no-blind-retry recovery;
- privacy and failure isolation;
- Pack/Provider replacement without identity loss.

Structural JSON Schema validation is insufficient. WP13 must enforce typed-reference kinds, range arithmetic, overlap/bounds, monotonic epochs, exact generation/fence correlation, budget inheritance, source/child/relationship lineage, backup coverage, compatibility freshness, ACK/read-back separation and privacy constraints.

## Candidate-completion verdict

**WP08 is candidate-complete for downstream Phase 0B use.**

It does not prove any parser, filesystem appliance, firmware adapter, USB/runtime service, loader/programmer/FDL, flasher, Device Provider, display/input stream or physical operation works.

## Deferred work

- Application/Browser/semantic UI/Shell — WP09;
- knowledge/data/Package/Plugin — WP10;
- isolation/placement/reservation/Lease/secure grants — WP11;
- security/Finding/Claim/Evidence extensions — WP12;
- executable harness/golden corpus — WP13/WP14;
- parser/device backend selection and physical test hardware — Phase 0C only.

## Acceptance decision

- `decisions/ADR-0025-DOMAIN-PACK-FIRMWARE-DISK-DEVICE-OPERATION-BOUNDARY.md`

## Do-not-build rule

> Candidate-complete WP08 contracts authorize downstream schema design only. They do not authorize selecting, installing or deploying parsers, filesystem appliances, firmware/device services, drivers, loaders/programmers, flashers, display/input backends or Device UI.
