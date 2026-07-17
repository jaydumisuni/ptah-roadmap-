# ADR-0007 — Object Graph, Decomposition, Views and Derivatives Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Phase:** 0A universal Object/decomposition closure

## Context

Ptah must accept arbitrary files and content while preserving the original, identifying what it may be, decomposing it progressively and exposing useful views without falsely claiming perfect understanding.

The inspected sources solve different parts:

- App Recover combines evidence-based application/installer detection, extraction, resources, strings, dependencies and rebuild blueprints.
- APK Extractor combines raw ZIP, Apktool and JADX views.
- Creative Studio provides editable image/motion projects, source Assets, rendered derivatives and visual proof gates.
- Document Generator creates structured HTML/PDF derivatives while preserving external truth boundaries.
- libarchive streams archive entries across many formats.
- Apache Tika orchestrates broad magic/container/text detection plus metadata/text extraction.
- Unstructured produces page/layout/document elements and OCR-aware views.
- LIEF parses structured executable and Android runtime formats.
- Binwalk maps embedded signatures, offsets, entropy and carved regions.
- JADX creates approximate Java-like source and graph views.
- Apktool creates decoded resource/smali/rebuild-oriented package views.
- libvips provides efficient image decoding/transforms/previews.
- FFmpeg/ffprobe provides media container/stream/frame/track structure and transforms.
- Tree-sitter creates incremental concrete syntax-tree views for source files.

No parser or product can define universal Object truth by itself.

## Decision

Ptah owns a versioned **Object Graph** and a versioned **Domain Pack contract**.

The immutable original Object remains preserved. Detection, metadata, decomposition, views, transforms, rebuilds and verification create linked records and new Objects rather than mutating the original silently.

The following concepts remain separate:

1. Object identity and bytes;
2. detector claims;
3. selected routing/classification;
4. inventory/metadata;
5. extracted child Objects;
6. semantic elements/regions;
7. views;
8. transformed derivatives;
9. rebuild blueprints/projects;
10. rebuilt outputs;
11. previews;
12. review/verification/acceptance.

---

# Object identity

Every immutable Object is identified independently of filename, extension, parser and storage location.

At minimum:

```text
object_id
object_type_version
size
qualified_content_digests
created_at
source_reference
storage_locations
privacy_class
retention_class
```

Filename, extension, MIME type and user labels are attributes or claims, not identity.

The original Object is never replaced by extracted, normalized, decoded, decompiled, rendered or rebuilt content.

---

# Detector claims

Detection is plural and evidence-bearing.

Each detector claim records:

```text
claim_id
object_id
detector_id
detector_version
detector_build_or_feature_set
claimed_type
claimed_subtype
confidence_or_priority
evidence_class
evidence_summary
byte_ranges_or_container_evidence
filename_or_metadata_hints_used
limitations
created_at
```

Evidence classes may include:

```text
extension_hint
filename_hint
metadata_hint
magic_signature
container_structure
parser_validated
embedded_signature
text_encoding
model_classification
caller_assertion
```

## Rules

- Extension-only classification never overrides stronger content evidence silently.
- Competing or conflicting claims are retained.
- A selected route/classification is a separate decision with its own reason and version.
- Confidence values remain detector-specific unless calibrated against a common corpus.
- `unknown`, `ambiguous`, `polyglot`, `encrypted`, `malformed`, `truncated`, `unsupported` and `opaque` are valid outcomes.
- Detection success does not imply safety, executability, completeness or semantic correctness.

## Initial detector composition

- Tika for broad magic/container/text claims and metadata/text routing.
- libarchive for archive/filter validity.
- LIEF for executable/runtime format validation.
- Binwalk for embedded signatures/regions.
- ffprobe for multimedia container/stream claims.
- libvips/image loaders for image claims.
- Android package adapters for APK/AAB/split claims.
- format-specific detectors may outrank generic claims when evidence is stronger.

---

# Progressive decomposition levels

Decomposition is progressive and caller-selectable.

