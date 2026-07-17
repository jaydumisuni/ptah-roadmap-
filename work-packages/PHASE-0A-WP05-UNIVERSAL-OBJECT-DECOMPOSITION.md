# Phase 0A — WP05 Universal Object and Decomposition Composition

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Runtime code:** NOT STARTED

## Purpose

Close the universal Object registration, detection, progressive decomposition, document, image, media, executable, Android application, source-structure, preview, derivative and rebuild boundaries through one composite donor set.

## Sources inspected and saved

### Internal

- App Recover
- APK Extractor
- TTG Creative Studio
- TTG Document Generator Templates

### External/upstream

- libarchive
- Apache Tika
- Unstructured
- LIEF
- Binwalk v3
- JADX
- Apktool
- libvips
- FFmpeg/ffprobe
- Tree-sitter

Saved records:

- `internal/APP-RECOVER.md`
- `internal/APK-EXTRACTOR.md`
- `internal/CREATIVE-STUDIO.md`
- `internal/DOCUMENT-GENERATOR.md`
- `donors/LIBARCHIVE.md`
- `donors/APACHE-TIKA.md`
- `donors/UNSTRUCTURED.md`
- `donors/LIEF.md`
- `donors/BINWALK.md`
- `donors/JADX.md`
- `donors/APKTOOL.md`
- `donors/LIBVIPS.md`
- `donors/FFMPEG-FFPROBE.md`
- `donors/TREE-SITTER.md`

## Composite result

```text
Ptah Object Graph
  immutable content identity, storage locations and versioned relationships

Detector Claims
  multiple evidence-bearing type claims and selected routing kept separate

Progressive Decomposition
  registration → detection → inventory → decomposition → enrichment
  → transform → rebuild → verification

Archive Pack
  libarchive plus specialist fallbacks

Document Pack
  Tika broad routing/metadata/text
  Unstructured page/layout/OCR elements
  private template/render packs and browser/PDF adapters

Image Pack
  libvips neutral decode/transform/preview
  Creative Studio editable layer/project UX and proof gates

Media Pack
  ffprobe inventory and FFmpeg transform/export

Binary Pack
  LIEF executable/runtime structures
  Binwalk embedded signatures/regions/entropy
  App Recover recovery/output taxonomy

Android Application Pack
  raw package view
  Apktool resources/smali/rebuild project
  JADX Java-like source/graphs/mappings
  LIEF DEX/OAT/VDEX/ART structures
  APK Extractor product orchestration

Source Structure Pack
  Tree-sitter syntax-tree views and later compiler/LSP completion
```

No parser, renderer, decompiler or product is universal Ptah Object truth.

## Accepted architecture

Saved as `decisions/ADR-0007-OBJECT-GRAPH-DECOMPOSITION-DERIVATIVE-BOUNDARY.md`.

Key decisions:

1. Immutable original Object bytes and identity are preserved.
2. Filename, extension, MIME, parser output and user labels are claims/attributes rather than identity.
3. Multiple detector claims and conflicts remain retained; route selection is a separate decision.
4. Unknown, ambiguous, polyglot, encrypted, malformed, truncated, unsupported and opaque are valid states.
5. Decomposition is progressive and can return early shallow results before deeper work finishes.
6. Child Objects, semantic elements, views, previews, transforms, rebuild projects and rebuilt outputs are separate relationships.
7. Source-like outputs explicitly declare original, decoded, disassembled, smali, decompiled, generated-skeleton or human-edited origin.
8. Recursive extraction inherits hard depth, bytes, child count, expansion ratio, time, memory and disk budgets.
9. Path traversal, absolute paths, symlink/hardlink escape and special files are rejected or quarantined.
10. Native parsers run in bounded provider processes/containers rather than the long-lived control plane.
11. Partial valid outputs remain registered after parser error, timeout, crash, cancellation or budget exhaustion.
12. Competing Tika/Unstructured, LIEF/Binwalk, Apktool/JADX and other views remain separately addressable.
13. Rebuild/transform outputs always receive new Object identity and invalidated signature/trust state where applicable.
14. Byte identity, structural equivalence, visual equivalence, functional equivalence and release acceptance remain separate.
15. Products reuse neutral Domain Packs and Objects without becoming Ptah Core.

## Requirement closure verdict

Closed for Phase 0B contract design:

- `CORE-003` Universal Object graph and catalogue
- Domain Pack portions of `CORE-004`
- `DECOMP-001` true-type detection
- `DECOMP-002` recursive archive/container decomposition
- `DOC-001` document structure/render/proof
- `MEDIA-001` video/audio decomposition and transforms
- `IMAGE-001` image decomposition and processing
- `BIN-001` executable/binary decomposition
- `APP-001` APK/AAB/DEX decomposition
- source-structure portions of search/editor requirements

Still dependent on later groups:

- firmware/vendor/disk/filesystem Domain Packs;
- interactive application runtimes;
- browser capture/live web;
- device-connected installed-package extraction;
- search/indexing and retrieval over generated Objects;
- security scanning and dynamic behavior;
- human Workspace UI over the graph.

## Phase 0B contracts required

1. Object identity/type/version schema.
2. Detector claim, evidence, confidence/conflict and route-selection schema.
3. Progressive decomposition level and coverage schema.
4. Relationship vocabulary and locator metadata.
5. Child Object versus structured View contract.
6. Domain Pack manifest and operation-capability contract.
7. Resource/extraction budget and inherited-budget schema.
8. encrypted/malformed/partial/opaque state schema.
9. parser/renderer/model/grammar/build-feature receipt.
10. preview/derivative/transform recipe schema.
11. source-like origin classification.
12. document page/element/table/image and render relationships.
13. image page/frame/band/color/profile/metadata relationships.
14. media container/stream/track/chapter/frame/subtitle relationships.
15. executable section/segment/symbol/import/resource/signature relationships.
16. Android package/set/manifest/component/resource/DEX/native/signing relationships.
17. rebuild/mutation before/after identity and invalidated-trust records.
18. parser isolation, partial-output and cancellation/restart semantics.
19. privacy/redaction/retention rules for recovered content.
20. backend replacement/conformance corpus.

## Validation set

- mixed corpus with all detector claims retained;
- mislabeled, extensionless, polyglot, encrypted, malformed, truncated and unknown inputs;
- bounded recursive archives and attack-path rejection;
- overlapping embedded regions and unknown gaps;
- document elements with source-coordinate overlays;
- image/media metadata and derivative generation under budgets;
- competing executable/Android parser views and coverage reports;
- decompiled/generated source origin enforcement;
- parser crash/cancel/restart with retained partial children;
- several simultaneous decomposition Activities without blocking unrelated work;
- rebuild/transform comparison at byte/structural/visual/functional levels;
- parser backend replacement without identity changes.

## Next Phase 0A group

Proceed with the **firmware, disks and filesystems cluster**:

- internal Apple firmware/tool work;
- blacktop/ipsw and Apple metadata sources;
- internal MediaTek/META and MTKClient;
- internal Qualcomm/DIAG/Firehose and EDL donors;
- internal Unisoc/SPD and PAC/FDL donors;
- internal Android OTA Manager;
- payload/dynamic-partition/sparse image tools;
- GPT/MBR and filesystem parsers;
- libguestfs and related mounting/extraction machinery;
- Binwalk/LIEF/libarchive reuse from WP05;
- other vendor/embedded firmware coverage and P5C recovery status.

This group must close disk/partition/image/filesystem Objects, vendor firmware package relationships, safe static decomposition, optional mounted views, compare/rebuild paths and device-flashing separation before device runtime work begins.
