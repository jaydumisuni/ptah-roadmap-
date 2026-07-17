# Donor Record — libguestfs

**Phase:** 0A / WP06  
**Status:** FIRST-PASS COMPLETE — PRIMARY ISOLATED DISK/FILESYSTEM INSPECTION CANDIDATE  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/libguestfs/libguestfs
- Default branch: `master`
- Pinned commit: `7dc893fdc36d4ddb02fded98c7a722367feb95de`
- Licence: library LGPL-2.1-or-later; command-line programs GPL-2.0-or-later; examples have separate liberal terms.
- Activity: Active and mature
- Classification: Isolated disk-image, partition, LVM, filesystem and guest-inspection machinery
- Ptah targets: raw/virtual disk image inventory, read-only mounts, partitions, logical volumes, filesystems, guest OS metadata, encrypted-volume opening, file extraction and isolated mutation copies

## Files/components inspected

- `README`
- `COPYING`
- `COPYING.LIB`
- `lib/guestfs.pod`
- `docs/guestfs-security.pod`
- search-located LUKS/cryptsetup and filesystem inspection components

## Verified capabilities and patterns

### Disk and filesystem model

- Accepts virtual-machine images, raw disk images, physical-disk copies, block devices and multiple related drives.
- Requires an explicit handle lifecycle: create, add drives, launch appliance, inspect/mount, shutdown and close.
- Lists devices, partitions, LVM physical/volume groups/logical volumes and filesystems.
- Can inspect unknown images and identify guest operating-system/filesystem information.
- Mounts filesystems inside the libguestfs appliance and exposes file/directory operations through the API.
- Supports read-only drive addition and read-only mounting.
- Supports partition-table and LVM creation/modification through separate mutation APIs.
- Can download arbitrary files or groups of files from an image and upload/write content when explicitly opened writable.
- Supports cryptsetup/LUKS-related operations and Clevis paths through appliance components.

### Isolation/security architecture

- Explicitly warns never to mount untrusted guest filesystems directly on the host kernel using loop/kpartx-style methods.
- Uses a layered model: untrusted filesystem → appliance kernel → non-root QEMU → optional libvirt/sVirt/SELinux → host kernel.
- Advises forcing the expected image format rather than allowing QEMU format autodetection, preventing crafted backing-file/header attacks.
- Warns that adding a live VM image read-write will almost certainly corrupt it; read-only is the safe inspection default.
- Treats guest filenames, strings, configuration and metadata as untrusted data requiring escaping and size/content controls.
- Warns against executing commands recovered from the guest.
- Documents historical filesystem/QEMU/parser CVEs and denial-of-service risks, reinforcing the need for patched isolated appliances.
- Protocol messages have defined size limits, but caller-side output/resource controls remain required.

### Platform and operation separation

- Virtual appliance device paths are independent of host device names.
- Multiple disk images can be attached for one related guest.
- Explicit format and read-only flags can be supplied per drive.
- Read-only inspection and writable customization are distinct choices.
- Higher-level tools such as guestfish, virt-inspector, virt-rescue and virt-customize sit above the library.

## What libguestfs completes

- A hardened alternative to direct host-kernel filesystem mounts.
- Unified disk→partition/LVM→filesystem→file inspection.
- Read-only extraction from raw and virtual disk images.
- Guest OS inspection and filesystem-aware views.
- Isolated mutation/customization paths for copied images.
- Encrypted-volume and multi-disk/LVM handling.
- A mature service/tool boundary suitable for Ptah rather than embedding many filesystem parsers directly into the control plane.

## Important limitations for Ptah

