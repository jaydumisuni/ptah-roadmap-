# Donor Record — Binwalk v3

**Phase:** 0A / WP05  
**Status:** FIRST-PASS COMPLETE — EMBEDDED SIGNATURE/ENTROPY DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/ReFirmLabs/binwalk
- Default branch: `master`
- Pinned commit: `704286902ee66922a028551048cc4a1009f46e6a`
- Package version: `3.1.1`
- Licence: MIT
- Activity: Active Rust rewrite
- Classification: Embedded file-signature scanner, extractor/carver, entropy and firmware-analysis donor
- Ptah targets: embedded content maps, offsets, signature confidence, extraction/carving, unknown regions, recursion and compression/encryption clues

## Files/components inspected

- `README.md`
- `Cargo.toml`
- `src/lib.rs`
- `src/binwalk.rs`
- `src/main.rs`
- documented Rust-library integration, signatures, extractors, JSON logging, entropy and recursive `matryoshka` behavior

## Verified capabilities and patterns

- Rust implementation identifies and optionally extracts files/data embedded inside other files.
- Focuses on firmware but supports a broad signature set.
- Entropy analysis can reveal regions likely to contain compressed or encrypted/high-entropy data.
- Can be integrated as a Rust library.
- `AnalysisResults` separates source file path, signature/file map and extraction results keyed to signature-result IDs.
- Signatures contain parsers/validators rather than accepting raw magic matches alone.
- Short signatures can be restricted to offset zero to reduce false positives.
- Aho-Corasick scans many magic patterns efficiently across the input.
- Signature results include offsets, sizes, descriptions and confidence used to advance scanning.
- Include/exclude filters and user-defined signatures are supported.
- Signature-to-extractor lookup is explicit.
- CLI supports JSON logging, entropy mode, extraction, raw carving, recursive analysis and configurable worker threads.
- Recursive extraction uses a separate pending-file queue to avoid placing an enormous backlog directly in the thread-pool queue.
- Extracted child files can be requeued for recursive analysis unless the extractor marks them `do_not_recurse`.
- Carving can preserve recognized and unknown byte regions separately.
- Worker panics cause the process to exit rather than silently continuing with corrupted state.

## What Binwalk completes

- Offset-based embedded content mapping across opaque binaries/firmware.
- Validated magic signatures with confidence and extractor relationships.
- Entropy views and unknown-region evidence.
- Recursive embedded extraction and carving.
- Rust-library integration suitable for a bounded Ptah Facility.
- A strong completion donor for LIEF and libarchive when content is embedded without an ordinary archive directory.
- Early firmware-decomposition foundations before vendor-specific packs.

## Important limitations for Ptah

- The inspected library examples and CLI read full input files into memory before scanning; very large firmware requires Ptah-level memory/input strategy or future streaming/chunk support.
- Recursive `matryoshka` processing does not by itself impose Ptah's maximum depth, total descendants, expanded bytes, time, memory or disk budgets.
- Signature confidence is tool-specific, not calibrated universal certainty.
- Magic/validator hits can overlap, conflict or miss obfuscated/custom content.
- High entropy suggests compression/encryption/randomness but does not prove which one.
- Extractors vary in maturity and may invoke/contain format-specific code with separate risks/dependencies.
- Carved unknown ranges are byte slices, not semantically identified Objects.
- Extraction directories and symlinks are implementation conveniences, not canonical Object relationships.
- The CLI creates a symlink to the target inside extraction output and requires path/security review in multi-tenant environments.
- Recursive extraction can repeatedly rediscover duplicate children without Ptah content-addressed deduplication.
- Worker panic exits the whole Binwalk process, which is good isolation behavior only when the process is separate from Ptah Core.
- Entropy graph generation and optional Plotly/Kaleido dependencies may download/use extra tooling and are not required for every Node.
- A Git dependency (`delink`) appears in the inspected Cargo manifest and needs pin/SBOM/licence review before reproducible packaging.
- Detection/extraction does not establish firmware correctness, safety or rebuildability.

## Must not be inherited

- Unlimited recursive `matryoshka` extraction.
- Whole-file memory loading for arbitrary-size Objects.
- Entropy interpreted as proof of encryption or maliciousness.
- Signature match treated as unquestionable file identity.
- Extracted paths/symlinks used as public Ptah identity.
- Binwalk process hosted inside the long-lived control plane.
- Carved unknown bytes discarded because they lack a known signature.
- Extractor success promoted to complete firmware decomposition.
- Unpinned Git dependencies in reproducible release builds.
- Input firmware executed or mounted merely because a signature was found.

## Integration decision

**ADOPT AS THE PRIMARY EMBEDDED-SIGNATURE/ENTROPY COMPLETION CANDIDATE, BEHIND PTAH OBJECT/BUDGET CONTRACTS.**

LIEF handles structured executable internals; libarchive handles ordinary archives; Binwalk maps embedded and unknown regions. Ptah combines their claims and registers each recognized or carved region as a child/view with source offset, length, detector receipt and content hash.

Recursive extraction is orchestrated by Ptah Activities so budgets, deduplication, cancellation, restart and provenance remain backend-neutral.

## Native Ptah gap

Ptah must define:

- embedded-region relationship with source offset/length and overlap support;
- detector/signature/parser/version/confidence evidence;
- recognized, unknown, padding, encrypted/compressed-suspected and gap region types;
- recursion depth/child/expanded-byte/time/memory/disk budgets;
- whole-file versus streaming/windowed scan capability;
- content-addressed deduplication and cycle/repeat prevention;
- extractor process isolation and dependency manifest;
- entropy derivative schema and interpretation limitations;
- cancellation/checkpoint/restart behavior;
- source symlink/path containment policy;
- JSON/receipt mapping independent of Binwalk IDs;
- stable release and reproducible dependency pinning;
- links to vendor-specific firmware Domain Packs.

## Exit strategy

Ptah's embedded-content detector contract remains implementable through Binwalk, custom signature scanners, YARA-like rules, format-specific parsers or carving libraries. Region/child Object identity does not depend on Binwalk.

## Validation required

1. Detect and map representative embedded filesystems, compressed streams, executables, images and configuration blocks in firmware/binary corpora.
2. Retain exact offsets, lengths, confidence, signature/parser version and overlapping/conflicting hits.
3. Carve unknown gaps as content-addressed children rather than discard them.
4. Enforce recursion depth, total descendants, expanded bytes, time, memory and disk limits.
5. Scan a very large Object without unbounded memory growth through a Ptah adapter strategy.
6. Compare Binwalk hits against LIEF/libarchive/vendor parsers and preserve disagreement.
7. Generate entropy views and label them as clues, not encryption verdicts.
8. Crash/panic an extractor process and preserve completed children while Ptah Core continues.
9. Deduplicate repeated embedded content and prevent recursive cycles/reprocessing.
10. Reproduce the exact Binwalk build with pinned dependencies and retained SBOM/licence evidence.
