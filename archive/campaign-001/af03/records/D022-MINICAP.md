# D022 — minicap

Status: candidate record — paired evidence complete

Primary Archivist: `AF03-P08`

Independent Verifier: `AF03-V08`

Inspected: 2026-07-23

## Canonical source identity

- source: `DeviceFarmer/minicap`;
- historical lineage: OpenSTF project transferred to DeviceFarmer;
- default branch: `master`;
- exact inspected commit: `f3d40d65da0cc7168846c4ae7466ada970441d4e`;
- root licence: Apache License 2.0;
- archived: false.

## Primary evidence packet

minicap is a component that streams Android screen-capture frames over a socket. It uses an ADB deployment path, an architecture-specific binary, SDK/architecture-specific shared libraries, virtual display or private AOSP screenshot APIs, libjpeg-turbo encoding and a simple push-based frame protocol.

Useful Ptah donor concepts include:

- separating screen-capture transport from higher-level remote-control workflows;
- explicit ABI, SDK, orientation, projection and process metadata;
- stream headers, frame lengths, quirks and socket lifecycle evidence;
- preflight compatibility checks before starting capture;
- preserving latency, frame-rate, single-connection and device-specific limitations.

## Independent verification packet

The verifier confirmed:

- the repository is Apache-2.0, but includes precompiled SDK/architecture libraries and a libjpeg-turbo submodule that require separate provenance and licence review;
- the README states non-root support through ADB only for SDK 28 and lower;
- minicap relies on private Android APIs and may fail or segfault on specific devices;
- emulators are not supported and Android 3.x is excluded;
- changes to shared-library code require rebuilding against corresponding AOSP branches;
- only one connection is supported at a time, and frame latency or tearing/quirks may occur;
- screen capture is not input control and does not establish device ownership or authorization.

## Contradiction and supersession

The donor pool classified minicap as an Android and physical-device donor. Current evidence supports legacy/read-only screen-capture protocol study, but not a current universal Android capture backend. Its compatibility and private-API assumptions are substantially narrower than modern Ptah Device Session requirements.

No frozen Ptah Device identity, transport, Session, Lease, Fence or authorization decision is superseded. A future adapter would require exact supported-device profiles, lawful authorization, current Android testing and a fallback Provider.

## Bounded outcome

`accepted_for_archive_legacy_android_screen_capture_with_private_api_and_compatibility_restrictions`

Allowed reuse:

- study or adapt the Apache-2.0 socket/frame protocol and capture-component separation;
- retain exact device, SDK, ABI, binary, shared-library, orientation, projection, stream and failure evidence;
- use only in explicitly tested, authorized legacy-device profiles.

Restrictions:

- preserve Apache-2.0 notices and independently review submodules and precompiled binaries;
- do not claim modern Android, emulator or universal-device compatibility;
- do not treat preflight `OK`, stream connection or received frames as device authority or complete session success;
- require explicit device/customer authorization, ADB authority, Lease/Fence and cleanup verification;
- do not make minicap the required or sole Ptah screen-capture Provider;
- do not expose captured private screen content outside configured privacy and retention policy.

This outcome does not authorize implementation.