# Donor Record — Apktool

**Phase:** 0A / WP05  
**Status:** FIRST-PASS COMPLETE — ANDROID RESOURCE/SMALI/REBUILD DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/iBotPeaches/Apktool
- Default branch: `main`
- Pinned commit: `d6ab7c3a3f202fc6a787177b17b17201dbf2aedb`
- Branch generation: Apktool 3.x
- Licence: Apache-2.0
- Activity: Active; 2.x remains a separate maintenance branch
- Classification: Android package resource/smali decoding and rebuild-oriented project donor
- Ptah targets: AndroidManifest/resources decoding, smali output, raw/original/unknown file preservation, compression metadata and rebuilt APK derivatives

## Files/components inspected

- `README.md`
- `brut.apktool/apktool-lib/src/main/java/brut/androlib/ApkDecoder.java`
- documented decode/build, resource, smali/baksmali and project-like output boundaries

## Verified capabilities and patterns

- Decodes Android application resources into a near-original editable form.
- Converts DEX source content to smali through a dedicated decoder.
- Decodes resources and AndroidManifest separately.
- Can copy DEX/resources/manifest raw when configured not to decode them.
- Uses configurable parallel background jobs for source decoding and propagates the first worker error.
- Copies original package files separately.
- Copies raw standard directories while excluding already-decoded content.
- Preserves unrecognized/non-standard files in an `unknown` area.
- Records package/build metadata in an Apktool project information file.
- Records which files/extensions were uncompressed in the original package for rebuild behavior.
- Rejects an existing output directory unless force mode is selected.
- Can rebuild decoded projects after modifications.
- Maintains Android-framework/resource handling required for decoding vendor/framework references.
- Closes workers and input resources in finalization paths.

## What Apktool completes

- Stable decoded-resource/manifest and smali views for APKs.
- A rebuild-oriented project structure.
- Preservation of original and unknown package files.
- Compression-state evidence needed to create a structurally similar rebuilt package.
- Parallel multidex/source decoding.
- A useful low-level counterpart to JADX's approximate Java-like output.
- Existing internal APK Extractor integration can be retained behind a neutral Ptah adapter.

## Important limitations for Ptah

- “Nearly original” resources do not mean original source/project identity or byte-perfect round trip.
- Smali is a derived assembly view, not the original Java/Kotlin source.
- Rebuilt APKs normally differ in bytes and require signing; original signatures are invalidated by modification.
- Resource IDs/names may be incomplete or depend on external framework files.
- Vendor/framework resource packages create dependency/version requirements.
- Unknown files are preserved by path but need content-addressed identity and semantic classification in Ptah.
- Output directories are mutable project views, not immutable Objects.
- Forced decoding removes an existing output tree, which can destroy prior evidence unless Ptah versions it.
- Apktool does not verify package signing trust, split-set completeness or runtime behavior.
- It is not a high-level source decompiler or code-understanding engine.
- Host execution of hostile packages and resource decoders requires isolation and resource limits.
- Rebuild success does not prove installability, semantic equivalence or safe behavior.
- Main 3.x branch and 2.x maintenance behavior differ; a stable release/version must be selected for implementation.

## Must not be inherited

- Apktool output described as the original Android project/source.
- Rebuilt package allowed to overwrite or inherit the original Object identity.
- Original signature/trust state retained after mutation.
- `force` deletion of prior output without Ptah revisions/checkpoints.
- Framework files installed globally without exact identity and scope.
- Unknown files omitted because they were not decoded.
- Build/decode exit code used as complete package verification.
- Output path/project filenames used as canonical child identity.
- Decoding performed inside the long-lived control plane with unbounded host access.

## Integration decision

**ADOPT AS THE PRIMARY RESOURCE/SMALI/REBUILD BACKEND FOR THE ANDROID APPLICATION DOMAIN PACK.**

Ptah should register separate views and children for:

- raw package entries;
- decoded manifest/resources;
- smali per DEX;
- original package metadata/files;
- unknown/unclassified entries;
- Apktool project metadata;
- rebuilt package derivatives.

JADX supplies Java-like source, call/control graph and deobfuscation views. LIEF supplies DEX/OAT/VDEX/ART structure. Android signing tools and bundletool complete verification and split/bundle behavior.

## Native Ptah gap

Ptah must define:

- package/manifest/resource/DEX/ABI/certificate child Object model;
- raw, decoded, smali, Java-like and rebuild-project relationship types;
- framework package identity/version/hash and credential/source records;
- per-file compression/method/path/hash metadata;
- unknown-file preservation and later routing;
- exact Apktool configuration/version/environment receipt;
- output coverage/warnings/errors;
- mutation/rebuild Activity with before/after revisions and invalidated-signature status;
- signing, alignment, install and runtime verification as separate operations;
- safe package extraction budgets and provider isolation;
- stable release selection and 2.x/3.x compatibility handling.

## Exit strategy

Ptah's Android resource/smali contract can use Apktool, aapt2, baksmali/smali, bundletool or future specialist adapters. Child Object identities and package relationships do not depend on Apktool output paths.

## Validation required

1. Decode manifest, resources, multidex smali, original and unknown files from representative APKs.
2. Retain exact original package, entry hashes/compression and framework dependencies.
3. Compare Apktool manifest/resources with JADX, raw ZIP and aapt2/bundletool outputs.
4. Decode packages requiring vendor/framework resources and reject ambiguous/missing framework identity.
5. Modify a versioned copy, rebuild, align and sign as separate Activities.
6. Prove rebuilt bytes/signature/Object identity differ from the original even when semantically similar.
7. Test malformed, resource-obfuscated, split-derived and very large packages in bounded execution.
8. Preserve successful partial views when one DEX/resource decode fails.
9. Install/run only through an explicitly selected Android runtime and retain separate runtime proof.
10. Upgrade between stable Apktool versions while preserving public Ptah schemas and comparing output differences.
