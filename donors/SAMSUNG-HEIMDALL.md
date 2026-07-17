# Donor Record — Samsung Heimdall / Odin Protocol

**Phase:** 0A / WP06  
**Status:** FIRST-PASS COMPLETE — OPTIONAL SAMSUNG DOWNLOAD-MODE BACKEND, MODERN COVERAGE REQUIRES PROOF  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/Benjamin-Dobell/Heimdall
- Default branch: `master`
- Pinned commit: `3997d5cc607e6c603c6e7c0d07e42e9868c62af2`
- Licence: MIT
- Activity: Mature historical project; current modern Samsung coverage must be verified because the inspected source is primarily 2010–2017-era protocol work with later build-maintenance commits.
- Classification: Samsung Download Mode, Loke/Odin protocol, PIT and partition-file transfer donor
- Ptah targets: Samsung USB transport identity, protocol handshake, PIT partition mapping, package-to-partition plan and separately authorized flashing

## Files/components inspected

- `README.md`
- `heimdall/source/BridgeManager.cpp`
- search-located PIT/file-transfer packet classes
- platform/driver documentation paths

## Verified capabilities and patterns

- Cross-platform suite for flashing Samsung mobile devices over USB.
- Communicates with low-level device software called Loke through Samsung's Odin 3 protocol.
- Uses libusb and enumerates supported Samsung USB VID/PID pairs.
- Discovers a CDC-data-like interface with separate IN/OUT endpoints.
- Explicitly claims/releases the USB interface and reattaches a detached Linux kernel driver during cleanup.
- Protocol initialization sends `ODIN` and requires `LOKE` as the handshake response.
- Separates session setup, device type, PIT transfer, phone/modem file transfer, sequence/part transfer and end-session packet classes.
- Can retrieve PIT data and use PIT entries to map partition/file transfer plans.
- File transfer has defined packet size, sequence length and timeout behavior.
- Verbose mode can report USB descriptor/serial/interface details.
- Supported host platforms include Linux, macOS and Windows.

## What Heimdall completes

- An open implementation of the Odin/Loke transport instead of making proprietary Odin the only backend.
- Samsung Download Mode handshake and USB-interface evidence.
- PIT as an explicit partition-layout authority/view.
- Separation of PIT transfer and partition-file transfer.
- A useful comparison backend for Samsung packages and physical flashing workflows.
- MIT-licensed protocol code suitable for study/adaptation after modern compatibility tests.

## Important limitations for Ptah

- The project is historically important but cannot be assumed to support all recent Samsung protocol versions, secure download modes, compression formats or device generations.
- USB VID/PID and `LOKE` handshake prove protocol presence, not target model/build/package compatibility.
- PIT partition names/IDs are device layout evidence but do not prove that one firmware image belongs on that target.
- Samsung firmware packages commonly include TAR/TAR.MD5, LZ4-compressed components, CSC/HOME_CSC and bootloader/baseband/application groups that require separate package parsing.
- Modern packages may include signed/encrypted/proprietary components not covered by historical Heimdall behavior.
- Device serial/descriptor values are sensitive and should not enter public logs.
- Flash transfer success requires post-flash/device read-back or boot verification; protocol ACK alone is insufficient.
- Detaching host kernel drivers is an administrative side effect and requires Node-level capability/cleanup receipts.
- There is no universal immutable package/download catalogue, signature verification or exact device/build compatibility model in Heimdall.
- PIT retrieval and flash operations are physical-device activities, not static package analysis.
- The tool does not replace Android sparse/super/AVB or filesystem decomposition.
- Main/master commit is not necessarily a current release candidate; fork/maintenance alternatives may need review.

## Must not be inherited

- Samsung/Odin protocol treated as generic Android flashing.
- PIT name/ID alone used to authorize an image write.
- `LOKE` handshake described as successful device compatibility or flash readiness.
- historical supported-device table advertised as modern universal coverage.
- protocol ACK promoted to verified flashed bytes or successful boot.
- USB serials/identifiers emitted publicly.
- driver detach/admin changes performed silently.
- static package analysis and physical download-mode flashing exposed as one capability.
- proprietary Odin packages/binaries redistributed without rights/provenance review.

## Integration decision

**SUPPORT AS AN OPTIONAL SAMSUNG DOWNLOAD-MODE BACKEND AFTER MODERN CONFORMANCE TESTS.**

Ptah should own:

- Samsung package/PIT/component/device compatibility records;
- static TAR/TAR.MD5/LZ4/AVB image decomposition;
- exact device selection and Download Mode session receipts;
- reviewed partition plan;
- backup/read-before-write where supported;
- post-write/read-back/boot proof.

Heimdall may implement transport and selected PIT/file-transfer operations. Proprietary Odin may be an external comparison/escape path, never the public canonical dependency.

## Native Ptah gap

- Samsung product/model/board/build/binary-revision schema;
- firmware package groups and component Object relationships;
- TAR.MD5/LZ4 extraction, checksums and signatures;
- PIT entry schema with partition IDs/types/attributes/block ranges;
- package-component→PIT target mapping and incompatibility reasons;
- Download Mode protocol/version/capability record;
- USB connection epoch and driver-state receipt;
- read/write/erase/repartition operation classes and authorization;
- post-flash read-back/boot/AVB verification;
- modern-device conformance corpus and stable backend selection.

## Exit strategy

Ptah's Samsung contracts remain backend-neutral. Heimdall, a maintained fork, vendor Odin used externally or a future native protocol implementation can replace one another without changing Package, PIT, Partition, Device or Receipt identities.

## Validation required

1. Parse representative Samsung TAR/TAR.MD5/LZ4 packages into immutable component Objects before connecting a device.
2. Retrieve PIT from representative old and modern devices and retain exact protocol/device evidence.
3. Compare package components with PIT and device build/binary-revision compatibility before transfer.
4. Prove USB detection, `LOKE` handshake, PIT transfer, file transfer and reboot/boot verification as separate levels.
5. Reject modern/unsupported protocol capability honestly rather than forcing a flash.
6. Preserve and restore host driver state after interface claim/failure.
7. Perform one authorized write only after plan review and verify the result independently.
8. Prove read-only/static-analysis users cannot invoke download-mode writes.
9. Compare Heimdall behavior with a known-good vendor path without making proprietary tooling mandatory.
