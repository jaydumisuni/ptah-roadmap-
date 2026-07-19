# Phase 0B WP05 — Workspace, Session, Checkpoint and Recovery Conventions

**Status:** CANDIDATE DRAFT  
**Date:** 2026-07-19  
**Contract family target:** `ptah.workspace` / `ptah.session` / `ptah.checkpoint` `0.1.0`  
**Implementation authorization:** NONE

## Purpose

Define persistent Workspace identity, intended Workspace configuration, runtime materializations, typed Sessions, checkpoint bundles, restore compatibility and recovery evidence without treating one directory, container, VM, Provider, shell layout or snapshot as the Workspace itself.

This package composes WP01 common identity/versioning, WP02 Activity/Attempt/Receipt proof, WP03 Object/Artifact/storage and WP04 Node/Facility/Provider/generation/freshness contracts.

---

# 1. Required separation

Ptah keeps the following distinct:

```text
Workspace
Workspace Revision
Workspace Membership
Workspace Provider Binding
Workspace Materialization
Workspace Journal / Outbox Cursor

Session
Session Attachment
Session Control/Lease reference
Session backend alias / stream / client projection

Checkpoint Request
Checkpoint Bundle
Checkpoint Component
Checkpoint Verification
Restore Request
Restore Compatibility Decision
Restore Run
Recovery Verification

Archive
Export Bundle
Import Decision / Import Run

Activity / Operation / Attempt / Receipt
Node / Provider / generations / connection epoch
Object / Revision / Artifact / Location
Shell Layout / Panel / View state
```

No generic `workspace_status`, `session_status` or `checkpoint_status` may collapse these truth classes.

---

# 2. Workspace identity

## 2.1 Workspace

`core.workspace` is the stable persistent namespace/world boundary within which Objects, Activities, Sessions, policies, memberships and runtime materializations are related.

A Workspace is not:

- a local directory or Git worktree;
- a container, VM, sandbox or remote host;
- a Provider or Provider Instance;
- a database row owned by one vendor;
- a shell window/layout;
- a Session;
- one checkpoint or backup;
- one Node;
- one Activity.

These remain bindings, projections, aliases or referenced entities.

## 2.2 Workspace lifecycle

Durable administrative lifecycle:

```text
active
suspended
archived
retired
```

Rules:

1. Workspace lifecycle does not mirror runtime materialization state.
2. Workspace `active` may have zero running materializations.
3. Workspace `suspended` blocks new ordinary mutation/materialization under policy but preserves identity/history.
4. Workspace `archived` is retained and normally not materialized; archive does not imply physical deletion.
5. Workspace `retired` prevents ordinary reactivation unless an explicit migration/import creates a successor.
6. Provider failure, Node offline state or client detachment never automatically changes Workspace lifecycle.

## 2.3 Workspace Revision

A Workspace Revision is an immutable version of intended Workspace configuration and namespace policy.

It may retain:

- parent revision(s);
- selected source/Object revisions;
- storage/mount intent;
- Facility and Provider requirements/preferences;
- environment/configuration references;
- network, credential, device and policy requirements;
- Workspace-level settings;
- expected service/application declarations;
- migration origin and limitations.

A Workspace Revision is not live runtime state and cannot prove that any Provider applied it.

Concurrent Workspace changes from the same base create divergent revisions. Merge/resolution creates a new revision with explicit parents rather than silent last-write-wins.

---

# 3. Membership, ownership and policy

Workspace Membership is a first-class, versioned authority record containing:

```text
workspace_ref
principal_or_group_ref
role_key
capability_or_permission_scope
issued_by
issued_at
expires_at
state
policy_ref
```

Membership states:

```text
active
suspended
revoked
expired
```

Workspace ownership, membership, policy, visibility, audience and runtime control are separate.

Rules:

- account/email/display name never becomes membership identity;
- revocation does not erase historical Activities/Receipts;
- Workspace access does not automatically grant Session input/control;
- control authority remains a typed Lease/secure-grant concern and is referenced rather than duplicated here;
- exported/imported Workspaces require explicit membership/authority decisions at the destination.

---

# 4. Workspace Provider Binding

A Workspace Provider Binding states which Facility Revision and Provider Instance/Revision may materialize one Workspace Revision under exact policies.

It retains:

```text
workspace_ref
workspace_revision_ref
facility_revision_ref
provider_ref_or_revision
preferred_or_required locality/isolation
compatibility constraints
network/credential/device/Object requirements
routing/failover policy
state and evidence
```

Binding is not a running environment and does not prove current eligibility/readiness.

Binding states:

