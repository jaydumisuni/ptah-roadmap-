# ADR-0008 — Disk Images, Firmware Packages and Physical Device Operations Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Phase:** 0A firmware, disk and filesystem closure

## Context

Ptah must analyze firmware packages, disk images and filesystems while also supporting specialist physical-device operations through compatible Nodes and Facilities.

These tasks are often dangerously collapsed:

- a package filename is treated as device compatibility;
- USB mode presence is treated as service readiness;
- a loader/programmer/FDL is selected by chipset name alone;
- package extraction is treated as successful flashing;
- write/erase protocol acknowledgement is treated as verified physical state;
- live device partitions are modified before an immutable backup exists;
- encrypted or signed components are silently replaced by decrypted/patched copies;
- disk images are mounted directly on the host;
- static analysis tools expose destructive operations in the same capability surface.

The inspected internal and external sources supply complementary pieces:

- Apple internal tool/ramdisk compatibility plus blacktop/ipsw package/BuildManifest analysis;
- internal read-only MediaTek META proof plus MTKClient GPT/flash machinery;
- Qualcomm Sahara/Firehose/EDL;
- Unisoc PAC/BootROM/FDL composition;
- Android update payload, sparse, super/dynamic partition and AVB specifications;
- Samsung Heimdall/Odin/PIT;
- libfdisk partition tables;
- libguestfs isolated filesystems;
- generic Binwalk/LIEF/libarchive/SRLabs Extractor coverage.

No firmware tool or device protocol is universal Ptah truth.

## Decision

Ptah owns separate but linked contracts for:

1. **Firmware Package Object** — immutable downloaded/acquired package bytes.
2. **Disk/Image Object** — immutable raw, sparse or virtual disk/partition bytes.
3. **Package/Image Manifest Graph** — components, operations, partitions, filesystems and verification claims.
4. **Device Profile** — observed physical device identity, hardware, transport and layout.
5. **Compatibility Result** — evidence-backed comparison among package, image, loader/programmer and device.
6. **Static Firmware/Disk Activity** — detect, inventory, decompose, verify, compare and rebuild copies.
7. **Physical Device Activity** — connect, boot mode, service session, read, backup, write, erase, reset, restore or flash.
8. **Operation Receipt** — exact proof level, attempt, source/target ranges, backend and authoritative read-back.

Static analysis never grants device-write capability automatically.

---

# Firmware Package and Image identities

Every original package/image is an immutable Ptah Object with qualified content digests and source records.

Potential package/image types include:

```text
apple_ipsw
apple_ota
mtk_scatter_package
unisoc_pac
unisoc_p5c_unknown
qualcomm_rawprogram_package
samsung_odin_package
android_update_payload
android_sparse_image
android_super_image
android_partition_image
raw_disk_image
qcow2_image
vmdk_image
vhd_or_vhdx_image
vendor_firmware_container
unknown_firmware_container
```

Filename/extension/model name is never sufficient identity or compatibility evidence.

## Source and catalogue record

A downloaded package retains:

```text
source_id
catalogue_or_vendor
url_or_provider_reference
product_or_model_claim
version_and_build_claim
expected_size
expected_vendor_digest_claims
etag_or_generation
last_modified
acquired_at
transfer_activity_id
verified_content_digests
signature_or_catalogue_receipts
```

Weak vendor/catalogue hashes such as SHA-1 remain claims while Ptah computes a stronger Object digest.

---

# Firmware Manifest Graph

A package can contain:

- manifests and metadata;
- loaders, programmers, FDLs, preloaders and Download Agents;
- bootloaders and kernel images;
- partition images;
- sparse/raw/delta representations;
- restore ramdisks;
- device trees;
- modem/baseband/SEP/co-processor firmware;
- vbmeta/AVB descriptors;
- filesystem images;
- patch/rawprogram/repartition plans;
- encrypted/signed/compressed components;
- checksums and signatures.

Each component becomes an Object or View linked to the package with exact path/offset/size/digest/role and parser provenance.

## Package operation graph

Packages that encode operations rather than only files retain an explicit graph:

