# Donor Record — DeviceFarmer adbkit

**Phase:** 0A / WP07  
**Status:** FIRST-PASS COMPLETE — PRIMARY PROGRAMMATIC ADB CLIENT DONOR, NOT AN ADB SERVER OR DEVICE-LEASE SYSTEM  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/DeviceFarmer/adbkit
- Default branch: `master`
- Pinned commit: `f474b57f6b1b1b41edd4abbfa1dd9bfad6420d6a`
- Pinned package version: `3.3.9`
- Licence: Apache-2.0
- Primary language: TypeScript/Node.js
- Activity: Active maintenance
- Classification: programmatic ADB-server client and Android transport library
- Ptah targets: `DEVICE-001`, portions of `DEVICE-002`, package/file/process/log/screenshot/port-forwarding facilities and device-state tracking

## Files/components inspected

- `README.md`
- `package.json`
- `LICENSE`
- `src/adb/client.ts`
- `src/adb/DeviceClient.ts`
- `src/adb/tracker.ts`

## Verified capabilities and patterns

### ADB server client boundary

- Implements a client for an existing ADB server rather than implementing the server itself.
- Supports local or remote ADB server host/port configuration.
- May start a local ADB server through the configured `adb` binary only when an initial local connection fails.
- Requires the caller/operator to own remote ADB-server lifecycle.
- Exposes client, connection, device and tracker abstractions rather than only shelling out for every operation.

### Device inventory and tracking

- Lists devices and devices with transport paths.
- Provides continuous device tracking.
- Tracker computes and emits add, change, remove and aggregate change-set events.
- Maintains current device list/map and explicitly ends/cancels the tracking stream.
- Per-device client is selected by serial and exposes observed state, device path and reported serial number.

### Device metadata and capability inventory

- Reads Android properties and feature declarations.
- Lists installed packages with filtering options.
- Supports state queries and boot-complete waiting.
- Exposes JDWP process tracking and lightweight `/proc/stat` monitoring.

### Process, application and package operations

- Opens streamed shell sessions.
- Starts activities and services.
- Installs APKs by pushing to a temporary device path and invoking package installation.
- Uninstalls packages and checks whether a package is installed.
- Clears package data.
- Supports reboot, root and remount commands where the target permits them.

### File and network transport

- Provides sync service, push, pull, stat and directory operations.
- Emits transfer progress/end/error events.
- Supports ADB forward and reverse mappings.
- Opens device-local sockets and direct TCP connections through ADB.
- Can bridge a device transport over TCP/USB patterns.

### Screen, logs and input-adjacent functions

- Captures screenshots through Android `screencap`, with framebuffer fallback.
- Exposes raw or converted framebuffer streams.
- Opens parsed logcat and raw log streams.
- Starts/connects to Android Monkey for key/touch event generation.
- Keeps these functions on the per-device client rather than conflating them with host inventory.

## What adbkit completes

- A reusable programmatic interface over the ADB server protocol.
- Continuous add/change/remove device tracking.
- Stream-oriented shell, log, file and screenshot operations.
- Per-device package/application/process APIs.
- Local and remote ADB-server connection patterns.
- A practical alternative to product-specific batch scripts for many normal Android operations.

## Important limitations for Ptah

- adbkit is not an ADB server and therefore does not own USB discovery, daemon keys, server lifecycle or server security.
- The configured serial is a transport selector, not a stable physical Device identity.
- The same physical device can appear simultaneously through USB and TCP; the README warns this can cause operational havoc.
- Tracker add/change/remove events do not carry Ptah connection epochs, leases, fencing tokens or authenticated provider identity.
- Host and device commands return library-level values/streams, not durable Activity receipts or authoritative physical proof.
- A successful install call does not by itself prove expected package version, signature, permissions or visible runtime state.
- Shell array escaping is documented as rudimentary convenience, not a security boundary.
- Root, remount, reboot, package clear and uninstall are mixed into the same broad client surface as read-only inventory.
- Framebuffer/screenshot/log/file operations can expose sensitive user data.
- Stream cancellation and process/provider restart need Ptah-level recovery and partial-Artifact handling.
- Remote ADB servers and TCP-connected devices require authenticated encrypted transport outside adbkit.
- Android/OEM compatibility varies by command and device policy.
- The Node.js/TypeScript implementation is replaceable machinery, not a requirement that Ptah Core use Node.

## Must not be inherited

- ADB serial used as universal Device identity;
- first-device or unscoped device selection;
- USB and TCP appearances treated as unrelated physical devices without reconciliation;
- one unrestricted client permission covering shell, file, package, logs, screen, root, remount and reboot;
- shell escaping treated as command-injection protection;
- install/process return value promoted to verified application state;
- automatic retry of reboot, clear, uninstall, root, remount or other non-idempotent operations;
- plaintext remote ADB/server assumptions;
- unbounded screen/log/file streams entering the control event channel;
- sensitive device contents written to ordinary logs or telemetry;
- backend connection or stream identity used as Ptah Session/Activity identity.

## Integration decision

**ADAPT OR WRAP AS A PRIMARY NORMAL-ADB CLIENT BACKEND BEHIND A NARROW DEVICE FACILITY.**

adbkit is suitable for a TypeScript provider or compatibility backend. Ptah must compile neutral capability calls into explicit adbkit operations and wrap every operation with lease checks, connection-epoch fencing, timeouts, resource limits, receipts and post-operation verification.

Recommended capability groups:

- ADB inventory and state;
- properties/features/packages;
- shell/process;
- package/application;
- file/sync;
- port forward/reverse/socket;
- logs/JDWP;
- screenshot/framebuffer;
- separately gated reboot/root/remount/clear/uninstall operations.

## Native Ptah gap

Ptah must define:

- stable Device and Device Interface identities;
- ADB Provider, ADB Server and ADB Transport identities;
- connection epoch and provider restart generation;
- USB/TCP deduplication and interface preference;
- exact device lease with fencing token;
- capability-scoped authorization;
- typed invocation/result/error contracts;
- operation ID, attempt, nonce and receipt correlation;
- stream references for shell/log/file/framebuffer data;
- package/application Objects and installed-state observations;
- read-back verification after install/uninstall/clear/start/reboot where applicable;
- cancellation, timeout, reconnect and late-result policy;
- command argument and shell-safety model;
- sensitive-data classification/redaction;
- backend version/capability manifest and conformance suite;
- alternate platform-tools/native backend compatibility.

## Exit strategy

The ADB Facility remains backend-neutral. Android platform-tools, a custom Rust/Go ADB protocol client, adbkit, STF, Appium or an OEM bridge can replace one another for specific capabilities without changing Device, Application, Activity, Stream or Receipt identities.

## Validation required

1. Track add/change/remove across multiple devices and preserve exact connection epochs.
2. Connect one physical device by USB and TCP and reconcile both interfaces under one Device identity.
3. Kill/restart the ADB server and reject stale streams/results from its previous generation.
4. Enforce an exclusive lease before shell, package, file, input or reboot operations.
5. Install an APK and independently verify package name, version, signature and launch/readiness state.
6. Cancel a large pull/push and preserve a bounded partial Artifact without reporting completion.
7. Drop a shell/log/framebuffer stream and reconnect without confusing it with the old stream identity.
8. Prove read-only inventory permissions cannot call root, remount, reboot, clear or uninstall.
9. Reject unsafe shell construction and preserve exact argv/command evidence without leaking secrets.
10. Replace adbkit with platform-tools commands for a conformance test without changing the Ptah contract.
