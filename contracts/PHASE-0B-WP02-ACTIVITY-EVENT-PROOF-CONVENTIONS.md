# Ptah Phase 0B WP02 — Activity, Event, Receipt and Proof Conventions

**Contract set:** `ptah.activity` `0.1.0`  
**Status:** CANDIDATE  
**Date:** 2026-07-18  
**Implementation:** NOT STARTED

## Purpose

Define the durable caller-visible work model and its exact relationship to logical Operations, physical Attempts, Events, telemetry, Receipts, output proof, Reviews and authoritative external results.

This contract preserves ADR-0003 and ADR-0004 while applying the typed-family and namespaced-state rules from ADR-0018.

---

# 1. Core separation

```text
Activity
  durable caller-visible unit of work

Operation
  one logical side effect or observation request inside an Activity

Attempt
  one physical execution try of an Operation

Event
  live/replayable notification about something observed or changed

Telemetry
  sampled/aggregated operational logs, metrics and traces

Receipt
  append-only correlated evidence from an identified producer/authority

Object/Artifact proof
  content-addressed output or captured state

Review/Verdict
  evaluator conclusion over exact evidence/checkpoint

Authoritative External Result
  result whose truth belongs to an external system or physical device
```

None substitutes automatically for another.

---

# 2. Activity Request versus Activity

A pre-ledger submission is an `Activity Request`, not an Activity state.

The request contains caller intent, target Workspace, parameters, desired proof, priority and budgets. The control plane validates scope/authorization and either:

- rejects the request with a typed outcome; or
- creates a durable `core.activity` in `queued` state and links it to the request.

Therefore `requested` is not part of `activity.lifecycle`.

The Activity ID exists only after durable ledger acceptance.

---

# 3. Activity lifecycle

## 3.1 Canonical lifecycle states

`activity.lifecycle` candidate `0.1.0`:

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

Meanings:

- `queued`: durable Activity accepted and waiting for dependencies, scheduling or preparation eligibility;
- `preparing`: acquiring placement/leases, materializing inputs, restoring state or preparing Providers;
- `running`: at least one required current Operation is actively executing or the orchestrator is advancing work;
- `waiting`: durable wait for dependency, timer, manual action, capacity, approval, credential, external result, backpressure, retry delay or checkpoint;
- `paused`: pause has been acknowledged and no new work may start except pause/health/control Operations;
- `resuming`: reacquiring/revalidating state after pause;
- `recovering`: reconciling uncertain/stale/disconnected state after failure, restart or lost observation;
- `completed`: Activity's declared completion condition and required Activity-level result references were recorded;
- `failed`: terminal under the current Activity policy;
- `cancelled`: cancellation reached its declared cleanup/termination boundary.

`completed` does not imply output verification, independent review or caller acceptance.

## 3.2 Initial transitions

Candidate transitions:

```text
null -> queued
queued -> preparing | waiting | recovering | failed | cancelled
preparing -> running | waiting | paused | recovering | failed | cancelled
running -> waiting | paused | recovering | completed | failed | cancelled
waiting -> preparing | running | paused | recovering | failed | cancelled
paused -> resuming | cancelled
resuming -> preparing | running | waiting | recovering | failed | cancelled
recovering -> preparing | running | waiting | paused | completed | failed | cancelled
```

`completed`, `failed` and `cancelled` are terminal for this Activity entity. Additional work creates a new Activity linked through `retry_of`, `resume_of`, `follow_up_to` or another explicit relationship when the original policy has already terminated.

## 3.3 Removed/moved Phase 0A labels

The following Phase 0A labels are represented, but not as Activity lifecycle states:

- `requested` → Activity Request state before Activity creation;
- `leasing` → placement/reservation/Lease entities plus Activity `preparing`;
- `cancelling` → separate cancellation dimension/request;
- `retrying` → Operation retry controller plus new Attempts;
- `detached` → observer/attachment state; Activity keeps its real lifecycle state;
- `unknown` → projection-health state when current ledger truth cannot be read; it never overwrites the durable lifecycle state.

This normalization prevents one global `status` field.

---

# 4. Activity auxiliary dimensions

## Cancellation state

```text
none
requested
acknowledged
completing
completed
rejected
expired
```

A Cancellation Request records requestor, authority, requested scope, reason, deadline and desired cleanup class.

