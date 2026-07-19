# Ptah Current State

**Last updated:** 2026-07-19  
**Overall status:** ACTIVE PLANNING — PHASE 0A FROZEN; PHASE 0B ACTIVE  
**Current phase:** Phase 0B — contracts, migrations, conformance and proof design  
**Active work package:** 0B-WP07 — Recipe, Build, provenance, SBOM, signature and verification  
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

All current v1 requirements are closed for contract design. That closure does not authorize implementation.

---

# Phase 0B completed candidate packages

## 0B-WP01 — Common identity, versioning and typed families

**Status:** CANDIDATE COMPLETE — downstream use approved; implementation freeze deferred.

Accepted candidate:

- `ptah.common` `0.1.0`;
- `schemas/phase-0b/common/schema-catalog.v0.1.0.json`;
- `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md`.

Active boundaries:

1. canonical entity IDs use lowercase UUIDv7 plus registered `entity_kind`;
2. backend and legacy identifiers remain scoped Aliases;
3. schemas use JSON Schema 2020-12, absolute Ptah URNs and local catalogs;
4. domain entities embed the common Entity Envelope;
5. record revision, Object Revision, schema version, generations and connection epoch remain separate;
6. Provider, Session, Lease, Event, Revision, Snapshot, Recipe, Protocol and Evidence are typed families;
7. state machines are namespaced/versioned and no global `status` enum exists;
8. migration preserves history and compatibility is directional;
9. audience, redaction, privacy, retention, tombstone and deletion are explicit;
10. structural validation never replaces semantic conformance.

## 0B-WP02 — Activity, Operation, Attempt, Event, Receipt and proof

**Status:** CANDIDATE COMPLETE — downstream use approved; executable conformance deferred.

Accepted candidate:

- `ptah.activity` `0.1.0` with corrected request schemas `0.1.1`;
- `schemas/phase-0b/activity/schema-catalog.v0.1.1.json`;
- `decisions/ADR-0019-ACTIVITY-OPERATION-ATTEMPT-EVENT-RECEIPT-PROOF-BOUNDARY.md`.

Active boundaries:

1. Activity Request, Activity, Operation and Attempt remain separate;
2. Operation persists across physical retries and every Attempt receives a new ID/nonce;
3. Attempts bind exact Node/Provider/workload generations and connection epoch;
4. request, placement, cancellation, retry, attachment and projection health remain outside Activity lifecycle;
5. Event and telemetry are not proof;
6. Receipt is immutable append-only producer evidence with exact correlation;
7. proof levels are bounded by domain rather than one universal ladder;
8. Review, Verdict, caller acceptance and authoritative external result remain separate;
9. stale, late, duplicate, contradictory and wrong-generation evidence is reconciled explicitly.

## 0B-WP03 — Object, Revision, View, Artifact and storage

**Status:** CANDIDATE COMPLETE — downstream use approved; executable graph/storage conformance deferred.

Accepted candidate:

- `ptah.object` / `ptah.storage` `0.1.0`;
- `schemas/phase-0b/object/schema-catalog.v0.1.0.json`;
- `decisions/ADR-0020-OBJECT-REVISION-VIEW-ARTIFACT-STORAGE-BOUNDARY.md`.

Active boundaries:

1. Content owns exact bytes/digests and authorized deduplication scope;
2. Object owns logical/source identity and Object Revision owns one immutable version;
3. Location owns one backend materialization and never canonical identity;
4. hash and detector observations remain plural evidence;
5. Relationships have stable identity plus immutable revisions;
6. children, Views, Previews and Derivatives cannot replace originals;
7. decomposition retains budgets, coverage, unknown gaps and partial outputs;
8. Artifact promotion does not imply verification, review, acceptance or release;
9. Artifact Release is immutable, allowlisted and audience/privacy constrained;
10. Location lifecycle, health and verification remain separate;
11. tombstone, replica deletion and shared Content-byte deletion remain separate and receipted.

## 0B-WP04 — Node, Facility, Provider, capability and health

**Status:** CANDIDATE COMPLETE — downstream use approved; executable runtime conformance deferred.

Accepted candidate:

- `ptah.runtime` `0.1.2`;
- 19 record schemas at `0.1.0`;
- six active lifecycle machines;
- `schemas/phase-0b/runtime/schema-catalog.v0.1.2.json`;
- `decisions/ADR-0021-NODE-FACILITY-PROVIDER-CAPABILITY-HEALTH-BOUNDARY.md`;
- `decisions/ADR-0021A-WP04-CATALOG-PROOF-VOCABULARY-CORRECTION.md`;
- `decisions/ADR-0021B-WP04-FINAL-CATALOG-CORRECTION.md`.

Active boundaries:

1. Node identity is separate from aliases, enrollment, trust, lifecycle, reachability, generation and connection epoch;
2. heartbeat proves recent authenticated contact only;
3. capability and resource snapshots are immutable, expiring and generation-bound;
4. Capability Definition, Claim, Verification, Availability and Snapshot remain separate;
5. Facility, Facility Revision and Facility Instance remain implementation-neutral;
6. Provider, Provider Revision and Provider Instance/generation remain separate;
7. lifecycle, reachability, readiness, health and pressure remain separate;
8. local Providers bind exact Node evidence; remote Providers bind approved remote-service evidence and never fabricate Nodes;
9. optional dependency loss degrades only affected operation/capability scope;
10. Dispatch Eligibility is immutable, operation-specific, exact-generation-bound and expiring;
11. Provider/backend/locality replacement preserves Facility identity and fences stale work/evidence.

## 0B-WP05 — Workspace, Session, checkpoint, restore and recovery

**Status:** CANDIDATE COMPLETE — downstream use approved; executable recovery conformance deferred.

Accepted candidate:

- `ptah.workspace` `0.1.0`;
- 19 schemas;
- nine namespaced lifecycle machines;
- `schemas/phase-0b/workspace/schema-catalog.v0.1.0.json`;
- `decisions/ADR-0022-WORKSPACE-SESSION-CHECKPOINT-RESTORE-RECOVERY-BOUNDARY.md`;
- `work-packages/PHASE-0B-WP05-WORKSPACE-SESSION-CHECKPOINT-RECOVERY.md`.

Active boundaries:

1. Workspace identity survives Revision, Provider, Node, Materialization, Session, client and layout changes;
2. Workspace Revision defines immutable intended configuration, not live runtime state;
3. Membership authority, Provider Binding and Materialization remain separate;
4. Materialization generation advances on create, restore, Provider/Node/backend/locality replacement or forced fencing;
5. Session identity is separate from process IDs, backend tokens, clients, panels, tabs and Attachments;
6. detaching the last client does not stop the Session or Workspace;
7. Workspace Journal/outbox/cursor supports reconstruction but never replaces Activity or source records;
8. Checkpoint Request, Component, Bundle and Verification remain separate;
9. created or hash-verified checkpoint bytes do not prove target compatibility;
10. Restore Compatibility is target-specific, component-specific and expiring;
11. restore creates new Activities, Attempts and generations;
12. `restored_runtime` does not mean application/service/data recovery;
13. Recovery Verification requires new-generation post-condition read-back;
14. uncertain non-idempotent external effects survive crash/restore until reconciled;
15. Export and Import require explicit identity, privacy, provenance and authority decisions.

## 0B-WP06 — Transfer, synchronization, conflict, backup and storage restore

**Status:** CANDIDATE COMPLETE — downstream use approved; executable transfer/backup conformance deferred.

Accepted candidate:

- `ptah.transfer` `0.1.0`;
- 18 schemas;
- seven namespaced lifecycle machines;
- `schemas/phase-0b/transfer/schema-catalog.v0.1.0.json`;
- `decisions/ADR-0023-TRANSFER-SYNC-CONFLICT-BACKUP-RESTORE-BOUNDARY.md`;
- `work-packages/PHASE-0B-WP06-TRANSFER-SYNC-CONFLICT-BACKUP.md`.

Active boundaries:

