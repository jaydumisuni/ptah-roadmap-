# ADR-0009 — Device Session, Display, Input and Semantic UI Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Phase:** 0A / WP07 Android device-runtime closure

## Context

Ptah must support physical Android devices, emulators and future application runtimes without collapsing several different guarantees into one vague “remote device” capability.

The inspected internal and external sources solve complementary parts:

- THETECHGUY Device Manager supplies authorized operator workflows, DPC/Device Admin state, ADB/package/policy requirements and honest manual-completion routes.
- MIBU supplies exact-device selection, nonce correlation, connection-aware stale-proof rejection and read-back evidence.
- DeviceFarmer STF supplies multi-device inventory, provider/per-device workers, booking/lease patterns and distributed device-host topology.
- adbkit supplies a programmatic ADB-server client and device tracker.
- official Android Platform Tools define ADB Client/Server/adbd and Fastboot transport boundaries.
- minicap and minitouch supply legacy display/input protocols with important compatibility and safety lessons.
- scrcpy supplies a modern composite Android session backend with separate video, audio and control streams.
- AndroidX UI Automator supplies official accessibility-tree selectors, element actions, waits and stale-object behavior.
- Appium supplies W3C WebDriver protocol compatibility and driver/plugin hosting.
- Appium UIAutomator2 supplies an Android semantic application-automation backend.
- TouchPilot supplies a local-first AccessibilityService provider, normalized context, typed tools, risk/approval vocabulary, retries and before/after verification.

No one donor defines Ptah Device identity, lease, Activity, Application Session, privacy or proof truth.

## Decision

Ptah will own a backend-neutral **Device and Application Session model** with separate contracts for:

1. Device identity;
2. Device interfaces/transports;
3. provider attachment and worker generation;
4. exclusive or shared lease ownership;
5. Device Session;
6. Application Session;
7. package/file/process/log Facilities;
8. display/video/audio streams;
9. input/clipboard Facilities;
10. semantic Screen Context and UI actions;
11. policy/administration Facilities;
12. operation receipts and produced Artifacts.

No USB path, ADB serial, Appium session, scrcpy process, accessibility node or application window is the canonical Device identity.

---

# Device identity

A physical or virtual Device has a stable Ptah identity:

```text
device_id
device_kind
manufacturer
brand
model
product
hardware_ids
serial_claims
attested_identity_references
first_seen_at
last_seen_at
profile_id
privacy_class
```

Possible `device_kind` values include:

```text
physical_android
android_emulator
physical_ios
ios_simulator
linux_host
windows_host
macos_host
virtual_machine
remote_application_provider
```

Observed properties are evidence claims with source and time, not immutable truth.

## Interface and transport identity

Each way of reaching a Device is a separate interface record:

```text
interface_id
device_id
provider_node_id
transport_type
transport_address
observed_serial
usb_topology
network_endpoint
mode
connection_epoch
state
first_seen_at
last_seen_at
backend_reference
```

Transport modes include:

```text
adb_usb
adb_tcp
adb_tls
fastboot_usb
fastboot_tcp
mtp
usb_serial
appium_proxy
accessibility_service
scrcpy_server
provider_native
```

The `connection_epoch` advances whenever the interface is recreated, re-enumerated, re-paired or otherwise loses continuity. Receipts from an older epoch cannot complete a newer operation.

## Correlation across modes

ADB, Fastboot, MTP and OEM modes for one physical Device are correlated through multiple claims, including immutable hardware evidence where available, previous transition receipt, USB topology, product/serial claims and explicit operator confirmation.

Filename, ADB serial or VID/PID alone is insufficient.

---

# Provider and worker boundary

A Device Provider is a Node-attached Facility that observes and controls Devices.

It owns:

- local transport processes and drivers;
- interface discovery;
- per-device workers;
- stream endpoints;
- backend helper deployment;
- local cleanup and health.

Ptah owns:

- Device identity;
- lease identity and fencing;
- Activity and operation identity;
- Session and Application Session records;
- permissions and caller restrictions;
- receipts and Artifacts;
- reconciliation across provider restart.

