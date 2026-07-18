# Ptah Current State

**Last updated:** 2026-07-18  
**Overall status:** ACTIVE PLANNING — PHASE 0A FROZEN; PHASE 0B ACTIVE  
**Current phase:** Phase 0B — contracts, migrations, conformance and proof design  
**Active work package:** 0B-WP01 — common identity, versioning and typed-family conventions  
**Runtime implementation:** NOT STARTED  
**Dependency selection:** NOT STARTED  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

# Frozen Phase 0A checkpoint

Phase 0A donor recovery, requirement closure, source cleanup and cross-requirement review are complete and frozen at:

```text
7d2dffee48f1400ba1cf88823343f09a3895ad33
```

Freeze decision:

- `decisions/ADR-0017-PHASE-0A-FREEZE-PHASE-0B-ENTRY.md`

Review and entry evidence:

- `work-packages/PHASE-0A-CROSS-REQUIREMENT-CONSISTENCY-REVIEW.md`
- `work-packages/PHASE-0B-ENTRY-CONTRACT-PROOF-INPUTS.md`
- `REQUIREMENT_CLOSURE_MATRIX.md`
- `DONOR_RECOVERY.md`

All current v1 requirements are closed for Phase 0B contract design. No implementation is authorized by that closure.

---

# Accepted Ptah position

Ptah is an independent, open-source, online-first concurrent digital world built around persistent Workspaces, Objects, Activities, Facilities, Nodes, Devices, Applications, Browsers, Sessions, Panels, Knowledge Sources, Datasets, Plugins, security Findings and Artifacts.

Ptah supplies the working world. Humans and compatible systems supply intent, reasoning, policy, restrictions, risk acceptance and acceptance criteria.

The public repository remains a no-code implementation shell and correctly states that implementation has not started.

---

# Phase 0A closure summary

Closed for design:

1. Core runtime, Activities, Events, recovery and proof.
2. Build, Artifact, SBOM, provenance, signing and verification.
3. Storage, transfer, synchronization, conflict and backup.
4. Universal Object graph and progressive decomposition.
5. Firmware, disks, filesystems and physical-device proof.
6. Android, Linux, Windows, macOS and iOS Device/Application runtimes.
7. Linux AT-SPI semantic automation and explicit visual fallback.
8. Browser profiles, contexts, pages, downloads and research evidence.
9. Human Workspace shell, Panels, Layout and control ownership.
10. Knowledge, data, search, Package and Plugin composition.
11. Isolation classes, placement, reservation, lease and distributed execution.
12. Security authorization, Findings, Claims, Evidence, remediation and reproduction.
13. Research/profile/documentation-source cleanup.
14. Cross-requirement identity, authority, lifecycle and proof consistency.

Accepted decisions are ADR-0001 through ADR-0017 and are indexed in `DECISIONS.md`.

---

# Cross-requirement rules now frozen

Phase 0B must preserve:

1. **Object owns content identity; Artifact owns durable promoted-result role.**
2. **Activity, Operation and Attempt are separate.**
3. **Event, telemetry, Receipt, Evidence, Review and authoritative external result are separate.**
4. **Observation, Claim, Finding Observation, Correlated Finding and Verdict are separate but linkable.**
5. **Recipe, Assessment Plan, Protocol and Run are separate.**
6. **Provider, Session, Lease, Event, Revision and Snapshot are typed families.**
7. **State machines are namespaced and versioned.**
8. **`completed`, `verified` and `accepted` never collapse into one state.**
9. **Node generation, Provider generation, workload generation and connection epoch remain distinct.**
10. **Capability availability, permission, authorization, placement, reservation and execution authority remain distinct.**
11. **Checkpoint production, restore and application recovery are different proof levels.**
12. **Deletion uses retention, tombstone, supersession and referential-integrity rules.**
13. **Audience, privacy and redaction classes travel with every exportable record.**
14. **Backend identifiers remain aliases rather than canonical Ptah identities.**

---

# Active work — 0B-WP01

## Common identity, versioning and typed-family conventions

Produce the shared contract foundation before domain schemas.

Required outputs:

### Identity primitives

- canonical entity identifier format;
- entity-kind registry;
- typed entity reference;
- backend alias/reference;
- revision and generation references;
- hash/digest representation;
- relationship identity and revision;
- source/provenance reference;
- authority/owner/caller reference;
- audience/privacy/redaction class;
- retention/tombstone/supersession fields;
- limitation and unsupported-capability records.

### Versioning

- schema identifier and schema version;
- compatibility policy;
- additive versus breaking change rules;
- migration identity and Receipt;
- old/new record coexistence;
- state-machine migration;
- export/import version manifest;
- canonical schema registry direction.

### Typed families

Define common envelopes plus explicit kinds for:

- Provider;
- Session;
- Lease;
- Event;
- Revision;
- Snapshot;
- Recipe;
- Protocol;
- Evidence;
- Relationship;
- Location;
- Capability.

