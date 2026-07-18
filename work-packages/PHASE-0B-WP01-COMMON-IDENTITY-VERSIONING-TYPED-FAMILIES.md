# Phase 0B — WP01 Common Identity, Versioning and Typed Families

**Status:** CANDIDATE COMPLETE — READY FOR WP02 DEPENDENCY USE; NOT IMPLEMENTATION-FROZEN  
**Date:** 2026-07-18  
**Common contract candidate:** `ptah.common` `0.1.0`  
**Implementation:** NOT STARTED

## Purpose

Turn the Phase 0A cross-requirement normalization rules into one concrete common contract layer before Activity, Object, Node, Workspace and other domain schemas are designed.

This work package prevents later domains from inventing incompatible meanings for IDs, Providers, Sessions, Leases, Events, revisions, state, migrations, privacy or deletion.

---

# 1. Inputs

- `decisions/ADR-0017-PHASE-0A-FREEZE-PHASE-0B-ENTRY.md`
- `work-packages/PHASE-0A-CROSS-REQUIREMENT-CONSISTENCY-REVIEW.md`
- `work-packages/PHASE-0B-ENTRY-CONTRACT-PROOF-INPUTS.md`
- ADR-0001 through ADR-0016
- `MASTER_ROADMAP.md`
- `CURRENT_STATE.md`
- `REQUIREMENT_CLOSURE_MATRIX.md`

External standards selected for the candidate:

- RFC 9562 UUID version 7;
- JSON Schema Draft 2020-12;
- Semantic Versioning 2.0.0 syntax.

---

# 2. Outputs committed

## Normative conventions

- `contracts/PHASE-0B-COMMON-CONTRACT-CONVENTIONS.md`
- `contracts/PHASE-0B-ENTITY-KIND-REGISTRY.md`
- `contracts/PHASE-0B-IDENTITY-KIND-REGISTRY.md`

## Machine-readable candidate schemas

- `schemas/phase-0b/common/definitions.v0.1.0.schema.json`
- `schemas/phase-0b/common/entity-envelope.v0.1.0.schema.json`
- `schemas/phase-0b/common/state-machine-definition.v0.1.0.schema.json`
- `schemas/phase-0b/common/state-transition.v0.1.0.schema.json`
- `schemas/phase-0b/common/typed-family-definition.v0.1.0.schema.json`
- `schemas/phase-0b/common/migration-definition.v0.1.0.schema.json`
- `schemas/phase-0b/common/migration-run.v0.1.0.schema.json`
- `schemas/phase-0b/common/compatibility-record.v0.1.0.schema.json`
- `schemas/phase-0b/common/schema-catalog.v0.1.0.json`

## Safety net and fixtures

- `conformance/PHASE-0B-WP01-COMMON-CONTRACT-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp01/common-contract-cases.v0.1.0.json`

---

# 3. Accepted candidate decisions

## 3.1 Canonical IDs

New canonical Ptah entities use:

```text
entity_id    lowercase UUIDv7
entity_kind  controlled registry token
```

The UUID is opaque. Its time bits are never authoritative creation time or authorization/routing data.

Imported backend/legacy IDs become scoped Aliases. They never become canonical automatically.

Public exports may remap IDs under a restricted lineage record when correlation/time leakage is unsafe.

## 3.2 Entity kind registry

`entity_kind` uses immutable versioned tokens:

```text
<namespace>.<name>
```

The initial registry covers Core, Object/Artifact, runtime, storage, Build/provenance, Domain Packs, firmware/disk, Devices, Applications/semantic UI, Browser, Shell, knowledge/data, Package/Plugin, security/proof, documentation and identity/authority entities.

A token identifies semantics—not a database table, route, class name or donor type.

## 3.3 Schema identity

Candidate schema IDs are absolute URNs:

```text
urn:ptah:schema:<namespace>:<name>:<semver>
```

The local schema catalog resolves them without network access.

Frozen schema bytes will later require digests/signatures/provenance. Candidate catalog entries intentionally omit frozen-byte claims.

## 3.4 JSON Schema composition

The common Entity Envelope is a nested object in domain records:

```json
{
  "envelope": {
    "entity_id": "...",
    "entity_kind": "...",
    "schema_id": "...",
    "schema_version": "..."
  },
  "domain_field": "..."
}
```

Domain schemas reference the envelope under the `envelope` property and close their own top-level shape.

They do **not** inherit the envelope as a root `allOf` base whose `additionalProperties` rules would prevent domain fields.

## 3.5 Record revision

`record_revision` is a positive monotonic optimistic-concurrency revision of one entity projection.

It is not an Object Revision, schema version, Provider/Node/workload generation or connection epoch.

## 3.6 Typed families

Provider, Session, Lease, Event, Revision, Snapshot, Recipe, Protocol, Evidence, Relationship, Location and Capability are families.

Every instance declares:

```text
family_name
kind
family_contract_version
```

Kinds define authority, capability, required fields, generations and state machine.

A kind cannot silently grant another kind's authority.

## 3.7 State machines

There is no global `status` enum.

Every mutable entity has a namespaced/versioned state machine and append-only transition history.

State dimensions such as Activity lifecycle, Provider health, connection, verification, review and acceptance remain separate.

`completed`, `verified` and `accepted` cannot imply one another.

## 3.8 Revision, Snapshot, Generation, Epoch and Checkpoint

- Revision: immutable historical version.
- Snapshot: captured/observed state, possibly partial.
- Generation: runtime incarnation that fences stale references.
- Connection epoch: transport/reconnection incarnation.
- Checkpoint: state intentionally prepared for recovery.

