# Phase 0A — WP02B Activity, Event and Observability Composition

**Status:** EXTERNAL DONOR COMPOSITION COMPLETE  
**Date:** 2026-07-17  
**Runtime code:** NOT STARTED

## Purpose

Complete the Activities, events, recovery and observability side of Ptah's core runtime donor cluster.

## Donors inspected and saved

- Temporal Server
- Temporal Rust SDK / Core SDK
- NATS Server
- JetStream implementation paths
- NATS Rust `async-nats` client
- OpenTelemetry Collector
- OpenTelemetry Collector Contrib
- OpenTelemetry Specification

## Composite result

```text
Ptah Activity Ledger
  caller-visible portable state and backend references

Temporal
  durable orchestration, history, retries, timers and worker recovery

NATS Core
  low-latency internal commands, request/reply and live events

JetStream
  bounded replayable operational events and acknowledgements

OpenTelemetry
  traces, metrics, logs and resource correlation

Dedicated stream transports
  PTY, Object/file, screen, audio/video and large Artifact bytes

Ptah Proof Receipts
  durable hash-linked evidence of side effects and produced Artifacts
```

No one of these layers is universal truth.

## Accepted boundary

Saved as `decisions/ADR-0003-ACTIVITY-EVENT-OBSERVABILITY-BOUNDARY.md`.

Key decisions:

1. Ptah owns a neutral Activity contract and Activity Ledger.
2. Temporal is the primary durable-backend candidate, not the public Activity model.
3. NATS is the primary internal live-event candidate; NATS subjects remain implementation details.
4. JetStream is for bounded replayable operational events, not the sole ledger or workflow engine.
5. OpenTelemetry is the telemetry standard/pipeline, not canonical execution state or proof alone.
6. Large streams remain separate from workflows, event messages and telemetry.
7. Side-effecting operations require operation IDs, idempotency keys and durable receipts.
8. Each Activity type declares retry semantics explicitly.
9. Disconnected Nodes require a Ptah-owned local outbox/journal and reconciliation process.
10. Proof-critical receipts are durable and unsampled even when ordinary telemetry is sampled.

## Saved evidence

- `donors/TEMPORAL.md`
- `donors/NATS-JETSTREAM.md`
- `donors/OPENTELEMETRY.md`
- `decisions/ADR-0003-ACTIVITY-EVENT-OBSERVABILITY-BOUNDARY.md`

## Requirement closure movement

- `CORE-002 Concurrent Activity runtime` — external composite candidate selected; internal worker recovery and validation remain.
- `RELAY-001 Live event transport` — external composite candidate selected; event schema and conformance remain.
- `RELAY-002 Durable Activity recovery` — Temporal backend candidate selected; backend-neutral ledger and proof remain.
- `OBS-001 Observability/resource accounting` — OpenTelemetry machinery selected; Ptah semantic conventions and proof classes remain.
- `DIST-001 Multi-Node placement/transfer` — event/correlation foundations improved; scheduler/object transport still open.
- `OFFLINE-001 Local-first/intermittent operation` — local journal/reconciliation boundary accepted; sync implementation still open.

## Remaining work before the core-runtime cluster can close for design

1. Recover internal THETECHGUY worker, process, terminal, relay, sync, evidence and recovery implementations.
2. Compare internal guarantees against the external composition.
3. Define versioned Phase 0B Activity, Event, telemetry and receipt schemas.
4. Decide the first vertical slice's durable backend deployment while preserving Temporal compatibility.
5. Define local journal/outbox and reconciliation contracts.
6. Complete licence/dependency review for selected deployment components.
7. Build validation plans and golden failure scenarios.
8. Amend ADRs if internal recovery reveals an intentional stronger design.

## Next inspection unit

Recover the internal core-runtime evidence cluster before declaring the subsystem closed:

- Hunter/AgentOps job and operation records;
- Foreman task/process state;
- Sergeant evidence and receipts;
- TechGuy Relay registration/heartbeat lessons;
- Software Builder and other background workers;
- Hunter online/local sync and failure-continuation rules;
- existing terminal/process/browser bridges;
- MIBU/device operation correlation and stale-result rejection.
