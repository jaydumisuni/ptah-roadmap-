# Phase 0A — WP07B Desktop and Apple Application Runtime Composition

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Runtime code:** NOT STARTED

## Purpose

Close Linux, Windows, macOS and iOS Application Provider, Window, Display Gateway, semantic automation and checkpoint boundaries, completing WP07 after the Android Device Runtime composition.

## Sources inspected and saved

### Linux/browser display

- Xpra and Xpra HTML5
- Apache Guacamole server/client
- noVNC and websockify
- earlier E2B Desktop and Workspace Provider records

### Windows

- QEMU
- libvirt
- FreeRDP
- FlaUI
- NovaWindows Appium Driver
- Appium Windows Driver / WinAppDriver compatibility path
- earlier Appium core record

### macOS/iOS

- Peekaboo
- Appium XCUITest Driver
- IDB
- Apple Xcode, Simulator/Device Hub, XCTest/XCUIAutomation and Virtualization framework official references

Saved records:

- `donors/XPRA.md`
- `donors/APACHE-GUACAMOLE.md`
- `donors/NOVNC-WEBSOCKIFY.md`
- `donors/QEMU-LIBVIRT.md`
- `donors/FREERDP.md`
- `donors/WINDOWS-SEMANTIC-AUTOMATION.md`
- `donors/PEEKABOO-MACOS.md`
- `donors/APPIUM-XCUITEST-IDB.md`
- `donors/APPLE-NATIVE-RUNTIME-FOUNDATIONS.md`

## Composite result

```text
Ptah Application Object
  installable/runnable software identity and provenance

Ptah Application Provider
  native host, OCI desktop, VM, simulator, physical device or remote service

Ptah Application Installation
  installed identity/version/signature and cleanup state

Ptah Application Session
  logical running app instance with processes, windows, streams and contexts

Ptah Process and Window records
  provider-local aliases tied to stable Session identity

Linux
  native/OCI provider + Xpra individual windows
  Guacamole/noVNC full-desktop fallback

Windows
  native Windows Node or QEMU/libvirt VM Provider
  FreeRDP/Guacamole display
  FlaUI direct semantics + NovaWindows W3C semantics

macOS
  native macOS Node or Apple Virtualization VM
  Peekaboo native visual/accessibility control

iOS/iPadOS/tvOS
  macOS-hosted Simulator/physical-device Provider
  IDB companions + Appium XCUITest/WebDriverAgent

Ptah Display Gateway
  Xpra HTML5, Guacamole, noVNC, scrcpy or platform-native presentation
```

No provider, VM, display protocol or automation session is canonical Ptah Application identity.

## Accepted architecture

Saved as `decisions/ADR-0010-APPLICATION-PROVIDER-WINDOW-DISPLAY-BOUNDARY.md`.

Key decisions:

1. Application Object, Provider, Installation, Session, Process, Window, Display Gateway and Semantic Context remain separate.
2. A Workspace may use several Application Providers concurrently.
3. Provider placement is capability/resource/licence/data-locality driven.
4. Installation exit code is not verified installed state.
5. Process launch, first window, first frame, semantic readiness and expected state are distinct proof levels.
6. Xpra is the primary individual Linux application/window display candidate.
7. Guacamole is the primary cross-protocol browser remote-desktop gateway candidate.
8. noVNC/websockify is the lightweight VNC compatibility path.
9. QEMU/libvirt is the primary Windows VM Provider candidate on Linux/KVM.
10. Native Windows Node remains a separate provider class.
11. FreeRDP/Guacamole is the primary RDP presentation path.
12. FlaUI is the primary direct Windows semantic donor.
13. NovaWindows is the primary modern W3C candidate but remains early/PowerShell-backed.
14. Appium Windows/WinAppDriver is compatibility-only due the unmaintained backend.
15. Peekaboo is the primary macOS native visual/accessibility automation candidate; its agent identity is excluded.
16. Appium XCUITest is the primary iOS W3C semantic backend candidate.
17. IDB is the primary remote Apple device/simulator companion donor.
18. Apple Xcode/Simulator/XCTest/Virtualization are mandatory proprietary platform dependencies, not reusable source foundations.
19. Display read, input, clipboard, file transfer, audio, printing, device redirection and recording are independently scoped.
20. Display reconnect is not process/application recovery.
21. Provider snapshots declare exact checkpoint class; VM state is not automatically application-consistent.
22. Visual and semantic evidence may disagree and remain separately addressable.

