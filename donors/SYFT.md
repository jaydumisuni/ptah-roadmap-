# Donor Record — Syft

**Phase:** 0A / WP03 and security/reproduction completion  
**Status:** FIRST-PASS COMPLETE — PRIMARY SOFTWARE-INVENTORY AND SBOM GENERATION DONOR  
**Inspected:** 2026-07-17; refreshed 2026-07-18

## Identity

- Canonical URL: https://github.com/anchore/syft
- Default branch: `main`
- Current pinned commit: `ae9534203d4a49f2b96a05dfc1383e2376993c72`
- Earlier WP03 inspection pin: `3e2bc6ed095f7ec1a415fb38cfe1c319e95dfed6`
- Licence: Apache-2.0
- Activity: Active
- Primary language: Go
- Classification: container/filesystem/archive package cataloguer, software inventory and SBOM generation donor
- Ptah targets: Build/Artifact package inventory, SBOM generation, package/file relationships, catalogue coverage and supply-chain evidence

## Files/components inspected

- `README.md`
- package/catalogue source locations
- `syft/format/syftjson/model/document.go`
- documented image/filesystem/archive targets, ecosystem support, output formats, conversion and attestation paths
- current repository/commit identity

## Verified capabilities and patterns

- Generates SBOMs from container images, filesystems and archives.
- Supports many OS and language package ecosystems.
- Resolves several image inputs including OCI and Docker representations.
- Emits versioned native Syft JSON plus SPDX and CycloneDX formats.
- Native documents retain source, generator/configuration, packages, files and relationships.
- Existing SBOMs can participate in supported conversion/input workflows.
- External in-toto/signing flows can bind an SBOM document to supply-chain attestations.
- Cataloguers inspect package databases, manifests, lockfiles, binaries and files according to target and configuration.
- Multiple catalogue methods can find the same package or disagree.
- Package locations and detector evidence are valuable and should not be flattened away.

## What Syft completes

- Broad package and file inventory for source, Build and final Artifacts.
- Standard SPDX/CycloneDX interoperability.
- Detailed native inventory and package relationships.
- Source and generator identity in a versioned SBOM document.
- A direct bridge to Grype, GUAC and attestation workflows.
- A practical primary SBOM Facility for Ptah Build and Artifact evidence.

## Important limitations for Ptah

- An SBOM is an observed inventory, not proof of complete software composition.
- Static inspection may miss runtime-loaded, remotely fetched, generated, encrypted or unsupported components.
- Package metadata may be absent, stale, malformed or misleading.
- Multiple cataloguers and ecosystems can duplicate or disagree on package identity/version.
- Image tags are mutable; digest and platform must be resolved before scanning.
- Different formats vary in expressiveness and conversion may lose data.
- PURL, CPE and licence metadata remain detector assertions requiring source/confidence.
- Tool, configuration or cataloguer changes can alter results with unchanged bytes.
- `no packages found` may mean opaque/unsupported input rather than empty software.
- Signed attestation proves signer/document binding, not inventory completeness or correctness.
- File paths/package metadata may be sensitive.
- Syft does not determine vulnerability exploitability, runtime reachability or release acceptance.
- Syft's use of `Artifact` terminology must not replace Ptah Artifact identity.

## Must not be inherited

- Syft package IDs, source paths or `Artifact` terms as canonical Ptah identities;
- mutable image tags scanned without resolved digest/platform;
- one SBOM treated as complete source truth;
- duplicate detector results collapsed without retained evidence;
- SPDX/CycloneDX conversion described as lossless without comparison;
- PURL/CPE/licence guesses accepted without provenance;
- zero discovered packages interpreted as proof of no software;
- SBOM signature interpreted as correctness;
- scanner/configuration/cataloguers omitted from evidence;
- SBOM generation used instead of Build provenance or runtime observation.

## Integration decision

**ADOPT SYFT AS THE PRIMARY SBOM/STATIC SOFTWARE-INVENTORY FACILITY BEHIND PTAH ARTIFACT, CLAIM, EVIDENCE AND PROVENANCE CONTRACTS.**

Recommended Ptah role:

1. resolve the Scan Target to an immutable Object/Artifact digest and platform;
2. record exact Syft binary/build, configuration, cataloguers and target provider;
3. retain native raw output as an immutable Scanner Report Artifact;
4. normalize package observations as Claims while preserving locations/cataloguer provenance;
5. emit SPDX/CycloneDX as derived interoperable Views;
6. retain disagreement, unsupported input, skipped content and extraction errors;
7. attach SBOMs to Build/Artifact provenance without claiming completeness;
8. ingest approved SBOMs into Grype/GUAC through explicit Activities;
9. re-scan after catalogue/tool changes as a new SBOM Revision;
10. permit replacement generators without changing Ptah identities.

## Native Ptah gap

Ptah must define:

- exact Scan Target and Artifact/Object/platform revision;
- Scanner and Cataloguer Set revision;
- raw Scanner Report Artifact;
- Package Observation/Claim and evidence location;
- identity aliases, PURL/CPE confidence and conflicts;
- SBOM Document and SBOM Revision;
- coverage, skipped, unsupported and extraction-error records;
- native versus SPDX/CycloneDX View relationships;
- signature/attestation and signer-trust records;
- SBOM diff, freshness and re-scan policy;
- privacy/redaction classification;
- multi-scanner correlation and review.

## Exit strategy

Ptah's SBOM/package-observation contracts remain independent. Syft, Trivy, cdxgen, package-manager-native tools, BuildKit metadata or future generators can contribute observations without changing Artifact, Package, Claim or Evidence identity.

## Validation required

1. Scan one immutable image through registry, OCI archive and unpacked filesystem paths.
2. Resolve mutable tags to exact digest/platform.
3. Run different cataloguer sets and retain additions/removals/disagreements.
4. Compare native, SPDX and CycloneDX outputs for information loss.
5. Exercise opaque, generated and runtime-loaded cases and retain coverage limits.
6. Sign an SBOM and prove signature does not imply completeness.
7. Re-scan unchanged bytes with a new Syft/cataloguer version as a new revision.
8. Feed one SBOM to Grype and GUAC while preserving original provenance.
9. redact sensitive paths/details for unauthorized audiences.
10. Replace Syft without identity loss.
