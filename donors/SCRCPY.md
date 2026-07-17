# Donor Record — scrcpy

**Phase:** 0A / WP07  
**Status:** FIRST-PASS COMPLETE — PRIMARY MODERN ANDROID DISPLAY/AUDIO/CONTROL BACKEND CANDIDATE  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/Genymobile/scrcpy
- Default branch: `master`
- Pinned commit: `2926c06c5dc3064ae6d8db706f1a98a37cfcf3f0`
- Pinned version: `4.1`
- Licence: Apache-2.0
- Primary languages: C host client and Java Android server
- Activity: Active
- Classification: modern Android screen/audio/control/recording/virtual-display backend
- Ptah targets: `DEVICE-002`, Android portions of `APP-002`-like display/session behavior, application/session extensions, screen/audio/input/clipboard/file transfer and recording

## Files/components inspected

- `README.md`
- `doc/develop.md`
- `doc/control.md`
- `doc/connection.md`
- `doc/virtual-display.md`
- `app/src/control_msg.h`
- repository licence text in README

## Verified capabilities and patterns

### Host/device split

- Consists of a host client and a Java server executed on the Android device as the `shell` user.
- The host pushes the version-matched server JAR to `/data/local/tmp` and starts it through `app_process`.
- Exact client/server versions are required; protocol compatibility is not promised across versions.
- A random `scid` identifies concurrent clients running on the same device.
- The device server is not left installed as an ordinary Android application.

### Separate media and control channels

- Uses separate sockets for video, audio and control; any one or two may be disabled, but not all.
- Dedicated threads handle each socket.
- Video and audio are one-way device-to-host streams.
- Control is bidirectional: host input/control messages go to the device and device messages such as clipboard updates return to the host.
- Default network-role inversion lets the host listen first and the device server connect, avoiding startup polling races.

### Video/display

- Captures screen, camera or virtual displays.
- Encodes video on-device using `MediaCodec`, H.264 by default, with other codecs/configurable size, bitrate and FPS.
- Restarts the encoding session on rotation or fold changes.
- Supports low-latency playback, optional buffering, no-playback recording, screen-off mirroring and configurable quality.
- Produces video packet headers and supports client-side decode, display, recording and Linux V4L2 output.
- Can create a new Android virtual display, resize it with the host window, start a chosen application, configure decorations/IME policy and destroy or preserve content on close.

### Audio

- Captures device output or microphone on supported Android versions.
- Encodes audio on-device, OPUS by default.
- Client can decode/play and mux audio/video into recordings.
- Audio forwarding requires Android 11/API 30+.

### Input and control

- Injects keycode, text, touch, scroll and system-panel/device commands.
- Supports SDK injection, UHID keyboard/mouse/gamepad and AOA/OTG modes.
- Provides control-only operation without video/audio.
- Supports read-only mode that disables input, clipboard and drag/drop interactions.
- Control protocol has bounded message sizes and explicit types for clipboard, display power, rotation, UHID lifecycle, starting apps, resetting video, camera controls, display resize and file scanning.
- Some control messages are marked non-droppable to preserve input/HID consistency.

### Clipboard and file operations

- Synchronizes clipboard in both directions by default.
- Allows disabling automatic clipboard synchronization.
- Warns that copying host clipboard content to Android exposes it to Android applications.
- Drag/drop can install APKs or push ordinary files to a configured target, then request media scanning.

### Device selection and transport

- Supports USB and TCP/IP ADB transport.
- Requires explicit serial/USB/TCP selection when multiple devices are present.
- Can switch/connect ADB TCP mode automatically.
- Supports OTG control without USB debugging for applicable HID control paths.

### Recording and artifacts

- Records encoded video/audio to MP4 or MKV on the host.
- Supports camera capture, webcam/V4L2 output and no-display/no-playback modes.
- Separates encoded stream, decoded display and recording paths.

## What scrcpy completes

- A modern Android display backend that avoids minicap's SDK-specific shared-library model.
- Explicit separation of video, audio and control channels.
- A robust host/device server version and session discriminator model.
- Low-latency encoded streams, recording and rotation/fold recovery.
- Multiple raw input strategies and control-only/read-only modes.
- Virtual display and application-start patterns useful for application sessions.
- Clipboard, file push, APK install and media-scan requirements.
- Cross-platform host support for Linux, Windows and macOS.

## Important limitations for Ptah

