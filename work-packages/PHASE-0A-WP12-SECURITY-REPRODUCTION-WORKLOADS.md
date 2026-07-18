# Phase 0A — WP12 Security Evidence, Reproduction and Workload Proof

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Runtime code:** NOT STARTED

## Purpose

Close Ptah's security-scanning, evidence, authorization, remediation and reproducibility boundaries without allowing a tool report, agent statement, signature, evidence card, graph or replay bundle to become authority by itself.

This work package completes the planning foundation for Master Roadmap Phase 11 — Provenance, signing, security evidence and workload proof.

## Sources inspected and saved

| Donor | Primary role | Record |
|---|---|---|
| ReproZip | observed execution dependency capture and replay | `donors/REPROZIP.md` |
| Syft | package inventory and SBOM generation | `donors/SYFT.md` |
| Grype | package/advisory matching | `donors/GRYPE.md` |
| GUAC | derived security/provenance graph | `donors/GUAC.md` |
| Semgrep | source and configuration analysis | `donors/SEMGREP.md` |
| Trivy | Artifact, configuration, secret and licence scanning | `donors/TRIVY.md` |
| OWASP ZAP | authorized dynamic web/API testing | `donors/ZAPROXY.md` |
| Strix | optional agentic validation workload | `donors/STRIX.md` |
| ClaimBound Evidence | narrow evidence cards and claim boundaries | `donors/CLAIMBOUND.md` |
| SparkDistill | recipe/data/checkpoint/claim/attestation/recheck separation | `donors/SPARKDISTILL.md` |

## Canonical pins

- ReproZip: `44687ce73efe7a889bf7a1ea982258e2d965c766`
- GUAC: `c66a25f6f15819609fc8bbf4d961d1e0ec78d671`
- Syft: `ae9534203d4a49f2b96a05dfc1383e2376993c72`
- Grype: `5917fe588250b59ebe4ee2fc5ebe03b8757f0dcb`
- Semgrep: `1f15ff4eb9f56f5a3b6a9afb958bdc82b5b6bcb0`
- Trivy: `3c6a1a2aca33893f231412a34d3dfddc4f64b456`
- OWASP ZAP: `eef487d8d65d91f182ef6f82a26b01376872c07b`
- Strix: `7d5a67d234bd3faef34d22be8c6f5a9607de41a3`
- ClaimBound Evidence: `a55bc4339f92f3b45e97e6ba4aceca2949e31f51`
- SparkDistill: `8721faaf9e7a6464df32a74a6fa0e9ff6435e878`

## Licence findings

- ReproZip: BSD-3-Clause.
- GUAC, Syft, Grype, Trivy, ZAP, Strix and ClaimBound: Apache-2.0 at the inspected roots.
- Semgrep open engine: LGPL-2.1-or-later; advanced services remain separate.
- SparkDistill source: MIT; datasets, models and provider outputs require independent rights review.
- Rules, databases, policy bundles, add-ons, images, models and dependencies require independent provenance/licence review.

## Composite model

```text
Scan Target
Scanner Revision
Security Test Authorization
Scan Activity and attempt
Raw Scanner Report Artifact
Finding Observation
Stable Finding
Bounded Claim
Evidence and Evidence Relationships
Risk Assessment
Adjudication
Exception or Accepted Risk
Remediation Proposal and Change
Verification and Closure
Reproduction Recipe
Reproduction Bundle
Reproduction Run and Comparison
Evidence Card View
Security Graph Revision
Independent Review and Release Decision
```

Tool-local rule, alert, report, package, task, graph and card IDs remain adapter metadata.

## Closed architecture

