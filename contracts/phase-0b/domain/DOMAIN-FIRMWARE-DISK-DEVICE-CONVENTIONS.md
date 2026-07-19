# Phase 0B WP08 — Domain Pack, Firmware, Disk, Filesystem and Device Conventions

**Status:** CANDIDATE DRAFT  
**Date:** 2026-07-19  
**Contract family target:** `ptah.domain` / `ptah.firmware` / `ptah.disk` / `ptah.device` `0.1.0`  
**Implementation authorization:** NONE

## Purpose

Define backend-neutral specialist Domain Pack, firmware package/image, disk/partition/filesystem and physical/virtual Device contracts without selecting parser, filesystem, driver, flasher, loader/programmer, ADB/Fastboot, vendor protocol, display or input backends.

This package composes:

- WP01 identity, typed families, privacy and migration;
- WP02 Activity/Operation/Attempt/Event/Receipt/proof;
- WP03 Content/Object/Revision/Relationship/View/Artifact/Location;
- WP04 Node/Facility/Provider/capability/generation/freshness;
- WP05 Workspace/Materialization/Session/checkpoint/recovery;
- WP06 Transfer/backup/restore/reconciliation;
- WP07 Recipe/Build/output/provenance/signature/verification;
- ADR-0007 Object/decomposition/Domain Pack boundary;
- ADR-0008 disk/firmware/physical-operation boundary;
- ADR-0009 Device Session/display/input boundary.

---

# 1. Required separation

Ptah keeps the following distinct:

```text
Domain Pack
Domain Pack Revision
Domain Pack Compatibility
Detector Observation
Classification Decision
Domain Operation Request
Domain Operation Run
Inventory
Coverage
Decomposition Run
Validation Run
Compare Run
Rebuild Run
Firmware Package role
Firmware Manifest revision
Firmware Component role
Loader/Programmer/FDL asset
Firmware/Device Compatibility Result
Disk/Image role
Partition Table revision
Partition
Filesystem observation
Filesystem Mount/Inspection Session
Device
Device Profile revision
Device Interface incarnation
Device Connection epoch
Device Session
Device Stream
Screen Context
Physical Protocol Operation
Physical Operation Attempt
Device Backup
Mutation Authorization
Write acknowledgement
Read-back Verification
Recovery/Cleanup
```

No parser exit, filename, USB mode, ADB serial, VID/PID, service PID, backend session, protocol acknowledgement or UI display state may collapse these records.

---

# 2. Domain Pack identity

## 2.1 Domain Pack

`domain.pack` is the durable logical identity for one specialist capability family.

A Pack is not:

- one library/binary/container image;
- one parser version;
- one MIME type or file extension;
- one Device protocol backend;
- one Platform/vendor product;
- one Activity or Run;
- one output View or Object.

## 2.2 Domain Pack Revision

A Pack Revision is immutable and declares:

```text
pack_ref
revision_number/content_digest
supported detector claims/types/subtypes
operation capabilities
input requirements
required/optional Facilities and capabilities
supported platforms/architectures
resource/budget classes
network and credential requirements
output relationship vocabulary
proof/read-back capabilities
isolation requirements
licence/dependency/provenance refs
known limitations
```

Operation vocabulary:

```text
detect
inventory
decompose
preview
open_or_mount
transform
compare
rebuild
validate
execute_or_run
```

Unsupported operations are explicit negative capabilities.

## 2.3 Pack compatibility

Compatibility is directional and binds one exact Pack Revision to:

- exact input Object Revision/type/size/structure;
- requested operation and depth/coverage;
- candidate Facility/Provider revision and generation;
- Node/runtime/platform/architecture;
- isolation and resource budgets;
- credential/network availability;
- caller policy and privacy/licence constraints.

Outcomes:

```text
compatible
compatible_with_conditions
compatible_for_partial_scope
incompatible
unsupported_operation
unsupported_input
missing_dependency
missing_credential
resource_or_policy_blocked
unknown
stale
```