Race results remain explicit:

- Activity completed before cancellation took effect;
- cancellation rejected by policy;
- cancellation acknowledged but cleanup incomplete;
- terminal `cancelled` reached;
- cancellation expired/was superseded.

## Attachment state

```text
attached
detached
```

This describes a client/observer relationship only. Detaching never pauses, cancels or hides the actual Activity lifecycle.

## Projection health

```text
current
stale
reconciling
unknown
```

This describes confidence in a projection. The durable ledger state remains unchanged until reconciliation accepts evidence/transitions.

## Wait reason

```text
dependency
timer
human_action
provider_capacity
external_result
credential
approval
backpressure
retry_backoff
checkpoint
other
```

A wait reason is structured detail for `waiting`, not a new lifecycle state.

---

# 5. Activity dependencies

A dependency edge is a first-class relationship containing:

```text
dependent_activity_ref
dependency_activity_ref
dependency_condition
failure_policy
required_result_or_proof
created_by
```

Initial dependency conditions:

```text
activity_completed
activity_terminal
result_available
artifact_available
proof_level_reached
manual_release
```

Initial failure policies:

```text
block
fail_dependent
continue_with_warning
skip_dependent
manual_decision
```

A dependency notification Event is not proof that the condition is satisfied. The current durable dependency subject/result is read/reconciled.

Cycles are rejected unless a future explicit coordination contract permits them.

---

# 6. Operation

An Operation is one logical request to observe or cause an effect.

Minimum fields:

```text
operation_id
activity_ref
operation_kind
logical_target_refs
command_or_action_ref
side_effect_class
retry_class
idempotency_class
idempotency_key
required_authority_refs
precondition_refs
desired_proof_claims
current_state
current_attempt_ref
created_at
```

## Side-effect class

```text
observation_only
reversible
idempotent_mutation
non_idempotent_mutation
destructive
external_authoritative
```

## Retry class

From ADR-0003:

```text
retry_safe
retry_requires_idempotency_receipt
non_retryable
manual_resume_only
compensating_action_required
```

## Idempotency class

```text
none_required
operation_identity
explicit_key
provider_key
receipt_guarded
manual_only
compensating
```

The retry and idempotency classes are related but not interchangeable.

Rules:

1. Operation ID persists across physical retries.
2. Idempotency key remains stable across Attempts of the same logical side effect.
3. Automatic retry is allowed only when retry class, idempotency policy and retained evidence permit it.
4. Non-idempotent physical/external Operations never retry automatically without evidence that the prior Attempt did not take effect or an approved compensating plan.
5. Operation success means its declared required proof claims were satisfied; it does not imply the Activity is accepted/reviewed.

## Operation lifecycle

Candidate `operation.lifecycle` `0.1.0`:

```text
planned
ready
dispatching
executing
waiting
uncertain
succeeded
failed
cancelled
blocked
```

`uncertain` is used when the physical effect may have occurred but current proof is insufficient. It requires reconciliation/read-back/manual review before retry or terminal interpretation.

---

# 7. Attempt

An Attempt is one physical try of an Operation.

Minimum fields:

```text
attempt_id
operation_ref
attempt_number
correlation_nonce
node_ref and node_generation
provider_ref and provider_generation
workload_generation
connection_epoch
producer_instance_ref and version
backend_aliases
started_at
completed_at
outcome
receipt_refs
resource_usage_refs
```

Rules:

- Every retry creates a new Attempt ID and new correlation nonce.
- The Operation's idempotency key remains stable where required.
- Attempt number is monotonic inside the Operation but is not identity.
- A late Receipt must match Operation, Attempt, nonce, generations and connection epoch before it can update current projections.
- Stale/duplicate evidence is retained with explicit disposition.

## Attempt lifecycle

Candidate `attempt.lifecycle` `0.1.0`:

```text
created
dispatched
accepted
executing
waiting
completed
failed
timed_out
cancelled
abandoned
superseded
```

`completed` means the producer declared the physical Attempt complete; Operation success still depends on required proof/read-back.

---

# 8. Event

An Event is a typed notification envelope.

Minimum fields:

```text
event_id
event_domain
event_type
event_version
source_ref
subject_ref
activity_ref
operation_ref
attempt_ref
node/provider/workload generations
connection_epoch
occurred_at
observed_at
sequence_scope_ref
sequence
causation_event_ref
correlation_ref
trace_context
retention_class
payload_schema_id
inline_small_payload or payload_ref or stream_ref
privacy/audience/redaction
```

## Event classes

```text
ephemeral
replayable
ledger_derived
proof_notification
```

`proof_notification` points to a Receipt/Evidence entity. The Event itself is not the proof.

## Payload classes

```text
inline_small
object_reference
artifact_reference
stream_reference
none
```

Large/continuous PTY, Object transfer, display, audio/video and media data remain separate streams/Objects/Artifacts.

## Delivery rules

- consumers handle duplicate/redelivered Events;
- sequence is scoped, not globally total;
- delivery does not prove execution;
- missing Events trigger snapshot/ledger reconciliation rather than invented state;
- backend subjects/consumer offsets remain Aliases/backend references;
- sensitive identities are excluded/redacted for public-safe Events.

---

# 9. Telemetry

Telemetry includes traces, logs, metrics, resource observations and performance data.

Telemetry may be sampled, aggregated, transformed or unavailable.

Telemetry does not own:

- canonical Activity state;
- side-effect proof;
- Object/Artifact identity;
- durable orchestration;
- Event delivery;
- authoritative external truth.

Telemetry correlates through Ptah IDs and optional trace context. Trace IDs never replace Ptah entity IDs.

Sensitive values and raw credentials are prohibited from ordinary telemetry.

---

# 10. Proof claims and levels

The initial proof taxonomy from ADR-0004 is retained as a **partially ordered vocabulary**, not one universal numeric ladder.

## Request/dispatch domain

```text
requested
accepted
routed
dispatched
```

## Runtime domain

```text
process_started
interface_launched
runtime_ready
operation_armed
progress_observed
operation_completed
```

## Output domain

```text
output_created
output_read_back
output_hash_verified
```

## External-result domain

```text
external_result_recorded
authoritative_external_result
```

## Review domain

```text
independently_reviewed
```

A Receipt contains one or more bounded proof claims:

```text
proof_domain
proof_level
subject_refs
claim_summary
observed_facts_or_payload_ref
limitations
```

Rules:

- a level in one domain does not imply another domain;
- later/higher-sounding labels are not inferred automatically;
- `operation_completed` does not imply `output_created` or hash verification;
- `independently_reviewed` applies only to exact evidence/checkpoint supplied;
- `external_result_recorded` is not `authoritative_external_result` unless the producer/source has that authority.

---

# 11. Receipt

A Receipt is append-only durable evidence from an identified producer.

Minimum fields:

```text
receipt_id
receipt_schema_version
receipt_kind
proof_claims
authority_class
activity_ref
operation_ref
attempt_ref
idempotency_key
correlation_nonce
node/provider/workload generations
connection_epoch
facility_ref
producer_instance_ref
producer_version
producer_authentication_or_attestation_refs
occurred_at
observed_at
received_at
receipt_outcome
summary
input_refs
output_refs
artifact_refs
checkpoint_refs
content_hashes
command_or_action_ref
result_ref
trace_context
event_refs
previous_or_superseded_receipt_refs
signature_or_attestation_refs
privacy/audience/redaction
limitations
payload_schema_id and payload/ref
```

## Receipt kinds

```text
request_acknowledgement
routing
work_dispatch
process_observation
runtime_observation
operation_observation
progress_checkpoint
output_observation
readback
hash_verification
external_result
review
correction
```

## Receipt authority classes

```text
caller_claim
ptah_control_plane
ptah_node
workspace_provider
facility_runtime
operating_system
physical_device
external_provider
human_confirmation
independent_reviewer
authoritative_external_system
```

## Receipt outcomes

```text
positive
negative
partial
inconclusive
corrected
superseded
```

Rules:

1. Receipt is immutable after acceptance.
2. Corrections create a new Receipt linked to the old one.
3. Large logs/screenshots/files are referenced as Objects/Artifacts.
4. Idempotency/correlation do not authenticate the producer; authentication/attestation remains separate.
5. A Receipt can support/contradict/limit a Claim but does not automatically transition the Activity.
6. Reconciliation validates authority, subject, nonce, generations, epoch, freshness and required proof.
7. Duplicate identical Receipts may be deduplicated in projection but remain addressable/auditable.

