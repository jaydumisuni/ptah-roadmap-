# Internal Recovery Record — APK Extractor

**Phase:** 0A / WP05  
**Status:** FIRST-PASS COMPLETE — WORKING APK DECOMPOSITION ORCHESTRATOR  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/apk-extractor`
- Visibility: Private
- Default branch: `main`
- Pinned commit: `e389851e430a64476e1c6e2522750c372cad6b4e`
- Commit state: one initial project import at the inspected pin
- Licence: no root `LICENSE` file or normal README was found; preserve private/internal status until ownership and extraction terms are documented.
- Ptah relevance: APK intake, raw package extraction, resource/smali recovery, Java-source derivatives, tool orchestration and Android application Domain Pack requirements.

## Files inspected

- `apk_extractor_qt.py`
- `build-thetechguy-installer.ps1`
- initial commit contents/diff, including the earlier CLI/one-click extraction implementation

## Verified implemented behavior

### Intake and UI

- PySide6 desktop UI supports browse and drag/drop for `.apk` files.
- Output is written beneath a dedicated extraction root with a caller-selected safe folder name.
- Existing extraction folders are not intended to be overwritten silently; the project includes output-name collision handling in its one-click source history.
- Tool installation/check and extraction run on worker threads rather than the main UI thread.
- Live subprocess output is streamed to the UI and an extraction log.

### Tool discovery and setup

- Detects/configures JDK 17, Apktool and JADX on Windows.
- Can install/check tools through `winget`.
- Records Java, Apktool and JADX paths/versions in execution output/logs.
- Uses application-relative resources when packaged by PyInstaller.

### APK decomposition

A normal extraction performs three distinct views:

1. **Apktool output** — decoded resources, manifest and smali-oriented project structure.
2. **JADX output** — Java-like source and JADX resources/output.
3. **Raw APK output** — ZIP-level package contents.

It then creates separate tree reports for each view and a complete extraction tree.

### Execution behavior

- Apktool is invoked before JADX; non-zero tool results stop the pipeline with an explicit error.
- Old `apktool`, `jadx` and `raw_apk` derivative folders are removed before a new extraction into the selected output.
- The original APK is copied to a `base.zip` derivative for raw ZIP extraction.
- Logs retain input path, output path, timestamps, tool output and completion/failure information.
- Generated installer packaging is separate from extraction behavior.

## Strong internal patterns for Ptah

1. One application package should expose several complementary views rather than one supposed canonical decompilation.
2. Raw package bytes, decoded resources/smali and Java-like source are distinct derivatives.
3. Tool availability/version is part of the extraction evidence.
4. Tool failures are explicit and stop dependent later work.
5. A background Activity with streamed logs is required for APK decomposition.
6. Existing output should not be overwritten silently.
7. Extraction trees are useful views but are not the same as semantic application inventory.
8. Specialist external tools remain responsible for their own decoding rather than reimplementing Apktool/JADX in the product UI.
9. The original package must remain preserved while all decoded/decompiled results are derivatives.
10. Different decompilers may disagree; Ptah must retain tool-specific provenance.

## Important limitations

### Android semantic gaps

- The current pipeline does not create a normalized package/application record containing package ID, version, SDK levels, permissions, activities, services, receivers, providers, intent filters or exported-component risk.
- AndroidManifest output is produced through tools but is not parsed into typed Objects/relationships.
- DEX files/classes/methods, native libraries/ABIs, resources, assets and certificates are not registered as semantic child Objects.
- APK signing certificates, signing schemes, signer lineage and signature verification are not inspected.
- No mapping links a JADX class back to exact DEX/method/offset evidence.
- Decompiler warnings, skipped classes and approximation quality are not represented as coverage fields.

### Format coverage gaps

- Intake is extension-gated to `.apk` and does not cover AAB, APKS, XAPK, APKM, split/base APK sets or installed-device package extraction.
- No bundletool/aapt2/apksigner integration is present.
- Multidex, resource-table variants, dynamic features and configuration splits are not modeled explicitly.
- No comparison/diff or deterministic rebuild/sign/install proof exists.

### Safety and scaling gaps

- Raw extraction uses `zipfile.extractall` without an explicit path-traversal, symlink, expanded-byte, child-count or compression-ratio budget.
- Apktool/JADX run directly on the host rather than in a bounded Workspace/Provider sandbox.
- Commands are string-built and executed with `shell=True` in the Qt application.
- Tool installation through `winget` is mixed into the application and is Windows/admin/network dependent.
- No cancellation, timeout, durable Activity state, worker lease or restart recovery is implemented.
- Output paths/folders are not content-addressed and no child hashes are generated.
- Old derivative folders are removed before the new run is proven successful, so earlier evidence can be lost.
- No disk-space estimate, output quota or huge-APK protection is present.

### Provenance and product boundaries

- Extraction logs do not consistently record exact binary hashes, tool package digests, environment identity or per-child provenance.
- A successful JADX/Apktool process is not proof of complete/correct source recovery.
- Decompiled Java is a generated view and must never be described as original source.
- Raw extracted files, decoded files and decompiled files may duplicate the same logical content without content-based deduplication.
- The project is Windows/product branded and has no public reuse licence at the inspected pin.

## What Ptah should reuse or adapt

- three-view APK decomposition: raw, resource/smali and Java-like source;
- background execution with streamed logs;
- explicit tool/version discovery and coverage status;
- separate derivative roots per decoder;
- preservation of the original package;
- output-collision and overwrite caution;
- specialist-tool adapter model;
- tree/file views as secondary representations;
- explicit failure when required tools are missing or fail.

## What Ptah must not inherit

- product branding in public Domain Pack contracts;
- `.apk` extension as sufficient package verification;
- raw `extractall` without containment/budgets;
- `shell=True` command strings;
- decompiled Java labeled as recovered original source;
- local output folders as Object identity;
- deleting prior derivatives before transactional replacement;
- Windows-only tool installation in the neutral Facility;
- process exit code as complete semantic/proof success;
- private/unlicensed source copied into public Ptah.

## Classification

**WRAP THE INTERNAL PRODUCT AROUND PTAH LATER; ADAPT ITS MULTI-VIEW WORKFLOW; USE APKTOOL/JADX AS MATURE FACILITY BACKENDS.**

APK Extractor is strong internal evidence for `APP-001`, `CORE-003`, `DECOMP-002`, `CORE-004`, `OBS-001` and `PROV-001`. The application remains a specialist product/caller, while Ptah owns the neutral Android Application Domain Pack.

## Native Ptah completion required

- Android package detector and container classification;
- AAB/APKS/split-package support through bundletool and related adapters;
- normalized manifest/component/permission/SDK model;
- APK signing certificate and scheme verification;
- DEX/class/method and source-view relationships;
- resource table, assets and native ABI/library child Objects;
- per-view coverage, warnings and approximation level;
- safe bounded ZIP extraction;
- immutable original and hashed child/derivative Objects;
- cancellation, durable recovery, quotas and resource accounting;
- exact tool/environment/command receipts;
- comparison and rebuild/sign/verify/install stages kept separate;
- provider-neutral execution and public/private licence separation.

## Validation inherited into Ptah

1. Preserve one APK as immutable original and generate raw, Apktool and JADX derivatives with exact tool provenance.
2. Parse package/manifest/components/permissions into typed Objects and relationships.
3. Verify v1/v2/v3/v4 signing evidence and signer identity where present.
4. Process multidex, native-library and resource-heavy APKs while retaining coverage warnings.
5. Process AAB/APKS and split APK sets without pretending one file is the whole installed application.
6. Reject ZIP traversal, symlink escape and decompression-bomb inputs under explicit budgets.
7. Demonstrate JADX failure/partial output without losing successful raw/Apktool derivatives.
8. Bind Java-like source as `decompiled_view`, never `original_source`.
9. Cancel/restart a long package decomposition without duplicating child Objects.
10. Rebuild/sign a selected derivative and prove that rebuilt package identity differs from the original while relationships remain explicit.
