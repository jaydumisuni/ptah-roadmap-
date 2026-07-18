# Phase 0B — WP02 Activity, Operation, Attempt, Event, Receipt and Proof

**Status:** CANDIDATE COMPLETE — READY FOR DOWNSTREAM PHASE 0B USE; NOT IMPLEMENTATION-FROZEN  
**Date:** 2026-07-18  
**Contract candidate:** `ptah.activity` `0.1.0` with corrected request schemas at `0.1.1`  
**Implementation:** NOT STARTED

## Purpose

Convert the Phase 0A Activity/Event/observability and Operation/Receipt/proof decisions into one coherent machine-readable contract layer.

The result must support concurrent durable work, retries, cancellation, reconnect/recovery, evidence, independent review and external authoritative results without confusing transport messages, telemetry or optimistic UI with truth.

---

# 1. Inputs

- `decisions/ADR-0003-ACTIVITY-EVENT-OBSERVABILITY-BOUNDARY.md`
- `decisions/ADR-0004-OPERATION-RECEIPTS-PROOF-LEVELS.md`
- `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`
- `contracts/PHASE-0B-COMMON-CONTRACT-CONVENTIONS.md`
- `schemas/phase-0b/common/schema-catalog.v0.1.0.json`
- `work-packages/PHASE-0B-ENTRY-CONTRACT-PROOF-INPUTS.md`

---

# 2. Outputs committed

## Normative contracts

- `contracts/PHASE-0B-WP02-ACTIVITY-EVENT-PROOF-CONVENTIONS.md`
- `contracts/PHASE-0B-WP02-ENTITY-KIND-SUPPLEMENT.md`
- `contracts/PHASE-0B-WP02-PROOF-LEVEL-REGISTRY.md`

## Candidate schemas

Active catalog:

- `schemas/phase-0b/activity/schema-catalog.v0.1.1.json`

Definitions:

- `schemas/phase-0b/activity/definitions.v0.1.0.schema.json`
- `schemas/phase-0b/activity/request-definitions.v0.1.0.schema.json`

Core work records:

- `schemas/phase-0b/activity/activity-request.v0.1.1.schema.json`
- `schemas/phase-0b/activity/activity.v0.1.0.schema.json`
- `schemas/phase-0b/activity/activity-dependency.v0.1.0.schema.json`
- `schemas/phase-0b/activity/cancellation-request.v0.1.1.schema.json`
- `schemas/phase-0b/activity/manual-action-request.v0.1.1.schema.json`
- `schemas/phase-0b/activity/operation.v0.1.0.schema.json`
- `schemas/phase-0b/activity/attempt.v0.1.0.schema.json`
- `schemas/phase-0b/activity/reconciliation-run.v0.1.0.schema.json`

Event and proof records:

- `schemas/phase-0b/activity/event-payload-type.v0.1.0.schema.json`
- `schemas/phase-0b/activity/event.v0.1.0.schema.json`
- `schemas/phase-0b/activity/proof-level-definition.v0.1.0.schema.json`
- `schemas/phase-0b/activity/proof-claim.v0.1.0.schema.json`
- `schemas/phase-0b/activity/receipt.v0.1.0.schema.json`
- `schemas/phase-0b/activity/review.v0.1.0.schema.json`
- `schemas/phase-0b/activity/verdict.v0.1.0.schema.json`
- `schemas/phase-0b/activity/external-result.v0.1.0.schema.json`

## State machines

- `state-machines/phase-0b/activity-request-lifecycle.v0.1.0.json`
- `state-machines/phase-0b/activity-lifecycle.v0.1.0.json`
- `state-machines/phase-0b/cancellation-request-lifecycle.v0.1.0.json`
- `state-machines/phase-0b/manual-action-request-lifecycle.v0.1.0.json`
- `state-machines/phase-0b/operation-lifecycle.v0.1.0.json`
- `state-machines/phase-0b/attempt-lifecycle.v0.1.0.json`

## Safety net and fixtures

- `conformance/PHASE-0B-WP02-ACTIVITY-EVENT-RECEIPT-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp02/activity-event-receipt-cases.v0.1.0.json`

---

# 3. Candidate architecture

```text
Activity Request
  pre-ledger caller submission and acceptance/rejection

Activity
  durable caller-visible work and lifecycle

Activity Dependency
  exact condition/failure policy between Activities

Operation
  one logical effect or observation request

Attempt
  one physical execution try under exact generations/epoch

Cancellation Request
  separate cancellation lifecycle and cleanup scope

Manual Action Request
  durable human/external action required by an Operation

Event
  live/replayable typed notification

Telemetry
  sampled/aggregated operational observations

Proof Level Definition
  bounded domain vocabulary and non-implication rules

Proof Claim
  one bounded assertion over exact subjects/evidence

Receipt
  append-only correlated producer evidence

Review
  evaluation process over exact checkpoint/evidence

Verdict
  separate immutable conclusion from the Review

Authoritative External Result
  result whose truth belongs to an external system/device

Reconciliation Run
  explicit disposition of late/stale/conflicting evidence and accepted transitions
```

