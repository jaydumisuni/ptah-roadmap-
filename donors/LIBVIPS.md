# Donor Record — libvips

**Phase:** 0A / WP05  
**Status:** FIRST-PASS COMPLETE — IMAGE TRANSFORM/PREVIEW FOUNDATION CANDIDATE  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/libvips/libvips
- Default branch: `master`
- Pinned commit: `0619d10a615dcdeea5c98d36215a8f07ad19de01`
- Licence: LGPL-2.1-or-later
- Activity: Active and fuzz-tested
- Classification: Demand-driven, low-memory image decode/transform/render foundation
- Ptah targets: image metadata, thumbnails/previews, resize/crop/rotate, color conversion, multi-page/frame views, image pyramids and efficient large-image processing

## Files/components inspected

- `README.md`
- documented demand-driven/horizontally threaded execution model
- format, operation, optional dependency and security boundaries
- C/C++/CLI and language-binding model

## Verified capabilities and patterns

- Demand-driven, horizontally threaded processing designed for high speed and low memory use.
- Roughly 300 operations covering arithmetic, histograms, convolution, morphology, frequency filters, color, resampling and statistics.
- Supports many numeric types and arbitrary band counts.
- Format coverage includes JPEG, JPEG 2000, JPEG XL, TIFF, PNG, WebP, HEIC, AVIF, FITS, Matlab, OpenEXR, PDF, SVG, HDR, PPM/PGM/PFM, CSV, GIF, Analyze, NIfTI, DeepZoom and OpenSlide, depending on build features.
- Optional ImageMagick/GraphicsMagick loading expands format coverage, including DICOM-like paths.
- Bindings exist for several languages including Python through pyvips and .NET through NetVips.
- ICC profile import/export/transform is available when lcms2 is enabled.
- EXIF, RAW, PDFium/Poppler, SVG, GIF, TIFF, HEIC/AVIF and other features are selected through optional build dependencies.
- DeepZoom/image-pyramid output can use libarchive.
- OSS-Fuzz coverage is active.
- Build configuration can explicitly enable or disable optional loaders/dependencies.
- The project explicitly warns that enabling ImageMagick for untrusted images expands attack surface.

## What libvips completes

- Efficient preview and derivative generation for large images.
- A neutral image engine stronger and more scalable than Creative Studio's Pillow-only paths.
- Broad image metadata/color/profile/format support.
- Demand-driven operation graphs suitable for thumbnails, regions and pyramids without decoding every pixel eagerly.
- Multi-language adapter options.
- Selectable build features enabling minimal hardened image-worker images.
- A mature foundation for Creative Studio and document/media image derivatives without making the product editor the core engine.

## Important limitations for Ptah

- Build-time optional dependencies materially change supported formats, behavior, security surface and licences.
- ImageMagick/GraphicsMagick fallback greatly expands hostile-input attack surface and should not be enabled casually.
- PDF/SVG/RAW/HEIC/AVIF support depends on external libraries with their own version/licence/CVE profiles.
- Image metadata can contain sensitive GPS, device, author, profile and thumbnail data.
- EXIF orientation, ICC profiles, alpha, animation/pages and HDR must be preserved or transformed explicitly.
- Pixel-equivalent output may not be byte-identical across encoders/platforms/builds.
- Lossy re-encoding creates a new derivative and cannot preserve original bytes.
- Demand-driven evaluation and internal caching do not replace Ptah Activity/cache/receipt identity.
- Decode/render success does not prove visual correctness.
- Native decoder crashes remain hostile-input risk despite fuzzing.
- Huge dimensions, pathological metadata, decompression bombs and page/frame counts still require Ptah limits.
- LGPL dynamic/static linking and distribution obligations require packaging review.
- libvips does not own editable layer/timeline/project semantics.

## Must not be inherited

- Original image overwritten by normalized/rotated/re-encoded output.
- Optional loaders enabled without capability/licence/security records.
- Metadata stripped or published silently.
- EXIF orientation applied without retaining source/orientation provenance.
- ICC/HDR conversion performed implicitly without color-transform receipt.
- Encoder output treated as byte-deterministic without proof.
- ImageMagick fallback exposed to untrusted input in the control plane.
- libvips cache/operation IDs used as canonical Ptah identities.
- Product-specific Creative Studio layer model forced into all Image Domain Pack work.

## Integration decision

**ADOPT AS THE PRIMARY IMAGE DECODE/TRANSFORM/PREVIEW FOUNDATION CANDIDATE, BEHIND PTAH IMAGE OBJECT/DERIVATIVE CONTRACTS.**

Ptah should use a hardened feature-selected libvips build for metadata, thumbnails, previews, region extraction, resize/crop/rotate, color conversion and image pyramids. Creative Studio remains an editable-product layer over these neutral Facilities.

Specialist adapters may handle formats/features excluded from the hardened base build.

## Native Ptah gap

Ptah must define:

- image detector/format/page/frame/band claim schema;
- dimensions, orientation, alpha, bit depth, color space/profile, HDR and metadata child/view records;
- source metadata privacy/redaction policy;
- transform recipe with crop/resize/interpolation/color/quality/encoder parameters;
- original versus normalized/preview/thumbnail/pyramid derivative relationships;
- page/frame/region identities and hashes;
- build feature/dependency/codec/loader manifest;
- decode pixel/page/memory/time/output budgets;
- deterministic/visual-equivalence classification;
- parser/decoder isolation and crash receipts;
- dynamic-linking/licence package record;
- editable project/Asset adapter for Creative Studio.

## Exit strategy

Ptah's Image Domain Pack can support libvips, Pillow, ImageMagick, platform codecs or specialist medical/scientific libraries. Image Objects and transform recipes remain backend-neutral.

## Validation required

1. Decode representative raster, animated, multi-page, HDR, SVG, PDF-page, RAW and scientific images under declared build capabilities.
2. Preserve original bytes and generate hashed thumbnail/preview/normalized/pyramid derivatives.
3. Verify orientation, alpha, ICC/color and metadata behavior explicitly.
4. Test enormous dimensions, decompression bombs, corrupt metadata and malformed files under resource limits.
5. Compare outputs across two compatible Nodes/builds and classify byte versus visual equivalence.
6. Disable ImageMagick fallback in the hardened worker and prove unsupported formats report missing capability honestly.
7. Strip/redact GPS/private metadata only through an explicit transform recipe.
8. Run native decoders in a bounded provider and survive crashes/timeouts.
9. Record exact libvips/loader/encoder versions and licence obligations.
10. Use the same Image Objects from Creative Studio without copying path-based source truth.
