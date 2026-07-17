# Phase 0A — WP02C Internal Core-Runtime Recovery

**Status:** FIRST-PASS COMPLETE — CORE RUNTIME CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Runtime code:** NOT STARTED

## Purpose

Compare the external core-runtime donor composition against existing THETECHGUY implementations and intentional operating rules before freezing Ptah contracts.

## Internal sources inspected and saved

- Hunter AgentOps
- Hunter Foreman
- Sergeant
- TechGuy Relay
- THETECHGUY Software Builder
- Hunter CodeOps
- MIBU
- Hunter runtime, local/source sync, file/process bridges, persistent Workflow Manager and Events V3 D1 outbox

Saved records:

- `internal/HUNTER-AGENTOPS.md`
- `internal/HUNTER-FOREMAN.md`
- `internal/SERGEANT.md`
- `internal/TECHGUY-RELAY.md`
- `internal/SOFTWARE-BUILDER.md`
- `internal/HUNTER-CODEOPS.md`
- `internal/MIBU.md`
- `internal/HUNTER-RUNTIME-SYNC.md`

## Internal capabilities that strengthen the external composition

### Operation and ownership boundaries

- Stable operation ID is separate from task text.
- Orchestrator, specialist executor, evidence producer and reviewer have different ownership.
- Approval/restriction references come from the caller/operation chain rather than Ptah inventing universal policy.
- Stable bridges keep specialist ownership outside the caller UI.

### Evidence and proof

- Result, evidence, review and authoritative external outcome are separate records.
- Evidence can include terminal output, files, commits, tests, logs, screenshots, archives, API responses and physical-device state, with different strengths.
- Review findings must be grounded to exact source/checkpoints.
- UNKNOWN, stale or unsupported evidence does not silently pass.
- Static/CI proof and physical-device proof have explicit boundaries.
- Complete release/Artifact bundles and checksum manifests are contractual.

### Correlation and stale-result rejection

- Device operations use random correlation nonces.
- Proof protocol and producer/app version are validated.
- Stale proof lines with another nonce are rejected.
- Launch evidence, runtime armed, completion and authoritative external result are distinct levels.
- A late authoritative status may reconcile a waiting operation.

### Durability and recovery

- Hunter has three distinct execution patterns:
  - process-local asynchronous Tasks;
  - JSON-file-backed checkpointed Workflows;
  - D1 transactional outbox with idempotency, claim, attempt history, retry/dead states and stale-lock recovery.
- The D1 outbox is the strongest existing internal durable-work pattern.
- Retry-of/resume-of and checkpoint relationships already exist.
- Partial, pending, blocked, failed and dead states are distinguished.

### Workspace and mutation safety

- Workspace-relative paths are validated before execution/edit.
- Dry-run and apply are separate.
- Existing files are backed up before mutation.
- Local file access is rooted, bounded and secret-aware.
- Writes may remain disabled until routed through approval/proof.
- Source synchronization reports status first, refuses dirty/divergent update and uses fast-forward-only apply.

### Shared machinery and background work

- Shared SDKs, caches, build tools and temporary workspaces should not be copied into each Project.
- Tool health and blocked reasons are planning inputs.
- Heavy work requires background workers, logs, progress, cancellation/request-stop and status.
- Build planning/readiness is distinct from actual build completion.

### Operational honesty and degradation

- Connected/not connected/degraded states are explicit.
- Optional Facility/provider import or configuration failure can degrade one capability without stopping unrelated safe capabilities.
- Message transport success is not external task fulfillment.
- Existing authoritative results prevent repeated physical actions.

## Internal implementations that must not become Ptah Core unchanged

- in-memory task/Node registries;
- daemon-thread execution as durable workers;
- local JSON files as multi-Node transactional state;
- synchronous subprocess calls as universal Activity execution;
- timestamp/short IDs without durable operation identity;
- text log markers as authenticated proof;
- one active mission across all Ptah work;
- priority-only routing;
- monolithic controller/server/UI files;
- Hunter, department, provider, customer or product identities in public Ptah schemas;
- D1/R2/KV or one cloud provider as mandatory public implementation;
- build plans described as completed builds;
- automatic retry of physical or non-idempotent operations;
- force sync/reset or silent conflict overwrite.