```text
L0 registered
  bytes hashed and stored; filename/source metadata retained

L1 detected
  detector claims and initial route

L2 inventoried
  shallow metadata, entries/streams/sections/pages without deep child processing

L3 decomposed
  child Objects/semantic elements extracted or mapped

L4 enriched
  OCR, source views, call graphs, thumbnails, waveforms, syntax trees and other derived views

L5 transformed
  explicit normalized/edited/transcoded/converted derivatives

L6 rebuilt
  new package/archive/binary/document/media output from a plan/project

L7 verified
  hashes, parser reopening, comparison, review, runtime or authoritative external proof as applicable
```

A higher level is never inferred merely because a lower-level tool exited successfully.

Deep decomposition can be scheduled after immediate registration/detection so intake remains responsive.

---

# Object relationships

Relationship records are versioned and may carry source path, offset, length, page, coordinates, stream index, DEX/class identity or other locator metadata.

Initial relationship vocabulary:

```text
contains
entry_of
embedded_in
carved_from
region_of
page_of
section_of
segment_of
stream_of
track_of
chapter_of
frame_of
attachment_of
resource_of
class_of
method_of
asset_of
layer_of
syntax_tree_of
text_view_of
metadata_view_of
ocr_view_of
decoded_view_of
decompiled_view_of
disassembly_view_of
preview_of
thumbnail_of
contact_sheet_of
waveform_of
transcript_of
normalized_from
converted_from
transcoded_from
remuxed_from
edited_from
rebuild_blueprint_for
rebuild_project_for
rebuilt_from
comparison_of
report_for
```

Relationships do not imply ownership or trust beyond their recorded type/provenance.

## Embedded regions and overlaps

Embedded content may overlap or share bytes. Region relationships retain source offset/length and can coexist without forcing a non-overlapping tree.

Unknown regions are preservable children/views and are not discarded merely because no parser recognizes them.

## Deduplication

Two child paths/regions producing the same content digest may reference one immutable child Object while retaining separate relationship/location records.

---

# Child Object versus View

## Child Object

A child Object has independently addressable bytes, such as:

- archive entry;
- embedded executable;
- image/resource;
- extracted audio track;
- DEX file;
- carved byte region;
- PDF attachment;
- rebuilt package.

## View

A View is a structured interpretation that may not have independent original bytes, such as:

- metadata JSON;
- parsed manifest model;
- syntax tree;
- page/layout elements;
- Java-like source;
- smali/disassembly;
- call graph;
- visual overlay;
- waveform data;
- comparison report.

Views are versioned derivatives with exact parser/configuration provenance and may have serialized Object representations.

---

# Domain Pack contract

A Domain Pack declares:

```text
pack_id
pack_version
supported_claims
required_facilities
optional_facilities
input_requirements
resource_budget_classes
network_requirement
credential_requirements
operations
output_relationships
proof_capabilities
known_limitations
licence_and_dependency_manifest
```

Required operation vocabulary:

```text
detect
inventory
decompose
preview
open_or_mount
transform
compare
rebuild
validate
execute_or_run   # only for packs that explicitly support a runtime
```

Not every pack supports every operation. Unsupported operations are explicit capabilities, not hidden failures.

## Initial Domain Packs

- Archive/Container Pack — libarchive plus specialist fallbacks.
- Document Pack — Tika, Unstructured and format/render adapters.
- Image Pack — libvips plus specialist loaders.
- Media Pack — ffprobe/FFmpeg.
- Binary/Executable Pack — LIEF plus Binwalk/platform tools.
- Android Application Pack — raw container, Apktool, JADX, LIEF and signing/bundle tools.
- Source Structure Pack — Tree-sitter grammars and later language-specific tools.
- Firmware/Disk packs follow in the next work package using the same contract.

---

# Resource and extraction budgets

Every decomposition Activity receives explicit budget classes and hard limits.

Potential limits include:

```text
max_input_bytes
max_runtime
max_cpu
max_memory
max_temporary_disk
max_output_bytes
max_child_objects
max_recursion_depth
max_expansion_ratio
max_archive_path_length
max_pages
max_pixels
max_frames
max_packets
max_audio_duration
max_ocr_pages
max_text_bytes
max_syntax_nodes
max_model_memory
```

## Rules

