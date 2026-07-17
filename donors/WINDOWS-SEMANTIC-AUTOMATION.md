# Donor Record — Windows Semantic Automation Composition

**Phase:** 0A / WP07B  
**Status:** FIRST-PASS COMPLETE — NATIVE UIA AND W3C WINDOWS AUTOMATION DONOR SET  
**Inspected:** 2026-07-17

## Identity

### FlaUI

- Canonical URL: https://github.com/FlaUI/FlaUI
- Default branch: `main`
- Pinned commit: `5e364212d4c7f37c68a8ca1016064be37926fb87`
- Licence: MIT
- Runtime: .NET over Microsoft UI Automation UIA2/UIA3

### NovaWindows Appium Driver

- Canonical URL: https://github.com/AutomateThePlanet/appium-novawindows-driver
- Default branch: `main`
- Pinned commit: `cb09b055f9135ab2ee494a7a589a68afb001c9a8`
- Pinned package version: `1.4.1`
- Licence: Apache-2.0
- Runtime: TypeScript/Appium with current PowerShell-based backend

### Appium Windows Driver / WinAppDriver compatibility path

- Canonical URL: https://github.com/appium/appium-windows-driver
- Default branch: `master`
- Pinned commit: `61d6543306f62cb0e541a7e6f4fb5a93a828bd02`
- Pinned package version: `6.0.5`
- Licence: Apache-2.0
- Backend: Microsoft WinAppDriver
- Status: compatibility/legacy path; the driver's current documentation warns that WinAppDriver has not been maintained for years and recommends NovaWindows as a modern replacement

- Classification: Windows native semantic UI, application attach/launch and W3C compatibility donor composition
- Ptah targets: `APP-003`, Windows Application Session, native UI hierarchy, element actions, windows, screenshots/recording and semantic proof

## Files/components inspected

- FlaUI `README.md` and `LICENSE.txt`
- Appium Windows Driver `README.md`
- NovaWindows Driver `README.md` and `LICENSE`
- Appium core donor record from WP07A
- documented UIA2/UIA3, app/window attach, locator, PowerShell and recording boundaries

## Verified capabilities and patterns

### FlaUI

- Wraps Microsoft's native UI Automation APIs.
- Supports Win32, WinForms, WPF and Store/UWP-style applications.
- Exposes both UIA2 and UIA3 because application-framework compatibility differs.
- Can launch, attach to and close applications.
- Resolves the main window and searches/interacts with descendant automation elements.
- Keeps native UI Automation objects available for unsupported or advanced cases.

### NovaWindows

- Supports UWP, WinForms, WPF and Win32 applications through an Appium driver.
- Provides Appium 2/3 compatibility without requiring WinAppDriver.
- Supports application launch, arguments, working directory and attach by top-level window handle.
- Adds RawView access, UI Automation conditions, enhanced text input and window/platform-specific actions.
- Supports WebView/Chromium/Edge contexts with explicit driver-version compatibility responsibilities.
- Supports FFmpeg-based screen recording.
- Current backend uses one persistent PowerShell session; a future .NET backend is planned.
- Project documentation explicitly describes the driver as early and evolving.

### Legacy Appium Windows path

- Proxies WinAppDriver and supports UWP, WinForms, WPF and Win32.
- Supports W3C sessions, app/top-level-window attachment, UIA locators and screen recording.
- Requires external WinAppDriver lifecycle management in modern releases.
- Its own current documentation warns that WinAppDriver is long-unmaintained.
- Arbitrary PowerShell is an opt-in insecure capability.

## What this composition completes

- A direct native Windows UI Automation path through FlaUI.
- A W3C/Appium-compatible semantic path through NovaWindows.
- A legacy WinAppDriver compatibility route for existing clients/workloads.
- Application launch versus attach-to-existing-window distinctions.
- UIA2/UIA3 compatibility selection for different Windows application frameworks.
- Semantic element and window operations independent from RDP pixels.
- Windows recording and WebView-context requirements.

