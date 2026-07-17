# Internal Recovery Record — THETECHGUY Software Builder

**Phase:** 0A / WP02C  
**Status:** FIRST-PASS COMPLETE — IMPLEMENTATION REQUIRES MAJOR COMPLETION  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/thetechguy-software-builder`
- Visibility: Private
- Default branch: `main`
- Pinned commit: `54c532c7b77ef8467ea9fba3efce87077cff70d9`
- Repository history at pin: one large initial commit
- Licence: No root licence was recovered; preserve private/internal status until ownership and extraction terms are documented.
- Ptah relevance: shared build environments, project scanning, build plans, background-worker requirements, logs, cancellation, dependency/tool health and artifact boundaries.

## Files inspected

- initial commit and repository contents
- `PROJECT_RULES_FOR_AI.md`
- `build.ps1`
- `scripts/create_project_build_plan.ps1`
- `scripts/scan_project_code_level.ps1`

No ordinary root `README.md` was found through the repository contents API during this pass.

## Verified implemented behavior

### Shared-environment rules

- Project repositories are intentionally kept free of duplicated SDKs, virtual environments, package caches, installer engines and temporary build workspaces.
- Projects retain source, project resources, `techguy-build.json`, a small launcher, final outputs and project-specific logs.
- Shared build tools, caches, dependencies, installer templates and temporary work remain in the Builder.
- Secrets and activation/provider credentials must not be hard-coded into project files, logs or installer assets.

### Build entry and planning

- `build.ps1` accepts a selected Project root and modes for scan, initialize, resources, plan, build, installer and full.
- Required scripts are checked before work proceeds.
- A run ID and JSON report path are generated.
- Project scanning, resource validation and build-plan generation are chained through JSON output.
- Warnings and next actions are recorded rather than hidden.
- Build reports retain Project, mode, scanner evidence, resource state, target plan, warnings and next actions.

### Project scanner

- Recursively scans source while excluding generated/cache directories inside the selected Project.
- Detects Python, Qt, Tkinter, Electron, Node, Android Gradle, Flutter, .NET and macOS/Swift signals.
- Inspects up to 250 code files for entry points and framework/code patterns.
- Records evidence paths and reasons for detected project types.
- Identifies likely target outputs and missing resource/config requirements.
- Produces a structured JSON scanner report.

### Build planner

- Uses a target registry, host platform, tool-health log, resource state and Project config.
- Selects suggested targets and records required/recommended tools, missing tools, output folder and blocked reasons.
- Detects host-platform incompatibility and missing required tools.
- Writes Project build plan plus Builder log copy as JSON.

## Explicitly documented but not implemented

The inspected `build.ps1` explicitly states that build and installer execution are not enabled in this integration foundation and would be routed to target-specific scripts in later patches.

Therefore the repository is not a completed universal Build Facility. It is currently strongest as:

- design rules;
- scanner/planner prototype;
- dependency/readiness model;
- shared-cache/environment direction;
- UI/background-worker requirements.

## Strong internal patterns for Ptah

1. Shared environments and caches must not be copied into every Project.
2. Active work, shared machinery and final Project outputs have different storage classes.
3. Project scan evidence and reasons should be retained.
4. Build target availability and blocked reasons are explicit.
5. Tool/dependency health is a first-class input to planning.
6. Heavy work must leave the UI thread and provide logs, progress, cancellation/request-stop and status.
7. Planning and readiness should occur before expensive execution.
8. User correction/override exists when automatic detection is wrong.
9. Critical dependencies cannot be silently skipped.
10. Reports and outputs are separate from source Projects.

## Important limitations

- Actual build/installer execution is not enabled in the inspected central entry.
- Background-worker requirements are documented more strongly than a general durable worker implementation is proven.
- Scanner rules are heuristic and use `SilentlyContinue`, risking hidden read/parse failures.
- The scanner limits code inspection to the first 250 selected files.
- Project and run identifiers are path/time based rather than durable Ptah identities.
- Build reports are local files without a universal Object/Artifact catalogue.
- Windows paths, PowerShell and local Builder-root assumptions are deeply embedded.
- Target execution, cache integrity, concurrency, restart recovery and cross-Node placement are not yet a neutral implementation.
- One large initial commit makes component history and maturity difficult to distinguish.
- Product-specific branding, installer rules and private release behavior cannot enter public Ptah Core.

## What Ptah should reuse or adapt

- shared toolchain/cache and clean-Project principle;
- scanner evidence and explicit readiness/blocked-reason model;
- target/capability registry ideas;
- project manifest import concepts;
- tool-health and dependency checks;
- background-worker, progress, cancellation and status requirements;
- report-to-Object/Artifact conversion;
- safe separation of Project source, active workspace, caches and final outputs.

## What Ptah must not inherit

- The current Builder as the universal Build Facility.
- Hard-coded Windows/local paths or one host platform.
- Heuristic detection treated as authority without confidence/evidence.
- Silent error suppression.
- Product branding and installer policy in the public Ptah contract.
- A single process/PowerShell script as durable Activity orchestration.
- Build-plan existence presented as completed build capability.
- Local report files without content hashes and provenance.

## Classification

**ADAPT REQUIREMENTS AND SELECTED SCANNER/PLANNER PATTERNS; REBUILD THE NEUTRAL EXECUTION LAYER.**

Software Builder is internal evidence for `CORE-002`, `CORE-004`, `EXEC-001`, `EXEC-003`, `STORE-001`, `OBS-001` and `PROV-001`. It will later be compared with BuildKit and Dagger. It is not the selected Ptah build engine.

## Native Ptah completion required

- versioned Build Recipe/Facility contract;
- BuildKit/Dagger and native tool adapters;
- durable concurrent Activities with streaming logs and cancellation;
- shared cache identities and integrity;
- provider/Node placement and platform capability matching;
- Object/Artifact registration and hashes;
- reproducible environment/image/tool identities;
- restart/retry semantics;
- public-neutral manifests separated from private branding/signing adapters;
- confidence and failure reporting for scanners.

## Validation inherited into Ptah

- two Projects share tool/cache machinery without sharing mutable Workspaces;
- heavy builds do not block the human interface or unrelated Activities;
- cancel/request-stop leaves explicit partial outputs and state;
- missing tools block only affected targets and name the reason;
- scanner evidence can be reviewed and corrected;
- exact environment/tool versions and Artifact hashes are retained;
- a Build plan is never reported as a completed Build;
- restart recovery does not duplicate side effects or corrupt caches.
