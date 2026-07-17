# ADR-0001 — Node Protocol and Workspace Provider Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Phase:** 0A requirement closure

## Context

Ptah needs to connect physical and virtual machines while also creating and managing working environments on those machines.

OpenClaw demonstrates a capable node/gateway protocol. Daytona demonstrates a capable sandbox/workspace lifecycle. They solve different layers and must not be blended into one universal object.

## Decision

Ptah will own two separate contracts:

1. **Ptah Node Protocol** — connects capability hosts to the Ptah control plane.
2. **Ptah Workspace Provider Contract** — creates and manages work environments through facilities available on a node.

A node is not a workspace. A workspace provider is one capability exposed by a node.

---

# Ptah Node Protocol

## Responsibility

The Node Protocol handles:

- connection and version negotiation;
- stable node identity and connection identity;
- platform, architecture, version and instance metadata;
- CPU, memory, storage, GPU and attached-device reporting;
- facility, command and runtime capability publication;
- capability refresh after connection;
- health, heartbeat, presence, last-seen and disconnect reason;
- request, response and event transport;
- idempotent invocation;
- cancellation and status queries;
- reconnect, connection epoch and event replay cursor;
- control-plane routing to the correct physical capability host.

## Initial control envelope

The first transport may use WebSocket with a versioned JSON control envelope:

```text
challenge
connect
hello-ok
request
response
event
```

Every side-effecting request requires an operation ID or idempotency key. Events carry a monotonically ordered sequence within their stream and may carry state versions.

## Streaming boundary

Large or continuous data must not be embedded into ordinary JSON control frames.

Separate streams are required for:

- PTY data;
- command logs;
- object and file transfer;
- screen and application streams;
- media;
- large artifacts.

The control envelope carries stream identity, state and metadata.

## Capability rule

Capabilities reported by a node are physical/runtime facts. They are not business policy decisions.

Examples:

```text
container.oci
workspace.local-process
browser.chromium
media.ffmpeg
device.android-adb
gpu.cuda
firmware.mtk
```

The caller or higher system decides what to request. Ptah routes the instruction to available machinery.

---

# Workspace Provider Contract

## Responsibility

A Workspace Provider manages one class of working environment on a node.

Initial provider families:

- local Linux process;
- OCI/container;
- remote Linux host;
- Dev Container.

Later providers:

- Linux VM or microVM;
- Windows node or VM;
- macOS node;
- Android emulator or physical device;
- GPU environment;
- specialist hardware node.

## Required provider operations

```text
create
start
stop
pause
resume
archive
restore
snapshot
fork
resize
destroy
status
attach_storage
detach_storage
expose_port
open_terminal
execute_process
file_operations
report_capabilities
```

Providers explicitly report unsupported operations. Ptah must never imply that pause, fork, memory snapshot or migration is universal.

## Lifecycle state family

The neutral lifecycle must be able to represent:

```text
requested
provisioning
starting
running
stopping
stopped
pausing
paused
resuming
archiving
archived
restoring
snapshotting
forking
resizing
deleting
deleted
error
unknown
```

Provider-specific states may exist, but they map to the neutral state family.

## Activity relationship

Every provider operation runs as a Ptah activity with:

- activity ID;
- workspace ID;
- node ID;
- provider ID;
- idempotency key;
- state and progress;
- events and logs;
- produced objects and artifacts;
- failure and retry information.

A workspace persists independently of individual activities.

---

# Separation from other Ptah foundations

## Activity Runtime

Schedules and tracks operations. It does not own the physical environment.

## Object and Storage System

Owns object identity, hashes, relationships and durable locations. Provider filesystems are execution surfaces, not the universal source of object truth.

## Session Vault

References workspace state, provider snapshots, object graphs, activities, terminals, browsers and artifacts. It does not require every provider to serialize live processes identically.

## Relay/Event Fabric

Moves live status and commands. Durable workflow history is a separate concern to be evaluated against Temporal and related donors.

---

# Donor decisions

## OpenClaw

- Primary architecture donor for Node Protocol patterns.
- Selective adaptation and protocol study.
- Not a direct Ptah Core dependency.
- Assistant, channel, reasoning and memory behavior excluded.

## Daytona

- Architecture-history donor for Workspace Provider lifecycle and runner separation.
- Study only because the public repository is unmaintained and AGPL-3.0.
- Not a direct dependency or code foundation.
- Native Ptah providers plus OCI/container machinery are the initial implementation direction.

---

# Consequences

## Positive

- Nodes can serve many workspaces and facilities.
- Ptah remains independent of one sandbox vendor.
- Local, cloud and future mini-PC execution share the same contracts.
- Provider limitations are represented honestly.
- Large streams can evolve independently from the control protocol.
- The future operating environment can add providers without redesigning Ptah Core.

## Costs

- Ptah must design and maintain neutral schemas.
- Provider conformance testing is mandatory.
- Node reconnect and workspace recovery require separate state machines.
- More than one transport may be needed for control, events and large streams.

## Do-not-break rule

> Never collapse Node, Workspace, Activity, Object or Session into one universal record. They have different lifecycles, ownership and recovery semantics.

## Required proof before freeze

1. A mock node connects, negotiates protocol and publishes capabilities.
2. Capability updates survive reconnect without creating a new node identity.
3. One node hosts two concurrent workspaces through a provider.
4. Workspace failure does not disconnect the node or stop the other workspace.
5. A detached terminal can be reattached.
6. Provider operations are idempotent.
7. Unsupported lifecycle operations are reported explicitly.
8. Large object transfer uses a separate data stream.
9. No assistant or private consumer identity appears in the public contracts.