# Phase 0A — WP03 Build, Artifact and Provenance Composition

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Runtime code:** NOT STARTED

## Purpose

Close the deterministic Build, Artifact storage/relationship, SBOM, attestation, signing and independent-verification requirements through one composite donor set.

## Sources inspected and saved

### Internal

- THETECHGUY Software Builder

### External and upstream

- BuildKit
- Dagger
- ORAS
- Witness
- in-toto
- Cosign
- Rekor
- Fulcio
- sigstore-go
- Syft
- OCI Image/Distribution specifications from the earlier runtime inspection

Saved records:

- `internal/SOFTWARE-BUILDER.md`
- `donors/BUILDKIT.md`
- `donors/DAGGER.md`
- `donors/ORAS.md`
- `donors/WITNESS.md`
- `donors/IN-TOTO.md`
- `donors/SIGSTORE-COSIGN-REKOR-FULCIO.md`
- `donors/SYFT.md`

## Composite result

```text
Ptah Build Recipe
  portable caller-visible intended work

Internal Software Builder
  source/project detection, readiness, target planning,
  shared machinery and user-facing requirements

Dagger
  typed programmable recipe/module layer and optional backend

BuildKit
  low-level DAG, workers, cache, secret mounts and exporters

Ptah Object/Artifact Graph
  immutable output identity, relationships and storage locations

ORAS + OCI
  OCI registry/layout transport and subject/referrer relationships

Syft
  package/file inventory and SPDX/CycloneDX/Syft SBOMs

Witness + in-toto
  attestors, materials/products, planned steps, DSSE and policy verification

Cosign/Sigstore/Fulcio/Rekor
  digest signing, signer identity, trust roots, offline bundles
  and transparency evidence

Ptah Receipts/Review/Reproduction
  proof levels, authoritative state, independent checks and acceptance
```

No component is universal Ptah truth.

## Accepted architecture

Saved as `decisions/ADR-0005-BUILD-ARTIFACT-PROVENANCE-BOUNDARY.md`.

Key decisions:

1. Ptah owns Build Recipe, Build Activity Graph, Object/Artifact Graph and Provenance/Verification Graph contracts.
2. BuildKit is the primary low-level engine candidate for suitable OCI/container builds.
3. Dagger is the primary typed recipe/module donor and optional execution backend.
4. The internal Software Builder contributes scanner/readiness/shared-environment and private release requirements, not the complete engine.
5. Native Windows/macOS/device/firmware and other builds remain alternative backends under the same Build Facility contract.
6. Cache is reusable derived state, not source truth or independent proof.
7. Volatile inputs that bypass cache identity must reduce reproducibility trust explicitly.
8. Secrets are opaque references and must not enter logs, caches, SBOMs, attestations or public recipes.
9. Ptah Artifact identity is content/object based and survives registry/tag/storage movement.
10. ORAS is a transport/relationship backend, not the universal Object store.
11. Syft SBOMs are inventory claims with explicit coverage limits, not dependency completeness or vulnerability verdicts.
12. Witness/in-toto attest planned and observed production chains; caller policy remains outside Ptah authority.
13. Sigstore verifies digest binding and signer identity under a trust root; signatures do not prove functional correctness.
14. Build, hash verification, SBOM, attestation, signature, review, reproduction and release acceptance are distinct levels.
15. Independent reproduction is not a cache hit on the original backend.

## Requirement closure verdict

Closed for Phase 0B contract design:

- `EXEC-003` Reproducible Build graph
- `STORE-002` durable Artifact storage class and backend abstraction direction
- `STORE-004` content hashing/deduplication foundation
- `PROV-001` provenance, attestations, signing and proof bundles
- Build-side portions of `PLUGIN-001`
- Build-side portions of `OBS-001`
- Build Artifact relationship portions of `CORE-003`

Still dependent on later groups:

- general Object catalogue and storage implementation (`CORE-003`, `STORE-001/003`);
- transfer/upload/download/synchronization backends;
- plugin registry/lifecycle beyond Build modules;
- vulnerability/security review (`SEC-001`);
- platform-specific Build Facilities;
- human UI and release-control adapters.

## Phase 0B contracts required

1. Build Recipe schema and hash.
2. Recipe capability/platform/toolchain requirements.
3. Backend compilation/adapter record.
4. Build operation/step mapping to Activity IDs.
5. Cache record and reproducibility-impact schema.
6. Secret/credential access receipt.
7. Artifact and relationship schemas.
8. Storage location, immutable digest and mutable alias schema.
9. SBOM record, coverage and generator identity.
10. Attestation and policy-verification records.
11. Signature, trust-root, transparency and offline-bundle records.
12. Verification/reproduction level taxonomy.
13. Partial Build/export/SBOM/attestation/signing failure states.
14. Private signing/release adapter boundary.
15. Backend exit/migration tests.

## Validation set

- parallel Build graph execution;
- exact cache reuse/invalidation evidence;
- secret-leak prevention;
- multiple Artifact outputs and storage locations;
- ORAS subject/referrer graph;
- Syft inventory with coverage limitations;
- Witness/in-toto policy verification;
- keyless/private/offline signature verification;
- mutable tag movement without identity loss;
- failed proof/signing after successful Build retains partial state;
- independent reproduction classification;
- Dagger/BuildKit backend replacement proof.

## Next Phase 0A group

Proceed with the **storage, transfer and synchronization cluster**:

- internal Download Manager/Lumi recovery;
- aria2;
- tus/tusd;
- rclone;
- Syncthing;
- restic;
- local content-addressed storage and metadata catalogue patterns;
- R2/S3/Drive transport;
- online/local Object revisions and conflict model.

This group must close active bytes, resumable intake, cloud/Node movement, backups, versions and synchronization without turning Drive/object storage into a live Build filesystem.
