# Donor Record — DeviceFarmer minicap

**Phase:** 0A / WP07  
**Status:** FIRST-PASS COMPLETE — LEGACY ANDROID DISPLAY-STREAM DONOR, COMPATIBILITY BACKEND ONLY  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/DeviceFarmer/minicap
- Default branch: `master`
- Pinned commit: `f3d40d65da0cc7168846c4ae7466ada970441d4e`
- Licence: Apache-2.0
- Primary language: C/C++ with NDK/AOSP shared-library builds
- Activity: Maintenance / compatibility updates
- Classification: Android real-time JPEG screen-capture socket backend
- Ptah targets: `DEVICE-002`, display stream, screenshot, projection/orientation metadata and remote-device visual proof

## Files/components inspected

- `README.md`
- `LICENSE`
- `jni/minicap/minicap.cpp`

## Verified capabilities and patterns

### Capture model

- Runs on the Android device and exposes a socket interface intended for a larger controller.
- Uses private AOSP capture APIs: older ScreenshotClient paths and newer virtual-display paths.
- Encodes frames as JPEG through libjpeg-turbo.
- Supports configurable physical/virtual projection, orientation, JPEG quality, display ID and frame rate.
- Can run a test-only compatibility probe before opening a long-lived stream.
- Can take a single screenshot to standard output.
- Can skip frames when a consumer cannot keep up.

### Stream protocol

- Opens an abstract Unix-domain socket, commonly forwarded through ADB to a host TCP port.
- Sends a one-time 24-byte global header containing protocol version, process ID, real/virtual dimensions, orientation and quirk flags.
- Sends each subsequent JPEG frame with a little-endian length prefix.
- Reports quirks for unchanged-frame behavior, always-upright output and possible tearing.
- Supports one consumer connection at a time.

### Performance and lifecycle

- Can reach smooth frame rates on supported devices, especially when downscaled.
- Sends only changed frames on Android 4.2+.
- Handles SIGINT/SIGTERM and stops its frame waiter.
- Uses a pending-frame queue and optional frame dropping for backpressure.
- Socket writes suppress SIGPIPE and return errors when the consumer disappears.

### Compatibility selection

- Requires ABI-specific binary and SDK/ABI-specific shared library.
- Requires callers to obtain screen size/projection and orientation separately.
- Provides a test command to detect unsupported/segfaulting combinations.
- Supports explicit socket names, enabling more than one named provider process when carefully coordinated.

## What minicap completes

- A concrete low-latency display-stream protocol with display/projection/orientation metadata.
- A device-side capture process separated from host rendering.
- Compatibility probing before session readiness.
- Frame dropping/backpressure behavior.
- Screen stream and one-shot screenshot as distinct operations.
- Evidence that device display metadata and frame stream must be versioned and correlated.

## Important limitations for Ptah

- Rootless operation is documented only through Android 9/API 28 and lower; newer Android support is not a safe assumption.
- It relies on private AOSP APIs and SDK/architecture-specific shared libraries.
- OEMs can break compatibility; unsupported devices may hang or segfault.
- Emulators are explicitly unsupported.
- Precompiled shared libraries require provenance, hashes, ABI/SDK compatibility and malware/licence review.
- One connection at a time is supported.
- JPEG frames are lossy and do not prove semantic UI state or exact pixel identity.
- Frame arrival does not prove the corresponding application is ready, foreground, interactive or unchanged after transmission.
- Projection/orientation can become stale during rotation or display changes.
- The protocol has no authentication, encryption, lease token, session ID or operation correlation.
- The process ID and socket name are backend-local values, not Ptah Device/Session identity.
- Display streams may contain passwords, personal messages, account details and other sensitive data.
- ADB forwarding and helper deployment require separate authorization and cleanup.
- Private API dependence makes it a compatibility backend, not the future primary Android display foundation.

## Must not be inherited

- a JPEG stream treated as semantic UI truth;
- process/socket/port used as Device or Session identity;
- private-API compatibility inferred only from Android version;
- ABI/SDK helper filename used as sufficient provenance or compatibility proof;
- one unscoped display stream shared across users/workspaces;
- stale projection/orientation silently applied after rotation or reconnect;
- screen frames routed through the control Event Fabric;
- frames persisted or exposed without sensitive-data policy;
- test command success promoted to long-running stream readiness without first-frame proof;
- automatic helper restart during a stale or expired Device lease.

## Integration decision

**WRAP AS AN OPTIONAL LEGACY/COMPATIBILITY DISPLAY BACKEND; DO NOT MAKE IT THE PRIMARY ANDROID DISPLAY ENGINE.**

Ptah should model minicap as one implementation of a neutral Display Facility. The provider must deploy the exact helper Object, probe compatibility, establish a versioned stream, register the first valid frame and preserve capture metadata and helper provenance.

## Native Ptah gap

Ptah must define:

- Display, Display Session and Display Stream identities;
- stable Device and connection-epoch binding;
- physical dimensions, logical dimensions, density, orientation, crop and projection schema;
- codec/pixel format, quality, frame rate, timestamps and sequence numbers;
- stream readiness levels: helper launched, socket listening, header validated, first frame decoded, continuous health;
- rotation/display-change events and generation changes;
- frame backpressure, dropping and latency metrics;
- screenshot/recording Artifact relationships;
- lease/fencing and capability-scoped authorization;
- encryption and transport authentication;
- helper Object hashes, source, licence, ABI/SDK/API compatibility and deployment receipts;
- sensitive-screen classification, retention, redaction and viewer audit;
- alternate scrcpy/MediaProjection/OEM/backend conformance.

## Exit strategy

The Display Facility is backend-neutral. scrcpy, Android MediaProjection, minicap, Appium screenshots, emulator display APIs, OEM farms or future platform services can implement the same Display Session and Stream contracts.

## Validation required

1. Select exact ABI/SDK helper Objects and reject a mismatched binary/shared-library pair.
2. Run compatibility probe, start stream, validate header and decode the first frame before READY.
3. Rotate the device and require a new display/projection generation rather than silently reusing stale coordinates.
4. Slow the consumer and verify bounded frame dropping/backpressure without memory growth.
5. Disconnect/reconnect ADB and reject frames from the previous connection epoch.
6. Expire the Device lease and terminate/deny the stream to the stale viewer.
7. Capture a screenshot and recording as separate hashed Artifacts with exact metadata.
8. Prove unsupported/newer Android devices fail honestly and fall back to another backend.
9. Run simultaneous streams from multiple devices without socket/port cross-talk.
10. Replace minicap with scrcpy or another provider without changing Display Session identity semantics.