1. Transfer Request, logical Run, physical Attempts, Manifest, Progress observations and Verification remain separate;
2. resume requires matching source identity/validators, partial state, protocol, checksum/encryption/compression and current authority;
3. provider acknowledgement or byte arrival does not create accepted Content/Object/Location truth;
4. unsafe finalize/commit/delete outcomes become uncertain rather than auto-retried;
5. Sync Relationship, Cursor, Run, Conflict and Resolution remain separate;
6. cursors advance only after destination acceptance and expire on endpoint/provider-generation drift;
7. conflicts preserve all competing revisions/tombstones and resolution creates explicit history;
8. Backup Policy, Snapshot, Verification, Prune Decision, Restore Decision and Restore Run remain separate;
9. sync, replica, checkpoint, export and backup are not interchangeable;
10. encrypted or signed backup data is not proven readable without key/decryption/read-back evidence;
11. prune requires dependency, retention, legal-hold, copy/failure-domain, authorization and post-delete verification;
12. `restored_storage` does not mean Workspace/runtime/application recovery;
13. replica repair is an explicit Transfer/Activity plus Verification.

---

# Active work — 0B-WP07

## Recipe, Build, provenance, SBOM, signature and verification

WP07 must turn the frozen Build/Artifact/Provenance architecture plus WP01–WP06 into exact candidate contracts without selecting BuildKit, Dagger, ORAS, Syft, Witness, in-toto, Sigstore or any native build backend.

### Required entities and boundaries

- Build Recipe identity and immutable Recipe Revision/hash;
- detector/proposal/readiness evidence versus accepted Recipe;
- requested targets, platforms, Facilities, toolchains, environments, services, network and proof requirements;
- backend-neutral Recipe versus backend-specific Compiled Plan;
- Build Run, Step/Operation mapping and exact physical Attempts;
- output declaration versus produced Object/Artifact/Location;
- cache entry, cache-use decision, validation and reproducibility impact;
- volatile input classification;
- secret/credential access grant and cleanup evidence without raw values;
- package/file observations and SBOM document/coverage;
- attestation statement, predicate, materials/products and policy verification;
- signature, signer identity/key reference, trust root, certificate and transparency evidence;
- online, private and offline verification paths;
- Build completion versus export, SBOM, attestation, signing, review, reproduction and release acceptance;
- independent Reproduction Run and byte-identical versus functional-equivalence Comparison;
- provenance graph relationships and backend aliases;
- partial failure, migration, compatibility and backend replacement.

### Core questions WP07 must resolve

1. Recipe identity versus proposal, configuration revision and compiled backend plan;
2. Recipe/Plan/Protocol/Run separation;
3. Build Run versus Activity/Operation/Attempt identity;
4. exact input/material resolution and mutable source aliases;
5. cache hit versus executed work and proof;
6. deterministic cache identity versus declared volatile inputs;
7. secret access versus output/cache/provenance contamination;
8. output Object creation versus Artifact promotion/release;
9. SBOM inventory claim versus completeness, vulnerability, licence or runtime-use claims;
10. attestation production versus policy verification;
11. signature validity versus functional correctness/release acceptance;
12. public transparency privacy versus private/offline signing;
13. same-backend cache reuse versus independent reproduction;
14. byte-identical versus functionally equivalent reproduction;
15. successful build with failed export/proof/signing retaining honest partial state;
16. BuildKit/Dagger/native/backend replacement without changing public Recipe/Artifact identity.

### Minimum proof cases

- one accepted Recipe compiles to two compatible backend plans without changing Recipe identity;
- unsupported or altered Recipe capabilities remain explicit;
- parallel steps retain exact dependency and Activity/Operation/Attempt mapping;
- cache reuse is accepted only when input/toolchain/policy identity matches;
- volatile output-affecting input lowers reproducibility trust;
- raw secrets are absent from recipes, logs, caches, SBOMs, attestations and public outputs;
- every output is registered as immutable Object and optional promoted Artifact;
- mutable OCI tag movement does not change digest-bound Artifact identity;
- SBOM records exact subject, generator revision and coverage limitations;
- attestation verification uses exact policy/trust inputs and remains separate from creation;
- signature verification proves digest binding/identity only;
- offline bundle verification works without transparency-network access where policy permits;
- proof/signing failure after successful build retains outputs and partial state;
- independent reproduction uses a distinct accepted environment and classifies differences;
- backend replacement preserves public Recipe, Object, Artifact and provenance identity.