- scrcpy is a user-facing application, not a multi-tenant Device Provider, lease manager or durable Activity system.
- ADB serial remains the primary selector and is not a stable physical Device identity.
- `scid` distinguishes backend clients but is not a Ptah Session or lease identity.
- Control permissions are broad and can trigger sensitive or destructive actions.
- Input injection may require OEM-specific security settings and can fail despite a working video stream.
- Clipboard synchronization can expose passwords or other secrets to Android applications and the host clipboard.
- Drag/drop APK installation or file push has little user-visible feedback and still requires independent verification.
- A successful control-message write does not prove the device or foreground app applied the action.
- Video frames are encoded observations, not semantic UI state.
- Audio/video streams and recordings may contain sensitive personal content.
- Hidden Android APIs and reflection remain version/OEM compatibility risks.
- Exact client/server version coupling simplifies compatibility but requires helper provenance and coordinated upgrades.
- The pushed server JAR must be hashed, sourced and cleaned up; `/data/local/tmp` is safer than world-writable paths but not an authentication mechanism.
- USB/TCP ADB security and provider authentication are external responsibilities.
- Virtual display lifetime/content behavior varies by application and Android implementation.
- `--no-control` combines several interaction classes; Ptah needs finer capability permissions.
- OTG/AOA/UHID and normal ADB control are materially different transports and proof paths.
- Automatic TCP configuration changes device/network state and must be separately authorized.

## Must not be inherited

- “scrcpy connected” treated as one universal Device Session success;
- video readiness used to imply input readiness or application readiness;
- control socket permission granting clipboard, file install, system actions and raw input together;
- ADB serial or `scid` used as stable Device/Session identity;
- clipboard autosync enabled for sensitive workspaces by default;
- file/APK drop success inferred only from console output;
- raw control messages blindly retried after disconnect;
- stale coordinates/input accepted after rotation, fold, display resize or reconnect;
- screen/audio/control streams carried through the control Event Fabric;
- recordings retained without explicit policy and Artifact registration;
- server JAR filename/version used as sufficient provenance;
- TCP/IP enabling/reconnection performed without a scoped operation and receipt;
- virtual display close semantics assumed to preserve or destroy app state universally.

## Integration decision

**WRAP AS THE PRIMARY MODERN ANDROID DISPLAY/AUDIO/RAW-CONTROL BACKEND THROUGH A PTAH DEVICE PROVIDER.**

Ptah should not launch the stock interactive client as its only integration. It should either:

1. wrap scrcpy as a supervised external service/process with structured parsing and dedicated streams; or
2. adapt the Apache-2.0 client/server protocol components into a provider while maintaining upstream compatibility.

Capability groups must remain separate:

- screen video;
- camera video;
- audio output;
- microphone;
- recording;
- screenshot/frame evidence;
- SDK raw input;
- UHID/AOA/OTG input;
- clipboard read/write/autosync;
- file push;
- APK install;
- application start;
- physical display controls;
- virtual display lifecycle.

## Native Ptah gap

Ptah must define:

- Device, Device Interface, connection epoch and provider generation;
- Device Session, Display Session, Audio Session, Input Session and Application Session identities;
- exact lease/fencing token and capability-scoped authorization;
- helper/server Object hash, source, licence, exact version and deployment receipt;
- stream descriptors for video/audio/control/device messages;
- codec, dimensions, display ID, crop, rotation/fold generation, timestamps and sequence metadata;
- readiness levels: ADB selected, helper pushed, server started, sockets established, metadata validated, first frame/audio packet, control probe, application visible;
- no-retry policy for non-idempotent control messages;
- post-action screen/semantic verification;
- clipboard secrecy/consent policy;
- recording/screenshot Artifact registration and retention;
- virtual display/application relationships and close/migration semantics;
- USB/TCP/OTG/AOA/UHID transport distinctions;
- reconnect and stale-stream rejection;
- multi-device/multi-session resource/port allocation;
- backend conformance against minicap/minitouch/Appium/platform APIs.

## Exit strategy

Display, Audio, Raw Input and Application Session contracts remain backend-neutral. scrcpy, minicap/minitouch, Android MediaProjection, Accessibility/UIAutomator, Appium, emulator APIs or OEM device farms can replace individual capability groups independently.

## Validation required

1. Start read-only video on an explicitly leased device and prove no input/clipboard/file/install capability is reachable.
2. Validate exact server/client Object versions and reject a mismatched server before session readiness.
3. Establish separate video, audio and control streams and prove one may fail without falsely completing the others.
4. Rotate/fold/resize a display and reject stale coordinates and old display generations.
5. Disconnect/reconnect ADB and reject packets/control results from the previous connection epoch.
6. Inject a tap/text/gesture once, prohibit blind retry and verify the result through a later screen or semantic observation.
7. Disable clipboard autosync by default in a sensitive workspace and audit every explicit clipboard transfer.
8. Push/install an Artifact and independently verify file/package hash/version/signature/state.
9. Create a virtual display, start an app, prove visible readiness, then verify exact destroy-or-preserve behavior on close.
10. Record video/audio into a hashed Artifact with exact codec/session/device metadata and retention policy.
11. Run several devices/sessions concurrently without port, `scid`, stream or input cross-talk.
12. Replace scrcpy video or input with another backend while preserving Ptah Session semantics.
