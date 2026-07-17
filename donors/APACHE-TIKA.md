# Donor Record — Apache Tika

**Phase:** 0A / WP05  
**Status:** FIRST-PASS COMPLETE — BROAD DETECTION/METADATA/TEXT DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/apache/tika
- Default branch: `main`
- Pinned commit: `39e83a82d86b8d224ca4fccba0c28396ab806aa0`
- Licence: Apache-2.0 for the collective work, with bundled parser/dependency notices and separate terms requiring component-level review.
- Runtime baseline at inspected pin: Java 17; Tika 2.x/Java 8 support ended in April 2025, while the repository is moving through 4.x development.
- Activity: Active Apache Software Foundation project
- Classification: Broad media-type detection, metadata and structured-text parser orchestrator
- Ptah targets: first-pass type claims, metadata/text extraction, container-specific detection and broad document coverage

## Files/components inspected

- `README.md`
- `tika-core/src/main/java/org/apache/tika/detect/DefaultDetector.java`
- documented parser packages, Tika app/server boundaries, reproducible-build support and security/dependency notices

## Verified capabilities and patterns

- Detects and extracts metadata and structured text from many document/content formats through existing parser libraries.
- Can be embedded as a Java library, run through a standalone app or exposed through a server deployment.
- Parser packages are modular and version-aligned through a BOM.
- `DefaultDetector` implements an ordered composite pipeline:
  - MIME magic-byte detection;
  - SPI-loaded container/specialist detectors;
  - text fallback for still-unknown data;
  - selection of the most specific registered media type.
- Records the magic-detected type separately in metadata.
- Container detectors can spool through `TikaInputStream` when random access is required.
- Detector ordering can be customized; override detectors can take precedence.
- Dynamic/static service loading permits extension or exclusion of detectors.
- Tika provides text, metadata and structured-output paths suitable for indexing/search/document workflows.
- The project supports reproducible builds and documents deterministic build configuration.
- Encrypted PDF parsing can use Bouncy Castle; cryptographic/dependency/export-control considerations are documented.

## What Tika completes

- Broad first-pass content detection beyond filename extensions.
- A detector pipeline combining magic, container knowledge and text fallback.
- A common metadata/text extraction API across many document types.
- A strong routing signal for selecting deeper Domain Packs.
- An embeddable/server option for polyglot Ptah use.
- Existing parser-library integration that avoids rebuilding broad format coverage.
- A useful complement to libarchive: Tika identifies/extracts metadata/text while libarchive streams archive entries.

## Important limitations for Ptah

- Tika's final media type is one selected claim, not the complete Ptah detector-consensus/evidence record.
- The selection algorithm may prefer a container detector for unrelated claims; conflicting claims need retention rather than only the winner.
- Detection confidence/calibration is not expressed as a universal numeric probability.
- Text/metadata extraction does not preserve every binary structure, original layout or exact child relationship.
- Embedded resources and parser recursion require explicit caller limits and Object registration.
- Parsers may spool input to disk, increasing temporary-storage and privacy requirements.
- Large or malformed inputs can consume significant CPU, memory, disk or time.
- Parser packages bring a large dependency and native/tool attack surface; component/version/CVE review is required.
- Tika server/app deployment must be isolated and resource bounded; it is not the control plane.
- OCR, rendering, tables and precise page/layout semantics often require completion tools.
- Encrypted content may require credentials and still yield partial metadata only.
- Tika does not own Ptah Objects, revisions, Activities, receipts, previews or derivatives.
- The inspected main pin is development code; Phase 0C must select a stable release/package rather than blindly shipping the main commit.

## Must not be inherited

- One Tika media type treated as unquestionable Object truth.
- Filename/metadata hints allowed to override stronger content evidence without retaining conflict.
- Unlimited embedded-resource parsing.
- Full parser package loaded into the long-lived control plane.
- Extracted text described as a lossless document representation.
- Temporary spooled files left without privacy/cleanup receipts.
- Tika server exposed to untrusted callers without authentication, quotas and provider isolation.
- Parser success promoted to document correctness, safety or acceptance.
- Development-branch dependencies selected without stable-release and licence/CVE review.

## Integration decision

**ADOPT AS THE PRIMARY BROAD DETECTOR/METADATA/TEXT FACILITY CANDIDATE, BEHIND PTAH DETECTOR-CLAIM AND DOCUMENT CONTRACTS.**

Tika should provide one or more detector/parser claims early in Object intake, then route deeper work to libarchive, Unstructured, LIEF, FFmpeg, image, APK or firmware Domain Packs.

Ptah retains all relevant claims, evidence and limitations rather than storing only Tika's final chosen type.

## Native Ptah gap

Ptah must define:

- detector-claim schema with detector/version, claimed type, evidence class, confidence/priority and bytes inspected;
- conflict/consensus and routing rules;
- input/temporary-file/embedded-resource limits;
- parser package/capability manifest;
- metadata field provenance and normalization;
- text derivative identity and source locations/page/embedded relationships where available;
- encrypted/password credential reference;
- parser timeout/crash/partial-output states;
- child Object registration and deduplication;
- secure parser service/container deployment;
- exact stable release/dependency/SBOM receipt;
- fallback when a Tika parser is missing or unsafe.

## Exit strategy

Ptah's detector/metadata contract supports libmagic, format-specific parsers, Tika or other services. Tika-generated metadata/text remains ordinary derivatives and can be regenerated by another backend.

## Validation required

1. Test mislabeled, extensionless, polyglot, encrypted, malformed and truncated samples while retaining all detector claims.
2. Compare Tika magic/container result with libmagic and specialist parsers; surface disagreement.
3. Extract metadata/text from representative PDF, Office, email, HTML, image, archive and multimedia inputs.
4. Bound embedded-resource recursion, output text, temporary bytes, CPU and time.
5. Kill/timeout a parser and preserve partial outputs plus an explicit failure receipt.
6. Verify temporary spool cleanup and privacy classification.
7. Run parser packages in an isolated provider and demonstrate control-plane survival after parser crash.
8. Record exact parser/component versions and selected stable release.
9. Prove extracted text is linked as a derivative and never replaces the original Object.
10. Swap Tika for a specialist detector on one format without changing Object identity or public contracts.
