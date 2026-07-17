# Donor Record — Peekaboo for macOS

**Phase:** 0A / WP07B  
**Status:** FIRST-PASS COMPLETE — PRIMARY MACOS VISUAL/ACCESSIBILITY APPLICATION-AUTOMATION DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/openclaw/Peekaboo
- Historical/project package identity: `@steipete/peekaboo`
- Default branch: `main`
- Pinned commit: `e2a46347138d60fa27f3a1cda84c338d41773e77`
- Pinned documented release line: 3.9.x
- Licence: MIT
- Runtime: Swift 6.2/macOS 15+ plus optional Node MCP wrapper
- Classification: macOS screen capture, accessibility-semantic context, window/application control and browser/MCP tool donor
- Ptah targets: `APP-004`, macOS native Application Session, windows, screenshots, semantic actions, background input, permissions and local automation service patterns

## Files/components inspected

- `README.md`
- documented permissions, architecture, command and service boundaries
- application/window/screen/menu/dialog/input tool surface
- warm daemon/Bridge and lease-owned socket pattern

## Verified capabilities and patterns

- Captures full screens, windows and menu bar with optional Retina scaling.
- Produces structured UI snapshots with opaque element IDs.
- Supports accessibility-based value setting and named actions such as `AXPress`.
- Supports click, type, press, hotkey, paste, scroll, swipe, drag and pointer movement.
- Enumerates and controls applications, windows, Spaces, menus, menu-bar extras, Dock and dialogs.
- Distinguishes background process-targeted input from foreground/focus-changing input.
- Resolves target process through application, PID, window ID or snapshot metadata.
- Uses accessibility actions first and synthetic coordinate/input fallback where needed.
- Requires explicit Screen Recording and Accessibility permissions; event synthesis may require a further permission.
- Exposes structured JSON through a native CLI and the same tools through MCP.
- Uses warm daemon and application Bridge hosts with distinct lease-owned sockets and local fallback.
- Supports reproducible typed workflows, session resume and snapshot/cache cleanup.
- Can launch, quit, relaunch and switch applications.

## What Peekaboo completes

- A strong macOS-native equivalent to Android semantic context plus visual fallback.
- Application, window, menu, dialog and Space control rather than only full-desktop pixels.
- Structured snapshots and element IDs paired with screenshots.
- Background versus foreground input as explicit behavior.
- Native macOS permission discovery and helper-service lifecycle requirements.
- A direct CLI/MCP interface suitable for adapters while Ptah retains its own contract.
- A strong model for linking an action to the exact snapshot/context used to target it.

## Important limitations for Ptah

- macOS 15+ at the inspected release narrows host compatibility.
- Peekaboo's integrated AI/agent/provider system is outside Ptah's role and must not be inherited.
- Opaque snapshot element IDs are backend-local and stale after UI changes.
- Accessibility coverage is incomplete for custom rendering, games, secure surfaces and some cross-process UI.
- Screen Recording, Accessibility and event-synthesis permissions are powerful host entitlements.
- Background input is not guaranteed to work for every application or control.
- Foreground/focus/Space switching can disrupt other concurrent human or automated work.
- MCP/CLI access can expose broad local desktop authority if not scoped behind Ptah leases.
- A clicked element or launched app does not prove the intended state.
- Screenshots, menus, clipboard and visible text may contain highly sensitive data.
- Warm daemon/Bridge sockets and snapshot caches require explicit lifecycle, ownership and cleanup.
- The project is a macOS automation product, not a VM/native Node Provider or Ptah reasoning layer.

## Must not be inherited

- Peekaboo's agent, model-provider or reasoning identity in Ptah Core.
- opaque element/snapshot IDs as canonical Ptah Window or Screen Context identity.
- Screen Recording, Accessibility and event-synthesis permission bundled as one unrestricted capability.
- local MCP/CLI exposed directly to untrusted callers.
- background input assumed safe or supported universally.
- focus/Space-changing input replayed automatically after disconnect.
- screenshot or action acknowledgement promoted to functional verification.
- snapshots/caches retained without privacy and cleanup policy.
- macOS 15-only assumption embedded in the generic Application Provider contract.

## Integration decision

**WRAP PEEKABOO AS THE PRIMARY MACOS NATIVE VISUAL/SEMANTIC APPLICATION-AUTOMATION BACKEND CANDIDATE.**

Recommended architecture:

1. macOS Node hosts native applications and Peekaboo helper/Bridge;
2. Ptah macOS Application Provider owns application/process/window/session identity;
3. Peekaboo adapter provides screenshots, structured context, windows/menus/dialogs and input;
4. Ptah owns lease, capability scope, privacy, Activity and receipts;
5. Peekaboo's agent/MCP front end remains optional caller compatibility, not the internal contract.

## Native Ptah gap

Ptah must define:

- macOS Application Session, process, window, display and Space identity;
- native permission status and entitlement capability records;
- stable selector intent plus snapshot/context ID and stale handling;
- background versus foreground/focus-changing action class;
- before/after visual and accessibility verification;
- application launch, first window, visible frame and semantic readiness receipts;
- short-lived helper socket credentials and lease/fencing;
- screenshot/recording/privacy/redaction rules;
- multi-user/session and concurrent-automation boundaries;
- compatibility matrix across macOS versions and application frameworks;
- helper daemon restart and cache cleanup receipts;
- backend replacement path.

## Exit strategy

Ptah's macOS Semantic/Visual Facility remains implementable through Peekaboo, direct Accessibility APIs, AppleScript/Shortcuts where appropriate, Appium mac2 or future platform APIs. Peekaboo snapshot/element/socket IDs remain adapter metadata.

## Validation required

1. Launch and attach to several native macOS applications and enumerate their windows.
2. Resolve and act on accessibility elements, menus, dialogs, Dock and Spaces.
3. Reject stale snapshot/element IDs after window/UI changes and re-resolve safely.
4. Distinguish background and foreground input with explicit side-effect receipts.
5. Revoke one permission and surface reduced capabilities without false readiness.
6. Run concurrent sessions without unintended focus/Space interference.
7. Restart the Bridge/daemon and reject stale socket/session results.
8. Redact sensitive screenshots and UI text before telemetry/export.
9. Keep the Peekaboo agent disabled while the same native tools work through Ptah.
10. Replace Peekaboo with another macOS adapter without changing Application Session identity.