```text
operation_type
source_component_or_partition
source_extents
source_hash
payload_blob_offset_and_length
destination_partition
destination_extents
destination_hash
compression_or_patch_algorithm
ordering_dependencies
required_source_build_or_layout
```

Android OTA operations, rawprogram/patch XML and repartition plans are represented as reviewable plans before execution.

---

# Disk, partition and filesystem graph

Relationships:

```text
disk_image
  contains partition_table
partition_table
  contains partitions
partition
  may contain lvm_or_dynamic_metadata
lvm_or_dynamic_metadata
  maps logical_volumes_or_partitions
partition_or_logical_volume
  contains filesystem_or_raw_payload
filesystem
  contains files/directories/metadata
```

Records retain:

- image format and backing chain;
- sector size and alignment;
- partition-table type/version;
- primary/backup table copies;
- CRC/checksum validity;
- partition index, GUID/type/name/attributes, LBA and byte range;
- LUN/physical block device;
- logical extents and groups;
- filesystem type, UUID, label, features, journal/dirty state;
- encryption container and unlock state;
- snapshot/overlay relationships.

Partition names, GUIDs and filesystem labels are metadata claims, not Object identity.

## Sparse and virtual images

Sparse/virtual encoding and expanded logical content are separate Objects/Views.

A sparse file's byte size is not the expanded partition size. Don't-care extents retain explicit semantics.

Virtual-image backing files are resolved only through approved Object/location references. Untrusted image headers cannot name arbitrary host files.

---

# Read-only and mutation capability separation

Every Firmware/Disk/Device Facility declares independent capabilities.

## Static/read-only capabilities

```text
detect_package
inventory_manifest
extract_components
verify_digests_and_signatures
compare_packages
parse_partition_table
inspect_filesystems_read_only
mount_in_isolated_appliance
read_device_identity
read_device_layout
read_partition_or_region
create_backup
```

## Mutation/device capabilities

```text
write_partition_or_region
erase_partition_or_region
repartition
patch_image
rebuild_package_or_image
load_device_programmer_or_fdl
execute_payload
reset_or_reboot
restore_or_flash
unlock_or_change_security_state
write_rpmb_or_efuse_or_nv_data
```

A caller/role/Firmare Pack receiving read-only capabilities cannot invoke mutation through generic raw-command escape hatches.

Arbitrary XML, shell, payload, poke, memory-write or protocol commands are separate high-risk capabilities and disabled by default.

---

# Device Profile

A connected target receives a stable observed profile containing only appropriate/redacted public fields and protected sensitive fields.

Common fields:

```text
device_profile_id
node_id
connection_epoch
transport
usb_vid_pid_interface_endpoints
protocol_and_version
manufacturer_and_platform
product_model_board
soc_chip_hwid
security_state
storage_type_and_sector_size
luns_or_boot_areas
partition_table_digest
firmware_build_and_patch_claims
boot_mode_or_service_mode
backend_capabilities
observed_at
```

Vendor-specific extensions include:

- Apple product/board/chip/security domain/build;
- MTK hwcode/BROM/Preloader/DA/META/security state;
- Qualcomm HWID/OEM/model/PKHash/Sahara/Firehose/storage;
- Unisoc chipset/board/BootROM/FDL1/FDL2/base addresses;
- Samsung Download Mode/Odin protocol/PIT/build/binary revision.

Sensitive serials, hardware hashes, IMEI, calibration/NV data, keys and partition contents remain private Objects/receipts.

---

# Connection and service proof levels

Physical-device state progresses through explicit proof levels:

```text
usb_detected
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

Examples:

- MTK PID_2007 is not a valid META read session.
- Qualcomm PID_9008 is not a configured Firehose session.
- Samsung `LOKE` is not package/device compatibility.
- Unisoc BootROM payload upload is not FDL2 partition-service readiness.

A higher proof level is never inferred from a lower one.

---

# Loader, programmer, FDL and tool identity

Executable device-side assets are first-class Objects.

```text
loader_object_id
role
vendor_or_source
content_digest
signature_or_trust_claim
licence_and_redistribution_state
supported_soc_hwid_board_models
required_base_address_or_mode
storage_or_protocol_capabilities
source_package_or_database
known_limitations
verification_receipts
```

Selection requires exact evidence. Chipset-family similarity alone is insufficient where board initialization, pin maps, signatures or secure boot differ.

Unknown/mismatched assets are rejected before execution.

---

# Compatibility Result

Compatibility is a durable record, not a boolean guessed from filenames.

It compares:

- package product/build/board/chip claims;
- component roles and target partitions;
- device profile and security/storage state;
- live partition layout digest;
- loader/programmer/FDL compatibility;
- source requirements for delta payloads;
- rollback index and trusted-key state;
- package signature/digest verification;
- binary revision/anti-rollback requirements;
- missing or unknown evidence.

Possible outcomes:

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
```