## Worker generation

Every provider worker has a generation/instance identity. Restarting the worker does not authorize automatic replay of earlier side effects.

## Registration acknowledgement

Provider introduction, Device observation, worker readiness and lease availability are separate states. A lost registration acknowledgement may be recovered for liveness, but cannot be promoted to authoritative ownership proof without reconciliation.

---

# Device lease

Physical Devices are scarce and stateful. Control operations require a lease unless an explicitly read-shared capability is allowed.

A lease contains:

```text
lease_id
device_id
workspace_id
holder_reference
mode
capability_scope
issued_at
expires_at
fencing_token
cleanup_recipe_reference
state
```

Lease modes may include:

```text
observe_shared
control_exclusive
maintenance_exclusive
policy_admin_exclusive
```

Every mutating or input operation presents the current fencing token. Stale sessions cannot send input, shell, package, policy or firmware operations.

Lease expiry or provider loss changes the Session to recovering/expired; it does not silently transfer control to another caller.

---

# Device Session

A Device Session binds a Workspace and lease to one Device over one or more current interfaces.

```text
device_session_id
device_id
workspace_id
lease_id
provider_id
worker_generation
interface_ids
started_at
updated_at
state
capability_snapshot_id
privacy_profile
application_session_ids
stream_ids
checkpoint_references
```

Session states include:

```text
preparing
connected
partially_available
recovering
disconnected
expired
closing
closed
failed
```

A Session can remain partially available when display works but semantic UI fails, or when ADB remains available while a scrcpy server restarts.

---

# Capability separation

Ptah advertises and authorizes Device capabilities independently.

## Inventory and transport

- observe connection state;
- query properties;
- pair/authorize;
- ADB server/transport management;
- Fastboot variables;
- MTP/USB/serial discovery.

## Package and application lifecycle

- list packages;
- inspect package/version/signature;
- install/update/uninstall;
- clear data;
- start/stop/activate application;
- read current activity/window/context.

## File and process

- push/pull/sync-like transfer;
- shell/process execution;
- port forwarding/reverse forwarding;
- log streams;
- bug reports;
- file inventory.

## Display and media

- screenshot;
- encoded video stream;
- audio stream;
- recording;
- orientation/display metadata;
- virtual display.

## Input and clipboard

- raw coordinate touch;
- key/text input;
- mouse/keyboard modes;
- clipboard read/write;
- file drop.

## Semantic UI

- hierarchy/context capture;
- element/window selectors;
- semantic click/type/scroll/drag;
- wait/stability conditions;
- app/system UI observation;
- before/after verification.

## Policy and administration

- Device Admin/Owner observation;
- approved DPC/policy operations;
- package hide/disable rules;
- kiosk/update/admin controls;
- reset/cleanup recipes.

Firmware operations remain governed by ADR-0008 and are not implied by a Device Session.

---

# Display, audio and control streams

Control/Event messages do not carry continuous screen/audio bytes.

A stream record contains:

```text
stream_id
device_session_id
stream_type
producer_backend
producer_version
interface_id
connection_epoch
codec_or_format
geometry
orientation
display_id
started_at
state
privacy_class
recording_artifact_id
```

Stream types include:

```text
video
audio
control
clipboard
log
shell
file_transfer
semantic_context
```

## scrcpy direction

scrcpy is the primary modern Android display/audio/control backend candidate. Its video, audio and control sockets are independently represented and permissioned.

The device-side server version must match the host adapter version. Deployment, socket setup, restart and cleanup are explicit receipts.

## legacy compatibility

minicap and minitouch remain compatibility backends only.

- minicap's private-API/version-specific binaries require an exact compatibility matrix;
- minitouch raw event streams are isolated, validated and never exposed directly to untrusted callers;
- newer Android paths relying on STFService or other helpers are declared separately.

---

# Input boundary

Input is a side effect and is separate from display observation.

Every input operation identifies:

```text
operation_id
attempt_id
device_session_id
lease_fencing_token
input_backend
input_type
target_display
coordinates_or_semantic_target
requested_at
before_context_id
after_context_id
verification_state
```