### State machines

Every canonical mutable entity must declare:

```text
state_machine_name
state_machine_version
allowed_states
allowed_transitions
transition_authority
required_preconditions
required_receipts_or_evidence
terminal_states
recovery_transitions
timeout_or_expiry_behavior
migration_mapping
```

A generic untyped `status` field is prohibited in canonical contracts.

### Initial conformance proof

- reject a backend alias used as canonical identity;
- reject an unknown entity kind;
- retain conflicting aliases;
- distinguish four different typed Lease kinds;
- distinguish Snapshot from restorable Checkpoint;
- reject an invalid state transition;
- migrate a versioned record without rewriting immutable history;
- preserve audience/privacy/redaction through export;
- tombstone an entity while preserving historical relationships.

---

# Ordered Phase 0B sequence

1. **0B-WP01** — common identity, versioning and typed-family conventions. **ACTIVE**
2. **0B-WP02** — Activity, Operation, Attempt, Event, Receipt and proof.
3. **0B-WP03** — Object, Revision, View, Artifact and storage relationships.
4. **0B-WP04** — Node, Facility, Provider, capability and health.
5. **0B-WP05** — Workspace, Session, checkpoint and recovery.
6. **0B-WP06** — transfer, sync, conflict and backup.
7. **0B-WP07** — Recipe, Build, provenance, SBOM, signature and verification.
8. **0B-WP08** — Domain Pack, firmware, disk and Device contracts.
9. **0B-WP09** — Application, Browser, semantic UI and Shell contracts.
10. **0B-WP10** — knowledge, data, Package and Plugin contracts.
11. **0B-WP11** — isolation, placement, reservation, lease and secure grants.
12. **0B-WP12** — security, Finding, Claim, Evidence and reproduction contracts.
13. **0B-WP13** — cross-contract migrations and conformance harness.
14. **0B-WP14** — golden/negative corpus and proof-plan freeze.
15. Phase 0B review/freeze and Phase 0C readiness decision.

---

# Parked and restricted items

These do not block Phase 0B:

- `.P5C` pending a lawful sample/specification/parser;
- shared cross-Node POSIX filesystems pending measured need;
- MiniRouter source reuse pending a compatible licence;
- Dify integration under its modified-licence boundary;
- exact GNOME Ponytail dependency approval;
- non-GNOME Wayland input completion;
- unaudited private device-manager modules;
- `chrisipanaque` prototype reuse pending licence and proof;
- missing `amertoglu16.github.io` source;
- donor source without a clear compatible licence;
- final public Ptah project licence.

Their v1 alternatives and reopening criteria are recorded in:

- `work-packages/PHASE-0A-CROSS-REQUIREMENT-CONSISTENCY-REVIEW.md`
- `DONOR_RECOVERY.md`

The public Ptah licence is a Phase 0C gate because no implementation or dependency distribution exists yet.

---

# No-build boundary

Allowed now:

- schema and state-machine design;
- migration and compatibility design;
- Provider/Facility adapter-contract design;
- conformance-suite design;
- lawful golden and negative fixture planning;
- proof-plan design;
- public/private schema and documentation boundaries;
- Phase 0C dependency/licence decision inputs.

Not allowed yet:

- runtime or large UI implementation;
- copying or adapting donor source;
- selecting or distributing dependencies;
- deploying Nodes, Providers, browsers, scanners or schedulers;
- activating a public plugin/package registry;
- presenting design closure as built, proven or complete.

Implementation begins only after Phase 0C selects and approves the first vertical slice in this file.

---

# Phase 0B completion gate

Phase 0B completes only when:

1. every schema is versioned and traceable to requirements and ADRs;
2. state machines and transitions are explicit;
3. saved records and Sessions have migration paths;
4. permissions, audience and redaction are represented;
5. Provider/Facility conformance contracts exist;
6. lawful golden and negative fixtures are pinned;
7. proof plans name exact required Receipts and Evidence;
8. backend replacement is testable;
9. online and later local Nodes use the same contracts;
10. private consumer knowledge is absent from public schemas;
11. public licence/dependency strategy is ready for Phase 0C;
12. the first vertical slice can be selected without identity or proof ambiguity.

---

# Chat continuation instruction

Read this file first, followed by:

1. `decisions/ADR-0017-PHASE-0A-FREEZE-PHASE-0B-ENTRY.md`;
2. `work-packages/PHASE-0B-ENTRY-CONTRACT-PROOF-INPUTS.md`;
3. `MASTER_ROADMAP.md`;
4. `PROGRESS.md`;
5. `DECISIONS.md`;
6. `MEMORY_PROTOCOL.md`;
7. `DONOR_RECOVERY.md`;
8. `REQUIREMENT_CLOSURE_MATRIX.md`;
9. the accepted ADRs and work packages relevant to the active Phase 0B schema.

Do not restart donor research or implementation from conversational memory.
