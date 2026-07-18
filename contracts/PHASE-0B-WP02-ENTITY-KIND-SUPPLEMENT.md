# Ptah Phase 0B WP02 — Activity and Proof Entity-Kind Supplement

**Parent registry:** `ptah.entity-kind` `0.1.0`  
**Status:** CANDIDATE  
**Date:** 2026-07-18

## Purpose

Add the entity vocabulary needed by the Activity/Event/Receipt/proof contract set without repurposing existing Phase 0B common tokens.

## New entity kinds

| Token | Meaning |
|---|---|
| `core.activity_request` | Pre-ledger caller submission that may be accepted into a durable Activity or rejected |
| `core.activity_dependency` | First-class dependency edge between Activities |
| `core.cancellation_request` | Scoped request to cancel an Activity or Operation |
| `core.manual_action_request` | Durable request for human/manual input required by an Activity |
| `core.reconciliation_run` | One durable reconciliation execution over ledger/provider/event/receipt state |
| `event.payload_type` | Versioned registration of one Event payload type/schema |
| `event.delivery_attempt` | One transport/delivery attempt for a replayable notification |
| `proof.proof_level_definition` | Versioned bounded proof-domain/level definition |
| `proof.proof_claim` | One Receipt-level bounded proof assertion over exact subjects |
| `proof.receipt_correction` | Explicit correction/supersession relationship between Receipts |

## Existing kinds reused

The following existing registry tokens remain canonical:

- `core.activity`
- `core.operation`
- `core.attempt`
- `event.event`
- `proof.receipt`
- `proof.review`
- `proof.verdict`
- `proof.external_result`
- `proof.evidence`
- `runtime.process`
- `runtime.provider`
- `runtime.session`

## Classification rules

1. `core.activity_request` exists before `core.activity`. Acceptance creates and links a new Activity; the request never becomes the Activity by changing kind.
2. `core.activity_dependency` is a relationship entity with dependency condition and failure policy, not a copied array entry with no identity.
3. `core.cancellation_request` is not an Activity lifecycle state.
4. `core.manual_action_request` is not a generic Event; it is durable required work with authority, expiry, response, and audit.
5. `core.reconciliation_run` does not rewrite stale evidence; it records accepted/rejected reconciliation decisions and resulting transitions.
6. `event.payload_type` registers payload schema and privacy/retention defaults; it never turns arbitrary event payload into trusted executable code.
7. `event.delivery_attempt` proves transport processing only, not recipient fulfillment.
8. `proof.proof_level_definition` defines vocabulary and implication restrictions; it is not itself proof.
9. `proof.proof_claim` is bounded by domain, level, subjects, producer authority, facts, and limitations.
10. `proof.receipt_correction` preserves both original and correcting Receipts.

## Rejected kind aliases

The following are not entity kinds:

- `requested` — Activity Request lifecycle state;
- `leasing` — placement/reservation/Lease behavior;
- `retrying` — Operation retry-controller condition and new Attempts;
- `cancelling` — Cancellation Request state;
- `detached` — client attachment state;
- `unknown` — projection-health state;
- Temporal Workflow ID, NATS subject, JetStream consumer, process ID, container ID, trace ID, scanner run ID, browser target ID — backend Aliases only.

## Conformance requirements

- reject changing `core.activity_request` into `core.activity` in place;
- reject cancellation state written into Activity lifecycle;
- retain dependency edge identity and exact condition/failure policy;
- reject Event payload without registered payload type where strict mode requires registration;
- reject delivery acknowledgement promoted to operation completion;
- reject proof level used outside its declared proof domain;
- preserve original Receipt after correction;
- reconcile stale evidence only through a receipted `core.reconciliation_run`.

Registration remains contract vocabulary and does not authorize runtime implementation.
