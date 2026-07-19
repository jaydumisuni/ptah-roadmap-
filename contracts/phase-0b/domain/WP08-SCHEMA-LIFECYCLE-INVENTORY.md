# WP08 Schema and Lifecycle Inventory

**Status:** CANDIDATE REVIEW CHECKLIST  
**Date:** 2026-07-19

This inventory is normative for WP08 catalog review. A record is either a new WP08 schema or an explicitly reused canonical family; no implementation may invent an overlapping identity.

## Domain Pack and operation schemas

Required new/active records:

- `domain.pack`
- `domain.pack_revision`
- `domain.pack_compatibility`
- `domain.detector_observation`
- `domain.classification_decision`
- `domain.operation_request`
- `domain.operation_run`
- `domain.inventory`
- `domain.coverage`
- `domain.validation_run`
- `domain.compare_run`
- `domain.rebuild_run`

Explicit reuse:

- `object.decomposition_run` remains the canonical decomposition-run identity.
- WP02 Activity, Operation, Attempt, Receipt and reconciliation records remain canonical execution/proof identities.
- WP03 Object, Object Revision, View, Relationship, Content and Artifact remain canonical source/output identities.

Required lifecycle machines:

- `domain.pack.lifecycle`
- `domain.operation_request.lifecycle`
- `domain.operation_run.lifecycle`

Inventory, Coverage, detector and Classification records are immutable result/decision records unless a later accepted ADR defines a separate lifecycle; supersession uses new records and references.

## Firmware schemas

Required active records:

- `firmware.package`
- `firmware.manifest`
- `firmware.component`
- `firmware.executable_asset`
- `firmware.compatibility_claim` where source/tool claims are imported
- `firmware.compatibility_result`
- `firmware.operation_plan`
- `firmware.mutation_authorization`
- `firmware.protocol_stage_observation`
- `firmware.operation`
- `firmware.operation_verification`

Required lifecycle machine:

- `firmware.operation.lifecycle`

Plan, Authorization, stage observations and verification results are immutable records. Retry remains WP02 Attempt lifecycle, never a reused firmware-operation identity.

## Disk and filesystem schemas

Required active records:

- `disk.image`
- `disk.image_revision`
- `disk.extent_map`
- `disk.partition_table`
- `disk.partition`
- `filesystem.observation`
- `filesystem.filesystem`
- `filesystem.mount_session`
- `filesystem.inspection_result`

Explicit reuse:

- exact bytes and digests remain WP03 Content/Object Revision identity;
- storage Locations remain WP03 storage identity;
- writable transformation/rebuild uses WP07 Recipe/Build and WP02 execution identities.

Required lifecycle machines:

- `filesystem.filesystem.lifecycle`
- `filesystem.mount_session.lifecycle`

Disk interpretation records are immutable revisions/results. A later reparse creates new records instead of mutating historical ranges.

## Device schemas

Required active records:

- `device.device`
- `device.profile_revision`
- `device.interface`
- `device.connection`
- `device.connection_observation`
- `device.session`
- `device.session_capability_snapshot`
- `device.stream`
- `device.stream_observation`
- `device.screen_context`
- `device.protocol_operation`
- `device.backup`
- `device.mutation_exception`
- `device.operation_recovery`

Explicit reuse:

- `runtime.lease` with lease type `device` is the canonical Lease identity; WP08 must not create `device.lease`.
- WP04 Provider revision/instance/generation and Node generation/connection epoch remain canonical runtime bindings.
- WP05 Session family rules apply, but Device Session remains its registered typed family.
- WP06 backup/storage verification and Transfer primitives are reused where applicable; Device Backup adds exact physical-target scope.
- WP02 Operation/Attempt remain canonical logical/physical execution identities.

Required lifecycle machines:

- `device.device.lifecycle`
- `device.interface.lifecycle`
- `device.connection.lifecycle`
- `device.session.lifecycle`
- `device.stream.lifecycle`
- `device.backup.lifecycle`
- `device.protocol_operation.lifecycle`
- `device.operation_recovery.lifecycle`

Profile revisions, capability snapshots, observations, Screen Context, Mutation Exceptions and verification records are immutable/freshness-bound records, not generic mutable status.

## Catalog requirements

The active WP08 catalog must:

1. include one entry for every new WP08 schema;
2. reference reused external Phase 0B catalogs rather than copying their `$id`;
3. include every lifecycle-machine file in its package manifest or associated catalog metadata;
4. contain no duplicate `$id`, schema name, entity kind or state-machine name;
5. resolve offline from repository-relative paths;
6. pin candidate package and record versions;
7. identify superseded/corrected records explicitly rather than silently replacing history.

## Review blockers

Block WP08 acceptance if:

- a record listed above has neither a schema nor an explicit reuse decision;
- two schemas claim the same entity kind;
- one schema uses a backend/path/serial/session identifier as canonical identity;
- a lifecycle projection names a missing machine;
- firmware operation and Device protocol operation overlap without an explicit mapping;
- a Device-specific Lease duplicates `runtime.lease`;
- disk-image interpreted identity duplicates WP03 byte identity;
- decomposition duplicates `object.decomposition_run`;
- acknowledgement or backend return code can produce verified success without the separate Verification record.
