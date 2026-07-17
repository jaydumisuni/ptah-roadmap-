# Donor Record — util-linux libfdisk

**Phase:** 0A / WP06  
**Status:** FIRST-PASS COMPLETE — PRIMARY PARTITION-TABLE PARSER/PLAN CANDIDATE  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/util-linux/util-linux
- Component: `libfdisk`
- Default branch: `master`
- Pinned commit: `0f1198780cb90e388e037339662b15972f62c30b`
- Licence: LGPL-2.1-or-later for libfdisk source; util-linux programs/components have file-specific licences and require packaging review.
- Activity: Active and mature
- Classification: Low-level partition-table/label parser, abstraction and mutation-plan donor
- Ptah targets: GPT, DOS/MBR, BSD, SGI and Sun partition tables; sector geometry; partition types/GUIDs; primary/backup metadata; collision detection; sfdisk-compatible plans

## Files/components inspected

- `libfdisk/src/libfdisk.h.in`
- `libfdisk/src/gpt.c`
- search-located label, DOS, context, partition and script components

## Verified capabilities and patterns

- Provides a reusable context API separate from the interactive `fdisk` program.
- Supports DOS/MBR, Sun, SGI, BSD and UEFI GPT disk labels.
- Assigns regular files or devices explicitly in read-only or writable mode.
- Exposes device use, regular-file state, sector size, physical sector size, I/O alignment, first/last LBA, number of sectors, geometry and model information.
- Detects partition-table collisions and collision regions.
- Represents partition types through numeric codes, GUID strings, aliases, shortcuts and human-readable names.
- Provides partition-table and partition abstractions plus iterators/tables.
- Supports sfdisk-compatible script/dump representations for planned layouts.
- GPT implementation models protective/hybrid MBR, primary and backup GPT headers, disk GUID, usable LBAs, partition-entry arrays, per-entry type GUID, unique partition GUID, start/end LBA, attributes and UTF-16 names.
- GPT validates/uses header and partition-entry CRC32 fields and retains primary/backup headers separately.
- Unknown partition type GUIDs remain representable rather than being discarded.
- The API can be configured for list-only/read-only behavior independently of mutation functions.

## What libfdisk completes

- Direct partition-table inventory without launching a filesystem appliance.
- Exact sector/LBA/GUID/type/name/attribute relationships.
- Primary/backup GPT comparison and corruption evidence.
- MBR/protective/hybrid collision awareness.
- A common abstraction for several disk-label formats.
- Scriptable mutation-plan representation suitable for dry-run/review before a copied-image rebuild.
- Completion of libguestfs: libfdisk parses table structure directly; libguestfs mounts/inspects filesystems in isolation.

## Important limitations for Ptah

- libfdisk parses partition tables, not filesystem contents, Android dynamic partitions, vendor firmware manifests or device-flash protocols.
- Partition type/name is metadata, not proof of the actual contained filesystem or payload.
- Hybrid MBR/GPT, corrupt backup headers and overlapping entries require explicit conflict reporting rather than automatic repair.
- Read/write APIs coexist; Ptah must expose read-only inventory separately from layout mutation.
- Mutating a live block device or image can destroy data.
- Sector-size assumptions must match the actual image/device.
- A regular-file image may be sparse, truncated, layered or backed by another image format; libfdisk sees only the supplied byte stream.
- GPT CRC validity does not prove partition content integrity.
- Disk/partition GUIDs can be duplicated or spoofed and are not Ptah Object identity.
- UTF-16 partition names can contain malformed/untrusted content.
- Script/dump replay against a different-size or different-layout disk requires exact compatibility validation.
- The library is native code and should not share the long-lived control plane with hostile input.
- Main-branch pin is research evidence; Phase 0C should select a stable util-linux release/package.

## Must not be inherited

- partition name/type treated as content truth.
- disk or partition GUID used as canonical Ptah Object identity.
- automatic repair of primary/backup GPT disagreement.
- mutation APIs exposed through the default analysis capability.
- sfdisk script executed against a device/image without exact source/target comparison and backup.
- live block devices opened writable during static decomposition.
- sector-size/geometry assumptions omitted from receipts.
- valid GPT CRC interpreted as valid filesystem or firmware content.
- untrusted partition labels emitted without normalization/escaping.

## Integration decision

**ADOPT LIBFDISK AS THE PRIMARY LOW-LEVEL PARTITION-TABLE PARSER AND DRY-RUN LAYOUT-PLAN BACKEND.**

Ptah should use libfdisk in read-only mode for ordinary disk/image inventory and combine it with:

- libguestfs for isolated filesystem/LVM inspection;
- AOSP liblp for Android logical partitions;
- vendor backends for physical-device GPT/LUN reads;
- sparse/virtual-image adapters for byte-stream presentation.

Partition-table creation/repair/rewrite remains a separate mutation/rebuild Activity operating on a copied/overlay image unless explicitly authorized for a physical device.

## Native Ptah gap

Ptah must define:

- disk-label claim and parser-version receipt;
- disk geometry/sector/alignment/size schema;
- primary/backup/protective/hybrid table relationships;
- partition index, start/end LBA, byte offset/length, type, GUID, attributes, name and content hash relationships;
- table/entry CRC validity and disagreement/collision states;
- malformed/truncated/overlap/unknown-type states;
- read-only versus planned/mutated/rebuilt capability classes;
- source/target layout comparison and size compatibility;
- before/after disk-image Objects and rollback/checkpoint references;
- exact stable library build/version/licence record;
- provider isolation and resource limits.

## Exit strategy

Ptah's Partition Table contract remains backend-neutral. libfdisk, GPT fdisk, platform parsers, libguestfs, vendor tools or native Rust parsers can replace one another without changing Disk/Partition Object identity.

## Validation required

1. Parse representative GPT, DOS/MBR, hybrid/protective MBR, BSD, SGI and Sun labels from regular-file images.
2. Retain exact sector sizes, LBAs, byte ranges, GUIDs, attributes and normalized names.
3. Detect primary/backup GPT CRC disagreement, relocated backup headers, overlaps and collisions without automatic repair.
4. Compare libfdisk inventory with libguestfs and vendor-device GPT reads.
5. Feed malformed, truncated and oversized partition tables in a bounded provider.
6. Generate a dry-run sfdisk-compatible mutation plan and bind it to the exact source disk hash/size.
7. Apply a mutation only to a copied/overlay image, then reopen and compare before/after tables and content.
8. Reject replay of a plan against a different-size/different-layout target.
9. Prove read-only users cannot invoke write/wipe APIs.
10. Pin a stable util-linux/libfdisk build and preserve API compatibility through an adapter.
