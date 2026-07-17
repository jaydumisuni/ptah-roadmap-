# Donor Record — JADX

**Phase:** 0A / WP05  
**Status:** FIRST-PASS COMPLETE — ANDROID SOURCE-VIEW DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/skylot/jadx
- Default branch: `master`
- Pinned commit: `dba5f4d33fd4d0c2c18f696ab3a0e238100140bc`
- Licence: Apache-2.0
- Runtime baseline: Java 11+ for released usage; JDK 17+ for source builds at the inspected pin
- Activity: Active
- Classification: DEX/Android bytecode decompiler, source/resource/search/call-graph view donor
- Ptah targets: Java-like code derivatives, class/method navigation, deobfuscation mappings, control/call graphs and source-view coverage

## Files/components inspected

- `README.md`
- documented CLI/GUI, library, input formats, decompilation modes, JSON output, plugins, checksum verification, call/control graphs and deobfuscation mappings

## Verified capabilities and patterns

- Decompiles Dalvik bytecode into Java-like source from APK, DEX, AAR, AAB and ZIP inputs.
- Current CLI input coverage also includes class/JAR, smali, ARSC, XAPK and APKM.
- Decodes AndroidManifest/resources in addition to source views.
- Includes deobfuscation and mapping support.
- GUI provides syntax highlighting, declaration navigation, usage search, full-text search and smali debugging.
- Can be embedded as a Java library.
- Separates source and resource output directories.
- Can emit Java or JSON output.
- Offers decompilation modes:
  - restructure/normal source-like output;
  - simple linear output with gotos;
  - fallback/raw instructions.
- Can show inconsistent/bad code instead of hiding it.
- Supports debug-line comments, access-modifier preservation, inlining/restoration controls, Unicode escaping and renaming controls.
- Can emit method control-flow and application call graphs.
- Supports several mapping formats and auto-generated deobfuscation maps.
- DEX input verifies checksums by default.
- Plugin architecture exposes input and metadata extensions.
- Thread count is configurable.
- Project documentation explicitly warns that 100% decompilation is generally impossible and errors are expected.

## What JADX completes

- Java-like class/method views missing from Apktool's smali/resource focus.
- Multiple decompilation modes for graceful fallback when high-level restructuring fails.
- Search/navigation/call/control graph derivatives.
- Deobfuscation mapping views and reversible alias evidence.
- Broader Android package input formats than the internal APK Extractor currently accepts.
- Programmatic/library integration rather than only CLI output.
- Explicit bad-code/error visibility that Ptah can preserve as coverage evidence.

## Important limitations for Ptah

- Decompiled Java/Kotlin-like output is an approximation and is not original source.
- Some methods/classes will fail, be incomplete or be semantically reconstructed incorrectly.
- Obfuscation, optimizations, reflection, dynamic loading, native code and generated code reduce recoverability.
- Decompiled source does not preserve original formatting, comments, build files, resources or exact names unless debug/mapping evidence exists.
- Deobfuscation aliases are derived views and can change with configuration/version.
- Exported Gradle projects are generated rebuild aids, not original projects or guaranteed compilable builds.
- Call graphs/control-flow graphs are static analysis views and may miss dynamic behavior.
- Plugins execute code and require explicit Facility/plugin trust/version control.
- GUI caches/config/project files may contain source paths or sensitive application data.
- Input/resource handling remains hostile-input attack surface requiring provider isolation and budgets.
- Tool thread defaults/resource use may overwhelm a Node on very large applications.
- JADX does not verify APK signatures, installed split completeness or application runtime correctness.
- Main/nightly behavior may change; Phase 0C must pin a stable release/package.

## Must not be inherited

- Decompiled output labeled `original_source`.
- Successful process exit interpreted as complete decompilation.
- Failed/inconsistent methods silently omitted from coverage reports.
- Deobfuscated aliases treated as authoritative original names.
- Exported Gradle project treated as original Build Recipe.
- Plugins downloaded/executed implicitly.
- GUI/cache paths used as Ptah Object identity.
- Static call graph interpreted as observed runtime behavior.
- Full application trusted/safe because DEX checksum passed.
- Main/nightly schemas exposed as public Ptah contracts.

## Integration decision

**ADOPT AS THE PRIMARY JAVA-LIKE AND STATIC CODE-VIEW BACKEND FOR THE ANDROID APPLICATION DOMAIN PACK.**

Ptah should invoke JADX in bounded headless/library mode and register:

- package/class/method/field views;
- Java-like source files;
- raw/fallback instruction views;
- warnings/errors and coverage;
- deobfuscation mappings;
- call/control graphs;
- decoded resource/manifest views where useful.

Apktool remains the primary smali/resource/rebuild backend. LIEF adds DEX/OAT/VDEX/ART structural views. Ptah owns cross-tool identity and consensus.

## Native Ptah gap

Ptah must define:

- DEX/class/method/field identities tied to source Object/dex/checksum;
- source-view relationship and approximation level;
- method/class success, warnings, inconsistent/bad and skipped coverage states;
- mapping/alias provenance and reversible names;
- source line/debug/bytecode offset relationships;
- call/control graph derivative schema;
- plugin/version/configuration manifest;
- resource/time/memory/thread limits;
- exact stable JADX build/version receipt;
- output hashes and deduplication;
- comparison across decompilation modes/tools;
- privacy and access control for recovered code.

## Exit strategy

Ptah's Android code-view contract can support JADX, CFR/Fernflower-like Java tools, smali/baksmali, LIEF or other decompilers. Decompiled child/view identities remain independent of JADX file paths.

## Validation required

1. Decompile representative APK, multidex, AAB, XAPK and APKM inputs.
2. Preserve method/class-level success/error/coverage and compare restructure, simple and fallback modes.
3. Link source lines and graph nodes back to exact DEX/class/method/bytecode evidence where possible.
4. Test obfuscated, Kotlin, reflection-heavy, native-heavy and malformed applications.
5. Keep deobfuscation aliases/mappings as derived reversible views.
6. Compare JADX source/resource claims with Apktool, LIEF and raw package contents.
7. Run in a bounded provider with cancellation, timeout and memory/thread limits.
8. Disable unapproved plugins/network access and pin exact tool build.
9. Export a Gradle project and prove it remains a generated derivative requiring independent build verification.
10. Never promote decompiled output to original-source or runtime-behavior proof.
