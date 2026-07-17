# Donor Record — LIEF

**Phase:** 0A / WP05  
**Status:** FIRST-PASS COMPLETE — EXECUTABLE STRUCTURE FOUNDATION CANDIDATE  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/lief-project/LIEF
- Default branch: `main`
- Pinned commit: `a01d9d8d0e8427f3cbc24cc6f1a28571a248e623`
- Licence: Apache-2.0
- Activity: Active
- Classification: Cross-platform executable/object-format parser, abstraction and controlled modification donor
- Ptah targets: PE, ELF, Mach-O, COFF, DEX/OAT/VDEX/ART structure, sections, symbols, imports/exports, signatures, resources, debug metadata and static executable views

## Files/components inspected

- `README.md`
- documented C++, Python, Rust and C API boundaries
- format families, extended DWARF/PDB/Objective-C/Dyld Shared Cache/disassembler/assembler features
- parsing, modification and abstraction model

## Verified capabilities and patterns

- Parses ELF, PE, Mach-O, COFF, OAT, DEX, VDEX and ART formats.
- Provides a common abstraction for sections, symbols and entry points while preserving format-specific APIs.
- Supports modification of selected binary structures, such as sections and symbols.
- Exposes C++, Python, Rust and C APIs.
- Extended functionality includes DWARF/PDB debug information, Objective-C metadata, Dyld Shared Cache/Dylib extraction and disassembly for several architectures.
- Provides PE resource and Authenticode-related functionality/tutorial paths.
- Supports Android runtime/package-related binary formats beyond ordinary native executables.
- Can operate as an embedded library rather than only a CLI tool.
- Stable release packages and nightly builds are separated.

## What LIEF completes

- A mature normalized executable inventory far beyond App Recover's basic `pefile` view.
- Cross-platform PE/ELF/Mach-O common concepts with specialist format detail.
- Static executable children and views: sections, segments, symbols, imports, exports, resources, signatures, debug information, architectures and embedded binaries.
- Android DEX/OAT/VDEX/ART structure useful to the APK/Android Domain Pack.
- A path for safe static comparison and selected rebuild/patch workflows.
- Native Rust bindings aligned with Ptah's preferred long-running core language.

## Important limitations for Ptah

- LIEF is a parser/modifier, not Ptah's universal Object graph, Activity runtime or malware verdict.
- Parser results can be partial or ambiguous for malformed, packed, obfuscated or adversarial binaries.
- A successfully parsed executable is not safe to execute.
- Modification APIs can invalidate signatures, checksums, loader assumptions or platform policy.
- Rebuilding a parsed binary may not be byte-identical and can alter layout/metadata.
- Disassembly is not full semantic decompilation or source recovery.
- Debug paths/symbols/resources may contain sensitive build-system/user data.
- Fat/universal binaries and embedded slices require explicit parent/child relationships.
- Signature parsing does not automatically establish trust or policy acceptance.
- Some extended/runtime features may vary by platform/build/package and require capability discovery.
- Nightly/main-branch APIs can change; Phase 0C must pin a stable release/build.
- Native parsing remains hostile-input attack surface and should run in a bounded provider.
- Exact parser coverage/warnings and unparsed byte ranges need retention.

## Must not be inherited

- Parser success interpreted as safe execution or benign status.
- LIEF object IDs/addresses used as canonical Ptah Object identity.
- Binary modification enabled by default during decomposition.
- Decompiled/disassembled output labeled as original source.
- Signature presence treated as trusted signer acceptance without independent verification.
- Debug paths/symbols exposed publicly without privacy review.
- Parsed/rebuilt binary allowed to overwrite the immutable original.
- Main/nightly API embedded directly in public Ptah schemas.
- Native parser loaded into the long-lived control plane with broad access.

## Integration decision

**ADOPT AS THE PRIMARY STRUCTURED EXECUTABLE/BINARY DOMAIN PACK PARSER CANDIDATE.**

Ptah should run LIEF in static/read-only mode by default and map format structures into typed child Objects/views. Modification/rebuild becomes a separate caller-requested Activity with snapshots, receipts and post-build verification.

Binwalk, platform signature tools, debug parsers and specialist decompilers complete LIEF where embedded content, packing or source-like views are required.

## Native Ptah gap

Ptah must define:

- executable detector/format/slice claim schema;
- parent binary, architecture slice, section/segment, import/export, resource, symbol/debug and signature relationships;
- virtual/file offsets, sizes and content hashes;
- parser warnings, coverage and unparsed ranges;
- static-only default and execution isolation policy;
- privacy classification for debug paths/resources;
- signature/certificate relationship to ADR-0005 verification records;
- disassembly/decompilation view identity;
- mutation plan, before/after Object versions, invalidated signature state and rollback;
- exact LIEF build/features/version receipt;
- stable-release selection and compatibility adapter;
- parser crash/timeout/resource limits.

## Exit strategy

Ptah's Binary Domain Pack can use LIEF, platform-native parsers, goblin/object libraries, LLVM tooling or specialist services. Parsed child Objects and views remain backend-neutral.

## Validation required

1. Parse representative PE, ELF, Mach-O/fat, COFF and Android DEX/OAT/VDEX/ART samples.
2. Register architecture slices, sections, imports/exports, resources and signatures as typed children/views with exact offsets/hashes.
3. Feed malformed, truncated, packed, obfuscated and polyglot binaries and retain partial coverage/warnings.
4. Compare LIEF claims with platform-native tools and Binwalk; preserve disagreements.
5. Verify Authenticode/code-signing evidence independently from parser presence.
6. Run native parsing in a bounded provider and survive crashes/timeouts.
7. Modify a copy under an explicit Activity, preserve the original, record invalidated signatures and compare output semantics/bytes.
8. Remove sensitive debug paths from public derivatives while retaining controlled evidence.
9. Pin a stable release and prove schema compatibility across an upgrade.
10. Demonstrate that static decomposition never executes the input binary.
