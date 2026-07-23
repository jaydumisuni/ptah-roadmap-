# D026 — scrcpy

Status: candidate record — paired evidence complete

Primary Archivist: `AF06-P10`

Independent Verifier: `AF06-V10`

Inspected: 2026-07-23

## Canonical source identity

- source: `Genymobile/scrcpy`;
- default branch: `master`;
- exact inspected commit: `2926c06c5dc3064ae6d8db706f1a98a37cfcf3f0`;
- root licence: Apache-2.0;
- repository role: low-latency Android display, input, recording and transfer tool;
- archived: false.

## Primary evidence packet

scrcpy demonstrates efficient USB/wireless display streaming, remote input, recording, clipboard and file-transfer patterns without installing a permanent application.

## Independent verification packet

ADB transport, server binary, codecs, device/Android version, input mode and network state are separate capability surfaces. Display frames can be stale or dropped, and input acknowledgement does not prove the intended semantic UI state. Wireless operation changes trust and exposure.

## Contradiction and supersession

scrcpy is a Device display/input Provider donor, not Ptah's Device identity or semantic UI authority.

## Bounded outcome

`accepted_for_archive_apache_android_display_input_provider_with_transport_codec_generation_and_postcondition_limits`

Allowed reuse:

- run or adapt pinned scrcpy components behind Ptah Device Session and Artifact boundaries;
- retain exact device epoch, ADB transport, server/client, codec, command and recording evidence.

Restrictions:

- preserve Apache notices and inspect bundled binaries/libraries separately;
- require Lease/Fence, stale-generation checks and semantic post-condition read-back;
- do not expose serial/socket/session IDs as canonical Device identity;
- do not assume wireless, clipboard, file-transfer or control capability without exact proof.

This outcome does not authorize implementation.