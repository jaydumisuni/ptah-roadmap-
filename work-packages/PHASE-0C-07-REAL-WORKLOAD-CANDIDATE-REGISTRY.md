# Phase 0C-07 — Real workload candidate registry

Status: candidate registry — not an implementation authorization or dependency selection

## Purpose

Preserve the real workloads identified during Phase 0C so Ptah is validated against genuine systems and THETECHGUY operating requirements rather than only synthetic demos. These workloads do not replace the frozen WP14 first slice and do not become Ptah Core.

## Candidate A — `jaydumisuni/linux-0.11-rs`

Classification:

- external systems workload;
- kernel, userland, QEMU/serial and disk-image laboratory;
- GPL code remains outside Apache-licensed Ptah Core;
- independently MIT-licensed image utilities may be evaluated separately.

Potential proofs:

- hardened Git clone;
- Rust build and build provenance;
- concurrent compilation Activities;
- MBR and Minix image production;
- Object/Artifact registration;
- archive/disk/filesystem decomposition;
- QEMU process supervision;
- serial terminal streaming;
- deterministic test execution;
- detach/reconnect and reproduction.

Boundary:

The repository is executed as a separate workload. Kernel implementation code is not copied into Ptah Core. Upstream/fork lineage, licences and exact commit are retained.

## Candidate B — `jaydumisuni/MIBU`

Classification:

- internal THETECHGUY Application/Device workload;
- Windows helper plus Android application and official-tool handoff;
- candidate private Domain Pack/Plugin and physical-device conformance workload.

Potential proofs:

- exact ADB device selection;
- application installation/version verification;
- nonce-correlated cross-device evidence;
- secret-reference and expiry handling;
- foreground-service recovery;
- ADB-to-fastboot connection-epoch transition;
- external official-result authority;
- retained negative/inconclusive outcomes;
- APK/Windows release Artifact composition and checksums.

Boundary:

MIBU-specific logic, captures, customer/device data and official-service workflow remain outside public Ptah Core. Ptah provides generic Device, Application, Evidence, Secure Grant and Recipe boundaries.

## Candidate C — `jaydumisuni/TTG-Device-X-Ray`

Classification:

- internal read-first Device Detector and evidence producer;
- candidate WP08 Detector/Domain Pack integration workload;
- not a destructive repair adapter.

Potential proofs:

- ADB, Fastboot/Fastbootd, Apple and MTK META observations;
- multi-transport correlation and disagreement;
- per-device candidate grouping;
- firmware fingerprint and storage summary;
- partition-map evidence;
- read-only IPSW inspection;
- signed/digest-sealed evidence bundle;
- exact Profile Revision proposal and reviewed match;
- stale evidence and multiple-device rejection.

Boundary:

X-Ray may observe, correlate, challenge, certify evidence and recommend. It must not authorize or execute destructive writes. Certified evidence is not repair authorization.

## Candidate D — `jaydumisuni/thetechguy-device-manager`

Classification:

- internal Android Device Owner/DPC workload;
- candidate policy and application-session Provider;
- existing ADB-session helper, not a universal disabled-ADB recovery mechanism.

Potential proofs:

- QR/device-owner provisioning;
- package/version/signature verification;
- Device Owner policy operation;
- reversible application visibility policy;
- policy Receipt and independent state verification;
- application restart and persistent policy state;
- policy rollback and cleanup;
- authorized USB ADB to legacy TCP/IP transition as a separate capability.

Boundary:

Raw partition, FRP, MDM-removal and other destructive recovery operations do not belong in the DPC Provider. Restricted operations require a separate Approved Device Recovery adapter with case, consent, identity, immutable backup, authorization and read-back verification.

## Admission order

These workloads are not prerequisites for the smallest first slice. Recommended admission sequence after the generic slice proves its substrate:

```text
1. linux-0.11-rs systems workload
2. TTG Device X-Ray read-only evidence workload
3. Device Manager reversible DPC policy workload
4. MIBU cross-application/device workflow
5. separately reviewed Approved Device Recovery adapters
```

## Admission requirements

Before any candidate is admitted:

- exact repository commit is pinned;
- ownership and licence inventory is recorded;
- public/private data boundary is defined;
- expected Ptah entities and lifecycle projections are mapped;
- positive, negative and disconnect/recovery fixtures exist;
- secrets and customer/device identifiers are excluded from public fixtures;
- backend/workload IDs remain Aliases;
- the workload cannot weaken WP13/WP14 proof requirements.

## Non-selection statement

This registry records useful workloads. It does not select any of them as a production dependency, public Ptah Core component or first-slice authorization blocker.