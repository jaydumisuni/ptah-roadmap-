# Ptah Phase 0B — Common Contract Conventions

**Contract set:** `ptah.common`  
**Candidate version:** `0.1.0`  
**Status:** CANDIDATE — normative input for 0B-WP01 review  
**Date:** 2026-07-18  
**Implementation:** NOT STARTED

## Purpose

Define the common identity, versioning, reference, state-machine, migration, privacy and extension rules that every later Ptah schema must reuse.

This document is normative for Phase 0B contract design. Domain schemas may add fields and stricter rules but may not silently redefine these meanings.

---

# 1. Standards baseline

Ptah Phase 0B contract documents use:

- UUID version 7 as standardized by RFC 9562 for newly generated canonical entity identifiers;
- JSON Schema Draft 2020-12 for machine-readable JSON contract schemas;
- Semantic Versioning 2.0.0 syntax for schema, state-machine and protocol versions;
- RFC 3339-compatible `date-time` strings, normalized to UTC `Z`, for serialized timestamps;
- lowercase ASCII registry tokens and lowercase canonical UUID text.

References:

- https://www.rfc-editor.org/rfc/rfc9562.html
- https://json-schema.org/draft/2020-12/schema
- https://semver.org/spec/v2.0.0.html

A standard or version label does not itself prove interoperability. Ptah compatibility matrices and conformance tests remain authoritative.

---

# 2. Canonical entity identity

## 2.1 Canonical ID

Every newly created canonical Ptah entity receives:

```text
entity_id      UUIDv7, lowercase canonical text
entity_kind    controlled registry token
```

Example:

```json
{
  "entity_id": "019bd54a-7c32-7d6d-934e-3e56bb42ca11",
  "entity_kind": "core.activity"
}
```

`entity_id` is opaque. Consumers must not derive authority, routing, Workspace, owner, current state or truth from its timestamp/order bits.

UUIDv7's embedded time component is useful for local generation and index locality but is not an authoritative `created_at` timestamp. IDs can be generated offline, clocks can drift, and imported entities may retain older identity.

## 2.2 Entity kind

`entity_kind` is a versioned registry token using:

```text
<namespace>.<name>
```

Pattern:

```regex
^[a-z][a-z0-9]*(?:\.[a-z][a-z0-9_-]*)+$
```

Examples:

```text
core.workspace
core.activity
core.operation
object.object
object.artifact
runtime.provider
runtime.session
runtime.lease
security.finding
proof.receipt
```

Entity kind is not inferred from an ID prefix or database table.

## 2.3 Canonical URI

A transport/display URI may be derived from the pair:

```text
ptah://entities/<entity_kind>/<entity_id>
```

Example:

```text
ptah://entities/core.activity/019bd54a-7c32-7d6d-934e-3e56bb42ca11
```

The URI is a reversible representation, not a second identity. Storage/database keys may use the UUID and kind separately.

## 2.4 Imported legacy identity

Imported entities may retain a non-UUID legacy identifier only as an Alias. A new Ptah canonical ID is assigned unless a frozen migration decision explicitly preserves a prior Ptah canonical ID.

No donor, database, provider, process, D-Bus, container, browser, scanner, GitHub, device or external service identifier becomes canonical by import alone.

## 2.5 Public identifier remapping

A public export may replace internal entity IDs with public export handles when correlation or creation-time leakage would be unsafe.

The public handle is an export alias. The restricted lineage record preserves its mapping to the canonical entity under access control.

---

# 3. Entity reference

A canonical reference contains:

```text
entity_id
entity_kind
```

Optional qualifiers include:

```text
revision_id
provider_generation
workload_generation
node_generation
connection_epoch
```

Qualifiers constrain the referenced incarnation or observation. Their omission never means “latest is safe”; the consuming contract states whether current resolution is permitted.

Example:

```json
{
  "entity_id": "019bd54a-7c32-7d6d-934e-3e56bb42ca11",
  "entity_kind": "runtime.provider",
  "provider_generation": 8
}
```

## Reference rules

1. The referenced `entity_kind` must match the target registry record.
2. Cross-Workspace references require explicit authorization.
3. Revision-qualified references never silently resolve to a newer revision.
4. Generation/epoch-qualified operations reject stale values.
5. A missing target produces a typed missing/tombstoned/unauthorized result; it is not silently recreated.
6. References do not inline mutable copies of target truth.

---

# 4. Alias and backend reference

An Alias records a non-canonical name or identifier:

```text
alias_id
subject_ref
alias_namespace
alias_value
provider_or_source_ref
valid_from
valid_until
provider_generation
connection_epoch
confidence
is_current_claim
source_evidence_refs
```

Examples:

- container ID;
- process ID;
- D-Bus name/path;
- browser target ID;
- USB serial/path;
- repository URL;
- image tag;
- external ticket/report ID;
- scanner fingerprint;
- legacy database primary key.

## Alias rules

- Aliases are scoped by namespace and source/provider.
- Aliases may be reused by an external system and therefore require time/generation scope.
- `is_current_claim` is an observation, not canonical truth.
- Alias conflicts remain visible.
- Mutable names/tags are never content identity.
- Alias deletion does not delete the canonical entity or historical evidence.

---

# 5. Schema identity and versioning

Every machine-readable schema declares:

```text
$schema
$id
x-ptah-schema-name
x-ptah-schema-version
x-ptah-maturity
```

Canonical schema identifier format:

```text
urn:ptah:schema:<namespace>:<name>:<semver>
```

Example:

```text
urn:ptah:schema:common:entity-envelope:0.1.0
```

## Maturity

Allowed maturity values:

```text
draft
candidate
frozen
deprecated
retired
```

Meaning:

- `draft`: actively incomplete; no persistence compatibility promise;
- `candidate`: complete enough for cross-contract review and fixtures;
- `frozen`: accepted for implementation/interop after the relevant phase gate;
- `deprecated`: accepted historical version with a supported migration path;
- `retired`: no longer accepted for new writes; historical reads/migration policy remains explicit.

No Phase 0B schema is `frozen` merely because its JSON file exists.

## Semantic version rules

- **MAJOR:** changes interpretation, required structure, identity semantics, state meaning or compatibility in a breaking way.
- **MINOR:** adds optional compatible capability under the declared unknown-field/enum rules and does not change existing meaning.
- **PATCH:** corrects documentation, examples or validation defects without changing accepted data meaning.

Compatibility is recorded explicitly. SemVer is not a substitute for a compatibility matrix.

Adding an enum value can be breaking for exhaustive consumers and therefore requires an explicit compatibility decision; it is not automatically MINOR.

## Frozen-schema immutability

A frozen schema file is immutable. Changes create a new schema version and migration/compatibility record. Repository history is not used as a substitute for contract versioning.

---

# 6. Entity envelope

Every canonical entity record includes an envelope with:

```text
entity_id
entity_kind
schema_id
schema_version
record_revision
created_at
updated_at
workspace_ref or declared global scope
owner_or_authority_ref
privacy_class
audience
redaction_policy
retention_policy
supersedes_ref
tombstone
extensions
```

## Record revision

`record_revision` is a monotonically increasing integer for optimistic concurrency over one logical entity projection.

It is not:

- an Object content revision;
- a Provider generation;
- a Node generation;
- a workload generation;
- a connection epoch;
- a schema version.

Updates require an expected prior `record_revision` or another explicit concurrency guard.

## Created and updated time

- `created_at` records when the canonical entity record was created.
- `updated_at` records the latest accepted projection update.
- domain observations use `occurred_at` and `observed_at` separately.
- source-owned timestamps retain source and confidence rather than overwriting Ptah timestamps.

---

# 7. Typed families

The following names represent families, not one universal entity type:

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

Every family record has:

```text
family_name
kind
family_contract_version
```

The `kind` determines required fields, authority and state machine.

## Provider kinds — initial seed

```text
workspace
process
oci_runtime
isolation_runtime
storage
transfer
build
browser
application
device
display
semantic_ui
knowledge
data
plugin_runtime
scheduler
security_scanner
reproduction
```

## Session kinds — initial seed

```text
workspace_recovery
shell
terminal
browser_process
browser_context
browser_page
device
application
display
semantic_context
```

## Lease kinds — initial seed

```text
resource_reservation
provider_execution
device_ownership
interactive_control
```

A Lease kind can never silently grant another kind's authority.

Examples:

- `resource_reservation` may reserve CPU/RAM but cannot send pointer input.
- `interactive_control` may send scoped input but cannot reserve GPU capacity.
- `device_ownership` cannot grant access to unrelated application or browser sessions.

## Snapshot kinds — initial seed

```text
node_capability
resource_pressure
semantic_ui
filesystem
container
sandbox
microvm
full_vm
knowledge_index
assessment_coverage
```

A Snapshot is an observation/capture. Restorability requires a typed Checkpoint contract and restore proof.

---

# 8. State-machine convention

There is no global Ptah `status` enum.

Every mutable entity declares a versioned state machine:

```text
state_machine_name
state_machine_version
current_state
state_sequence
```

Every state machine specification defines:

```text
allowed_states
allowed_transitions
transition_authority
preconditions
required_receipts_or_evidence
terminal_states
recovery_transitions
timeout_or_expiry_behavior
migration_mapping
```

## State namespaces

Examples:

```text
activity_state
provider_health_state
connection_state
capability_availability_state
verification_state
review_state
acceptance_state
lease_state
reservation_state
finding_state
```

