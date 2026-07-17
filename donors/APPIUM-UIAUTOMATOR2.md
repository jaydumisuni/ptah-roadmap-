# Donor Record — Appium UiAutomator2 Driver

**Phase:** 0A / WP07  
**Status:** FIRST-PASS COMPLETE — PRIMARY ANDROID SEMANTIC APPLICATION-AUTOMATION BACKEND CANDIDATE  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/appium/appium-uiautomator2-driver
- Default branch: `master`
- Pinned commit: `5e7f19e70caa31851f620b1381509d442c4854ac`
- Pinned package version: `8.1.0`
- Licence: Apache-2.0
- Primary language/runtime: TypeScript driver plus Android UiAutomator2 instrumentation server
- Activity: Active
- Compatibility: driver major 5+ requires Appium 3; inspected version depends on Appium 3 and UiAutomator2 server 10.2.1
- Classification: Android native/hybrid/web semantic automation backend
- Ptah targets: `DEVICE-002`, Android Application Session, element tree, semantic find/action, app lifecycle, screenshots, context switching and session cleanup

## Files/components inspected

- `README.md`
- `package.json`
- `docs/architecture.md`
- `lib/driver.ts`

## Verified capabilities and patterns

### End-to-end architecture

- W3C client commands arrive at Appium core and are forwarded to the UiAutomator2 driver.
- The driver uses ADB/platform tools for install, shell and port forwarding.
- A device-side UiAutomator2 instrumentation server exposes an HTTP API.
- The server uses Google's UiAutomator framework and accessibility tree to interact with the application under test.
- Hybrid/WebView contexts are proxied through managed Chromedriver sessions.

### Exact target and session setup

- Supports real devices and emulators on Linux, Windows and macOS hosts.
- Requires Android platform tools, JDK and exact environment setup.
- Current major supports Android API 26+; older driver versions covered earlier APIs with different compatibility.
- `udid` is the exact real-device selector and is explicitly recommended for parallel sessions.
- `deviceName` is not used to select the device.
- If `udid` is absent the driver may autodetect/choose a device; this is unacceptable for Ptah multi-device execution.
- Allocates a host system port, normally from 8200–8299, for the device server and recommends explicit ports for parallel sessions.
- Claims the active session/UDID before creating the ADB instance and starting the server.

### Server/helper lifecycle

- Installs/checks the UiAutomator2 server unless explicitly skipped.
- Exposes separate install, launch and read timeouts.
- Can validate prerequisites through an Appium driver-doctor command.
- Creates ADB port forwards to the instrumentation server.
- Starts application preparation and UiAutomator2 session before returning session readiness.
- Can attach an MJPEG screenshot stream.
- On failure during creation, calls session deletion/cleanup.

### Semantic view and element actions

- Supports locator strategies including XPath, resource ID, class name, accessibility ID, CSS-to-native translation and Android UiAutomator expressions.
- Exposes page source, element attributes/text/state/rect/screenshot, find element(s), click, clear and value replacement.
- Supports gestures such as click, double-click, drag, fling, long-click, pinch, scroll and swipe.
- Supports keyboard/keycode/text actions, alerts, notifications, orientation, displays/windows, clipboard, deep links and navigation.
- Provides viewport, density, status-bar, display and device details.
- Supports native and WebView contexts.

### Application lifecycle and policy controls

- Accepts APK/APKS path or URL, package/activity identifiers, browser sessions and app wait rules.
- Supports no-reset, full-reset, auto-launch, force-launch, termination and permission-grant behavior.
- Can install related apps or uninstall selected packages.
- Supports application-start waits and explicit install timeouts.
- Session teardown can stop recordings/streams/Chromedriver, delete the device server session, force-stop/uninstall the app under configured reset rules, restore animation/IME/hidden-API policy and release forwarded ports.

### Concurrency and cleanup

- Uses per-session system ports and active-session/UDID claims.
- Maintains per-session Chromedriver mappings.
- Explicitly releases ports and stops recording/streaming services on delete.
- Cleanup is best-effort: many failures are logged and ignored to allow remaining cleanup.

## What UiAutomator2 completes

- A mature Android semantic UI tree and element-action backend.
- App lifecycle, package/install/start/wait/reset patterns.
- Real-device/emulator target and per-session port requirements.
- Native/WebView context switching.
- Page source, element screenshots and semantic-state evidence.
- A device-side instrumentation server separate from Appium host routing.
- Extensive gesture, keyboard, alert, display, clipboard and application commands.
- Session cleanup/restoration requirements.

## Important limitations for Ptah

