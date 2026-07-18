# Phase 0B Entry — Contract, Migration, Conformance and Proof Inputs

**Status:** ENTRY INPUTS COMPLETE — PHASE 0B WORK NOT YET EXECUTED  
**Date:** 2026-07-18  
**Purpose:** freeze the exact design inputs required before Ptah implementation selection

## Entry rule

Phase 0B converts accepted Phase 0A boundaries into versioned schemas, state machines, migrations, conformance suites and proof fixtures.

Phase 0B does **not** select production dependencies or authorize runtime implementation. That occurs only in Phase 0C.

---

# 1. Common contract foundation

Every canonical record requires a shared foundation for:

```text
stable ID and entity type
schema name and schema version
entity/revision generation
created, updated, occurred and observed timestamps
Workspace and caller scope
authority and ownership references
provider/facility/backend references
source and provenance references
audience, privacy and redaction class
retention and deletion policy
extension/vendor metadata
limitations and confidence where applicable
```

## Typed-family rule

The following require common envelopes plus explicit subtype/kind fields:

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

No generic `status`, `session_id`, `lease_id`, `snapshot_id` or `provider_id` can be interpreted without its entity kind and state-machine/schema version.

## State-machine rule

Each entity state machine defines:

```text
state_machine_name
state_machine_version
allowed_states
allowed_transitions
transition authority
required preconditions
required receipts/evidence
terminal states
recovery transitions
timeout/expiry behavior
migration mapping
```

`completed`, `verified` and `accepted` are never one state.

---

# 2. Core world schemas

## B01 — Identity and relationship primitives

Required schemas:

- Entity Reference;
- Typed Alias/Backend Reference;
- Revision Reference;
- Relationship and Relationship Revision;
- Authority Reference;
- Audience/Privacy/Redaction Class;
- Capability Claim;
- Limitation/Unsupported Capability;
- Tombstone/Supersession;
- Hash/Digest and content identity;
- Location and Replica Reference.

Required proof:

- reject alias as canonical identity;
- retain conflicting aliases;
- migrate an old entity reference;
- preserve tombstoned relationships without dangling silent loss.

## B02 — Node, Facility and Provider

Required schemas:

- Node Identity and Node Generation;
- Node Capability Snapshot;
- Resource/Pressure Snapshot;
- Facility Definition and Facility Revision;
- Provider Definition, Instance and Generation;
- Provider Capability/Health/Degraded State;
- Adapter/Backend Reference;
- Service/Port/Route registration;
- Node connection epoch and reconnect record.

Required proof:

- stale Node/provider generation rejected;
- capability snapshot expires/reconciles;
- degraded Provider does not mark Facility unavailable globally;
- one Facility switches backend without identity loss.

## B03 — Workspace and Session

Required schemas:

- Workspace;
- Workspace Revision/Configuration;
- Workspace Provider Binding;
- Workspace Membership/Permission;
- Workspace Session/Recovery Record;
- Workspace Archive/Export/Import;
- Workspace deletion/tombstone plan;
- shared Object/Artifact reference protection.

Required proof:

- Workspace persists while unrelated Activities run/fail;
- archive/import preserves identity and revisions;
- deleting one Workspace does not delete shared Objects silently;
- provider replacement preserves Workspace identity.

## B04 — Activity, Operation and Attempt

Required schemas:

- Activity;
- Activity Dependency Edge;
- Operation;
- Attempt;
- Idempotency Key;
- Correlation Nonce;
- Retry/Resume/Recovery relationship;
- cancellation/pause/manual-action records;
- resource and time budget;
- current state plus state history.

Required proof:

- ten independent Activities coexist;
- one failure does not stop unrelated work;
- retries create new Attempts without duplicate side effects;
- non-idempotent operation refuses unsafe automatic retry;
- reconnect reconstructs current state from durable records.

## B05 — Event, telemetry and Receipt

Required schemas:

- Event Envelope;
- Event Domain Payload registration;
- sequence/cursor/replay metadata;
- Telemetry Correlation;
- Receipt;
- Proof Level;
- Authority Class;
- Review/Verdict;
- Authoritative External Result.

