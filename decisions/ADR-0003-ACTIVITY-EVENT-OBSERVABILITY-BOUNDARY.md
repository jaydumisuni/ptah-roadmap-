# ADR-0003 — Activity, Event and Observability Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Phase:** 0A requirement closure

## Context

Ptah requires several kinds of state and communication that are often incorrectly collapsed into one queue or one workflow system:

- caller-visible Activity state;
- durable long-running orchestration;
- low-latency commands and progress;
- reconnectable/replayable operational events;
- terminal, Object, screen and media streams;
- logs, metrics and traces;
- proof that physical side effects and Artifacts occurred.

Temporal, NATS/JetStream and OpenTelemetry each solve part of this problem. None is the complete Ptah Activity Runtime.

## Decision

Ptah will own a neutral **Activity contract and Activity Ledger**. External machinery is placed behind distinct adapters:

1. **Durable Orchestrator** — Temporal is the primary backend candidate.
2. **Live Event Fabric** — NATS is the primary backend candidate.
3. **Replayable Event Stream** — JetStream is the primary bounded-persistence candidate.
4. **Telemetry Pipeline** — OpenTelemetry/OTLP and Collector are the primary machinery.
5. **Large Data Streams** — dedicated PTY, Object, display and media transports.
6. **Proof and Receipts** — Ptah-owned durable records linked to Objects and Artifacts.

No backend-specific identifier or schema becomes the public canonical Activity model.

---

# Ptah Activity Ledger

The Activity Ledger is the portable caller-visible state of work.

It records at minimum:

```text
activity_id
operation_id
idempotency_key
workspace_id
node_id
provider_id
facility_id
caller_reference
activity_type
requested_state
observed_state
priority
dependencies
inputs
outputs
progress
retry_class
cancellation_state
checkpoint_references
produced_object_ids
produced_artifact_ids
failure
created_at
started_at
updated_at
completed_at
backend_references
receipt_references
```

The ledger does not contain large Object bytes or continuous stream payloads.

Backend references may point to Temporal Workflow/Run IDs, NATS stream/consumer metadata, provider process IDs or other implementation details. Those references are replaceable and are not public identity.

## Activity state family

Phase 0B must define a versioned neutral state family capable of representing:

```text
requested
queued
leasing
preparing
running
waiting
paused
resuming
cancelling
cancelled
retrying
recovering
completed
failed
unknown
```

Facilities and durable backends may expose richer internal states, but map them to the neutral family.

---

# Durable Orchestrator boundary

Temporal may own:

- durable workflow history;
- timers;
- retries;
- cancellation orchestration;
- worker task queues;
- long-running wait states;
- crash recovery;
- orchestration replay.

Temporal does not own:

- Ptah Activity identity;
- Object or Artifact bytes;
- PTY/display/media streams;
- provider filesystem truth;
- proof that a physical side effect is correct;
- the public Ptah API.

## Retry rule

Every Activity type must declare one of:

```text
retry_safe
retry_requires_idempotency_receipt
non_retryable
manual_resume_only
compensating_action_required
```

Device, firmware, payment, destructive and external physical operations must never receive automatic retry merely because a workflow engine supports retries.

## Staging rule

Temporal is the primary durable-backend candidate. The first vertical slice may use a smaller SQL-backed implementation only when:

- the same Activity contract is preserved;
- durability and idempotency tests remain mandatory;
- migration to Temporal is explicitly retained;
- the smaller implementation is not described as equivalent without proof.

---

# Event Fabric boundary

## Public control protocol

The Ptah Node Protocol remains the versioned public/Node-facing control contract.

It handles requests, responses, connection/session negotiation, capability publication and public events. It does not expose NATS subjects as the API.

## Internal live events

Core NATS may carry:

- Activity progress;
- Node presence and health transitions;
- capability announcements;
- service commands and request/reply;
- fast operational notifications;
- terminal/session metadata;
- Artifact/Object availability notifications.

## Replayable operational events

JetStream may retain bounded event classes requiring acknowledgement/replay, including:

- Activity state transitions;
- Node disconnect/reconnect transitions;
- limited progress checkpoints;
- work dispatch receipts;
- notification delivery.

JetStream is not the sole Activity Ledger or workflow history.

## Event envelope

Phase 0B must define a versioned envelope containing at minimum:

```text
event_id
event_version
event_type
occurred_at
source_type
source_id
project_id
workspace_id
activity_id
operation_id
node_id
provider_id
facility_id
object_id
artifact_id
connection_epoch
stream_id
sequence
trace_id
causation_id
correlation_id
retention_class
payload_reference_or_small_payload
```

Only relevant fields are populated. Sensitive/private identities must not appear in public-safe envelopes unless explicitly intended.

## Delivery rule

Message delivery is not proof of successful execution.

