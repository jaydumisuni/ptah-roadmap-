# Donor Record — Android OTA Payload, Sparse Image, Dynamic Partition and AVB Foundations

**Phase:** 0A / WP06  
**Status:** FIRST-PASS COMPLETE — PRIMARY ANDROID IMAGE/OTA FORMAT FOUNDATIONS  
**Inspected:** 2026-07-17

## Sources inspected

### AOSP Update Engine metadata

- Canonical source: `platform/system/update_engine/update_metadata.proto`
- Licence: Apache-2.0
- Inspected exact source commit: `e8acc072264fed67dc5e01886983d16924b53b52`
- Current-main file blob additionally inspected: `6d16da40e53720078b2e4f3689dbb296eb325bee`
- Classification: authoritative OTA payload manifest and operation schema.

### AOSP libsparse

- Canonical source: `platform/system/core/libsparse`
- Licence: Apache-2.0
- Inspected exact source commits/blobs include:
  - `f0dd09c8898a94d58bf4ad950202e6cc21f1604c`
  - current inspected `sparse_format.h` source at `605f8706c88b2cd5d024b0a6b7253a78d968ba72`
- Classification: authoritative Android sparse image encoding/decoding foundation.

### AOSP liblp / dynamic partitions

- Canonical source: `platform/system/core/fs_mgr/liblp`
- Licence: Apache-2.0
- Inspected current-main `metadata_format.h` blob: `8d77097ed67b047603d4571e514730ca98b63cf8`
- Inspected current-main `liblp.h` blob: `04f8987fde7f5ae81e0271423a5fd8f98906d97c`
- Classification: authoritative `super`/logical-partition metadata schema.
- Phase 0C must pin an exact Android platform release/tag/commit rather than a moving main ref.

### Android Verified Boot / libavb

- Canonical source: `platform/external/avb`
- Licence: permissive/MIT-style terms in inspected libavb source files.
- Inspected exact source commit: `18666abc5d8276a743111e6c3608e66f6c85fb51`
- Classification: authoritative vbmeta/signature/descriptor/rollback verification foundation.

### payload-dumper-go

- Canonical URL: https://github.com/ssut/payload-dumper-go
- Pinned commit: `a51234eaead276ff3d8b8c4c439c51c7f46a96a8`
- Licence: Apache-2.0
- Classification: practical parallel full-payload partition-image extractor.

## Files/components inspected

- AOSP `update_metadata.proto`
- AOSP `libsparse/sparse_format.h`
- AOSP `libsparse/include/sparse/sparse.h`
- AOSP `fs_mgr/liblp/include/liblp/metadata_format.h`
- AOSP `fs_mgr/liblp/include/liblp/liblp.h`
- AOSP `libavb/avb_vbmeta_image.h`
- AOSP AVB architecture/tool documentation
- `payload-dumper-go/README.md`
- `payload-dumper-go/payload.go`

## Verified OTA payload model

- Payload magic is `CrAU` followed by major version, manifest length and metadata-signature length.
- The manifest is an ordered protobuf `DeltaArchiveManifest`.
- Payloads may be full or delta; minor version zero represents full payload while other versions can require a specific source build/content.
- Major v2 represents updated partitions by name and supports more than two partitions.
- Manifest metadata includes maximum OS timestamp, dynamic-partition metadata, partial-update state, APEX information and security patch level.
- Each partition carries source/new partition information, hashes/sizes and ordered install operations.
- Operations include REPLACE, compressed replace variants, SOURCE_COPY, SOURCE_BSDIFF, ZERO, DISCARD, PUFFDIFF, ZUCCHINI, LZ4DIFF and other version-dependent forms.
- Source and destination extents are explicit block ranges.
- Data-blob and source-extent SHA-256 hashes can be present and must be verified where specified.
- Metadata and whole-payload signatures are distinct structures.
- Dynamic/Virtual A/B metadata and merge-operation hints can be embedded.
- Update generation is separate from application; AOSP recommends higher-level wrapper tools rather than invoking `delta_generator` directly.

## Verified payload-dumper-go behavior