Required proof:

- reject wrong operation/attempt/nonce/epoch;
- reject incompatible/unauthenticated producer;
- preserve late valid completion after reconnect;
- distinguish Event, telemetry, Receipt, review and external authority;
- preserve proof-critical Receipts when telemetry export fails.

---

# 3. Object, storage and Artifact schemas

## B06 — Object and revision graph

Required schemas:

- Object;
- Object Revision;
- Content Blob/Digest;
- Parent/Child Relationship;
- Detector Observation;
- Declared versus detected type;
- View;
- Preview;
- Derivative/Transformation;
- Decompilation/Rebuild relationship;
- recursive decomposition budget and truncation;
- Object permission and retention.

Required proof:

- identical content deduplicates without collapsing logical references;
- detector disagreement remains visible;
- progressive decomposition preserves original bytes;
- deep recursion is bounded and resumable;
- rebuild result links to exact source Objects and recipe.

## B07 — Artifact and provenance role

Required schemas:

- Artifact;
- Artifact Revision/Release;
- Artifact/Object membership;
- Artifact Relationship;
- Verification State;
- retention/visibility;
- publication/export alias;
- report/SBOM/attestation/signature/review/reproduction references.

Required proof:

- Artifact references Object content identity rather than duplicating it;
- mutable tag/path cannot replace immutable Artifact identity;
- Artifact location changes without identity change;
- deletion/retention policy preserves required evidence lineage.

## B08 — Storage, transfer, sync and backup

Required schemas:

- Storage Class;
- Object Location/Replica;
- Transfer Intent/Session/Attempt;
- partial-range/chunk state;
- streaming hash/checkpoint;
- Resume Token/Backend Cursor;
- Sync Revision Vector;
- Conflict;
- Backup Set/Snapshot;
- Restore Run and verification;
- Drive/OCI/R2/S3/local export references.

Required proof:

- interrupted upload/download resumes;
- corrupt partial data is detected;
- source changes during transfer produce explicit conflict/restart;
- two offline revisions create a retained conflict;
- backup existence is separate from successful restore/read-back.

---

# 4. Build and provenance schemas

## B09 — Recipe and Build

Required schemas:

- Recipe and Recipe Revision;
- Build Recipe subtype;
- compiled backend plan/graph;
- Build Activity/Operation mapping;
- cache record/reuse Receipt;
- secret/credential reference;
- output declaration;
- Build Result;
- unsupported/altered capability record.

Required proof:

- same Recipe compiles to two backends with explicit differences;
- cache hit records source/input/output identities;
- volatile input marks output non-reproducible until verified;
- secret values do not enter Recipe/log/cache/provenance;
- native platform build uses same outer contract without pretending to be BuildKit.

## B10 — SBOM, attestation, signature and verification

Required schemas:

- SBOM Document/Revision;
- Package Observation and package identity aliases;
- Attestation Statement and Envelope;
- Signature;
- Transparency/identity evidence;
- Verification Run/Result;
- signer/reviewer trust policy;
- revocation and stale verification;
- Provenance Graph Relationship.

Required proof:

- signature integrity is separate from semantic correctness;
- SBOM conversion loss is visible;
- advisory/database changes create new scan revision;
- revoked/stale signer evidence does not rewrite historical record;
- another verifier reproduces the exact validation result or records disagreement.

---

# 5. Domain Pack and specialist schemas

## B11 — Domain Pack

Required schemas:

- Domain Pack Definition/Revision;
- detector and confidence;
- inventory/decompose/preview/open/transform/validate/compare/rebuild/execute capability;
- supported formats/platforms;
- recursion/resource limits;
- unsupported/partial result;
- plugin/package/provider bindings.

Required proof:

- one Pack replaced without Object identity loss;
- unsupported capability remains explicit;
- malicious archive/path/traversal inputs remain contained;
- generated derivative retains exact origin.

## B12 — Firmware, disk and filesystem

Required schemas:

- Firmware Package/Manifest/Component;
- compatibility target and confidence;
- Disk/Image/Partition/Table/Filesystem;
- mount/open/convert/extract/rebuild operation;
- Device Programmer/Loader/Protocol Stage;
- backup/read-back/rollback evidence;
- physical mutation authorization.

Required proof:

- static inspection cannot authorize physical write;
- exact target compatibility is required;
- pre-write backup and post-write read-back remain separate;
- unsupported `.P5C` registers as unknown/parked rather than guessed;
- wrong device/interface epoch blocks operation.

## B13 — Device

Required schemas:

- Device Identity;
- Interface/Connection Epoch;
- Device Provider/Generation;
- Device Session;
- Device Lease/Control Lease;
- display/input/stream;
- package/application operation;
- semantic Screen Context;
- protocol operation and physical proof;
- unstable-connection recovery.

Required proof:

- reconnect does not reuse stale device alias/epoch;
- only current control lease sends input;
- screen stream loss does not falsely end Device Session;
- non-idempotent action refuses unsafe retry;
- cleanup/revocation verified.

---

# 6. Application, Browser and Shell schemas

## B14 — Application and Window

Required schemas:

- Application Object/Package;
- Installation;
- Application Provider/Generation;
- Application Session;
- Process;
- Window;
- Display/Remote Display Session;
- Semantic Provider/Context;
- Semantic Snapshot/Target/Selector/Event/Action;
- input/control method and post-condition proof;
- checkpoint/restore compatibility.

Required proof:

- process launch differs from runtime ready;
- Window alias/generation changes are reconciled;
- stale semantic target is rejected/reacquired;
- semantic action requires semantic/visual read-back;
- unsupported/opaque UI degrades explicitly;
- X11/GNOME-Wayland/visual paths remain distinct.

## B15 — Browser

Required schemas:

- Browser Binary/Revision;
- Profile;
- Process;
- Context;
- Page;
- Frame/Popup;
- Download;
- cookie/storage/session state;
- navigation/source/DOM/accessibility/screenshot/video/trace/network evidence;
- challenge/authentication/human-completion state;
- research Source/Citation.

Required proof:

- one profile supports multiple isolated Contexts;
- stale Page/process reference is rejected;
- challenge/manual state remains explicit;
- source/DOM/visual evidence disagreement is retained;
- private profile export is prevented/redacted;
- browser restart/reconnect preserves only supported state.

## B16 — Human Workspace shell

Required schemas:

- Shell Client;
- Shell Session;
- Panel Type/Revision;
- Panel Instance;
- binding;
- Layout Profile/Revision;
- View State;
- Control Lease;
- takeover/return Receipt;
- Activity/Evidence projections;
- form-factor/accessibility profile.

Required proof:

- Panel/Layout state never becomes runtime truth;
- phone layout remains usable without free-form docking;
- stale control token rejected;
- human takeover and return are receipted;
- underlying Activity continues after panel close/reconnect;
- public/private contribution boundaries enforced.

---

# 7. Knowledge, data and plugin schemas

## B17 — Knowledge and search

Required schemas:

- Knowledge Source/Revision;
- acquisition and permission record;
- Corpus;
- Document Revision;
- Chunk;
- Index Revision;
- embedding/model reference;
- Query;
- Result/Ranking Explanation;
- Citation;
- freshness/tombstone/reconciliation;
- caller-owned conversation/memory references.

Required proof:

- source deletion/tombstone removes derived retrieval without losing audit;
- Citation binds exact source revision/range;
- index is rebuilt from source Objects;
- permission change is reflected in retrieval;
- two backends return explainable differing rankings.

## B18 — Data

Required schemas:

- Dataset;
- Dataset Revision/Snapshot;
- Table;
- Column Schema;
- Data Query;
- Transformation;
- Result;
- lineage and reproducibility;
- engine/backend references;
- resource/streaming plan.

Required proof:

- Polars and DuckDB execute equivalent bounded queries with explicit differences;
- source revision and schema drift remain visible;
- analytical Result is not transactional source truth;
- large query respects resource budget and partial/failure state.