Consumers must handle duplicate or redelivered events. Side-effecting commands require idempotency keys and receipts.

---

# Large-stream boundary

Ordinary control/event messages must not carry large or continuous data.

Separate transports are required for:

- PTY input/output;
- command log streams;
- Object/file transfer;
- screen and application display;
- audio/video/media;
- large Artifact upload/download.

Control events carry stream identity, metadata, hashes, state and authorization references.

---

# Observability boundary

OpenTelemetry may carry:

- distributed traces;
- operational logs;
- metrics;
- resource attributes;
- performance and usage data;
- Collector/internal health.

OpenTelemetry does not own:

- canonical Activity state;
- guaranteed audit/proof receipts;
- Object or Artifact identity;
- workflow recovery;
- event delivery.

## Correlation semantics

Phase 0B must define Ptah semantic conventions for Project, Workspace, Activity, operation, Node, Provider, Facility, Object, Artifact and Session references.

Trace IDs complement but do not replace Ptah IDs.

## Evidence classes

Ptah distinguishes:

1. **Operational telemetry** — may be sampled or aggregated.
2. **Proof-critical receipts** — durable, unsampled and hash-linked.
3. **Sensitive diagnostics** — access-controlled and redacted.

Telemetry pipelines may transform or drop ordinary telemetry; they must not silently remove proof-critical receipts.

---

# Offline and intermittent Nodes

A disconnected Node requires a local outbox/journal for permitted local work.

The Node must record:

- local Activity state transitions;
- event sequence and connection epoch;
- idempotency/operation identifiers;
- produced Object and Artifact references;
- pending acknowledgements;
- reconciliation conflicts.

On reconnect:

1. identity and epoch are negotiated;
2. duplicate commands/events are rejected by stable IDs;
3. missing events are replayed according to retention class;
4. durable Activity state is reconciled;
5. Object/Artifact content is transferred separately;
6. conflicts are surfaced rather than silently overwritten.

NATS/JetStream may assist transport, but the local journal is Ptah-owned.

---

# Failure semantics

A Ptah Activity may encounter separate failures:

```text
control_failure
event_transport_failure
durable_orchestrator_failure
node_failure
provider_failure
facility_failure
process_failure
stream_failure
object_transfer_failure
artifact_validation_failure
telemetry_failure
caller_cancellation
```

Failure in telemetry or optional live transport must not automatically terminate physical work. Failure of required durable state or execution machinery must produce explicit degraded/recovering status.

---

# Donor decisions

## Temporal

- Primary durable-orchestration backend candidate.
- Used behind Ptah Activity contracts.
- Deterministic Workflows do not define every Activity.
- Large bytes and streams excluded from Workflow history.
- Rust SDK public-preview status retained as a risk; mature SDK and backend-neutral worker paths remain.

## NATS and JetStream

- Primary internal live/replayable event-fabric candidate.
- NATS subjects and consumer metadata remain private implementation details.
- At-least-once/redelivery behavior requires idempotent consumers.
- Not the canonical Activity ledger.

## OpenTelemetry

- OTLP and semantic conventions adopted for telemetry compatibility.
- Collector wrapped as a replaceable pipeline.
- Not canonical execution state or proof by itself.

---

# Consequences

## Positive

- Ptah can combine low latency with durable recovery.
- Backend systems remain replaceable.
- Interactive streams are not slowed or bloated by workflow/event storage.
- Telemetry can be sampled without weakening proof receipts.
- Offline Nodes can reconcile safely.
- Side effects are protected by idempotency and explicit retry classes.

## Costs

- Ptah must maintain an Activity Ledger and projections alongside backend references.
- Correlation across several systems requires strict schemas and tests.
- Local outbox/reconciliation logic is mandatory for intermittent Nodes.
- Operators may run Temporal, NATS and OpenTelemetry components at scale.
- The first vertical slice must be intentionally smaller while preserving these boundaries.

## Do-not-break rule

> Never use one queue, workflow history, telemetry backend or message stream as universal Ptah truth. Activity state, durable orchestration, live events, large streams, telemetry and proof receipts have different guarantees and must remain explicit.

---

# Required proof before freeze

1. Ten concurrent Activities emit independent live events and traces.
2. A worker dies and the durable backend resumes without duplicate side effects.
3. NATS disconnect/reconnect preserves defined replayable events and rejects duplicates.
4. A slow consumer triggers bounded backpressure rather than unbounded memory growth.
5. Collector/exporter failure does not stop required execution and buffered telemetry later recovers.
6. One Activity can be traced from request through Node, Provider, Facility and Artifact.
7. Proof-critical receipt remains available even when ordinary telemetry is sampled.
8. PTY/Object/display streams remain outside workflow and event payloads.
9. A disconnected Node journals local state and reconciles correctly.
10. Backend identifiers can change without changing public Ptah Activity identity.
