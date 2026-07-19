# Phase 0B WP05 — Workspace, Session, Checkpoint and Recovery

**Status:** CANDIDATE COMPLETE — DOWNSTREAM CONTRACT USE APPROVED; IMPLEMENTATION FREEZE DEFERRED  
**Date:** 2026-07-19  
**Runtime implementation:** NOT STARTED  
**Dependency/backend selection:** NOT STARTED

## Purpose

Turn the frozen persistent Workspace, Session Vault, Shell-control, Provider-generation, Object/storage and Activity/Receipt architecture into exact candidate identities, schemas, lifecycles, migration rules and recovery proof requirements.

WP05 closes the contract boundary needed to preserve Workspace identity across client detach, Provider restart, checkpoint, restore, archive, export/import and backend replacement without claiming runtime or application recovery from weak evidence.

## Normative records

- `contracts/PHASE-0B-WP05-WORKSPACE-SESSION-CHECKPOINT-RECOVERY-CONVENTIONS.md`
- `contracts/PHASE-0B-WP05-ENTITY-KIND-SUPPLEMENT.md`
- `schemas/phase-0b/workspace/schema-catalog.v0.1.0.json`
- `migrations/phase-0b/WP05-WORKSPACE-SESSION-CHECKPOINT-RECOVERY-MIGRATION-COMPATIBILITY.md`
- `conformance/PHASE-0B-WP05-WORKSPACE-SESSION-CHECKPOINT-RECOVERY-SAFETY-NET.md`
- `conformance/fixtures/phase-0b/wp05/workspace-session-checkpoint-cases.v0.1.0.json`

## Candidate schema set

The Workspace catalog contains 19 active schemas:

1. shared definitions;
2. Workspace;
3. Workspace Revision;
4. Workspace Membership;
5. Workspace Provider Binding;
6. Workspace Materialization;
7. Workspace Journal Entry;
8. Workspace Import Decision;
9. Workspace Export;
10. runtime Session;
11. Session Attachment;
12. Checkpoint Request;
13. Checkpoint Component;
14. Checkpoint Bundle;
15. Checkpoint Verification;
16. Restore Request;
17. Restore Compatibility;
18. Restore Run;
19. Recovery Verification.

Dependencies:

- `ptah.common` `0.1.0`;
- `ptah.activity` `0.1.1`;
- `ptah.object` `0.1.0`;
- `ptah.runtime` `0.1.2`.

## Lifecycle machines

Nine namespaced lifecycle machines are included:

- `workspace.lifecycle`;
- `workspace.membership.lifecycle`;
- `workspace.provider_binding.lifecycle`;
- `workspace.materialization.lifecycle`;
- `session.lifecycle`;
- `session.attachment.lifecycle`;
- `checkpoint.request.lifecycle`;
- `restore.request.lifecycle`;
- `restore.run.lifecycle`.

Compatibility, consistency, completeness, sensitivity, portability, attachment/control, Provider readiness/health and Recovery Verification outcomes remain separate from lifecycle.

## Accepted boundaries

### Workspace identity and revisions

1. Workspace is stable persistent namespace/world identity.
2. path, repository, container, VM, sandbox, Provider, Node and Shell layout remain aliases/bindings/projections.
3. Workspace may remain `active` with zero runtime Materializations.
4. Workspace Revision is immutable intended configuration/policy and never live runtime state.
5. divergent revisions remain separate until an explicit merge revision exists.
6. Workspace lifecycle does not follow Provider/Node/client/runtime state automatically.

### Membership and policy

1. Workspace Membership is first-class, scoped and issued by named authority.
2. membership does not automatically grant Session control/input.
3. suspension/revocation/expiry fences current authority according to policy without deleting history.
4. imported memberships require destination re-authorization.

### Provider binding and Materialization

1. Workspace Provider Binding expresses compatibility/policy intent; it is not a running environment.
2. Workspace Materialization is one runtime incarnation of one exact Workspace Revision.
3. Materialization binds exact Provider Instance/generation/epoch and exactly one local-Node or remote-service locality.
4. Materialization generation advances on fresh create, restore, Node/Provider/backend/locality replacement or forced fencing.
5. client/shell reconnect never advances Materialization generation.
6. Materialization `running` proves runtime existence only—not Provider readiness or application recovery.
7. Provider/backend replacement preserves Workspace identity and revision history.
8. destroying Materialization does not destroy Workspace identity, Objects, Activities or history.

### Session and attachment

1. runtime Session is a typed family root for workspace/process/PTY/shell/browser/application/device/display/semantic/filesystem/service relationships.
2. backend tokens, process IDs, panels, tabs, sockets and client connections remain aliases or children.
3. Session binds exact Workspace/Materialization/Provider generations and locality.
4. Session Attachment is a separate time-bounded human/automation/service/client relationship.
5. detaching the last client does not close the Session or Workspace.
6. observer attachment and mutation/control authority remain separate; control references typed Lease/fencing records.
7. Shell layout/panel restoration is presentation only and never proves runtime Session recovery.
8. stale epoch/fence input is rejected.

### Journal and reconnect

1. Workspace Journal is append-only reconstruction support, not Activity Ledger or source truth.
2. outbox/cursor state does not authorize replay of non-idempotent effects.
3. reconnect compares canonical identities, generations, epochs and cursors before accepting projections.
4. stale client/UI/runtime projections are rejected.
5. uncertain work is reconciled through WP02 Receipts/external truth rather than repeated from missed Events.