- Parses version-2 `CrAU` headers, manifest and metadata signatures.
- Lists named target partitions and output sizes.
- Reconstructs full partition images in parallel.
- Handles REPLACE, REPLACE_XZ, REPLACE_BZ, ZSTD and ZERO operations.
- Writes operations at destination extents and checks expected expanded byte counts.
- Verifies per-operation payload data SHA-256 where present.
- Supports OTA ZIP input containing `payload.bin`.
- Explicitly does **not** support incremental/delta payloads at the inspected pin.
- Worker error handling is weak: extraction errors can be printed inside workers without being propagated through the overall `ExtractSelected` return path; output files may therefore exist despite partial failure.
- Output files are created/truncated directly and are not atomically promoted after whole-partition verification.
- It relies on external/native xz code for performance.

## Verified Android sparse image model

- Sparse images carry a header with magic/version/header sizes, block size, total expanded blocks/chunks and image checksum fields.
- Chunk types represent raw data, repeated fill values, skipped/don't-care ranges and CRC records.
- libsparse can import sparse or raw images, expand sparse images, create sparse images, split/resparse images and verify CRC when requested.
- Expanded logical length is distinct from sparse file byte size.
- Sparse encoding is a transport/storage representation, not a partition/filesystem identity.

## Verified dynamic partition / `super` model

- `super` metadata has geometry, primary/backup metadata copies and logical-partition tables.
- Geometry includes magic, struct size, SHA-256 checksum, metadata maximum size, metadata slot count and logical block size.
- Metadata headers are versioned and contain independent SHA-256 checksums for header and tables.
- Logical partitions have names, attributes, group membership and ordered extents.
- Extents can map to physical block-device sectors or zero targets.
- Partition groups have maximum-size constraints.
- Block-device entries retain size, alignment, alignment offset, first logical sector, partition name and flags.
- A/B/Virtual A/B, slot-suffixed and updated/disabled/read-only attributes are explicit.
- Dynamic partitions can be created/resized/destroyed during OTA operations within the available `super` space.

## Verified AVB model

- `vbmeta` uses magic `AVB0` and contains a fixed header, authentication block and auxiliary block.
- It records required libavb version, algorithm, hash/signature ranges, public-key data, descriptors, rollback index, flags and release string.
- Verification-disabled and hashtree-disabled flags are explicit and security-significant.
- libavb verification distinguishes valid, unsigned, invalid-header, unsupported-version, hash-mismatch and signature-mismatch states.
- A valid cryptographic signature is insufficient until the embedded public key is matched to a known trusted key.
- Rollback indexes must be compared against trusted device/platform state.
- Whole-slot/partition verification and chained/delegated partition descriptors are broader than checking one vbmeta header.

## What this donor set completes

- Authoritative Android OTA operation/extent/hash relationships.
- Full versus delta/source-dependent payload distinction.
- Sparse-versus-expanded image identity and conversion.
- `super` physical-device, logical-partition, group and extent relationships.
- AVB/vbmeta verification, key and rollback evidence.
- A practical fast full-payload extraction backend.
- A package-analysis path independent of connected devices or update-service controls.

## Important limitations for Ptah

- Parsing/extracting a payload is not applying an OTA.
- A full payload can reconstruct target images independently; a delta payload requires exact source partition bytes/hashes and operation support.
- `payload-dumper-go` does not support incremental payloads and cannot be the universal extractor.
- Per-operation data hashes do not automatically verify the complete reconstructed partition unless the final partition hash is checked.
- Metadata signatures are parsed by the practical dumper but not necessarily verified against an authorized key.
- Partial worker failures can leave files and still permit the top-level extraction path to appear complete.
- ZERO operation allocation can be memory-expensive in the inspected implementation.
- Sparse expanded size can be much larger than input size and requires explicit output budgets.
- Don't-care regions have semantics that must not be confused with verified zero bytes unless the conversion path defines them.
- Dynamic partition metadata has multiple primary/backup copies and slots; one parsed copy may be stale/corrupt.
- Logical extents are not filesystem files and may span several physical block devices.
- Rebuilding `super` or applying dynamic-partition changes is a mutation activity, not ordinary decomposition.
- AVB verification requires known trust roots and rollback state; self-consistent signatures alone do not prove authorization.
- Verification/hashtree-disabled flags must never be hidden.
- `vbmeta` patching invalidates or intentionally disables trust and belongs in a separate explicit mutation operation.
- Moving-main AOSP source must be replaced by exact platform release pins in Phase 0C.
- OEM/vendor payload operation variants, encryption and package wrappers may require completion adapters.

