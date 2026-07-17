# ADR-0004 — Operation Identity, Receipts and Proof Levels

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Phase:** 0A internal core-runtime recovery

## Context

Internal implementations expose a repeated failure mode that Ptah must prevent:

- a command being accepted is called success;
- an application or process being launched is treated as completion;
- a message being delivered is treated as the external action being fulfilled;
- a log line from an earlier operation is accepted as current evidence;
- a review result is accepted without proving which checkpoint it reviewed;
- telemetry is mistaken for durable proof;
- a workflow status is accepted without verifying produced Objects or physical state.

Hunter AgentOps, CodeOps, Foreman, Sergeant, MIBU and Hunter Events each solve parts of this problem. Ptah needs one neutral contract joining their strongest patterns.

## Decision

Ptah will distinguish:

1. **Activity State** — caller-visible state of work.
2. **Operation Identity** — stable identity for one side-effecting or observable attempt.
3. **Event** — live or replayable notification about state/change.
4. **Telemetry** — operational traces, metrics and logs.
5. **Receipt** — durable evidence that a specific producer observed or performed a specific step.
6. **Artifact/Object Proof** — content-addressed output or captured state.
7. **Review/Verdict** — an external evaluator's conclusion about an exact checkpoint.
8. **Authoritative External Result** — truth owned by an external system or physical device that Ptah must not invent.

No one category substitutes automatically for another.

---

# Operation identity

Every side-effecting or asynchronous action requires:

```text
activity_id
operation_id
idempotency_key
attempt_id
correlation_nonce
node_id
connection_epoch
provider_id
facility_id
producer_instance_id
producer_version
requested_at
```

Not every read-only operation needs an idempotency key, but every asynchronous proof must remain correlated to the Activity and operation that requested it.

## Identity rules

- `activity_id` persists across backend retries and provider references.
- `operation_id` identifies one logical side effect or observation request.
- `attempt_id` identifies one physical execution attempt.
- `correlation_nonce` rejects stale or unrelated asynchronous evidence.
- `connection_epoch` rejects output from an earlier Node connection/session.
- `producer_instance_id` and `producer_version` identify who emitted the receipt.
- Idempotency and correlation do not authenticate the producer; signed/attested identity is separate.

---

# Proof levels

Ptah will define a versioned proof-level taxonomy. Initial levels:

```text
requested
accepted
routed
dispatched
process_started
interface_launched
runtime_ready
operation_armed
progress_observed
operation_completed
output_created
output_read_back
output_hash_verified
external_result_recorded
independently_reviewed
authoritative_external_result
```

A higher level is not inferred merely because a lower level occurred.

Examples:

- `interface_launched` does not imply `operation_armed`.
- `process_started` does not imply `operation_completed`.
- `operation_completed` does not imply `output_hash_verified`.
- `message delivered` does not imply the recipient completed the requested work.
- `timing window reached` does not imply an external vendor approved an action.
- `review PASS` applies only to the exact checkpoint/object hashes supplied to the reviewer.

## Proof authority

Every receipt declares an authority class:

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

Ptah may preserve and display an authoritative external result but must not fabricate one from weaker evidence.

---

# Receipt schema direction

Phase 0B must define a versioned receipt containing at minimum:

```text
receipt_id
receipt_version
receipt_type
proof_level
authority_class
activity_id
operation_id
attempt_id
idempotency_key
correlation_nonce
node_id
connection_epoch
provider_id
facility_id
producer_instance_id
producer_version
occurred_at
observed_at
status
summary
input_object_ids
output_object_ids
artifact_ids
checkpoint_id
content_hashes
command_or_action_reference
result_reference
trace_id
event_id
previous_receipt_id
signature_or_attestation_reference
redaction_class
limitations
```

Large payloads, raw logs, screenshots, recordings and files remain separate Objects/Artifacts referenced by the receipt.

## Immutability

Receipts are append-only. Corrections create a new receipt linked to the superseded receipt; they do not silently rewrite history.

---

# Review and verdict boundary

A review or verification result must identify:

- exact Activity and operation;
- exact checkpoint/commit/object hashes;
- reviewer/Facility identity and version;
- evidence inputs considered;
- verdict;
- limitations and unavailable checks;
- whether physical/runtime proof was included.

