# D023 — minitouch

Status: candidate record — paired evidence complete

Primary Archivist: `AF04-P10`

Independent Verifier: `AF04-V10`

Inspected: 2026-07-23

## Canonical source identity

- source: `DeviceFarmer/minitouch`;
- default branch: `master`;
- exact inspected commit: `1773320a0992203a37245faf9beaa058992aedc7`;
- root licence: Apache-2.0;
- repository role: Android multitouch socket/input adapter;
- archived: false.

## Primary evidence packet

minitouch exposes a line-oriented socket/stdin protocol for touch-down, movement, release, commit and reset operations. It demonstrates ABI-specific deployment, ADB forwarding, coordinate/pressure capability headers and low-level gesture transport.

## Independent verification packet

The verifier confirmed major limitations: Android 10+ needs STFService forwarding; the build guidance is old NDK-era material; only one connection is supported; the protocol generally returns no action responses; invalid streams can freeze input and require reboot; display and touch coordinates may differ. Input acknowledgement therefore cannot prove UI post-conditions.

## Contradiction and supersession

The donor remains useful for legacy touch transport only. It cannot serve as Ptah's semantic UI model or a broadly compatible modern Android input Provider without exact device/SDK evidence.

## Bounded outcome

`accepted_for_archive_legacy_android_touch_transport_with_sdk_single_connection_and_postcondition_restrictions`

Allowed reuse:

- study or adapt the Apache-2.0 touch protocol and capability-header patterns;
- use only under exact device ABI, SDK, service, coordinate and connection evidence;
- place any adapter behind Ptah Device Lease, Fence, Attempt and post-condition read-back.

Restrictions:

- preserve Apache notices and separately review bundled submodules, STFService and build dependencies;
- do not claim modern Android compatibility without device-specific proof;
- do not treat socket writes or command commits as proof that the intended UI action occurred;
- isolate malformed streams and retain reset/reboot/failure evidence;
- do not make minitouch Ptah's semantic Android authority or mandatory input backend.

This outcome does not authorize implementation.