---

# 4. State-model normalization

Phase 0A used several useful but overlapping labels. WP02 normalizes them into separate dimensions.

## Activity lifecycle

```text
queued
preparing
running
waiting
paused
resuming
recovering
completed
failed
cancelled
```

## Moved out of Activity lifecycle

- `requested` → `core.activity_request` lifecycle;
- `leasing` → placement/reservation/Lease records plus Activity `preparing`;
- `cancelling` → `core.cancellation_request` lifecycle;
- `retrying` → Operation retry policy plus new Attempts;
- `detached` → client attachment state;
- `unknown` → projection-health state.

This allows the true facts to coexist. An Activity may remain `running` while:

- the observing client is detached;
- cancellation is requested but not complete;
- Provider health is degraded;
- a UI projection is stale;
- one child Operation is waiting or uncertain.

## Terminality

Activity `completed`, `failed` and `cancelled` are terminal for that Activity entity. A later retry/resume/follow-up after terminal state is a new linked Activity, not a silent resurrection.

Operation/Attempt terminality remains separate.

---

# 5. Request and acceptance boundary

A submitted request is not yet an Activity.

Request acceptance:

1. validates scope/authorization, Workspace, parameters, policy, budgets and duplicate-submission handling;
2. creates a new durable Activity identity;
3. records an acceptance decision/Receipt;
4. links Request to Activity;
5. transitions Activity to `queued`.

A rejected/expired/withdrawn Request creates no Activity.

The initial request/cancellation/manual-action `0.1.0` drafts used bare state fields. Rather than rewriting them, WP02 issued corrected `0.1.1` schemas with versioned state projections and recorded the supersession in catalog `0.1.1`.

---

# 6. Operation and Attempt boundary

## Operation

One logical intended effect or observation.

- identity persists across retries;
- declares targets, action, authority, side-effect class, retry class and idempotency class;
- declares desired bounded proof;
- remains `uncertain` when the physical effect may have occurred but proof is insufficient.

## Attempt

One physical try.

- new ID, attempt number and nonce for every retry;
- exact Node, Provider and workload generations;
- exact connection epoch;
- producer instance/version and backend Aliases;
- own lifecycle/outcome/Receipts.

An Attempt may physically complete while its Operation remains uncertain or failed because required output/read-back proof is absent.

---

# 7. Retry and idempotency

Retry classes:

```text
retry_safe
retry_requires_idempotency_receipt
non_retryable
manual_resume_only
compensating_action_required
```

Idempotency classes:

```text
none_required
operation_identity
explicit_key
provider_key
receipt_guarded
manual_only
compensating
```

Rules:

1. Operation ID and required idempotency key remain stable across Attempts.
2. Attempt ID and nonce always change on retry.
3. Automatic retry requires the declared retry and idempotency policies plus current evidence.
4. Non-idempotent external/physical work is not retried automatically if effect is uncertain.
5. Read-back, authoritative result or manual decision resolves uncertainty.
6. Compensating retry requires an explicit compensating Operation.

---

# 8. Activity dependencies

Dependencies are first-class entities with:

- dependent and dependency Activity refs;
- exact condition;
- failure policy;
- required result/proof refs;
- evidence of satisfaction/manual release.

Dependency Events are notifications only. The durable condition is reread/reconciled.

Cycles are rejected unless a future explicit coordination contract authorizes them.

---

# 9. Cancellation and manual action

## Cancellation

Cancellation is a request lifecycle:

```text
requested
acknowledged
completing
completed
rejected
expired
```

It records exact subject/scope, authority, cleanup class, reason, deadlines and evidence.

Cancellation races remain visible. An Activity may complete before cancellation takes effect; this does not rewrite either history.

Activity reaches `cancelled` only after the required cancellation/cleanup boundary is proven.

## Manual action

A durable Manual Action Request carries:

- exact parent Activity/Operation;
- action kind;
- authorized responder(s);
- instruction/context refs;
- response schema;
- expiry;
- response, responder and outcome.

An Event/notification alone does not satisfy a manual-action wait.

---

# 10. Event and telemetry boundary

## Event

A typed Event carries source, subject, correlations, generations, epoch, sequence scope, payload schema/class and retention/privacy.

Event classes:

```text
ephemeral
replayable
ledger_derived
proof_notification
```

`proof_notification` points to a Receipt; the Event is not proof.

Large/continuous output uses streams/Objects/Artifacts rather than inline Event payloads.

Duplicate, out-of-order and missing Events are expected and reconciled.

## Telemetry

Logs, metrics and traces are operational observations. They may be sampled/lost/transformed and do not own Activity state or side-effect proof.

Trace IDs remain correlation metadata, not canonical identity.

---

# 11. Receipt and bounded proof model

