# Phase 0B WP08 — Domain, Firmware, Disk and Device Conventions 0.1.1 Corrections

**Status:** CANDIDATE CORRECTION  
**Date:** 2026-07-19  
**Supersedes:** named/extended clauses in `DOMAIN-FIRMWARE-DISK-DEVICE-CONVENTIONS.md`  
**Implementation authorization:** NONE

## Purpose

Preserve the original WP08 candidate draft while restoring precision from the frozen Phase 0A firmware/device records. All original clauses remain active except where explicitly extended below.

---

# C-001 — Firmware compatibility includes backup-specific authority

The Firmware Compatibility Result outcome family is extended with:

```text
compatible_for_backup
```

Rules:

1. `compatible_for_read` proves only the requested read capability/range;
2. `compatible_for_backup` requires exact range/size/digest/Location/retention and restoration-strategy feasibility;
3. backup compatibility does not imply write compatibility;
4. write compatibility does not remove the backup requirement;
5. compatibility remains operation-specific, exact-context-bound and expiring.

---

# C-002 — Firmware Operation Plan is separate from physical execution

Before any connected-device Operation, Ptah owns an immutable reviewable `firmware.operation_plan` record.

It binds:

```text
package_manifest_component_refs
source_object_and_digest_refs
device_profile_interface_connection_session_refs
provider_pack_tool_loader_programmer_revisions
target_LUN_partition_region_ranges
operation_graph_and_ordering
compatibility_result_ref
mutation_authorization_ref
lease_and_fencing_requirements
backup_requirement_or_exception
retry_and_uncertainty_class
read_back_and_verification_protocol
expected_side_effects
rollback_and_recovery_limits
created_activity_and_receipts
```

Rules:

- parsing rawprogram/patch/payload/scatter/PIT instructions creates a plan, not execution authority;
- plan review cannot mutate the Device;
- physical execution uses WP02 Operations/Attempts under a current Plan, Session, Lease and fence;
- plan revision or target-generation change invalidates prior execution authority;
- raw backend commands remain separate high-risk capabilities disabled by default.

---

# C-003 — Protocol-stage observations include transport authorization and cleanup

The physical protocol-stage vocabulary is extended with:

```text
transport_authorized
cleanup_verified
```

Recommended ordering remains evidence-specific rather than one automatic ladder:

```text
interface_detected
interface_claimed
transport_authorized
protocol_handshake
boot_or_download_mode_confirmed
first_stage_loaded
second_stage_or_programmer_loaded
service_configured
layout_inventoried
read_completed
backup_verified
write_acknowledged
write_read_back_verified
device_reset_observed
device_boot_observed
cleanup_verified
authoritative_external_result
```

A stage is never inferred merely from the previous stage.

---

# C-004 — Cleanup failure quarantines Device authority

Ending a Device Session or Lease does not prove that accounts, data, helper binaries, forwarding rules, temporary credentials, screen/control services or physical state were cleaned.

Cleanup is a separate Activity/Operation with Receipts.

Rules:

1. successful cleanup produces `cleanup_verified` evidence;
2. unverified or failed cleanup blocks ordinary reassignment;
3. affected Device/Session/Interface is placed in an explicit quarantined administrative state or quarantine decision;
4. Provider reachability or successful disconnect cannot restore availability;
5. quarantine release requires authorized remediation plus read-back/inspection evidence;
6. historical cleanup failure remains retained after release.

WP11 completes generic Lease authority; WP08 fixtures must still reject reassignment after cleanup failure.

---

# C-005 — Sensitive public export is allowlisted and remapped

Public or broadly shared exports must not reveal raw:

- IMEI, serials, account identifiers or hardware hashes;
- calibration/NV/RPMB/eFuse data;
- loader/programmer private paths or credentials;
- private firmware/device topology;
- screenshots, hierarchy text, clipboard, logs or partition contents beyond explicit approval.

Exports use remapped Device/Principal identifiers, allowlisted fields, redaction policies and exact audience/retention records. Restricted source evidence may remain linked through protected provenance without entering public bytes.

---

# C-006 — `.P5C` remains parked and extension-only routing is forbidden

`.P5C` is not an accepted supported firmware format.

Until an authoritative sample/specification/tool or verified source recovery exists:

- `.P5C` may be recorded only as an extension/filename Claim;
- it must not be silently classified as Unisoc PAC;
- no Pack may advertise parse, rebuild or physical-execution support;
- output remains `unknown`, `unsupported` or `unsupported_vendor_semantics` with evidence;
- reopening requires a recorded decision, lawful source/provenance and positive/negative fixtures.

---

# C-007 — Driver packages and host-admin changes remain separate

A Device/Firmware Pack may declare a driver or host-admin requirement, but installation/application is a separate authorized Activity.

Records must retain:

- exact driver/package Object and signature/provenance;
- target host/Node/platform/architecture;
- requested host changes and privilege class;
- before/after inventory;
- restart/reboot requirements;
- rollback/uninstall path;
- authorization, Receipts and limitations.

Driver presence does not prove Device Interface readiness or physical-operation compatibility.

---

# Additional conformance cases

1. read compatibility cannot authorize backup/write;
2. backup compatibility requires exact range, digest, durable Location and restoration constraints;
3. parsed rawprogram/scatter/PIT/payload graph cannot execute without an accepted immutable Operation Plan;
4. transport authorization is separate from interface presence and protocol handshake;
5. Session close with failed cleanup quarantines the Device and blocks reassignment;
6. public export redacts/remaps sensitive Device/profile/backup fields;
7. `.P5C` extension-only input remains parked/unsupported;
8. driver package success does not imply Interface/Provider readiness;
9. Plan target/generation changes invalidate execution authority;
10. cleanup verification cannot be inferred from Provider disconnect.

## Do-not-break rule

> Backup compatibility, Operation planning, transport authorization, cleanup verification, quarantine, sensitive export and parked-format status are separately evidenced. None may be inferred from filename, connection, parser success, plan creation, process exit or Session closure.
