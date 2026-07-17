# ADR-0010 — Application Provider, Window, Display and Platform Runtime Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Phase:** 0A / WP07B application-runtime closure

## Context

Ptah must open and operate applications such as Linux GUI programs, Windows EXE/MSI/UWP applications, macOS applications, Android packages and iOS applications. It must support direct human interaction and automation without assuming that one remote-desktop protocol, VM system or semantic driver defines the application itself.

The inspected donors solve different layers:

- E2B Desktop supplies graphical sandbox/API patterns.
- Xpra supplies reconnectable individual Linux application windows and desktops.
- Apache Guacamole supplies a browser gateway over RDP, VNC and SSH.
- noVNC/websockify supplies a lightweight browser VNC path.
- QEMU/libvirt supplies VM lifecycle, hardware, storage and snapshots.
- FreeRDP supplies RDP protocol and channels.
- FlaUI supplies direct Windows UIA2/UIA3 automation.
- NovaWindows supplies modern Appium/W3C Windows automation while remaining early and PowerShell-backed.
- Appium Windows/WinAppDriver is a legacy compatibility path.
- Peekaboo supplies macOS windows, accessibility context, screenshots and input.
- Appium XCUITest and IDB supply iOS/iPadOS/tvOS simulator/device control and semantic automation.
- Apple Xcode, Simulator, XCTest and Virtualization are required proprietary platform foundations for Apple workloads.
- ADR-0009 already defines Device, lease, stream, input and semantic Screen Context guarantees.

No donor owns Ptah's Application identity, provider placement, Workspace relationship, process/window lifecycle, checkpoint, privacy or proof model.

## Decision

Ptah will own separate backend-neutral contracts for:

1. Application Object;
2. Application Provider;
3. Application Installation;
4. Application Session;
5. Process;
6. Window and Display Surface;
7. Display Gateway;
8. Input and clipboard channels;
9. Semantic Screen Context;
10. Session checkpoint and recovery;
11. recording/evidence Artifacts;
12. platform-specific credential/licence dependencies.

A VM, container, native host, remote desktop connection, automation session and window handle are implementation references rather than canonical Application identity.

---

# Application Object

An Application Object describes the installable/runnable software independently of a running instance.

```text
application_object_id
object_id_or_source_reference
application_type
platforms
architectures
package_or_bundle_identity
version
publisher_or_signature_claims
entry_points
runtime_requirements
installation_requirements
licence_reference
provenance_references
verification_state
```

Application types include:

```text
linux_native
linux_package
windows_exe
windows_msi
windows_msix_or_uwp
macos_app
macos_pkg
ios_ipa
ios_app_bundle
android_apk_or_bundle
web_application
containerized_application
virtual_machine_application
```

Static package decomposition remains governed by ADR-0007. Application execution never changes the original package Object.

---

# Application Provider

An Application Provider is a Node-attached environment capable of installing and running one or more application classes.

```text
application_provider_id
node_id
provider_type
platform
architecture
os_version
runtime_versions
capabilities
resource_capacity
user_session_model
display_backends
semantic_backends
checkpoint_classes
health
worker_generation
```

Provider types include:

```text
native_linux
oci_linux_desktop
linux_vm
native_windows
windows_vm
native_macos
macos_vm
ios_simulator
physical_ios_device
android_emulator
physical_android_device
remote_application_service
```

The provider advertises what it can execute; Ptah does not infer compatibility from file extension alone.

## Provider versus Workspace

A Workspace may use one or more Application Providers. The provider supplies runtime machinery while the Workspace supplies Objects, revisions, permissions and Activities.

## Placement

Placement considers:

- platform/architecture;
- application/package compatibility;
- required GPU, display, audio, USB/device or network capabilities;
- licence/activation availability;
- installed runtime/tool versions;
- resource capacity and current load;
- caller restrictions and data locality;
- checkpoint/recovery class;
- privacy and trust class.

---

# Installation

Installation is a separate Activity and state from execution.

```text
application_installation_id
application_object_id
provider_id
workspace_id
installed_identity
installed_version
signature_or_publisher_readback
install_location_reference
user_or_machine_scope
installed_at
verification_state
cleanup_reference
```

States include:

```text
planned
installing
installed
verification_failed
repairing
updating
uninstalling
removed
cleanup_failed
```

Installer exit code alone is insufficient. Where possible, Ptah reads back package/bundle identity, version, signature/publisher and installed files/registration.

---

# Application Session

An Application Session represents one running application instance or logical application context.

```text
application_session_id
application_object_id
application_installation_id
workspace_id
provider_id
provider_worker_generation
user_session_id
process_ids
window_ids
stream_ids
semantic_context_ids
started_at
state
checkpoint_references
privacy_profile
```

