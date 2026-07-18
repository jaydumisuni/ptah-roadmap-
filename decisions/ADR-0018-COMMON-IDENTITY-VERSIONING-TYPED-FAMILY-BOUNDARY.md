# ADR-0018 — Common Identity, Versioning and Typed-Family Boundary

**Status:** ACCEPTED FOR PHASE 0B CANDIDATE CONTRACT USE  
**Date:** 2026-07-18  
**Contract candidate:** `ptah.common` `0.1.0`  
**Implementation authorization:** NONE

## Context

Phase 0A deliberately kept several words broad across domains: Provider, Session, Lease, Event, Revision, Snapshot, Recipe, Protocol, Evidence and Relationship.

Without one shared contract layer, later schemas could accidentally:

- use backend IDs as canonical identity;
- create one ambiguous global `status` enum;
- confuse record revision with Object Revision or runtime generation;
- treat a Snapshot as restorable Checkpoint;
- grant cross-kind Lease authority;
- infer compatibility from SemVer alone;
- mutate frozen history during migration;
- expose restricted identifiers/data through exports;
- rely on backend cascade deletion;
- produce schema `$ref` behavior that varies by resolver.

0B-WP01 produced normative conventions, initial registries, candidate JSON schemas, a local schema catalog, positive/negative fixtures and a consolidated safety-net specification.

## Decision

### 1. Canonical entity identity

New canonical Ptah entities use:

```text
entity_id    lowercase UUID version 7
entity_kind  controlled versioned registry token
```

The ID is opaque. UUID time bits are not authoritative creation time, authority, routing or state.

Backend/legacy identifiers are scoped Aliases. Public exports may use remapped handles under restricted lineage.

### 2. Entity kind

`entity_kind` uses immutable tokens:

```text
<namespace>.<name>
```

Frozen tokens are never silently repurposed. Renames require new tokens and migration/supersession records.

### 3. Machine-readable schema baseline

Phase 0B candidate JSON contracts use JSON Schema Draft 2020-12.

Canonical schema IDs use absolute URNs:

```text
urn:ptah:schema:<namespace>:<name>:<semver>
```

A local schema catalog resolves URNs without requiring network access. Frozen schema bytes later require digest/provenance binding.

### 4. Contract versioning

Schema, state-machine, protocol and migration versions use Semantic Versioning 2.0.0 syntax.

Compatibility remains an explicit directional record for read, write and round-trip behavior. SemVer alone never proves compatibility.

Frozen schemas are immutable. Changes create new versions and migration/compatibility records.

### 5. Common Entity Envelope

Every domain entity embeds a nested common `envelope` object.

Domain schemas do not inherit a closed envelope as the root through `allOf`; each domain schema closes its own top-level shape while referencing the nested envelope.

The envelope carries canonical identity, schema/version, record revision, timestamps, scope, authority, privacy, audience, redaction, retention, supersession/migration/tombstone and extensions.

### 6. Record revision

`record_revision` is one entity projection's optimistic-concurrency revision.

It is distinct from:

- Object/source Revision;
- schema version;
- Node generation;
- Provider generation;
- workload generation;
- connection epoch.

### 7. Typed families

Provider, Session, Lease, Event, Revision, Snapshot, Recipe, Protocol, Evidence, Relationship, Location and Capability are typed families.

Each instance declares family name, kind and family-contract version. Kind defines authority, capability scope, schema, state machine, privacy and generation requirements.

Cross-kind authority is forbidden unless an explicit adapter/parent grant contract permits it.

### 8. Namespaced state machines

There is no global Ptah `status` enum.

Every mutable entity has a namespaced/versioned state machine and append-only transition records.

Lifecycle, health, connection, availability, verification, review, acceptance, reservation, lease, Finding and reproduction states remain separate dimensions.

`completed`, `verified` and `accepted` never imply one another.

### 9. Revision, Snapshot, Generation, Epoch and Checkpoint

These concepts remain distinct:

- Revision: immutable historical version;
- Snapshot: observed/captured state;
- Generation: runtime incarnation that fences stale references;
- Connection epoch: transport/reconnection incarnation;
- Checkpoint: prepared recovery state.