A parser can be compatible for static inventory while incompatible for rebuild or physical execution.

---

# 3. Detection and classification

Detection remains plural evidence.

Each Detector Observation records:

- exact input Object Revision/digest;
- detector/Pack/Provider revision;
- claimed type/subtype and evidence class;
- byte/container/metadata/filename evidence;
- confidence/priority under detector-specific calibration;
- parser validation state;
- warnings and limitations.

A Classification Decision is separate and records selected route(s), authority/policy, rationale, conflicting observations and expiry/supersession.

Valid outcomes include unknown, ambiguous, polyglot, encrypted, malformed, truncated, unsupported and opaque.

No extension, filename, model string, chipset family or USB identifier overrides stronger content/live evidence silently.

---

# 4. Domain operation model

## 4.1 Domain Operation Request

A request binds:

- exact Pack Revision and operation type;
- exact input Object/Device/Session references;
- requested depth/scope;
- budget and isolation policy;
- required outputs/relationships/proof;
- credential/network refs;
- mutation class;
- caller authorization.

## 4.2 Domain Operation Run

A Run binds:

- accepted Request and Pack Compatibility;
- Workspace/Materialization;
- Facility/Provider revision/generation and locality;
- Node generation/epoch where local;
- Activity plus Operations/Attempts;
- budgets consumed;
- output Objects/Views/Relationships/Inventories;
- coverage and unknown gaps;
- Receipts, failures, cleanup and limitations.

Static and physical runs use the same Activity/Operation/Attempt foundations but different authority and proof requirements.

## 4.3 Budgets and partial output

Every recursive/decomposition operation has hard limits for runtime, CPU, memory, temporary/output bytes, child count, depth, expansion ratio, pages/pixels/frames/text/nodes and other registered resources.

When a limit is reached:

- valid partial children/Views remain registered;
- Coverage records missing/unknown scope;
- state is `budget_exhausted` or partial, not success-complete;
- child work inherits remaining budget rather than resetting it;
- content identity/ancestor tracking prevents cycles/repeated expansion.

---

# 5. Inventory, decomposition and derived outputs

Inventory is a structured immutable result over one exact input and Pack/Provider configuration.

A Decomposition Run produces:

- independently addressable child Object Revisions where bytes exist;
- Views where output is interpretation without independent original bytes;
- exact Relationships with paths, offsets, lengths, pages, coordinates, extents or semantic locators;
- retained overlaps and unknown regions;
- coverage, warnings, errors and budgets;
- parser/Pack/Provider provenance.

Competing parser outputs coexist. Comparison/consensus never erases them.

A higher decomposition level is not inferred from a lower-level tool exit.

---

# 6. Validation, compare and rebuild

Validation Run records one frozen protocol over exact Objects/Views/manifests and retains passed, conditional, failed, inconclusive or blocked results plus evidence.

Compare Run binds exact subjects, comparison method, differing ranges/fields/structures and accepted tolerances.

Rebuild Run uses an immutable Recipe/Blueprint, exact source/material Objects, Pack Revision, Build Run/Operations/Attempts and produces new Object Revisions. It never mutates the original silently.

Reopening/parsing, hash comparison, semantic comparison, runtime test, independent review and external authoritative result remain different proof domains.

---

# 7. Firmware package and manifest

A Firmware Package is an Object/Artifact role over immutable acquired bytes.

Potential types include Apple IPSW/OTA, MTK scatter packages, Unisoc PAC, Qualcomm rawprogram packages, Samsung/Odin packages, Android update payload/sparse/super/partition images, vendor containers and unknown firmware containers.

Filename/model/version strings are claims only.

A Firmware Manifest Revision records:

- package subject/digests;
- parser/Pack Revision;
- product/build/board/chip/security claims;
- component and operation graph;
- signatures/checksums/encryption/compression;
- partition targets/extents/order/dependencies;
- source-build/layout requirements;
- rollback/trusted-key requirements;
- coverage and unknown/unsupported sections.

