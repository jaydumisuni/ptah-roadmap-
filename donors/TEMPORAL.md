# Donor Record — Temporal

**Phase:** 0A  
**Status:** FIRST-PASS COMPLETE — DURABLE EXECUTION DONOR  
**Inspected:** 2026-07-17

## Identity

### Temporal Server

- Canonical URL: https://github.com/temporalio/temporal
- Default branch: `main`
- Pinned commit: `3aec474f48ab52a2f8299bdfdf030143f8514800`
- Licence: MIT
- Activity: Active and mature

### Temporal Rust SDK / Core SDK

- Canonical URL: https://github.com/temporalio/sdk-rust
- Pinned commit: `3dac9013b9031e5ffd51d7335838585b2db42efb`
- Licence: Apache-2.0
- Rust SDK status: Public Preview at the inspected pin
- Core SDK status: production foundation used by the TypeScript, Python, .NET and Ruby SDKs

- Classification: Durable workflow/activity backend and architecture donor
- Ptah targets: durable Activity history, retries, timers, cancellation, worker execution, crash recovery and replay

## Files/components inspected

- Temporal server `README.md`
- `docs/architecture/README.md`
- service architecture: Frontend, History and Matching
- Workflow/Activity separation and event-sourced replay model
- Temporal Rust SDK `README.md`
- Rust Core SDK `ARCHITECTURE.md`
- worker polling and task-completion model
- integration/load-test and OpenTelemetry hooks documented by the Rust SDK

## Verified capabilities and patterns

- Durable execution that survives transient failures in server and user-hosted worker processes.
- Append-only Workflow history and deterministic replay reconstruct state.
- Explicit separation between deterministic Workflow code and side-effecting Activity code.
- Workflow and Activity Task queues polled by user-hosted workers.
- History Service retains durable execution state; Matching Service distributes tasks.
- Horizontal concurrency over many Workflow executions.
- User-hosted execution environments: the orchestration cluster does not need to run user Activities itself.
- Self-hosted server/database or managed cloud deployment.
- Rust Core SDK provides common task polling, state machines and gRPC behavior for several language SDKs.
- Language layers own language-appropriate concurrency while Core manages Temporal protocol/state-machine concerns.
- Integration tests, load tests, history replay tools and OpenTelemetry support are present.

## What Temporal completes

- Durable execution history missing from OpenClaw, workspace platforms and an ordinary message bus.
- Retriable long-running operations, timers and worker crash recovery.
- Separation of orchestration logic from physical execution workers.
- Replayable state and observable Workflow history.
- A proven Task Queue and worker-poll model.

## Important limitations for Ptah

- Temporal Workflows must be deterministic; many Ptah Activities are ordinary processes, transfers, browser sessions and interactive streams rather than deterministic Workflow code.
- Activities are normally at-least-once unless designed otherwise; Ptah must require idempotency keys and receipts for side effects.
- Temporal payload/history is not a place for large files, PTY streams, screen/video data or full Object bytes.
- The server, persistence database and worker estate are operationally substantial for a first small vertical slice.
- Temporal Workflow IDs and histories cannot become Ptah's universal Activity/Object/Session identity.
- The Rust user-facing SDK is still Public Preview; Ptah cannot assume it has the maturity of all established SDKs.
- Interactive low-latency events still require a separate live-event transport.
- Provider snapshots and physical process state remain outside Temporal's responsibility.

## Must not be inherited

- Every Ptah Activity forced to be a Temporal Workflow.
- Deterministic orchestration code confused with side-effecting physical execution.
- Large binary or streaming data stored in Workflow history.
- Temporal-specific IDs or state exposed as Ptah's public canonical contract.
- Automatic retry of non-idempotent device, firmware, payment or destructive operations.
- Temporal Cloud or one SDK language made mandatory.
- Workflow completion treated as proof that an external artifact or device action is valid.

## Integration decision

**ADOPT AS THE PRIMARY DURABLE-BACKEND CANDIDATE, BEHIND PTAH-OWNED ACTIVITY CONTRACTS.**

Temporal is the strongest inspected donor for `CORE-002` and `RELAY-002`. Ptah should design an Activity Orchestrator adapter capable of using Temporal without making Temporal the public Activity model.

For the first vertical slice, Ptah may prove a smaller SQL-backed coordinator if operating Temporal would slow the proof excessively, but the contract and tests must preserve a clean Temporal adoption path. This is an implementation staging decision, not permission to weaken durability semantics.

## Native Ptah gap

Ptah must own:

- Activity, operation and idempotency identities;
- relationship to Workspace, Node, Provider, Object, Artifact and Session;
- classification of retry-safe, non-retryable and human-resumable operations;
- cancellation and compensation semantics;
- external progress and live-event correlation;
- checkpoint references to provider/object state;
- caller-visible state independent of backend Workflow state;
- backend adapter and migration/exit strategy;
- limits preventing large bytes from entering durable history;
- proof receipts for physical side effects.

## SDK/runtime direction

- Temporal Server remains language-neutral over gRPC.
- Rust Core SDK is a valuable architecture donor and possible foundation for a Rust integration.
- Because the end-user Rust SDK is Public Preview, Go or another mature supported SDK remains an exit path for initial worker implementations.
- Ptah's Activity worker protocol must remain language-neutral so facilities can run in Rust, Go, Python, TypeScript, Java or other suitable languages.

## Exit strategy

Ptah's Activity contract and ledger remain backend-neutral. A native SQL coordinator or another durable workflow engine can replace Temporal if required. Stored Ptah Activity/receipt state must not depend solely on Temporal history retention.

## Validation required

1. Start a long Activity and terminate a worker; a new worker resumes without duplicate side effects.
2. Terminate and restart the control plane while Workflow history remains durable.
3. Exercise retries, non-retryable failure, cancellation, timers and manual waiting.
4. Correlate durable history with live events and OpenTelemetry traces.
5. Keep Object bytes and PTY/display streams outside Workflow history.
6. Prove idempotency and receipts for a side-effecting operation.
7. Reconstruct caller-visible Ptah Activity state without exposing Temporal-specific schemas.
8. Demonstrate an alternate coordinator against the same Ptah contract or a documented migration test.