```text
declared
validated
incompatible
deprecated
revoked
```

A new Provider/backend may replace a binding without changing Workspace identity. Compatibility and migration evidence are required before materialization.

---

# 5. Workspace Materialization

A Workspace Materialization is one runtime incarnation of one exact Workspace Revision through one exact Provider Instance/generation and, for local Providers, Node generation.

```text
materialization_id
workspace_ref
workspace_revision_ref
materialization_generation
facility_revision_ref
provider_instance_ref
provider_generation
connection_epoch
node_ref_and_generation_or_remote_service_ref
started_activity/attempt/receipts
mounted Object/Revision/Location refs
runtime process/service/session refs
lifecycle
readiness/health projections
created_at
stopped_at
```

## 5.1 Materialization generation

`materialization_generation` advances whenever prior runtime authority/state must be fenced, including:

- fresh create/start after stopped/destroyed materialization;
- restore from checkpoint;
- Provider Instance/generation replacement;
- Node migration/replacement;
- backend/locality replacement;
- forced reconciliation after uncertain runtime state.

Reconnect of a client or shell does not advance materialization generation.

## 5.2 Materialization lifecycle

```text
provisioning
starting
running
pausing
paused
resuming
stopping
stopped
restoring
archiving
destroying
destroyed
failed
quarantined
```

Rules:

1. lifecycle is separate from Provider readiness/health and Workspace lifecycle;
2. `running` means the incarnation exists, not that all declared services/applications are recovered;
3. `paused` is supported only when the Provider proves it;
4. `failed` requires correlated exact-generation evidence and reconciliation;
5. `quarantined` blocks ordinary new work while permitting narrow investigation/cleanup;
6. `destroyed` removes runtime incarnation, not Workspace identity, Objects or history.

---

# 6. Session typed family

`runtime.session` is the common stable root for one scoped runtime or presentation relationship.

Session kinds include:

```text
workspace
process
pty
shell
browser
application
device
display
semantic_ui
filesystem_mount
service
other_registered
```

A subtype with existing independently registered entity kind may use that kind while still declaring its Session family/kind.

## 6.1 Session identity

A Session binds:

- exact Workspace and Materialization generation where applicable;
- exact Provider Instance/generation and connection epoch;
- subtype-specific subject references;
- owner/caller and policy;
- lifecycle;
- attachment/control references;
- stream and backend aliases;
- checkpoint support/limitations.

A Session is not a client connection, browser tab, panel, process ID, PTY file descriptor, Device interface, Window handle or backend session token. Those remain child entities or aliases.

## 6.2 Session lifecycle

Neutral family lifecycle:

```text
creating
active
idle
suspending
suspended
resuming
closing
closed
failed
quarantined
```

Subtype state machines may add stricter states but must map explicitly and may not weaken proof requirements.

## 6.3 Attachment

Session Attachment is a separate time-bounded relationship between a Session and a human, automation, service or client projection.

Attachment states:

```text
attaching
attached
detached
expired
revoked
```

Rules:

- detaching a client does not stop the Session or Workspace;
- several observers may attach while one scoped control Lease holder may mutate/input;
- stale connection epochs/fencing tokens are rejected;
- Shell Session and Panel state remain presentation projections, not runtime Session truth;
- closing a panel or browser window does not close the underlying Session unless an explicit Activity does so.

---

# 7. Journal, outbox and reconciliation

A Workspace Journal records durable Workspace-scoped changes/references needed to reconstruct projections.

An outbox records pending delivery/synchronization intentions. Event cursors record replay position. None replaces the Activity Ledger, Object graph or source records.

Reconnect/recovery sequence:

1. authenticate current caller/Node/Provider/Session context;
2. load canonical Workspace, current Revision, Materialization and Session records;
3. compare generation/epoch/cursor state;
4. replay/reconcile durable Events and Receipts;
5. query Providers/external systems for uncertain work where required;
6. reject stale client/runtime projections;
7. create new reconciliation records and transitions rather than rewriting history.

No side effect is replayed automatically solely because a client missed an Event.

---

# 8. Checkpoint model

## 8.1 Checkpoint Request

A Checkpoint Request declares:

- exact Workspace/Materialization/Session/Activity subjects;
- requested checkpoint class/components;
- consistency target;
- quiesce/pause policy;
- inclusion/exclusion policy;
- privacy, credential and encryption policy;
- portability target;
- destination/retention;
- timeout/resource budget;
- required proof/read-back.

Request acceptance does not guarantee provider support or successful capture.

## 8.2 Checkpoint classes

