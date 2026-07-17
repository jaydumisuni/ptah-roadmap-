# Internal Recovery Record — TTG Creative Studio

**Phase:** 0A / WP05  
**Status:** FIRST-PASS COMPLETE — EDITABLE IMAGE/MOTION FOUNDATION WITH STRONG PROOF DISCIPLINE  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/ttg-creative-studio`
- Visibility: Public
- Default branch: `main`
- Pinned commit: `670215de820775ce7f4543cfa52ab6ee9a520301`
- Licence: no root `LICENSE` file was found at the inspected pin; public visibility does not establish reuse rights, so source extraction remains blocked pending an explicit licence.
- Ptah relevance: editable image/motion project schema, media asset intake, layer/timeline derivatives, deterministic rendering, previews, visual proof, human approval and optional FFmpeg export.

## Files/components inspected

- `README.md`
- `src/ttg_creative_app.py`
- `src/ttg_project_schema.py`
- `src/ttg_asset_package.py`
- `src/ttg_canvas_engine.py`
- `src/ttg_property_engine.py`
- `src/ttg_reference_still_renderer.py`
- `src/ttg_reference_motion_renderer.py`
- `src/ttg_image_intelligence.py`
- `scripts/build_ad_project_from_assets.py`
- `scripts/self_test_ad_project_workflow.py`
- `scripts/self_check_visual_pipeline.py`
- `scripts/review_gate_all.py`
- `scripts/build_release_decision.py`
- `scripts/build_video_proof.py`
- `packs/video-export-pack.json`

## Verified implemented behavior

### Editable project model

- Versioned JSON project format supports image, text, text3D, shape, SVG, video, audio, particle, camera, light, diagram, connector, measurement and group layer types.
- Canvas records width, height, frame rate, duration and background.
- Layers retain stable IDs, visibility/lock state, transforms, property dictionaries, effects, keyframes and child IDs.
- Assets retain ID, kind, name, path, optional SHA-256, pack ID and required flag.
- Projects retain audio markers and export settings.
- Save/load reconstructs project, canvas, assets, layers, transforms and keyframes.
- Manual deterministic editor operation is explicitly the foundation; intelligence is optional and later.

### Property/timeline engine

- Edits can target layer name/visibility/lock, transforms, arbitrary properties and effect fields.
- Locked layers reject ordinary edits.
- Layer start/end timing extends project duration.
- Keyframes are sorted by time and basic numeric interpolation is implemented.
- Timeline clips can be listed from layer timing properties.
- Property and timing behavior have dedicated review tests.

### Asset package intake

- Accepts media folders and ZIP packages.
- Supports selected image, video and audio extensions.
- ZIP member paths are resolved and required to remain inside the extraction root.
- Only supported media types are copied into the imported asset Workspace.
- Imported files are grouped into image/video/audio collections.
- Ad workflow converts folder/ZIP images into an editable `.ttgstudio.json` project with Assets, image layers, timing, keyframes, title, CTA and audio markers.

### Rendering and derivatives

- Pillow-based canvas renderer supports image, text/text3D, shapes, particles and diagram-like layers.
- Image rendering supports transforms, opacity, rotation, basic blur/glow and reflections.
- Text rendering supports styling/effects through a separate text renderer.
- Deterministic procedural still renderer creates a branded 2.5D reference image.
- Deterministic motion renderer generates frame sequences with easing, crop/zoom, brightness/contrast, wipes, scanlines and fades.
- Proof generation includes still images, motion frames, contact sheets and GIF previews.
- MP4 proof generation is gated and uses optional FFmpeg only after visual proof approval.
- Video export tooling is represented as an optional pack rather than bloating the base installation.

### Review and release proof

- One review command runs structural, compile, claims, property/timeline, asset package, ad workflow, canvas, worker, preset, offscreen UI, visual proof and benchmark-gap checks.
- Review stops on the first failing command and retains a review log.
- Release decision separates engine/workflow closure, automated visual guardrails, explicit human visual approval, visual proof closure and release-candidate decision.
- Non-empty proof artifacts are required.
- Final release requires both automated visual checks and human approval.
- The repository explicitly distinguishes engine/workflow closure from user-release closure and target-machine verification.

### Intelligence boundary

- Image intelligence request/result/task/module schemas exist.
- Suggested workflows are intended to map to editable actions/layers rather than hide work in one flattened bitmap.
- Background removal is modeled as an editable-mask adapter with review required.
- The current implementation explicitly returns `stubbed_native_architecture`; it is not a finished image-understanding/generation engine.

## Strong internal patterns for Ptah

1. Manual deterministic capability exists independently of optional intelligence.
2. Source media, editable project, rendered frames, contact sheets, GIF/MP4 and review reports are different derivatives/Artifacts.
3. Layer-based project state is more valuable than flattening every edit into a bitmap.
4. Tool packs can be optional capabilities discovered only when a workflow requires them.
5. Human visual approval and automated guardrails are separate proof levels.
6. Engine/workflow closure and user-release closure are separate.
7. Visual proof should contain actual composed output, not only source or test claims.
8. Project schemas need version, stable IDs, assets, layers, transforms, effects, timing and export intent.
9. ZIP/folder asset intake belongs below UI so it can be tested headlessly.
10. Image-worker output should be an editable plan/action set and generated child Assets, not opaque final pixels only.
11. Product claims are checked against implementation and generated evidence.
12. UI is a shell over proven engine/workflow capability.

## Important limitations

### Object/asset identity gaps

- Assets are path-based; `sha256` exists but the inspected ad import path does not populate it.
- Project files use local absolute paths and do not resolve through Ptah Object/location identities.
- Imported media are copied without content deduplication, exact source relationships or immutable Object registration.
- The import Workspace is deleted and recreated, which can destroy earlier evidence if not versioned externally.
- Project save is a direct JSON write without migration validation, atomic replacement or revision history.

### Asset-intake safety/scaling gaps

- ZIP traversal is checked, but no limits exist for file count, expanded bytes, compression ratio, per-file size, total time or nested packages.
- ZIP symlink/special-entry handling is not modeled explicitly.
- Supported type is selected by extension, not verified content type.
- Directory import recursively scans without explicit count/size/time budgets.
- Video/audio/image metadata is not probed at intake.

### Rendering gaps

- The generic canvas renderer currently ignores video, audio, camera and light layers and uses placeholders for some layer types.
- The renderer receives a time value but does not generally evaluate project keyframes during layer drawing.
- The reference motion renderer is a separate procedural proof path rather than a full timeline-driven project renderer.
- Audio mixing, video decoding/compositing, color management, masks, blend modes, codecs and synchronized A/V export are incomplete.
- Project layer width/height/fit settings are not fully respected by the generic image renderer.
- Font identity/fallback, color profiles, EXIF/orientation and deterministic cross-platform rendering need stronger records.
- FFmpeg pack metadata is still a placeholder and lacks real URLs/checksums.

### Proof and runtime gaps

- Proof outputs and project Assets are copied by paths rather than registered as hashed Objects/Artifacts with producer receipts.
- Visual scoring/approval proves selected benchmark outputs, not every project/render path.
- Human approval is repository-specific and should be caller/project policy, not universal Ptah authority.
- No durable Activity orchestration, cancellation, resume, frame cache identity or multi-Node rendering exists.
- Render steps are mostly local Python/Pillow processes without Node resource accounting.
- Clean-clone and target-machine proof are acknowledged as separate and not universally completed by the engine gate.

### Intelligence gaps

- Image understanding/generation/planning modules are architecture stubs.
- Suggested actions have no confidence/evidence/source-region grounding.
- Generated asset paths are proposed rather than proven created.
- No model/tool identity, deterministic seed, prompt receipt, source mask or content hash exists for intelligence results.

### Product/licence boundaries

- BrandKit and examples are THETECHGUY-specific and cannot become neutral public Ptah defaults.
- The repository has no explicit root licence at the inspected pin.
- Private brand assets, prompts, worker topology and approval policy must remain outside public Ptah contracts.

## What Ptah should reuse or adapt

- versioned editable media-project/layer concepts;
- asset/layer/keyframe/effect/transform taxonomy;
- deterministic manual-first editing and rendering;
- source→editable project→frame/preview/export derivative chain;
- safe-root ZIP path validation;
- optional runtime-tool pack/capability model;
- background-worker and headless-testable workflow requirements;
- visual proof package and explicit automated/human approval separation;
- engine versus release closure distinction;
- editable-action planning boundary for future image intelligence;
- contact-sheet/GIF/frame derivatives as useful views.

## What Ptah must not inherit

- THETECHGUY branding/default BrandKit in neutral Ptah schemas;
- local path as Asset identity;
- extension-only media type claims;
- unbounded asset-package extraction;
- stubbed image intelligence presented as working capability;
- procedural benchmark renderer presented as full timeline engine;
- visual approval as universal Ptah policy;
- placeholder FFmpeg pack described as installed/verified;
- direct project overwrite without revisions;
- private/unlicensed source copied into public Ptah.

## Classification

**ADAPT PROJECT/LAYER/DERIVATIVE AND PROOF PATTERNS; HOST CREATIVE STUDIO AS A SPECIALIST PRODUCT; USE LIBVIPS/FFMPEG AND PTAH OBJECTS AS THE NEUTRAL MEDIA FACILITIES.**

Creative Studio provides strong internal evidence for `CORE-003`, `IMAGE-001`, `MEDIA-001`, `CORE-004`, `UI-001`, `OBS-001` and `PROV-001`. It does not replace Ptah's neutral Image/Media Domain Packs or Object catalogue.

## Native Ptah completion required

- Object-backed Asset references and immutable hashes;
- project revision/migration/atomic-save model;
- media detector and metadata claims;
- libvips-backed image transforms and previews;
- FFmpeg/ffprobe-backed stream/track/container/A/V model;
- timeline-driven frame rendering and synchronized audio/video export;
- masks, blend modes, color/ICC/EXIF/orientation handling;
- extraction/intake budgets and nested-package policy;
- render cache and derivative identities;
- Activity/cancellation/restart/multi-Node rendering;
- model/seed/prompt/mask/tool receipts for intelligence-generated Assets;
- caller-configured review/approval policy;
- public/private asset and licence separation.

## Validation inherited into Ptah

1. Import folder and ZIP media under explicit file/count/byte/time limits and reject traversal/special entries.
2. Register each source Asset as an immutable Object and retain project references independent of local paths.
3. Save/edit/reload projects across schema versions without losing layer identity.
4. Render the same still deterministically on two compatible Nodes and record expected renderer/font/profile differences.
5. Evaluate keyframes through the actual generic timeline renderer, not only the procedural reference renderer.
6. Probe and decompose image/video/audio metadata into typed child Objects.
7. Export frames, contact sheet, GIF and MP4 as related derivatives with exact tool/codec receipts.
8. Fail FFmpeg/video capability honestly while still allowing image-only workflows.
9. Keep automated visual guardrails, human approval and release acceptance as separate verdicts.
10. Prove any intelligence-generated or background-removed Asset has source/mask/model/seed/tool provenance and remains editable.
