# Phase 0B WP02 — Activity, Event, Receipt and Proof Safety Net

**Suite ID:** `ptah.conformance.activity.0.1.0`  
**Status:** CANDIDATE TEST SPECIFICATION  
**Date:** 2026-07-18  
**Runtime harness:** NOT IMPLEMENTED

## Purpose

Define one large safety-net suite for Activity Requests, Activities, Operations, Attempts, dependencies, cancellation/manual action, Events, Receipts, Reviews, Verdicts, authoritative external results and reconciliation.

The suite verifies both JSON structure and the semantic rules that JSON Schema cannot prove.

---

# A. Activity Request and Activity identity

| ID | Case | Expected |
|---|---|---|
| A01 | Submit valid `core.activity_request` in `submitted` state | PASS |
| A02 | Accept request and create separate `core.activity` in `queued` | PASS; explicit link retained |
| A03 | Change entity kind of Activity Request into Activity in place | FAIL identity/history rule |
| A04 | Request marked `accepted` without Activity reference/outcome | FAIL validation |
| A05 | Duplicate submission with same idempotent submission key | One accepted Request/Activity policy result; duplicates linked/rejected, not duplicate work |
| A06 | Expired request accepted after expiry | FAIL stale/expired authorization |
| A07 | Rejected request creates an Activity anyway | FAIL |
| A08 | Activity has no originating request where policy requires one | FAIL conformance |

# B. Activity lifecycle dimensions

| ID | Case | Expected |
|---|---|---|
| B01 | `null -> queued` under `activity.lifecycle 0.1.0` | PASS with acceptance evidence |
| B02 | `queued -> completed` directly | FAIL invalid transition |
| B03 | Activity is `running`, client attachment is `detached` | PASS; Activity continues |
| B04 | Activity is `running`, cancellation is `requested` | PASS; separate dimensions |
| B05 | Activity is `running`, projection health is `stale` | PASS; durable lifecycle not overwritten |
| B06 | Activity `waiting` without structured wait reason | FAIL validation |
| B07 | Activity not `waiting` but carries current wait reason | FAIL structural/semantic rule |
| B08 | Activity `completed` automatically marks output verified | FAIL proof-dimension separation |
| B09 | Activity `completed` automatically marks caller accepted | FAIL authority separation |
| B10 | Provider health degrades while Activity continues | PASS; Provider and Activity state machines separate |
| B11 | Terminal Activity returns to `running` in place | FAIL; create linked follow-up/retry/resume Activity if policy permits |
| B12 | Recovery resets transition sequence/history | FAIL; append `recovering` transitions |

# C. Dependencies

| ID | Case | Expected |
|---|---|---|
| C01 | Dependent waits for exact dependency completion condition | PASS |
| C02 | Dependency Event received but durable condition is not satisfied | Remain waiting; Event is notification only |
| C03 | Required result/proof missing even though dependency Activity completed | Remain waiting or follow failure policy |
| C04 | Dependency failed with `continue_with_warning` | Dependent may proceed with retained warning/evidence |
| C05 | Dependency failed with `fail_dependent` | Dependent transitions under policy with evidence |
| C06 | Dependency cycle introduced | FAIL cycle validation unless future explicit coordination contract permits |
| C07 | Dependency edge removed without history/tombstone | FAIL relationship lifecycle |

# D. Operation identity, retry and idempotency

| ID | Case | Expected |
|---|---|---|
| D01 | One logical Operation creates first Attempt | PASS |
| D02 | Retry creates new Attempt ID/number/nonce while Operation ID stays stable | PASS |
| D03 | Retry changes explicit idempotency key for same logical effect | FAIL |
| D04 | `retry_safe` observation retries after transport failure | PASS under policy |
| D05 | `retry_requires_idempotency_receipt` retries without required Receipt | FAIL/block |
| D06 | `non_retryable` Operation retried automatically | FAIL |
| D07 | `manual_resume_only` retried without manual authority | FAIL |
| D08 | `compensating_action_required` lacks compensating Operation | FAIL validation |
| D09 | Non-idempotent mutation times out with uncertain effect | Operation enters `uncertain`; no automatic retry |
| D10 | Read-back proves prior uncertain mutation did not occur | New Attempt may be authorized under retry policy |
| D11 | Read-back proves prior mutation occurred | Operation reconciles toward success; duplicate retry blocked |
| D12 | Physical Attempt completes but desired output/read-back is absent | Attempt may be completed; Operation cannot be succeeded |

# E. Attempt generation and correlation

