# Internal Recovery Record — App Recover

**Phase:** 0A / WP05  
**Status:** FIRST-PASS COMPLETE — SUBSTANTIAL RECOVERY/DECOMPOSITION PROTOTYPE  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/app-recover`
- Visibility: Private
- Default branch: `main`
- Pinned commit: `b2bae02d0889ed9085535ac9b225ee1435a9d390`
- Commit state: one initial project import at the inspected pin
- Licence: no root `LICENSE` file or normal README was recovered; preserve private/internal status until ownership and extraction terms are documented.
- Ptah relevance: executable/installer detection, payload extraction, static metadata, resource recovery, string/dependency clues, rebuild derivatives and platform-specific recovery.

## Files inspected

- `app_recover_qt.py`
- `POSTPROCESS_EXISTING_RECOVERY.py`
- initial commit contents/diff

## Verified implemented behavior

### Detection and evidence

- Accepts app/installer/package files through browse or drag/drop.
- Detection records file path, extension, primary type, confidence, best method, recovery potential, secondary clues, PE metadata and notes.
- Uses header checks for ZIP, 7-Zip, RAR and PE/MZ content rather than extension alone for several formats.
- Uses `pefile` to record PE architecture, subsystem, entry point, sections and imported DLLs.
- Detects .NET through CLR/COM directory and `mscoree.dll` import evidence.
- Scores multiple installer/application clues rather than returning only one unqualified match.
- Uses embedded markers and 7-Zip listing evidence for Inno, NSIS, SFX, Electron, PyInstaller, AutoIt and UPX-like candidates.
- Separates primary type from secondary clues and records reasons.
- Includes macOS/iOS input detection and explicitly disables Windows Resource Hacker operations for those inputs.

### Recovery output structure

The main recovery Workspace creates named derivative areas including:

- `00_detection`;
- `01_extracted_payload`;
- `02_strings`;
- `03_resources`;
- `04_dotnet_source`;
- `05_dependencies`;
- `06_rebuild_prep`;
- `07_builder_recovery`;
- `08_rebuild_workspace`;
- `12_rebuild_artifacts`;
- `13_remote_dependency_recovery`;
- platform-specific macOS/iOS recovery output where applicable.

A full tree report and operation log are created.

### Extraction and static recovery

- Runs 7-Zip extraction/listing for supported packages and self-extracting executables.
- Performs a printable-string sweep and stores recovered text.
- Can use Resource Hacker for Windows resources and icons.
- Can use 7-Zip as a PE/resource fallback.
- Can use `ilspycmd` for .NET project/source recovery where .NET is detected.
- Copies the original input into recovery output rather than discarding it.
- Scans extracted payloads for source, scripts, configs, databases, assets, native dependencies and installer project files.
- Categorizes rebuild-value files into source, Python, .NET, Qt, Electron/web, installer, command, config/database, asset and driver/dependency folders.
- Marks high-value project/source artifacts such as `.csproj`, `.ui`, `.qrc`, `.pro`, `.qml`, `.iss`, `.nsi`, `.asar`, scripts and databases.

### Rebuild derivatives

- Produces a project-type guess, recovery score, recovery route and explicit notes on what can/cannot normally be recovered.
- Generates feature, command, UI, dependency and remote-download clue maps.
- Filters many binary/debug/runtime strings away from human action maps.
- Creates an editable PySide6 rebuild skeleton from recovered tabs, features and UI/action clues.
- Produces an app blueprint JSON and Markdown/text rebuild guides.
- Separates original/recovered assets from derived rebuild Workspace files.
- Extracts URL, endpoint, package filename, runtime dependency, device-pack and function-to-download clues.
- States explicitly that native C++/Qt source is not magically recreated and that recovered evidence may only support a manual rebuild.

### Execution/UI behavior

- Detection and recovery use Qt worker threads so the main UI is not intentionally blocked by all work.
- Subprocess output is streamed into the UI log and recovery log.
- macOS/iOS fast paths skip incompatible Windows-only steps.
- The original input and generated recovery folders remain inspectable after completion.

## Strong internal patterns for Ptah

1. Preserve the original input and create derivatives rather than replacing it.
2. Detection produces evidence, confidence, competing clues and a recommended parser/route.
3. Type detection and recovery depth are separate operations.
4. Unsupported/partial source recovery is described honestly.
5. Recovery output is organized by purpose and rebuild value, not only file extension.
6. Static analysis, extracted payload, source derivatives, assets, dependencies and rebuild plans remain separate.
7. Platform-incompatible tools are explicitly skipped.
8. Tool availability changes recovery coverage and should be recorded.
9. A rebuild Workspace is a derivative/blueprint, not proof of original source recovery.
10. Remote dependency clues are useful child evidence but not automatically trusted downloads.
11. Binary-noise filtering and human-action maps should remain separate views of the same recovered evidence.
12. Original artifact, extracted child files, reports and generated skeletons need different Object relationship types.

## Important limitations

### Object and provenance gaps

- Files and directories are copied into named folders but are not registered as immutable Ptah Objects with hashes, parent/child relationships and producing Activities.
- Reports do not consistently retain exact tool version, command, exit status, content hashes or per-child provenance.
- Copy failures and many secondary processing failures are logged or silently ignored without typed receipts.
- Duplicate recovered files are organized by paths/extensions rather than content identity.
- The generated PySide6 skeleton is a heuristic derivative and could be mistaken for recovered source without stronger relationship labels.

### Detection gaps

- Detection combines useful signatures with heuristic whole-file substring searches and fixed scores.
- Extension is authoritative for MSI before parser verification.
- The entire input is read into memory for detection and string extraction, which is unsafe for very large files.
- Confidence values are hand-tuned scores rather than calibrated detector confidence.
- PE metadata is limited compared with LIEF and specialist signature/resource tooling.
- No generalized MIME/container detector, parser consensus or detector-conflict schema exists.
- Encrypted, malformed, truncated, polyglot and intentionally adversarial files are not modeled as first-class states.

### Decomposition safety gaps

- 7-Zip extraction is shallow from the initial input; recursive child-archive decomposition is not a native bounded graph operation.
- No extraction budget exists for recursion depth, expanded bytes, child count, CPU/time, path length or compression ratio.
- Archive path traversal, symlink/device-file handling and output-root containment rely mainly on external tool behavior.
- The code scans/copies many extracted files without explicit maximum counts/bytes.
- Remote URLs/endpoints are recovered as clues but no safe fetch/verification contract is attached.

### Runtime gaps

- The application is Windows/path specific (`D:\projects`, Desktop output and Windows tool locations).
- Shell commands are constructed as strings and run with `shell=True`.
- Cancellation, durable Activity state, restart recovery and worker leases are absent.
- Subprocesses have inconsistent timeouts and no neutral Facility capability contract.
- UI/source contain repeated/duplicated sections and repeated timer initialization, indicating patch accumulation.
- Several helper capabilities appear duplicated between the main file and postprocessor, increasing drift risk.
- Many `except Exception: pass` paths hide lost evidence.
- Output folder naming is user/path based rather than stable Object/Activity identity.
- No root licence is present.

## What Ptah should reuse or adapt

- evidence-bearing detector claims with primary and secondary candidates;
- immutable-original and derivative-first workflow;
- recovery-level and honest limitation language;
- purpose-specific views for strings, resources, dependencies, source, assets, remote clues and rebuild guides;
- platform/tool capability routing;
- high-value rebuild-artifact classification;
- static-only safe default for executables/installers;
- original versus extracted versus generated-skeleton relationship distinction;
- child evidence useful for later Build/Facility routing;
- background Activity and progressive-output requirements.

## What Ptah must not inherit

- product/brand identity in public Object/Domain Pack contracts;
- hard-coded local paths and Desktop output;
- whole-file reads for arbitrary-size Objects;
- heuristic score as authoritative file type;
- `shell=True` string commands;
- unbounded archive extraction;
- folder names as Object identity;
- copy success as provenance proof;
- generated rebuild skeleton presented as recovered original source;
- silent exception handling;
- private/unlicensed source copied into public Ptah.

## Classification

**ADAPT DETECTION/RECOVERY UX, OUTPUT TAXONOMY AND REBUILD-DERIVATIVE PATTERNS; REBUILD AS PTAH DOMAIN PACKS OVER MATURE PARSERS.**

App Recover is strong internal evidence for `CORE-003`, `DECOMP-001`, `DECOMP-002`, `BIN-001`, parts of `APP-001`, `CORE-004`, `OBS-001` and `PROV-001`. It remains a specialist product/caller rather than Ptah Core.

## Native Ptah completion required

- universal Object/relationship graph and content hashes;
- detector claim schema with evidence, confidence and parser/version identity;
- progressive detection/decomposition depth;
- bounded recursive extraction service;
- LIEF/Binwalk/libarchive and platform-specific adapters;
- per-child Object registration and deduplication;
- typed unsupported/encrypted/malformed/truncated/polyglot states;
- operation receipts and exact subprocess/tool identity;
- safe argument arrays and sandbox/provider execution;
- cancellation, restart recovery and resource accounting;
- preview/view/derivative contracts;
- remote clue Objects kept separate from verified fetched dependencies;
- calibrated and testable detection rules;
- public/private extraction and licence decision.

## Validation inherited into Ptah

1. Preserve the input Object unchanged and hash every generated child/derivative.
2. Feed mislabeled, malformed, encrypted, polyglot and very large inputs; retain conflicting detector claims honestly.
3. Recursively decompose nested archives under explicit depth/byte/count/time limits.
4. Reject path traversal, symlink escape, device files and decompression-bomb expansion.
5. Run PE/.NET/installer/Electron/PyInstaller/macOS samples through specialist adapters and compare claims.
6. Prove tool absence changes coverage status rather than producing false success.
7. Bind rebuild plans/skeletons as `derived_blueprint`, never `recovered_original_source`.
8. Retain per-child source offsets/path, tool version, command, exit code and parent relationship.
9. Cancel/restart a long decomposition Activity without losing completed child Objects or duplicating outputs.
10. Run two unrelated decompositions concurrently without blocking other Workspace Activities.