## B19 — Package and Plugin lifecycle

Required schemas:

- Package;
- immutable Package Release;
- Registry Entry;
- Installed Plugin;
- Activation;
- Manifest/Contribution;
- permissions/resources/isolation class;
- dependency/compatibility;
- migration/health/rollback;
- removal/cleanup/tombstone;
- signature/SBOM/scan/provenance.

Required proof:

- registry presence does not imply approval;
- install does not imply activation;
- upgrade rollback preserves previous release/configuration;
- removal revokes credentials, processes, routes and contributions;
- high-risk plugin escalates isolation or is blocked;
- MCP/Deno/OCI implementation can be replaced behind the same contract.

---

# 8. Isolation and distributed schemas

## B20 — Isolation and secure grants

Required schemas:

- Isolation Class/Revision;
- Runtime Provider capability;
- workload revision/generation;
- Object/View mount grant;
- Network Identity/Policy Grant;
- Device/Accelerator Grant;
- Credential Grant;
- secret delivery/revocation;
- containment/degraded/unsupported result.

Required proof:

- workload never silently falls to weaker isolation;
- stale workload generation loses grants;
- network egress outside allowlist fails;
- exact Object revision mount enforced;
- credential removed on lease loss/stop;
- runtime replacement preserves outer identity/proof.

## B21 — Placement, reservation, lease and fencing

Required schemas:

- Placement Request;
- Candidate and rejection explanation;
- Placement Decision;
- Reservation and atomic bundle;
- Lease;
- workload/node/provider generations;
- Fence Token;
- interruption/preemption policy;
- reschedule/migration/checkpoint relationship;
- locality/cost/failure-domain score components.

Required proof:

- hard infeasible candidate rejected before scoring;
- partial gang reservation never becomes ready;
- stale worker/fence rejected;
- one-Node and multi-Node use same contracts;
- reschedule retains Activity identity and new Attempt/generation;
- external non-fenceable side effect uses nonce/idempotency/read-back reconciliation.

---

# 9. Security and reproduction schemas

## B22 — Security Authorization and Assessment

Required schemas:

- Security Assessment Authorization;
- Assessment Plan;
- exact Target Revision;
- included/excluded scope;
- permitted/prohibited test classes;
- Scanner/Rule/Database/Policy/Add-on/Model Revision;
- credential/network/time/rate/change budget;
- emergency stop and cleanup/read-back;
- Coverage;
- raw Scanner Report Artifact.

Required proof:

- active work blocked without valid authorization;
- out-of-scope target/action blocked;
- scanner database/rule drift creates new report revision;
- no-findings retains skipped/error/unsupported scope;
- sensitive report evidence is redacted/restricted.

## B23 — Finding, Claim, Evidence and disposition

Required schemas:

- Finding Observation;
- Correlated Finding;
- Claim and allowed claim sentence;
- Evidence and Evidence Relationship;
- Risk Assessment dimensions;
- Adjudication/Disposition;
- Suppression/Exception/Accepted Risk;
- remediation proposal/change;
- Verification Run and closure;
- Evidence Card View.

Required proof:

- detector disagreement preserved;
- correlation can split/merge without deleting observations;
- exception expires and returns to review;
- agent/scanner suggestion cannot auto-merge/apply;
- verified closure binds exact remediation and re-test evidence;
- public card cannot exceed bounded claim or leak restricted evidence.

## B24 — Reproduction

Required schemas:

- Protocol and Protocol Revision;
- Reproduction Recipe;
- Reproduction Bundle;
- Reproduction Run;
- Comparison;
- exact/semantic/tolerance result;
- variance/nondeterminism;
- reproduction/verification/review/acceptance levels;
- attestation relationship;
- failed/blocked/drift result.

Required proof:

- bundle assembly does not mark reproduced;
- command replay without output comparison stays lower level;
- nondeterministic output uses frozen tolerance;
- invalid/stale attestation rejected without erasing run;
- failed and blocked reproduction retained;
- alternate backend reproduces or records explicit incompatibility.

---