### Checkpoint capture

1. Checkpoint Request, Component, Bundle and Verification remain separate.
2. Request acceptance creates a distinct Activity and never mutates into the Bundle.
3. each Component retains exact source subjects/generations, producer revision/generation, consistency, completeness, portability, sensitivity, output Objects/Artifacts/Locations and Receipts.
4. Bundle is an immutable manifest over Components.
5. required missing/failed/unknown/excluded Components prevent `complete_for_declared_scope`.
6. mixed consistency remains mixed; unknown/crash consistency never becomes application/transaction consistency without evidence.
7. checkpoint creation proves production only.
8. manifest/hash/signature verification proves bounded integrity/identity only, not compatibility or recovery.

### Privacy and credentials

1. raw credentials/tokens/keys are excluded by default.
2. sensitive state is omitted, encrypted under explicit policy or retained as restricted references.
3. encryption keys remain separate credential references.
4. restore/import re-authorizes and re-delivers fresh credentials where possible.
5. expired/revoked credentials are never reactivated from checkpoint bytes.
6. export uses allowlist/redaction and states omitted/nonportable state and impact on recovery.

### Restore compatibility, execution and recovery

1. Restore Compatibility is target-specific, component-specific and expiring.
2. incompatible/unknown target is rejected before mutation.
3. partial compatibility requires explicit reduced-scope approval.
4. local restore requires Node/generation/capability/resource evidence; remote restore requires approved remote-service/Provider evidence without fictional Nodes.
5. Restore is a new Activity/Operations/Attempts and new Materialization/Provider/workload generations.
6. old Attempts/Receipts cannot prove restored-generation work.
7. `restored_runtime` proves runtime existence only.
8. Recovery Verification uses new-generation application/service/data/session postconditions and read-back.
9. `recovered` requires required postconditions pass and no required unresolved Operations.
10. failed/partial/cancelled restore retains partial outputs, cleanup/containment, limitations and uncertain external effects.
11. checkpoint/restore never resolves non-idempotent external uncertainty automatically.

### Archive, export and import

1. archive is administrative/runtime-storage handling, not portable recovery proof.
2. Workspace Export is immutable allowlisted Artifact/View with included/omitted records, hashes, provenance and privacy policy.
3. Import requires explicit create-new, restore-existing-under-authority, fork, merge-by-plan, reference-only or reject decision.
4. cross-installation import normally assigns new local IDs plus provenance/alias mapping unless identity-preserving authority exists.
5. Content/Object identity may be retained where digest/privacy/deduplication policy permits.
6. memberships, credentials, policies, bindings and Locations are re-authorized/remapped.
7. imported runtime/checkpoint claims remain unverified until local checks.
8. silent overwrite/merge is forbidden.

## Migration closure

The migration record forbids:

- path/container/provider-derived Workspace identity;
- mutable Revision overwrite;
- layout/panel/client state promoted to runtime recovery;
- Attachment promoted to Session/control authority;
- checkpoint completeness/consistency overclaim;
- integrity promoted to compatibility;
- Provider start promoted to application recovery;
- old generation evidence reused after restore;
- credential reactivation;
- uncertain effects erased;
- silent import merge;
- fictional remote-service Node;
- negative/partial/nonportable evidence deletion.

## Conformance closure

The safety net and fixture suite cover:

- active Workspace without Materialization;
- multiple concurrent Activities/Sessions;
- revision divergence and merge;
- membership/control separation;
- Provider replacement and generation fencing;
- local/remote Materialization locality;
- Session detachment without close;
- stale attachment/fencing rejection;
- missed Event versus side-effect replay;
- required-component completeness;
- consistency overclaim;
- integrity versus compatibility;
- sensitive checkpoint/export handling;
- compatibility before mutation;
- runtime restored/application partial;
- stale pre-restore evidence;
- uncertain external effects;
- partial restore approval;
- explicit import identity/provenance;
- Workspace failure isolation.

Structural validation is insufficient. WP13 must execute typed-reference, graph/history, time/expiry, generation/epoch, locality, lifecycle, component completeness, privacy, authority and cross-record proof invariants.

## Candidate-completion verdict

**WP05 is candidate-complete for downstream Phase 0B use.**

It does not prove that any Workspace Provider, Session backend, checkpoint engine, snapshot format, archive/export system, restore path, runtime recovery or application recovery exists or works.

## Deferred work

- transfer/sync/conflict/backup — WP06;
- Build/provenance — WP07;
- domain/device/application/browser/shell subtype contracts — later WPs;
- isolation/placement/reservation/Lease/secure grants — WP11;
- security/reproduction — WP12;
- executable harness and golden corpus — WP13/WP14;
- runtime/dependency/backend selection — Phase 0C only.

## Acceptance decision

- `decisions/ADR-0022-WORKSPACE-SESSION-CHECKPOINT-RESTORE-RECOVERY-BOUNDARY.md`

## Do-not-build rule

> Candidate-complete contracts authorize downstream schema design only. They do not authorize selecting or implementing a Workspace Provider, Session backend, checkpoint format, VM/container snapshot engine, browser-profile vault, archive/export system or restore service.