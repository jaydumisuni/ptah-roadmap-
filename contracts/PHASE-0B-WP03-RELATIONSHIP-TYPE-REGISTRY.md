# Phase 0B WP03 — Relationship Type Registry

**Status:** CANDIDATE
**Registry version:** `0.1.0`

Every relationship revision declares one registered type, direction and semantic class. Unregistered strings are rejected by canonical conformance.

## Structural/content relationships

| Type | Direction | Meaning |
|---|---|---|
| `contains` | container → member | broad containment claim; completeness is separate |
| `entry_of` | entry → container | archive/package entry membership |
| `embedded_in` | embedded object → host | content located within host bytes |
| `carved_from` | carved object → source | bytes recovered from source range/signature |
| `region_of` | region/view → source | located byte/page/coordinate region |
| `page_of` | page → document | page membership |
| `section_of` | section → binary/document | structural section membership |
| `segment_of` | segment → source | segment membership |
| `stream_of` | stream → media/container | media/data stream membership |
| `track_of` | track → media | track membership |
| `frame_of` | frame → media | frame membership |
| `attachment_of` | attachment → source | attachment membership |
| `resource_of` | resource → package/application | resource membership |
| `asset_of` | asset → project/object | asset membership |
| `layer_of` | layer → project/image | layer membership |

## Interpretation/View relationships

| Type | Direction | Meaning |
|---|---|---|
| `view_of` | View → source Revision | generic structured interpretation |
| `metadata_view_of` | View → source Revision | metadata interpretation |
| `text_view_of` | View → source Revision | extracted/decoded text |
| `ocr_view_of` | View → source Revision | OCR-derived text/layout |
| `syntax_tree_of` | View → source Revision | syntax tree interpretation |
| `decoded_view_of` | View → source Revision | decoded representation |
| `decompiled_view_of` | View → source Revision | approximate decompiled source |
| `disassembly_view_of` | View → source Revision | disassembly representation |
| `comparison_of` | View/report → compared subjects | comparison result over exact subjects |
| `report_for` | report → subject | bounded report association |

## Preview relationships

| Type | Direction | Meaning |
|---|---|---|
| `preview_of` | Preview → source Revision | human-oriented derived representation |
| `thumbnail_of` | Preview → source Revision | thumbnail |
| `contact_sheet_of` | Preview → source Revision | contact sheet |
| `waveform_of` | Preview → source Revision | waveform/sample view |
| `transcript_of` | transcript View → source Revision | speech/media transcript |

## Transformation/derivative relationships

| Type | Direction | Meaning |
|---|---|---|
| `derived_from` | output Revision → source Revision | generic explicit derivation |
| `normalized_from` | output Revision → source Revision | normalization |
| `converted_from` | output Revision → source Revision | format conversion |
| `transcoded_from` | output Revision → source Revision | media transcode |
| `remuxed_from` | output Revision → source Revision | media/container remux |
| `edited_from` | output Revision → source Revision | human/tool edit |
| `patched_from` | output Revision → source Revision | patch application |
| `rebuilt_from` | output Revision → source Revision(s) | rebuild output |
| `supersedes_revision` | newer Revision → older Revision | logical supersession without erasure |

## Artifact/proof/release relationships

| Type | Direction | Meaning |
|---|---|---|
| `artifact_contains` | Artifact → Object Revision | promoted result membership |
| `artifact_for` | Artifact → subject | promoted result purpose/subject |
| `release_of` | Artifact Release → Artifact | immutable release manifest |
| `sbom_for` | SBOM Artifact → subject Artifact/Object Revision | inventory relation |
| `attestation_for` | attestation Artifact → subject | attestation relation |
| `signature_for` | signature Artifact → subject | signature relation |
| `review_of` | Review/Verdict → checkpoint/Artifact | exact review subject |
| `reproduction_of` | Reproduction Run/Artifact → claim/result | bounded reproduction relation |

## Storage relationships

| Type | Direction | Meaning |
|---|---|---|
| `materializes` | Location → Content | Location stores/materializes exact Content |
| `replica_of` | Location → Content | independent replica relation |
| `repair_source_for` | verified Location → repair/target Location | repair source relation |
| `export_of` | export Object/Artifact → source set | portable/export relation |
| `backup_of` | backup snapshot/Artifact → source set | backup relation; not live state |
| `cache_of` | cache record/location → source result | disposable derived cache relation |

## Locator requirements

Relationship revisions may carry one or more typed locators:

- byte range (`offset`, `length`);
- logical path/entry name;
- page number and bounding box;
- stream/track/frame index;
- section/segment identifier;
- class/method/resource identifier;
- timeline range;
- JSON Pointer or schema path.

A locator is evidence/metadata, not child identity.

## Semantic constraints

1. Relationships are directional; inverse display is a projection.
2. A relationship cannot change type or endpoints in place.
3. Conflicting or overlapping relationships coexist.
4. `contains` never implies complete coverage unless coverage evidence says so.
5. `decompiled_view_of` and `decoded_view_of` never imply original source.
6. `artifact_contains` never grants release/acceptance by itself.
7. `materializes` never proves the Location is available or verified.
8. Deletion authority is never inferred from relationship direction.
