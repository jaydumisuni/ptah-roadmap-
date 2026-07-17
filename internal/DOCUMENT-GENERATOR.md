# Internal Recovery Record — TTG Document Generator Templates

**Phase:** 0A / WP05  
**Status:** FIRST-PASS COMPLETE — WORKING HTML/PDF DOCUMENT RENDERER AND TEMPLATE PACK  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/ttg-document-generator-templates`
- Visibility: Private
- Default branch: `main`
- Pinned commit: `46b0b37550b39543e125a19adda77c365a95d3a2`
- Package version: `1.0.0`
- Licence: `package.json` declares ISC, but no root licence text was found; preserve private/internal extraction status until the licence file/ownership boundary is confirmed.
- Ptah relevance: structured payload normalization, versioned document templates, HTML/PDF derivatives, browser rendering, overflow/layout safety, payment-truth separation and document metadata.

## Files/components inspected

- `README.md`
- `package.json`
- `scripts/render-document-v8.js`
- `scripts/render-pay-gateway-payload-v1.js`
- `scripts/check-pay-gateway-payload-support.js`
- documented quote/receipt/disclaimer/invoice and referral commission template paths

## Verified implemented behavior

### Supported document workflows

- Main renderer supports quote, receipt, disclaimer confirmation and invoice payloads.
- A separate Pay Gateway renderer supports `receipt-ready-payload` and `commission-ready-payload` envelopes.
- Compact one-page quote mode is documented.
- Quote templates support several conditional service/order modes.
- Optional sections include TPIN, email, tracking, warranty, payment instructions, photos, acceptance and signatures.
- Shared CSS is intended to solve overflow/layout problems centrally rather than post-editing generated PDFs.
- Long document numbers, business names, phone/email values, references, serial/IMEI values, URLs, table cells, totals and footer/card content are explicitly considered by the layout safety rules.

### Payload normalization

- Renderer initializes nested payload sections and applies defaults.
- Items are normalized into numbered rows with description, category, quantity, unit price and line total.
- Totals include subtotal, discount, tax, amount received, balance and grand total.
- Currency defaults to ZMW.
- Template-specific normalizers prepare quote, receipt, disclaimer and invoice values.
- Unsupported template/payload types are rejected explicitly.
- Pay Gateway envelopes can be unwrapped from `{ok, payload}` form.
- Pay Gateway-derived documents retain source markers such as generated-by, payment-truth source and payload type.
- Payment/commission payload support has a repository test that checks renderer paths, payload normalization markers, truth fields, templates and package scripts.

### Rendering and outputs

- Handlebars compiles HTML templates with ordinary escaping enabled.
- Shared CSS and normalized payload are combined into HTML.
- Generated HTML is retained beside the PDF.
- Playwright Chromium loads the HTML and prints an A4 PDF with background graphics and template-specific scaling.
- Output filename uses a sanitized document number.
- The renderer returns JSON containing success, template, renderer ID, PDF path, HTML path and document metadata.
- Failure returns a structured error code/message and non-zero process status.
- Browser closure is protected by `finally`.

### Ownership and truth boundaries

- The repository explicitly states that the generator must not send WhatsApp/email, verify or confirm payment, contact customers or decide business rules.
- The intended flow keeps payload preparation, rendering, delivery and payment truth in separate systems.
- Pay Gateway renderer marks Pay Gateway as the source of payment truth rather than creating payment truth from rendering.
- Generated customer PDFs, real payloads, signatures, phone numbers, private photos, NRCs, keys and secrets are prohibited from source control.

## Strong internal patterns for Ptah

1. Structured payload, template, rendered HTML and rendered PDF are separate Objects/derivatives.
2. Rendering is not delivery and does not establish payment or business truth.
3. Source-system/truth markers should travel with generated documents.
4. Template-specific normalization belongs in a versioned adapter rather than ad hoc PDF edits.
5. Layout/overflow fixes belong in template/style code and should be regression-tested.
6. Conditional sections should render only when supplied/enabled.
7. HTML should remain as a useful intermediate/proof derivative beside PDF.
8. Renderer identity/version and selected template belong in the result.
9. Unsupported payload/template types must fail explicitly.
10. Document output can be generated headlessly and invoked as a Facility.
11. Sensitive live payloads and generated customer outputs must remain outside source control.
12. A document can preserve the authority/source of underlying facts without becoming that authority.

## Important limitations

### Schema and semantic gaps

- Payloads are normalized through JavaScript defaults but are not validated against versioned JSON Schema.
- Unknown fields, type mismatches and required-field omissions may be silently normalized into defaults.
- Several document numbers are generated from the current date and are not collision-safe durable IDs.
- Renderer IDs are string constants but template/CSS/browser/package hashes and exact Playwright/Chromium versions are not returned.
- There is no neutral Document Object model for sections, tables, fields, pages, images and signatures.
- HTML/PDF text, pages, tables and embedded images are not decomposed back into semantic child Objects.
- Accessibility, PDF/A, tagged PDF, embedded-font and archival conformance are not verified.

### Policy leakage

- Despite the stated rule that the generator must not decide business rules, the renderer embeds default quote/receipt/disclaimer/warranty/payment wording and deposit behavior.
- Defaults can influence legal/commercial meaning when the caller omitted fields.
- Ptah must treat such wording as caller/project template policy, not neutral rendering logic.
- The Pay Gateway `paymentTruth` marker is a claim from the supplied payload; the renderer does not cryptographically verify its origin or receipt identity.

### Determinism/provenance gaps

- `today()` and date-derived numbers make output dependent on render time when the caller omits values.
- Chromium/PDF metadata, font availability, network resources and environment may make bytes non-deterministic across Nodes.
- The PDF/HTML are written directly rather than atomically promoted after verification.
- Output files are not hashed or registered as immutable Objects/Artifacts.
- Input payload hash, template hash, CSS hash, browser/tool version, font set and renderer environment are not captured in the result.
- No page render/image proof or PDF reopening/validation occurs after generation.

### Security/privacy gaps

- `page.setContent(..., waitUntil: "networkidle")` can load resources referenced by generated HTML; remote asset/network policy is not explicitly restricted.
- Data URI photos/signatures can substantially enlarge or destabilize output and lack explicit size/type limits.
- Input JSON size, item count, photo count (other than a three-photo slice), text lengths and total page count are not governed by a general resource budget.
- Handlebars escaping protects ordinary fields, but triple-brace/template or URL/data content still requires template review and CSP/network restrictions.
- Generated HTML contains the full sensitive document payload and needs the same retention/access classification as PDF.
- Output paths are caller/process paths rather than approved Ptah Object/Workspace targets.

### Runtime and lifecycle gaps

- Rendering is one local Node.js process with no Activity Ledger, cancellation, timeout, worker lease or restart recovery.
- A new Chromium process is launched per render; no controlled browser pool/resource accounting is present.
- No concurrency, queue, rate/size quota or backpressure contract is defined.
- Tests mostly check source strings/existence for Pay Gateway support rather than full semantic/rendered-output assertions.
- No cross-platform/clean-container visual regression corpus was inspected.
- Delivery status, signature collection and payment verification remain outside the renderer but need typed external receipt links.

### Product/licence boundaries

- Brand, legal wording, payment modes, warranty, business identity and templates are private company policy/content and must not become public Ptah defaults.
- Real customer data and generated documents are private Objects.
- No root licence file was found despite ISC package metadata.

## What Ptah should reuse or adapt

- structured payload→normalized document model→HTML→PDF derivative chain;
- headless browser rendering as one Document Facility backend;
- template/version/result identity and structured errors;
- shared layout safety and visual regression requirements;
- preserved HTML intermediate;
- source authority/truth references;
- strict separation among generation, delivery, payment truth and acceptance;
- conditional sections and compact/full layout variants;
- privacy classifications for payload, HTML, PDF, photos and signatures;
- domain-specific private template packs over a neutral public renderer.

## What Ptah must not inherit

- THETECHGUY brand/legal/payment defaults in public Ptah schemas;
- renderer defaults deciding caller business rules;
- date-derived document number as canonical Object identity;
- unverified `paymentTruth` string treated as an authoritative receipt;
- unrestricted network/resource loading during rendering;
- local paths as document identity;
- PDF generation exit code as semantic or visual verification;
- direct output overwrite without Object finalization;
- private customer payloads in telemetry, source control or public Artifacts;
- source extraction before licence text/ownership is confirmed.

## Classification

**ADAPT THE PAYLOAD/TEMPLATE/HTML/PDF AND TRUTH-SEPARATION PATTERNS; HOST PRIVATE TEMPLATES AS CALLER-SPECIFIC PACKS; BUILD A NEUTRAL PTAH DOCUMENT DOMAIN PACK.**

This repository is strong internal evidence for `DOC-001`, `CORE-003`, `CORE-004`, `PROV-001`, `OBS-001` and delivery-proof relationships. It is not Ptah's universal document model or policy authority.

## Native Ptah completion required

- versioned neutral Document payload/schema and template-manifest contract;
- private caller template/policy packs;
- stable document/operation IDs and content hashes;
- exact input/template/CSS/font/browser/renderer provenance;
- restricted network/resource loading and input budgets;
- atomic render/finalize/validate path;
- HTML/PDF/page/image/text/table/section child Object relationships;
- PDF parsing, page rendering and archival/accessibility validation adapters;
- visual regression and overflow corpus;
- Activity cancellation, timeout, pooling, concurrency and resource accounting;
- signed source-truth/receipt references for payment or external facts;
- privacy, retention, redaction and secure deletion classes;
- delivery and signature receipts kept separate from generation.

## Validation inherited into Ptah

1. Render quote, receipt, disclaimer and invoice from schema-valid payloads and reject invalid/unknown types.
2. Bind every PDF/HTML to exact payload, template, CSS, font, Chromium and renderer hashes/versions.
3. Reopen/render generated PDF pages and verify page count, text presence, overflow and non-empty visual output.
4. Test extreme long values, tables, Unicode, URLs, serials, photos and signatures under explicit size/page budgets.
5. Disable remote network access and prove all required assets are content-addressed/local or explicitly allowed.
6. Confirm HTML escaping and reject script/resource injection through fields, URLs and data content.
7. Preserve source payment/authority receipt references and prove document generation cannot create payment truth.
8. Render on two compatible Nodes and classify byte/visual differences honestly.
9. Fail PDF generation after HTML creation and preserve a partial derivative state rather than universal success.
10. Keep private template/legal/brand packs removable without changing public Ptah Document/Object contracts.
