# Phase 0B WP05 — Workspace, Session, Checkpoint and Recovery Migration Compatibility

**Status:** CANDIDATE  
**Contract catalogs:** common 0.1.0, activity 0.1.1, object 0.1.0, runtime 0.1.2, workspace 0.1.0  
**Date:** 2026-07-19

## Purpose

Define how legacy projects, directories, sandboxes, sessions, snapshots, archives and recovery records enter Ptah without fabricating Workspace identity, runtime continuity, checkpoint completeness, restore compatibility or application recovery.

## Preservation rules

1. Workspace identity is never derived from path, repository URL/ref, container/VM/sandbox ID, Provider ID, Node ID or shell layout.
2. Workspace, immutable Workspace Revision and runtime Materialization remain separate.
3. Session, client Attachment, control Lease, backend alias and Shell layout remain separate.
4. Checkpoint Request, Component, Bundle, Verification, Restore Compatibility, Restore Run and Recovery Verification remain separate.
5. bundle creation, integrity verification, target compatibility, runtime restore and application recovery are different proof domains.
6. Node, Provider, materialization/workload generations and connection epochs are preserved or marked unknown.
7. old uncertain external/non-idempotent Operations remain unresolved after migration/restore.
8. credentials, cookies, keys and sensitive session state are not reactivated merely because checkpoint bytes exist.
9. historical negative, partial, incompatible and failed recovery evidence is retained.
10. backend aliases/paths/locations remain aliases and are remapped explicitly.

## Legacy Workspace import

A legacy project/environment record may produce:

- one `core.workspace` only after stable logical ownership/scope is identified;
- one or more immutable `core.workspace_revision` records;
- zero or more `core.workspace_provider_binding` records;
- zero or more runtime Materializations and Sessions;
- source/object/location aliases and provenance.

When several directories/containers clearly represent the same logical Workspace, retain separate materializations/aliases and create explicit evidence rather than merging silently.

When identity is ambiguous, create separate Workspaces or import as reference-only pending review.

## Workspace Revision migration

Mutable settings/configuration history is converted into immutable revisions. Unknown historical values remain limitations rather than being filled from current runtime state.

Concurrent divergent settings create separate revisions with explicit parentage. Last-write-wins is not used to fabricate a merge.

## Membership migration

Legacy users/roles are imported only with exact principal/group resolution, issuer/authority, scope and policy. Display names/emails/usernames remain aliases.

Unverifiable or expired access becomes suspended/revoked/expired or manual-review evidence, not active membership.

Control authority is not inferred from membership alone.

## Provider binding and Materialization migration

Legacy environment/provider records are decomposed into:

```text
Workspace Provider Binding
Provider/Revision/Instance
Workspace Materialization
Sessions and runtime components
```

A running container/VM/process is not a Workspace.

Missing generations receive migration-assigned generations with explicit unknown-history limitation. Existing Attempts/Receipts lacking exact generations remain historical but cannot prove current work.

Local/remote Provider locality follows WP04 rules. External services never receive fictional Node records.

## Session migration

Legacy terminal/browser/application/device/shell sessions map to a `runtime.session` root and optional specialist subtype.

Client/WebSocket/browser-tab/panel connections map to Session Attachments or Aliases, not Session identity.

If only presentation/layout state exists, import it as shell/layout/view state and do not create a recovered runtime Session.

Missing provider/materialization/generation evidence yields historical/closed/unknown-limited Session records, not active current Sessions.

## Checkpoint migration

Legacy snapshots/backups/checkpoint files are imported as Components and Bundles only when exact source, producing machinery, hashes and scope can be established.

Unknown consistency becomes `unknown`. Missing required components make completeness partial/mixed/unknown. A provider snapshot file alone is not a complete Workspace checkpoint.

Existing signatures/hashes become integrity evidence only. Restore compatibility remains target-specific and must be re-evaluated.

## Secrets and private state

Legacy archives are inspected/classified before import. Secret material is excluded, encrypted under approved policy, or retained as prohibited/restricted evidence.

Credentials are re-authorized and re-delivered as fresh references where possible. Expired/revoked secrets remain inactive.

## Restore migration

Legacy restore logs may become Restore Runs only when target, bundle, Activity/Attempt, provider/materialization generations and component results are identifiable.

A successful process/container/VM start does not become `recovered`. Recovery Verification requires target-generation read-back and declared postconditions.

Old pre-restore Receipts cannot prove restored-generation work.

## Archive/export/import migration

A legacy archive/export becomes an immutable Workspace Export/Artifact with included/omitted records, privacy policy, hashes, provenance and limitations.

Import requires one explicit decision: create new, restore existing under authority, fork, merge by plan, reference-only or reject.

Cross-installation imports normally create new local canonical IDs with provenance/alias mapping unless an authorized identity-preserving protocol exists.

Memberships, credentials, provider bindings, policies and Locations are re-authorized/remapped.

## State migration

Legacy global `status` fields are split into the relevant namespaces:

- Workspace lifecycle;
- Membership lifecycle;
- Provider Binding lifecycle;
- Materialization lifecycle;
- Session lifecycle;
- Attachment lifecycle;
- Checkpoint/Restore Request lifecycle;
- Restore Run lifecycle;
- Provider readiness/health/reachability;
- compatibility, completeness, consistency and recovery outcomes.

Ambiguous values become unknown/partial/manual-review records. They are never guessed into active, complete, compatible, restored or recovered.

## Compatibility and breaking changes

Breaking changes include changes to:

- Workspace identity/revision semantics;
- Session family/subtype identity;
- materialization/generation semantics;
- checkpoint class, consistency or completeness meanings;
- secret/privacy/export behavior;
- restore compatibility rules;
- recovery postconditions;
- lifecycle transition authority.

They require versioned Migration Definition/Run records, retained source records, validation and rollback/export strategy.

## Backend replacement

Provider/runtime replacement:

1. preserves Workspace identity/revision history;
2. creates/selects compatible binding and Provider revisions/instances;
3. creates new Provider and Materialization generations;
4. remaps aliases/Locations;
5. re-evaluates checkpoint compatibility;
6. re-runs readiness and Recovery Verification;
7. preserves old Sessions, checkpoints, Attempts, Receipts and failures;
8. exposes unsupported/nonportable state rather than claiming equivalence.

## Negative migration cases

Reject or require manual review when migration attempts to:

- use a directory/container/VM/provider ID as Workspace identity;
- convert panel/layout state into runtime recovery;
- treat client attachment as Session existence/control authority;
- claim checkpoint complete with missing/unknown required components;
- treat integrity verification as compatibility;
- treat runtime start as application recovery;
- reuse old materialization/provider/workload generation after restore;
- reactivate checkpointed credentials automatically;
- erase uncertain Operations or failed restore evidence;
- silently merge imported Workspace identities/memberships;
- fabricate Node evidence for a remote Provider;
- discard omissions/privacy/nonportable limitations from exports.

WP13/WP14 must execute these migrations and round-trip/export tests; structural schema validation is insufficient.