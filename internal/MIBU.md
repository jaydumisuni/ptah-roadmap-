# Internal Recovery Record — MIBU

**Phase:** 0A / WP02C  
**Status:** FIRST-PASS COMPLETE  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/MIBU`
- Visibility: Public
- Default branch: `main`
- Pinned commit: `b76e90bfab8789763e1dfb8c0b60c3e1a38de554`
- Current documented Android version: `0.2.0-dev`
- Licence: Requires separate root-licence verification before code extraction; this record focuses on internal architectural evidence.
- Ptah relevance: correlated physical-device proof, stale-result rejection, exact device states, versioned proof protocols, authoritative-result preservation and complete-release validation.

## Files inspected

- `README.md`
- `pc-helper/qt6/mibu_pc_helper_v3.py`
- `pc-helper/qt6/mibu_actions.py`
- `pc-helper/qt6/mibu_status.py`

## Verified implemented behavior

### Device and tool discovery

- Prefers bundled ADB/fastboot tools, then configured paths and system PATH.
- Parses only recognized ADB states: device, unauthorized, offline, recovery, sideload and bootloader.
- Requires exactly one normal online ADB device and reports multiple-device ambiguity explicitly.
- Distinguishes no device, unauthorized, offline and unsupported state.
- Verifies Android reports `adb_enabled=1`.
- Parses only real fastboot device rows and rejects multiple fastboot devices.

### Installation proof

- Checks whether the app is installed and reads `versionName`.
- Reinstalls/updates rather than accepting any installed package.
- Does not trust `adb install` output alone; verifies the installed app version against `0.2.0-dev`.
- Falls back to the Android/MIUI system installer when silent installation is blocked and describes the remaining human step honestly.

### Correlation and stale-result rejection

- Every import, waiting and status-proof request receives a cryptographically random nonce.
- The nonce is sent to the Android activity and expected in returned log proof.
- Log filtering ignores lines with a different nonce rather than clearing the entire device log.
- Status proof carries protocol version, app version, captures, verification, community state and lanes.
- Status lines with the wrong nonce, incompatible proof protocol or wrong app version are rejected.
- Success and failure markers are separated and checked against the correlated proof lines.

### Evidence hierarchy

- Launching an activity is not treated as proof that the foreground service is armed.
- Waiting succeeds only after a correlated service marker such as ARMED or COMPLETE.
- Early correlated rejection markers return explicit failure instead of ambiguous timeout.
- Fastboot handoff is blocked until phone status proves timing completion.
- Existing authoritative official results are preserved and stop a new waiting or fastboot cycle.
- An official result is not invented from timing, Settings toast or mere fastboot presence.

### Release proof

- Build flow runs Android lint/tests/build, source-contract review, UI baseline validation, geometry tests, unit tests and offscreen construction.
- Release bundles app, platform tools, expected UI evidence and checksum manifest.
- Build fails rather than publishing a partial release.
- Static/CI proof is explicitly separated from physical-device proof.

## Strong internal patterns for Ptah

1. Correlation nonce on every physical or asynchronous proof request.
2. Stale evidence from another operation is ignored, not accepted.
3. Protocol version and producer/application version are part of proof.
4. Launch evidence, service-state evidence and authoritative external result are different proof levels.
5. Exact device states and multiple-device ambiguity are represented honestly.
6. An operation can complete while the caller is checking state; later status truth outranks a stale waiting assumption.
7. Recorded authoritative results prevent accidental repeated actions.
8. External facts require physical proof; source/CI cannot claim them.
9. Complete release contents and checksums are contractual.
10. Sensitive values never return through status proof.

## Important limitations

- ADB/fastboot commands use synchronous subprocess calls and polling loops.
- Logcat proof is text-marker based and not cryptographically signed by the device app.
- Nonces correlate requests but do not authenticate the producer.
- Status is transported through filtered logcat rather than a typed authenticated IPC or Ptah Device stream.
- Fixed polling windows can fail on slow devices despite eventual completion.
- The workflow is product/device specific and cannot become universal Ptah policy.
- Tool discovery contains product-specific local Windows paths.
- Result objects contain only boolean/message rather than universal Activity, Object, Artifact and receipt references.
- The current operation loop is local and not durable across PC helper restart unless reconstructed from phone status.

## What Ptah should reuse or adapt

- Operation correlation nonce plus stable Activity/operation ID.
- Proof protocol version and producer version.
- Explicit proof-level taxonomy: command accepted, process/activity launched, runtime armed, operation complete, external authoritative result.
- Stale-event rejection using operation ID/nonce and connection epoch.
- Exact device-state classification and ambiguity handling.
- Verification after install/write rather than trusting command success.
- Preservation of authoritative result/checkpoint state.
- Static proof versus physical-runtime proof boundary.
- Complete Artifact bundle and checksum-manifest gates.
- Sensitive-payload exclusion from status/evidence.

## What Ptah must not inherit

- MIBU/Xiaomi workflow rules as generic Ptah Device policy.
- Text log markers as the universal proof transport.
- Polling loop as the durable Activity Runtime.
- Nonce alone treated as authentication.
- Fixed local paths and Windows-only assumptions.
- Boolean/result message as sufficient evidence.
- Automatic retry of physical/device operations.
- Timing completion interpreted as official external success.

## Classification

**ADAPT CORRELATION, PROOF-LEVEL, STALE-REJECTION AND RELEASE-COMPLETENESS PATTERNS.**

MIBU is strong internal evidence for `CORE-002`, `RELAY-001`, `RELAY-002`, `DEVICE-001`, `DEVICE-002`, `OBS-001` and `PROV-001`. Its product workflow remains a specialist application using Ptah, not Ptah Core.

## Native Ptah completion required

- typed signed Device receipt/envelope;
- operation ID, nonce, Node connection epoch and producer identity together;
- durable Activity state and local outbox;
- asynchronous event subscription instead of log polling where possible;
- verification-level field and authoritative-source classification;
- Device/Object/Artifact references and hashes;
- configurable timeouts and late-result reconciliation;
- transport authentication and replay protection;
- provider-neutral Device Facility contract.

## Validation inherited into Ptah

1. A stale receipt with the wrong operation ID/nonce/epoch is rejected.
2. A correct nonce from an unauthenticated producer is also rejected.
3. Launch success never implies runtime or operation success.
4. An operation completing during reconnect is reconciled from authoritative status.
5. Two connected devices produce an ambiguity error unless the caller selects one explicitly.
6. Install/write success is independently read back and verified.
7. Automatic retry is blocked for non-idempotent physical operations.
8. Partial release/Artifact bundles fail validation.
9. Static tests never claim facts requiring physical hardware.
10. Secrets and sensitive captured values do not enter telemetry or status receipts.
