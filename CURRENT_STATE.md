# Ptah Current State

**Last updated:** 2026-07-18  
**Overall status:** ACTIVE PLANNING — PHASE 0A FROZEN; PHASE 0B ACTIVE  
**Current phase:** Phase 0B — contracts, migrations, conformance and proof design  
**Active work package:** 0B-WP02 — Activity, Operation, Attempt, Event, Receipt and proof  
**Runtime implementation:** NOT STARTED  
**Dependency selection:** NOT STARTED  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

# Frozen Phase 0A checkpoint

Phase 0A is complete and frozen at:

```text
7d2dffee48f1400ba1cf88823343f09a3895ad33
```

Freeze decision:

- `decisions/ADR-0017-PHASE-0A-FREEZE-PHASE-0B-ENTRY.md`

All current v1 requirements are closed for contract design. No runtime implementation is authorized by that closure.

---

# Accepted Ptah position

Ptah is an independent, open-source, online-first concurrent digital world built around persistent Workspaces, Objects, Activities, Facilities, Nodes, Devices, Applications, Browsers, Sessions, Panels, Knowledge Sources, Datasets, Plugins, security Findings and Artifacts.

Ptah supplies the working world. Humans and compatible systems supply intent, reasoning, policy, restrictions, risk acceptance and acceptance criteria.

The public `Ptah-space` repository remains a no-code implementation shell.

---

# Phase 0B common layer — candidate complete

0B-WP01 produced candidate `ptah.common` `0.1.0` and is approved for downstream Phase 0B schema use.

Accepted decision:

- `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`

Work package:

- `work-packages/PHASE-0B-WP01-COMMON-IDENTITY-VERSIONING-TYPED-FAMILIES.md`

Normative inputs:

- `contracts/PHASE-0B-COMMON-CONTRACT-CONVENTIONS.md`
- `contracts/PHASE-0B-ENTITY-KIND-REGISTRY.md`
- `contracts/PHASE-0B-IDENTITY-KIND-REGISTRY.md`
- `schemas/phase-0b/common/`
- `conformance/PHASE-0B-WP01-COMMON-CONTRACT-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp01/common-contract-cases.v0.1.0.json`

## Common rules now active

1. New canonical entity IDs use lowercase UUIDv7 plus registered `entity_kind`.
2. Backend and legacy identifiers remain scoped Aliases.
3. Candidate schemas use JSON Schema 2020-12, absolute Ptah URNs and a local catalog.
4. Domain entities embed a nested common Entity Envelope.
5. `record_revision`, Object Revision, schema version, Node/Provider/workload generations and connection epoch remain separate.
6. Provider, Session, Lease, Event, Revision, Snapshot, Recipe, Protocol, Evidence and related concepts are typed families.
7. There is no global `status` enum.
8. State machines and transitions are namespaced, versioned and append-only.
9. `completed`, `verified` and `accepted` remain separate dimensions.
10. Authentication, authorization, technical capability and organizational acceptance remain separate.
11. Migration preserves frozen history and reports loss/defaults/coercion.
12. Compatibility is directional and evidence-backed, not inferred from SemVer alone.
13. Tombstone and physical deletion remain separate.
14. Privacy, audience, redaction and retention travel with exportable records.
15. Structural schema validation never replaces semantic conformance.

## WP01 proof status

- normative conventions: complete candidate;
- entity and identity registries: complete candidate;
- eight common machine-readable schemas: complete candidate;
- local schema catalog: complete candidate;
- positive/negative fixtures: committed;
- consolidated safety-net specification: committed;
- executable conformance harness: deferred to 0B-WP13/0B-WP14;
- implementation freeze: not granted.

---

# Active work — 0B-WP02

## Activity, Operation, Attempt, Event, Receipt and proof

WP02 must turn ADR-0003, ADR-0004 and the common candidate layer into machine-readable contracts.

### Required entities

- `core.activity`;
- Activity dependency edge;
- `core.operation`;
- `core.attempt`;
- idempotency and correlation-key records;
- `event.event` and event-domain payload registration;
- `proof.receipt`;
- proof-level definition;
- `proof.review` and `proof.verdict`;
- `proof.external_result`;
- retry, pause, cancellation, recovery and reconnect records.

### Activity contract requirements

```text
activity_id
workspace_ref
caller_or_owner_ref
activity_kind
intent_and_parameters_ref
state_machine_name_and_version
current_state_and_sequence
dependency_edges
priority_and_budgets
created_started_completed timestamps
current_attempt summaries
result_refs
failure_or_wait_reason
privacy_retention_and_extensions
```

Activity is caller-visible durable work. It is not a Temporal workflow ID, queue job, process, container, browser task or scanner run ID.

### Operation contract requirements

```text
operation_id
activity_ref
operation_kind
logical_target_refs
idempotency_class
idempotency_key_or_nonce
preconditions
authority_and_permission refs
side_effect_class
expected_receipt_and_readback
retry_policy
```

Operation is one logical side effect or observation. Retries preserve Operation identity.

### Attempt contract requirements

```text
attempt_id
operation_ref
attempt_number
node_provider_workload_generation refs
connection_epoch
started_completed timestamps
physical backend aliases
outcome
receipt_refs
resource_usage
```

Attempt is one physical execution try. Every retry creates a new Attempt.

### Event contract requirements

The Event envelope must include:

```text
event_id
event_domain
event_type
event_version
source_ref
subject_ref
activity_operation_attempt refs
provider_workload generations
connection_epoch
occurred_at
observed_at
sequence_or_cursor
payload_schema_id_and_ref
privacy_and_retention
```

Event is notification/history input. It is not automatically a Receipt or authoritative state.

### Receipt contract requirements

Receipt must bind:

```text
receipt_id
producer_and_authority class
activity_operation_attempt
nonce_or_idempotency key
node_provider_workload generations
connection_epoch
subject_and_result refs
proof_level
observed facts
limitations
signature_or_integrity refs
occurred_at
received_at
```

Receipts are append-only evidence. A Receipt cannot silently mutate Activity state without accepted transition/reconciliation rules.

### Initial Activity lifecycle

Candidate states remain:

```text
queued
preparing
running
waiting
paused
resuming
completed
failed
cancelled
detached
recovering
```

WP02 must specify exact allowed transitions, authorities, preconditions, retry/recovery semantics and proof requirements.

### Required failure and recovery distinctions

- provider unavailable;
- waiting for dependency;
- waiting for human/manual action;
- retryable attempt failure;
- non-idempotent retry blocked;
- cancellation requested versus acknowledged versus completed;
- disconnected versus detached;
- recovering versus resumed;
- Activity completed versus output verified versus caller accepted;
- late current-generation Receipt versus stale-generation evidence;
- missing Event versus fresh snapshot/reconciliation.

### WP02 safety-net proof

At minimum:

1. ten unrelated Activities run independently;
2. one failed Attempt does not fail unrelated Activities;
3. retry creates a new Attempt without duplicating a non-idempotent side effect;
4. wrong nonce/Operation/Attempt/generation/epoch Receipt is rejected;
5. late valid current-generation completion is reconciled after reconnect;
6. stale generation/epoch output is retained but cannot update current state;
7. Event loss does not erase durable Activity truth;
8. telemetry loss does not erase proof-critical Receipts;
9. cancellation races preserve exact result;
10. completed/verified/accepted remain separate;
11. Review/Verdict remains separate from external authoritative result;
12. crash/restart reconstructs Activity state and attempt history.

---

# Ordered Phase 0B sequence

1. **0B-WP01** — common identity/versioning/typed families. **CANDIDATE COMPLETE**
2. **0B-WP02** — Activity/Operation/Attempt/Event/Receipt/proof. **ACTIVE**
3. **0B-WP03** — Object/Revision/View/Artifact/storage relationships.
4. **0B-WP04** — Node/Facility/Provider/capability/health.
5. **0B-WP05** — Workspace/Session/checkpoint/recovery.
6. **0B-WP06** — transfer/sync/conflict/backup.
7. **0B-WP07** — Recipe/Build/provenance/SBOM/signature/verification.
8. **0B-WP08** — Domain Pack/firmware/disk/Device.
9. **0B-WP09** — Application/Browser/semantic UI/Shell.
10. **0B-WP10** — knowledge/data/Package/Plugin.
11. **0B-WP11** — isolation/placement/reservation/lease/secure grants.
12. **0B-WP12** — security/Finding/Claim/Evidence/reproduction.
13. **0B-WP13** — migrations and executable conformance harness.
14. **0B-WP14** — golden/negative corpus and proof-plan freeze.
15. Phase 0B review/freeze and Phase 0C readiness decision.

---

# Parked and restricted items

The parked/restricted Phase 0A items remain non-blocking and retain their recorded reopening criteria:

- `.P5C`;
- shared cross-Node POSIX filesystems;
- MiniRouter licence;
- Dify modified-licence integration;
- exact GNOME Ponytail dependency selection;
- non-GNOME Wayland input completion;
- unaudited private device-manager source;
- `chrisipanaque` prototype reuse;
- missing `amertoglu16.github.io` source;
- donor source without a clear compatible licence;
- final public Ptah project licence.

Detailed audit:

- `work-packages/PHASE-0A-CROSS-REQUIREMENT-CONSISTENCY-REVIEW.md`
- `DONOR_RECOVERY.md`

---

# No-build boundary

Allowed now:

- contract/schema/state-machine design;
- migration/compatibility design;
- conformance and fixture design;
- proof-plan design;
- public/private schema boundaries;
- Phase 0C dependency/licence inputs.

Not allowed yet:

- runtime or large UI implementation;
- donor-source copying/adaptation;
- production dependency selection/distribution;
- Node/Provider/browser/scanner/scheduler deployment;
- public registry activation;
- presenting candidate contracts as built or proven.

Implementation begins only after Phase 0C approval is recorded in this file.

---

# Chat continuation instruction

Read this file first, followed by:

1. `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`;
2. `work-packages/PHASE-0B-WP01-COMMON-IDENTITY-VERSIONING-TYPED-FAMILIES.md`;
3. `contracts/PHASE-0B-COMMON-CONTRACT-CONVENTIONS.md`;
4. `schemas/phase-0b/common/schema-catalog.v0.1.0.json`;
5. `decisions/ADR-0003-ACTIVITY-EVENT-OBSERVABILITY-BOUNDARY.md`;
6. `decisions/ADR-0004-OPERATION-RECEIPTS-PROOF-LEVELS.md`;
7. `work-packages/PHASE-0B-ENTRY-CONTRACT-PROOF-INPUTS.md`;
8. `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md` and `REQUIREMENT_CLOSURE_MATRIX.md`.

Do not restart donor research or implementation from conversational memory.
