# Internal Recovery Record — Apple Tool, Compatibility and Ramdisk Foundations

**Phase:** 0A / WP06  
**Status:** FIRST-PASS COMPLETE — TOOL/DEVICE COMPATIBILITY EVIDENCE, NOT YET AN IPSW DOMAIN PACK  
**Inspected:** 2026-07-17

## Sources inspected

### TechGuyCheckm8

- Repository: `jaydumisuni/TechGuyCheckm8`
- Visibility: Public
- Pinned commit: `29f97f5a4c3bea0a7290ac55d8ea72981ebe49ba`
- Root README only labels the project as a jailbreak tool.
- The initial import also contains broader TechGuy Tool/Doctor/model-database support rather than a standalone verified firmware parser.
- No root licence was confirmed during this pass; do not extract code into public Ptah until ownership/licence is explicit.

### TechGuyTool Ramdisks

- Repository: `jaydumisuni/ttgtool-ramdisks`
- Visibility: Public
- Pinned commit: `70612b8007681ba98ed7708ae8f45bc997683b98`
- Repository currently documents ramdisk naming/compatibility rather than publishing a complete auditable file set at the inspected pin.
- No root licence was confirmed.

### TG Doctor Index

- Repository: `jaydumisuni/tg-doctor-index`
- Visibility: Public
- Pinned commit: `526e044c0fe626aaf57ad72ce402d0fb524c9801`
- File inspected: `apple-mac.json`
- No root licence was confirmed.

## Verified implemented/documented behavior

### Tool health and dependency index

- A versioned macOS doctor index (`version: 2.5`) declares required Apple tooling and health checks.
- The index describes a downloadable TechGuyCheckm8 pack and checks for `irecovery` presence/execution.
- It separately checks Python/pyusb, libusb, libimobiledevice/usbmuxd and ipwndfu availability.
- Installation/check behavior is represented as data rather than only hard-coded UI logic.
- Tool availability is verified through explicit commands or file checks.
- The index includes an Arduino/helper presence path for USB-host/device workflows.

### Ramdisk compatibility naming

- Ramdisk assets are intended to follow `{device_id}-{board}_ios{major}` naming.
- The documented catalogue distinguishes Apple product identifiers/board variants and supported iOS major ranges.
- Coverage includes several checkm8-era iPhone and iPad families.
- Device model and board identity are treated as compatibility inputs rather than only marketing names.

### Broader tool-shell evidence

- The TechGuyCheckm8 import contains a headless Doctor/check/fix model with stable check IDs, human names, severity, details and optional fix IDs.
- The Doctor checks Apple-tool presence separately from Android tools and other runtime/environment health.
- The imported project also contains brand/model database merge behavior that backs up prior data before in-place updates and deduplicates model records.

## Strong internal patterns for Ptah

1. Apple operation capability depends on exact product/board/iOS/tool compatibility rather than one generic “iPhone supported” flag.
2. Device/tool compatibility data should be versioned and inspectable as data.
3. Tool presence and runtime health belong to a Facility capability/Doctor record.
4. Ramdisk, restore image and support assets require exact device/board/build relationships.
5. Downloaded tool packs need install/check/health metadata rather than silent assumptions.
6. Compatibility database updates should preserve backups and report what changed.
7. Apple device communication, firmware package analysis, ramdisk preparation and physical device operations are different Facilities/Activities.

## Important limitations

- The inspected internal repositories do not yet establish a neutral IPSW/OTA parser, BuildManifest parser or Apple firmware Object graph.
- No verified relationship was recovered among IPSW build identity, product/board configuration, component filenames, cryptographic digests and ramdisk assets.
- Ramdisk coverage is documented by naming/table, but file hashes, build provenance, source IPSW, toolchain and verification evidence are not present in the README.
- Tool-pack download references use mutable latest/archive URLs rather than immutable content digests in the inspected index.
- Tool health checks verify executable presence/help/version behavior, not authenticity or compatibility with one exact device operation.
- ipwndfu/checkm8-style tooling is device-exploitation/runtime machinery, not a firmware-analysis foundation.
- Public repository names/content include jailbreak/service-operation concerns that must not be conflated with neutral firmware decomposition.
- No restore/session/backup/SHSH/SEP/baseband compatibility model was recovered in this pass.
- No root licences were confirmed for these internal repositories.
- The Apple tooling path is macOS/Linux/USB-environment sensitive and cannot be assumed on every Ptah Node.

## What Ptah should retain

- exact product/board/build compatibility records;
- versioned tool-health manifests;
- immutable ramdisk/restore-asset identities and source relationships;
- separate analysis, preparation and physical-device operation Facilities;
- explicit unsupported and missing-capability states;
- compatibility-data updates as reviewed/versioned Objects;
- health checks that do not expose secrets.

## What Ptah must not inherit

- jailbreak/checkm8 identity as the Apple Firmware Domain Pack.
- mutable release URLs as proof of exact tools/assets.
- marketing model name as sufficient compatibility.
- executable presence as proof of correct device support.
- ramdisk filename alone as authoritative provenance.
- downloaded binaries/assets without hashes, signatures, SBOM/licence and source records.
- physical device exploit/restore actions inside static firmware decomposition.
- private/unlicensed source or payloads copied into public Ptah.

## Classification

**ADAPT THE COMPATIBILITY/DOCTOR/ASSET-IDENTITY REQUIREMENTS; REBUILD THE APPLE FIRMWARE DOMAIN PACK AROUND AUTHORITATIVE IPSW/OTA METADATA AND MATURE PARSERS.**

This internal evidence informs `FW-001`, `CORE-004`, `DEVICE-001`, `OBS-001` and the firmware-asset relationship model. It does not close Apple firmware analysis by itself.

## Native Ptah completion required

- Apple product/build/board/device schema;
- IPSW/OTA manifest and component relationships;
- exact component size/digest/signature/encryption/key state;
- restore ramdisk/kernelcache/iBoot/SEP/baseband/DeviceTree/trustcache/filesystem relationships;
- source catalogue and immutable download receipts;
- compatibility claims for analysis, ramdisk preparation and restore separately;
- tool/asset package hashes, signatures, licences and provenance;
- SHSH/APTicket/SEP/baseband compatibility records where caller workflows require them;
- strict separation of static analysis from exploit/DFU/recovery/restore device operations;
- bounded parser/provider execution and cross-platform capability reporting.

## Validation inherited into Ptah

1. Resolve one Apple product/board/build to the exact IPSW/OTA and component manifest.
2. Bind every ramdisk/tool asset to immutable hashes and source/build provenance.
3. Reject a ramdisk/tool whose product/board/iOS compatibility does not match the target.
4. Report missing macOS/Linux/USB tool capability without degrading unrelated firmware analysis.
5. Preserve compatibility-database revisions and evidence for every change.
6. Prove static IPSW decomposition works without connecting or exploiting a device.
7. Require separate caller-authorized Activities and receipts for DFU/recovery/restore operations.
8. Complete licence/source verification before redistributing any tool pack or payload.
