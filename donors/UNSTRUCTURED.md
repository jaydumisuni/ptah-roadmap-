# Donor Record — Unstructured

**Phase:** 0A / WP05  
**Status:** FIRST-PASS COMPLETE — DOCUMENT ELEMENT/PARTITION DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/Unstructured-IO/unstructured
- Default branch: `main`
- Pinned commit: `d309caf8ee20b735eb105d4e16ac3f04e5a48172`
- Licence: Apache-2.0
- Activity: Active
- Classification: Document/image/email partitioning, layout-element and enrichment-provenance donor
- Ptah targets: page/section/title/narrative/table/image/list/email elements, coordinates, OCR/layout routes, document chunking and structured text derivatives

## Files/components inspected

- `README.md`
- `LICENSE.md`
- `unstructured/documents/elements.py`
- documented automatic partition routing, format extras, OCR/Poppler/LibreOffice/Pandoc dependencies and telemetry boundary

## Verified capabilities and patterns

- Open-source library for ingesting and preprocessing PDFs, HTML, Word documents, emails, images and many other formats.
- Automatic `partition` function detects file type and routes to a format-specific partitioner.
- File-specific partition functions allow tighter control where needed.
- Produces ordered document elements rather than only one flat text string.
- Element metadata supports:
  - page number/name;
  - parent ID/category depth;
  - coordinates plus coordinate-system dimensions;
  - file type/name/directory and source metadata;
  - links and emphasized text;
  - tables as HTML/cells, extraction method and table/chunk identity;
  - image path/base64/MIME metadata;
  - email headers/recipients/subject/message ID;
  - language and continuation markers;
  - layout-routing decisions/scores;
  - detection class probabilities;
  - per-attribute enrichment origins including provider/model identity;
  - audio transcription segment timestamps.
- Element coordinates enforce that points and coordinate-system metadata appear together.
- Original pre-chunk elements can be retained when chunking.
- Partitioning supports optional extras so deployments can install only required document types.
- PDF/image paths can use Poppler and Tesseract OCR; Office conversion can use LibreOffice; Pandoc supports conversions.
- Docker images are commit/version tagged and support multiple architectures.
- Telemetry is off by default and can be explicitly opted in/out.

## What Unstructured completes

- A rich neutral starting point for document element schemas.
- Page/layout-aware partitioning beyond Tika's broad text/metadata output.
- Tables, images, coordinates, links, email metadata and parent relationships.
- OCR and scanned-document support.
- Explicit enrichment/model provenance fields.
- Retention of original elements across chunking.
- Format-specific dependency/capability selection.
- A strong complement to Tika: Tika routes broadly; Unstructured produces document-oriented semantic elements.

## Important limitations for Ptah

- The project is oriented toward LLM/RAG preprocessing, so chunking/embedding convenience must not define Ptah's canonical Document Object model.
- Element classification, OCR, layout routing and tables can be probabilistic or model-dependent.
- Different strategies/models/dependencies may produce different ordering, coordinates, text and table structures.
- OCR text is a derived claim, not the original page content.
- Some metadata stores source filenames/paths, image base64 and email/contact information requiring privacy control.
- Image base64 and original-element embedding can make outputs very large.
- Full format support brings heavy Python/native/system dependencies and optional model downloads.
- LibreOffice, Poppler, Tesseract and model execution are separate toolchains with their own security/licence/version concerns.
- Automatic partition routing returns a selected path but does not replace Ptah detector consensus.
- Processing malformed or hostile documents should be isolated and resource bounded.
- Hosted Transform/Pipelines products are distinct from the open-source library and must not become mandatory.
- Element IDs/parent IDs are library output identity, not Ptah Object identity.
- Table/layout results do not guarantee semantic correctness.
- The library does not provide durable Activities, Object storage, rendering proof or original-vs-derivative authority.

## Must not be inherited

- RAG chunks used as canonical document structure.
- OCR/model output promoted to unquestionable text/layout truth.
- Hosted Unstructured services made mandatory.
- Source paths, email addresses, image base64 or private metadata emitted without classification/redaction.
- All document extras/models installed in every Node.
- Automatic router result stored as the only type claim.
- Element IDs used as durable Ptah Object IDs.
- Original source replaced by extracted elements/chunks.
- Model/network downloads allowed implicitly during deterministic or offline work.
- Telemetry enabled without explicit deployment choice.

## Integration decision

**ADAPT THE ELEMENT/METADATA MODEL AND WRAP FORMAT-SPECIFIC PARTITIONERS AS DOCUMENT FACILITIES.**

Tika remains the broad first-pass detector/metadata/text candidate. Unstructured is the primary layout/document-element completion candidate for PDFs, Office documents, emails, HTML, images and OCR-heavy content.

Ptah should map each stable element/region/table/image/page into typed child Objects or views linked to the immutable original, while retaining strategy/model/tool provenance and confidence.

## Native Ptah gap

Ptah must define:

- Document Object model and relationship types for page, region, title, paragraph, list, table, cell, image, attachment, link, header/footer and chunk;
- element identity derived from source Object, page/region and parser receipt rather than library UUID alone;
- multiple competing parser/OCR/layout views;
- coordinates normalized across page/render coordinate systems;
- OCR/model strategy, version, configuration, language and confidence;
- source-page render references and visual evidence;
- privacy/redaction classes for email/contact/image/source-path data;
- output size limits and external Object references instead of embedded base64 where appropriate;
- parser/provider isolation and dependency packs;
- offline/model-download policy;
- exact ordering and parent/child preservation;
- chunk-as-view distinction;
- comparison/verification against PDF text layer or alternate OCR.

## Exit strategy

Ptah's Document Domain Pack remains compatible with Unstructured, native format libraries, OCR engines, Tika and other layout models. Element Objects and provenance survive backend replacement.

## Validation required

1. Partition born-digital, scanned, mixed-layout and malformed PDF samples into pages/elements/tables/images.
2. Preserve coordinates and render overlays proving source-region alignment.
3. Compare Tika text, PDF text layer and two OCR/layout strategies; retain disagreements/confidence.
4. Parse DOCX, PPTX, XLSX, HTML, email and image documents with only required dependency packs installed.
5. Keep email/contact/private metadata access-controlled and remove source paths from public derivatives.
6. Bound pages, pixels, OCR time, model memory, element count, base64 bytes and chunk outputs.
7. Disable network/model downloads and produce explicit missing-capability state.
8. Preserve original elements when creating chunks and label chunks as views, not source structure.
9. Crash/timeout a parser model without losing completed page/element Objects.
10. Replace one partitioner/model while keeping original Object and competing-view relationships stable.
