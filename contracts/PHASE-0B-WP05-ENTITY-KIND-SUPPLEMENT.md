# Phase 0B WP05 — Entity Kind Supplement

**Status:** CANDIDATE DRAFT  
**Parent registry:** `ptah.entity-kind` `0.1.0`  
**Date:** 2026-07-19

## New entity kinds

| Entity kind | Canonical role | Mutability rule |
|---|---|---|
| `core.workspace_revision` | immutable intended configuration/policy revision of one Workspace | immutable |
| `core.workspace_membership` | versioned principal/group authority in one Workspace | lifecycle projection; decisions/history retained |
| `core.workspace_provider_binding` | compatibility/policy binding between Workspace Revision and Facility/Provider | lifecycle projection; revisions/history retained |
| `core.workspace_materialization` | one runtime incarnation of one Workspace Revision | lifecycle projection with monotonic materialization generation |
| `core.workspace_journal_entry` | append-only Workspace-scoped durable change/reference record | immutable |
| `core.workspace_import_decision` | explicit create/fork/merge/restore/reference/reject identity decision | immutable |
| `runtime.session_attachment` | time-bounded observer/client/caller attachment to one Session | lifecycle projection; history retained |
| `runtime.checkpoint_request` | requested checkpoint scope/consistency/privacy/portability intent | lifecycle projection; accepted request creates capture work |
| `runtime.checkpoint_component` | one immutable component entry in a checkpoint bundle | immutable |
| `runtime.checkpoint_verification` | immutable integrity/completeness/privacy verification over bundle/components | immutable |
| `runtime.restore_request` | requested restore target/scope/policy intent | lifecycle projection |
| `runtime.restore_compatibility` | target-specific time-bounded compatibility decision | immutable |
| `runtime.restore_run` | one restore execution result root linked to Activity/Attempts | immutable result/projection root; retries create new Attempts |
| `runtime.recovery_verification` | application/runtime post-restore read-back result | immutable |
| `object.workspace_export` | immutable allowlisted Workspace export/recovery Artifact role | immutable |
| `object.workspace_import` | immutable import source/report Artifact role | immutable |

## Existing kinds reused

- `core.workspace` — stable persistent namespace/world identity.
- `runtime.session` — typed Session root.
- `runtime.checkpoint` — checkpoint definition/root where independently referenced.
- `runtime.checkpoint_bundle` — immutable multi-component checkpoint manifest.
- `storage.restore_run` — storage-backend restore result where used by WP06; it does not replace runtime restore/recovery records.
- `event.cursor` — replay/reconnect cursor.
- `runtime.provider`, `runtime.provider_revision`, `runtime.provider_instance` — WP04 Provider identities.
- `runtime.lease` — control/execution authority root; WP05 references but does not redefine it.
- `object.object`, `object.revision`, `object.artifact`, `storage.location` — WP03 data/provenance identities.
- `core.activity`, `core.operation`, `core.attempt`, `proof.receipt`, `proof.evidence` — WP02 execution/proof records.
- `shell.session`, `shell.panel`, `shell.layout_revision`, `shell.view_state` — presentation records, never runtime Session/Workspace truth.

## Session kinds

`runtime.session` declares a registered `session_kind`:

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

Existing specialist entity kinds such as `shell.session`, `application.session`, `device.session`, `browser.context`, `runtime.pty` and `filesystem.mount_session` remain independently referenced subtype identities where needed. They may link to a `runtime.session` root; they do not change its identity in place.

## Typed-reference rules

- `workspace_ref` requires `core.workspace`.
- `workspace_revision_ref` requires `core.workspace_revision`.
- `workspace_materialization_ref` requires `core.workspace_materialization`.
- `workspace_provider_binding_ref` requires `core.workspace_provider_binding`.
- `session_ref` requires `runtime.session` or a registered specialist Session-family kind according to the field contract.
- `session_attachment_ref` requires `runtime.session_attachment`.
- `checkpoint_bundle_ref` requires `runtime.checkpoint_bundle`.
- `checkpoint_component_ref` requires `runtime.checkpoint_component`.
- `restore_compatibility_ref` requires `runtime.restore_compatibility`.
- `restore_run_ref` requires `runtime.restore_run`.
- `recovery_verification_ref` requires `runtime.recovery_verification`.

The executable harness must enforce cross-document kind, parentage, generation, locality, compatibility, completeness and authority constraints that JSON Schema alone cannot express.

## Identity prohibitions

The following cannot become canonical Workspace, Session or checkpoint identities:

- directory/worktree/root path;
- Git repository URL/ref;
- container/VM/sandbox ID;
- Provider/Node ID;
- process ID, PTY descriptor, browser target, window handle or Device interface ID;
- client/WebSocket/session cookie;
- shell/panel/layout ID;
- checkpoint filename/path/backend snapshot ID;
- cloud object key, ETag or backup snapshot ID;
- export archive filename;
- user email/display name;
- runtime state string.

## Classification rules

1. Workspace and Workspace Revision are separate.
2. Workspace Materialization is runtime state and never Workspace identity.
3. Session and Session Attachment are separate.
4. Shell Session is presentation and does not replace runtime Workspace/Session records.
5. Checkpoint Request, Bundle, Component, Verification, Compatibility, Restore Run and Recovery Verification are separate.
6. storage restore and runtime/application recovery are separate proof domains.
7. export/import is not checkpoint/resume and requires explicit identity/provenance decisions.
8. registration does not authorize implementation or imply universal checkpoint support.