Each component becomes an Object/View role with exact locator, size/digest, role and provenance.

---

# 8. Loader, programmer, FDL and executable assets

Device-side executable assets are first-class Objects with:

```text
asset role
source/vendor/licence/provenance
content digest/signature/trust claim
supported SoC/HWID/board/models
required mode/base address/storage/protocol
capability scope
known limitations
verification evidence
```

Selection requires exact compatibility evidence. Chipset-family similarity or filename is insufficient.

Unknown/mismatched/unlicensed assets are blocked before execution. Executable assets never become hidden Pack resources.

---

# 9. Firmware/Device compatibility

Compatibility Result compares exact:

- package/manifest/component claims and digests;
- Device Profile Revision and current Interface/Connection epoch;
- live storage/layout/partition-table digest;
- selected loader/programmer/FDL/tool/Provider revision;
- security state, trusted keys, rollback/binary revision;
- source requirements for delta payloads;
- requested operation and ranges;
- missing/unknown evidence;
- backup/read-back capability.

Outcomes remain operation-specific:

```text
compatible_for_static_analysis
compatible_for_read
compatible_for_rebuild_copy
compatible_for_write
incompatible
ambiguous
missing_source_image
missing_loader_or_programmer
missing_key_or_credential
layout_mismatch
security_or_rollback_blocked
unsupported_backend_capability
stale
```

Analyzable never implies writable.

---

# 10. Disk, partition and filesystem graph

## 10.1 Disk/Image

`disk.image` is an Object role over exact raw/sparse/virtual bytes. Encoding and expanded logical content remain separate Objects/Views.

Records retain format, virtual backing chain, logical/physical size, sector size/alignment, sparse extents and approved backing Object references.

Untrusted headers cannot select arbitrary host backing files.

## 10.2 Partition Table and Partition

Partition Table Revision retains:

- scheme/version;
- sector size;
- primary/backup copies and CRC/check validity;
- table ranges;
- parser/Pack provenance;
- overlap/alignment/bounds warnings.

Partition retains stable identity under one exact table/image revision plus index, type/GUID/name/attributes, LBA and byte ranges, LUN/group/logical extent relationships.

Names/GUIDs/labels are metadata, not Object identity.

## 10.3 Filesystem

Filesystem observation retains exact container/partition/image revision, type/version, UUID/label/features, journal/dirty state, encryption/unlock state, size/geometry and parser evidence.

## 10.4 Mount/Inspection Session

Untrusted images/filesystems are opened only through an isolated Provider/appliance.

Session records:

- exact subject and expected format;
- read-only/writable mode;
- Provider/Node/generation;
- isolation class;
- backing Object allowlist;
- mount/open aliases;
- visible filesystem root;
- changes/overlay if writable;
- cleanup/unmount evidence.

Read-only capability cannot silently become writable. Host-kernel loop/kpartx mounts for untrusted content are not the default Ptah path.

---

# 11. Device identity and profile

`device.device` is stable physical/virtual target identity independent of USB path, serial, VID/PID, ADB/Fastboot/Appium/scrcpy session or Provider worker.

Observed identity properties remain time/source-bound claims.

Device Profile Revision records:

- manufacturer/brand/model/product/board/platform;
- hardware/SoC/HWID claims and attestation refs;
- security/storage state;
- firmware build/patch claims;
- current layout digest and storage geometry;
- supported modes/protocols/capabilities;
- protected sensitive identifiers under privacy policy;
- observed evidence and limitations.

Profile changes create new revisions.

---

# 12. Device Interface and Connection

Each transport/mode incarnation is a separate Device Interface:

```text
transport type/address/topology
observed aliases/serial/VID/PID/endpoints
mode/protocol/version
Provider/Node/generation
first/last observation
state and capabilities
```

A Device Connection binds one Interface incarnation to one continuity epoch.

Connection epoch advances on re-enumeration, reconnect, re-pair, mode transition without proven continuity, Provider restart/fencing or loss of transport continuity.