A package may be analyzable while not writable to the selected device.

---

# Backup and read-before-write rule

Before any destructive or uncertain physical mutation, Ptah requires an operation-specific backup/checkpoint unless the caller explicitly accepts a documented exception and the Facility declares why backup is impossible.

Backup records include:

- selected device/profile/connection epoch;
- exact LUN/partition/region/offset/length;
- pre-operation bytes and qualified digest;
- partition table/layout copy;
- relevant NV/calibration/configuration data according to privacy policy;
- read backend/tool/loader identity;
- verification and storage locations;
- restoration recipe and compatibility limits.

A backup is not valid merely because a file exists; expected size/range and digest must be verified.

## Non-retryable physical operations

Write, erase, repartition, reset, security-state, RPMB/eFuse/NV and device-side payload operations default to:

```text
retry_requires_authoritative_read_back
manual_resume_only
or non_retryable
```

Transport loss cannot trigger blind replay.

---

# Post-operation verification

Protocol ACK/process exit is an intermediate receipt.

A write operation must attempt independent verification appropriate to the capability:

- read back exact range and compare digest;
- retrieve updated partition table/layout;
- verify vbmeta/AVB/signature/rollback state;
- reopen and parse rebuilt image;
- observe expected boot/service mode;
- compare device-reported build/version;
- retain limitations when read-back is unavailable.

`write_acknowledged` and `write_read_back_verified` are separate states.

---

# Static analysis versus physical application

Static Firmware/Disk Packs must work without a connected device.

Static operations include:

- download/acquire;
- hash/signature verification;
- manifest/package inventory;
- component extraction;
- disk/partition/filesystem inventory;
- read-only isolated mount;
- comparison;
- reconstruction/rebuild of a copy;
- compatibility analysis.

Physical operations require:

- selected Device/Node;
- current connection epoch;
- exact capability/service session;
- compatibility result;
- caller authorization;
- backup/checkpoint;
- operation receipt and read-back strategy.

No static package parser can invoke flashing implicitly.

---

# Mounted filesystem boundary

Untrusted disk/filesystem images are mounted only in isolated appliances/providers such as libguestfs.

Rules:

- no direct host-kernel loop/kpartx mount for untrusted content;
- expected image format is forced where known;
- backing files resolve only through approved Object references;
- read-only is default;
- writable work uses copy-on-write overlays or copied images;
- guest commands are not executed during decomposition;
- mount/session cleanup is durable and observable;
- extracted files become hashed child Objects.

---

# Encryption, signatures and trust

States remain explicit:

```text
unencrypted
locked_encrypted
credential_required
decrypted_child_created
signature_present
signature_valid_untrusted_key
signature_valid_trusted_key
signature_invalid
rollback_state_unknown
rollback_allowed
rollback_blocked
verification_disabled
hashtree_disabled
```

Decrypted/patched/rebuilt outputs never replace the encrypted/signed original or inherit its trust state.

Keys/passwords/programmer credentials remain scoped credential references.

---

# Vendor-pack direction

## Closed v1 vendor packs

- Apple IPSW/OTA analysis.
- MediaTek package/device-profile and read/flash backend contract.
- Qualcomm EDL/Sahara/Firehose contract.
- Unisoc PAC/FDL contract.
- Android OTA/sparse/super/AVB contract.
- Samsung package/PIT/Odin contract.

## Generic v1 pack

Unknown/vendor firmware uses the generic Binwalk/LIEF/libarchive/libguestfs/libfdisk/SRLabs extraction path and retains `unsupported_vendor_semantics` when no specific pack exists.

## Future optional packs