Checkpoint produced, integrity verified, restore accepted, restored, application recovered and post-condition verified remain different proof levels.

### 10. Identity and authority entities

Ptah defines canonical Principal, Organization, Group, Role, Policy, Permission Grant, Approval, Credential Reference, Trust Anchor and Authentication Session entities.

Emails, usernames, OAuth subjects, UIDs and provider account IDs remain Aliases.

Authentication, authorization, capability and organizational acceptance remain separate.

### 11. Privacy and extensions

Every exportable record declares privacy, audience, redaction and retention metadata.

Canonical objects are closed by default. Extensions use namespaced entries with their own schema/version. Unknown extensions may be preserved but are not trusted or executed.

### 12. Migration and compatibility

Migration is a versioned Activity/Operation/Attempt with explicit definition and run records.

Frozen history is not rewritten. Output links to input through migration/supersession relationships. Loss, defaults, coercion, unsupported content and uncertainty are explicit.

Compatibility is directional and evidence-backed. Unknown compatibility blocks unsafe writes/mutations.

### 13. Tombstone and deletion

Tombstones preserve identity, reason, authority, policy and historical relationships.

Physical byte deletion is a separate receipted Activity subject to retention/shared-reference policy. Backend cascade deletion cannot define canonical Ptah lifecycle.

### 14. Structural versus semantic validation

JSON Schema validates structure but does not prove registry membership, identity target matching, current generation/epoch, allowed transition graph, authorization, migration correctness or privacy export permission.

Those invariants belong to the common conformance safety net and later executable harness.

## Candidate artifacts

- `contracts/PHASE-0B-COMMON-CONTRACT-CONVENTIONS.md`
- `contracts/PHASE-0B-ENTITY-KIND-REGISTRY.md`
- `contracts/PHASE-0B-IDENTITY-KIND-REGISTRY.md`
- `schemas/phase-0b/common/`
- `conformance/PHASE-0B-WP01-COMMON-CONTRACT-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp01/common-contract-cases.v0.1.0.json`
- `work-packages/PHASE-0B-WP01-COMMON-IDENTITY-VERSIONING-TYPED-FAMILIES.md`

## Consequences

### Positive

- Every later schema starts from one identity/versioning language.
- Backend IDs cannot silently become canonical.
- State/proof/acceptance confusion is structurally constrained.
- Runtime generations and transport epochs can fence stale work.
- Migration/deletion/privacy behavior is part of contracts from the start.
- Offline/local schema resolution does not depend on a website.
- Future public schema publication can map the same URNs to verified bytes.

### Costs

- Records carry explicit envelope and typed references.
- Schema catalogs and compatibility matrices must be maintained.
- State transitions and migrations require append-only evidence.
- Semantic conformance requires more than JSON validation.
- Public export/remapping needs explicit lineage handling.

## Rejected alternatives

### Random/untyped string IDs

Rejected. They invite collisions, alias confusion and inconsistent validation.

### Donor/backend IDs as canonical IDs

Rejected. They are provider-local, mutable/reusable or externally controlled.

### One global `status` field

Rejected. Lifecycle, health, verification, review and acceptance have different authority and evidence.

### One universal Session/Lease/Provider schema without kind

Rejected. It would allow authority/capability confusion.

### Schema version inferred from repository commit

Rejected. Persisted/exported records require explicit contract identity independent of Git history.

### Relative schema references from URN base IDs

Rejected. Resolution can vary or fail; absolute URNs and local catalogs are explicit.

### In-place migration of frozen history

Rejected. It destroys evidence and rollback/audit ability.

### SemVer as automatic compatibility proof

Rejected. Compatibility is directional and use-case-specific.

### Physical deletion through database cascade

Rejected. Retention, shared references and proof require explicit lifecycle operations.

## Status and next work

The common contract set is accepted as Phase 0B candidate `0.1.0` and may be used by downstream schema work.

It is not frozen for implementation until the executable migration/conformance harness and golden/negative corpus prove it before Phase 0C.

Next active work package:

- 0B-WP02 — Activity, Operation, Attempt, Event, Receipt and proof.

No runtime implementation is authorized by this ADR.
