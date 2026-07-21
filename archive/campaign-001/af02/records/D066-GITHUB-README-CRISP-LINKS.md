# D066 — GitHub README Crisp Links Archive Record

Outcome: ACCEPTED FOR ARCHIVE — documentation-presentation tool only; no README-security or semantic-proof claim

Campaign: `CAMPAIGN-001`

Formation: `AF02`

Primary Archivist: `AF02-P02`

Independent Verifier: `AF02-V02`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `aza-ali/github-readme-crisp-links`;
- owner: Aza Ali;
- visibility: public;
- archived: false;
- default branch: `main`;
- inspected commit: `1503b45546a9b50777e5755aa2368be9297cf719`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root licence: MIT;
- licence evidence: `LICENSE` blob `c07cf2af1e2ff560afc2ac9b3b0e177cddfc040c`;
- generated SVGs may contain text, branding and font-derived path data whose use remains the operator's responsibility;
- system/user fonts retain their own rights and redistribution limits;
- activity state: active; inspected head changes gradient rendering to vector paths.

## Primary evidence packet — AF02-P02

Inspected:

- `README.md` blob `95aa04ea4a9de1e6ab709f0c59b7e8dc4f500c1a`;
- `crisp.py` blob `984aec8e716cf136665ebec23db76c43b155725f`;
- root `LICENSE`;
- exact current head.

Verified:

- the project is a small Python CLI plus browser-facing demonstration for creating SVG-only README links;
- it avoids GitHub's text-link underline by placing an SVG image inside an anchor;
- solid-color output uses SVG text while gradient output converts glyphs to vector paths using fontTools;
- Pillow measures text width; fontTools is optional except for gradient/path mode;
- inputs include names, links, colors, gradients, font paths, sizes and batch JSON;
- source validates color formats and escapes/generated output through bounded templates;
- README documents GitHub sanitizer, image proxy caching, dark-mode and font-width limitations.

Primary conclusion:

Crisp Links is a valid small presentation-tool donor for generated README assets and documentation polish. It is not evidence about linked project correctness, accessibility completeness, security, package quality or architectural fitness.

## Independent verification packet — AF02-V02

Repeated checks:

- canonical identity and `main` branch;
- exact current head;
- MIT root licence;
- executable Python CLI rather than documentation-only claims;
- font/Pillow/fontTools dependencies and vector-path behavior;
- documented cache, theme and rendering limitations.

Challenges retained:

- SVG link labels can become stale or misleading if the underlying destination changes;
- generated image text must preserve meaningful `alt` text for accessibility;
- embedding untrusted text/URLs requires validation and review even when HTML escaping is used;
- font-derived path output may create redistribution questions for some fonts;
- presentation polish cannot replace textual documentation, provenance or validation evidence.

Verifier conclusion: primary findings supported. The tool belongs in documentation/presentation support, not Ptah runtime authority.

## Ptah relationship

- frozen donor group: documentation and public presentation;
- current classification: optional documentation-generation tool;
- requirements supported: branded README navigation assets, repeatable SVG generation and presentation experiments;
- prohibited inheritance: image labels as canonical metadata, generated links as source verification, presentation output as accessibility/security proof;
- replacement/exit strategy: keep generated assets reproducible, retain source text/URLs separately and allow replacement with plain Markdown or native documentation tooling.

## Contradiction and supersession

- the campaign label “GitHub README Crisp Links” resolves to `aza-ali/github-readme-crisp-links`;
- current source confirms it is executable software, unlike the adjacent curated catalogue;
- identity resolution does not promote the tool into Ptah Core or alter documentation authority.

## Bounded outcome

`accepted for archive` retains the current tool, licence and limitations. It does not authorize use of third-party fonts/branding, certify generated links, reopen Phase 0A, start AF03, accept ADR-0033 or authorize Ptah runtime implementation.
