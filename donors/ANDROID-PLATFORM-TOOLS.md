# Donor Record — Android Platform Tools: ADB and Fastboot

**Phase:** 0A / WP07  
**Status:** FIRST-PASS COMPLETE — OFFICIAL TRANSPORT AND BOOTLOADER PROTOCOL FOUNDATION  
**Inspected:** 2026-07-17

## Identity

### Android Debug Bridge

- Canonical source: https://android.googlesource.com/platform/packages/modules/adb/
- Branch inspected: `main`
- Pinned commit: `1cf2f017d312f73b3dc53bda85ef2610e35a80e9`
- Licence: Apache-2.0
- Owner: Android Open Source Project / Google

### Fastboot

- Canonical source: https://android.googlesource.com/platform/system/core/+/master/fastboot/
- Exact source snapshot inspected: `6866041ff03e6ddd07145be37f6806c51fc18173`
- Licence: AOSP source files carry Apache-2.0 or file-specific permissive notices; dependency and file-level licence review remains required when embedding source.
- Owner: Android Open Source Project / Google

- Classification: Official Android device-transport and bootloader-protocol foundation
- Ptah targets: device discovery, transport identity, shell, file transfer, port forwarding, package installation, logs, wireless pairing and bootloader communication

## Sources/components inspected

### ADB

- repository README and tree
- `docs/dev/internals.md`
- developer documentation for overview, services, protocol and sync
- client/server/adbd separation
- smart-socket and Transport model
- `asocket`, `apacket` and `amessage` stream multiplexing
- sync protocol used by push/pull
- pairing, TLS, Wi-Fi and protobuf source areas
- host and device integration-test paths

### Fastboot

- `fastboot/README.md`
- host-driven command/response protocol
- USB, TCP and UDP transports
- response classes such as `OKAY`, `FAIL`, `DATA`, `INFO` and newer text/status behavior
- client variables and logical-partition command families
- platform-specific USB host implementations
- transport, driver and test source paths

## Verified capabilities and patterns

### ADB architecture

- ADB has three distinct components: host Client, host Server and device `adbd` Daemon.
- The host Server continuously manages device/emulator Transports over USB or TCP.
- Multiple logical byte streams are multiplexed over one Transport.
- Smart-socket services select a target Transport and service.
- Shell, file sync, forwarding, JDWP/debug, package and other services are different protocol/service families rather than one command channel.
- The sync protocol powers push and pull and is separate from command/shell streams.
- ADB has explicit host/device tests, platform abstractions and protocol documentation.
- Wireless ADB includes pairing/authentication/TLS machinery rather than being equivalent to an unauthenticated TCP socket.

### Fastboot architecture

- Fastboot communicates with bootloaders, not Android `adbd`.
- It is host-driven and synchronous, unlike ADB's multiplexed asynchronous stream model.
- USB and network transports share a simple command/response framing model.
- Device responses explicitly distinguish success, failure, data transfer and progress/information.
- Device variables can identify product, serial, protocol, bootloader, baseband and secure state.
- Logical partition operations exist on compatible implementations and must be capability-negotiated.

## What the official sources complete

- The authoritative protocol and lifecycle model beneath adbkit, STF, Appium, scrcpy and THETECHGUY ADB tooling.
- A clean distinction among Client, Server, Daemon and physical Transport.
- A clean distinction between ADB mode and bootloader/Fastboot mode.
- Independent service/stream identities for shell, sync, forwarding and debug traffic.
- Official authentication/pairing and wireless architecture references.
- Official host-driven Fastboot proof states and capability queries.
- Cross-platform host behavior for Linux, macOS and Windows.

## Important limitations for Ptah

