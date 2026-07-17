# Internal Recovery Record — THETECHGUY Device Manager Runtime

**Phase:** 0A / WP07  
**Status:** FIRST-PASS COMPLETE — DPC/ADB PRODUCT FOUNDATION, NOT A COMPLETE MULTI-DEVICE RUNTIME  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/thetechguy-device-manager`
- Visibility: Private
- Default branch: `main`
- Pinned commit: `e40189f6a4832124c91172b77967c46c06b5c66a`
- Repository state: single large initial import
- Licence: no root `LICENSE` found; no code extraction is authorized until ownership/licensing is recorded explicitly
- Product package: `com.thetechguy.ttgdevicemanager`
- Ptah relevance: authorized Android setup/device-management application, PC-side ADB workflows, DPC/Device Admin provisioning, app/package operations, device profile detection and operator-facing safety boundaries

## Files/components inspected

- `README.md`
- `app/src/main/AndroidManifest.xml`
- `app/src/main/java/com/thetechguy/ttgdevicemanager/MainActivity.kt`
- `app/src/main/java/com/thetechguy/ttgdevicemanager/TTGDeviceAdminReceiver.kt`
- `app/src/main/java/com/thetechguy/ttgdevicemanager/TTGDnsShieldService.kt`
- initial-commit evidence containing the Windows ADB all-in-one workflow and brand-aware package/profile logic

## Verified implemented behavior

### Android application identity and provisioning

- Declares the Device Admin receiver `TTGDeviceAdminReceiver` with `BIND_DEVICE_ADMIN`.
- Receives Device Admin enabled, profile-provisioning-complete and provisioning-successful events.
- Launches the main application after provisioning completion.
- Declares internet and broad package-query permission.
- Disables Android application backup.
- Includes a non-exported `VpnService`-based DNS shield service.
- README explicitly limits use to authorized service/setup/device-management work and states that logs should avoid private/security secrets.

### Operator-facing Android controls

- Shows whether the package is active as Device Owner.
- Opens Active Admins, Device Admin enrollment, Developer Settings, Wi-Fi Settings, Android Settings, App Manager, battery settings, browser support page and dialer.
- Lists app-management operations in the UI.
- Hides/unhides packages through `DevicePolicyManager.setApplicationHidden` only when Device Owner is active.
- Presents factory reset as a helper/explanation rather than falsely claiming the app performed it.
- Explicitly says that full package lists/search/dumps require the PC-side ADB helper.

### PC-side ADB workflow recovered from the initial import

- Resolves bundled or configured `adb.exe` paths.
- Starts/restarts the ADB server and displays `adb devices -l`.
- Reads manufacturer, brand, model, Android release, SDK, build and ADB serial.
- Maps observed brand/manufacturer/model text to product-specific update-package profiles.
- Installs/reinstalls the Device Manager APK, opens it and offers a signature-mismatch uninstall/reinstall path.
- Opens Device Admin settings, attempts `dpm set-device-owner`, lists owners/admins/packages and manages package enable/disable state.
- Supports package listings/search/dumps, Wi-Fi ADB setup/connect and system-setting helpers.
- Contains explicit danger-zone and confirmation-oriented operations rather than pretending every action is harmless.

## Strong internal patterns for Ptah

1. Keep the on-device application and the PC transport/orchestration layer separate.
2. Treat Device Owner/Admin state as observed capability, not an assumed entitlement.
3. Expose system settings and human-completion routes honestly when Android blocks silent automation.
4. Detect brand/device properties before selecting product-specific operations.
5. Keep package management, provisioning, ADB/Wi-Fi transport and policy operations as distinct capability groups.
6. Use explicit operator confirmation around destructive or ownership-changing actions.
7. Mark authorized-service scope and sensitive-log restrictions in the product itself.
8. Preserve direct-human access to the same device functions exposed to automation.

## Important limitations

- The repository is one large initial import with no incremental architecture history.
- The Android app is primarily an operator UI and DPC/Device Admin helper, not a neutral remote-device runtime.
- Several app buttons are explanatory placeholders that redirect full functionality to the ADB helper.
- Device identity is mostly ADB serial plus displayed properties; there is no Ptah-stable Device identity or connection epoch.
- The PC helper uses fixed local Windows paths and shell/batch orchestration.
- ADB server restart and command execution are process-oriented, with no durable Activity Ledger or typed receipts.
- Brand matching is substring-based and package-profile lists are assumptions until read back on the exact device/ROM.
- `dpm set-device-owner`, package disable, OTA/package policy and reset operations require stronger compatibility, authorization and post-operation proof.
- The DNS shield establishes a VPN interface but the inspected service does not show a complete packet-processing/filtering loop.
- Broad `QUERY_ALL_PACKAGES` and package/device data require privacy review.
- No root licence was found.
- No multi-device lease, concurrent worker, remote display/input, semantic UI or reconnect model is implemented here.

## Must not be inherited

- fixed drive-letter/project paths as runtime identity;
- ADB serial alone as stable Device identity;
- substring brand detection as sufficient device compatibility proof;
- command exit code or UI text as physical-state proof;
- automatic ADB server restarts that can disrupt unrelated concurrent devices without Node-level coordination;
- package/profile lists treated as universal truth across OEM versions;
- Device Owner or destructive operations exposed without exact selection, lease, authorization and read-back;
- Device Manager product branding or private workflow policy embedded in neutral Ptah contracts;
- broad package/device data copied into logs or telemetry;
- unlicensed source copied into public Ptah code.

## Classification

**ADAPT PRODUCT REQUIREMENTS AND SAFE OPERATOR WORKFLOWS; DO NOT USE AS THE PRIMARY DEVICE RUNTIME.**

The repository is strong internal evidence for `DEVICE-001`, `DEVICE-002`, `APP-001`, `UI-001`, `UI-002` and application/session extensions. Ptah should expose its functions through neutral Device Facilities while the THETECHGUY application remains a specialist product/caller.

## Native Ptah completion required

- stable Device identity separate from ADB serial, USB path and network endpoint;
- transport/interface connection epoch and re-enumeration history;
- exact Device selection and lease ownership;
- typed ADB/Fastboot/MTP/package/file/process/policy operations;
- command, launch, visible-runtime, completion and read-back proof levels;
- multi-device concurrency and ADB-server coordination;
- capability/profile discovery with evidence and versioned compatibility claims;
- Android application/package/session Objects;
- sensitive-data classification, redaction and scoped access;
- durable Activity/receipt/Artifact links;
- remote display/input/semantic UI providers;
- provider-neutral API/SDK/CLI contracts;
- source/licence record before code extraction.

## Exit strategy

The Device Manager remains an internal Android product and operator interface. Ptah contracts must allow adbkit/platform-tools, STF-like providers, Appium, scrcpy, custom native engines or future OEM services to replace one another without changing Device, Application Session, Operation, Stream or Receipt identities.

## Validation inherited into Ptah

1. Connect two Android devices and require explicit selection/lease rather than first-device fallback.
2. Re-enumerate one device across USB, ADB and Fastboot while preserving stable Device identity and changing connection epoch.
3. Reject a package/policy operation when brand/profile evidence is missing or stale.
4. Install an APK, then read back package/version/signature state before PASS.
5. Attempt Device Owner enrollment and preserve Android's authoritative rejection without inventing success.
6. Disconnect during a package or file operation and reject stale completion from the previous epoch.
7. Prove read-only package/device inventory cannot reach reset, ownership or policy mutations.
8. Run simultaneous operations on separate devices without restarting or corrupting the shared ADB server.
9. Preserve operator-visible instructions where Android requires manual confirmation.
10. Prove package/device identifiers and logs are redacted according to workspace policy.