States include:

```text
preparing
launching
process_running
first_window_waiting
visible
semantic_ready
backgrounded
suspended
recovering
crashed
stopping
stopped
closed
failed
```

Process launch, first window, first frame, semantic readiness and expected application state are distinct proof levels.

---

# Process boundary

A process record is one OS-level execution instance:

```text
process_id
application_session_id
provider_process_reference
parent_process_id
executable_object_or_path_reference
arguments_reference
working_directory
user_identity_reference
started_at
exit_state
resource_usage
```

A multi-process application may have several process records under one Application Session. Process IDs are provider-local and never canonical identity by themselves.

Process restart does not automatically preserve Application Session state or authorize replay of earlier side effects.

---

# Window and display surface

A Window is a provider-observed application surface:

```text
window_id
application_session_id
backend_window_reference
title_claim
role
bounds
display_id
workspace_or_space_reference
z_order_or_visibility
captured_at
state
```

Window handles, X11 IDs, accessibility IDs, RDP surfaces and Xpra IDs are aliases with capture/generation metadata.

States include:

```text
created
visible
hidden
minimized
occluded
closed
stale
unknown
```

Window visibility is not semantic readiness or functional correctness.

## Display Surface

A display surface may represent:

- one application window;
- one desktop/session;
- one VM console;
- one mobile-device display;
- one virtual display;
- several monitors.

The display surface produces video/frame streams separately from input and semantic context.

---

# Display Gateway

A Display Gateway translates provider-native display protocols into browser/native client streams.

Gateway backends include:

- Xpra/Xpra HTML5;
- Guacamole over RDP/VNC;
- noVNC/websockify;
- scrcpy;
- platform-native display APIs;
- future WebRTC gateways.

A gateway does not own provider lifecycle or Application Session identity.

## Gateway session

```text
gateway_session_id
application_session_id_or_device_session_id
gateway_backend
backend_connection_reference
approved_target_reference
capability_scope
issued_at
expires_at
stream_ids
state
```

Browser/client credentials are short-lived and scoped to one approved target/session.

## Channel separation

The following are independently advertised and authorized:

```text
display_read
input_control
clipboard_read
clipboard_write
file_transfer
audio_output
audio_input
printing
notifications
usb_or_device_redirection
recording
```

A read-only display token cannot send input or clipboard changes.

---

# Semantic UI boundary

Semantic Screen Context remains independent of pixel/display gateways.

Platform backends include:

- AndroidX UI Automator, Appium UIAutomator2 and TouchPilot;
- FlaUI UIA2/UIA3 and NovaWindows/Appium;
- Peekaboo Accessibility tools;
- Appium XCUITest/XCUIAutomation;
- future Linux accessibility/AT-SPI adapters.

A semantic backend observes one Application Session/Window/context at a capture time and generation. Element/window references can become stale.

Visual and semantic observations may disagree. Ptah records both, coverage and limitations rather than silently selecting one as truth.

---

# Platform directions

## Linux

- native Linux/OCI Workspace Provider launches application processes;
- Xpra is the primary individual-window/reconnectable display backend candidate;
- Guacamole/VNC and noVNC are desktop/compatibility paths;
- a future AT-SPI semantic adapter is required before claiming full Linux semantic automation;
- Wayland/X11/compositor support is advertised explicitly.

## Windows

- native Windows Node and QEMU/libvirt Windows VM are separate provider classes;
- QEMU/libvirt is the primary Windows VM Provider candidate on Linux/KVM;
- FreeRDP/Guacamole is the primary RDP browser-display path;
- FlaUI is the primary direct native semantic backend donor;
- NovaWindows is the primary W3C/Appium candidate, but remains early and PowerShell-backed;
- Appium Windows/WinAppDriver remains legacy compatibility only.

## macOS

- native macOS Node is the primary provider for native applications;
- Peekaboo is the primary native visual/accessibility automation backend candidate;
- Apple Virtualization provides macOS VM lifecycle on supported Apple silicon;
- platform permissions are capability state, not assumed access;
- Xpra/Guacamole-style remote presentation may be added only after native compatibility proof.

## iOS/iPadOS/tvOS

- macOS Node hosts physical-device and Simulator providers;
- IDB supplies remote companion/device-lab primitives;
- Appium XCUITest supplies W3C semantic automation;
- Xcode/Simulator/XCTest and Apple signing/provisioning remain mandatory platform dependencies;
- simulator and physical-device results remain separate proof classes.

---

# Checkpoint and recovery

Checkpoint classes include:

```text
none
process_restart_only
application_managed_state
workspace_files_only
container_checkpoint
vm_disk_snapshot
vm_memory_and_disk_snapshot
application_consistent_snapshot
provider_native_session_resume
```