## Important limitations for Ptah

- UI Automation trees may be incomplete for games, custom-rendered surfaces, elevated apps, secure desktops and some legacy controls.
- UIA2 and UIA3 have different bugs/coverage; one cannot be assumed universally superior.
- Automation element/runtime IDs and top-level window handles are process/session-local and can become stale.
- NovaWindows is early-stage and currently depends on a single PowerShell session.
- Arbitrary PowerShell is highly privileged and must not be part of ordinary semantic action permissions.
- Appium Windows/WinAppDriver is a legacy compatibility path, not the preferred future foundation.
- Developer mode/host prerequisites differ by backend.
- WebView driver versions must match installed browser/runtime versions.
- Application launch success does not prove first window, semantic readiness or intended state.
- Windows desktop session isolation, elevation/UAC and user-profile state affect accessibility and control.
- Semantic automation is not a Windows VM/native Node provider and does not supply RDP display.

## Must not be inherited

- window handles, runtime IDs or Appium session IDs as canonical Ptah Application/Window identity;
- legacy WinAppDriver as the sole Windows automation dependency;
- arbitrary PowerShell enabled under generic semantic UI permission;
- one UIA version forced across all application frameworks;
- selector/action acknowledgement promoted to verified state;
- automatic driver/FFmpeg downloads without pinned hashes and caller/provider approval;
- elevated/UAC bypass assumptions;
- semantic hierarchy treated as complete visual truth;
- backend-specific capabilities used as public Ptah schemas.

## Integration decision

**ADAPT FLAUI AS THE PRIMARY DIRECT NATIVE WINDOWS SEMANTIC BACKEND; SUPPORT NOVAWINDOWS AS THE PRIMARY W3C/APPIUM CANDIDATE; RETAIN APPIUM WINDOWS/WINAPPDRIVER AS LEGACY COMPATIBILITY ONLY.**

Recommended architecture:

1. native Windows Node or Windows VM runs a Ptah Windows Application Provider;
2. a .NET/FlaUI Facility supplies direct UIA2/UIA3 semantic context/actions;
3. NovaWindows supplies W3C/Appium interoperability where required;
4. legacy WinAppDriver workloads remain isolated and explicitly marked compatibility mode;
5. FreeRDP/Guacamole supplies pixels/display separately.

## Native Ptah gap

Ptah must define:

- Windows Application Object and Application Session identity;
- process, user session, desktop, window and display records;
- stable selector intent plus backend-specific UIA/Appium compilation;
- UIA2/UIA3/backend capability and application-framework profile;
- stale window/element detection and re-resolution;
- launch, process-ready, first-window, visible-frame and semantic-ready receipts;
- UAC/elevation/session-boundary status;
- input/action before/after verification;
- WebView context and driver-version records;
- PowerShell/shell operation as a separate high-risk Facility;
- screenshot/recording Artifact and privacy metadata;
- backend health, version pinning and replacement tests.

## Exit strategy

Ptah's Windows Semantic Facility remains independent of FlaUI, NovaWindows, WinAppDriver and Appium. Microsoft UI Automation adapters, commercial automation tools or future platform APIs can replace them without changing Application Session, Screen Context or Receipt identity.

## Validation required

1. Launch and attach to Win32, WinForms, WPF and UWP applications.
2. Compare UIA2 and UIA3 coverage and record framework-specific limitations.
3. Resolve and interact with elements through FlaUI and NovaWindows under one normalized Screen Context contract.
4. Destroy/recreate a window and reject stale handles/elements before re-resolution.
5. Distinguish process launched, first window found, visible frame and semantic readiness.
6. Exercise UAC/elevated application boundaries without silently claiming control.
7. Prove arbitrary PowerShell is separately authorized and disabled by default.
8. Record a session and link video/screenshots to exact Application Session and action receipts.
9. Run one legacy WinAppDriver workload without making it the preferred backend.
10. Replace NovaWindows/FlaUI with another adapter without changing public Ptah identities.