1. Scan Activity state, Finding Observation, stable Finding, Claim, Evidence, risk, adjudication, reproduction, independent review and release acceptance remain separate.
2. Every scan binds to an exact target revision and exact tool, engine, ruleset, database, policy, add-on and model/provider revision.
3. Native raw reports, errors, skipped inputs and coverage records remain immutable restricted Artifacts.
4. Finding classes remain separate: inventory, advisory match, source analysis, configuration, secret, licence, dynamic, runtime, provenance, privacy and agent/manual claims.
5. `No findings` is bounded by successful recorded scope, enabled classes, database/rule freshness and limitations; it never means universally safe.
6. Every detector output remains a Finding Observation. Correlation, split, merge and duplicate relationships are reviewable Claims and never erase evidence.
7. Risk keeps severity, confidence, reachability, exploitability, known exploitation, likelihood, business impact, exposure, criticality, cost and uncertainty separate.
8. Adjudication and exceptions retain issuer, rationale, exact scope, evidence and expiry without deleting the original observation.
9. State-changing, credentialed, load-producing or autonomous security work requires an externally approved Security Test Authorization.
10. A URL, repository or reachable service is never authorization, and a tool cannot expand its own scope.
11. Security tools may propose changes; Code Ops or the correct specialist department owns implementation, Sergeant owns independent proof where applicable, and organization policy owns risk/release acceptance.
12. Verified closure requires the approved change, relevant build/deployment evidence, targeted verification, negative read-back, regression checks and authorized reviewer acceptance.
13. Reproduction Recipe, Bundle, Run and Comparison remain separate. Bundle assembly or signature does not prove reproduction.
14. Reproduction levels distinguish manifest-only, integrity verification, command replay, semantic comparison, partial/full independent reproduction, failed and blocked outcomes.
15. Public Evidence Cards are permission-filtered Views over restricted raw records and always retain the narrow claim boundary and limitations.
16. GUAC or another security graph remains a derived, versioned, permission-filtered and rebuildable index over retained source documents.
17. Every donor remains optional and replaceable behind Ptah contracts.

## Donor placement

- **Syft:** primary SBOM/package inventory Facility.
- **Grype:** primary package/advisory matching Facility.
- **Trivy:** primary broad Artifact/configuration scanner.
- **Semgrep:** primary source-level static-analysis Facility.
- **OWASP ZAP:** primary authorized dynamic web/API scanner.
- **Strix:** optional caller-owned agentic validation workload requiring independent verification.
- **ReproZip:** optional observed dependency capture/replay Facility.
- **GUAC:** optional derived security/provenance graph Facility.
- **ClaimBound Evidence:** primary narrow public evidence-card donor.
- **SparkDistill:** optional AI-training reproduction workload.

## Accepted decision

Saved as:

- `decisions/ADR-0016-SECURITY-FINDING-CLAIM-EVIDENCE-REPRODUCTION-BOUNDARY.md`

## Requirement closure verdict

Closed for Phase 0B contract design:

- `SECURITY-001` scanner execution, Findings, Claims, Evidence, risk, authorization, exceptions, remediation and closure;
- `REPRO-001` Reproduction Recipe, Bundle, Run, Comparison and reproduction levels;
- security completion portions of `PROV-001`, `SEARCH-001`, `PLUGIN-001`, `ISOLATION-001`, `UI-002`, `OBS-001` and `SESSION-001`.

No scanner service, security graph, validation agent, reproduction engine, Finding database, policy engine or security UI implementation is approved yet.

## Phase 0B contracts required

1. Security Test Authorization.
2. Scan Target and Scanner Revision.
3. Scan Activity and raw Scanner Report Artifact.
4. Finding Observation and stable Finding.
5. Claim and Evidence.
6. Risk Assessment and Adjudication.
7. Suppression, Exception and Accepted Risk.
8. Remediation and verified closure.
9. Reproduction Recipe, Bundle, Run and Comparison.
10. Evidence Card View.
11. Security Graph Revision.
12. coverage, negative, blocked and drift records.
13. sensitive-evidence, redaction, retention and audience policy.
14. backend replacement and historical migration.

## Validation set

- exact target and scanner revision pinning;
- no-findings with explicit skipped/unsupported/error coverage;
- changed rules/databases/policies against unchanged target bytes;
- multi-scanner disagreement retained;
- reviewed Finding split/merge/correlation;
- exceptions with exact scope and expiry;
- sensitive-result redaction and revocation evidence;
- authorized tests blocked outside scope;
- emergency stop, cleanup and read-back;
- agent-originated claims independently validated or rejected;
- proposed changes routed through specialist ownership and Sergeant review;
- trace-versus-package drift detection;
- exact/semantic/tolerance reproduction comparisons;
- failed and blocked reproduction retained;
- signatures/attestations kept separate from semantic proof;
- public pass/negative/blocked/drift Evidence Card Views;
- security graph rebuilt from source Objects;
- donor replacement without Ptah identity loss.

## Next Phase 0A work

1. research/documentation-source and unresolved-profile cleanup;
2. cross-requirement Phase 0A review;
3. explicit parked/rejected-gap audit;
4. Phase 0A freeze/readiness decision for Phase 0B.

No runtime implementation is approved yet.