A provider declares supported classes and limitations.

## Recovery rules

- display reconnection alone does not prove process or application continuity;
- process restart alone does not prove state restoration;
- VM snapshot restore does not prove guest application consistency;
- application-consistent recovery requires guest/application quiesce or explicit state export plus read-back;
- stale windows, streams and semantic contexts from an earlier provider generation are rejected;
- non-idempotent application side effects are never replayed blindly.

---

# Recording and evidence

Screenshots, video, audio, UI trees, logs and input traces become protected Artifacts linked to exact Session/Window/Activity/operation IDs.

Recording states include:

```text
requested
started
capturing
stopped
finalizing
verified
failed
```

A recording proves what the capture backend observed, not caller intent or semantic correctness.

Privacy/retention policies apply to:

- screen content;
- audio;
- clipboard;
- file transfer;
- UI hierarchy/text;
- notifications;
- account/session data;
- credentials visible in dialogs.

---

# Security and credentials

Credentials remain opaque references:

- OS user/login;
- RDP/VNC/SSH;
- Apple Developer/signing/provisioning;
- application licence/activation;
- browser/gateway token;
- platform keychain or certificate.

Display gateways cannot accept arbitrary target hosts/ports from callers. Targets are resolved from an approved Provider/Session reference.

PowerShell, shell, AppleScript, arbitrary command execution and host-device passthrough are separate high-risk Facilities, not semantic UI actions.

---

# Donor decisions

- **Xpra:** primary individual Linux application/window display candidate; GPL service boundary.
- **Guacamole:** primary cross-protocol browser remote-desktop gateway candidate.
- **noVNC/websockify:** lightweight VNC/browser compatibility backend.
- **QEMU/libvirt:** primary Windows/Linux VM Provider machinery candidate.
- **FreeRDP:** primary RDP protocol backend.
- **FlaUI:** primary direct Windows semantic donor.
- **NovaWindows:** primary modern W3C Windows candidate; early-stage and isolated.
- **Appium Windows/WinAppDriver:** legacy compatibility only.
- **Peekaboo:** primary macOS native visual/accessibility automation candidate; agent identity excluded.
- **Appium XCUITest:** primary iOS W3C semantic backend candidate.
- **IDB:** primary remote Apple device/simulator companion donor.
- **Apple Xcode/Simulator/XCTest/Virtualization:** mandatory proprietary platform foundation for Apple workloads.

All remain behind Ptah-owned contracts and conformance tests.

---

# Consequences

## Positive

- Applications remain identifiable across provider, display and automation backend replacement.
- Native, container, VM, simulator and physical-device applications share one lifecycle model.
- Browser pixels, windows, processes and semantic elements no longer impersonate one another.
- Multiple unrelated applications and windows can run concurrently.
- Direct human interaction and automation can share the same Application Session with separately scoped controls.
- Platform-specific dependencies remain explicit rather than hidden behind generic promises.
- Checkpoint claims become honest and provider-specific.

## Costs

- Application, installation, process, window, gateway and checkpoint schemas are required.
- Linux semantic automation still needs an AT-SPI donor pass later.
- Platform-specific provider testing and licensing are substantial.
- Several display and semantic backends must be maintained.
- Visual and semantic evidence disagreement requires explicit UI/status handling.
- Apple workloads require owned/approved Mac hardware and proprietary tooling.

## Do-not-break rule

> Never treat package installation, process launch, VM running state, remote-desktop connection, first frame, window presence, semantic element action or display reconnect as universal application completion. Application Object, Provider, Installation, Session, Process, Window, Display Gateway, Semantic Context and verified outcome have separate identities and guarantees.

---

# Required proof before freeze

1. Launch Linux, Windows and macOS applications under distinct provider classes and retain one neutral Application Session model.
2. Run several independent applications/windows concurrently without stream, input or identity cross-talk.
3. Replace one display gateway while preserving Application Session identity.
4. Replace one semantic backend and preserve selector intent plus receipt identity.
5. Prove package installed, process started, first window, first frame, semantic ready and expected state as separate levels.
6. Reconnect a display client without falsely claiming process/application recovery.
7. Restore a VM checkpoint and independently verify guest/application consistency.
8. Enforce separate permissions for display, input, clipboard, files, audio, printing and recording.
9. Reject stale window/semantic/gateway results after provider or worker generation changes.
10. Run iOS Simulator and physical-device flows with separate proof classes.
11. Protect Apple signing, OS login and application-licence credentials from logs/public records.
12. Record screenshots/video/UI trees as privacy-classified Artifacts linked to exact Sessions and operations.