A Receipt is immutable append-only evidence tied to:

- exact Activity/Operation/Attempt;
- idempotency key and nonce;
- Node/Provider/workload generations;
- connection epoch;
- producer identity/version/authority;
- proof claims;
- inputs/outputs/Artifacts/checkpoints/hashes;
- events/traces/signatures/attestations;
- privacy, retention and limitations.

Corrections create new Receipts and preserve the original.

The proof registry is partially ordered by domain:

- request/dispatch;
- runtime;
- output;
- external result;
- review.

No cross-domain implication is automatic.

Examples:

- `operation_completed` does not imply `output_created`;
- `output_created` does not imply read-back;
- read-back does not imply hash match;
- external result recorded is not authoritative external result;
- independently reviewed does not imply PASS or acceptance.

---

# 12. Review, Verdict and external authority

A Review is an evaluation process over exact evidence/checkpoint/protocol.

A Verdict is a separate immutable conclusion:

```text
pass
fail
conditional
inconclusive
unsupported
```

A Verdict does not mutate the subject automatically and does not equal caller acceptance.

An Authoritative External Result retains source identity, source alias, authority evidence, exact result schema/payload, time/freshness and integrity/read-back evidence.

Ptah may record and verify it but cannot fabricate it from a weaker Receipt.

---

# 13. Reconciliation and intermittent Nodes

A Reconciliation Run explicitly compares:

- durable ledger/projections;
- current generations and epoch;
- local Node journals/outbox;
- Events;
- Receipts;
- Objects/Artifacts;
- authoritative external results.

Every input gets a disposition such as:

```text
accepted_current
accepted_historical
duplicate
stale_generation
stale_epoch
wrong_subject
wrong_nonce
unauthenticated
contradictory
inconclusive
rejected
```

Accepted/rejected transitions are retained.

Event/telemetry loss does not erase durable truth. Content transfer remains separate from Event replay.

---

# 14. Candidate review corrections

## Mutable request state

The first request schemas used bare state and sequence fields. WP02 corrected this through new `0.1.1` schemas and versioned lifecycle definitions instead of mutating the earlier candidate files.

## Activity lifecycle collision

Phase 0A labels `requested`, `leasing`, `cancelling`, `retrying`, `detached` and `unknown` were split into their proper entities/dimensions.

## Universal proof ladder

The earlier ordered vocabulary was retained but redefined as bounded domains with explicit non-implication. This prevents a runtime completion claim from being displayed as output verification or acceptance.

## Attempt completion versus Operation success

The schemas/state machines now allow physical Attempt completion without Operation success when output/read-back/authority proof is absent.

---

# 15. Known candidate limitations

1. Schemas/state machines are candidate contracts, not executable runtime implementations.
2. The executable JSON Schema/semantic conformance harness remains WP13/WP14 work.
3. Event payload maximum size is declared by payload registration but enforcement is transport-specific.
4. Global Event ordering is intentionally absent; sequence is scoped and semantic validation is required.
5. State-machine definitions still need executable graph checks for duplicate/missing states and unreachable transitions.
6. Proof-level definition instances are currently normative in the Markdown registry; a frozen entity corpus will be created with the golden corpus.
7. Receipt signatures/attestations reference later provenance contracts.
8. Resource usage and telemetry schemas are deferred to Node/observability packages.
9. Offline journal storage format is deferred, though required fields/behavior are fixed.
10. Activity kinds and Operation kinds need separate registries as domain Facilities are designed.
11. No Temporal, NATS, JetStream, SQL, OTel or other backend is selected.
12. No database indexing/projection/storage layout is selected.
13. Schema bytes are not frozen/digest-signed yet.

These limitations do not block WP03 domain schema design.

---

# 16. Candidate completion gate

WP02 is candidate-complete because:

- Activity/Operation/Attempt identity and state are explicit;
- request/dependency/cancellation/manual-action dimensions are separate;
- retry/idempotency and uncertainty are explicit;
- Events/telemetry/Receipts/proof/Review/external results are separated;
- state machines and machine-readable schemas exist;
- superseded candidate history is visible;
- reconciliation/offline behavior is explicit;
- positive/negative fixtures and one large safety net are committed;
- no implementation/dependency choice was made.

It is not implementation-frozen until WP13/WP14 execute the conformance suite and frozen corpus.

---

# 17. Handoff to 0B-WP03

WP03 must define:

- Object and Object Revision;
- Detector Observation/Claim;
- Relationship and relationship revision;
- View, Preview, Derivative and child Objects;
- Artifact and Artifact Release role;
- content hashes and immutable byte identity;
- storage Location and replica;
- Object/Artifact production links to Activity/Operation/Attempt/Receipt;
- progressive decomposition run/result;
- tombstone/deletion/retention behavior;
- migration/compatibility and proof fixtures.

Every WP03 record must use the common envelope and Activity/Receipt correlation contracts.

No runtime implementation is authorized by completion of WP02.
