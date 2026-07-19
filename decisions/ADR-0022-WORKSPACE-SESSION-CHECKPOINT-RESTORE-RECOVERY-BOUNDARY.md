# ADR-0022 — Workspace, Session, Checkpoint, Restore and Recovery Boundary

**Status:** ACCEPTED FOR PHASE 0B DOWNSTREAM CONTRACT DESIGN  
**Date:** 2026-07-19  
**Phase:** 0B-WP05  
**Implementation authorization:** NONE

## Context

Ptah must preserve persistent working-world identity while runtime environments, Providers, Nodes, Sessions, clients and layouts start, stop, fail, reconnect, checkpoint, migrate and restore.

The frozen architecture requires:

- Workspace independent of Node and Provider;
- many concurrent Activities and Sessions in one Workspace;
- shell/layout state separate from runtime truth;
- exact Provider/Node/materialization generations and stale-evidence fencing;
- immutable Objects/Artifacts/Locations and Activity/Receipt proof;
- checkpoint/restore capability varying by runtime;
- private credentials and session state handled explicitly;
- recovery proven through new-generation read-back rather than optimistic process start.

No donor or backend snapshot defines canonical Workspace, Session, checkpoint or recovery truth.

## Decision

Ptah owns distinct records for:

1. Workspace;
2. immutable Workspace Revision;
3. Workspace Membership;
4. Workspace Provider Binding;
5. Workspace Materialization and Materialization Generation;
6. Workspace Journal Entry and replay cursor references;
7. typed runtime Session;
8. Session Attachment and control-Lease reference;
9. Checkpoint Request;
10. Checkpoint Component;
11. immutable Checkpoint Bundle;
12. Checkpoint Verification;
13. Restore Request;
14. target-specific Restore Compatibility;
15. Restore Run;
16. Recovery Verification;
17. Workspace Export;
18. Workspace Import Decision.

Backend paths, repository refs, container/VM IDs, process IDs, browser targets, PTY descriptors, client tokens, panel/layout IDs and snapshot filenames remain aliases or references.

## Workspace boundary

Workspace is stable persistent namespace/world identity. It may remain `active` with no Materialization and survives Provider, Node, Session, client and layout changes.

Workspace lifecycle is administrative:

```text
active
suspended
archived
retired
```

Provider failure, Node offline state, client detach or layout close never automatically changes Workspace lifecycle.

Workspace Revision is immutable intended configuration/policy. It is not live filesystem/runtime state. Divergent revisions remain separate until an explicit merge revision exists.

## Membership and authority

Workspace Membership is scoped, issued authority. It does not automatically grant Session input/control. Revocation/expiry fences current grants/attachments according to policy while preserving history.

Imported membership/authority requires destination re-authorization.

## Provider binding and Materialization

Workspace Provider Binding expresses compatibility/policy intent and remains separate from running state.

Workspace Materialization is one runtime incarnation of one exact Workspace Revision through one exact Provider Instance/generation and one truthful locality.

Materialization Generation advances on fresh create, restore, Provider/Node/backend/locality replacement or forced fencing. Client/shell reconnect does not advance it.

Materialization `running` proves runtime existence only. Provider readiness, declared application/service recovery and caller acceptance remain separate.

Destroying one Materialization does not destroy Workspace identity, Objects, Activities or history.

## Session and attachment

`runtime.session` is a typed family root for Workspace/process/PTY/shell/browser/application/device/display/semantic/filesystem/service Sessions.

Session identity is not a client connection, process ID, backend token, tab, panel, Window handle or Device interface.

Session Attachment is separate and time-bounded. Detaching the last client does not close the Session or Workspace. Observer attachment and mutation/control authority remain separate; control uses typed Lease/fencing references.

Shell layout/panel/view restoration is presentation only and never proves runtime Session recovery.

## Journal and reconnect

Workspace Journal/outbox/cursor supports reconstruction but never replaces Activity Ledger or source records.

Reconnect verifies canonical identities, generations, epochs and cursor state; stale projections are rejected. Missed Events never authorize automatic replay of a side effect. Uncertain work is reconciled through WP02 Receipts and authoritative read-back.

## Checkpoint boundary

Checkpoint Request, Component, Bundle and Verification remain separate.

Each Component records exact source subjects/generations, producing Provider revision/generation, consistency, completeness, portability, sensitivity, output Objects/Artifacts/Locations and Receipts.

Checkpoint Bundle is immutable manifest over Components.

Required missing/failed/unknown/excluded Components prevent `complete_for_declared_scope`. Mixed consistency remains mixed. Creation or integrity verification does not prove restore compatibility.

## Privacy and credentials

Raw credentials/tokens/keys are excluded by default. Sensitive state is omitted, encrypted under explicit policy or retained as restricted references. Encryption keys remain separate.

Restore/import re-authorizes and re-delivers fresh credential references where possible. Expired/revoked credentials are never reactivated from checkpoint bytes.

Public/export bundles are allowlisted/redacted and declare omissions/nonportable state and recovery impact.

## Restore compatibility