```text
workspace_manifest
filesystem_or_object_snapshot
process_checkpoint
container_checkpoint
sandbox_checkpoint
microvm_snapshot
full_vm_checkpoint
application_checkpoint
browser_profile_checkpoint
device_or_emulator_checkpoint
service_data_checkpoint
composite
```

## 8.3 Consistency classes

```text
metadata_only
crash_consistent
filesystem_consistent
application_consistent
transaction_consistent
component_mixed
unknown
```

A composite bundle may contain components with different consistency classes. The bundle's overall claim cannot exceed its weakest required component or explicit mixed status.

## 8.4 Checkpoint Component

Each component retains:

- component type and required/optional role;
- source subject and exact generations/revisions;
- producing Provider/runtime revision;
- Content/Object/Artifact/Location references;
- consistency and completeness;
- compatibility requirements;
- sensitivity/credential/secret classification;
- encryption/signature/verification;
- Activity/Operation/Attempt/Receipts;
- limitations and excluded state.

## 8.5 Checkpoint Bundle

A Checkpoint Bundle is an immutable manifest over components.

Bundle states/claims remain separate:

```text
assembled
verified
restore_compatible_for_target
restored
application_recovered
```

These are not one lifecycle ladder. A bundle may be assembled and integrity-verified yet incompatible with a target or fail application recovery.

Bundle completeness:

```text
complete_for_declared_scope
partial
mixed
failed
unknown
```

Required components missing/failed prevent `complete_for_declared_scope`.

Checkpoint creation proves only that declared files/state/manifest were produced. It does not prove restore compatibility or recovery.

---

# 9. Secrets, credentials and sensitive state

Credentials remain opaque references and are not ordinary checkpoint bytes by default.

Checkpoint component classification:

```text
contains_no_secret_material
contains_encrypted_secret_material
contains_recoverable_credential_reference_only
contains_sensitive_session_state
unknown_sensitive_content
prohibited_for_export
```

Rules:

- raw credentials/tokens/keys are excluded unless a named policy explicitly permits encrypted inclusion;
- browser cookies/profiles, SSH agents, device keys, wallet/payment state and customer data are restricted;
- encryption keys remain separate credential references;
- import/restore re-authorizes and re-delivers fresh credentials where possible;
- expired/revoked credentials are never silently reactivated;
- public/export bundles apply allowlist/redaction and may omit nonportable sensitive components;
- omission must be declared and may reduce restore/recovery capability.

---

# 10. Checkpoint verification and compatibility

## 10.1 Verification

Checkpoint Verification is immutable evidence over exact bundle/components:

- manifest/schema validation;
- component digest/read-back;
- encryption/signature verification;
- required-component presence;
- consistency evidence;
- privacy/export policy checks;
- limitations.

Integrity verification does not prove restore compatibility.

## 10.2 Restore Compatibility Decision

A Restore Compatibility Decision is target-specific and time-bounded.

It evaluates:

- target Node/Provider/Facility revisions and capabilities;
- architecture, kernel, runtime, hypervisor, CPU/device/driver compatibility;
- checkpoint component type/version;
- required Object/Location availability;
- storage/network/device/credential grants;
- isolation/security policy;
- privacy/licence/location constraints;
- migration/conversion requirements;
- known unsupported/missing components.

Decisions:

```text
compatible
compatible_with_conversion
partially_compatible
incompatible
unknown
```

`partially_compatible` cannot be used for a requested full restore without explicit scope reduction/approval.

---

# 11. Restore and recovery

## 11.1 Restore Request

A Restore Request binds:

- exact Checkpoint Bundle;
- target Workspace or new Workspace intent;
- target Workspace Revision;
- target Provider/Node or placement constraints;
- restore scope/components;
- overwrite/fork/merge/import policy;
- compatibility decision;
- credential/network/device policies;
- required read-back and acceptance.

## 11.2 Restore Run

Restore is a new Activity with new Operations/Attempts, Reservation/Lease where required, Provider generation and Materialization generation.

Restore states:

```text
requested
validating
preparing
restoring
starting
verifying
partially_restored
restored_runtime
recovery_failed
cancelled
```

`restored_runtime` means the Provider/materialization exists after restore. It does not prove application/service/session recovery.

## 11.3 Recovery Verification

Recovery Verification evaluates declared postconditions, for example:

- Provider readiness;
- filesystem/Object digest checks;
- process/service inventory;
- application-defined health and data checks;
- browser/session profile state where permitted;
- Device/emulator state;
- external authoritative results;
- unresolved Operations and limitations.

Outcomes:

```text
recovered
partially_recovered
not_recovered
inconclusive
```