- It is test-oriented and may reset, uninstall, force-stop, change permissions, disable animations, alter IME or hidden-API policy depending on capabilities.
- `udid` is an ADB selector, not stable physical Device identity.
- Omitting `udid` can select the first connected device.
- UiAutomator/accessibility trees can omit custom-rendered, secure, WebView or transient content.
- Element IDs and page-source nodes become stale as UI state changes.
- A successful element command does not prove business outcome or authoritative external result.
- Session creation changes device state by installing helper packages, forwarding ports and running instrumentation.
- `skipServerInstallation` or `skipDeviceInitialization` can trade startup speed for stale/incompatible state.
- Reset/cleanup behavior is complex and capability-dependent.
- Cleanup catches/ignores some failures; Ptah must preserve incomplete cleanup evidence.
- Parallel sessions need exact devices and unique ports; default range allocation alone is not a universal distributed allocator.
- Page source and screenshots may expose highly sensitive data.
- Clipboard and permission APIs are security-sensitive.
- Hybrid sessions add Chromedriver/version/WebView compatibility and supply-chain dependencies.
- API-level minimum and driver/Appium/server versions change over time.
- ADB, JDK, Android SDK, settings app, instrumentation APK and Chromedriver are separate dependency/provenance surfaces.
- UIAutomator2 instrumentation may be killed or blocked by OEM power/security policies.
- Appium/driver session claim is not a Ptah cross-provider lease/fencing mechanism.

## Must not be inherited

- first-device selection when `udid` is absent;
- Appium/ADB session claim treated as Ptah Device lease;
- page source treated as complete visual or application truth;
- element command HTTP success promoted to business/authoritative success;
- reset/uninstall/permission/animation/IME/hidden-policy changes hidden inside ordinary session startup;
- `skipServerInstallation` accepted without exact helper-version read-back;
- ignored cleanup failure promoted to clean Session closure;
- default local port allocation used as distributed resource authority;
- automatic retry of click/type/gesture/install/reset actions;
- stale element IDs reused after UI generation/context change;
- screenshot/page-source/clipboard data entering telemetry without redaction;
- mutable npm/package/helper versions used without pinned Artifact identity.

## Integration decision

**WRAP AS THE PRIMARY ANDROID SEMANTIC UI/AUTOMATION BACKEND, WITH PTAH OWNING DEVICE LEASE, SESSION POLICY AND PROOF.**

Recommended separated capability groups:

- semantic tree/page source;
- element find/read;
- element click/type/clear;
- gestures/raw W3C actions;
- screenshots/viewport/display inventory;
- application install/start/stop/reset/uninstall;
- alerts/notifications/system panels;
- clipboard;
- permissions/device settings;
- native/WebView context;
- recording/streaming;
- helper/server lifecycle.

Every state-mutating capability must be explicit in the Ptah Session recipe rather than hidden in a generic capability blob.

## Native Ptah gap

Ptah must define:

- stable Device and Application identities;
- exact Device lease/fencing outside Appium;
- Application Session and Semantic View generation;
- helper/server/settings/Chromedriver Artifact identities and compatibility;
- normalized session recipe separating observation, app lifecycle and device mutation;
- page-source/element/view relationships and stale-element generation checks;
- semantic action IDs, no-retry classes and post-action verification;
- display/screenshot/semantic-tree correlation;
- port/resource allocation across Nodes/providers;
- readiness levels: device selected, helper verified, instrumentation ready, app process launched, target activity/window visible, semantic tree available;
- cleanup checklist and partial-cleanup receipts;
- sensitive-data/redaction/retention policy;
- reconnect, late-result and instrumentation-death handling;
- hybrid context/Chromedriver compatibility model;
- conformance and fallback to raw display/input or Accessibility/Tou​​chPilot-like providers.

## Exit strategy

The Android Semantic UI Facility remains backend-neutral. Direct UiAutomator, AccessibilityService, Appium UiAutomator2, Espresso, TouchPilot-like agents, OCR/vision or OEM/cloud services can provide competing semantic Views/actions while preserving Ptah Application Session identities.

## Validation required

1. Require an exact leased Device; reject absent `udid`/ambiguous target selection.
2. Pin and verify Appium, driver, UiAutomator2 server, settings app, ADB/JDK/SDK and Chromedriver dependencies.
3. Create two parallel sessions with unique devices/ports and no cross-talk.
4. Prove helper installation/instrumentation/app launch/visible activity/semantic tree as separate readiness levels.
5. Capture page source and screenshot at one generation, mutate UI, and reject stale element use.
6. Click/type once with no blind retry and verify a later semantic/display state.
7. Run a no-reset session and prove it does not uninstall/clear/force-stop unexpectedly.
8. Run a full-reset session only with explicit authorization and verify cleanup/state afterward.
9. Kill instrumentation during action/cleanup and preserve partial failure instead of claiming a clean session.
10. Exercise native→WebView→native context changes with exact context/Chromedriver evidence.
11. Redact sensitive page-source, screenshot and clipboard contents according to workspace policy.
12. Replace UiAutomator2 with another semantic backend while preserving Ptah Session/View/Action contracts.