## Must not be inherited

- payload extraction described as OTA application.
- full-payload-only tool used silently on delta payloads.
- worker-printed errors treated as successful partition extraction.
- partially written partition files registered as verified Objects.
- sparse file size used as expanded partition size.
- don't-care chunks treated as trusted original zero data without explicit semantics.
- one `super` metadata copy trusted without checksum/version/backup comparison.
- logical partition name used as sufficient device compatibility.
- vbmeta signature accepted without known-key and rollback-policy verification.
- verification-disabled/hashtree-disabled flags omitted from receipts.
- rebuilt/patched vbmeta or partition images retaining original trust/Object identity.
- OTA apply, fastboot flash or device update-service control exposed through static package analysis.

## Integration decision

**ADOPT AOSP FORMAT/VERIFICATION SPECIFICATIONS; WRAP PAYLOAD-DUMPER-GO ONLY AS A FULL-PAYLOAD COMPLETION BACKEND; BUILD NATIVE PTAH IMAGE RELATIONSHIPS.**

Ptah should expose separate capabilities:

- payload header/manifest/signature inventory;
- full/delta/source compatibility determination;
- operation graph and extent/hash inventory;
- full-payload extraction;
- delta reconstruction with a more complete AOSP-compatible backend;
- sparse/raw conversion;
- dynamic `super` inventory/extraction/rebuild;
- AVB/vbmeta inventory and authorized verification;
- separately gated apply/flash/update operations.

## Native Ptah gap

Ptah must define:

- OTA package/payload/manifest/signature Object schema;
- source/target build, timestamp, patch level and partial/full/delta compatibility;
- partition source/new hashes, sizes and operation/extents graph;
- operation algorithm/capability and unsupported-operation states;
- whole-partition reconstruction hash and atomic finalization;
- sparse header/chunk/expanded-image relationships;
- super geometry/metadata-slot/copy/partition/group/block-device/extent relationships;
- dynamic-partition source/target metadata comparison;
- vbmeta/descriptors/public-key/rollback/trust-root/verification-state schema;
- exact AOSP platform release/tool build receipt;
- bounded CPU/memory/disk/concurrency/cancellation/restart behavior;
- partial-output cleanup/recovery and worker error propagation;
- package analysis versus device apply/flash separation;
- device/build/profile compatibility and read-before-write backup.

## Exit strategy

Ptah's Android OTA/Image contracts remain backend-neutral. AOSP update_engine/delta_generator libraries, payload-dumper-go, payload-dumper-rust, liblp/libsparse/avbtool or OEM adapters can replace one another without changing Package, Manifest, Operation, Partition Image or Verification identities.

## Validation required

1. Parse representative full, delta, partial and Virtual A/B payloads and retain exact source/target requirements.
2. Reconstruct full-payload partitions with operation and final partition hash verification.
3. Reject delta extraction without exact source partition Objects and support the required operation algorithms through a complete backend.
4. Crash/fail one worker and preserve partial output as unverified rather than completed.
5. Convert sparse→raw→sparse while retaining expanded size, chunk semantics and checksum evidence.
6. Reject decompression/output expansion beyond configured disk/byte budgets.
7. Parse all primary/backup `super` metadata copies, validate checksums/version and surface disagreement.
8. Extract logical partitions by mapping ordered extents across physical block devices.
9. Verify vbmeta cryptographically, match an authorized key and check rollback policy separately.
10. Preserve verification-disabled/hashtree-disabled states and new identity after any patch/rebuild.
11. Prove all package/image analysis works without connected devices.
12. Apply/flash only through a separately authorized Device Activity after exact build/layout compatibility and immutable backups.