# 10. Session, checkpoint and recovery schemas

## B25 — Checkpoint Bundle and recovery

Required schemas:

- Checkpoint Bundle;
- component checkpoint reference;
- compatibility group;
- produced/verified/restored/application-recovered states;
- export/import manifest;
- credential/private-state classification;
- missing/unsupported component;
- recovery Activity and read-back.

Required proof:

- checkpoint creation differs from restore and usable application recovery;
- incompatible Node/runtime blocks restore honestly;
- partial recovery lists missing components;
- credentials/private browser/device state are protected;
- session resumes on another compatible Node without identity loss.

---

# 11. Migration and versioning plan

Phase 0B must define:

- semantic versioning policy for public contracts;
- schema-version field and canonical schema registry;
- backward/forward compatibility policy;
- additive versus breaking change rules;
- migration Activity and migration Receipt;
- old/new record coexistence during migration;
- rollback where possible;
- unsupported migration result;
- alias and identifier migration;
- state-machine transition migration;
- event/receipt version negotiation;
- plugin/provider contract compatibility;
- export/import version manifests;
- golden historical fixtures for every released schema.

Migration never silently rewrites immutable history. New canonical records may supersede old records through explicit relationships.

---

# 12. Conformance suites

Every Provider/Facility adapter must pass a common conformance structure:

```text
identity and alias behavior
capability declaration
configuration and health
start/stop/reconnect
Activity/Operation/Attempt correlation
Event ordering/replay limits
Receipt and proof behavior
permissions and denial
resource limits
cancellation and timeout
retry/idempotency
crash/recovery
cleanup/revocation
privacy/redaction
unsupported/degraded behavior
backend replacement
```

Domain suites add specialist tests for transfer, Build, decomposition, firmware, Device, Application, Browser, knowledge, plugin, isolation, security and reproduction behavior.

Conformance proves contract behavior, not universal correctness of the underlying tool.

---

# 13. Golden proof corpus

## Core fixtures

- concurrent independent Activity set;
- stale/duplicate/wrong-nonce Receipt set;
- provider disconnect/reconnect generations;
- out-of-order and missing Events;
- idempotent and non-idempotent operations;
- partial/cancelled/recovered Activities.

## Object/storage fixtures

- duplicate content under different logical names;
- nested mixed archive;
- malformed/truncated archives;
- file changed during transfer;
- corrupt partial ranges;
- sync conflict and tombstone;
- backup that fails restore.

## Build/provenance fixtures

- small multi-language source project;
- container and native build variants;
- cache hit/miss/poison scenarios;
- secret-influence/leak scenario;
- SBOM format conversion loss;
- valid/invalid/stale signature and attestation;
- independently reproduced and non-reproduced outputs.

## Firmware/device fixtures

- lawful immutable example packages for supported families;
- wrong-target compatibility case;
- read-only disk/filesystem images;
- failed/partial physical operation simulation;
- unstable USB/connection epoch case;
- device control lease conflict.

## Application/browser/UI fixtures

- GTK3, GTK4, Qt and Electron/Chromium semantic examples;
- opaque/custom-canvas UI;
- X11 and GNOME-Wayland paths;
- stale Window/Page/Semantic Target;
- browser challenge/manual-completion case;
- profile/cookie privacy export case;
- desktop/tablet/phone layouts;
- control takeover/fencing case.

## Knowledge/data/plugin fixtures

- versioned document corpus with exact citations;
- changed/deleted/permission-revoked source;
- conflicting retrieval rankings;
- dataset schema drift;
- plugin install/upgrade/rollback/removal;
- malicious or overprivileged plugin;
- MCP/Deno/OCI adapter equivalence cases.

## Security/reproduction fixtures

- intentionally vulnerable source/application images;
- scanner disagreement and false-positive case;
- no-findings with skipped scope;
- expired suppression/accepted risk;
- active test blocked outside scope;
- redacted secret evidence;
- agent-originated unsupported claim;
- deterministic and nondeterministic reproduction cases;
- invalid/mismatched attestation;
- failed, blocked and drifted Evidence Cards.

