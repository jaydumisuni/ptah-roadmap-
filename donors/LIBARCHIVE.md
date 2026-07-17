# Donor Record — libarchive

**Phase:** 0A / WP05  
**Status:** FIRST-PASS COMPLETE — ARCHIVE STREAM/ENTRY FOUNDATION CANDIDATE  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/libarchive/libarchive
- Default branch: `master`
- Pinned commit: `0362c77f9f7317274bb784816fe208fd49f01aad`
- Licence: permissive BSD-style two-clause terms for the main library, with file-specific exceptions/public-domain/triple-licensed components documented in `COPYING`; individual bundled/build-file licences still require packaging review.
- Activity: Active and mature
- Classification: Streaming archive/container reader-writer and entry metadata foundation
- Ptah targets: broad archive detection, streaming entry inventory/extraction, compression filters, large-input processing and archive creation

## Files/components inspected

- `README.md`
- `COPYING`
- documented `archive_read`, `archive_write`, `archive_entry`, `archive_write_disk` and format/filter model
- thread-safety and streaming-design notes

## Verified capabilities and patterns

- Portable C library for streaming archive read/write plus bsdtar, bsdcpio, bsdcat and bsdunzip utilities.
- Automatically detects archive format and compression/filter layers on read.
- Reads many tar/cpio variants, ISO9660, ZIP/ZIPX, ar, mtree, 7-Zip, CAB, LHA/LZH, RAR/RAR5 with limitations, WARC and XAR.
- Detects wrapper/compression layers including RPM, gzip, bzip2, LZW, LZMA/lzip/xz, lz4, lzop and zstd.
- Creates several tar/cpio/ZIP/7-Zip/ISO/WARC/XAR formats and compression filters.
- One streaming API handles many formats and can process inputs too large to materialize in memory/disk by reading sequentially.
- Callback-oriented I/O permits memory, file, socket or other byte sources/sinks.
- Individual archive entries are represented independently through `archive_entry` metadata.
- Multiple independent archive stream objects can be open concurrently.
- Features/formats can be selectively linked to reduce static dependency footprint.
- The library is generally thread-safe when separate archive objects are used, subject to platform/runtime caveats.

## What libarchive completes

- A mature common API for archive format/filter detection and entry streaming.
- Broad coverage beyond Python `zipfile` and product-specific 7-Zip subprocess paths.
- Large-input single-pass operation.
- Per-entry metadata and data callbacks suitable for direct Object creation without first writing every child to a temporary extraction tree.
- Archive creation/repack support for future compare/rebuild workflows.
- A smaller neutral archive foundation that can be embedded in a Rust/C-compatible Facility through FFI or wrapped by a process/service.

## Important limitations for Ptah

- libarchive is a parser/stream library, not a recursive Ptah Object graph or Activity runtime.
- It does not impose recursion depth, child count, expanded-byte, compression-ratio, time, memory or disk budgets; the caller must enforce them.
- It does not make archive entry paths safe automatically for every extraction strategy. Disk-writing options and explicit containment/policy remain caller responsibilities.
- Symlinks, hard links, special/device files, permissions, ACLs, sparse files and platform-specific metadata need explicit policy.
- Encrypted archives require credential/password handling and may expose only partial inventory until unlocked.
- RAR support has proprietary-format limitations.
- The streaming model does not provide true random access or in-place modification.
- `archive_write_disk_header()` is not thread-safe on POSIX because of process-wide `umask` behavior; caller serialization or avoiding the convenience path is required.
- Directory-tree traversal helpers can use `chdir()` and conflict with multi-threaded process assumptions.
- The library performs no locking/thread management for shared archive objects.
- Automatic format detection returns a parser decision, not calibrated confidence or detector consensus.
- Parsing hostile archives remains native-code attack surface and should be isolated/updated/fuzzed.
- File-specific licensing/build dependencies require release review.

## Must not be inherited

- Archive entry path used directly as host output path.
- Unlimited recursive extraction.
- Symlink/hardlink/device/permission restoration enabled by default.
- Parser success treated as complete or trusted content classification.
- One extraction directory treated as canonical child identity.
- Shared archive handles accessed concurrently without synchronization.
- `archive_write_disk` convenience behavior used without thread/security review.
- Native parser run inside the long-lived control plane with broad host access.
- Archive format limitations hidden from caller/evidence.

## Integration decision

**ADOPT AS THE PRIMARY LOW-LEVEL ARCHIVE STREAM/ENTRY FOUNDATION CANDIDATE, BEHIND A BOUNDED PTAH ARCHIVE DOMAIN PACK.**

Ptah should use libarchive to inventory and stream supported archive entries directly into landing/content-addressed Objects where possible. Specialist tools remain completion paths for formats/features libarchive cannot decode completely.

The Domain Pack—not libarchive—owns recursion, budgets, path/link policy, child identity, receipts, encrypted/unsupported states and rebuild verification.

## Native Ptah gap

Ptah must define:

- archive detector claim and exact format/filter chain;
- entry Object schema: logical path, normalized path, type, size, mode, timestamps, links, sparse metadata, source offset/index where available;
- safe path policy and collision/case-normalization behavior;
- recursion/expanded-byte/child-count/compression-ratio/time/memory budgets;
- per-entry streaming hash and content-addressed deduplication;
- symlink/hardlink/special-file policy;
- encrypted archive/password credential reference;
- partial/unsupported/corrupt/truncated states;
- parser process/container isolation and resource accounting;
- exact libarchive build/version/features receipt;
- archive reconstruction and semantic/byte comparison levels;
- fallback adapters for unsupported/proprietary formats.

## Exit strategy

Ptah's Archive Domain Pack remains implementable through libarchive, 7-Zip, language-native parsers or format-specific libraries. Child Object/relationship schemas never expose libarchive structures as canonical truth.

## Validation required

1. Inventory/extract representative ZIP/ZIPX, tar variants, 7z, CAB, ISO, cpio, RAR and compressed wrappers.
2. Stream a very large archive into hashed child Objects without whole-file memory loading.
3. Reject traversal, absolute paths, drive prefixes, symlink/hardlink escapes and special/device files according to policy.
4. Stop decompression bombs at child-count, ratio, bytes, time and disk limits while preserving partial evidence.
5. Handle encrypted, malformed, truncated and unsupported archives honestly.
6. Recursively decompose nested archives with stable parent/contains relationships and deduplication.
7. Run several archive Activities concurrently without unsafe shared handles or `umask/chdir` interference.
8. Rebuild a supported archive and classify semantic equivalence separately from byte identity.
9. Crash/restart during extraction and resume without duplicating verified child Objects.
10. Run a hostile corpus in a bounded provider and record crashes/timeouts as evidence rather than control-plane failure.