| ID | Case | Expected |
|---|---|---|
| E01 | Attempt uses current Node/Provider/workload generations and epoch | PASS |
| E02 | Receipt has wrong Activity ID | Reject current-state effect; retain evidence disposition |
| E03 | Receipt has correct Activity but wrong Operation | Reject current-state effect |
| E04 | Receipt has correct Operation but wrong Attempt | Reject current-state effect |
| E05 | Receipt has wrong nonce | Reject current-state effect |
| E06 | Receipt has stale Provider/workload generation | Retain as historical/stale; cannot update current projection |
| E07 | Receipt has stale connection epoch | Retain as stale-epoch evidence |
| E08 | Duplicate identical Receipt | Projection deduplicates; original evidence remains auditable |
| E09 | Late valid current-generation Receipt after reconnect | Eligible for reconciliation |
| E10 | Attempt number reused inside one Operation | FAIL |
| E11 | Attempt marked superseded without replacement reference | FAIL validation |
| E12 | Timed-out/abandoned Attempt lacks uncertainty reason | FAIL validation |

# F. Cancellation races

| ID | Case | Expected |
|---|---|---|
| F01 | Cancellation requested while Activity running | Cancellation Request created; Activity state unchanged until accepted transition |
| F02 | Producer acknowledges cancellation | Request becomes acknowledged; Activity may still be running/recovering |
| F03 | Activity completes before cancellation takes effect | Record completion race; cancellation rejected/completed according to policy without rewriting evidence |
| F04 | Cancellation reaches required cleanup boundary | Request completed; Activity may transition to cancelled |
| F05 | Cancellation claims completed but required cleanup evidence absent | FAIL/block terminal transition |
| F06 | Cancellation deadline expires while physical effect uncertain | Request expired; Activity/Operation may enter recovering/uncertain |
| F07 | `current_attempt_only` cancellation terminates entire Activity silently | FAIL scope violation |

# G. Manual action

| ID | Case | Expected |
|---|---|---|
| G01 | Activity waits on a durable Manual Action Request | PASS |
| G02 | Event asks a human to act but no durable request exists | Notification only; cannot satisfy wait condition |
| G03 | Unauthorized responder submits response | Reject/retain attempt; request remains open or reviewed |
| G04 | Response fails declared schema | Reject structural validation |
| G05 | Response accepted after request expired | FAIL stale response |
| G06 | Manual response accepted but Activity auto-completes without required Operation proof | FAIL |
| G07 | Parent Operation no longer needs action | Request may be cancelled with reason/evidence |

# H. Events and payloads

| ID | Case | Expected |
|---|---|---|
| H01 | Registered inline-small Event payload under size/privacy policy | PASS |
| H02 | Unregistered payload type in strict mode | FAIL invalid contract |
| H03 | Large PTY/display/file bytes embedded in Event | FAIL; use stream/Object/Artifact reference |
| H04 | `proof_notification` lacks Receipt reference | FAIL validation |
| H05 | Event delivered twice | Consumer handles idempotently |
| H06 | Events arrive out of order within scope | Reorder/reconcile by sequence policy; do not invent state |
| H07 | Sequence gap detected | Mark projection stale/reconcile from ledger/snapshot |
| H08 | Event delivery acknowledgement promoted to operation completion | FAIL |
| H09 | Trace ID used as canonical Activity ID | FAIL identity rule |
| H10 | Public-safe Event exposes restricted alias/credential | FAIL privacy leakage test |

# I. Receipts and proof levels

| ID | Case | Expected |
|---|---|---|
| I01 | Receipt matches Activity/Operation/Attempt/nonce/generations/epoch | Structurally eligible; authority/proof checks still required |
| I02 | Unauthenticated producer issues high-authority Receipt | Reject authority; retain evidence |
| I03 | Facility Runtime claims authoritative external result without authority | Retain lower claim; do not promote |
| I04 | `operation_completed` Receipt implies output hash verified | FAIL implication rule |
| I05 | Output hash Receipt references exact Object/Artifact/hash | PASS for output domain only |
| I06 | Correction Receipt replaces old bytes in place | FAIL; original plus correction relationship required |
| I07 | Correction Receipt references prior Receipt and new proof claims | PASS |
| I08 | Receipt contains large logs/file bytes inline | FAIL; reference Object/Artifact/stream |
| I09 | Idempotency key authenticates producer | FAIL; producer identity evidence separate |
| I10 | Negative/partial/inconclusive Receipt discarded | FAIL; retain as evidence |
| I11 | Receipt timestamps conflict materially | Mark limitation/reconciliation issue, do not silently reorder truth |
| I12 | Proof level used in wrong proof domain | FAIL semantic conformance |

# J. Reviews, Verdicts and acceptance

