# Donor Record — Grype

**Phase:** 0A / Security and reproduction completion  
**Status:** FIRST-PASS COMPLETE — PRIMARY SBOM/ARTIFACT VULNERABILITY-MATCHING DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/anchore/grype
- Default branch: `main`
- Pinned commit: `5917fe588250b59ebe4ee2fc5ebe03b8757f0dcb`
- Licence: Apache-2.0
- Activity: Active
- Primary language: Go
- Classification: container/filesystem/SBOM vulnerability matcher, advisory-database and risk-prioritization donor
- Ptah targets: vulnerability observations, advisory/database provenance, package-to-vulnerability matching, VEX handling and re-scan/freshness rules

## Files/components inspected

- `README.md`
- current repository/commit identity
- documented image/filesystem/SBOM inputs, vulnerability database, risk/EPSS/KEV enrichment, VEX and output behavior

## Verified capabilities and patterns

### Targets and matching

- Grype scans container images, filesystems and SBOM documents.
- It matches OS and language package observations against known vulnerability/advisory data.
- Syft integration provides a common SBOM/package-inventory path.
- Match results can retain package identity/version/type/location, vulnerability/advisory identifiers, fixed versions, severity and related metadata.
- Matching behavior depends on ecosystem-specific version rules and advisory sources.

### Database and enrichment

- Vulnerability results depend on a separately updated vulnerability database.
- Database freshness and tool version materially affect results.
- Risk prioritization can incorporate CVSS/severity, EPSS and known-exploited-vulnerability information.
- These signals represent different questions: technical severity, exploitation probability and known active exploitation.
- VEX/OpenVEX can modify or contextualize applicability, but remains a statement from an issuer with scope and revision.

### Security-evidence lesson

- A package-to-advisory match is a detector Claim, not proof that vulnerable code is reachable or exploitable in the deployed environment.
- A fixed-version suggestion is advisory metadata, not proof that an upgrade is compatible or sufficient.
- Vulnerability status can change without Artifact bytes changing because databases, advisories, VEX and enrichment feeds evolve.
- Re-scans therefore create new Scan Report revisions rather than overwriting historical evidence.

## What Grype contributes

- Broad package-vulnerability matching for images, filesystems and SBOMs.
- Ecosystem-aware version comparison.
- Vulnerability database lifecycle and freshness concerns.
- EPSS, KEV and risk-prioritization inputs.
- VEX-aware result handling.
- Strong complement to Syft inventory and GUAC correlation.
- A practical primary vulnerability matcher for Build and Artifact release evidence.

## Important limitations for Ptah

- Results inherit omissions and identity errors from the input SBOM/catalogue.
- Advisory databases can be stale, incomplete, duplicated or contradictory.
- Package-version matching can produce false positives/negatives for patched vendor packages, forks or unusual version schemes.
- Severity does not equal exploitability, reachability, business impact or release policy.
- EPSS is probabilistic and KEV indicates known exploitation generally, not exposure of this specific deployment.
- VEX statements can be outdated, incorrectly scoped or issued by an untrusted party.
- `fixed in` data does not prove the suggested version is compatible, available or free of other risks.
- A no-findings result is bounded by scanner/database/input coverage.
- The same Artifact can receive different results after database updates.
- Grype does not test live exploitability or application logic.
- Grype IDs/output records are not canonical Ptah Finding or Vulnerability identity.
- Scans can expose proprietary package inventories and require permission/privacy controls.

## Must not be inherited

- Grype match IDs as canonical Ptah Findings;
- severity alone used as release/acceptance policy;
- every advisory match described as reachable or exploitable;
- no findings described as safe/clean;
- database timestamp/version omitted from retained evidence;
- VEX applied without issuer, signature, scope and revision checks;
- EPSS/KEV flattened into CVSS or one universal risk score;
- fixed-version advice automatically applied;
- changed database results used to rewrite historical reports;
- Syft/Grype combined output treated as independent corroboration when both share the same inventory assumptions;
- vulnerability matching used instead of dynamic or manual validation where required.

## Integration decision

**ADOPT GRYPE AS A PRIMARY PACKAGE/ARTIFACT VULNERABILITY-MATCHING FACILITY; NORMALIZE ITS OUTPUT AS VERSIONED CLAIMS UNDER PTAH FINDING, EVIDENCE, REVIEW AND RELEASE-POLICY CONTRACTS.**

Recommended Ptah role:

1. bind each scan to an immutable Artifact/Object or SBOM revision;
2. retain exact Grype build/configuration and vulnerability database metadata;
3. store raw output as an immutable Scanner Report Artifact;
4. normalize matches into Finding Observations with package/advisory evidence;
5. keep severity, EPSS, KEV, reachability, exploitability and business impact separate;
6. apply VEX only as a separately verified contextual Claim;
7. correlate multiple advisories/scanners without erasing disagreement;
8. re-scan on database/tool/SBOM changes as a new revision;
9. route remediation proposals to the owning department/Code Ops and independent review;
10. allow replacement scanners without changing Ptah Finding/Vulnerability identity.

## Native Ptah gap

Ptah must define:

- exact Scan Target/SBOM revision;
- Scanner and Vulnerability Database revision/freshness;
- raw Scanner Report Artifact;
- package-to-vulnerability Observation and matching rationale;
- canonical Vulnerability/Advisory aliases;
- severity, likelihood, KEV, reachability, exploitability and impact fields;
- VEX issuer/signature/scope/revision and applied status;
- Finding correlation/dedup with independent evidence retained;
- false-positive, not-affected, accepted-risk and suppression records;
- remediation proposal and verification/re-scan relationship;
- stale-result and re-scan policy;
- release-policy decision separate from scanner output.

## Exit strategy

Ptah's vulnerability/Finding contracts remain scanner-neutral. Grype, Trivy, OSV-Scanner, vendor tools, language-native audit tools or future matchers can add observations without changing Artifact, Vulnerability, Finding or Review identity.

## Validation required

1. Scan one immutable Artifact directly and through a Syft SBOM and compare results.
2. Pin database metadata and reproduce the same report with the same inputs.
3. update the database and retain changed results as a new report revision.
4. exercise vendor-backported packages and unusual version schemes.
5. apply valid, invalid, stale and contradictory VEX statements.
6. keep CVSS, EPSS, KEV, reachability and impact separate in normalized results.
7. prove a no-findings report is labelled with coverage limits.
8. correlate Grype with Trivy without erasing disagreement.
9. validate a proposed upgrade independently and re-scan the resulting Artifact.
10. replace Grype without changing Ptah identities.