- Limit reached produces `budget_exhausted` with retained partial evidence.
- Partial valid outputs remain registered.
- Child Activities inherit reduced remaining budgets rather than resetting limits.
- Recursive cycles/repeated content are prevented by content identity and ancestor tracking.
- Huge outputs are streamed/paginated into Objects rather than retained in memory/event payloads.
- A parser must not silently expand arbitrary content outside the selected Workspace/storage root.

---

# Extraction safety

Archive/package/container extraction must enforce:

- normalized relative paths;
- rejection/quarantine of absolute paths, drive prefixes and traversal;
- explicit symlink/hardlink policy;
- rejection/quarantine of device/special files;
- case/collision normalization records;
- no restoration of dangerous ownership/permissions by default;
- atomic child Object finalization after hashing;
- temporary/partial cleanup receipts;
- no executable launch during static decomposition.

Native parsers and hostile formats run in bounded provider processes/containers, not the long-lived control plane.

---

# Encrypted, malformed and partial content

Ptah records structured states:

```text
complete
partial
locked_encrypted
credential_required
wrong_credential
unsupported_encryption
malformed
truncated
parser_error
parser_crash
timeout
budget_exhausted
unsupported_format
opaque
```

Credential references are opaque and scoped to the selected Activity/Facility. Raw passwords never enter Objects, logs, telemetry or receipts.

Partial metadata/children remain usable with explicit coverage and missing sections.

---

# Multi-view and consensus

Several tools may interpret the same Object:

- Tika text versus Unstructured elements/OCR;
- LIEF sections versus Binwalk embedded regions;
- raw APK versus Apktool resources/smali versus JADX source;
- libvips metadata versus Tika image metadata;
- ffprobe stream claims versus container-specific parsers;
- Tree-sitter syntax versus compiler/language-server diagnostics.

Ptah retains each view and its provenance. A comparison/consensus Activity may identify agreement/disagreement, but it does not erase competing views.

---

# Source-like output origin

Every source-like Object/View declares origin:

```text
original_source
recovered_embedded_source
decoded_resource
disassembly_view
smali_view
decompiled_view
generated_rebuild_skeleton
generated_project
human_edited_derivative
```

JADX output and App Recover-generated skeletons can never be labeled `original_source` without independent source evidence.

---

# Preview and rendering boundary

Previews are derivatives:

- image thumbnail/normalized preview;
- document page image;
- video frame/contact sheet/GIF;
- audio waveform/sample;
- syntax-highlighted source view;
- executable/firmware map.

Every preview records source Object, renderer/decoder version, recipe/settings, output dimensions/duration/range, color/font/codec environment and content hash.

A preview proves renderability under one backend; it does not replace the original or prove complete semantic correctness.

---

# Transform and rebuild boundary

Transforms/rebuilds are explicit Activities with recipes, before/after Objects and receipts.

Examples:

- image resize/color conversion;
- media remux/transcode;
- document render;
- archive repack;
- APK rebuild/sign;
- binary patch;
- generated rebuild project.

## Rules

- Original Object remains immutable.
- Rebuilt output receives a new Object identity.
- Invalidated signature/trust state is recorded.
- Byte-identical, structurally equivalent, visually equivalent, functionally equivalent and merely parseable are different comparison levels.
- Rebuild success does not imply installability/runtime correctness/release acceptance.
- Signing and runtime proof are separate Activities.

---

# Document-specific boundary

Document generation, parsing and rendering remain distinct:

- caller payload/policy;
- normalized document model;
- template/CSS/fonts/assets;
- HTML intermediate;
- PDF output;
- page renders;
- extracted text/elements/tables/images;
- delivery/signature/payment-authority receipts.

A generated document cannot create payment or external truth. Private brand/legal templates remain caller-specific packs.

---

# Image/media-specific boundary

Creative Studio projects are editable derivatives referencing Object-backed Assets.

- libvips handles efficient neutral image operations.
- ffprobe/FFmpeg handles multimedia structure/transforms.
- Creative Studio provides layer/timeline/project UX and caller-specific proof gates.
- Intelligence-generated Assets require model/prompt/seed/mask/tool receipts and remain editable derivatives.