- ADB/Fastboot are transport and service protocols, not Ptah's Device, Activity, Session, Object or Receipt model.
- `adb devices` presence does not prove authorization, stable connection, application readiness or correct target selection.
- ADB serial strings may be missing, duplicated, unstable or changed across connection modes.
- An ADB shell command returning zero does not prove the requested physical/application state without read-back evidence.
- File push completion does not prove final file identity unless size/hash/read-back are verified.
- Fastboot `OKAY` proves bootloader acknowledgement only; it does not by itself prove flashed bytes, bootability or device health.
- ADB and Fastboot identities for the same physical device require explicit correlation.
- OEM ADB/Fastboot implementations vary and may omit, alter or restrict services.
- Root, remount, flashing, erase, unlock and reboot operations have different destructive risk classes.
- Directly embedding AOSP source would create a large maintenance burden; invoking official binaries or using protocol-compatible libraries is usually preferable.
- Wireless endpoints and pairing material require scoped credential and network treatment.

## Must not be inherited

- ADB server or Fastboot process IDs used as canonical Ptah Device identity.
- Device presence interpreted as authorization or readiness.
- Arbitrary shell/Fastboot commands exposed as one unrestricted public tool.
- Command acknowledgement promoted to verified external result.
- Blind automatic retry of install, reboot, erase, flash, unlock or other physical mutations.
- ADB sync called equivalent to Ptah synchronization or backup.
- One OEM's serial/property behavior treated as universal.
- Raw wireless pairing material emitted into logs, receipts or public configuration.
- Fastboot logical-partition commands used without capability and exact-device checks.

## Integration decision

**ADOPT THE OFFICIAL PROTOCOL/BEHAVIOR AS THE FOUNDATION; WRAP OFFICIAL PLATFORM-TOOLS BINARIES OR COMPATIBLE CLIENT LIBRARIES BEHIND PTAH DEVICE FACILITIES.**

Recommended separation:

1. **ADB Transport Facility** — host server lifecycle, discovery, authorization, shell/sync/forward/log streams.
2. **Fastboot Transport Facility** — bootloader discovery, variables, download/flash/read-like operations where supported.
3. **Package/App Facility** — install, uninstall and app lifecycle through typed operations.
4. **Device Session** — stable Ptah identity that correlates connection modes and epochs.
5. **Operation Receipts** — exact command/service, target, attempt, acknowledgement and read-back proof.

adbkit, Appium, scrcpy and internal tools remain adapters/consumers over this official boundary.

## Native Ptah gap

Ptah must define:

- stable physical Device identity and ADB/Fastboot transport aliases;
- connection mode and connection epoch;
- authorization state, pairing credential references and revocation;
- exact-device selection and multi-device ambiguity handling;
- service/stream IDs for shell, sync, log, forwarding and package operations;
- command schemas and risk/retry classes;
- per-operation timeout, cancellation and process cleanup;
- file Object identities and transfer/read-back hashes;
- package/install verification and version/signature read-back;
- ADB-to-Fastboot transition receipts and correlation;
- OEM capability/profile records;
- event and telemetry normalization;
- backend version pinning and replacement path.

## Exit strategy

Ptah's Device contracts remain independent of the `adb` and `fastboot` executables. Official binaries, adbkit, libusb/native protocol clients or future platform APIs may implement the adapters without changing Device, Activity or Receipt identities.

## Validation required

1. Discover no-device, unauthorized, offline, recovery, sideload, bootloader and normal-online states distinctly.
2. Reject ambiguous multi-device operations unless an exact Device is selected.
3. Restart the ADB server and preserve Ptah Device identity while advancing the connection epoch.
4. Open simultaneous shell, sync, log and forwarding streams without conflating their lifecycle.
5. Push/pull a file and verify size plus cryptographic digest independently.
6. Install an APK and read back package, version and signature rather than trusting command output.
7. Transition one device from ADB to Fastboot and correlate the same physical Device with a new transport epoch.
8. Execute a Fastboot query and preserve `OKAY`, `FAIL`, `DATA` and progress responses separately.
9. Simulate transport loss during a destructive operation and prove no blind retry occurs.
10. Replace official CLI invocation with a compatible library adapter without changing public Ptah records.
