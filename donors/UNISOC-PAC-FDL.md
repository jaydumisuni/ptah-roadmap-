# Donor Record — Unisoc / Spreadtrum PAC, BootROM and FDL Composition

**Phase:** 0A / WP06  
**Status:** FIRST-PASS COMPLETE — COMPOSITE UNISOC FOUNDATION, NOT ONE UNIVERSAL TOOL  
**Inspected:** 2026-07-17

## Donors inspected

### spreadtrum_flash / spd_dump

- Canonical URL: https://github.com/ilyakurdyukov/spreadtrum_flash
- Pinned commit: `8bd3b3b380a1479e639ae3177778fa6dc0e3d982`
- Activity: Active
- Licence: no root licence file was found. Source contains an “as-is/no warranty” notice but no complete permission grant was recovered; source reuse/distribution remains blocked pending clarification.
- Classification: most complete inspected open device-side FDL read/write/partition workflow.

### unpac

- Canonical URL: https://github.com/iscle/unpac
- Pinned commit: `cf128ba101ea3e0d038b816d0e19ad311c748eba`
- Activity: Small/simple project
- Licence: no licence file was recovered; source reuse remains blocked.
- Classification: minimal static PAC header/file-table extractor.

### sprdproto

- Canonical URL: https://github.com/kagaimiq/sprdproto
- Pinned commit: `fd3cc8895fdb0e9a200833a404fe0eabe11938fa`
- Licence: MIT
- Activity: Proof-of-concept transport project
- Classification: BootROM/FDL1 USB/UART payload-upload protocol donor.

## Files/components inspected

- `spreadtrum_flash/README.md`
- `spreadtrum_flash/spd_dump.c`
- `unpac/README.md`
- `unpac/CMakeLists.txt`
- `unpac/main.c`
- `sprdproto/README.md`
- `sprdproto/LICENSE`

## Verified capabilities and patterns

### Static PAC package extraction

- PAC header fields include version, product name/version/alias, file count, file-table offset, flash/NAND strategy flags, magic and CRC fields.
- Each PAC file-table entry includes file ID, filename, file version, size, flags, check flag, data offset, omit flag and up to five address values.
- `unpac` memory-maps the complete PAC and extracts entries whose file flag is non-zero.
- PAC metadata establishes a useful static package→entry→offset/size/address relationship foundation.

### BootROM and FDL transport

- Spreadtrum/Unisoc download mode commonly uses USB VID/PID `1782:4d00` and HDLC-like framing/transcoding with CRC/checksum variants.
- `sprdproto` uploads a first payload through BootROM and an optional second payload through FDL1.
- BootROM and FDL1 have different payload/block-size and checksum behavior.
- USB and UART paths are separate transport implementations.
- Boot key/power-cycle/device-mode entry is a distinct prerequisite.
- `sprdproto` is explicitly a payload runner/proof of concept rather than a flash manager.

### FDL1/FDL2 and device operations

- Smartphones generally require FDL1 to initialize RAM and FDL2 to initialize/operate flash.
- Exact FDL images and base addresses come from the original firmware/package XML.
- The project warns that FDL2 from another model on the same chipset may still damage hardware because board/pinmap initialization can differ.
- `spreadtrum_flash` supports partition-list export to XML, configurable block size, partition reads, whole-flash reads, writes, erases and repartition.
- Destructive write/erase/repartition commands ask for confirmation.
- Special raw access names include whole user flash and boot areas.
- eMMC/boot partitions and A/B-style names are represented.
- Read commands can target partition, offset and length; write protocol may lack equivalent offset support for some operations.
- The tool supports feature-phone SC6530/SC6531 families and documents limited smartphone testing, especially Tiger T310.
- 4G feature-phone families such as UMS9117/T117 require compatible FDL1/FDL2 and separate boot areas.
- USB endpoints are discovered through libusb; kernel drivers may be detached before interface claim.
- Protocol implementation contains explicit transcoding, CRC16 and Spreadtrum checksum handling.

## What this donor set completes

- A concrete PAC package-header/file-entry model.
- BootROM versus FDL1 versus FDL2 transport/session separation.
- Exact FDL address/SoC/board compatibility requirements.
- Partition XML inventory and partition/full-flash read foundations.
- Cross-platform libusb evidence and a UART completion path.
- Read/write/erase/repartition operation vocabulary.
- A viable route to build a neutral Unisoc Domain Pack without relying on proprietary ResearchDownload as the canonical implementation.

## Important limitations for Ptah

### Static PAC parser risks

- `unpac` trusts file count, offsets, sizes and filenames without sufficient bounds validation.
- It memory-maps the entire PAC and writes filenames directly beneath the output path without traversal/collision sanitization.
- UTF-16-like strings are reduced to low-byte ASCII, losing Unicode information.
- It does not validate PAC magic, CRCs, file check flags, overlaps, encryption/compression or address semantics.
- It opens output files without truncation/exclusive/atomic finalization and ignores partial-write return values.
- It does not emit hashes or structured metadata.
- No licence was found.

### Device/FDL risks

