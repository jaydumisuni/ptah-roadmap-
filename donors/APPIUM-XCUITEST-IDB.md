# Donor Record — Appium XCUITest Driver and IDB

**Phase:** 0A / WP07B  
**Status:** FIRST-PASS COMPLETE — IOS DEVICE/SIMULATOR AND SEMANTIC AUTOMATION DONOR SET  
**Inspected:** 2026-07-17

## Identity

### Appium XCUITest Driver

- Canonical URL: https://github.com/appium/appium-xcuitest-driver
- Default branch: `master`
- Pinned commit: `1f2cf57ee5e7480d824a923d5e7ac06c3d4a109b`
- Pinned package version: `11.17.7`
- Licence: Apache-2.0
- Compatibility: Appium 3 since driver major version 10

### IDB

- Canonical URL: https://github.com/facebook/idb
- Default branch: `main`
- Pinned commit: `d2ac8d7466e2a0b7e0ce5b67a7b8c59e4ac8a44f`
- Licence: MIT
- Runtime: macOS companion plus remote Python/CLI client

- Classification: iOS/iPadOS/tvOS simulator/physical-device control and semantic application-automation donor composition
- Ptah targets: `APP-004`, Apple Device Provider, iOS Simulator Provider, application installation/launch, WebDriver semantic UI, remote device labs and Application Sessions

## Files/components inspected

- XCUITest Driver `README.md`
- XCUITest Driver `package.json`
- XCUITest capabilities documentation
- IDB `README.md`
- Appium core boundary from WP07A
- official Apple Xcode/XCTest/Device Hub runtime documentation

## Verified capabilities and patterns

### Appium XCUITest Driver

- Automates native and hybrid applications on iOS, iPadOS and tvOS.
- Uses Appium core as W3C protocol host and XCUITest/WebDriverAgent as the device-side backend.
- Supports simulators and physical devices.
- Depends on Xcode, WebDriverAgent, simulator tooling, device tooling, remote debugger and platform-specific packages.
- Supports `.ipa`, `.app` and zipped `.app` application inputs plus bundle-ID attachment.
- Supports application installation, launch, reset modes, localization, Safari/WebView contexts and real-device operations.
- Physical-device selection should use an exact UDID, especially for parallel work.
- WebDriverAgent build, signing, bundle ID, provisioning profile, derived-data path, host/device ports and startup/reuse are separately configurable.
- Reusing an existing WDA is recommended for real-device stability and speed rather than reinstalling it for every session.
- Driver includes separate functional tests for devices, parallel execution, web contexts and other paths.

### IDB

- Splits a macOS companion from a Python/CLI client that can run elsewhere.
- Attaches one companion process to each simulator/device target.
- Supports remote device labs and sharded workloads over pools of simulators.
- Exposes granular primitives intended to be sequenced by higher-level workflows.
- Aims for consistent operations across iOS versions and between physical devices and simulators.
- Lists targets, installed applications and runtime state, and launches applications.
- Uses FBSimulatorControl and FBDeviceControl frameworks included in the repository.
- Leverages private Xcode/macOS frameworks for functionality not exposed by public tooling.
- Requires Xcode and macOS for the companion/build side.

## What this donor set completes

- A practical iOS Simulator and physical-device Provider architecture.
- Remote Mac-hosted companion processes controlled by clients on other Nodes.
- W3C/Appium semantic application automation through XCUITest.
- Exact simulator/device target selection and per-target companion concepts.
- App installation, launch, inspection, WebView/Safari contexts and parallel sessions.
- A device-lab topology in which macOS hosts remain near Apple tooling while callers can be remote.
- Reusable/prebuilt WebDriverAgent and derived-data isolation requirements.

## Important limitations for Ptah

