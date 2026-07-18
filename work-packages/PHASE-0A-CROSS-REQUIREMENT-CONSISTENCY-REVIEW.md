# Phase 0A — Cross-Requirement Consistency Review

**Status:** COMPLETE — NO DESIGN-BLOCKING CONTRADICTION FOUND  
**Date:** 2026-07-18  
**Implementation:** NOT STARTED

## Purpose

Review the accepted Phase 0A architecture as one system rather than separate donor clusters. Confirm that identity, authority, lifecycle, proof and public/private rules can be expressed coherently in Phase 0B schemas.

## Canonical sources reviewed

- `CURRENT_STATE.md`
- `MASTER_ROADMAP.md`
- `PROGRESS.md`
- `DECISIONS.md`
- `DONOR_RECOVERY.md`
- `REQUIREMENT_CLOSURE_MATRIX.md`
- `MEMORY_PROTOCOL.md`
- ADR-0001 through ADR-0016
- closed Phase 0A work packages and relevant donor/internal records
- public `jaydumisuni/Ptah-space` repository and README

The accepted-decision index is the highest architecture authority after explicit future ADRs.

---

# 1. Identity consistency

## Stable Ptah identities

Ptah owns stable identities for the world and its historical records. Backend/runtime identifiers remain aliases.

Canonical hierarchy:

```text
Node
Workspace
Activity
Operation
Attempt
Object
Object Revision / View / Derivative
Artifact
Facility
Provider
Application / Device / Browser / Shell / Terminal Sessions
Event
Receipt
Claim
Finding Observation
Correlated Finding
Evidence
Recipe
Protocol
Assessment Plan
Reproduction Run
Checkpoint
```

## Object and Artifact

No contradiction remains.

- An **Object** is the universal immutable content identity.
- An **Artifact** is a durable promoted result/record that references one or more Objects and carries production, retention, verification and relationship metadata.
- Artifact bytes never gain a second competing content identity.
- Reports, SBOMs, attestations, screenshots, patches and proof bundles may be both Objects and promoted Artifacts.
- Mutable tags, paths and registry names remain aliases/locations.

Phase 0B rule:

```text
Object owns content identity.
Artifact owns durable result role and provenance relationships.
```

## Activity, Operation and Attempt

No contradiction remains.

- Activity is the caller-visible durable unit of work.
- Operation is one logical side effect or observation inside an Activity.
- Attempt is one physical execution try.
- Retries preserve Activity/Operation identity and create new Attempts.
- provider/runtime task IDs remain aliases.

## Provider identities

`Provider` is intentionally reused across Workspace, Device, Application, Browser and runtime domains, but Phase 0B must define a typed provider envelope:

```text
provider_id
provider_kind
provider_revision
provider_instance_id
provider_generation
capabilities
health
backend_aliases
```

Provider kinds are not interchangeable. A Browser Provider cannot satisfy an Application Provider requirement without an explicit adapter/capability claim.

## Session identities

`Session` is a family, not one universal mutable record.

Required typed subtypes include:

- Workspace Session / recovery record;
- Shell Session;
- Terminal/PTY Session;
- Browser Profile/Process/Context/Page lifecycle records;
- Device Session;
- Application Session;
- display/input streams;
- security/reproduction execution sessions where needed.

A common session envelope may exist, but every subtype keeps its own ID, lifecycle, owner, provider generation and recovery semantics.

## Lease identities

`Lease` is also a family.

Required kinds include:

- Node/resource reservation lease;
- Provider/workload lease;
- Device ownership/control lease;
- Shell/human-input control lease;
- browser/application/device input lease;
- other scoped exclusive authority.

Phase 0B must define:

```text
lease_id
lease_kind
resource_reference
holder_reference
capability_scope
issued_at
expires_at
state
fencing_token
parent_reservation_or_authorization
```

A control lease cannot reserve CPU/RAM. A placement lease cannot grant pointer/keyboard input. Shared envelope does not imply shared authority.

## Revision, Snapshot and Checkpoint

These terms are compatible when typed:

- Revision: immutable historical version of a logical entity/configuration/source.
- Snapshot: observed state at a time, possibly derived/partial.
- Checkpoint: state intentionally prepared for resume/recovery.

Examples remain separate:

- Object Revision;
- Layout Revision;
- Index Revision;
- Ruleset/Database/Protocol Revision;
- Node Capability Snapshot;
- Semantic Snapshot;
- filesystem/VM snapshot;
- Checkpoint Bundle.

A Snapshot is not automatically restorable. A Checkpoint is not proven usable until restore and application read-back succeed.

---

# 2. State-machine consistency

## Canonical Activity state

The Master Roadmap and core ADRs remain authoritative for Activity state:

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

Additional planning states may be introduced in Phase 0B only through an explicit migration/versioned state-machine decision.

## Cross-entity lifecycle labels

One normalization issue was found: the Human Workspace ADR lists labels such as `planned`, `configured`, `available`, `connected`, `verified` and `accepted` beside Activity labels.

