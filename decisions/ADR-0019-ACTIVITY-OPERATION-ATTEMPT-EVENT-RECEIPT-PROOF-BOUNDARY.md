# ADR-0019 — Activity, Operation, Attempt, Event, Receipt and Proof Boundary

**Status:** ACCEPTED FOR PHASE 0B CANDIDATE CONTRACT USE  
**Date:** 2026-07-18  
**Contract candidate:** `ptah.activity` `0.1.0` with corrected request schemas `0.1.1`  
**Implementation authorization:** NONE

## Context

Phase 0A accepted that durable work, live Events, telemetry and proof have different guarantees. It also identified a stable correlation chain:

```text
Activity -> Operation -> Attempt -> Receipt
```

However, Phase 0A used several overlapping state labels—`requested`, `leasing`, `cancelling`, `retrying`, `detached`, `unknown`—and retained an ordered proof vocabulary that could be misread as one automatic ladder.

Phase 0B needs exact contracts that support:

- many concurrent Activities;
- logical Operations and physical retries;
- idempotency and non-idempotent uncertainty;
- dependencies, pause, cancellation and manual action;
- Event duplication/loss/out-of-order delivery;
- sampled telemetry;
- immutable Receipts;
- independent Reviews and Verdicts;
- external authoritative results;
- Node disconnect/reconnect and reconciliation.

## Decision

### 1. Activity Request and Activity are separate

A caller first creates `core.activity_request`.

Acceptance creates a new durable `core.activity` in `queued` state and links the two. Rejected, expired or withdrawn Requests create no Activity.

Request identity never changes kind in place.

### 2. Activity lifecycle is narrow and versioned

`activity.lifecycle` `0.1.0` states:

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

`completed`, `failed` and `cancelled` are terminal for that Activity entity.

Phase 0A labels are moved:

- `requested` → Activity Request lifecycle;
- `leasing` → placement/reservation/Lease plus Activity `preparing`;
- `cancelling` → Cancellation Request lifecycle;
- `retrying` → Operation policy and new Attempts;
- `detached` → observer/client attachment state;
- `unknown` → projection-health state.

This allows concurrent facts without one ambiguous `status` field.

### 3. Activity auxiliary dimensions remain separate

Activity cancellation state, client attachment, projection health and wait reason are separate from lifecycle.

Provider health and connection state remain Provider/connection state machines.

An Activity may therefore remain `running` while a client is detached, cancellation is requested, a Provider is degraded or the UI projection is stale.

### 4. Dependencies are first-class

`core.activity_dependency` records exact dependent/dependency Activities, condition, failure policy, required result/proof and evidence of satisfaction/manual release.

An Event never satisfies a dependency by delivery alone. Current durable condition is read/reconciled.

### 5. Operation owns the logical effect

`core.operation` is one logical observation or side effect.

It owns:

- target/action;
- authority and preconditions;
- side-effect class;
- retry class;
- idempotency class/key;
- desired proof;
- Attempt history;
- uncertain/success/failure interpretation.

Operation identity persists across retries.

### 6. Attempt owns one physical try

`core.attempt` records one physical execution with:

- new Attempt ID, number and nonce;
- exact Node/Provider/workload generations;
- exact connection epoch;
- producer identity/version;
- backend Aliases;
- lifecycle, outcome and Receipts.

Every retry creates a new Attempt. Attempt completion does not automatically mean Operation success.

### 7. Retry and uncertainty are explicit

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

A non-idempotent physical/external effect with uncertain outcome cannot be retried automatically. Read-back, authoritative result or manual decision must resolve it.

### 8. Cancellation is a separate request lifecycle

`core.cancellation_request` has its own versioned lifecycle:

```text
requested
acknowledged
completing
completed
rejected
expired
```

It records exact subject/scope, authority, cleanup class, deadlines and evidence.

Activity reaches `cancelled` only after the declared cancellation/cleanup boundary is proven.

Completion races remain visible rather than rewriting history.

### 9. Manual action is durable

`core.manual_action_request` records exact Activity/Operation, action kind, authorized responders, instruction/context, response schema, expiry, response and outcome.

A notification Event alone cannot satisfy a manual-action wait.

### 10. Events are notifications, not proof

`event.event` uses a typed envelope with domain/type/version, source/subject correlations, generations/epoch, scoped sequence, retention/privacy and payload class.

Event classes:

```text
ephemeral
replayable
ledger_derived
proof_notification
```

A proof notification points to a Receipt. Large or continuous bytes use streams/Objects/Artifacts.

Duplicate, redelivered, out-of-order and missing Events are expected and reconciled.

### 11. Telemetry remains operational observation

Logs, metrics and traces may be sampled, aggregated, transformed or lost.

Telemetry does not own Activity state, Event delivery, Object/Artifact identity, side-effect proof or authoritative external truth.