## Coordinate/raw input

Coordinate input must reference the exact display geometry, orientation and frame/context on which the coordinates were derived. Stale geometry rejects the action.

## Semantic input

Semantic actions identify selector intent and the resolved element/context. If the element becomes stale, the backend re-resolves under the same operation or returns an explicit stale-target result.

Input acknowledgement is not proof of intended UI outcome.

---

# Semantic Screen Context

Ptah defines a normalized backend-neutral Screen Context:

```text
screen_context_id
device_session_id
application_session_id
connection_epoch
captured_at
package
activity_or_context
window_and_display_metadata
semantic_nodes
visible_text
interactive_targets
screenshot_object_id
backend_source
backend_version
coverage
redaction_profile
limitations
```

The context may be produced by AndroidX UI Automator, Appium UIAutomator2, TouchPilot or another accessibility/semantic backend.

## Selector intent

Caller-facing selectors remain neutral:

```text
resource_id
package
text_or_pattern
description_or_pattern
class
state
ancestor_descendant_relations
window_display_constraints
relative_geometry
```

Adapters compile these into backend-specific selectors.

## Semantic truth limitations

Accessibility hierarchy is a partial observation, not complete visual truth. Games, video, custom rendering, WebViews, secure surfaces and OEM UIs may require visual/raw fallback.

## Stability and stale state

A semantic context or element carries a capture ID and epoch. Cached elements are never assumed valid after meaningful UI change. Stability waits use hierarchy and optionally visual evidence; fixed sleeps alone are insufficient proof.

---

# Application Session

An Application Session represents one running application/context on a Device or application provider.

```text
application_session_id
device_session_id
application_object_id
package_or_bundle_id
installed_version
signature_or_identity
runtime_backend
process_ids
window_contexts
started_at
state
stream_ids
semantic_context_ids
checkpoint_references
```

States include:

```text
installing
installed
launching
visible
backgrounded
suspended
stopped
crashed
recovering
closed
```

Install command success, process launch, activity start, first visible frame, semantic readiness and expected application state are separate proof levels.

---

# Semantic backend composition

## AndroidX UI Automator

- official native hierarchy, selectors, gestures, waits and stale-object model;
- direct Android semantic Facility foundation.

## Appium core

- W3C WebDriver-compatible external protocol host;
- does not own Device inventory, leases or physical provider state.

## Appium UIAutomator2

- primary Android WebDriver semantic backend candidate;
- device-side instrumentation server plus ADB forwarding and application lifecycle;
- Appium session ID remains backend metadata.

## TouchPilot

- local-first long-lived AccessibilityService backend;
- normalized/redacted context, typed tools, action verification, risk/approval vocabulary and local audit;
- agent/reasoning identity is not inherited by Ptah.

## Visual/raw fallback

scrcpy screenshot/video plus raw input remains available when semantic coverage is insufficient. Fallback is explicit in receipts.

---

# Safety, privacy and cleanup

## Sensitive data classes

Device screens, hierarchy text, clipboard, logs, accounts, package lists, files and notifications may contain sensitive data.

Each stream/context/Artifact has a privacy class and caller/workspace retention policy.

## Redaction

Backend and Ptah adapters redact configured fields before telemetry, export or shared review. Raw evidence may be retained only in an explicitly protected Object class.

## Device cleanup

A physical-device lease defines a cleanup/reset recipe appropriate to the Device and use case. STF's incomplete-reset warning is retained: ending a session without verified cleanup may leave accounts and data.

Cleanup itself is an Activity with receipts. Failure places the Device in `quarantined`, not automatically `available`.

## Authorization

Remote ADB, shell, files, clipboard, screen, input, package, DPC/policy and firmware are separately scoped capabilities.

---

# Proof levels

Device/Application operation evidence distinguishes:

```text
requested
lease_validated
transport_observed
transport_authorized
backend_server_deployed
backend_ready
command_accepted
stream_started
application_installed
application_launched
first_frame_observed
semantic_context_ready
input_acknowledged
state_change_observed
read_back_verified
cleanup_verified
authoritative_external_result
```

