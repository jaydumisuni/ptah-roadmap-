# Donor Record — DeviceFarmer STF

**Phase:** 0A / WP07  
**Status:** FIRST-PASS COMPLETE — MULTI-DEVICE PROVIDER/INVENTORY/REMOTE-CONTROL DONOR, NOT PTAH CORE  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/DeviceFarmer/stf
- Default branch: `master`
- Pinned commit: `36d1a3e4336f2ecdf7885e3644fe34d0a4282c87`
- Pinned package version: `3.7.9`
- Licence: Apache-2.0
- Primary language/runtime: Node.js/JavaScript with native/device helper dependencies
- Activity: Active but hardware-heavy and comparatively slow-moving
- Classification: distributed Android device-farm, inventory, provider-worker, booking and browser-control donor
- Ptah targets: `DEVICE-001`, `DEVICE-002`, application/session extensions, multi-device inventory, device leases, reconnect, remote shell/files/logs/screen/input and per-device workers

## Files/components inspected

- `README.md`
- `package.json`
- `LICENSE`
- `doc/DEPLOYMENT.md`
- `lib/units/provider/index.js`
- commit `160c15cbf9cc8e4f481ceb344b0cf0d51813f6b0` fixing lost registration acknowledgements

## Verified capabilities and patterns

### Device inventory and state

- Tracks Android devices through adbkit and emits add/change/remove events.
- Represents connected, offline/unavailable, unauthorized and unplugged inventory states.
- Filters unusable `????????????` ADB entries and can distinguish remote ADB endpoints.
- Provider publishes device introduction, status and absence messages.
- Tracks ready, waiting and ignored device sets separately.
- Provides broad device attributes, search, battery/health and hardware information in the product layer.

### Provider and per-device worker model

- Separates provider hosts attached to physical devices from application, database and proxy roles.
- Provider hosts run ADB plus one provider unit that tracks devices.
- Allocates a fixed group of ports per device worker.
- Forks a dedicated process for each eligible device.
- Starts a worker only for usable `device` or `emulator` states and stops it for other states.
- Restarts a worker after abnormal non-zero exit, while deliberate signal/clean exits are handled separately.
- Returns allocated ports to the pool and removes ready/waiting state during cleanup.
- Handles device change and removal events without treating them as ordinary command errors.

### Registration and recovery

- Device introduction waits for a registration acknowledgement before normal work.
- A recent fix recognizes that a fire-and-forget ZeroMQ acknowledgement can be lost, especially when ADB re-adds a rebooted device and recreates the closure.
- The provider now times out the registration wait after 15 seconds and proceeds with a warning rather than leaving the device permanently stuck offline.
- This is valuable evidence that registration, worker readiness and actual device state must be independently recoverable.

### Remote-control facility breadth

- Browser-based real-time screen view and rotation.
- Keyboard, clipboard and multitouch through minicap/minitouch-related components.
- APK drag/drop install and launcher activity start.
- Shell commands with streaming output.
- Device logs, file explorer and remote ADB access.
- Website opening, browser discovery and Chrome remote debugging.
- Device ownership/usage display plus booking and partitioning/group models.
- REST API and independently deployable service units.

### Distributed topology

- Multiple independent units communicate using ZeroMQ and Protocol Buffers.
- Provider/app/database/proxy roles can be distributed across hosts.
- Application, authentication, processor, reaper, storage, websocket, API, group engine and triproxy units are separately deployable.
- The provider role must remain near attached physical devices.

## What STF completes

- A proven provider/per-device-worker architecture for many attached Android devices.
- Inventory add/change/remove flows and unusable-state handling.
- The concept of booking/partitioning/ownership around scarce physical devices.
- Remote display, touch, keyboard, shell, logs, files, APK install and remote ADB product requirements.
- Recovery examples for lost registration acknowledgement and reboot/re-add behavior.
- A concrete distributed deployment where physical-device hosts are distinct from application services.

## Important limitations for Ptah

