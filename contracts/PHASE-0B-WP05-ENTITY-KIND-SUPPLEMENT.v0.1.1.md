# Phase 0B WP05 — Workspace, Session, Checkpoint and Recovery Entity-Kind Supplement

**Registry supplement:** `ptah.entity-kind`  
**Candidate version:** `0.1.1`  
**Status:** CANDIDATE  
**Date:** 2026-07-19  
**Supersedes:** `contracts/PHASE-0B-WP05-ENTITY-KIND-SUPPLEMENT.md` (`0.1.0`)

## Purpose

Register the Workspace/recovery identities needed by WP05 without changing the frozen base registry. This version adds the durable Workspace outbox identity that was named by the normative conventions but omitted from the first supplement.

## Workspace identities

| Token | Meaning |
|---|---|
| `core.workspace_revision` | Immutable desired-state/configuration revision of one Workspace |
| `core.workspace_membership` | Versioned principal/role/membership relationship to one Workspace |
| `core.workspace_provider_binding` | Versioned allowed/preferred Facility/Provider binding policy |
| `core.workspace_materialization` | One runtime incarnation/generation of an exact Workspace Revision |
| `core.workspace_journal_entry` | Append-only durable Workspace/runtime/recovery fact |
| `core.workspace_outbox_entry` | Durable intended Event/command publication with delivery/reconciliation state |
| `core.workspace_import_decision` | Explicit restore/clone/fork/merge/reject identity decision |

`core.workspace` remains the canonical logical Workspace identity from the base registry.

## Session and recovery identities

| Token | Meaning |
|---|---|
| `runtime.session_attachment` | One human, automation or service attachment/connection epoch to a Session |
| `runtime.checkpoint_request` | Intent and policy for a checkpoint capture Activity |
| `runtime.checkpoint_component` | One immutable captured component with generation, consistency and sensitivity evidence |
| `runtime.checkpoint_verification` | Integrity/completeness/consistency verification over a Checkpoint Bundle |
| `runtime.restore_request` | Intent and authority for validation or restore |
| `runtime.restore_compatibility` | Target-specific, expiring restore compatibility decision |
| `runtime.restore_run` | One restore execution Activity/result root |
| `runtime.recovery_verification` | Post-restore readiness/read-back/reconciliation result |

`runtime.session`, `runtime.checkpoint_bundle` and `event.cursor` remain base-registry identities reused by WP05.

## Export/import identities

| Token | Meaning |
|---|---|
| `object.workspace_export` | Immutable allowlisted export/archive/handoff package Artifact role |
| `object.workspace_import` | Immutable imported package/evidence root before identity decision |

## Rules

1. The Workspace, Workspace Revision, Materialization, Session and Attachment identities never collapse.
2. Journal, outbox, Event and cursor remain distinct.
3. Checkpoint Request, Component, Bundle, Verification, Restore Request, Compatibility, Run and Recovery Verification remain distinct.
4. Export/import package identity never decides whether an existing Workspace is resumed, cloned, forked or merged.
5. Backend, path, container, VM, endpoint and connection identifiers remain scoped aliases.
6. Registration does not authorize implementation or public visibility.