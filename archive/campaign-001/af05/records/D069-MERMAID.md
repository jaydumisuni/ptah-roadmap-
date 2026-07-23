# D069 — Mermaid

Status: candidate record — paired evidence complete

Primary Archivist: `AF05-P08`

Independent Verifier: `AF05-V08`

Inspected: 2026-07-23

## Canonical source identity

- source: `mermaid-js/mermaid`;
- default branch: `develop`;
- exact inspected commit: `56219a3bd9c80d8cef439642de0a7a6a8a429ac1`;
- root licence: MIT;
- repository role: text-to-diagram rendering library and documentation tooling;
- archived: false.

## Primary evidence packet

Mermaid can generate architecture, activity, relationship and facility diagrams from text definitions and is useful for Ptah documentation and human-readable Views.

## Independent verification packet

The verifier confirmed that rendering, themes, browser integration, sanitization and host embedding are separate concerns. A diagram is a projection of supplied text, not authoritative system state or evidence acceptance.

## Contradiction and supersession

Mermaid remains documentation/presentation tooling only.

## Bounded outcome

`accepted_for_archive_mit_text_diagram_and_documentation_projection_tool`

Allowed reuse:

- render caller-approved diagrams and relationship projections;
- preserve source text, generator version and output Artifact linkage.

Restrictions:

- preserve MIT notices and review plugins/themes separately;
- sanitize untrusted diagram content and links;
- do not treat rendered diagrams as canonical records or proof;
- do not expose private Workspace data in public documentation.

This outcome does not authorize implementation.