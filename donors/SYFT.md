# Donor Record — Syft

**Phase:** 0A / WP03  
**Status:** FIRST-PASS COMPLETE — SBOM AND PACKAGE-INVENTORY DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/anchore/syft
- Default branch: `main`
- Pinned commit: `3e2bc6ed095f7ec1a415fb38cfe1c319e95dfed6`
- Licence: Apache-2.0
- Activity: Active
- Classification: Package/file catalogue and SBOM generation donor
- Ptah targets: Build/package inventory, filesystem/image inspection, SPDX/CycloneDX outputs and signed SBOM attestation content

## Files/components inspected

- `README.md`
- package/catalogue source locations
- `syft/format/syftjson/model/document.go`
- documented scan targets, ecosystem support, output formats and in-toto attestation path

## Verified capabilities and patterns

- Generates SBOMs from container images, filesystems and archives.
- Supports many package ecosystems including OS packages and Go, Python, Java, JavaScript, Ruby, Rust, PHP and .NET.
- Handles several image formats including OCI and Docker.
- Emits multiple formats including CycloneDX, SPDX and versioned Syft JSON.
- Can convert among supported SBOM formats.
- Can create signed SBOM attestations using in-toto-compatible flows.
- The Syft JSON document contains discovered packages, package relationships, files, original source, detected distribution, generator descriptor and versioned schema.
- Generator descriptor records tool name, version and configuration.
- The project maintains explicit JSON schemas and compatibility handling for earlier document variants.
- Syft is available as both CLI and Go library.

## What Syft completes

- Actual package and file inventory content for Build/Artifact proof.
- Standard SPDX/CycloneDX interoperability.
- Source and generator identity in a versioned SBOM document.
- Package relationships rather than only a flat list.
- A direct bridge to vulnerability scanners and in-toto attestations.
- Inspection of both images and ordinary filesystems/archives.

## Important limitations for Ptah

- An SBOM is a discovery result and may be incomplete because of unsupported formats, hidden dependencies, build-time-only inputs or parser limits.
- Package presence does not establish vulnerability, exploitability, licence compliance or runtime use.
- Syft's `Artifact` term means discovered packages and should not be confused with Ptah Artifact identity.
- SBOM generation does not replace Build provenance, exact source materials, signatures or independent review.
- Different SBOM formats may lose or transform detail.
- Cataloguing large filesystems/images can be expensive and should be a separate Activity.
- Generated SBOM may contain file paths/package metadata requiring privacy review.
- Scanner configuration and catalogue selection influence results and must be retained.
- Syft does not own Ptah Object storage, Activity state, release policy or acceptance.

## Must not be inherited

- Syft package IDs or `Artifact` terminology used as Ptah Artifact identity.
- SBOM generation success promoted to complete dependency knowledge.
- SBOM used as a vulnerability verdict without a separate scanner/database timestamp.
- One output format made universal.
- Tool/configuration identity omitted from retained proof.
- Path/package metadata published without caller privacy classification.
- Syft CLI output used as the only durable inventory record.

## Integration decision

**WRAP SYFT AS THE PRIMARY SBOM/PACKAGE-INVENTORY FACILITY CANDIDATE.**

Ptah should run Syft against selected source/build/result Objects and retain:

- native Syft JSON for maximum recovered detail;
- one or more interoperable SPDX/CycloneDX outputs when required;
- tool/configuration/version receipt;
- source Object/Artifact digest;
- coverage/limitation classification;
- relationship to Build Recipe, Activity and attestation.

## Native Ptah gap

Ptah must define:

- SBOM Artifact type/version and subject relationship;
- source Object/Artifact digest and scan scope;
- generator Facility/version/configuration identity;
- coverage, warnings and unsupported-input fields;
- privacy/redaction classification;
- relationship between pre-build, build-environment and final-output inventories;
- diff/comparison between SBOMs;
- verification/signature/attestation links;
- vulnerability-scan records kept separate from package inventory;
- ORAS/R2/local storage locations and retention.

## Exit strategy

Ptah's SBOM Facility may support Syft, package-manager-native inventories, SPDX/CycloneDX generators or platform-specific tools. Standard outputs and Ptah catalogue relationships remain usable if Syft is replaced.

## Validation required

1. Generate SBOMs from a source directory, OCI image, ordinary filesystem and archive.
2. Retain Syft JSON plus SPDX/CycloneDX and compare information loss.
3. Bind each SBOM to the exact source digest and generator configuration.
4. Scan before and after a build and explain package/file relationship changes.
5. Inject an unsupported or hidden dependency and surface coverage limitations rather than claim completeness.
6. Attach/sign the SBOM through ORAS and Sigstore while preserving independent verification state.
7. Remove sensitive paths/metadata according to a configured redaction class.
8. Run a second SBOM generator on a representative Artifact and record disagreements.
9. Prove SBOM presence remains separate from vulnerability and release acceptance.