All fixtures require lawful redistributable sources or generated synthetic data.

---

# 14. Negative-proof corpus

The corpus must retain expected failures for:

- invalid schema/version;
- unknown entity kind;
- stale alias/generation/epoch;
- wrong authority/permission;
- expired lease/authorization/exception;
- duplicate side effect;
- partial reservation;
- out-of-order Event;
- unavailable Provider;
- unsupported capability;
- corrupt/missing Object;
- hash mismatch;
- failed cleanup/revocation;
- incomplete semantic tree;
- visual/semantic disagreement;
- challenge/manual handoff;
- incompatible checkpoint;
- source/index drift;
- scanner/rule/database errors;
- no-findings with incomplete coverage;
- invalid signature/attestation;
- failed independent reproduction;
- leaked private data in public build;
- migration failure/rollback.

A failure fixture passes when Ptah reports the exact bounded failure honestly and preserves evidence.

---

# 15. Compatibility matrices

Phase 0B must define matrix formats for:

- schema and API versions;
- client/server/Node compatibility;
- Provider and Facility contract versions;
- runtime/isolation/host kernel/architecture;
- checkpoint restore compatibility;
- Browser binary/profile versions;
- Device protocol/OEM/OS versions;
- Application platform/toolkit/compositor;
- firmware family/target/tool version;
- plugin package/runtime/permissions;
- scanner/rules/database versions;
- documentation build dependencies;
- export/import migration versions.

Unknown compatibility is explicit and blocks unsafe operations.

---

# 16. Public/private and licence inputs

Before Phase 0C:

- select a public Ptah project licence compatible with the approved dependency/source strategy;
- define third-party notice/SBOM generation;
- define copied/adapted/forked/wrapped dependency boundaries;
- define public schema/docs source tree;
- define private consumer adapter boundary;
- define generated public documentation leakage checks;
- define security-evidence disclosure/redaction policy;
- define lawful fixture licences and provenance.

No donor source is copied during Phase 0B unless a later explicit implementation approval permits it.

---

# 17. Ordered Phase 0B work packages

Recommended order:

1. **0B-WP01 Common identity, versioning and typed-family conventions**
2. **0B-WP02 Activity, Operation, Attempt, Event, Receipt and proof**
3. **0B-WP03 Object, Revision, View, Artifact and storage relationships**
4. **0B-WP04 Node, Facility, Provider, capability and health**
5. **0B-WP05 Workspace, Session, checkpoint and recovery**
6. **0B-WP06 Transfer, sync, conflict and backup**
7. **0B-WP07 Recipe, Build, provenance, SBOM, signature and verification**
8. **0B-WP08 Domain Pack, firmware, disk and Device contracts**
9. **0B-WP09 Application, Browser, semantic UI and Shell contracts**
10. **0B-WP10 Knowledge, data, Package and Plugin contracts**
11. **0B-WP11 Isolation, placement, reservation, lease and secure grants**
12. **0B-WP12 Security, Finding, Claim, Evidence and reproduction contracts**
13. **0B-WP13 Cross-contract migrations and conformance harness**
14. **0B-WP14 Golden/negative corpus and proof-plan freeze**
15. **0B review/freeze and Phase 0C readiness decision**

The first four work packages establish identifiers and proof primitives needed by every later schema.

---

# 18. Phase 0B completion gate

Phase 0B completes only when:

1. every schema is versioned and linked to accepted requirements/ADRs;
2. typed state machines and transitions are explicit;
3. migrations exist for saved records and sessions;
4. permissions, audience and redaction are represented;
5. every Provider/Facility has a conformance contract;
6. golden and negative fixtures are lawful and pinned;
7. proof plans state exact required Receipts/Evidence;
8. backend replacement is testable;
9. online and later local Nodes use the same contracts;
10. no private consumer knowledge enters public schemas;
11. public project licence/dependency strategy is ready for Phase 0C;
12. exact first vertical slice can be selected without unresolved identity/proof ambiguity.

No implementation is authorized by this entry checklist.