Restore Compatibility is target-specific, component-specific and time-bounded.

- incompatible or unknown target is rejected before mutation;
- partial compatibility requires explicit reduced-scope approval;
- local restore requires current Node/generation/capability/resource evidence;
- remote restore requires approved remote-service/Provider evidence without fictional Node records;
- generation, runtime, policy, grant or dependency changes expire prior compatibility;
- required conversion is explicit and not assumed lossless.

## Restore and recovery

Restore is a new Activity with new Operations/Attempts and new Provider/materialization/workload generations.

`restored_runtime` means the target runtime/materialization exists. It does not mean application/service/session/data state recovered.

Recovery Verification uses new-generation postconditions/read-back and yields:

```text
recovered
partially_recovered
not_recovered
inconclusive
```

`recovered` requires all required postconditions pass and no required unresolved Operations remain.

Old Attempts/Receipts cannot prove restored-generation work. Crash/restore never clears uncertain non-idempotent external effects; authoritative read-back, compensation or review is required.

## Archive, export and import

Archive is administrative/runtime-storage handling, not portable recovery proof.

Workspace Export is immutable allowlisted Artifact/View containing selected records, hashes, provenance, privacy policy and omissions.

Import requires explicit decision:

```text
create_new_workspace
restore_existing_identity_under_authority
fork_workspace
merge_into_workspace
reference_only
reject
```

Cross-installation imports normally create new local canonical IDs plus provenance/alias mapping unless authorized identity-preserving transfer exists. Memberships, credentials, policies, bindings and Locations are re-authorized/remapped. Silent overwrite/merge is forbidden.

## Schema and conformance decision

Accepted candidate package:

- 19 schemas in `schemas/phase-0b/workspace/schema-catalog.v0.1.0.json`;
- nine namespaced lifecycle machines;
- conventions and entity-kind supplement;
- migration/compatibility record;
- positive/negative cross-record fixtures;
- consolidated safety net.

Structural JSON Schema validation is not sufficient. WP13 must enforce typed references, immutability/parent graphs, generations/epochs, locality XOR, expiry/freshness, authority, component completeness, privacy, transition validity and recovery-proof invariants.

## Consequences

### Positive

- Workspace identity survives runtime/backend/client changes.
- multiple Activities/Sessions coexist without one-current-task assumptions.
- layout restore and runtime recovery cannot be confused.
- checkpoint completeness/consistency/privacy are explicit.
- target compatibility is checked before mutation.
- restore runtime existence and application recovery are separate proof levels.
- stale-generation evidence and uncertain external effects remain fenced.
- local and remote providers use truthful shared contracts.
- export/import preserves provenance and authority decisions.

### Costs

- richer records than one project/session/snapshot table;
- checkpoint components and postconditions require explicit manifests/protocols;
- sensitive state and portability reduce automatic restore convenience;
- migration from simple workspace/container systems often needs manual review.

## Rejected alternatives

### Directory/container/VM as Workspace identity

Rejected because runtime/storage bindings change and can be duplicated.

### Client or panel connection as Session identity

Rejected because presentation detaches while runtime persists.

### Snapshot file equals complete checkpoint

Rejected because scope, consistency, required components, secrets and provenance vary.

### Hash verified equals restore-compatible

Rejected because target runtime/hardware/policy compatibility is separate.

### Provider/process started equals recovered

Rejected because application/service/data/session postconditions require new-generation read-back.

### Restore clears uncertain external effects

Rejected because external truth may outlive local checkpoint state.

### Silent import merge by same name/path

Rejected because identity and authority must be explicit.

## Downstream requirements

WP06 and later packages may reference WP05 candidates but must preserve:

- Workspace/Revision/Materialization separation;
- Session/Attachment/control separation;
- generation/epoch fencing;
- checkpoint Component/Bundle/Verification separation;
- compatibility-before-mutation;
- runtime restore versus Recovery Verification;
- privacy/credential/export/import rules;
- WP02 Activity/Attempt/Receipt correlation;
- WP03 Object/Artifact/Location identity;
- WP04 Node/Provider/locality/capability evidence.

No Workspace Provider, Session backend, checkpoint format, VM/container snapshot engine, archive/export service, browser-profile vault or restore runtime is authorized by this ADR.

## Related records

- `work-packages/PHASE-0B-WP05-WORKSPACE-SESSION-CHECKPOINT-RECOVERY.md`
- `contracts/PHASE-0B-WP05-WORKSPACE-SESSION-CHECKPOINT-RECOVERY-CONVENTIONS.md`
- `contracts/PHASE-0B-WP05-ENTITY-KIND-SUPPLEMENT.md`
- `schemas/phase-0b/workspace/schema-catalog.v0.1.0.json`
- `migrations/phase-0b/WP05-WORKSPACE-SESSION-CHECKPOINT-RECOVERY-MIGRATION-COMPATIBILITY.md`
- `conformance/PHASE-0B-WP05-WORKSPACE-SESSION-CHECKPOINT-RECOVERY-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp05/workspace-session-checkpoint-cases.v0.1.0.json`
