# Donor Record — NATS Server, JetStream and Rust Client

**Phase:** 0A  
**Status:** FIRST-PASS COMPLETE — LIVE EVENT FABRIC DONOR  
**Inspected:** 2026-07-17

## Identity

### NATS Server

- Canonical URL: https://github.com/nats-io/nats-server
- Default branch: `main`
- Pinned commit: `146b0be65b3591e925cce61ce9d2cae32cdeb227`
- Licence: Apache-2.0
- Activity: Active CNCF project

### Rust Client

- Canonical URL: https://github.com/nats-io/nats.rs
- Pinned commit: `d00e6b58d8da89a1b60f23b756173b6379dccbd7`
- Licence: Apache-2.0
- Selected crate direction: `async-nats`; the older `nats` crate is deprecated

- Classification: Internal live event, command and intermittent-connectivity fabric donor
- Ptah targets: Node events, Activity progress, request/reply commands, capability announcements, streaming output, replay and edge communication

## Files/components inspected

- NATS Server `README.md`
- server JetStream stream, consumer, storage and clustering source locations
- JetStream acknowledgement and consumer implementation paths
- Rust client `README.md`
- `async-nats` Core NATS, JetStream, KV, Object Store and Service API surfaces
- client layering between protocol-level `async-nats` and higher-level Orbit utilities

## Verified capabilities and patterns

- Lightweight communication across cloud, on-premise, edge and small devices.
- More than forty client-language implementations.
- Core publish/subscribe and request/reply communication.
- Subject-based routing and service-style command patterns.
- JetStream persistent streams, consumers and acknowledgement-based delivery.
- Clustered JetStream storage and recovery implementation.
- Rust `async-nats` supports Core NATS, JetStream API/management, KV, Object Store and Service API.
- Official client parity is treated as a protocol-level concern; higher-level opinionated utilities are separated.
- TLS, authentication and reconnection belong to the core client layer.
- Apache-2.0 permits direct dependency and adaptation with attribution.

## What NATS completes

- Low-latency internal event distribution missing from Temporal's durable orchestration history.
- Request/reply command transport and capability announcements.
- A practical fabric between online control plane, local Nodes and edge/device Nodes.
- JetStream replay and acknowledgement for events that need limited persistence without becoming full workflows.
- Language-neutral communication for polyglot Facilities.

## Important limitations for Ptah

- Core NATS delivery is not durable workflow history.
- JetStream persistence does not replace Temporal-style timers, deterministic orchestration, compensation or full Activity state machines.
- At-least-once delivery and redelivery require idempotent consumers.
- Event retention and consumer state cannot become Ptah's only canonical Activity ledger.
- NATS payloads are not a substitute for object/file, PTY, screen or media streaming protocols.
- Subject naming and message schemas need Ptah-owned versioning and tenancy boundaries.
- A central NATS deployment alone does not solve offline local execution; Nodes need local queues/state and reconciliation.
- JetStream Object Store is not automatically Ptah's universal durable Object storage.

## Must not be inherited

- NATS subjects exposed as Ptah's public API contract.
- Message delivery interpreted as proof an operation completed.
- Automatic redelivery of non-idempotent physical/device operations.
- Large artifact bytes or continuous screen/video streams placed on ordinary event subjects.
- JetStream used as the sole source of truth for Workspaces, Objects, Activities or Sessions.
- One NATS cluster made an irreversible architectural dependency.
- Deprecated Rust `nats` crate selected for new Ptah code.

## Integration decision

**ADOPT AS THE PRIMARY INTERNAL LIVE-EVENT FABRIC CANDIDATE, BEHIND PTAH EVENT CONTRACTS.**

NATS/JetStream is the strongest inspected donor for the internal side of `RELAY-001` and part of `DIST-001` and `OFFLINE-001`.

The public Ptah Node Protocol remains independent. NATS may carry internal commands/events between services and connected Nodes, while Temporal or another durable coordinator owns long-running orchestration history.

## Event-class direction

Ptah should distinguish:

1. **Ephemeral live events** — terminal progress, presence and fast status; Core NATS candidate.
2. **Replayable operational events** — bounded Activity progress, Node transitions and notifications; JetStream candidate.
3. **Durable orchestration state** — retries, timers, cancellation and long-running state; Temporal/backend ledger.
4. **Large streams and Objects** — dedicated PTY, object, display and media transports.

## Native Ptah gap

Ptah must own:

- versioned event envelope and schema registry;
- event identity, source, Workspace/Activity/Node/Object correlation and connection epoch;
- sequence and replay cursor semantics;
- subject mapping hidden behind the event adapter;
- retention and delivery class per event type;
- consumer idempotency and duplicate detection;
- backpressure and slow-consumer behavior;
- local queue/reconciliation for disconnected Nodes;
- transport-independent public subscriptions;
- bridge to OpenTelemetry traces and durable Activity history.

## Exit strategy

Ptah's Event Fabric interface must be implementable over NATS, WebSocket/SSE plus a durable store, another broker or a local embedded transport. Subject names and JetStream metadata are never public canonical truth.

## Validation required

1. Route request/reply commands and live Activity progress across several services.
2. Disconnect a Node, retain permitted replayable events and reconcile on reconnect.
3. Prove ordered per-stream sequence and duplicate handling.
4. Prove bounded buffers and backpressure with a slow consumer.
5. Restart NATS/JetStream and recover retained events/consumer state.
6. Correlate events to Temporal history and OpenTelemetry traces.
7. Prove large PTY/Object/display streams remain outside ordinary event messages.
8. Run a compatibility test using `async-nats` and at least one other official client language.
