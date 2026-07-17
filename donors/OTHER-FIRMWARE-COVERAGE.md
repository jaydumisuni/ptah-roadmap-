# Donor Record — Other Vendor and Embedded Firmware Coverage

**Phase:** 0A / WP06  
**Status:** FIRST-PASS COMPLETE — GENERIC STATIC FOUNDATION CLOSED; VENDOR-SPECIFIC PACKS REMAIN EXTENSIBLE  
**Inspected:** 2026-07-17

## Primary generic donor

### SRLabs Extractor

- Canonical URL: https://github.com/srlabs/extractor
- Default branch: `master`
- Pinned commit: `c624b7e5de988e06f7dbdd78ace92a3d553e714b`
- Licence: Apache-2.0
- Classification: Android/vendor firmware format router and extraction workbench

## Files/components inspected

- `README.md`
- latest dependency update commit
- documented format/dependency, loop-mount and Docker boundaries
- WP05 generic donors: Binwalk, LIEF and libarchive
- WP06 vendor donors: Samsung Heimdall, Apple ipsw, MTKClient, Qualcomm EDL, Unisoc PAC/FDL and Android OTA/image foundations

## Verified generic coverage

SRLabs Extractor documents support for:

- Android sparse images;
- EROFS;
- ext-family filesystems;
- Android signed images;
- Android data images and Brotli variants;
- PAC;
- ZIP;
- LZ4;
- TAR/TAR.MD5;
- Sony SIN;
- Oppo OZIP;
- APP;
- LG KDZ;
- BIN;
- CPB;
- Android `super` images.

It can emit an extracted system-directory view or TAR output and supplies a Docker execution path.

Its dependency set includes Android sparse utilities, LZ4, Brotli, unrar, XML and Python libraries plus Git submodules.

The default host installation requires root because it uses temporary loopback mounts.

## Composite other-vendor direction

### Generic embedded/static foundation

- Binwalk maps embedded signatures, regions, entropy and carved unknown bytes.
- LIEF maps executable/boot/runtime structures.
- libarchive maps archive/container entries.
- libguestfs maps disks, partitions, LVM, filesystems and files through an isolated appliance.
- libfdisk maps GPT/MBR/other partition tables.
- AOSP sparse/liblp/AVB tools map Android image formats.
- SRLabs Extractor supplies a broad Android/vendor wrapper-routing comparison path.

### Vendor-specific packs already represented

- Apple: `blacktop/ipsw` plus internal product/board/ramdisk compatibility evidence.
- MediaTek: internal META read path plus MTKClient GPT/partition backend.
- Qualcomm: EDL/Sahara/Firehose.
- Unisoc: PAC/FDL composition.
- Samsung: Heimdall/Odin/PIT plus TAR/TAR.MD5/LZ4/AVB static components.

### Vendor-specific packs not yet fully closed

- Huawei/Honor UPDATE.APP and signed/encrypted variants;
- Sony SIN bundles beyond generic extraction;
- LG KDZ/DZ component metadata;
- Oppo/Realme OZIP/OPS variants;
- ZTE/ZTE-specific package and service protocols;
- Allwinner/PhoenixSuit image formats;
- Rockchip update images;
- UEFI/BIOS capsule/region/volume/filesystem firmware;
- router/IoT/embedded vendor packages;
- automotive, modem, Bluetooth/headset and other specialist firmware.

These formats may be registered and analyzed through generic detectors immediately. Exact vendor semantics require separate Domain Packs when samples, demand and trustworthy parser evidence exist.

## What this composition closes

- A public, extensible v1 route for unknown vendor/embedded firmware.
- Safe generic detection, embedded-region mapping, archive/disk/filesystem extraction and Object registration.
- A clear difference between generic parseability and vendor-aware compatibility/rebuild/flashing.
- An extension path that does not block Ptah v1 on every proprietary firmware ecosystem.
- A rule that unknown/custom wrappers remain immutable Objects with detector claims and carved children rather than being rejected or falsely classified.

## Important limitations

- SRLabs Extractor's broad format list does not prove complete or current support for every vendor/build/variant.
- Root/loopback mounting directly on the host is incompatible with Ptah's default untrusted-image isolation rule; use a bounded container/VM or libguestfs-style appliance.
- External tools/submodules determine actual supported formats, licences and security surface.
- Extracted directories are not automatically content-addressed Object graphs.
- Vendor package signatures, encryption, device compatibility and rebuild rules are not universally verified.
- Generic extraction does not establish flashability, authenticity or safe device application.
- Some proprietary formats may require legally restricted keys/tools or remain opaque.
- Format wrappers with the same extension may differ by vendor/version.
- Host-root requirements and loop mounts create a large blast radius unless isolated.
- Dependency versions in the current project include old packages alongside recent bumps and require SBOM/CVE review.

## Must not be inherited

- “supported format” interpreted as complete vendor-aware support.
- root loop-mount operations performed directly on the Ptah host.
- one generic extractor used as the canonical parser for every vendor.
- output directories treated as Object identity.
- proprietary signatures/encryption ignored after successful extraction.
- generic extracted partitions described as compatible with a device.
- firmware application/flashing enabled through the static generic pack.
- vendor packs promised without golden samples and live proof.

## Integration decision

**ADOPT A GENERIC FIRMWARE DOMAIN PACK OVER WP05/WP06 FOUNDATIONS; WRAP SRLABS EXTRACTOR ONLY AS AN ISOLATED COMPLETION/COMPARISON BACKEND.**

Ptah v1 closes `FW-006` at the framework level:

1. register and hash unknown firmware;
2. retain multiple detector claims;
3. map archives, embedded regions, disks, partitions, filesystems and Android images;
4. generate generic previews/inventories;
5. route recognized vendor types to optional packs;
6. retain `unsupported_vendor_semantics` where no trusted pack exists;
7. never expose physical flashing from the generic pack.

Vendor-specific rebuild/flash support is added only through versioned Domain Packs and exact compatibility receipts.

## Native Ptah gap

- vendor/format/variant claim and coverage-level schema;
- generic versus vendor-aware decomposition level;
- parser/tool dependency and capability manifest;
- isolated loop/mount/extraction provider;
- vendor signature/encryption/key states;
- exact sample/golden corpus and parser coverage receipts;
- format-specific component relationships;
- pack install/pin/upgrade/rollback lifecycle;
- legal/licence/key/tool restrictions;
- safe transition from static package analysis to separately authorized device operation.

## Exit strategy

Ptah's generic Firmware Domain Pack remains independent of SRLabs Extractor. New vendor parsers, commercial external tools or clean-room adapters can be added/removed without changing firmware Object identity or shared relationships.

## Validation required

1. Run a mixed corpus across sparse, EROFS/ext, TAR.MD5, SIN, OZIP, APP, KDZ, CPB, PAC, super and unknown BIN inputs.
2. Compare SRLabs output with native libarchive/Binwalk/libguestfs/AOSP/vendor-pack results and preserve disagreement.
3. Execute all root/loop-dependent extraction inside an isolated disposable provider.
4. Register every child as a hashed Object with exact parser/tool provenance.
5. Preserve opaque/encrypted/unsupported regions and never claim vendor compatibility from generic extraction.
6. Crash/timeout one external extractor without affecting Ptah Core.
7. Add one vendor pack later without reidentifying the original/child Objects.
8. Prove the generic pack has no device-write/flash capability.
