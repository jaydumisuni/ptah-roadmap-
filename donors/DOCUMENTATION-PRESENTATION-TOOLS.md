# Donor Record — Documentation and Public Presentation Tools

**Phase:** 0A / source cleanup  
**Status:** COMPLETE — OPTIONAL PRESENTATION TOOLING, NOT PTAH CORE  
**Inspected:** 2026-07-18

## Purpose

Classify the original donor pool's README, documentation-site and diagram tools without confusing generated public presentation with Ptah's authoritative roadmap, Objects, Activities, Claims or Evidence.

The tools in this record are replaceable build/presentation Facilities.

---

## 1. GitHub README Crisp Links

### Identity

- Canonical repository: https://github.com/aza-ali/github-readme-crisp-links
- Default branch: `main`
- Pinned commit: `1503b45546a9b50777e5755aa2368be9297cf719`
- Licence: MIT
- Primary implementation: Python CLI plus browser-facing static utility
- Classification: optional README asset generator

### Verified capabilities

- Generates small SVG text labels for use as image-only GitHub links.
- Supports solid colours, gradients, custom fonts, sizing and batch JSON input.
- Uses Pillow for font measurement.
- Uses fontTools path conversion for gradient glyph rendering.
- Emits the SVG plus a copy-ready HTML/Markdown snippet.
- Handles GitHub image-proxy caching through ordinary filename/query-version practices.

### Ptah use

- optional donor/facility lists;
- branded README links;
- public project cards and navigation labels;
- generated documentation assets.

### Limitations and boundaries

- It is a presentation workaround for GitHub README CSS, not a documentation architecture.
- SVG dimensions depend on local font availability/metrics.
- Path-based text can increase asset size.
- GitHub cache behavior can make updates appear stale.
- Text-as-image can reduce selection, translation and accessibility quality if alt text is poor.
- Generated labels must not replace meaningful text in source documents or hide link destinations.
- User-provided strings/links and generated SVGs require escaping and review before publication.
- Font files are environmental inputs and must not be committed or redistributed without rights.

### Decision

**OPTIONAL PUBLIC-ASSET GENERATOR ONLY.**

Use plain Markdown/HTML text by default. Use generated SVG labels only where visual value justifies accessibility and maintenance costs.

---

## 2. Material for MkDocs

### Identity

- Canonical repository: https://github.com/squidfunk/mkdocs-material
- Default branch: `master`
- Pinned commit: `b3e6dd886a974aa8200759ecfd7db28c598a2894`
- Inspected release preparation: 9.7.7
- Licence: MIT
- Primary implementation: Python/MkDocs theme and plugins with web assets
- Classification: primary candidate for a lightweight technical documentation site

### Verified capabilities

- Markdown-first static documentation.
- Responsive desktop/tablet/mobile presentation.
- Search, navigation, tags, blog, metadata, offline, privacy and optimization plugin entry points.
- Localization and configurable branding.
- Static output that can be hosted independently.
- Python package entry points around MkDocs themes/plugins.

### Ptah use

- architecture manuals;
- operator/developer guides;
- ADR and donor-record publishing;
- versioned public documentation;
- static documentation builds in CI.

### Limitations and boundaries

- Generated pages are derived Views; repository Markdown and exact revisions remain source truth.
- Plugins can execute code during builds and require independent pin/licence/security review.
- Theme or plugin upgrades may alter navigation, anchors, search and rendering.
- Client-side search indexes can expose content included in a public build.
- Private roadmap material must never enter a public build merely because navigation hides it.
- Static output does not provide application authorization or dynamic Ptah UI behavior.

### Decision

**PRIMARY LIGHTWEIGHT DOCUMENTATION-SITE CANDIDATE, SUBJECT TO PHASE 0C SELECTION.**

It is not selected for implementation yet and remains replaceable by another static documentation system.

---

## 3. Docusaurus

### Identity

- Canonical repository: https://github.com/facebook/docusaurus
- Default branch: `main`
- Pinned commit: `a0bc32214436d52a5ac9de9be1a515d872987366`
- Inspected package line: 3.10.1
- Licence: MIT for code; repository documentation carries separate Creative Commons terms
- Primary implementation: TypeScript/React monorepo
- Classification: optional richer documentation/project-site candidate

### Verified capabilities

- Docs, pages and blog under one project site.
- Versioned documentation and localization.
- React-based customization and component composition.
- Static-site build/deployment.
- Search/community plugin ecosystem and conventional project-site pages.

