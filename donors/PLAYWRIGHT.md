# Donor Record — Playwright

**Phase:** 0A / WP08  
**Status:** FIRST-PASS COMPLETE — PRIMARY BROWSER FACILITY FOUNDATION  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/microsoft/playwright
- Default branch: `main`
- Pinned commit: `37b39b798589fcca525cb71ffa1a3191a6d2fd91`
- Licence: Apache-2.0
- Activity: Active
- Classification: cross-browser process/context/page automation, testing and evidence foundation
- Ptah targets: `BROWSE-001`, `BROWSE-002`, `BROWSE-003`, Browser Profile/Context/Page lifecycle, authenticated state, downloads, screenshots, video, trace, console and network evidence

## Files/components inspected

- `README.md`
- core client/server channel definitions and protocol validation locations
- documented Browser, BrowserContext, Page, locator, storage-state, trace, video, screenshot, PDF, route/network and CDP boundaries
- cross-browser and language-binding architecture

## Verified capabilities and patterns

- Drives Chromium, Firefox and WebKit through one API on Linux, macOS and Windows.
- Supports headed and headless execution.
- Distinguishes a browser process from lightweight isolated Browser Contexts and Pages.
- Each test can receive a fresh Context with near-zero isolation overhead.
- Authentication/cookie/local-storage state can be exported and reused through storage-state files.
- Persistent contexts can use a browser user-data directory, while ordinary contexts are ephemeral.
- Locators use role, label, placeholder, test ID and other user-facing semantics with auto-wait/actionability.
- Pages support navigation, frames, popups, downloads, dialogs and network interception.
- Tracing can retain actions, DOM snapshots, network requests, console messages, screenshots and video.
- Library use supports screenshots, PDF generation, device emulation and request routing without requiring the test runner.
- Tests and browser work can execute in parallel.
- Playwright can connect to browser processes and Chromium CDP endpoints rather than always launching a new browser.
- Python, .NET and Java bindings expose the same core browser protocol from other languages.

## What Playwright completes

- The main Browser Facility machinery rather than a one-off web-fetch utility.
- Browser process, isolated Context and Page/Tab separation.
- Reusable authenticated state and persistent profile support.
- Chromium, Firefox and WebKit coverage.
- Downloads, screenshots, video, PDF, trace, network and console evidence.
- Structured locators and accessibility-informed actions.
- Browser-process reuse and parallel Contexts.
- A language-neutral core protocol with several supported bindings.
- Testing, interactive browsing and programmatic extraction under one mature foundation.

## Important limitations for Ptah

- Playwright Browser/Context/Page IDs are backend-local and not Ptah identities.
- Browser Context isolation is strong for cookies/storage but does not automatically prove full OS/network/file/extension isolation.
- Persistent profile directories contain sensitive cookies, credentials, history and extension state.
- One real Chrome profile must not be opened concurrently by unrelated browser processes.
- Exported storage state may omit some browser/profile data and remains sensitive.
- A successful locator action or navigation does not prove intended page outcome.
- DOM/accessibility state is incomplete for canvas, video, custom rendering, cross-origin frames and some browser UI.
- CDP connections are Chromium-specific and can expose broad browser authority.
- Downloads are temporary browser outputs until registered and verified as Ptah Objects.
- Trace/video/screenshots can contain secrets and personal data.
- Browser binaries and exact build versions materially affect behavior.
- Playwright does not own live-search citation, source authority, reasoning or research acceptance.
- Browser challenges, logins, passkeys, MFA and CAPTCHAs may require human/provider completion.

## Must not be inherited

- Browser, Context, Page or locator references as canonical Ptah identity.
- shared persistent profiles across unrelated Workspaces or callers.
- authentication state stored in public files, logs or ordinary Artifacts.
- browser/CDP endpoints exposed directly to untrusted callers.
- page load or click acknowledgement promoted to verified outcome.
- DOM/accessibility snapshot treated as complete visual/source truth.
- browser downloads bypassing Ptah Transfer/Object finalization.
- one browser engine assumed equivalent to all others.
- trace/video evidence retained without privacy/retention policy.
- Playwright Test configuration used as Ptah's universal Browser contract.

## Integration decision

**ADOPT PLAYWRIGHT AS THE PRIMARY BROWSER FACILITY FOUNDATION.**

Recommended architecture:

1. Ptah Browser Provider supervises pinned browser binaries and processes;
2. Browser Profiles own persistent user-data/authentication state;
3. Browser Processes host one or more compatible Contexts;
4. Browser Contexts isolate Workspace/caller sessions;
5. Pages/Tabs/Frames/Popups receive stable Ptah aliases;
6. Downloads route through the Transfer/Object Facility;
7. screenshots, video, trace, network and console become separate Artifacts;
8. Playwright MCP/CLI and Browser-Use remain adapters/callers over the native Browser contract.

## Native Ptah gap

Ptah must define:

- Browser Profile identity, owner, storage, encryption and lease;
- Browser binary/engine/version and Provider capability record;
- Process, Context, Page, Frame, Popup and Download identities;
- connection/generation epoch and stale-page rejection;
- persistent versus ephemeral context rules;
- cookie/storage/extension/credential privacy classification;
- profile cloning, exclusive locking and cleanup;
- navigation/action state and before/after proof;
- download Object landing/finalization;
- screenshot/video/trace/network/console Artifact schemas;
- DOM, accessibility, rendered pixels and source-response as separate Views;
- browser crash/restart and Context/Page recovery;
- resource accounting, pooling and backpressure;
- source/citation and research-result contracts;
- backend/language-binding replacement tests.

## Exit strategy

Ptah's Browser contracts remain implementable through Playwright, native CDP/WebDriver BiDi, browser-specific automation or future engines. Playwright IDs and schemas remain adapter metadata.

## Validation required

1. Run Chromium, Firefox and WebKit under one Browser Facility contract.
2. Run several isolated Contexts concurrently in one process without cookie/storage leakage.
3. Use one persistent authenticated Profile with exclusive lease and safe restart.
4. Clone an approved Profile without copying transient locks or exposing credentials.
5. Recover after browser-process crash and reject stale Page/Frame references.
6. Route a download into Ptah landing storage and independently verify the final Object.
7. Capture screenshot, video, trace, network and console as separately classified Artifacts.
8. Compare DOM, accessibility, source response and pixels and retain disagreements.
9. Reconnect through CDP while preserving Ptah Session identity and advancing backend epoch.
10. Replace Playwright binding/backend without changing Browser Profile/Context/Page identity.