- Xcode, Apple SDKs, device support, code signing and provisioning are proprietary Apple platform dependencies.
- Physical iOS device automation requires a Mac host and valid signing/provisioning for WebDriverAgent.
- Simulator behavior does not prove physical-device behavior or hardware-specific features.
- IDB relies on private frameworks and may break across Xcode/macOS releases.
- UDID, Appium session ID, WDA URL/port and IDB companion ID are backend/transport identities, not Ptah Device identity.
- Application installation success does not prove installed bundle/version/signature or successful launch/readiness.
- `noReset`/`fullReset` semantics do not guarantee complete account/data cleanup on physical devices.
- WDA reuse improves stability but increases stale-session/ownership risks if not fenced.
- Signing keys, certificates, profiles and keychain passwords are highly sensitive credential references.
- Appium/XCUITest semantic trees may be incomplete for custom rendering, secure surfaces and games.
- IDB private-framework use and Apple licence terms require continuous compatibility/legal review.
- Neither donor provides Ptah lease, privacy, Activity, Artifact, backup or authoritative cleanup truth.

## Must not be inherited

- UDID or WDA/Appium/IDB session IDs used as canonical Ptah Device/Application Session identity.
- signing keys, profile secrets or keychain passwords stored in recipes, logs or public source.
- automatic reuse of an existing WDA without lease/owner/epoch verification.
- simulator success promoted to physical-device proof.
- install/launch command acknowledgement promoted to application readiness.
- arbitrary remote WDA URLs or companion endpoints exposed to callers.
- private-framework behavior described as stable Apple public API.
- cleanup/reset flags treated as verified data removal.
- Appium capability schema exposed as Ptah's canonical application contract.

## Integration decision

**ADOPT APPIUM XCUITEST AS THE PRIMARY IOS W3C SEMANTIC BACKEND CANDIDATE; ADAPT IDB AS THE PRIMARY REMOTE DEVICE/SIMULATOR COMPANION DONOR.**

Recommended architecture:

1. macOS Node hosts Xcode, simulators, physical-device connections and signed helper tools;
2. an Apple Device/Application Provider owns target discovery, companions and helper lifecycle;
3. IDB-like granular primitives supply inventory/install/launch/file/log/simulator operations;
4. Appium XCUITest supplies W3C semantic actions and hybrid/WebView compatibility;
5. Ptah owns Device identity, lease/fencing, connection epoch, Application Session and proof.

## Native Ptah gap

Ptah must define:

- stable Apple Device and Simulator identity;
- physical-device, simulator, companion and WDA interface epochs;
- macOS provider/worker identity and exact Xcode/platform-support versions;
- lease/fencing across WDA and IDB companions;
- application Object, bundle/version/signature and install-state record;
- simulator runtime/device-type configuration;
- signing certificate/profile/keychain credential references;
- WDA build/install/reuse and cleanup receipts;
- application launch, first frame, semantic-ready and expected-state proof;
- physical-versus-simulator proof classification;
- sensitive device/account/log/screenshot privacy rules;
- Xcode/private-framework compatibility matrix;
- backend replacement and device-lab conformance tests.

## Exit strategy

Ptah's Apple Device/Application contracts remain independent of Appium, XCUITest, WebDriverAgent and IDB. Xcode command-line tools, `devicectl`, `simctl`, alternative lab providers or future public Apple APIs may replace adapters without changing Device/Application Session identity.

## Validation required

1. Inventory several simulators and physical devices without identity collision.
2. Enforce exact target selection and lease fencing across parallel sessions.
3. Install an `.ipa`/`.app` and read back bundle ID, version and signing identity.
4. Reuse WDA only when target, lease, helper identity and connection epoch match.
5. Restart WDA/IDB companion and reject stale semantic results from the earlier generation.
6. Run the same application flow on simulator and physical device and retain separate proof classes.
7. Exercise native and WebView contexts without conflating their element identities.
8. Keep signing credentials out of logs, receipts and public configuration.
9. Verify cleanup/reset and quarantine the target when cleanup cannot be proven.
10. Replace one adapter without changing Ptah Device or Application Session identity.