Huawei/Honor, Sony, LG, Oppo/Realme, ZTE, Allwinner, Rockchip, UEFI/BIOS, router/IoT and other specialist packs are added when samples and trustworthy parser evidence justify them.

## P5C

`.P5C` remains parked/unverified. Extension-only routing through PAC is forbidden until a verified sample/spec/tool closes the format.

---

# Backend and licence boundaries

- GPL tools such as MTKClient and Qualcomm EDL run as separate Facilities/services.
- Vendor DLLs, loaders, programmers, FDLs, ramdisks, keys and driver packs require independent rights/provenance review.
- Internal private engines remain private unless source/ownership/licence review authorizes extraction.
- Public Ptah schemas contain neutral Device/Firmware concepts, not proprietary tool names or private workflows.
- Backends are replaceable behind the same contracts.

---

# Donor decisions

- **blacktop/ipsw:** primary Apple package/manifest/extraction backend.
- **Internal Apple tools:** compatibility/tool-health/ramdisk requirements, not IPSW parser.
- **Internal MTK META:** proven read-only service-session evidence.
- **MTKClient:** primary GPL GPT/partition/flash backend.
- **Qualcomm EDL:** primary GPL Sahara/Firehose backend.
- **Unisoc composition:** native PAC parser direction, MIT protocol reference and optional backend after licence proof.
- **AOSP update_engine/libsparse/liblp/libavb:** authoritative Android image/OTA specifications.
- **payload-dumper-go:** full-payload extraction completion backend only.
- **Heimdall:** optional Samsung Odin/PIT backend after modern tests.
- **libfdisk:** primary partition-table parser/plan donor.
- **libguestfs:** primary isolated filesystem inspection/mount backend.
- **SRLabs Extractor:** isolated generic format-router/comparison backend.
- **P5C:** parked pending verified evidence.

---

# Consequences

## Positive

- Firmware analysis can be safe, useful and online without connected devices.
- Physical mutation cannot hide behind a generic parser or raw-command function.
- Package, loader/programmer, device and layout compatibility become explicit evidence.
- Every destructive operation has a backup/read-back path or an explicit documented exception.
- Vendor backends remain replaceable.
- Unknown/proprietary firmware can still receive generic Object decomposition without false support claims.
- Private identifiers, keys and vendor assets remain protected.

## Costs

- Device and package schemas are detailed and vendor extensions are required.
- Physical proof may take additional reads/storage/time.
- Some devices cannot support complete read-back or backups, resulting in honest limits rather than one-click claims.
- GPL/vendor backends require process/service isolation and packaging work.
- Maintaining golden device/package/loader profiles is ongoing work.
- USB driver and mode transitions add Node-specific complexity.

## Do-not-break rule

> Never treat a firmware filename, package extraction, USB VID/PID, protocol handshake, loader upload, command ACK, process exit, sparse expansion, mounted filesystem or rebuilt image as proof of device compatibility or successful physical application. Static Objects, device profiles, compatibility, mutation, backup and authoritative read-back remain distinct.

---

# Required proof before freeze

1. Parse representative Apple, MTK, Qualcomm, Unisoc, Samsung and Android OTA packages without connected devices.
2. Register exact component/manifest/partition/image relationships and hashes.
3. Inspect raw/virtual disks through libfdisk/libguestfs without direct host mounts.
4. Preserve encrypted originals and create separate decrypted children with credential/key receipts.
5. Establish USB/protocol/service proof levels independently on representative devices.
6. Match loaders/programmers/FDLs/ramdisks to exact target evidence and reject mismatches.
7. Compare package layout and live device GPT/PIT/partition lists before mutation.
8. Create immutable verified backups before an authorized write.
9. Perform one controlled write per vendor family only where legal/safe test hardware exists, then read back and verify exact bytes/state.
10. Disconnect/re-enumerate mid-operation and reject stale receipts/blind retries.
11. Prove read-only users and static packs cannot access write/erase/reset/raw-command capabilities.
12. Crash/timeout a native/vendor backend while Ptah Core and completed Objects survive.
13. Replace one backend in each major family without changing public schemas.
14. Keep P5C and unsupported vendor semantics honest until verified evidence exists.
