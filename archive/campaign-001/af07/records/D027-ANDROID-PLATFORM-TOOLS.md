# D027 — Android Platform Tools / ADB

Status: candidate record — paired evidence complete

Primary Archivist: `AF07-P04`

Independent Verifier: `AF07-V04`

Inspected: 2026-07-23

## Canonical source identity

- canonical source: `android.googlesource.com/platform/packages/modules/adb`;
- corroborating mirror: `aosp-mirror-neo/platform_packages_modules_adb`;
- branch: `main`;
- exact inspected commit: `1cf2f017d312f73b3dc53bda85ef2610e35a80e9`;
- source licence: Apache-2.0 notices across AOSP ADB source;
- repository role: ADB host, daemon, transport, authentication and forwarding implementation.

## Primary evidence packet

ADB provides device discovery, authorization state, shell, file transfer, package operations and port forwarding foundations.

## Independent verification packet

Serials, USB endpoints, transport IDs and server state are aliases and epochs, not canonical Device identity. Host/server/client versions can differ. Command transport success does not prove device-side post-conditions, and risky commands require separate caller authority.

## Contradiction and supersession

Official ADB source is a transport/provider foundation, not Ptah Device identity or permission authority.

## Bounded outcome

`accepted_for_archive_official_android_adb_transport_with_version_identity_authorization_and_postcondition_boundaries`

Allowed reuse: use pinned official tools/source behind Ptah Device Provider boundaries.

Restrictions: retain exact client/server/device/transport revisions; require Device Lease/Fence and read-back; never infer risky-operation authority from ADB availability; keep serial/transport IDs as aliases.

This outcome does not authorize implementation.