Old Attempts/Receipts remain historical and cannot prove restored-generation work. New read-back/Receipts are required.

## 11.4 Uncertain side effects

Crash/restore never resets uncertain external effects. Non-idempotent Operations remain `uncertain` until read-back, authoritative external result, compensation or human review resolves them.

---

# 12. Archive, export and import

## 12.1 Archive

Archive is a Workspace administrative/runtime-storage action. It may stop materializations and produce selected checkpoint/export/backup records, but it does not by itself prove portable recovery.

## 12.2 Export Bundle

An Export Bundle is an immutable allowlisted Artifact containing selected:

- Workspace and Revision manifests;
- Objects/Artifacts and verified locations or embedded bytes;
- Activities/Receipts/evidence as policy permits;
- Session/checkpoint manifests;
- source/configuration documents;
- migration/readme/limitations.

It is not live Workspace storage and does not embed private host paths or unrestricted secrets.

## 12.3 Import

Import creates an explicit decision:

```text
create_new_workspace
restore_existing_identity_under_authority
fork_workspace
merge_into_workspace
reference_only
reject
```

Rules:

- cross-installation import normally creates new local canonical IDs plus provenance/alias mapping unless an authorized identity-preserving transfer protocol applies;
- Object/Content identity may be retained when digests and privacy/deduplication scope permit;
- memberships, credentials, provider bindings and policies are re-authorized;
- backend aliases/Locations are remapped;
- imported runtime/checkpoint claims remain unverified until local checks run;
- no silent overwrite or merge.

---

# 13. Provider and backend replacement

Replacing Workspace Provider/backend:

1. preserves Workspace identity and revision history;
2. creates/selects compatible Facility/Provider revisions and binding;
3. creates a new Materialization generation;
4. advances/fences Provider/workload generations;
5. remaps runtime aliases/Locations;
6. retains old Sessions/checkpoints/evidence;
7. re-evaluates checkpoint compatibility;
8. re-runs readiness and recovery postconditions;
9. exposes unsupported/nonportable state rather than fabricating equivalence.

Workspace runtime failure does not disconnect the Node or destroy unrelated Workspaces.

---

# 14. Migration rules

Migration must not:

- derive Workspace identity from path, repository, container, VM or provider ID;
- mutate a Workspace into a Session or Materialization;
- turn a mutable runtime filesystem into an immutable Object without checkpoint/hash registration;
- treat layout/panel restoration as Session/runtime recovery;
- treat client attachment as Session existence or control authority;
- claim checkpoint completeness when required components are missing/partial;
- treat bundle integrity as restore compatibility;
- treat successful Provider start as application recovery;
- reuse old materialization/provider/workload generation after restore;
- reactivate expired/revoked credentials from checkpoint;
- silently merge imported Workspaces or memberships;
- discard unresolved Operations, negative restore evidence or nonportable limitations.

Breaking schema/state/compatibility changes require versioned migration definitions/runs and retained source records.

---

# 15. Required conformance cases

1. Workspace survives shell/client detachment and all Activities/Sessions continue according to policy.
2. several unrelated Activities and Sessions coexist in one Workspace.
3. Workspace lifecycle `active` with zero materializations is valid.
4. Provider restart/replacement creates new Provider/Materialization generation while preserving Workspace identity.
5. layout/panel restore does not claim runtime Session recovery.
6. Checkpoint Bundle cannot claim complete when a required component is partial, failed, excluded or unknown.
7. assembled/integrity-verified checkpoint may still be restore-incompatible.
8. incompatible target is rejected before mutation.
9. restored Provider/materialization still requires readiness and Recovery Verification.
10. old Attempts/Receipts cannot prove restored-generation work.
11. uncertain non-idempotent Operations survive crash/restore as unresolved.
12. secret-bearing components are excluded, encrypted or restricted under explicit policy.
13. partial restore retains component-level limitations and negative evidence.
14. export/import applies allowlist/redaction and explicit identity/provenance decisions.
15. backend replacement preserves Workspace identity while remapping bindings/materializations/aliases.
16. one Workspace failure does not stop another Workspace or disconnect the Node.
17. provider-specific unsupported checkpoint/pause/fork features are explicit.
18. local one-Node and later multi-Node recovery use the same canonical records.

---

# Do-not-break rule

> Never collapse Workspace identity, Workspace Revision, runtime Materialization, Session, client attachment, shell layout, Checkpoint Bundle, restore execution or Recovery Verification into one record or one status. Checkpoint files created, Provider started, client reconnected and layout restored are all weaker facts than verified application recovery.