Checkpoint production, integrity, restore, application recovery and post-condition verification remain different proof levels.

## 3.9 Identity and authority

Canonical identity entities include Principal, Organization, Group, Role, Policy, Permission Grant, Approval, Credential Reference, Trust Anchor and Authentication Session.

Emails, usernames, OAuth subjects, OS UIDs and provider account IDs remain Aliases.

Authentication, authorization, technical capability and organizational acceptance remain separate.

## 3.10 Privacy and export

Every exportable record declares privacy, audience, redaction and retention metadata.

Public publication is explicit. Credentials remain opaque references. Public Views do not mutate restricted source records.

## 3.11 Extensions

Canonical objects are closed by default. Extensibility uses namespaced `extensions` entries with their own schema ID/version.

Unknown extensions may be preserved but are not trusted or executed.

## 3.12 Migration

Migration is a versioned Activity/Operation/Attempt with a Migration Definition and Migration Run.

Frozen history is not rewritten. Output records link to sources through migration/supersession relationships. Loss/default/coercion/unknown fields are explicit.

## 3.13 Compatibility

Compatibility is directional:

- read;
- write;
- round trip.

SemVer does not prove compatibility. The compatibility record and conformance evidence are authoritative.

## 3.14 Tombstone and deletion

Tombstone preserves identity, reason, authority, policy and historical relationships.

Physical byte deletion is a separate receipted Activity subject to retention and shared-reference policy. Backend cascade deletion cannot define canonical lifecycle.

---

# 4. Review findings and corrections made

## Absolute schema references

Initial Entity Envelope references used repository-relative paths while the schema base ID was an opaque URN. This was corrected before downstream schemas: every `$ref` now uses the absolute definitions URN and the local catalog supplies resolution.

## Authority identity gap

The first entity registry did not explicitly include Principals, Organizations, Policies, Grants, Credentials and Approvals. The `identity` namespace supplement closes that gap.

## Root-schema composition risk

A closed root envelope would conflict with domain fields under `allOf`. The accepted composition is nested `envelope`, avoiding ambiguous unevaluated-property behavior across implementations.

## JSON Schema versus semantic conformance

JSON Schema cannot prove:

- entity kind is registered;
- ID/kind target matches storage truth;
- state names/transitions reference declared states uniquely;
- timestamp ordering;
- schema ID/version fields agree;
- generation/epoch is current;
- migration is truly idempotent/lossless;
- authorization is valid;
- privacy export is permitted.

These remain explicit semantic tests in the consolidated safety net and later executable harness.

---

# 5. Known candidate limitations

1. Schema files are candidate `0.1.0`, not frozen implementation contracts.
2. No executable JSON Schema validator/conformance harness is committed yet.
3. Candidate schema bytes do not yet carry frozen content digests/signatures.
4. JSON Schema `format` enforcement varies by validator; the conformance harness must enable/check it explicitly.
5. Entity-kind uniqueness and registry membership require semantic validation.
6. State/transition uniqueness and graph correctness require semantic validation.
7. Version-constraint syntax in Migration Definition remains a string pending the migration-harness package.
8. Canonical hashing/signing serialization is deferred to the provenance package.
9. Public ID remapping format/lineage is defined directionally but awaits export schemas.
10. The initial registry may remove unused speculative tokens before Phase 0B freeze; frozen tokens cannot be repurposed afterward.
11. Timestamp precision and canonical serialization details require a later cross-language interoperability decision.
12. No database/storage layout is selected.

None of these blocks WP02 schema design because the semantic boundaries are explicit.

---

# 6. Consolidated safety net

The safety-net specification includes structural and semantic cases for:

- schema catalog/URN resolution;
- UUIDv7 identity and public remapping;
- entity-kind registry;
- envelope scope/audience/extensions;
- revisions/generations/epochs;
- Alias conflicts/reuse;
- typed Lease/Provider/authority boundaries;
- state transitions/reconstruction;
- Snapshot versus Checkpoint;
- migration and compatibility;
- privacy/redaction/export;
- tombstone/referential integrity/deletion;
- typed failure outcomes.

The future executable suite must retain exact failed cases and produce a hashed/signable conformance report Artifact.

---

# 7. Candidate completion gate

This work package is candidate-complete because:

- the common vocabulary is explicit;
- every frozen Phase 0A normalization rule has a contract representation;
- machine-readable schemas exist for the shared records;
- a local schema catalog exists;
- positive/negative fixtures exist;
- structural versus semantic validation gaps are named;
- downstream work can reference one common candidate version;
- no implementation/dependency choice was made.

It is **not implementation-frozen** until the Phase 0B migration/conformance harness and golden/negative corpus execute the safety net.

---

# 8. Handoff to 0B-WP02

0B-WP02 must define:

- Activity;
- Activity dependency edge;
- Operation;
- Attempt;
- Event envelope/domain payload registration;
- idempotency and correlation nonces;
- Receipt and proof level;
- Review/Verdict and external authoritative result references;
- retry, pause, cancellation, recovery and reconnect behavior;
- initial `activity.lifecycle` state machine.

Every WP02 schema must:

- embed `common.entity-envelope` `0.1.0`;
- use registered entity kinds;
- use absolute schema URNs/local catalog;
- distinguish record revision, generation and epoch;
- define authority/privacy/retention;
- add compatibility/migration direction;
- add positive and negative fixtures to the common safety net.

No runtime implementation is authorized by completion of WP01.