- `spreadtrum_flash` has very limited tested smartphone coverage and expects code changes for other chipsets.
- FDL1/FDL2 are executable device-side binaries with exact chipset/board/base-address dependencies.
- Cross-model FDL2 reuse is explicitly dangerous.
- FDL binaries extracted by proprietary tools or downloaded from releases require immutable provenance, signature/licence and malware review.
- Partition-list XML from a connected device and XML from a PAC package are different authorities and must be compared.
- Read/write/repartition behavior varies by FDL implementation.
- Destructive confirmation in a CLI is not sufficient Ptah authorization or proof.
- `write_part` may leave remainder bytes undefined/unchanged when the partition is larger than the file.
- A/B aliases and special partition names need normalized relationships, not string assumptions.
- The tool can detach host kernel drivers and usually requires elevated USB permissions.
- USB presence or payload upload does not prove FDL initialization or partition service readiness.
- Source licence for `spreadtrum_flash` is unclear.

### Transport gaps

- `sprdproto` is proven mainly on SC7731G and is explicitly not a flash tool.
- It waits indefinitely for device connection unless wrapped by Ptah timeouts/cancellation.
- Payload execution is not safe read-only analysis.
- UART/USB activity needs Node epoch and exact device selection.
- It does not provide PAC parsing, partition inventory, backup or write verification.

### Internal recovery gap

- No separate auditable internal Unisoc engine repository/handoff was found.
- The private `thetechguy-device-manager` import may contain SPD/Unisoc work, but its exact files were not discoverable through the current connector/index. No implementation claim is made until exact paths/source are inspected.

## Must not be inherited

- PAC file-table data trusted without bounds/CRC/magic validation.
- PAC filenames written directly to host paths.
- FDL matched by chipset name alone.
- cross-model FDL2 reuse as a normal fallback.
- payload upload described as successful flash-service initialization.
- partition write/erase/repartition exposed through read-only analysis.
- CLI confirmation used as the only authorization/evidence.
- write success accepted without exact read-back verification.
- undefined remainder behavior hidden from the caller.
- device IDs/partitions/NV data emitted publicly.
- source with missing/unclear licence copied into Ptah.
- proprietary ResearchDownload used as canonical truth without independent package/device comparison.

## Integration decision

**BUILD A NATIVE PTAH UNISOC PAC/PROFILE CONTRACT; ADAPT PROTOCOL IDEAS; WRAP DEVICE BACKENDS ONLY AFTER LICENCE AND LIVE VALIDATION.**

Recommended composition:

- native/safe PAC parser inspired by the documented structures but independently implemented with strict bounds and Object registration;
- `sprdproto` MIT protocol code/patterns as a transport/reference option;
- `spreadtrum_flash` as a study/optional backend pending licence clarification and broader device tests;
- proprietary tools only as external comparison/asset-extraction sources, never canonical public dependencies.

## Native Ptah gap

Ptah must define:

- PAC package/header/file-entry schema with UTF-16 names, offsets, sizes, flags, addresses, CRC/check state and overlap detection;
- package XML/manifest and device partition-list relationships;
- FDL1/FDL2/payload Object identity, base address, chipset/board/model/source/signature/licence compatibility;
- transport→BootROM→FDL1→FDL2→partition-service proof levels;
- USB VID/PID/interface/endpoint/boot-key and connection-epoch evidence;
- flash/boot-area/partition/A-B/special-region relationships;
- read/full-backup/write/erase/repartition operation classes and retry policy;
- immutable backup and post-write read-back verification;
- exact block/checksum/transcoding capabilities;
- safe native PAC extraction with budgets/path containment/hashes;
- sensitive-data classification;
- driver/udev/admin-change records;
- backend licence and stable-source decision;
- internal SPD engine recovery when exact source paths become available.

## Exit strategy

Ptah's Unisoc contracts remain backend-neutral. A native protocol engine, `sprdproto`, `spreadtrum_flash`, vendor DLoader or future audited internal engine can replace one another without changing PAC, FDL, Device, Partition, Operation or Receipt identities.

## Validation required

1. Parse representative PAC files with strict bounds, magic/CRC/check validation and content-addressed child entries.
2. Reject traversal, overlapping, out-of-range, malformed and Unicode-hostile PAC metadata.
3. Extract FDL1/FDL2/XML with exact package/source hashes and base addresses.
4. Match FDLs to exact chipset/board/model evidence and reject cross-model risk by default.
5. Prove BootROM, FDL1 upload, FDL2 initialization and partition-service readiness as separate levels.
6. Export live partition XML and compare it with PAC/package layout before writes.
7. Read selected partitions/full flash into immutable backup Objects.
8. Disconnect/re-enumerate mid-operation and reject stale receipts.
9. Execute one explicitly authorized write only after backup and verify exact post-write bytes; expose undefined remainder policy.
10. Prove read-only users cannot invoke payload/write/erase/repartition capabilities.
11. Run protocol backends in isolated Facilities with exact source/licence/SBOM evidence.
12. Reinspect and map internal SPD/Unisoc source when a discoverable handoff/path is available.