No lower level implies a higher one.

A screenshot, semantic context, log segment, recording, package dump or read-back may become an Artifact linked to the receipt.

---

# Failure and reconnect semantics

Failure classes include:

```text
device_removed
transport_offline
unauthorized
provider_lost
worker_restarted
lease_expired
stale_fencing_token
backend_version_mismatch
stream_lost
semantic_backend_failed
stale_element
application_crashed
cleanup_failed
```

On reconnect:

1. stable Device identity is reconciled;
2. a new interface connection epoch is created;
3. provider worker generation is recorded;
4. lease/fencing state is revalidated;
5. old stream and semantic receipts are rejected;
6. read-only state is rediscovered;
7. side effects are never replayed blindly;
8. Application Session is resumed only when backend/runtime evidence supports it.

---

# Donor decisions

- **THETECHGUY Device Manager:** adapt operator requirements, DPC/package/policy boundaries and honest manual-completion patterns; not the runtime core.
- **MIBU:** adapt exact-device, nonce, stale-proof and read-back patterns.
- **STF:** adapt provider/per-device-worker, inventory, lease and distributed-host patterns; do not adopt the full legacy stack.
- **adbkit:** optional programmatic ADB client adapter.
- **official Android Platform Tools:** authoritative ADB/Fastboot protocol foundation.
- **minicap/minitouch:** legacy compatibility backends only.
- **scrcpy:** primary modern Android display/audio/control backend candidate.
- **AndroidX UI Automator:** official native semantic UI foundation.
- **Appium:** external W3C protocol compatibility and driver host.
- **Appium UIAutomator2:** primary Android WebDriver semantic backend candidate.
- **TouchPilot:** device-side AccessibilityService/context/action/safety donor and optional backend.

All remain behind Ptah-owned identities and conformance tests.

---

# Consequences

## Positive

- One Device can expose several independently healthy/recovering capabilities.
- Multiple physical devices can run concurrently without stream or identity cross-talk.
- Backends can restart or change without changing Device/Application Session identity.
- Semantic UI and pixels/raw input complement rather than impersonate one another.
- Stale UI and stale transport results are rejected by context and epoch.
- Direct human control and automated control can use the same neutral Session.
- Sensitive device data receives explicit privacy and retention treatment.

## Costs

- Device, interface, lease, Session, stream, context and Application Session schemas are required.
- OEM/version compatibility testing is substantial.
- Several helper processes and device-side servers need versioned deployment and cleanup.
- Physical-device cleanup/quarantine adds operational overhead.
- Visual and semantic evidence may disagree and require explicit handling.
- Cross-platform application providers still need separate completion donors.

## Do-not-break rule

> Never treat Device presence, ADB authorization, backend deployment, command acceptance, stream start, application launch, semantic action acknowledgement or screenshot presence as universal completion. Device identity, lease, interface epoch, stream, semantic context, Application Session and verified outcome are separate guarantees.

---

# Required proof before freeze

1. Attach several Android devices and preserve unique stable identities across USB/TCP/ADB/Fastboot transitions.
2. Enforce lease fencing so stale sessions cannot send input, shell, package or policy actions.
3. Run independent shell, file, log, video, audio, control and semantic streams without cross-talk.
4. Restart scrcpy/Appium/TouchPilot/ADB helpers and reconcile new worker/interface generations without changing Device identity.
5. Reject a screenshot, semantic result or input acknowledgement from an older connection epoch/context.
6. Install and launch an app, then separately prove installed version/signature, first visible frame and semantic readiness.
7. Perform the same semantic action through AndroidX, Appium and TouchPilot adapters and compare receipts.
8. Fall back from semantic to visual/raw control while preserving Activity identity and recording reduced proof strength.
9. Disconnect during a non-idempotent operation and prove no blind replay occurs.
10. End a lease, run cleanup and quarantine the Device if cleanup verification fails.
11. Redact sensitive screen/hierarchy/log/clipboard evidence according to policy.
12. Replace one provider/backend without changing public Device, Session or Application Session identity.