- libguestfs is a disk/filesystem access appliance, not Ptah's Object Graph, Session model or canonical partition parser.
- Exact image-format support depends on QEMU and appliance build features.
- The library and programs have different LGPL/GPL boundaries; CLI/tool redistribution and modifications require licence compliance.
- Launching the appliance adds latency and resource overhead unsuitable for every shallow detector operation.
- Filesystem inspection strings and guest configuration can be false, malicious or oversized.
- Read-only mounting prevents ordinary writes but journal replay/filesystem semantics still require careful flags and verification.
- Encrypted volumes require credential references and may remain locked/partially identifiable.
- Direct file download does not automatically register hashes, parent filesystem relationships or privacy classifications.
- Partition/LVM/filesystem mutation APIs can destroy data and must not be available through the default read-only pack.
- FUSE/local mounting can expose paths to other host processes and requires separate access/lifecycle controls.
- Related multi-disk sets need exact ordering/identity; wrong combinations can produce misleading or corrupt views.
- Snapshots/backing chains and virtual image references need explicit validation to prevent host-file escapes.
- Application-consistent inspection of a live VM requires a snapshot/quiesce reference; read-only attachment alone does not guarantee temporal consistency.
- The appliance can still be compromised by a sufficiently chained kernel/QEMU vulnerability; isolation reduces but does not eliminate risk.
- Main-branch pin is research evidence, not the final stable release for Phase 0C.

## Must not be inherited

- untrusted filesystem mounted directly on the Ptah Node host kernel.
- image format autodetection used for untrusted images when expected format is known.
- live VM disks opened read-write.
- read-only inspection and mutation APIs exposed through one undifferentiated capability.
- guest hostname/configuration treated as authoritative external truth.
- recovered guest binaries executed during decomposition.
- provider/appliance device names used as canonical Ptah Object identity.
- credentials passed in logs/command lines or retained in guest metadata.
- GPL command-line source copied into permissive Ptah Core without a compliant boundary.
- successful mount interpreted as filesystem consistency or complete recovery proof.

## Integration decision

**ADOPT AS THE PRIMARY ISOLATED DISK/FILESYSTEM INSPECTION AND MOUNT BACKEND, THROUGH A SEPARATE FACILITY/APPLIANCE.**

Ptah should expose separate capabilities:

- disk/image format and backing-chain inventory;
- read-only device/partition/LVM/filesystem inventory;
- read-only mount and file extraction;
- encrypted-volume unlock with scoped credential references;
- guest OS inspection as a non-authoritative View;
- copied/overlay-backed mutation and rebuild through separately authorized Activities.

Lower-level partition/image parsers and AOSP sparse/super tools remain completion donors. libguestfs does not replace the Ptah Disk/Partition/Filesystem schemas.

## Native Ptah gap

Ptah must define:

- disk image Object and explicit format/backing-chain schema;
- disk→partition-table→partition→LVM→filesystem→file relationships;
- device/partition offsets, sizes, sector sizes, GUID/type/flags and hashes;
- filesystem type, UUID/label/features/journal/dirty state and mount recipe;
- multi-disk set/order/relationship identity;
- encrypted-container/credential-required/unlocked View relationships;
- read-only versus overlay/copy-on-write versus writable-mutation capabilities;
- application snapshot/quiesce and temporal-consistency receipts;
- extracted file Object registration, paths, metadata and privacy;
- exact appliance/QEMU/kernel/tool build and SBOM receipt;
- mount/session cleanup, timeout, cancellation and restart recovery;
- format-forcing and backing-file access policy;
- stable-release/package/licence boundary.

## Exit strategy

Ptah's Disk/Filesystem Domain Pack remains implementable through libguestfs, guestfish/virt tools, platform-native parsers, The Sleuth Kit, qemu-nbd in a hardened helper or filesystem-specific services. Disk, Partition, Filesystem and File Object identities remain backend-neutral.

## Validation required

1. Inspect representative raw, qcow2, VMDK/VHD-like and physical-disk-copy inputs with explicit format declarations.
2. Reject crafted backing-file/header format confusion and host-path escapes.
3. Map GPT/MBR, LVM and filesystems into typed Objects with exact offsets/sizes/hashes.
4. Mount untrusted filesystems read-only inside the appliance and extract files without direct host-kernel mounting.
5. Test ext4, XFS, Btrfs, FAT/exFAT, NTFS and other selected filesystems under a pinned appliance feature set.
6. Open LUKS/encrypted content with scoped credentials and retain locked/unlocked state without leaking secrets.
7. Inspect a consistent snapshot of a running VM and distinguish it from an unquiesced live-disk View.
8. Crash/timeout the appliance and prove Ptah Core and completed child Objects survive.
9. Perform a mutation only on an overlay/copied image, retain before/after Objects and validate/reopen the result.
10. Pin a stable libguestfs/QEMU/appliance build with SBOM/licence evidence and replace the backend for one read-only view without identity changes.