`completed`, `verified` and `accepted` remain different dimensions.

## Transition record

Every accepted transition is append-only and records:

```text
transition_id
subject_ref
state_machine_name
state_machine_version
sequence
from_state
to_state
transition_reason
authority_ref
activity_operation_attempt refs
precondition_evidence_refs
receipt_refs
occurred_at
observed_at
```

The current-state field is a projection from accepted transitions.

## Transition rules

1. A transition must match the state-machine version active for the entity revision.
2. Sequence must advance monotonically.
3. Invalid transitions are retained as rejected attempts/evidence where required; they do not mutate current state.
4. A side-effecting transition requires the relevant operation/attempt and Receipt/read-back evidence.
5. UI actions cannot directly write current state.
6. Provider health loss does not automatically fail every Activity.
7. Activity completion does not imply verification or acceptance.
8. Expiry transitions identify the clock/authority that evaluated expiry.
9. Recovery creates explicit transitions rather than resetting state.

---

# 9. Revision, Snapshot, Generation and Epoch

These terms are not interchangeable.

## Revision

An immutable historical version of a logical entity, contract, source, configuration or dataset.

Examples:

- Object Revision;
- Layout Revision;
- Index Revision;
- Ruleset Revision;
- Protocol Revision.

## Snapshot

An observed/captured state at a time, possibly partial or derived.

Examples:

- Node Capability Snapshot;
- Semantic Snapshot;
- resource pressure snapshot.

## Generation

A monotonic incarnation of a runtime identity whose stale references must be rejected.

Examples:

- Node generation;
- Provider generation;
- workload generation;
- Application Session generation.

## Connection epoch

A monotonic connection/reconnection incarnation. It scopes output and asynchronous evidence to the correct transport session.

## Checkpoint

State intentionally prepared for resume/recovery. A Checkpoint can reference several snapshots or provider-native checkpoint artifacts.

Checkpoint proof levels remain separate:

```text
produced
integrity_verified
restore_accepted
restored
application_recovered
postcondition_verified
```

---

# 10. Authority and scope

Every mutable/actionable record identifies the authority domain responsible for its meaning.

Initial authority classes include:

```text
caller
workspace_owner
organization_policy
ptah_control_plane
ptah_node
provider
facility
operating_system
physical_device
external_provider
human_operator
independent_reviewer
authoritative_external_system
```

Authority rules:

- authentication is not authorization;
- capability is not permission;
- permission is not placement;
- placement is not reservation;
- reservation is not execution authority;
- UI focus is not an input-control lease;
- scanner reachability is not assessment authorization;
- signature identity is not semantic correctness;
- reviewer verdict is not caller acceptance.

---

# 11. Privacy, audience and redaction

Every exportable entity declares a privacy class:

```text
public
internal
confidential
restricted
```

Audience scopes include:

```text
private_owner
workspace
organization
named_recipients
public
```

Redaction actions include:

```text
none
mask
hash_only
omit
encrypted_reference
```

Rules:

1. `public` audience requires an explicit export/publication decision.
2. A public View never changes the restricted source record.
3. Raw credentials/secrets are not entity payloads; records contain opaque references.
4. Source snippets, security findings, HTTP exchanges, device identifiers and private model/dataset inputs inherit restrictive defaults.
5. Derived search indexes and generated documentation inherit source audience and must be leakage-tested.
6. Public ID remapping may be applied where internal correlation is sensitive.

---

# 12. Extensions and unknown fields

Canonical schema objects are closed by default with `additionalProperties: false` or `unevaluatedProperties: false`.

Extensibility uses:

```json
{
  "extensions": {
    "org.example.feature": {
      "schema_id": "urn:example:schema:feature:1.0.0",
      "value": {}
    }
  }
}
```

Extension namespace rules:

- `ptah.*` is reserved for accepted Ptah extensions;
- external namespaces use a stable reverse-domain or organization-controlled token;
- extensions cannot override canonical field meaning;
- extension values declare their schema/version;
- unknown extensions may be preserved without being trusted or executed;
- required behavior cannot be hidden only in an optional extension.

---

# 13. Relationships and referential integrity

A relationship is a first-class revisioned entity with:

```text
relationship_id
relationship_kind
source_ref
target_ref
direction
relationship_revision
valid_from
valid_until
claim_or_evidence_refs
confidence
created_by
privacy_class
tombstone
```

Rules:

- relationships never rely only on embedded copied IDs;
- detector-produced relationships remain Claims/Observations until accepted at the relevant authority level;
- conflicting relationships coexist;
- tombstoning one entity does not silently erase historical relationships;
- current projections exclude unavailable/tombstoned relationships according to contract policy;
- backend cascade deletion cannot define canonical lifecycle.

