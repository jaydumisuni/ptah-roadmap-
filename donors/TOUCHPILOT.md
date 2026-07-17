# Donor Record — TouchPilot

**Phase:** 0A / WP07  
**Status:** FIRST-PASS COMPLETE — CANONICAL REPOSITORY RESOLVED; ANDROID SEMANTIC-ACTION/SAFETY DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/touchpilot/touchpilot
- Canonical owner: `touchpilot` organization
- Default branch: `main`
- Pinned commit: `3dedb1deda373a8202e95953119a773ca130503d`
- Related repository: `tmimmanuel/touchpilot` currently exposes the same pinned commit/history and appears to be the author's mirror/original location; Ptah should treat the organization repository as canonical while verifying future divergence
- Licence: MIT
- Copyright holder in licence: `tmimmanuel`
- Primary language/runtime: Kotlin native Android application
- Current build manifest version at the pin: `0.1.0`, minSdk 26, target/compile SDK 35
- Activity: Active
- Classification: local-first AccessibilityService-based Android semantic observation/action, policy, approval and audit donor
- Ptah targets: `DEVICE-002`, Android Application Session semantic Views/actions, normalized screen context, action verification, risk/approval vocabulary, compatibility testing and local device-side provider patterns

## Files/components inspected

- `README.md`
- `LICENSE`
- `app/build.gradle.kts`
- `app/src/main/AndroidManifest.xml`
- `docs/CODE_STRUCTURE.md`
- `docs/TOOL_SPEC.md`
- `docs/SAFETY_MODEL.md`
- `docs/POLICY.md`
- `app/src/main/java/dev/touchpilot/app/androidcontrol/AccessibilityBridge.kt`
- `app/src/main/java/dev/touchpilot/app/tools/AndroidToolExecutor.kt`
- latest commit evidence for local bug-report export and redaction

## Verified capabilities and patterns

### Native Android provider boundary

- Runs as an Android application rather than requiring a desktop companion.
- Declares a non-exported AccessibilityService protected by `BIND_ACCESSIBILITY_SERVICE`.
- Uses AccessibilityService for semantic screen observation, foreground-app state and Android actions.
- Central `AccessibilityBridge` exposes connected state, raw/normalized observation, tap, long-press, double-tap, type, scroll, swipe, drag, back, home, recents, keyboard dismissal and bounded waits.
- Maintains a direct separation between Android-control bridge, tool execution, screen models, security/policy, logs and agent/runtime packages, even though they are currently one Gradle module.

### Typed semantic tool contract

- Tools are the only documented path by which the agent affects the Android device.
- Tool catalogue contract is frozen at version 1 and defines names, arguments and risk.
- Implements observation, application opening, allowlisted Settings panels, semantic tap/press/type/clear, scroll-to-element, swipe, drag/drop, system navigation, structured waits, foreground-app state, element finding and keyboard control.
- Distinguishes accessibility scroll actions from raw swipe gestures.
- Supports selectors by text, content description, stable node ID, view ID and bounds.
- Missing or ambiguous semantic targets fail rather than guessing.
- Waits and composite scroll/search operations are explicitly bounded.

### Normalized screen context

- Provides raw accessibility-tree output for debugging and a normalized `ScreenContext` for decisions.
- Normalized context includes application/window metadata, visible semantic nodes, roles, bounds and action flags.
- Redacts passwords, tokens, OTPs, email addresses, card numbers and other sensitive text in structured output.
- Flags redacted nodes and whether a screen contains sensitive content.
- Exported run traces include redacted initial/final contexts.

### Execution, retry and verification

- Validates tool name/arguments before execution.
- Resolves foreground application and execution source.
- Runs policy/approval gates for direct debug execution and documents upstream policy gates for agent/workflow/skill execution.
- Captures before and after `ScreenContext` around actions.
- Runs a `ToolVerifier` and converts nominal success into failure when verification fails.
- Records tool attempts and result evidence.
- Has a configurable retry policy, attempt count, delay and idle wait.
- Observation tools reuse the same context rather than pretending they caused a UI transition.

### Risk policy and approval

- Policy contract defines subject, workflow class, risk band and strictest-wins decision precedence.
- Default tool mapping allows LOW, asks for MEDIUM/HIGH and blocks BLOCKED.
- Sensitive workflow classes include message send, payment, purchase, deletion, account changes/recovery, permission/security settings, sensitive text entry, external MCP and unknown-sensitive paths.
- Current 1.0 policy blocks most sensitive workflow classes rather than silently executing them.
- Policy changes cannot become less strict without contract-version and changelog treatment.
- User approval and audit logs are central to the runtime.

### Audit and information safety

- Tool runs, approval decisions and workflow traces are locally logged.
- Bug-report export records app/device compatibility data, accessibility state, foreground app, tool logs and current screen.
- Safe redaction is the default bug-report export level; an explicit no-redaction mode exists.
- API keys for optional OpenAI-compatible fallback are encrypted with Android Keystore-backed AES-256-GCM before preferences storage.
- Application backup is disabled.

### Compatibility and release discipline

- Tracks Android API 31–35 and OEM compatibility through a manual-first matrix/checklist.
- Documents weak/empty accessibility trees and OEM battery/foreground-service behavior as unresolved compatibility work.
- Includes device instrumentation smoke tests.
- Release signing accepts explicit keystore environment/properties, otherwise the current release build falls back to debug signing.
- The repository has begun signed-release/checklist work, but production release identity remains a separate gate.

## What TouchPilot completes

- A concrete device-side semantic Android provider rather than only a desktop test harness.
- Typed semantic tool contracts and stable names/arguments.
- Normalized, redacted Accessibility screen context.
- Safe selector resolution and bounded waits/composite actions.
- Before/after semantic verification.
- Risk classes, strict policy precedence, approvals and audit traces.
- Compatibility-matrix and OEM testing requirements.
- A useful complement to Appium: local native AccessibilityService operation with inspectable tools.

