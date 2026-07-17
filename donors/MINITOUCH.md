# Donor Record — DeviceFarmer minitouch

**Phase:** 0A / WP07  
**Status:** FIRST-PASS COMPLETE — RAW ANDROID MULTITOUCH INPUT DONOR, HIGH-RISK COMPATIBILITY BACKEND  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/DeviceFarmer/minitouch
- Default branch: `master`
- Pinned commit: `1773320a0992203a37245faf9beaa058992aedc7`
- Licence: Apache-2.0
- Primary language: C with libevdev/Android NDK
- Activity: Maintenance
- Classification: device-side raw multitouch injection socket backend
- Ptah targets: `DEVICE-002`, raw contact input, gestures, coordinate mapping, input capability negotiation and input-session safety

## Files/components inspected

- `README.md`
- `LICENSE`
- `jni/minitouch/minitouch.c`

## Verified capabilities and patterns

### Input model

- Runs on the Android device and opens an abstract Unix-domain socket or accepts commands through stdin/file mode.
- Exposes explicit touch-down, move, touch-up, commit, reset and wait commands.
- Supports multiple simultaneous contacts and gestures such as tap, swipe and pinch.
- Separates queued contact changes from `commit`, making an input frame/transaction boundary explicit.
- Provides a reset operation that attempts to release active contacts and commit the clean state.

### Capability negotiation

- Sends protocol version first.
- Sends maximum contacts, X, Y and pressure values reported by the selected touch device.
- Sends the helper process ID.
- Requires callers to map display coordinates to touch-device coordinates rather than assuming they match.
- Allows explicit touch-device selection or internal autodetection.

### Device selection

- Inspects input character devices through libevdev.
- Requires multitouch position capabilities.
- Scores candidate devices using slot/contact count, direct-input property, resolution and name heuristics.
- Penalizes keypad/side-sense-like devices and tends to prefer larger direct touch surfaces.
- Supports a maximum of ten contacts in the inspected implementation.

### Android compatibility

- Historically works without root on older Android releases through direct input-device access.
- Android 10+ requires a service/agent forwarding workaround such as STFService because of tightened security policy.
- Uses ABI-specific binaries and older NDK/libevdev build machinery.

## What minitouch completes

- A compact raw multitouch protocol with capability negotiation.
- A clear distinction between contact updates and committed visible input.
- Coordinate-space mismatch handling requirements.
- A reset/release operation for recovering potentially stuck contacts.
- Evidence that input provider selection and contact-state integrity are safety-critical.
- A lower-level input backend separate from semantic application automation.

## Important limitations for Ptah

- Android 10+ does not work directly by default and requires STFService or another privileged/accessibility bridge.
- Direct input-device access depends heavily on device/ROM security and permissions.
- Only one connection is supported because multiple writers can corrupt the event stream.
- The protocol returns only initial metadata; there are no per-command acknowledgements or authoritative action results.
- Malformed, lost or out-of-order contact sequences can freeze device input and require reboot.
- Reset is best-effort and cannot prove the target UI accepted or acted on input.
- Autodetection uses heuristics and may still choose the wrong touch surface on unusual devices.
- Touch-device coordinate ranges usually differ from display pixels.
- Screen rotation, insets, cutouts, fold states and secondary displays complicate mapping.
- Process/socket identity is not a Ptah Input Session identity.
- The protocol is unauthenticated and unencrypted.
- Raw input is highly sensitive and can confirm dialogs, submit payments, expose data or trigger destructive operations.
- Input commands are non-idempotent; network or provider retry can duplicate touches.
- Helper binaries/submodules require provenance, hashes and exact ABI/API compatibility evidence.
- This backend cannot provide semantic element identity, text/action intent or accessibility-state verification.

## Must not be inherited

- input permission implied by display-view permission;
- multiple independent writers to one physical input surface;
- automatic retry of taps, gestures, text entry or confirmation actions;
- display pixels passed directly as touch coordinates without a versioned mapping;
- helper startup or socket connection treated as proof that an input occurred;
- input completion inferred without post-action screen/semantic observation;
- process/socket/port used as Device/Input Session identity;
- heuristic touch-device selection accepted without capability/probe evidence;
- stale input session continuing after rotation, reconnect or lease expiry;
- raw input exposed without strong user/workspace authorization and audit;
- minitouch used as a semantic UI backend.

## Integration decision

**WRAP ONLY AS AN OPTIONAL RAW-INPUT COMPATIBILITY BACKEND WITH STRICT EXCLUSIVE LEASE AND NO AUTOMATIC RETRY.**

Ptah must treat minitouch as one implementation of a Raw Input Facility. Every input batch must bind to an exact Device, display generation, coordinate transform, input-session generation and lease fencing token. Higher-level semantic actions must remain a separate Facility.

## Native Ptah gap

Ptah must define:

- Input Session and Input Stream identities;
- stable Device, interface and connection-epoch binding;
- exclusive writer lease/fencing;
- raw pointer/contact/key/text/clipboard capability groups;
- display-to-input coordinate transform with orientation, scaling, crop, insets and fold/display generation;
- input transaction/batch, sequence number and no-retry policy;
- contact-state machine and guaranteed release-on-close procedure;
- provider/helper provenance and compatibility manifest;
- readiness levels: helper launched, socket connected, header validated, mapping accepted, reset state confirmed;
- post-action observation/evidence through display or semantic UI providers;
- sensitive-action policy, confirmation and audit;
- late/stale command rejection;
- fallback to scrcpy, Accessibility/UIAutomator/Appium or OEM/emulator input APIs;
- bounded input rate and abuse protection.

## Exit strategy

The Raw Input Facility remains backend-neutral. scrcpy control, minitouch, Android input commands, AccessibilityService, UIAutomator, emulator APIs or OEM device-farm controls can implement separate capability sets without changing Ptah Input Session semantics.

## Validation required

1. Negotiate protocol/capabilities and reject unsupported versions or impossible coordinate ranges.
2. Compare display and touch coordinate spaces and prove the selected transform on all four corners.
3. Rotate/change display generation and reject commands encoded for the previous mapping.
4. Send tap, swipe and pinch batches with exact sequence receipts and no blind retries.
5. Break a gesture mid-stream and release/reset all contacts without leaving the device frozen.
6. Attempt a second writer and enforce exclusive input-session fencing.
7. Expire the Device lease and reject all subsequent contact commands.
8. Verify every important input through a later display or semantic-state observation rather than protocol optimism.
9. Fail honestly on Android 10+ without an approved helper/service and select a different backend.
10. Replace minitouch with scrcpy/Appium input while preserving the Ptah Raw Input contract.