## Composite core-runtime result

```text
Ptah-owned contracts
  Node Protocol
  Workspace Provider
  Activity Ledger
  Event Envelope
  Facility Manifest
  Object/Artifact references
  Session/Checkpoint manifest
  Operation Receipt and Proof Levels

External machinery
  containerd/OCI        owned container execution
  Temporal              durable orchestration backend candidate
  NATS/JetStream        live and bounded replayable Event Fabric candidate
  OpenTelemetry         traces, metrics and logs
  Dev Containers        portable compatibility format

External completion donors
  OpenClaw              Node/gateway patterns
  Daytona               lifecycle/runner history
  Coder                 persistent human Workspace patterns
  E2B/Desktop           automation and graphical sandbox API patterns
  DevPod                provider portability
  OpenHands             caller/tool/computer interaction patterns

Internal completion evidence
  AgentOps              operation/evidence ownership
  Foreman               status/bridge honesty
  Sergeant              Facility manifests and grounded proof
  Relay                 pairing/heartbeat lessons and anti-patterns
  Software Builder      shared machinery/background-worker requirements
  CodeOps               capability route, dry-run/apply, backups and review loop
  MIBU                  nonce/protocol/version proof and stale rejection
  Hunter runtime        safe sync, checkpoints, outbox, attempts and degradation
```

## Accepted decisions produced

- ADR-0001 — Node Protocol and Workspace Provider Boundary
- ADR-0002 — Composite Donor Closure Method
- ADR-0003 — Activity, Event and Observability Boundary
- ADR-0004 — Operation Identity, Receipts and Proof Levels

## Core-runtime requirement verdict

The following requirements are now **closed for Phase 0B contract design**, while still requiring schemas, conformance tests and later live proof before build:

- `CORE-001` Persistent Workspace model
- `CORE-002` Concurrent Activity runtime
- `CORE-004` Facility/plugin host foundation
- `CORE-005` Node Protocol and capability reporting
- `RELAY-001` Live Event transport
- `RELAY-002` Durable Activity recovery
- `EXEC-001` Terminal/process supervision foundation
- `EXEC-002` OCI/container Workspace Provider foundation
- `SESSION-001` core checkpoint/recovery relationship model
- `OBS-001` logs, metrics, traces and resource-accounting foundation
- `OFFLINE-001` local journal/reconciliation boundary

`DIST-001` remains only partially closed because scheduling, secure Node identity/networking and Object transport require later donor groups.

`EXEC-003` remains open until BuildKit/Dagger and internal Builder are compared as a build subsystem.

## Phase 0B contracts required from this closure

1. Node identity, connection epoch and capability schema.
2. Workspace Provider capability/lifecycle contract.
3. Activity Ledger, retry class, dependency and backend-reference schema.
4. Event envelope, retention class and replay cursor.
5. Local Node journal/outbox and reconciliation contract.
6. Facility manifest and invocation/result contract.
7. Operation receipt, proof level and authority class schema.
8. Proof-critical receipt versus operational telemetry classification.
9. PTY/Object/display/media stream-reference contract.
10. Checkpoint, retry-of, resume-of and provider-snapshot references.
11. Credential-reference and secret-redaction contract.
12. Mutation plan, before/after Object version and rollback contract.
13. Failure taxonomy and degraded-capability semantics.
14. OTel semantic conventions and resource accounting.

## Known implementation staging question

Temporal is the preferred durable-backend candidate. The first vertical slice may temporarily use a smaller SQL-backed coordinator only if:

- all Phase 0B Activity/receipt contracts are preserved;
- durability, idempotency and restart tests remain mandatory;
- the implementation is not falsely claimed as Temporal-equivalent;
- a tested migration/adoption path remains.

## Next Phase 0A group

Continue requirement closure with the deterministic build and provenance cluster:

- BuildKit;
- Dagger;
- internal Software Builder comparison;
- Witness;
- in-toto;
- Cosign/Sigstore/Rekor/Fulcio;
- ORAS;
- SBOM donors as required.

This group must close build recipes, caches, Artifact relationships, attestations, signing and independently verifiable proof without making one build or registry product universal Ptah truth.