### Ptah use

- richer public project website;
- versioned technical docs;
- blog/release communication;
- custom interactive documentation components.

### Limitations and boundaries

- Larger Node/React dependency and build surface than a Markdown-first MkDocs site.
- Plugins/themes execute within the documentation build chain.
- Custom React pages can become an application-maintenance burden.
- Documentation-source licences differ from framework-code licence.
- Public build filtering and secret/private-source exclusion remain Ptah repository policy, not a framework guarantee.
- It must not become the Human Workspace shell or Ptah runtime UI merely because it supports React pages.

### Decision

**OPTIONAL RICH DOCUMENTATION/PROJECT-SITE ALTERNATIVE.**

Choose only if versioning, blog and custom-site requirements justify the added build/runtime dependency surface.

---

## 4. Mermaid

### Identity

- Canonical repository: https://github.com/mermaid-js/mermaid
- Default branch: `develop`
- Pinned commit: `f0ffb41c1ee1ff667b528e86c3b082249726eeef`
- Licence: MIT
- Primary implementation: TypeScript/JavaScript diagram parser and renderer
- Classification: primary text-defined documentation-diagram candidate

### Verified capabilities

- Markdown-inspired text definitions rendered as diagrams.
- Flowcharts, sequence, class, Gantt, git and other diagram families.
- Browser/library/editor integrations.
- Build, parser, unit, end-to-end and visual-regression tooling in the inspected repository.
- Text source is easier to diff and revise than hand-maintained binary diagrams.

### Ptah use

- architecture diagrams;
- Activity and state graphs;
- Object and relationship views;
- Facility maps;
- donor/composition diagrams in documentation.

### Limitations and boundaries

- Diagram source is a documentation View, not authoritative schema or executable workflow.
- Layout/rendering can change across Mermaid versions.
- Complex graphs may become unreadable and require deliberate decomposition.
- Rendering untrusted diagram text is code/parser-facing input and must use an approved security configuration and isolated build/render path.
- Links and labels must not expose private repository, customer or security information in public builds.
- Accessibility still requires explanatory surrounding text.
- A rendered green node or arrow is never runtime/proof state.

### Decision

**PRIMARY TEXT-DIAGRAM CANDIDATE FOR DOCUMENTATION, NOT A RUNTIME GRAPH ENGINE.**

Pin the renderer for reproducible builds and retain diagram source plus rendered output as separate revisions.

---

## Composite documentation model

```text
Authoritative source
  Markdown, ADR, schema, donor record, Object or Activity record

Documentation build recipe
  exact generator, theme, plugins, configuration and dependency lock

Generated documentation Artifact
  static HTML, search indexes, styles, assets and diagrams

Publication
  exact site target, audience and public/private filter

Validation
  link, accessibility, search, content-leak, visual and build checks
```

Generated documentation never becomes source truth merely because it is public or visually polished.

## Public/private rules

1. Public documentation builds consume an explicit allowlisted public source tree.
2. Private roadmap, consumers, credentials, topology, customer data and unremediated security evidence are excluded before build.
3. Search indexes, source maps, generated JSON and static assets are checked for leakage.
4. Build dependencies/plugins are pinned and scanned as normal Artifacts.
5. Broken links and stale external sources are recorded rather than silently redirected to unrelated content.
6. Accessibility, mobile layout and reduced-motion behavior are tested.
7. Every published site records source commit and build Artifact digest.
8. Publication status does not imply implementation or requirement completion.

## Final classification

| Tool | Classification | Preferred role |
|---|---|---|
| Crisp Links | Optional presentation utility | README labels/assets only |
| Material for MkDocs | Primary lightweight candidate | Technical documentation site |
| Docusaurus | Optional richer alternative | Versioned project site/blog/custom pages |
| Mermaid | Primary diagram candidate | Text-defined documentation diagrams |

## Phase 0C selection criteria

- required documentation features;
- contributor skill and maintenance cost;
- dependency and plugin surface;
- offline/static hosting needs;
- localization/versioning/blog requirements;
- public/private build isolation;
- accessibility and mobile quality;
- deterministic/reproducible builds;
- replacement/export cost.

No documentation framework is approved for implementation by this record.

## Exit strategy

All documentation sources remain ordinary repository content. MkDocs Material, Docusaurus, Mermaid and Crisp Links can be replaced without changing Ptah Core, runtime APIs, Objects, Activities, Claims, Evidence or accepted decisions.
