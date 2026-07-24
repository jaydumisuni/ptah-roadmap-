# I015 — Fastboot engine

Status: candidate record — paired module evidence complete

Primary Archivist: `AF09-P03`
Independent Verifier: `AF09-V03`
Inspected: 2026-07-23

## Canonical source identity
- supporting sources: `jaydumisuni/android-drivers` at `ca582dcdb3058ed4086f717d61fae57de6ef469a` and `jaydumisuni/TechGuyTool-Android-OTA-IdiotProof` at `a4fea0be1bf5ab042fa9e0f23bba985dc05f9e14`;
- standalone engine repository: not established;
- role: Fastboot/Fastbootd transport and technician engine requirements.

## Evidence and boundary
The record establishes driver, device discovery, bootloader/fastbootd distinction, partition/profile and command evidence requirements. The verifier confirmed that unlocked state, command transport and target names do not authorize flashing/erase/bootloader changes.

## Bounded outcome
`accepted_for_archive_fastboot_engine_requirements_with_driver_mode_partition_profile_and_write_authority_boundaries`

Restrictions: require exact device/mode/epoch, driver and partition profile; separate read/query from writes; require backup, lawful approval, anti-rollback/signature checks and post-condition read-back; no standalone source reuse claim.

This outcome does not authorize implementation.