- The project explicitly warns that there is little or no security/encryption between many internal processes.
- It originated as a trusted internal test-device system and does not fully reset devices between users, so accounts and sensitive data may remain.
- Example deployments include insecure/default ADB-key patterns and privileged containers with `/dev/bus/usb` access.
- RethinkDB, ZeroMQ, GraphicsMagick, Protobuf, native JPEG/minicap/minitouch and legacy frontend dependencies make the full stack heavy.
- Several architecture choices predate Ptah's accepted NATS/Activity Ledger/Object/Receipt boundaries.
- A 15-second lost-ack timeout restores liveness but is not proof that registration was accepted by an authoritative owner.
- ADB serial/device type remains central; Ptah needs stronger stable Device identity and connection epochs.
- Worker restart policy must not blindly replay non-idempotent physical actions.
- Remote ADB access is extremely powerful and needs scoped leases, authorization and audit.
- Booking/group models are product/domain policy, not automatically the Ptah universal lease model.
- Screen/log/file access can expose highly sensitive user/device data.
- README claims broad Android support, but exact OEM/version/helper compatibility still requires Phase 0C hardware proof.
- Windows production support is not a project priority.
- Product UI, database schema and deployment topology should not be adopted wholesale.

## Must not be inherited

- trusting an internal network or users by default;
- unencrypted unauthenticated internal device-control messages;
- default/insecure ADB keys;
- incomplete device reset between unrelated users/workspaces;
- privileged USB containers as the only provider design;
- ADB serial as sole stable Device identity;
- worker restart interpreted as permission to retry physical side effects;
- lost registration ack timeout promoted to authoritative registration proof;
- RethinkDB/ZeroMQ/product schema as Ptah truth;
- remote ADB, shell, file, screen and input bundled into one unrestricted permission;
- booking/group semantics embedded directly into Ptah Core;
- screen/log/file data exposed without workspace policy and redaction.

## Integration decision

**ADAPT THE PROVIDER/PER-DEVICE-WORKER, INVENTORY, LEASE AND REMOTE-CONTROL PATTERNS; DO NOT ADOPT THE WHOLE STF STACK.**

STF should be treated as a major architecture and compatibility donor. Selected Apache-2.0 components may be adapted after licence/source review, but Ptah should normally implement a neutral Device Provider over its existing Node Protocol, Activity Ledger, Event Fabric, Object streams and receipts.

## Native Ptah gap

Ptah must define:

- stable Device identity separate from ADB serial, USB path, network endpoint and provider-local ID;
- Device Interface/Transport identities and connection epochs;
- provider registration, authoritative acknowledgement, heartbeat, liveness and reconciliation;
- exact Device lease/ownership with fencing token and expiration;
- device state taxonomy: observed, available, unauthorized, offline, bootloader, recovery, sideload, emulator, reserved, busy and quarantined;
- per-device worker/session identities and restart generation;
- capability-specific permissions for screen, input, shell, file, package, logs, remote ADB and policy operations;
- idempotency/retry classes and receipts for each operation;
- large display/video/log/file streams outside the control Event Fabric;
- Device/Application Session checkpoints and reconnect compatibility;
- sensitive-data isolation, redaction and reset/cleanup recipes;
- provider-neutral database and API contracts;
- multi-provider deduplication when the same physical device appears through USB and TCP;
- hardware/helper compatibility matrix and versioned provider manifest.

## Exit strategy

The Device Provider contract remains independent of STF. A native Rust/Go provider, adbkit/platform-tools service, scrcpy/Appium provider, OEM lab system, cloud device farm or a wrapped STF deployment can all implement the same Ptah Device/Lease/Session/Operation contracts.

## Validation required

1. Attach multiple Android devices and prove add/change/remove inventory without identity collision.
2. Reboot a leased device and reconcile its new ADB/USB connection epoch without transferring the lease to a different device.
3. Drop a provider registration acknowledgement and recover liveness without falsely recording authoritative registration.
4. Kill a per-device worker during a read-only operation and resume safely; kill it during a non-idempotent operation and block automatic replay.
5. Connect the same device by USB and TCP and deduplicate it under one stable Device identity with separate interfaces.
6. Enforce lease fencing so a stale session cannot send shell/input/package operations.
7. Prove screen, input, shell, file, logs and remote ADB are separately permissioned.
8. Reset/clean a test device between unrelated workspaces and retain a verification receipt.
9. Run concurrent display/input/shell/file operations on several devices without stream cross-talk.
10. Replace the STF-derived provider with another backend without changing Device or Session identities.