Receipts from an old epoch cannot complete newer Operations.

Correlation across ADB/Fastboot/MTP/META/DIAG/Download/OEM modes uses multiple evidence sources and explicit operator confirmation where required. One alias/VID/PID is insufficient.

---

# 13. Device lease and Session

Physical/stateful mutation requires a current `runtime.lease` of type `device`, with Workspace/holder, mode, capability scope, expiry, fencing token and cleanup recipe.

WP08 consumes the typed Lease boundary; WP11 completes generic reservation/lease contracts. Until WP11, no implementation authority is implied.

Device Session binds:

- Workspace and Device;
- current Lease/fencing token;
- Provider/worker generation;
- current Interface/Connection refs;
- capability snapshot;
- privacy profile;
- streams/screen contexts;
- checkpoint/cleanup refs.

Session lifecycle is independent from individual Interface reachability or stream health. Partial availability remains explicit.

---

# 14. Device streams and Screen Context foundation

Streams are independent typed records for video, audio, control, clipboard, log, shell, file transfer and semantic context.

Each Stream binds exact Session, Interface/Connection epoch, Provider generation, codec/format/geometry/orientation/display, privacy and recording Artifact.

Screen Context is a captured observation over one exact Session/connection/display epoch with screenshot Object, visible text/semantic targets where available, backend revision, coverage/redaction and limitations.

WP08 defines identity and capture foundations only. WP09 completes Application, Browser, semantic selector/action and Shell contracts.

Display observation, semantic context, raw/semantic input and outcome verification remain separate.

---

# 15. Static versus physical capability

Static/read-only capability includes detect, inventory, extract, verify, compare, parse disk layout, inspect filesystem read-only, read Device identity/layout/region and create backup.

Mutation capability includes write/erase/repartition, patch/rebuild, load programmer/FDL, execute payload, reset/reboot, restore/flash, security-state change and protected NV/RPMB/eFuse writes.

Rules:

1. static Pack/Facility cannot invoke physical mutation implicitly;
2. generic raw shell/XML/payload/poke/memory-write escape hatches are separate high-risk capabilities disabled by default;
3. mutation requires exact Device Session, Lease/fence, current connection epoch, Compatibility Result, authorization, backup/read-back strategy and operation scope;
4. read-only permissions cannot reach mutating backend functions.

---

# 16. Physical protocol stages and proof

Presence is not readiness.

Protocol-stage observations may include:

```text
interface_detected
interface_claimed
protocol_handshake
boot_or_download_mode_confirmed
first_stage_loaded
second_stage_or_programmer_loaded
service_configured
layout_inventoried
read_completed
backup_verified
write_acknowledged
write_read_back_verified
device_reset_observed
device_boot_observed
authoritative_external_result
```

Stages remain evidence records, not one universal lifecycle/proof ladder. A higher stage is never inferred from a lower one.

Examples:

- USB PID presence is not a usable service session;
- MTK META transport is not successful META service/read;
- Qualcomm 9008 is not configured Firehose;
- BootROM upload is not partition-service readiness;
- Odin/LOKE handshake is not package compatibility.

---

# 17. Physical Device Operation

A Physical Protocol Operation binds:

- exact Device/Profile/Interface/Connection/Session/Lease/fence;
- Facility/Provider/Pack/tool/loader/programmer revisions;
- compatibility and authorization;
- operation type and exact LUN/partition/region/ranges;
- input source Object/digest;
- required backup and read-back protocol;
- WP02 Operation and physical Attempts;
- protocol-stage evidence;
- acknowledgement, verification, cleanup and outcome.

Write, erase, repartition, reset, security, RPMB/eFuse/NV and device-side payload Operations default to non-retryable or retry-after-authoritative-read-back/manual-resume.

Transport loss never triggers blind replay.

---

# 18. Backup-before-write

Before destructive/uncertain mutation, Ptah requires an operation-specific immutable backup unless an authorized exception explicitly records why backup is impossible and accepts the consequence.

Device Backup records:

- exact Device Profile/Session/Connection epoch;
- LUN/partition/region/range;
- expected and actual size;
- pre-operation bytes and qualified digest;
- partition/layout copy and relevant protected data by privacy policy;
- read backend/tool/asset identity;
- verification/Locations;
- restoration Recipe/compatibility limits;
- proof/retention/access restrictions.

File existence is not backup proof. Expected range/size/digest and read-back must pass.

---

# 19. Mutation authorization and read-back

Mutation Authorization is separate from compatibility and operation execution. It records caller/owner, policy/legal basis, exact target/range/action, backup requirement/exception, accepted risks, time/expiry and review/approval.

Protocol ACK/process exit is intermediate evidence only.

Post-operation verification may include:

- exact range read-back/digest comparison;
- partition-table/layout re-read;
- AVB/signature/rollback state;
- rebuilt image reopen/parse;
- expected service/boot mode;
- device-reported build/version;
- authoritative external result.

`write_acknowledged` and `write_read_back_verified` remain distinct.

When read-back is unavailable, outcome remains acknowledged-with-limitations, uncertain or requires manual/external verification; never silently verified.

---

# 20. Failure, cleanup and recovery

Partial outputs, backups, protocol evidence and unknown states remain retained.

On disconnect/provider restart/lease expiry:

- stale fence/epoch work is rejected;
- Session may enter partial/recovering state;
- non-idempotent operation becomes uncertain;
- no blind retry or silent control transfer occurs;
- new Profile/Layout/Compatibility may be required;
- cleanup/reset/release is separately receipted;
- operation recovery never rewrites historical Attempts.

A failed Pack/provider/device operation does not fail unrelated Workspaces/Devices/Providers.

---

# 21. Privacy and security

Sensitive Device identifiers, keys, serials, IMEI, hardware hashes, calibration/NV/RPMB/eFuse data, partition contents, screenshots/logs and operator actions are restricted by default.

Raw credentials never enter Objects, logs, telemetry, Receipts or public fixtures.

Untrusted packages/images/parsers execute in bounded isolation. Extracted content is non-executable by default. Device-side executable assets require exact provenance/licence/trust and compatibility.

---

# 22. Backend and Pack replacement

Replacing parser, Pack implementation, filesystem appliance, firmware adapter or Device Provider:

- preserves source Object and Device identity;
- creates new Pack/Facility/Provider revisions and Runs;
- creates new Inventories/Views/Relationships/Profile revisions/Compatibility results;
- advances Provider/connection generations as applicable;
- retains prior conflicting/negative evidence;
- requires comparison/conformance before equivalence claims;
- never reuses old acknowledgements/Receipts as current proof.

---

# 23. Minimum conformance invariants

1. Pack, Pack Revision, Compatibility, Request and Run remain separate.
2. detection observations remain plural; classification is separate.
3. partial/budget-exhausted operations retain outputs and incomplete Coverage.
4. child Objects/Views/Relationships preserve exact source locators/provenance.
5. static and physical mutation capabilities are separately authorized.
6. firmware compatibility is operation-specific and exact-evidence-bound.
7. disk/partition/filesystem ranges obey geometry, bounds and overlap rules.
8. untrusted filesystem access is isolated and read-only unless explicitly authorized.
9. Device identity survives interface/mode/Provider changes.
10. connection epoch and fencing reject stale operations/evidence.
11. mutation requires exact compatibility, authorization, backup/read-back policy and current Session.
12. protocol ACK never becomes verified physical state without read-back/authoritative evidence.
13. non-idempotent disconnect becomes uncertain and is not blindly retried.
14. sensitive identifiers/data obey privacy/redaction/retention.
15. Pack/Provider replacement preserves canonical history and negative evidence.

## No-build boundary

These are candidate contracts only. No parser, filesystem appliance, firmware downloader, loader/programmer/FDL database, USB driver, ADB/Fastboot/vendor protocol service, flasher, display/input backend or Device UI implementation is authorized by this document.
