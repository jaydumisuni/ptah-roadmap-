# Ptah Phase 0B — Entity Kind Registry WP08 Supplement

**Registry:** `ptah.entity-kind`  
**Candidate version:** `0.1.0`  
**Status:** CANDIDATE  
**Date:** 2026-07-19

This supplement extends the common registry for WP08 without modifying earlier registry history.

## Domain Pack and operations

| Token | Meaning |
|---|---|
| `domain.pack_compatibility` | Directional compatibility of one Pack Revision with exact input/operation/runtime context |
| `domain.detector_observation` | One Pack/detector type/classification assertion over an exact Object Revision |
| `domain.classification_decision` | Selected route/classification retaining conflicting detector evidence |
| `domain.operation_request` | Requested Pack operation, scope, budget, proof and mutation class |
| `domain.operation_run` | One accepted Pack operation execution over exact context |
| `domain.coverage` | Requested/processed/skipped/unknown/budget-exhausted operation coverage |

Existing kinds remain canonical:

- `domain.pack`;
- `domain.pack_revision`;
- `domain.inventory`;
- `domain.validation_run`;
- `domain.compare_run`;
- `domain.rebuild_run`;
- `object.decomposition_run`.

## Firmware and physical operation

| Token | Meaning |
|---|---|
| `firmware.compatibility_result` | Operation-specific package/component/asset/Device compatibility result |
| `firmware.executable_asset` | Loader, programmer, DA, FDL, ramdisk or other device-side executable asset role |
| `firmware.mutation_authorization` | Explicit authority for one exact physical mutation scope |
| `firmware.protocol_stage_observation` | One observed transport/service/write/read-back protocol stage |
| `firmware.operation_verification` | Post-operation physical/read-back verification result |

Existing firmware kinds remain canonical:

- `firmware.package`;
- `firmware.manifest`;
- `firmware.component`;
- `firmware.compatibility_claim` as a source/package/tool claim, distinct from reviewed `firmware.compatibility_result`;
- `firmware.operation`.

## Disk and filesystem

| Token | Meaning |
|---|---|
| `disk.image_revision` | Exact interpreted disk/sparse/virtual-image revision role over Object Revision |
| `disk.extent_map` | Immutable physical/logical/sparse/backing extent mapping |
| `filesystem.observation` | One parser/provider filesystem identification/state observation |
| `filesystem.inspection_result` | Read-only filesystem inventory/result produced by one mount/open Session |

Existing kinds remain canonical:

- `disk.image`;
- `disk.partition_table`;
- `disk.partition`;
- `filesystem.filesystem`;
- `filesystem.mount_session`.

## Device

| Token | Meaning |
|---|---|
| `device.profile_revision` | Immutable observed Device profile/layout/security/capability revision |
| `device.connection_observation` | Reachability/transport/mode observation under one Interface/epoch |
| `device.session_capability_snapshot` | Expiring capability snapshot for one Device Session |
| `device.stream_observation` | Health/format/geometry/availability observation for one Device Stream |
| `device.mutation_exception` | Explicit reviewed exception to required backup/read-back policy |
| `device.operation_recovery` | Reconciliation/cleanup/recovery result after interrupted physical operation |

Existing Device kinds remain canonical:

- `device.device`;
- `device.interface`;
- `device.connection`;
- `device.session`;
- `device.stream`;
- `device.screen_context`;
- `device.protocol_operation`;
- `device.backup`.

## Rules

1. `runtime.lease` remains the typed Lease root; WP08 uses lease type `device` and does not create a competing Device Lease identity before WP11.
2. `firmware.compatibility_claim` is one source/tool claim; `firmware.compatibility_result` is the reviewed exact-context decision.
3. `domain.detector_observation` complements generic WP03 `object.detector_observation` with Pack-operation context; adapters may emit both through explicit relationships without identity collapse.
4. `disk.image_revision` is an interpreted role over one exact Object Revision, not a second byte identity.
5. `filesystem.observation` and canonical `filesystem.filesystem` remain separate: several observations may support/conflict before identity selection.
6. protocol-stage, acknowledgement and read-back Verification remain separate entities.
7. Registration does not authorize implementation, mutation capability or public visibility.