| ID | Case | Expected |
|---|---|---|
| J01 | Review names exact subjects/hashes/protocol/evidence | PASS |
| J02 | Review succeeds and creates separate Verdict | PASS |
| J03 | Review outcome itself treated as Verdict | FAIL separation |
| J04 | PASS Verdict issued with unavailable required checks | FAIL or conditional/inconclusive under protocol |
| J05 | Conditional Verdict lacks conditions | FAIL validation |
| J06 | Verdict automatically changes Activity/Object/Artifact | FAIL; separately authorized transition required |
| J07 | Reviewer Verdict treated as caller acceptance | FAIL authority separation |
| J08 | New Verdict supersedes old while preserving history | PASS |
| J09 | Review applies to different source checkpoint than claimed | FAIL exact-subject validation |

# K. Authoritative external results

| ID | Case | Expected |
|---|---|---|
| K01 | External result includes source identity, source alias, authority evidence and read-back/integrity evidence | PASS |
| K02 | Ptah fabricates authoritative result from generic Receipt | FAIL |
| K03 | Result is stale/expired | Retain and label; do not use as current without policy |
| K04 | Late current authoritative result resolves waiting Activity | Reconciliation may accept transition |
| K05 | External source changes result | New result supersedes old; history preserved |
| K06 | Result payload schema/version unknown | Preserve read-only or reject interpretation under policy |

# L. Reconciliation and offline journal

| ID | Case | Expected |
|---|---|---|
| L01 | Control plane restarts with durable ledger and Node journal | Reconstruct Activity/Operation/Attempt state |
| L02 | Event stream lost but Receipts/ledger remain | Durable truth survives; projection reconciles |
| L03 | Telemetry export lost | Proof-critical Receipts remain |
| L04 | Node reconnects with new epoch | Negotiate epoch; disposition stale old-epoch evidence |
| L05 | Node journal replays duplicate command/Receipt | Deduplicate/disposition without duplicate effect |
| L06 | Conflicting current-generation Receipts | Preserve conflict; Activity enters recovering/Operation uncertain as needed |
| L07 | Reconciliation silently discards rejected evidence | FAIL; disposition required |
| L08 | Reconciliation accepts transition without transition record | FAIL |
| L09 | Content transfer coupled to Event replay and blocks control reconciliation | FAIL architecture; content moves separately |
| L10 | Provider unavailable but external physical work may continue | Explicit stale/recovering state; do not falsely fail/complete |

# M. Failure isolation and concurrency

| ID | Case | Expected |
|---|---|---|
| M01 | Ten unrelated Activities are queued/running/waiting independently | PASS |
| M02 | One Attempt fails | Parent Operation/Activity follows policy; unrelated Activities unaffected |
| M03 | Optional telemetry Provider fails | Work continues; observability degradation visible |
| M04 | Event transport fails temporarily | Durable Activity truth remains; live projection degrades |
| M05 | Durable ledger/orchestrator unavailable | New transitions blocked or journaled under explicit mode; no fake progress |
| M06 | Heavy stream saturates control Event path | FAIL isolation/backpressure requirement |
| M07 | One Workspace/Activity cancellation globally stops others | FAIL scope isolation |

# N. Privacy and retention

| ID | Case | Expected |
|---|---|---|
| N01 | Receipt/Event references restricted evidence without exposing payload | PASS |
| N02 | Raw credentials appear in Activity parameters, Event, Receipt or telemetry | FAIL secret-leak test |
| N03 | Public Event carries private provider/device identifiers | FAIL/redact/remap |
| N04 | Proof-critical Receipt assigned ephemeral retention | FAIL retention policy |
| N05 | Corrected/superseded Receipt physically deleted despite historical policy | FAIL |
| N06 | Manual Action Request exposes sensitive instruction/response to unauthorized audience | FAIL |

---

# Execution profile

The future executable suite should:

1. load common and Activity schema catalogs locally;
2. validate positive and negative JSON fixtures;
3. validate state-machine definitions and transition graphs;
4. run Activity/Operation/Attempt projection reconstruction;
5. inject duplicate, stale, late, wrong-nonce and conflicting Events/Receipts;
6. simulate retry/idempotency and non-idempotent uncertainty;
7. simulate cancellation completion races;
8. simulate Event/telemetry loss and Node reconnect;
9. verify Review/Verdict/external-result authority separation;
10. run privacy/redaction/retention leakage checks;
11. produce one hashed conformance report Artifact retaining every failed assertion.

## Candidate completion gate

WP02 can be used by downstream Phase 0B schemas when:

- candidate schemas and state machines are internally reviewed;
- superseded candidate schemas are recorded rather than hidden;
- structural/semantic gaps are explicit;
- positive/negative fixtures exist;
- no runtime backend is selected.

WP02 cannot be implementation-frozen until the executable harness proves the suite in WP13/WP14.
