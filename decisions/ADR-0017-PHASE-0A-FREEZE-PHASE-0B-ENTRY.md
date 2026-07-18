# ADR-0017 — Phase 0A Freeze and Phase 0B Entry

**Status:** ACCEPTED  
**Date:** 2026-07-18  
**Frozen Phase 0A evidence checkpoint:** `7d2dffee48f1400ba1cf88823343f09a3895ad33`  
**Implementation authorization:** NONE

## Context

Phase 0A recovered internal and external foundations, inspected composite donors, closed every current v1 architecture requirement for contract design, resolved research/documentation/profile sources, and completed a cross-requirement consistency review.

The review confirmed:

- no accepted ADR requires reversal;
- no v1 requirement lacks a composite design path;
- no donor-local identity is required as canonical Ptah identity;
- Object, Artifact, Activity, Receipt, Claim, Finding, Evidence, Session, Lease, Provider, Snapshot and Protocol boundaries can be represented coherently;
- one state-machine normalization issue belongs in Phase 0B: lifecycle labels must be namespaced by entity and cannot become one global `status` enum;
- every parked/restricted item has a non-blocking v1 path or an explicit future reopening criterion;
- the public `Ptah-space` repository still contains no implementation and does not conflict with the private roadmap.

Phase 0B inputs have been enumerated in:

- `work-packages/PHASE-0B-ENTRY-CONTRACT-PROOF-INPUTS.md`.

The cross-requirement review is recorded in:

- `work-packages/PHASE-0A-CROSS-REQUIREMENT-CONSISTENCY-REVIEW.md`.

## Decision

### 1. Freeze Phase 0A

Phase 0A architecture and donor closure is frozen at roadmap commit:

```text
7d2dffee48f1400ba1cf88823343f09a3895ad33
```

Later changes to accepted Phase 0A architecture require a new ADR that explains:

- the discovered problem;
- new evidence;
- affected requirements/contracts;
- migration impact;
- donor/internal impact;
- public/private impact;
- whether the change reopens Phase 0A or can be handled inside Phase 0B.

Routine typo, link, source-pin, formatting and status-index corrections do not reopen Phase 0A unless they alter architecture or closure evidence.

### 2. Enter Phase 0B

The active roadmap phase becomes:

> Phase 0B — Contracts, migrations, conformance and proof design.

Authorized Phase 0B work is limited to:

- schemas and typed state machines;
- versioning and migrations;
- event/receipt/proof envelopes;
- Provider/Facility adapter contracts;
- conformance suites;
- lawful golden and negative fixtures;
- proof-plan design;
- public/private schema and documentation boundaries;
- Phase 0C dependency/licence/vertical-slice decision inputs.

### 3. Preserve the no-build boundary

Phase 0B does not authorize:

- runtime implementation;
- large UI implementation;
- copying donor source;
- selecting or distributing dependencies;
- deploying Nodes, schedulers, browsers, scanners or Providers;
- activating a public/plugin registry;
- presenting design closure as built/proven/complete.

Exact implementation begins only after Phase 0C selects and approves the first vertical slice in `CURRENT_STATE.md`.

### 4. Accept the canonical normalization rules

Phase 0B must implement the following cross-requirement rules:

1. **Object owns content identity; Artifact owns durable promoted-result role.**
2. **Activity, Operation and Attempt remain separate.**
3. **Event, telemetry, Receipt, Evidence, Review and authoritative result remain separate.**
4. **Observation, Claim, Finding Observation, Correlated Finding and Verdict remain separate but linkable.**
5. **Recipe, Assessment Plan, Protocol and Run remain separate.**
6. **Provider, Session, Lease, Event, Revision and Snapshot use typed families, not ambiguous global IDs.**
7. **Every state machine is namespaced/versioned; `completed`, `verified` and `accepted` never collapse.**
8. **Provider generation, Node generation, workload generation and connection epoch remain distinct.**
9. **Snapshot production, Checkpoint restoration and application recovery are different proof levels.**
10. **Capability availability, permission, authorization, placement, reservation and execution authority remain separate.**
11. **Deletion uses retention, tombstone, supersession and referential-integrity rules rather than silent cascades.**
12. **Public/private audience and redaction classes travel with every exportable record.**