## Important limitations for Ptah

- The project is an Android AI-agent application, while Ptah must remain the environment/facility layer rather than inherit its reasoning loop, chat UI, model routing, skills identity or policy as universal truth.
- It is currently one Android application module with substantial orchestration still in `MainActivity`.
- Build version remains `0.1.0` while documentation freezes “1.0” contracts; release/version truth needs reconciliation.
- Release builds fall back to debug signing when production credentials are absent.
- `android:usesCleartextTraffic="true"` is enabled and requires network-security review.
- AccessibilityService sees only what Android/OEM/apps expose; custom canvases, games, secure windows, WebViews and transient UI can produce weak or empty trees.
- Node IDs are provider-generated semantic references, not stable across all screen generations or app versions.
- Before/after screen change is not sufficient proof of business outcome.
- Some navigation actions are documented as retryable; Ptah must not blindly retry semantically non-idempotent actions.
- The current in-process policy model has no per-user/per-device overrides and is not remotely managed.
- Accessibility permission is extraordinarily powerful and may observe/type sensitive content or approve system dialogs.
- Raw local debug logs may contain information that structured exports redact.
- An explicit no-redaction export mode remains a high-risk data-release action.
- Local app/provider restart and Android process death need durable external Session reconciliation.
- Compatibility work is manual-first and many OEM rows remain incomplete.
- No external lease/fencing exists: the on-device service assumes its local app is the controlling authority.
- `ToolResult` remains a local ok/message/data structure rather than a Ptah receipt with Device/Session/Object/Artifact identity.
- The optional cloud/model/MCP paths expand network and supply-chain surface beyond semantic device control.

## Must not be inherited

- TouchPilot's model router, chat identity, local inference or agent loop as Ptah Core;
- its skill/prompt/workflow semantics as universal Device policy;
- local Accessibility connection used as proof of an exclusive Ptah lease;
- LOW/MEDIUM/HIGH mapping copied as the only policy system;
- screen change treated as authoritative action/business success;
- retries of tap/type/send/payment/confirmation actions without idempotency and stronger evidence;
- node ID reused after screen/app/provider generation changes;
- AccessibilityService permission bundled with model/network/MCP permission;
- raw/no-redaction traces exported without explicit sensitive-data authorization;
- debug-signed release treated as production provenance;
- cleartext network traffic accepted by default;
- application process state used as durable Ptah Session truth;
- TouchPilot branding or agent philosophy embedded in neutral Ptah contracts.

## Integration decision

**ADAPT THE SEMANTIC SCREEN-CONTEXT, TYPED TOOL, SELECTOR, POLICY/APPROVAL, VERIFICATION AND DEVICE-SIDE PROVIDER PATTERNS. SUPPORT TOUCHPILOT AS AN OPTIONAL ANDROID SEMANTIC FACILITY/APP.**

Potential integration forms:

1. protocol-compatible Ptah Android provider implementing equivalent typed semantic operations;
2. a reviewed TouchPilot service/app build exposing a narrow authenticated local IPC/MCP-like bridge;
3. selective MIT-licensed adaptation of stable screen/tool/security components after source/provenance review.

The reasoning/model loop is out of scope for Ptah adoption.

## Native Ptah gap

Ptah must define:

- Android Semantic Provider identity/version and authenticated registration;
- stable Device and external lease/fencing token;
- Application Session, Semantic View and view-generation identity;
- normalized node/role/action/bounds/sensitivity schema independent of one provider;
- provider-origin node IDs and stale-generation rules;
- semantic observation/action capability groups;
- policy input from caller/workspace rather than one fixed app policy;
- action operation ID, attempt, nonce, connection epoch and no-retry classification;
- before/after semantic/display evidence plus authoritative-result levels;
- signed/typed receipts and Artifact references;
- encrypted local IPC/Node transport and offline outbox;
- Android process/service death/reconnect reconciliation;
- helper APK signing/provenance/SBOM/version compatibility;
- sensitive-screen/trace/log retention and no-redaction export controls;
- compatibility profiles across API/OEM/app/UI types;
- fallback and competing Views from UiAutomator2, raw display/vision or OEM services;
- direct-human review/approval UI as one caller, not the sole authority.

## Exit strategy

The Android Semantic UI contract remains provider-neutral. TouchPilot, Appium UiAutomator2, direct AccessibilityService, UIAutomator, Espresso, OCR/vision or OEM/cloud device services can provide competing semantic Views/actions. Ptah retains Device, lease, Session, policy, Activity and proof identities.

## Validation required

1. Verify canonical organization and personal repositories remain identical at the pin; alert on future divergence.
2. Build from source, verify package/version/signature and prohibit debug-signed production use.
3. Register the Android provider through authenticated local/Node IPC and bind it to an external leased Device.
4. Observe a normalized screen, redact sensitive text and preserve a versioned Semantic View Artifact.
5. Change the screen and reject a node ID from the prior generation.
6. Resolve an ambiguous target and prove the provider fails rather than guesses.
7. Execute one semantic action once and verify later semantic/display state without blind retry.
8. Exercise a payment/account/security workflow and prove caller policy can require approval or block it before the Accessibility action.
9. Kill/restart the app/service and reject stale actions/results from the prior provider epoch.
10. Export a safe bug report and prove raw secrets are absent; require explicit high-risk authorization for no-redaction export.
11. Test stock Android plus Samsung/Xiaomi/Oppo/OnePlus profiles and preserve compatibility/limitation evidence.
12. Replace TouchPilot with UiAutomator2 for the same semantic contract while preserving Ptah Device/Application Session identity.