---

# 14. Tombstone, supersession and deletion

## Tombstone

A Tombstone records that an entity/revision is no longer active/available under a named policy while preserving identity and history.

Required fields include:

```text
tombstoned_at
tombstone_reason
authority_ref
policy_ref
replacement_ref
retention_until
evidence_refs
```

## Supersession

A new entity/revision may supersede an older one through an explicit relationship. Supersession does not rewrite the old record.

## Deletion

Physical byte deletion is a separate receipted Activity subject to retention, legal, shared-reference and backup policy.

A deleted byte location does not erase Object identity, provenance or historical Receipts where retention policy requires them.

---

# 15. Migration convention

Migration is a versioned Ptah Activity, not an invisible database rewrite.

A Migration Definition declares:

```text
migration_id
migration_version
source_schema_ids_or_ranges
target_schema_id
transform_tool_and_digest
preconditions
loss_policy
compatibility_class
rollback_or_reverse_migration
```

A Migration Run records:

```text
activity_operation_attempt
input_entity_ref_and_revision
source_hash
target_entity_ref_and_revision
target_hash
field_mapping_report
loss_or_default_report
validation_result
receipt_refs
supersession_relationship
```

Rules:

1. Frozen historical records are not mutated in place.
2. A migrated record links to the source through `migrated_from`/`supersedes` relationships.
3. Loss, defaults and unknown fields are explicit.
4. Pure deterministic transforms are preferred and hash-tested.
5. Side effects use separate Operations and Receipts.
6. Migration failure leaves the source valid and produces a bounded failure record.
7. Bulk migration is resumable and idempotent.
8. Export/import manifests name every included schema version and migration requirement.

---

# 16. Compatibility convention

Compatibility is directional and use-case-specific.

The compatibility matrix records:

```text
producer_schema
consumer_schema
read_compatibility
write_compatibility
round_trip_compatibility
migration_required
lossy_fields
unsupported_features
conformance_evidence
```

Compatibility states:

```text
compatible
compatible_with_ignored_extensions
compatible_with_migration
lossy
incompatible
unknown
```

`unknown` blocks unsafe mutation or automated migration.

---

# 17. Error and unsupported-result convention

Canonical operations return typed outcomes rather than ambiguous strings.

Common outcome classes:

```text
success
partial
rejected
unauthorized
forbidden
not_found
tombstoned
conflict
stale_generation
stale_revision
unsupported
invalid_contract
timeout
cancelled
provider_unavailable
inconclusive
failed
```

An outcome includes:

```text
outcome_class
stable_code
summary
subject_refs
retryability
required_action
limitations
evidence_or_receipt_refs
```

`failed`, `unsupported`, `inconclusive`, `partial` and `blocked` remain evidence-bearing states and are not flattened into empty results.

---

# 18. Serialization and canonicalization

Initial canonical interchange is JSON validated by JSON Schema 2020-12.

Rules:

- UTF-8;
- lowercase canonical UUID text;
- timestamps normalized to UTC `Z`;
- integers for sequences/generations/revisions;
- decimal/measurement values define units explicitly;
- byte content remains Objects/Artifacts, not base64 fields in ordinary records;
- field ordering is not semantically significant;
- hashing/signing uses a separately defined canonical serialization profile in a later provenance schema;
- JSON number precision is not used for identifiers or high-precision financial/scientific values without a typed string/decimal contract.

---

# 19. Conformance requirements for this common layer

A conforming implementation must prove:

1. canonical UUIDv7 IDs are generated and normalized without trusting timestamp bits as truth;
2. backend aliases cannot replace canonical IDs;
3. unknown/mismatched entity kinds are rejected;
4. stale revision, generation and connection epoch are distinguishable;
5. typed Lease kinds do not grant cross-kind authority;
6. Snapshot and Checkpoint are distinct;
7. invalid state transitions do not mutate current state;
8. transition history reconstructs current state;
9. schema compatibility is explicit rather than inferred from SemVer alone;
10. migration preserves source history and reports loss/defaults;
11. tombstones preserve identity and references;
12. privacy/audience/redaction survive export and migration;
13. unknown extensions are preserved but not trusted/executed;
14. public ID remapping does not break restricted lineage;
15. no generic global `status` enum appears in canonical domain schemas.

---

# 20. Phase 0B usage rule

Every later Phase 0B work package must:

- reference this common contract version;
- register new entity/family kinds;
- define state-machine names and versions;
- identify authoritative fields and producers;
- define aliases/generations/epochs;
- define privacy/retention/deletion behavior;
- define migrations and compatibility;
- add conformance and negative fixtures;
- state any deliberate deviation in an accepted ADR.

No runtime implementation is authorized by this convention document.