### Required outputs

- normative Recipe/Build/Provenance conventions;
- entity-kind and proof-level supplements where required;
- candidate schemas and local catalog;
- namespaced lifecycle state machines;
- migration/compatibility record;
- positive/negative fixtures;
- consolidated safety net;
- WP07 work-package record and ADR-0024 if review accepts the boundary.

---

# Ordered Phase 0B sequence

1. 0B-WP01 — common identity/versioning/typed families. **CANDIDATE COMPLETE**
2. 0B-WP02 — Activity/Operation/Attempt/Event/Receipt/proof. **CANDIDATE COMPLETE**
3. 0B-WP03 — Object/Revision/View/Artifact/storage. **CANDIDATE COMPLETE**
4. 0B-WP04 — Node/Facility/Provider/capability/health. **CANDIDATE COMPLETE**
5. 0B-WP05 — Workspace/Session/checkpoint/recovery. **CANDIDATE COMPLETE**
6. 0B-WP06 — transfer/sync/conflict/backup. **CANDIDATE COMPLETE**
7. 0B-WP07 — Recipe/Build/provenance/SBOM/signature/verification. **ACTIVE**
8. 0B-WP08 — Domain Pack/firmware/disk/Device.
9. 0B-WP09 — Application/Browser/semantic UI/Shell.
10. 0B-WP10 — knowledge/data/Package/Plugin.
11. 0B-WP11 — isolation/placement/reservation/lease/secure grants.
12. 0B-WP12 — security/Finding/Claim/Evidence/reproduction.
13. 0B-WP13 — migrations and executable conformance harness.
14. 0B-WP14 — golden/negative corpus and proof-plan freeze.
15. Phase 0B review/freeze and Phase 0C readiness decision.

---

# Parked/restricted items

The Phase 0A parked/restricted items remain non-blocking with recorded reopening criteria, including `.P5C`, shared POSIX filesystems, MiniRouter licence, Dify modified licence, Ponytail/non-GNOME Wayland completion, unaudited private device source, prototype repositories without clear licences/proof, missing `amertoglu16` source and the final public Ptah project licence.

---

# No-build boundary

Allowed now:

- contracts, schemas and state machines;
- migration/compatibility design;
- conformance and lawful fixture design;
- proof plans and public/private export boundaries.

Not allowed yet:

- runtime or UI implementation;
- donor-source reuse;
- production dependency/backend selection;
- deployment of Nodes, Providers, Workspaces, build workers, registries or signing infrastructure;
- presenting candidate contracts as built or proven.

Implementation begins only after Phase 0C approval is recorded here.

---

# Chat continuation instruction

Read this file first, then:

1. `decisions/ADR-0023-TRANSFER-SYNC-CONFLICT-BACKUP-RESTORE-BOUNDARY.md`;
2. `work-packages/PHASE-0B-WP06-TRANSFER-SYNC-CONFLICT-BACKUP.md`;
3. `schemas/phase-0b/transfer/schema-catalog.v0.1.0.json`;
4. `decisions/ADR-0005-BUILD-ARTIFACT-PROVENANCE-BOUNDARY.md`;
5. `work-packages/PHASE-0A-WP03-BUILD-ARTIFACT-PROVENANCE.md`;
6. `internal/SOFTWARE-BUILDER.md`;
7. `donors/BUILDKIT.md`, `donors/DAGGER.md`, `donors/ORAS.md`, `donors/WITNESS.md`, `donors/IN-TOTO.md`, `donors/SIGSTORE-COSIGN-REKOR-FULCIO.md`, `donors/SYFT.md`;
8. `decisions/ADR-0018-COMMON-IDENTITY-VERSIONING-TYPED-FAMILY-BOUNDARY.md` through `decisions/ADR-0023-TRANSFER-SYNC-CONFLICT-BACKUP-RESTORE-BOUNDARY.md`;
9. `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `REQUIREMENT_CLOSURE_MATRIX.md`.

Do not restart donor research or implementation from conversational memory.
