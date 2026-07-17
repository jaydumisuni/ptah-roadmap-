# Phase 0A — WP06 Firmware, Disk and Filesystem Composition

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Runtime code:** NOT STARTED

## Purpose

Close the firmware-package, disk-image, partition, filesystem, vendor compatibility and physical-device mutation boundaries through a composite donor set while preserving strict read-only/static analysis defaults.

## Sources inspected and saved

### Internal

- Apple tool/ramdisk/device-compatibility foundations
- MediaTek native read-only META handoff and MTKClient META-mode bridge
- Android OTA updater-package device-control utility
- Android driver repository gap
- private Device Manager firmware-engine source recovery gap
- MIBU proof/correlation evidence from WP02C

### External/upstream

- blacktop/ipsw
- MTKClient
- Qualcomm EDL/Sahara/Firehose
- Unisoc PAC/BootROM/FDL composition
- AOSP update_engine payload metadata
- AOSP libsparse
- AOSP liblp dynamic-partition metadata
- AOSP AVB/libavb
- payload-dumper-go
- Samsung Heimdall/Odin/PIT
- libguestfs
- util-linux libfdisk
- SRLabs Extractor
- Binwalk, LIEF and libarchive reuse from WP05

### Explicitly parked/unresolved

- `.P5C` firmware format
- JuiceFS/SeaweedFS remained parked from WP04 and are not disk-image parsers
- exact private Qualcomm/Unisoc Device Manager modules pending local/source-tree recovery

Saved records:

- `internal/APPLE-TOOL-FOUNDATIONS.md`
- `internal/MTK-META-FOUNDATIONS.md`
- `internal/ANDROID-OTA-CONTROL.md`
- `internal/ANDROID-DRIVER-REPOSITORIES.md`
- `internal/DEVICE-MANAGER-FIRMWARE-ENGINE-RECOVERY-GAP.md`
- `donors/BLACKTOP-IPSW.md`
- `donors/MTKCLIENT.md`
- `donors/QUALCOMM-EDL.md`
- `donors/UNISOC-PAC-FDL.md`
- `donors/ANDROID-OTA-IMAGE-FOUNDATIONS.md`
- `donors/SAMSUNG-HEIMDALL.md`
- `donors/LIBGUESTFS.md`
- `donors/LIBFDISK.md`
- `donors/OTHER-FIRMWARE-COVERAGE.md`
- `donors/P5C-STATUS.md`

## Composite result

```text
Ptah Firmware Package Object
  immutable acquired/downloaded package identity and source catalogue evidence

Ptah Firmware Manifest Graph
  components, loaders/programmers, images, operations, signatures and encryption states

Ptah Disk/Image Graph
  format, backing chain, partition table, partitions, LVM/logical partitions,
  filesystems and extracted files

Ptah Device Profile
  transport, connection epoch, protocol/service state, hardware/profile,
  security, storage and observed layout

Ptah Compatibility Result
  package + loader/programmer/FDL + device + layout + security/rollback evidence

Static Firmware/Disk Domain Packs
  detect, inventory, extract, verify, compare, mount read-only and rebuild copies

Physical Device Facilities
  connect, load stage/programmer, read, backup, write, erase, reset and flash
  with independent capabilities and receipts
```

No firmware tool, package extension, USB state or protocol acknowledgement is universal truth.

## Vendor composition

### Apple

- Internal compatibility/tool-health/ramdisk records.
- blacktop/ipsw for BuildManifest, product/board/build/component inventory, extraction, diff and encrypted component states.
- Device interaction, TSS, restore, patching and exploit paths remain separately gated.

### MediaTek

- Native internal META read-only attach/inventory proof.
- MTKClient as separate GPL GPT/partition/full-flash backend.
- BROM, Preloader, DA, V6, META, stock and exploit modes remain distinct.
- APDB/MDDB/loaders/preloaders are first-class compatibility Objects.

### Qualcomm

- EDL transport, Sahara identity, programmer selection and Firehose storage/GPT/LUN/partition layers.
- Rawprogram/patch XML is parsed into a reviewed operation graph before execution.
- DIAG remains a separate future Facility from EDL/Firehose.

### Unisoc

- Native safe PAC parser direction.
- BootROM, FDL1, FDL2 and partition service remain distinct levels.
- `sprdproto` provides an MIT transport reference.
- `spreadtrum_flash` remains optional/study pending licence and broader live proof.
- P5C remains parked.

### Android OTA/images

- AOSP payload, sparse, super/liblp and AVB schemas are authoritative foundations.
- Full/delta/source-dependent payloads remain distinct.
- payload-dumper-go is only a full-payload completion backend.
- package analysis and device application are separate.

### Samsung

- Heimdall supplies open Odin/Loke/PIT transport concepts.
- TAR/TAR.MD5/LZ4/AVB package decomposition remains static.
- Modern device/protocol coverage must be proven before physical use.

### Other vendor/embedded

- Generic Binwalk/LIEF/libarchive/libguestfs/libfdisk/SRLabs path closes v1 static coverage.
- Huawei/Honor, Sony, LG, Oppo/Realme, ZTE, Allwinner, Rockchip, UEFI/BIOS, router/IoT and other specialist packs remain extensible additions when samples and trustworthy parsers justify them.

## Disk/filesystem composition