## Requirement closure verdict

Closed for Phase 0B contract design:

- `APP-002` Linux graphical/native Application Runtime;
- `APP-003` Windows EXE/MSI/UWP native/VM Application Runtime;
- `APP-004` macOS application and iOS Device/Simulator Runtime;
- cross-platform Application Provider, Installation, Session, Process, Window and Display Gateway models;
- application portions of `SESSION-001`;
- runtime/application portions of `UI-001` and `UI-002`;
- display/recording portions of `OBS-001` and `PROV-001`;
- platform application/provider portions of `CORE-004`, `CORE-005`, `DIST-001` and `OFFLINE-001`.

## Remaining known gap

Linux semantic automation needs a dedicated AT-SPI/accessibility donor pass before claiming feature parity with Android, Windows and macOS semantic backends. This does not block the generic Application Provider/Window/Display contract or Linux visual/manual operation, but remains a Phase 0B/later completion item.

## Phase 0B contracts required

1. Application Object and platform/runtime requirements.
2. Application Provider manifest and placement capabilities.
3. Installation and read-back verification schema.
4. Application Session, Process and Window schemas.
5. Display Surface, Display Gateway and channel-capability schemas.
6. short-lived scoped browser/native client connection-token schema.
7. semantic Screen Context cross-platform extensions.
8. selector intent and backend compilation records.
9. provider/window/backend generation and stale-result rules.
10. checkpoint class and application-consistency schema.
11. recording/screenshot/audio/UI-tree Artifact schema.
12. OS login, RDP/VNC, Apple signing and application-licence credential references.
13. platform/tool/runtime version and compatibility matrix.
14. provider/display/semantic conformance suites.
15. direct human and automation ownership/reconciliation rules.

## Validation set

- simultaneous Linux, Windows, macOS and mobile application sessions;
- multiple independent windows/processes without cross-talk;
- provider and display-backend replacement;
- install/read-back/launch/window/frame/semantic/state proof separation;
- browser-display token scoping and target isolation;
- independent clipboard/file/audio/input/recording permissions;
- VM checkpoint plus application-consistency verification;
- stale window/context/session rejection after provider restart;
- simulator versus physical-device proof separation;
- privacy/redaction of screen, audio, clipboard and UI trees;
- credential secrecy and licence/platform constraint reporting.

## WP07 closure

WP07A and WP07B together close the complete Device and Application Runtime cluster for Phase 0B contract design:

- Android physical devices/emulators;
- ADB/Fastboot/package/file/process/log Facilities;
- display/audio/input/semantic UI;
- physical-device leases and cleanup;
- Linux graphical applications;
- Windows native/VM applications;
- macOS native/VM applications;
- iOS Simulator/physical-device applications;
- shared Application Session, Window, Display Gateway and proof boundaries.

No runtime dependency or implementation is approved yet.

## Next Phase 0A group

Proceed with **WP08 — Browser and Live Research Composition**:

- Playwright and language bindings;
- Playwright MCP;
- Browser-Use;
- TurboWebFetch canonical repository and implementation recovery;
- Chromium persistent profiles, authenticated contexts, downloads, screenshots, video, trace and network evidence;
- browser pool/reuse and crash recovery;
- rendered extraction and source provenance;
- live-search/council-member caller boundary without embedding reasoning into Ptah.