Automated visual checks, human approval and release acceptance remain separate.

---

# Android application boundary

One application package can yield parallel views:

- raw entries;
- normalized manifest/components/permissions;
- resource table/assets;
- DEX/native libraries;
- certificates/signing evidence;
- Apktool decoded resources/smali/project;
- JADX Java-like source/mappings/graphs;
- LIEF runtime-format structures;
- rebuilt/signed/installed derivatives.

APK, AAB, APKS, split sets, XAPK and APKM require explicit package-set relationships. One file is not assumed to be the entire installed application.

---

# Provenance and telemetry

Every parser/transform receipt links:

- Activity/operation/attempt;
- source Object(s);
- Facility/Domain Pack/version/build features;
- command/configuration/model/grammar;
- Node/Provider;
- budget used;
- outputs/children/views;
- warnings/coverage/limitations;
- trace ID;
- exact hashes.

Telemetry may be sampled; proof-critical receipts and Object relationships remain durable.

---

# Donor decisions

- **App Recover:** internal detection/recovery/output-taxonomy donor; not universal engine.
- **APK Extractor:** internal Android multi-view orchestrator; product remains separate.
- **Creative Studio:** editable media project/proof donor; not neutral media engine.
- **Document Generator:** private template/render/truth-separation donor.
- **libarchive:** primary archive stream/entry foundation.
- **Tika:** primary broad detector/metadata/text candidate.
- **Unstructured:** primary document element/layout/OCR completion candidate.
- **LIEF:** primary structured executable/runtime parser candidate.
- **Binwalk:** primary embedded-signature/entropy completion candidate.
- **JADX:** primary Android Java-like source/static graph backend.
- **Apktool:** primary Android resource/smali/rebuild backend.
- **libvips:** primary neutral image transform/preview backend.
- **FFmpeg/ffprobe:** primary multimedia inventory/transform backend.
- **Tree-sitter:** optional source syntax-tree Facility.

All remain behind Ptah-owned contracts and exit strategies.

---

# Consequences

## Positive

- Original bytes and identity remain trustworthy.
- Multiple parsers can disagree without data loss.
- Huge and hostile inputs are bounded and isolated.
- Progressive results appear early while deep work continues concurrently.
- Products such as App Recover, APK Extractor, Creative Studio and Document Generator can reuse neutral Objects/Facilities without becoming Ptah Core.
- Generated/decompiled/rebuilt content cannot masquerade as original source.
- New firmware/application/document packs fit one common extension model.

## Costs

- The Object Graph and relationship vocabulary are richer than a directory tree.
- Budgets, partial states and competing views increase schema/UI complexity.
- Native parser isolation and dependency packs require operational maintenance.
- Exact parser/build/model provenance increases storage.
- Rebuild and verification need separate Activities rather than one success flag.

## Do-not-break rule

> Never overwrite the immutable original or promote extension hints, parser success, extracted text, decompiled source, decoded resources, previews, rebuilt outputs or review results into universal Object truth. Each is a distinct claim, child, view, derivative or proof level with exact provenance and limits.

---

# Required proof before freeze

1. Register one mixed corpus and preserve immutable originals plus all detector claims.
2. Detect mislabeled, extensionless, polyglot, encrypted, malformed, truncated and unknown Objects honestly.
3. Recursively decompose nested archives under hard depth/byte/count/time limits and reject traversal/link attacks.
4. Map overlapping embedded regions and unknown gaps by offset/hash.
5. Parse documents into page/text/table/image views and prove coordinate overlays.
6. Decode images/media into metadata, frames/tracks/previews under pixel/frame/time budgets.
7. Parse binaries and Android packages through competing tools while retaining coverage/disagreement.
8. Label decompiled/generated source origins correctly.
9. Cancel/crash/restart deep decomposition and preserve verified partial child Objects without duplication.
10. Run unrelated decomposition Activities concurrently without blocking terminals, transfers or builds.
11. Rebuild/transform a copy and classify byte/structural/visual/functional equivalence separately.
12. Replace one parser backend without changing original/child Object identities or public Domain Pack contracts.