- libfdisk is the direct partition-table parser and dry-run plan backend.
- libguestfs is the isolated filesystem/LVM/guest inspection and read-only mount backend.
- AOSP liblp handles Android logical partitions and `super` metadata.
- AOSP libsparse handles sparse/raw encoding relationships.
- Untrusted filesystems never mount directly on the Ptah host kernel.
- Image format and backing chains are explicit; autodetection/backing-file host escapes are rejected.
- Mutation uses copies/overlays by default and creates new Object identity.

## Accepted architecture

Saved as `decisions/ADR-0008-DISK-FIRMWARE-DEVICE-OPERATION-BOUNDARY.md`.

Key decisions:

1. Firmware Package, Disk/Image, Manifest Graph, Device Profile, Compatibility Result, Static Activity and Physical Device Activity are separate contracts.
2. Filename/model/chipset/partition name is insufficient compatibility evidence.
3. Package analysis works without a connected device.
4. USB detection, protocol handshake, loader/programmer stage, configured service session and physical read/write proof are distinct levels.
5. Read-only and mutation capabilities are separately declared and authorized.
6. Loader/programmer/FDL/ramdisk assets are immutable Objects with exact source, digest, licence and target compatibility.
7. Physical writes require reviewed compatibility, immutable backup and post-operation read-back where technically possible.
8. Write ACK/process exit is not verified physical state.
9. Non-idempotent physical operations are manual-resume/non-retryable unless authoritative read-back proves safe continuation.
10. Encrypted/signed originals remain preserved; decrypted/patched/rebuilt results are new Objects with new trust states.
11. Untrusted disk filesystems use an isolated appliance, not host loop mounts.
12. Vendor GPL/proprietary backends remain separate Facilities behind neutral Ptah contracts.
13. Generic static coverage does not imply vendor-aware flash support.
14. `.P5C` stays parked until an authoritative sample/spec/tool exists.
15. Private Device Manager engine source remains preserved for later exact recovery and is not credited without inspection.

## Requirement closure verdict

Closed for Phase 0B contract design:

- `FW-001` Apple firmware
- `FW-002` MediaTek firmware
- `FW-003` Unisoc firmware
- `FW-004` Qualcomm firmware
- `FW-005` Android OTA, sparse and dynamic partitions
- `FW-006` generic other-vendor/embedded firmware framework
- `FS-001` disks, partitions, images and filesystems
- firmware-side physical-operation boundary of `DEVICE-001`
- firmware/image relationships for `CORE-003` and `CORE-004`
- image/snapshot relationships for `SESSION-001`

Explicitly parked:

- `.P5C` format support until reopening criteria are met.

Still dependent on later groups:

- general Android device inventory/UI/screen/input runtime;
- Windows/macOS/Linux application runtimes;
- secure remote display;
- exact internal private Qualcomm/Unisoc source reuse decision;
- production driver packs;
- broader vendor-specific firmware packs beyond generic static analysis;
- actual legal/safe hardware test corpus and physical-operation proof.

## Phase 0B contracts required

1. Firmware Package and source catalogue schema.
2. Firmware manifest/component/operation graph.
3. Disk/image/format/backing-chain schema.
4. Partition-table/partition/LUN/logical-partition/filesystem relationships.
5. Device Profile and vendor extension schema.
6. USB/protocol/service connection proof levels.
7. Loader/programmer/FDL/DA/preloader/ramdisk Object and compatibility schema.
8. Package/device/layout/security/rollback Compatibility Result.
9. static/read-only versus mutation capability classes.
10. backup/read-before-write and restoration record.
11. write/read-back verification and partial/unknown states.
12. rawprogram/patch/payload/repartition plan schema.
13. encryption/signature/trust/rollback state schema.
14. isolated mount/session/overlay lifecycle.
15. sensitive identifier/NV/key privacy classifications.
16. backend/source/licence/SBOM records.
17. driver package and host-admin-change schema.
18. generic vendor pack and `unsupported_vendor_semantics` state.
19. parked-format reopening records.
20. physical operation retry/cancellation/recovery rules.

## Validation set

- package-only analysis across all major vendor families;
- exact package/component/partition/image hashes and relationships;
- raw/virtual disk inventory with libfdisk/libguestfs isolation;
- encrypted/signature/trust state preservation;
- separate USB/protocol/service proof levels;
- exact loader/programmer/FDL compatibility and rejection;
- package versus live device layout comparison;
- immutable backup before mutation;
- controlled writes followed by read-back on dedicated test hardware where legal/safe;
- stale connection-epoch rejection and no blind retries;
- read-only capability cannot reach raw write/erase/reset commands;
- parser/backend crash isolation;
- backend replacement without public schema changes;
- P5C/unsupported formats remain honest.

## Next Phase 0A group

Proceed with the **device and application runtime cluster**:

- internal Device Manager/MIBU/ADB/Fastboot/MTP/USB shared-core recovery;
- DeviceFarmer STF, adbkit, minicap and minitouch;
- Appium and UIAutomator2;
- scrcpy;
- TouchPilot upstream/fork relationship;
- Linux graphical application runtime completion and remote-display gateway;
- Windows and macOS application/VM/runtime boundaries;
- installed-package/device-file/screen/input/session relationships;
- physical-device lease, multi-device inventory, live display and semantic UI proof.

This group must build on ADR-0008: device runtime and UI control remain separate from firmware package analysis and destructive flashing.
