# Donor Record — AndroidX UI Automator

**Phase:** 0A / WP07  
**Status:** FIRST-PASS COMPLETE — OFFICIAL ACCESSIBILITY-TREE AUTOMATION FOUNDATION  
**Inspected:** 2026-07-17

## Identity

- Canonical source: https://android.googlesource.com/platform/frameworks/support/
- GitHub mirror used for source inspection: https://github.com/androidx/androidx
- Default branch: `androidx-main`
- Pinned commit: `448c34296e1546830c5a29b1b9e06d34a5912ce2`
- Relevant module: `test/uiautomator/uiautomator`
- Licence: Apache-2.0
- Owner: Android Open Source Project / AndroidX
- Classification: Official semantic Android UI inspection, selector, wait and gesture foundation
- Ptah targets: hierarchy inspection, element selection, app/system UI actions, semantic waits, accessibility-node screenshots and typed UI state

## Files/components inspected

- `test/uiautomator/uiautomator/api/current.txt`
- `test/uiautomator/uiautomator/src/main/java/androidx/test/uiautomator/UiObject2.java`
- public selector, window-selector and accessibility-node extension APIs
- current API surface for hierarchy search, attributes, gestures, screenshots and stability waits
- legacy platform UI Automator source/documentation for historical boundary comparison

## Verified capabilities and patterns

- `UiObject2` represents a concrete accessibility-backed UI element.
- UI objects expose parent/child traversal, selector-based search, attributes and gestures.
- `By`/`BySelector` support semantic predicates including package, resource ID, text, description, class, state, ancestry, descendants, depth and display/window properties.
- Multi-window and display-aware selectors are supported in the current API.
- Accessibility nodes/windows can produce screenshots and expose structured traversal helpers.
- Stability waits can evaluate hierarchy and optionally screenshot stability rather than relying only on fixed sleeps.
- Gesture behavior includes margins designed to avoid accidental system-edge gestures.
- Conditions and waits are explicit APIs.
- Element handles are tied to a particular underlying view instance and may become stale when the UI changes.
- Stale objects must be re-resolved from a selector/device state.
- The implementation is based on Android accessibility/window structures and instrumentation/testing primitives.

## What AndroidX UI Automator completes

- The official semantic hierarchy and selector layer beneath Appium UIAutomator2 and similar adapters.
- Structured UI state that is more meaningful than pixels alone.
- Element and window queries across application and system UI.
- Typed gestures bound to element geometry and display identity.
- Explicit stale-element and wait/stability behavior.
- A direct Android-native implementation path independent of an Appium server.
- Official source and Apache-2.0 compatibility for a Ptah Android Semantic Facility.

## Important limitations for Ptah

- Accessibility hierarchy is not guaranteed to expose every visible or interactive pixel.
- Custom rendering, games, video surfaces, WebViews, secure windows and OEM interfaces may provide incomplete or misleading semantic trees.
- `UiObject2` instances can become stale after layout/navigation changes.
- Text, resource IDs and content descriptions vary across languages, versions and OEM skins.
- Instrumentation/testing context and deployment requirements differ from an ordinary long-lived AccessibilityService such as TouchPilot.
- Semantic action success does not prove the expected application state without before/after verification.
- Fixed selectors may break when an application updates.
- Accessibility bounds can differ from visible/touchable regions because of clipping, overlays or system windows.
- UI Automator does not provide video streaming, audio, clipboard, ADB transport, device booking or multi-device inventory.
- Shell execution exposed by higher-level device APIs must remain a separate risk-classed operation.
- Screenshot or hierarchy capture may contain sensitive information.

## Must not be inherited

- UI Automator selector or object IDs used as durable Ptah UI identity.
- A cached `UiObject2` retained across arbitrary UI changes without re-resolution.
- Element click/gesture return treated as proof of intended outcome.
- Accessibility hierarchy treated as complete visual truth.
- Hard-coded English text selectors as universal skills.
- Arbitrary shell/test privileges bundled into every semantic UI action.
- Semantic automation used when the caller explicitly selected raw input or visual-only interaction.
- Screenshots/hierarchies stored without privacy/redaction classification.

## Integration decision

**ADOPT ANDROIDX UI AUTOMATOR AS THE OFFICIAL NATIVE SEMANTIC-AUTOMATION FOUNDATION, WITH APPIUM UIAUTOMATOR2 AND TOUCHPILOT AS COMPLEMENTARY ADAPTERS.**

Recommended roles:

1. **AndroidX UI Automator adapter** — direct device/instrumentation semantic queries and actions.
2. **Appium UIAutomator2 adapter** — W3C/WebDriver compatibility and cross-platform test-client integration.
3. **TouchPilot Accessibility adapter** — long-lived on-device normalized context, typed tools, risk controls and before/after verification.
4. **scrcpy/raw input adapter** — visual/manual or coordinate-based fallback.

Ptah chooses among these based on advertised capabilities and the requested operation; no layer silently impersonates another.

## Native Ptah gap

Ptah must define:

- normalized semantic Screen Context independent of AndroidX/Appium/TouchPilot schema;
- UI snapshot ID, device connection epoch, app/package/activity/window/display identity;
- selector intent plus backend-specific compiled selector;
- element observation receipt and stale/re-resolution state;
- action request, risk class, approval reference and before/after verification;
- localization/OEM/app-version compatibility metadata;
- fallback order among semantic, accessibility-service, visual and raw-input methods;
- privacy/redaction for text, hierarchy and screenshots;
- timeout, polling, stability and retry classes;
- application/session and produced screenshot/trace Artifact links;
- compatibility test corpus across Android versions and OEMs.

## Exit strategy

Ptah's semantic Device Facility remains backend-neutral. AndroidX UI Automator, Appium UIAutomator2, TouchPilot, OEM accessibility services or future platform APIs can implement it without changing Ptah Screen Context, Activity or Receipt contracts.

## Validation required

1. Resolve elements by resource ID, package, text, description, class and hierarchy relation.
2. Change the UI, reject a stale object and re-resolve it from the stable selector intent.
3. Perform click, type, scroll, drag and multi-window actions with before/after state verification.
4. Compare hierarchy state with a screenshot and record incomplete-semantic coverage explicitly.
5. Exercise localization and one OEM-skinned system UI without relying only on English text.
6. Detect an element obscured by an overlay and avoid claiming a successful user-visible action from a raw click result.
7. Fall back to scrcpy/visual control when the semantic tree is unavailable while preserving the same Activity identity.
8. Redact sensitive hierarchy text and screenshots according to caller policy.
9. Run the same normalized semantic action through direct AndroidX, Appium and TouchPilot adapters and compare receipts.
10. Upgrade the AndroidX/Appium backend without changing public Ptah Screen Context identity.