`UNKNOWN`, malformed, stale, uncorrelated or unsupported review output never becomes PASS.

A review verdict does not mutate the underlying Activity or Artifact automatically. A caller/operation chain decides the next transition.

---

# Device and asynchronous proof

For device, firmware, application and remote-node work:

- operation ID, nonce and connection epoch must all match;
- producer identity/version must be compatible;
- stale or duplicate receipts are retained/rejected explicitly;
- launch/transport proof and runtime completion remain distinct;
- late authoritative results can reconcile a waiting/recovering Activity;
- multiple-device ambiguity must be surfaced unless the caller selected a target;
- automatic retries are disabled for non-idempotent physical operations unless a safe receipt/read-back proves the previous attempt did not take effect.

---

# Mutation and rollback proof

A file/Object mutation should produce:

- pre-mutation Object/version/hash;
- proposed edit/patch Artifact;
- dry-run receipt;
- caller authorization reference when required by the caller;
- applied-operation receipt;
- post-mutation Object/version/hash;
- rollback/snapshot reference;
- partial-application state when the complete plan did not finish.

A backup directory path alone is not sufficient durable rollback evidence.

---

# Delivery and outbox proof

Outbox processing distinguishes:

```text
recorded
claimed
attempted
provider_accepted
provider_rejected
retry_scheduled
dead
partially_delivered
delivered
```

Even `delivered` proves transport/provider acknowledgement only. It does not prove the recipient performed the requested external work.

Every attempt remains separately addressable and linked to the original idempotent delivery intent.

---

# Telemetry boundary

Telemetry can link to receipts through Activity/operation/trace IDs, but:

- sampled telemetry cannot replace proof-critical receipts;
- log text alone is not authenticated proof;
- sensitive values must not enter telemetry or status receipts;
- proof receipts remain durable when Collector/exporter systems are unavailable.

---

# Internal evidence supporting this decision

- Hunter AgentOps: operation ID, separate result/evidence and approval ownership.
- Hunter CodeOps: route/execution/evidence/review separation, dry-run/apply and backups.
- Foreman: versioned bridge events and honest connection states.
- Sergeant: grounded evidence, versioned missions/tool manifests and exact checkpoint review.
- MIBU: nonces, stale-log rejection, protocol/app versions, proof levels and authoritative-result preservation.
- Hunter Events V3: unique idempotency key, transactional outbox, attempt history, stale-lock recovery and partial/dead delivery states.
- Hunter Workflow Manager: checkpoint, retry-of and resume-of relationships.

---

# Consequences

## Positive

- Ptah avoids false-success claims.
- Retries can be made safe by evidence rather than guesswork.
- Physical, remote and asynchronous operations can reconcile after reconnect.
- Reviews and proof remain bound to exact outputs.
- Activity state, telemetry and evidence can evolve independently.
- External authority is preserved honestly.

## Costs

- More IDs and retained records are required.
- Facilities must emit typed receipts rather than only stdout text.
- Legacy tools need adapters that translate logs/output into bounded proof levels.
- Signatures/attestation and receipt storage add implementation work.
- Callers must decide what proof level is sufficient for their workflow.

## Do-not-break rule

> Never promote command acceptance, process launch, message delivery, log presence, workflow completion or review output into stronger proof without a correlated receipt from the appropriate authority and the exact Object/checkpoint identity.

---

# Required proof before freeze

1. Reject a stale receipt with the wrong operation ID, nonce or connection epoch.
2. Reject a correctly correlated receipt from an unauthenticated/incompatible producer.
3. Preserve a late valid completion receipt after Node reconnect.
4. Demonstrate launch, runtime-ready, complete and read-back-verified as separate states.
5. Retry an idempotent operation without duplicating the side effect.
6. Refuse automatic retry of a non-idempotent device operation without proof of non-application.
7. Bind a review verdict to exact content hashes and reject a verdict for an older checkpoint.
8. Retain all outbox attempts and distinguish delivery from external fulfillment.
9. Sample ordinary telemetry while preserving every proof-critical receipt.
10. Apply a multi-file mutation with dry-run, before/after hashes and rollback; expose partial application honestly on failure.
