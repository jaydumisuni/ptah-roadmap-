# Donor Record — Apple Native Runtime Foundations

**Phase:** 0A / WP07B  
**Status:** FIRST-PASS COMPLETE — OFFICIAL PROPRIETARY PLATFORM FOUNDATION, NOT REUSABLE SOURCE DONOR  
**Inspected:** 2026-07-17

## Identity

- Official references:
  - https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices
  - https://developer.apple.com/documentation/xctest/
  - https://developer.apple.com/documentation/virtualization
  - https://developer.apple.com/documentation/virtualization/running-macos-in-a-virtual-machine-on-apple-silicon
- Provider: Apple
- Licence/source status: proprietary platform frameworks, Xcode toolchain, SDKs and documentation; use is governed by Apple platform and developer agreements
- Classification: official Apple platform dependency and behavior reference
- Ptah targets: `APP-004`, macOS VM Provider, iOS Simulator/Device Provider, Xcode build/run destinations, XCTest/XCUIAutomation and Apple-host capability boundaries

## Official capabilities and patterns verified

### Xcode devices and simulators

- Xcode selects a build scheme and a simulated or physical run destination.
- Simulator supports iOS, iPadOS, tvOS, visionOS and watchOS configurations installed on a Mac.
- Physical-device use requires pairing, Developer Mode where applicable, signing and provisioning.
- Simulator does not replicate every physical-device hardware feature or performance characteristic.
- Physical-device and Simulator results therefore have different proof strength.
- Xcode/Device Hub shows target status and provides interactive display for running applications.

### XCTest and XCUIAutomation

- XCTest supplies unit, performance and UI testing integrated with Xcode.
- XCUIAutomation interacts with application UI and validates interaction flows.
- Test activities may retain attachments such as files and screenshots.
- XCTest/XCUIAutomation remains a testing/automation framework, not Ptah's Device or Application Session model.

### Apple Virtualization framework

- Creates and manages macOS and Linux virtual machines on supported Mac hosts.
- Configures virtual CPUs, memory, network, storage, sockets, serial and other VIRTIO-style devices.
- macOS guests use Apple-provided restore images and Apple platform/hardware configuration.
- Official sample code installs macOS from an IPSW restore image into a VM bundle containing disk, auxiliary storage, hardware model and machine identifier state.
- VMs can start, pause, resume and restore saved machine state.
- `VZVirtualMachineView` presents the graphical display and handles keyboard/mouse input.
- macOS virtualization is tied to supported Apple hardware/OS behavior and is not a general cross-platform VM backend.

## What the official platform completes

- The authoritative boundary for Xcode builds, platform SDKs, simulators, physical-device pairing and Apple code signing.
- The official macOS/iOS semantic testing foundation beneath Appium XCUITest.
- A supported macOS VM Provider path on Apple silicon.
- Native VM display/input and saved-state foundations.
- A clear requirement that Apple workloads remain on compatible macOS/Apple hardware Nodes.

## Important limitations for Ptah

- Xcode, SDKs, Simulator, signing/provisioning and Virtualization are proprietary platform dependencies.
- Apple workloads cannot be fully reproduced on arbitrary Linux/Windows Nodes.
- Simulator is not physical-device proof.
- macOS guest virtualization requires compatible Apple host hardware and restore images.
- VM saved state, disk bundle and Apple identity/hardware-model data have different portability constraints.
- Moving a macOS VM between hosts can alter platform identity and account/service behavior.
- An Xcode build/run success does not prove application functional correctness.
- Apple Developer credentials, certificates, profiles and account state are sensitive and caller/operator owned.
- VM display state does not provide semantic application context by itself.
- Apple tool/platform versions change compatibility and must be pinned per Node.

## Must not be inherited

- proprietary Apple tools or SDKs redistributed as public Ptah source/dependencies without permission;
- simulated-device success promoted to physical-device acceptance;
- Mac hardware/VM identity treated as portable across hosts without reconciliation;
- Xcode run destination or Simulator UUID as canonical Ptah Device identity;
- signing/account credentials stored in recipes, logs or public configuration;
- VM saved state treated as complete application-consistent checkpoint without proof;
- Apple-only constraints embedded in generic Application Provider contracts.

## Integration decision

**TREAT APPLE TOOLING AS A REQUIRED PLATFORM PROVIDER DEPENDENCY, NOT A CODE DONOR.**

Recommended provider classes:

1. native macOS Application Provider on a macOS Node;
2. iOS Simulator Provider through Xcode/Simulator tooling;
3. physical iOS Device Provider through paired macOS Nodes;
4. macOS VM Provider through Apple Virtualization on supported Apple silicon;
5. Xcode Build Facility for Apple application builds/signing.

Ptah owns neutral identities, Activities, Objects, credentials references, Sessions, proof and backend capability records.

## Native Ptah gap

Ptah must define:

- Apple Node capability and Xcode/SDK/platform-support inventory;
- Simulator, physical Device and macOS VM provider manifests;
- scheme, run-destination and build-output records;
- signing/provisioning/account credential references;
- physical-versus-simulator proof classification;
- VM bundle/saved-state/disk/hardware-model Object relationships;
- Apple host identity and VM portability limitations;
- application launch, first frame, semantic readiness and test-result receipts;
- protected XCTest attachments and logs;
- provider replacement/upgrade and compatibility tests.

## Exit strategy

There is no complete non-Apple replacement for Apple-native build, Simulator and physical-device tooling. Ptah remains provider-neutral but records Apple tooling as a mandatory capability for Apple workloads. Third-party adapters such as Appium and IDB remain replaceable above the platform.

## Validation required

1. Inventory exact Xcode, SDK and installed platform-support versions on a macOS Node.
2. Build and run one application on Simulator and one physical device with separate proof classes.
3. Capture XCTest/XCUIAutomation results and attachments as Artifacts.
4. Create, start, pause, save, restore and display a macOS VM on supported Apple silicon.
5. Verify VM disk, saved state and hardware/platform identifiers as separate Objects.
6. Move/recreate a VM or simulator and reconcile identity changes rather than silently retaining stale Session identity.
7. Keep signing/account credentials out of logs and public records.
8. Upgrade Xcode/platform support and run compatibility/conformance tests before provider promotion.