These are **not** one Activity state enum.

They belong to different namespaces:

```text
configuration_state
capability_availability_state
connection_state
activity_state
proof_or_verification_state
review_or_acceptance_state
```

UI may present them together, but every label must display its entity/type. `completed`, `verified` and `accepted` remain separate.

## Domain state machines

Each entity owns a versioned state machine:

- Workspace lifecycle;
- Activity lifecycle;
- Provider/connection health;
- Transfer state;
- Build state;
- Device/Application/Browser/Shell Session state;
- Reservation/Lease state;
- Finding/disposition/remediation state;
- Reproduction/result/review state;
- Plugin installation/activation state.

A generic `status` field without state-machine type/version is prohibited in canonical schemas.

---

# 3. Event, telemetry, receipt and proof consistency

## Event

`Event` is a typed notification envelope, not one universal semantic.

Phase 0B must include:

```text
event_id
event_version
event_domain
event_type
source_identity
subject_identity
activity_operation_attempt
provider_generation
connection_epoch
occurred_at
observed_at
sequence_or_cursor
payload_reference
```

Examples:

- Activity/Event Fabric events;
- semantic UI events;
- provider health events;
- transfer progress;
- scanner/reproduction events.

Semantic AT-SPI events and NATS Event Fabric messages use the same outer correlation rules but retain different domain payloads and guarantees.

## Telemetry

Logs, metrics and traces are operational observations. Sampled or unauthenticated telemetry cannot replace proof-critical Receipts.

## Receipt

A Receipt is append-only producer evidence bound to an exact Activity/Operation/Attempt, nonce/epoch, producer and proof level.

A Receipt may reference Objects/Artifacts/Evidence but is not the same as any of them.

## Evidence

Evidence is an immutable item or relationship used to support, contradict or limit a Claim/Finding/review. Evidence can reference:

- Objects and Artifacts;
- Receipts;
- source ranges;
- HTTP exchanges;
- screenshots/video;
- logs/traces;
- reports and SBOMs;
- signatures/attestations;
- physical/external read-back;
- reproduction comparisons;
- reviewer records.

## Proof and authority

Proof level and authority class remain separate.

Examples:

- a provider may report operation completion;
- a physical device may provide read-back;
- an external service may own authoritative result;
- an independent reviewer may issue a verdict;
- organization/caller policy may accept or reject.

No stronger level is inferred from a weaker one.

---

# 4. Claim, Observation, Finding and review consistency

## Observation

An Observation is one detector/provider/tool assertion tied to exact source and machinery revision.

Examples:

- file-type detection;
- package observation;
- scanner alert;
- semantic UI node snapshot;
- device protocol observation.

## Claim

A Claim is one bounded proposition with scope, period, protocol and limitations.

Claims can be supported, contradicted or limited by Evidence.

## Finding Observation and Correlated Finding

Security-specific structure remains compatible with the general Claim/Evidence model:

- Finding Observation: one security detector/source assertion;
- Correlated Finding: stable reviewed issue identity grouping observations;
- correlation/split/merge/duplicate decisions are Claims;
- original observations never disappear.

## Review/Verdict

A Review or Verdict is an evaluator conclusion over exact inputs/checkpoint and declared evidence. It does not mutate the underlying Activity, Artifact or Finding automatically.

## Acceptance

Acceptance belongs to the caller/organization policy domain, not the scanner, provider, reviewer or Ptah runtime itself.

---

# 5. Recipe, Plan, Protocol and Run consistency

## Recipe

A Recipe describes intended executable work.

Typed recipes include:

- Build Recipe;
- transformation/render recipe;
- Reproduction Recipe;
- reusable deterministic operation graph.

## Assessment Plan

A Security Assessment Plan describes the authorized target, scope, machinery, coverage and sequence. It is not itself execution or a proof protocol.

## Protocol

A Protocol freezes how a Claim/result will be evaluated:

- target/source/environment boundary;
- commands/actions;
- expected outputs;
- tolerances;
- negative/drift rules;
- required evidence;
- result/reproduction/review levels.

A Protocol may reference a Recipe or Assessment Plan.

## Run

A Build, Scan, Assessment, Reproduction or Verification Run is an Activity/attempt applying an exact Recipe/Plan/Protocol revision.

The following remain separate:

```text
specification accepted
run completed
output produced
output read back
claim supported
independently reproduced
review passed
caller accepted
```

---

# 6. Authority and permission consistency

No contradiction remains among general execution, provider, UI-control, plugin, security and organizational boundaries.

Authority is layered:

1. caller/user/organization grants intent and policy authority;
2. Ptah control plane validates contract and permissions;
3. scheduler/Provider grants scoped technical capacity;
4. Facility executes within granted capabilities;
5. human/control leases govern interactive input;
6. Receipts/Evidence record what happened;
7. independent reviewers evaluate exact checkpoints;
8. external systems/physical devices retain their own authoritative outcomes;
9. caller/organization accepts, rejects or tolerates risk.

Required separation:

- authentication is not authorization;
- capability availability is not permission;
- placement is not reservation;
- reservation is not execution authority without lease;
- UI focus is not control authority;
- scanner target reachability is not security-test authorization;
- plugin installation is not activation;
- signed code/report is not approved behavior;
- reviewer PASS is not organizational acceptance.

---

# 7. Lifecycle consistency

All mutable logical entities require:

- created/current revision;
- explicit owner/scope;
- versioned state machine;
- health/degraded state where applicable;
- retry/recovery relationships;
- archive/export behavior;
- deletion/tombstone behavior;
- cleanup verification;
- historical record preservation.

## Deletion rules

- immutable Objects/Artifacts/Receipts are removed only through explicit retention/deletion policy and tombstone/audit records;
- derived indexes/caches/previews can be rebuilt and may be evicted;
- plugin removal cleans registrations, permissions, runtime state and secrets;
- session deletion does not silently delete shared Objects/Artifacts;
- finding suppression does not delete observations;
- revocation does not rewrite historical signatures/attestations;
- Workspace deletion must reconcile active Activities, mounted resources, credentials, backups and shared references.

Phase 0B must define referential-integrity and tombstone rules rather than relying on backend cascades.

---

# 8. Public/private consistency

No contradiction was found.

- `ptah-roadmap-` remains private planning/recovery truth.
- `Ptah-space` remains the public implementation repository.
- the public repository currently contains only a neutral README and explicitly states implementation has not started.
- private consumers, topology, credentials, customer data and unreleased security evidence remain outside public source.
- public documentation builds consume explicit allowlisted public source.
- generated search indexes/assets/source maps are checked for leakage.

Open Phase 0C decision:

- select the public Ptah project licence after exact dependency/source layout is approved.

This is not a Phase 0A architecture blocker because no implementation code or dependency distribution exists yet.

---

# 9. Parked/restricted gap audit

| Gap | Phase 0A verdict | Non-blocking v1 path | Reopening criterion |
|---|---|---|---|
| `.P5C` | Parked | unknown-format registration and generic binary research path | lawful sample, specification or verified parser |
| shared cross-Node POSIX filesystem | Parked | Object transfer, local cache and explicit copies/mounts | measured workload requiring shared POSIX semantics |
| MiniRouter licence | Source reuse blocked | native Ptah placement/routing contracts; optional evaluation only | compatible licence and source review |
| Dify modified licence | Restricted | LlamaIndex/native facilities or separately licensed deployment | approved separate licence/use boundary |
| GNOME Ponytail exact dependency | Phase 0B/0C selection item | X11, AT-SPI semantic action, visual fallback and manual handoff | exact source pin, licence, security and deployment approval |
| non-GNOME Wayland input | Partial/parked | semantic read where available; visual/manual fallback | compositor-specific supported provider evidence |
| unaudited private device-manager modules | Source-recovery gap | public Android/platform donors plus existing internal evidence/contracts | lawful source access and file-level review |
| `chrisipanaque` prototypes | Source reuse parked | accepted native/policy/OTel/MCP composition | exact requirement gap, clear licence and proof |
| `amertoglu16.github.io` | Parked | no dependency | valid source/archive or recoverable lineage |
| donor without clear licence | Reuse blocked | study patterns only or alternative donor | licence resolved |
| public Ptah licence | Phase 0C decision | no distributed code yet | dependency/source layout approved |

No item blocks Phase 0B schema/proof design.

---

# 10. Corrections and normalization required in Phase 0B

1. Use namespaced state machines; do not create one global `status` enum.
2. Define typed envelopes for Provider, Session, Lease, Event, Revision and Snapshot.
3. Keep Object content identity separate from Artifact role identity.
4. Define Evidence as references/relationships over immutable records, not copied truth.
5. Keep Claim, Observation, Finding and Review schemas distinct but linkable.
6. Define common Activity/Operation/Attempt correlation across every Facility.
7. Separate provider generation, Node generation, workload generation and connection epoch.
8. Define Recipe, Assessment Plan, Protocol and Run relationships explicitly.
9. Define deletion/tombstone/referential-integrity rules.
10. Version every contract and state machine with migration paths.
11. Preserve public/private audience and redaction classes in every exportable record.
12. Define canonical requirement IDs, including `SEC-001` and `REPRO-001`; older wording is an alias only.

---

# 11. Review verdict

## Result

**PASS FOR PHASE 0A DESIGN CONSISTENCY.**

No accepted ADR requires reversal. No v1 requirement lacks a composite design path. No parked item blocks Phase 0B.

The review found normalization work that belongs exactly in Phase 0B schemas, especially typed state/lease/session/event/snapshot families. Those are contract-design tasks, not unresolved architecture.

## Remaining prerequisites for Phase 0A freeze

1. enumerate Phase 0B schemas, migrations, conformance suites and proof corpus;
2. record the Phase 0A freeze/Phase 0B entry decision;
3. synchronize Master Roadmap, Progress, Current State, Matrix and Decision index.

No implementation is authorized by this review.
