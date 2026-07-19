# Phase 0B WP05 — Workspace, Session, Checkpoint and Recovery Safety Net

**Status:** CANDIDATE SPECIFICATION  
**Date:** 2026-07-19  
**Executable harness:** DEFERRED TO WP13  
**Fixture suite:** `conformance/fixtures/phase-0b/wp05/workspace-session-checkpoint-cases.v0.1.0.json`

## Purpose

Define structural, cross-record, temporal, generation, authority, privacy, checkpoint and recovery invariants that every WP05 implementation and migration must satisfy.

JSON Schema validation alone is insufficient.

---

# A. Workspace identity and revision

1. reject path, repository, container, VM, sandbox, Provider, Node or layout ID as Workspace identity;
2. preserve Workspace identity when no materialization exists;
3. permit several unrelated Activities, Materializations and Sessions in one Workspace;
4. require immutable Workspace Revisions with explicit parentage;
5. reject in-place mutation of a frozen Revision;
6. divergent revisions from the same base remain distinct until an explicit merge revision exists;
7. Workspace lifecycle does not mirror runtime/provider/client state;
8. Provider/Node failure or Shell detach cannot automatically suspend/archive/retire Workspace.

# B. Membership and authority

1. membership requires resolved principal/group identity, role/scope, issuer and policy;
2. username/email/display name remains Alias evidence;
3. expired/revoked/suspended membership cannot authorize new work/attachment/control;
4. membership does not automatically grant Session input/control;
5. revocation fences active control grants/attachments as policy requires without deleting history;
6. imported memberships require destination authorization.

# C. Provider binding and Materialization

1. Binding is not Materialization and does not prove readiness;
2. Materialization binds exact Workspace Revision, Provider Instance/generation and exactly one local/remote locality form;
3. local Materialization requires Node/generation; remote Materialization forbids Node fields;
4. Provider restart, restore, migration or backend replacement creates/advances Materialization generation;
5. client reconnect does not advance Materialization generation;
6. `running` Materialization does not imply Provider readiness or declared application/service recovery;
7. Workspace identity survives Provider/backend/locality replacement;
8. failed/quarantined Materialization requires exact-generation evidence and blocks ordinary work;
9. destroyed Materialization does not delete Workspace/Object/Activity history;
10. one Workspace Materialization failure does not alter unrelated Workspaces or disconnect Node globally.

# D. Session and Attachment

1. Session identity is not client connection, panel, process ID, PTY descriptor, browser target, Window handle or backend token;
2. Session binds exact Workspace/Materialization/Provider generations and locality;
3. detached/expired/revoked Attachment does not automatically close Session;
4. closing a panel/layout does not close Session without explicit Activity;
5. active Session may have zero Attachments;
6. several observer Attachments may coexist with one scoped control Lease;
7. stale connection epoch/fencing token cannot mutate Session;
8. attachment capability scope cannot exceed membership/policy/Lease;
9. subtype lifecycle must explicitly map to neutral Session lifecycle;
10. Session restore creates new current-generation evidence; old Receipts cannot prove it.

# E. Journal and reconnect

1. Journal sequence is monotonic per Workspace scope;
2. journal/outbox/cursor is not Activity Ledger or source truth;
3. missed Event never automatically replays a side effect;
4. reconnect compares Workspace/Materialization/Session generations and epochs before accepting client projection;
5. stale layout/client/runtime projection is rejected;
6. uncertain work is reconciled through WP02 records and Provider/external read-back;
7. journal compaction preserves referenced durable records and cursor semantics.

# F. Checkpoint Request and Components

1. Request and Checkpoint Bundle are separate entities;
2. accepted request creates a distinct Activity; Request kind never mutates into Bundle;
3. requested consistency/portability must be supported or downgraded only by explicit accepted scope change;
4. every Component binds exact source subjects/generations and producing Provider revision/generation;
5. every Component retains consistency, completeness, portability, sensitivity and excluded state;
6. required Components missing/failed/unknown prevent complete-for-declared-scope;
7. partial valid Components remain retained after cancellation/failure;
8. a provider snapshot/file alone cannot claim complete Workspace checkpoint;
9. unknown consistency cannot be promoted to application/transaction consistency;
10. checkpoint creation Receipt proves production only, not restore compatibility.

# G. Bundle, verification and privacy

