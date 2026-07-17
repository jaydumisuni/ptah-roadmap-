# Phase 0A — WP07A Android Device Runtime Composition

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Runtime code:** NOT STARTED

## Purpose

Close the Android physical-device, emulator, ADB/Fastboot, multi-device provider, display, input, semantic UI and Android Application Session boundaries before extending the same model to Linux, Windows, macOS and iOS runtimes.

## Sources inspected and saved

### Internal

- THETECHGUY Device Manager runtime
- MIBU device/correlation/read-back patterns
- firmware/device operation boundary from WP06

### External and official

- DeviceFarmer STF
- DeviceFarmer adbkit
- minicap
- minitouch
- scrcpy
- Appium core
- Appium UIAutomator2 driver
- TouchPilot
- official Android ADB source and Fastboot source/protocol
- AndroidX UI Automator

Saved records:

- `internal/DEVICE-MANAGER-RUNTIME.md`
- `internal/MIBU.md`
- `donors/DEVICEFARMER-STF.md`
- `donors/ADBKIT.md`
- `donors/MINICAP.md`
- `donors/MINITOUCH.md`
- `donors/SCRCPY.md`
- `donors/APPIUM.md`
- `donors/APPIUM-UIAUTOMATOR2.md`
- `donors/TOUCHPILOT.md`
- `donors/ANDROID-PLATFORM-TOOLS.md`
- `donors/ANDROIDX-UIAUTOMATOR.md`

## Composite result

```text
Ptah Device Identity
  stable physical/virtual identity independent of transport

Ptah Device Interface
  ADB USB/TCP/TLS, Fastboot, MTP, USB serial, provider-native

Ptah Device Provider
  inventory, per-device workers, local helpers and health

Ptah Device Lease
  scoped ownership, expiry and fencing token

Ptah Device Session
  Workspace + lease + Device + current interfaces/capabilities

Official ADB/Fastboot
  authoritative transport and bootloader protocol foundation

adbkit
  optional programmatic ADB client adapter

STF patterns
  multi-device inventory, provider workers, booking/lease and recovery

scrcpy
  primary modern Android video/audio/control backend

minicap/minitouch
  legacy compatibility display/input backends

AndroidX UI Automator
  official native semantic hierarchy/action foundation

Appium + UIAutomator2
  W3C semantic automation compatibility/backend

TouchPilot
  local-first AccessibilityService context/action/safety backend

Ptah Application Session
  installed/running app identity, windows/contexts, streams and proof
```

No donor is canonical Ptah Device or Session truth.

## Accepted architecture

Saved as `decisions/ADR-0009-DEVICE-SESSION-DISPLAY-INPUT-SEMANTIC-UI-BOUNDARY.md`.

Key decisions:

1. Device identity is separate from USB path, ADB serial, network address, provider worker and automation session ID.
2. Every interface has a connection epoch; stale results from an older epoch cannot complete current work.
3. Device observation, provider registration, worker readiness, lease ownership and application readiness are separate states.
4. Physical-device control uses scoped leases and fencing tokens.
5. Inventory, shell, file, package, logs, display, audio, input, clipboard, semantic UI, policy/admin and firmware are separately advertised and authorized capabilities.
6. Continuous streams remain outside ordinary control/event messages.
7. scrcpy is the primary Android video/audio/control backend candidate.
8. minicap/minitouch remain compatibility backends only.
9. AndroidX UI Automator is the official semantic foundation.
10. Appium provides W3C protocol compatibility; UIAutomator2 is an Android semantic backend, not the Device provider.
11. TouchPilot supplies device-side normalized context, typed tools, risk/approval and action-verification patterns without donating its agent identity.
12. Accessibility hierarchy and pixels/raw input are complementary observations with different limitations.
13. Element handles and screen contexts are capture-bound and may become stale.
14. Input acknowledgement, application launch and stream start do not prove intended application state.
15. Device screens, hierarchy, logs, files and clipboard require privacy, redaction and retention classifications.
16. Cleanup is a verified Activity; failed cleanup quarantines the Device.
17. Firmware writes remain governed separately by ADR-0008.

## Requirement closure verdict

Closed for Phase 0B contract design:

- `DEVICE-001` Android inventory, ADB/Fastboot, exact selection and provider/lease foundation;
- `DEVICE-002` Android display, input and semantic UI foundation;
- Android Device Session and Android Application Session portions of `SESSION-001`;
- Android application/package runtime portions of the broader application-runtime model;
- device-side portions of `UI-002` Activity Centre and reconnect/proof display;
- Android-side portions of `CORE-004`, `CORE-005`, `RELAY-001`, `OBS-001` and `OFFLINE-001`.

Still open in WP07B:

- Linux native/graphical Application Provider;
- Windows EXE/MSI/VM Application Provider;
- macOS application and iOS Device/Simulator Provider;
- common desktop remote-display gateway;
- cross-platform window/application-session checkpoint/reconnect;
- final WP07 Device/Application Runtime composition record.

## Phase 0B contracts required

1. Device identity and observed identity-claim schema.
2. Device interface, mode and connection-epoch schema.
3. Device Provider and worker-generation schema.
4. Device lease, capability scope and fencing-token schema.
5. Device Session lifecycle and capability snapshot.
6. Package/Application Object and Application Session schema.
7. display/audio/control/log/shell/file stream records.
8. normalized semantic Screen Context and selector-intent schema.
9. input operation, geometry/context and before/after verification schema.
10. backend deployment/version/cleanup receipt.
11. privacy/redaction/retention profile for device evidence.
12. cleanup/quarantine recipe and receipt.
13. backend capability/conformance matrix.
14. Android-to-Fastboot/MTP/OEM transition correlation.
15. device/session reconnect and stale-result rejection contract.

## Validation set

- concurrent inventory/control of several physical Devices;
- ADB USB/TCP and Fastboot mode correlation;
- lease fencing and stale-session rejection;
- independent shell/file/log/video/audio/control/semantic streams;
- helper/server restart and reconnect reconciliation;
- package install/version/signature read-back;
- app launch, first frame and semantic readiness as separate evidence;
- stale-element re-resolution;
- semantic/visual fallback without Activity identity loss;
- non-idempotent disconnect with no blind replay;
- verified cleanup or quarantine;
- sensitive evidence redaction;
- backend replacement without Device/Session identity change.

## Next inspection unit

Continue WP07B with desktop and Apple application runtimes:

1. Linux native application execution and remote-display gateway;
2. browser-delivered desktop/display options already implied by E2B Desktop;
3. Windows VM/native application execution, process/window/display and MSI/EXE boundaries;
4. macOS application execution, Xcode/iOS Simulator and physical iOS automation;
5. Appium platform drivers and Peekaboo-like macOS visual/application control;
6. common Application Provider, Window, Display Stream and Application Session contracts;
7. checkpoint/reconnect/recording across VM, emulator and native host providers.