---

# 12. Review and Verdict

A Review is an evaluation process over exact inputs/checkpoint.

Minimum fields:

```text
review_id
review_kind
subject_refs and exact revisions/hashes
activity/operation refs
reviewer principal/facility/provider/version
protocol_ref
input_evidence_refs
checks_performed
checks_unavailable
physical/runtime proof included
started/completed timestamps
review_run_outcome
```

A Verdict is a separate immutable conclusion:

```text
verdict_id
review_ref
subject_refs/hashes
verdict
summary
limitations
evidence_refs
issued_by
issued_at
supersedes_verdict_ref
```

Initial verdicts:

```text
pass
fail
conditional
inconclusive
unsupported
```

Malformed, stale, uncorrelated or unsupported output does not become a PASS Verdict.

A Verdict does not mutate the reviewed Activity/Object/Artifact automatically. A separately authorized transition/Operation decides the next action.

---

# 13. Authoritative External Result

An Authoritative External Result records truth owned by an external system or physical device.

Minimum fields:

```text
external_result_id
source_system_or_device_ref
source_result_alias
source_authority_evidence
activity/operation/attempt refs
subject_refs
result_type and result_schema
result_payload_ref
occurred_at
retrieved_at
freshness/expiry
signature/attestation/readback refs
limitations
```

Ptah may retrieve, preserve, verify and display this result. Ptah must not fabricate it from weaker evidence.

A late valid authoritative result may reconcile an Activity in `waiting` or `recovering` through an accepted transition.

---

# 14. Reconciliation

Reconciliation compares:

- durable Activity/Operation/Attempt records;
- current provider/Node generation and connection epoch;
- local Node journal/outbox;
- replayable Events;
- Receipts;
- current Object/Artifact/external state;
- authoritative external results.

Rules:

1. Event loss does not erase durable state.
2. Telemetry loss does not erase Receipts.
3. stale generations/epochs cannot update current projections.
4. late current-generation evidence remains eligible for reconciliation.
5. conflicting evidence remains visible.
6. uncertain non-idempotent Attempts block automatic retry until read-back/authority resolves them.
7. reconnect negotiates a new epoch and replays only retained classes.
8. Object/Artifact bytes move through separate transfer paths.

---

# 15. Failure semantics

Failure classes remain separate:

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
authorization_failure
proof_failure
reconciliation_conflict
```

A failure record identifies affected scope and whether Activity/Operation/Attempt truth is known, stale or uncertain.

Telemetry or optional live-event failure does not automatically stop physical work. Required ledger/orchestrator/execution failure enters explicit waiting/recovering/failed behavior according to policy.

---

# 16. Offline/intermittent Node journal

A permitted disconnected Node records locally:

```text
Activity/Operation/Attempt IDs
state-transition attempts
Event sequence and connection epoch
idempotency keys and correlation nonces
Receipts and producer identity
produced Object/Artifact references
pending acknowledgements
conflicts and uncertainty
```

On reconnect:

1. Node identity/generation and connection epoch are negotiated;
2. duplicate commands/Events/Receipts are rejected or dispositioned;
3. retained Events are replayed by class;
4. durable state is reconciled;
5. content transfer occurs separately;
6. conflicts are surfaced.

The local journal is Ptah-owned even when NATS/JetStream/Temporal assist transport/orchestration.

---

# 17. Mutation and rollback proof

A mutating Operation should reference:

- pre-mutation Object/revision/hash;
- proposed change/patch Artifact;
- dry-run Receipt when supported;
- required authorization/Approval;
- applied-operation Receipt;
- post-mutation Object/revision/hash;
- rollback/checkpoint reference;
- partial-application evidence.

A backup path string alone is not durable rollback proof.

---

# 18. Candidate schema composition rule

Every WP02 domain record:

- embeds `common.entity-envelope` `0.1.0` under `envelope`;
- uses registered entity/family kinds;
- uses absolute schema URNs and the local catalog;
- declares state-machine name/version where mutable;
- uses typed Entity References;
- records privacy/audience/redaction/retention;
- remains closed except namespaced extensions;
- separates inline small payload from Object/Artifact/stream references;
- adds structural and semantic conformance fixtures.

No runtime backend, message broker, workflow engine, database or telemetry vendor is selected by this contract.