### 5. Accept parked/restricted items as non-blocking

The following do not block Phase 0B:

- `.P5C` unknown format support;
- shared cross-Node POSIX filesystem;
- MiniRouter source reuse pending licence;
- Dify modified-licence integration;
- exact GNOME Ponytail dependency selection;
- non-GNOME Wayland input completion;
- unaudited private device-manager source;
- `chrisipanaque` prototype reuse;
- missing `amertoglu16.github.io` source;
- any donor source without a clear compatible licence;
- final public Ptah project licence.

Their reopening criteria and v1 alternatives are recorded in the consistency review and donor register.

The public Ptah licence becomes a Phase 0C gate because no implementation/dependency distribution exists yet.

### 6. Use the ordered Phase 0B sequence

Phase 0B proceeds in this order:

1. common identity, versioning and typed-family conventions;
2. Activity/Operation/Attempt/Event/Receipt/proof;
3. Object/Revision/View/Artifact/storage relationships;
4. Node/Facility/Provider/capability/health;
5. Workspace/Session/checkpoint/recovery;
6. transfer/sync/conflict/backup;
7. Recipe/Build/provenance/SBOM/signature/verification;
8. Domain Pack/firmware/disk/Device;
9. Application/Browser/semantic UI/Shell;
10. knowledge/data/Package/Plugin;
11. isolation/placement/reservation/lease/secure grants;
12. security/Finding/Claim/Evidence/reproduction;
13. migrations and conformance harness;
14. golden/negative corpus and proof-plan freeze;
15. Phase 0B review/freeze and Phase 0C readiness decision.

The first four packages establish the shared identities and proof primitives used by later schemas.

## Phase 0B completion gate

Phase 0B completes only when:

1. all schemas are versioned and traceable to requirements/ADRs;
2. state machines and transitions are explicit;
3. saved objects/sessions have migration paths;
4. permission, audience and redaction are represented;
5. Provider/Facility conformance contracts exist;
6. lawful golden and negative fixtures are pinned;
7. proof plans name exact required Receipts/Evidence;
8. backend replacement is testable;
9. online and later local Nodes use the same contracts;
10. private consumer knowledge is absent from public schemas;
11. public licence/dependency strategy is ready for Phase 0C;
12. the first vertical slice can be selected without identity/proof ambiguity.

## Consequences

### Positive

- Phase 0A stops expanding indefinitely.
- Phase 0B has a concrete ordered input set.
- donor selection remains deferred until schemas and proof are stable.
- parked features cannot silently block the first vertical slice.
- future architecture changes require explicit migration-aware decisions.
- public implementation remains honest and unopened.

### Costs

- Phase 0B must design many typed schemas before coding.
- shared envelopes and state-machine versions add discipline and complexity.
- golden/negative fixtures and conformance suites require substantial preparation.
- some donor/dependency choices remain deferred to Phase 0C.

## Rejected alternatives

### Continue donor research without freezing

Rejected. All current v1 requirements have composite design closure; further undirected research creates architecture noise.

### Begin the first implementation immediately

Rejected. Shared identities, migrations and proof contracts are not yet frozen.

### Select dependencies during schema design

Rejected. Phase 0B should stay backend-neutral; exact dependency/source layout is a Phase 0C decision.

### Treat parked gaps as hidden blockers

Rejected. Each item has an explicit v1 alternative and reopening criterion.

## Required synchronization

After accepting this ADR:

- update `DECISIONS.md`;
- update `MASTER_ROADMAP.md` current phase/status;
- update `PROGRESS.md`;
- update `CURRENT_STATE.md`;
- update `REQUIREMENT_CLOSURE_MATRIX.md` conclusion;
- preserve the Phase 0A checkpoint commit above.