Trace IDs are correlation metadata, not Ptah identity.

### 12. Proof is bounded by domain

Initial proof domains:

```text
request_dispatch
runtime
output
external_result
review
```

Initial levels retain the Phase 0A vocabulary but no cross-domain implication is automatic.

Examples:

- operation completed does not imply output created;
- output created does not imply read-back;
- read-back does not imply hash verification;
- external result recorded does not imply authoritative external result;
- independently reviewed does not imply PASS or acceptance.

### 13. Receipt is append-only producer evidence

`proof.receipt` binds exact Activity/Operation/Attempt, idempotency key, nonce, generations, epoch, producer identity/version/authority, proof claims, inputs/outputs/hashes, signatures/attestations, privacy and limitations.

Corrections and supersession create new Receipts and preserve the original.

A Receipt may support, contradict or limit a Claim. It does not mutate state automatically.

### 14. Review and Verdict are separate

`proof.review` is the evaluation process over exact subjects/checkpoint/evidence/protocol.

`proof.verdict` is the separate immutable conclusion:

```text
pass
fail
conditional
inconclusive
unsupported
```

Verdict does not automatically mutate the subject and is not caller acceptance.

### 15. Authoritative external results remain source-owned truth

`proof.external_result` records result/source identity, source alias, authority evidence, exact result schema, time/freshness and integrity/read-back.

Ptah may retrieve, preserve and verify it. Ptah cannot fabricate it from weaker evidence.

### 16. Reconciliation is explicit

`core.reconciliation_run` compares ledger state, current generations/epoch, Node journal, Events, Receipts, Objects/Artifacts and external results.

Every evidence item receives an explicit disposition. Accepted/rejected transitions are retained.

Stale generation/epoch evidence may remain historical but cannot update current projections. Late valid current-generation evidence remains eligible.

### 17. Corrected request schemas preserve candidate history

Initial `0.1.0` Activity Request, Cancellation Request and Manual Action Request schemas used bare state fields.

They remain visible as superseded candidate history. Corrected `0.1.1` schemas use versioned state projections and the catalog records the replacement.

## Consequences

### Positive

- durable work is backend-neutral;
- retries cannot silently duplicate a logical effect;
- cancellation races and uncertain effects are representable;
- Event/telemetry loss cannot erase proof-critical truth;
- stale and late evidence can be reconciled safely;
- proof wording cannot climb an implied ladder;
- Review, external authority and acceptance remain distinct;
- intermittent Nodes can journal and reconnect under the same identities.

### Costs

- more entities and state dimensions;
- explicit correlation/generation/epoch checks;
- append-only Receipt and transition history;
- semantic conformance beyond JSON Schema;
- more careful retry/cancellation/reconciliation implementation later.

## Rejected alternatives

### One Activity `status` containing requested/leasing/retrying/cancelling/detached/unknown

Rejected. These describe different entities or dimensions and can coexist.

### Queue job/process/container ID as Activity identity

Rejected. Backend IDs remain Aliases.

### Every retry is a new Activity

Rejected for non-terminal logical retries. Operation identity persists and Attempts change. Terminal follow-up/retry after Activity closure creates a new linked Activity.

### Event delivery as proof of execution

Rejected. Events notify; Receipts/read-back prove bounded facts.

### Telemetry as durable proof

Rejected. It may be sampled/lost/transformed.

### One numeric proof ladder

Rejected. Proof is partially ordered and domain-specific.

### Attempt completion equals Operation success

Rejected. Required output/read-back/authority proof may be absent.

### Reviewer PASS equals caller acceptance

Rejected. Authority differs.

### Overwrite incorrect Receipt

Rejected. Correction/supersession preserves history.

### Retry uncertain non-idempotent work automatically

Rejected. It risks duplicate external/physical effects.

## Candidate artifacts

- `contracts/PHASE-0B-WP02-ACTIVITY-EVENT-PROOF-CONVENTIONS.md`
- `contracts/PHASE-0B-WP02-ENTITY-KIND-SUPPLEMENT.md`
- `contracts/PHASE-0B-WP02-PROOF-LEVEL-REGISTRY.md`
- `schemas/phase-0b/activity/schema-catalog.v0.1.1.json`
- `state-machines/phase-0b/`
- `conformance/PHASE-0B-WP02-ACTIVITY-EVENT-RECEIPT-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp02/activity-event-receipt-cases.v0.1.0.json`
- `work-packages/PHASE-0B-WP02-ACTIVITY-EVENT-RECEIPT-PROOF.md`

## Status and next work

WP02 is accepted as a Phase 0B candidate contract set for downstream schemas.

It is not implementation-frozen until WP13/WP14 execute the conformance harness and golden/negative corpus.

Next active work package:

- 0B-WP03 — Object, Revision, View, Artifact and storage relationships.

No runtime implementation or dependency selection is authorized by this ADR.