1. Bundle is immutable manifest over Components;
2. overall consistency cannot exceed component evidence and mixed components remain mixed;
3. overall completeness follows declared scope and required Component results;
4. integrity verification does not imply compatibility or recovery;
5. signature/attestation proves identity/integrity under its trust chain only;
6. unknown-sensitive or prohibited Components cannot be silently exported;
7. raw credentials/tokens/keys are absent unless explicitly encrypted/permitted and separately referenced;
8. encryption key is never embedded as ordinary bundle content;
9. public/external export uses allowlist/redaction and lists omissions/effect on recovery;
10. corrupt/missing Location is not hidden by a valid manifest digest.

# H. Restore compatibility

1. compatibility is target-specific, operation-specific and time-bounded;
2. incompatible/unknown target is rejected before mutation;
3. partial compatibility cannot satisfy requested full restore without explicit scope reduction/approval;
4. local compatibility requires target Node/generation/capability/resource evidence;
5. remote compatibility requires approved remote-service and Provider evidence and forbids fabricated Node evidence;
6. changed Provider/Node/materialization generation, runtime version, policy or grant expires prior compatibility;
7. conversion/migration requirements are explicit Activities and cannot be assumed lossless;
8. component-level incompatible/missing results remain visible.

# I. Restore Run and Recovery Verification

1. Restore is a new Activity/Operations/Attempts and new Materialization generation;
2. old Attempts/Receipts cannot prove restored-generation work;
3. `restored_runtime` proves target runtime existence only;
4. Recovery Verification uses new-generation postcondition/read-back evidence;
5. `recovered` requires every required postcondition pass and zero unresolved required Operations;
6. `partially_recovered` retains failed/not-tested postconditions and limitations;
7. failed/cancelled restore retains partial outputs, cleanup/containment and uncertain effects;
8. successful Provider start does not imply application/service/session recovery;
9. uncertainty for non-idempotent external effects survives crash/restore;
10. authoritative external results/compensation/human review resolve uncertain effects, not checkpoint rollback assumptions.

# J. Archive, export and import

1. archive does not imply portable checkpoint/recovery;
2. Workspace Export is immutable allowlisted Artifact/View with included/omitted records and provenance;
3. export never contains private host paths or unrestricted secret values;
4. import has explicit create/restore/fork/merge/reference/reject decision;
5. cross-installation identity retention requires authority; otherwise new IDs plus mapping/provenance are used;
6. Content/Object identity retention follows digest/privacy/deduplication policy;
7. memberships, policies, credentials, Provider bindings and Locations are re-authorized/remapped;
8. imported checkpoint/runtime claims remain unverified until local checks;
9. no silent overwrite/merge;
10. failed/rejected import retains evidence and leaves target unchanged.

# K. Migration and replacement

1. legacy global status is split into namespaced lifecycle/attachment/compatibility/completeness/recovery dimensions;
2. ambiguous values become unknown/partial/manual review;
3. backend replacement preserves Workspace identity/revision history;
4. replacement creates/selects compatible binding/Provider and new generation;
5. old Sessions/checkpoints/evidence remain historical;
6. unsupported/nonportable state is explicit;
7. no stale dispatch/compatibility/Lease/Attachment survives generation or policy change;
8. migration retains negative/partial/incompatible/failed evidence.

# L. Property-based invariants for WP13

- Workspace ID is stable under materialization/session/provider changes;
- Workspace Revision records are immutable and parent graph is acyclic;
- Materialization generation is monotonic per Workspace materialization identity;
- local/remote locality is XOR for Materialization, Session, Compatibility and Restore Run;
- Attachment terminal state never mutates Session lifecycle automatically;
- `complete_for_declared_scope` implies all required Components are present and nonfailed;
- `recovered` implies required postconditions passed and no required unresolved Operations;
- compatibility/attachment/availability decisions are rejected after expiry;
- old-generation Receipts cannot satisfy new-generation proof;
- public export contains only approved audience/redaction/allowlist records.

# Exit condition

WP05 is candidate-complete only when:

1. all schemas resolve through one local catalog;
2. lifecycle machines use registered state/proof vocabulary;
3. fixtures cover every mandatory positive/negative case;
4. migration rules preserve identities/history/privacy;
5. work package and ADR reference this safety net;
6. implementation/dependency selection remains blocked until Phase 0C.