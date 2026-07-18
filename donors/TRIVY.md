# Donor Record — Trivy

**Phase:** 0A / Security and reproduction completion  
**Status:** FIRST-PASS COMPLETE — PRIMARY BROAD ARTIFACT/FILESYSTEM/CONFIGURATION SECURITY SCANNER DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/aquasecurity/trivy
- Default branch: `main`
- Pinned commit: `3c6a1a2aca33893f231412a34d3dfddc4f64b456`
- Licence: Apache-2.0
- Activity: Active
- Primary language: Go
- Classification: container image, filesystem, repository, SBOM, vulnerability, misconfiguration, secret and licence scanner donor
- Ptah targets: broad Artifact security scans, database/policy-bundle freshness, normalized multi-class Findings, ignored/modified results and report interoperability

## Files/components inspected

- `README.md`
- `pkg/types/report.go`
- `pkg/types/version.go`
- current repository/commit activity
- documented target/scanner classes, output formats, databases, policy bundles and attestation paths

## Verified capabilities and patterns

### Target and scanner classes

- Trivy can scan container images, filesystems, repositories and SBOM inputs.
- Result classes include OS packages, language packages, misconfiguration, secrets, licences and custom resources.
- One scan report can contain package inventory, vulnerabilities, configuration findings, secrets and licence observations while retaining class/type separation.
- Target metadata can include image IDs, diff IDs, repository tags/digests, image configuration/layers, repository URL/branch/tags/commit and commit author/message details.
- Artifact IDs in Trivy are scanner-local hashes and are absent for some target classes.

### Structured report and interoperability

- Reports include schema version, Trivy client/server version, report ID, creation time, target metadata and result groups.
- Results retain target, class, type, packages, vulnerabilities, misconfiguration summaries/findings, secrets, licences and custom resources.
- Modified findings can retain results changed from their original state, including ignored/not-affected/severity-adjusted cases.
- Supported outputs include JSON, SARIF, CycloneDX, SPDX, GitHub and cosign-vulnerability formats.
- Report format conversion does not replace retention of native raw output and exact tool configuration.

### Database and policy revision

- Version information separates the Trivy client/server from vulnerability DB, Java DB and check/policy bundle metadata.
- Database metadata includes version, UpdatedAt, NextUpdate and DownloadedAt.
- Check bundles retain digest and download time.
- Findings on unchanged bytes may change when databases or policy bundles change.
- Database/policy freshness is therefore part of the evidence, not incidental runtime state.

### Finding modification and policy lesson

- Scan result and downstream policy are separate: findings can be ignored, marked not affected or severity-adjusted while the modified state remains visible.
- A generic `Failed()` decision in the report model checks presence of selected result classes, but release policy still belongs outside the scanner.
- A passed scan may reflect configuration thresholds, disabled classes, ignored findings or missing/unsupported coverage.

## What Trivy contributes

- One broad scanner for Artifact/package vulnerabilities, IaC/configuration, secrets and licences.
- Structured target metadata and exact image/repository references.
- Explicit database and policy-bundle revision/freshness information.
- Modified/ignored finding retention.
- JSON/SARIF/SPDX/CycloneDX/GitHub interoperability.
- SBOM production/consumption and attestation paths.
- A useful primary all-round security Facility for intake, Build, image and deployment checks.

## Important limitations for Ptah

- Each scanner class has different evidence, false-positive and coverage properties.
- Package vulnerability results inherit inventory and advisory-database limitations.
- Misconfiguration findings depend on policy/check bundle content and context.
- Secret findings can expose credentials in reports and may be false positives or already revoked.
- Licence detections are observations, not legal conclusions.
- Repository/image metadata can be mutable or incomplete unless bound to commit/digest/platform.
- Trivy ArtifactID is not universal or canonical and can include repository context in ways unsuitable for Ptah identity.
- A no-findings result can reflect disabled scanners, stale databases, missing policies, skipped files, unsupported formats or scan errors.
- Modified/ignored findings can hide risk if the original observation and authority/reason are not retained.
- DB/check-bundle download introduces network, registry and supply-chain dependencies.
- Trivy does not prove runtime reachability, exploitability, business impact or successful remediation.
- Scanner output can contain sensitive source, paths, packages and secrets.
- One combined report must not flatten fundamentally different Finding classes.

## Must not be inherited

- Trivy ArtifactID/report ID as canonical Ptah Object, Artifact or Finding identity;
- all scanner classes normalized into one undifferentiated severity list;
- no findings presented without enabled-scanner, error, skip and database/policy context;
- ignored/not-affected/severity-adjusted findings deleted from evidence;
- database/check-bundle metadata omitted;
- mutable image tag or branch used instead of digest/commit/platform;
- secret values retained in plaintext reports or UI;
- licence result presented as legal approval;
- vulnerability match presented as exploitability proof;
- Trivy exit/failure state used directly as universal release policy;
- policy/database updates used to overwrite historical results.

## Integration decision

**ADOPT TRIVY AS THE PRIMARY BROAD ARTIFACT/CONFIGURATION SECURITY SCANNER; KEEP EACH FINDING CLASS, DATABASE/POLICY REVISION, MODIFICATION AND RELEASE DECISION EXPLICIT IN PTAH.**

Recommended Ptah role:

1. bind each scan to exact Object/Artifact/image digest/platform or repository commit;
2. record exact Trivy client/server build, enabled scanners, configuration, DB metadata and policy-bundle digest;
3. retain raw native JSON as an immutable Scanner Report Artifact;
4. normalize vulnerabilities, misconfigurations, secrets and licences into separate Finding classes;
5. redact secret values while retaining hashed/location evidence and revocation status;
6. preserve original and modified/ignored finding states with issuer, reason, scope and expiry;
7. separate scanner result, risk adjudication and release-gate decision;
8. re-scan after target/tool/DB/policy changes as a new revision;
9. correlate with Syft/Grype/Semgrep without hiding shared assumptions or disagreement;
10. permit replacement scanners without changing Ptah Finding identity.

## Native Ptah gap

Ptah must define:

- exact Scan Target and target-resolution record;
- Scanner Configuration and enabled Finding classes;
- vulnerability DB, Java DB and policy/check-bundle revision/freshness;
- raw Scanner Report Artifact;
- Vulnerability, Misconfiguration, Secret and Licence Observation classes;
- secret redaction/hash/revocation evidence;
- original versus modified/ignored/not-affected Finding state;
- issuer/authority/reason/scope/expiry for modifications;
- coverage, skipped, disabled, unsupported and error records;
- multi-scanner correlation and independent evidence;
- risk adjudication and release decision separate from scan;
- re-scan/freshness and historical retention policy.

## Exit strategy

Ptah's scanner/Finding contracts remain independent. Trivy, Grype, Syft, Semgrep, OSV-Scanner, Checkov, secret scanners, licence tools or future products can contribute observations without changing target, Finding, Claim, Evidence or Review identity.

## Validation required

1. Scan one exact image, filesystem, repository and SBOM with pinned target identity.
2. retain enabled scanners, DB versions/times and check-bundle digest.
3. update the DB/policy bundle with unchanged bytes and retain a new report revision.
4. disable one scanner class and prove the no-findings result is visibly partial.
5. ignore/mark-not-affected one Finding and preserve the original observation and authority.
6. detect a secret, redact the value and verify revocation/remediation separately.
7. compare Trivy package results with Syft/Grype and preserve disagreement/shared lineage.
8. compare JSON/SARIF/SPDX/CycloneDX for information loss.
9. prove Trivy failure/exit status is not automatically release acceptance.
10. replace Trivy without identity loss.
