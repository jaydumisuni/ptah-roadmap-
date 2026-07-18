# Phase 0A — WP12 Security Evidence, Reproduction and Workload Proof

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Runtime code:** NOT STARTED

## Purpose

Close Ptah's security-scanning, evidence, authorization, remediation and reproducibility boundaries without allowing a tool report, agent statement, signature, evidence card or replay bundle to become authority by itself.

This work package completes the planning foundation for Master Roadmap Phase 11 — Provenance, signing, security evidence and workload proof.

## Sources inspected and saved

- ReproZip — execution dependency capture and replay.
- Syft — package inventory and SBOM generation.
- Grype — package/advisory matching.
- GUAC — derived security/provenance graph.
- Semgrep — source and configuration analysis.
- Trivy — Artifact, configuration, secret and licence scanning.
- OWASP ZAP — authorized dynamic web/API testing.
- Strix — optional agentic validation workload.
- ClaimBound Evidence — narrow evidence cards and claim boundaries.
- SparkDistill — recipe/data/checkpoint/claim/attestation/recheck separation.

Saved records:

- `donors/REPROZIP.md`
- `donors/SYFT.md`
- `donors/GRYPE.md`
- `donors/GUAC.md`
- `donors/SEMGREP.md`
- `donors/TRIVY.md`
- `donors/ZAPROXY.md`
- `donors/STRIX.md`
- `donors/CLAIMBOUND.md`
- `donors/SPARKDISTILL.md`

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
- Rules, databases, policy bundles, add-ons, images, models and dependencies require their own provenance and licence records.

## Composite model

```text
Scan Target
  exact Object, Artifact, commit, image digest/platform,
  deployment, Application Session, Device or environment revision

Scanner Revision
  tool/build, engine/tier, configuration, rules, databases,
  policy bundle, add-ons and model/provider revision

Security Test Authorization
  target owner, basis, exact scope, permitted test classes,
  credentials, rate/time limits, isolation and cleanup

Scan Activity
  Activity/operation/attempt under one authorization,
  target and scanner revision

Raw Scanner Report Artifact
  native report, logs, errors, skipped scope and metadata

Finding Observation
  one detector/source assertion with exact evidence

Stable Finding
  reviewable correlation across observations and revisions

Claim
  one bounded allowed sentence under one exact protocol

Evidence
  immutable support, contradiction, limitation or reproduction material

Risk Assessment
  severity, confidence, reachability, likelihood, impact and uncertainty

Adjudication
  named review decision without deleting the observation

Exception / Accepted Risk
  named authority, reason, exact scope and expiry

Remediation Proposal / Change
  routed to the correct specialist owner

Verification / Closure
  new build, deployment, re-scan, read-back and review evidence

Reproduction Recipe / Bundle / Run / Comparison
  frozen recipe and materials, new execution and explicit comparison

Evidence Card View
  public-safe narrow claim with result, reproduction and limitations

Security Graph Revision
  optional rebuildable graph over retained source documents
```

Tool-local report, rule, alert, package, graph, task and card identifiers remain adapter metadata.

## Security truth classes

Ptah keeps separate:

1. Scan Activity state.
2. Finding Observation.
3. Stable Finding.
4. Claim.
5. Evidence.
6. Risk Assessment.
7. Adjudication.
8. Reproduction level.
9. Independent review.
10. Release or acceptance decision.

No single field or colour may replace these distinctions.

## Finding classes

Ptah retains separate semantics for:

- software inventory;
- known vulnerability/advisory matches;
- source/static analysis;
- configuration and Infrastructure-as-Code;
- secret/credential exposure;
- licence observations;
- dynamic web/API testing;
- runtime/behavioral evidence;
- supply-chain/provenance findings;
- binary/malware findings;
- privacy/data exposure;
- manual or agentic security claims.

An inventory is not a vulnerability verdict. An advisory match is not exploitability proof. Static analysis is not runtime proof. A licence observation is not legal approval.

## Coverage and negative evidence

Every scan records requested, resolved, successfully scanned, skipped and unsupported scope, plus errors, timeouts, disabled classes and unavailable/stale rules or databases.

`No findings` means only that no observations were produced inside the recorded successful scope and limitations. It never means universally safe or secure.

Negative, blocked, partial, drifted and failed-to-reproduce outcomes remain first-class evidence.

## Donor roles

### Syft

Primary package/SBOM inventory Facility. Native output is retained; SPDX/CycloneDX are derived Views; target digest/platform and catalogue coverage are explicit.

### Grype

Primary package/advisory matcher. Database revision is mandatory. Severity, probability, known exploitation, reachability and impact remain separate. VEX remains a scoped issuer Claim.

### Trivy

Primary broad Artifact/configuration scanner. Vulnerability, configuration, secret and licence classes remain separate. Database and policy-bundle revisions are retained. Original and modified/ignored states remain visible.

### Semgrep

Primary source-level static-analysis Facility. Source ranges, ruleset, engine tier, dataflow, errors and skipped scope are retained. Suggested changes remain remediation proposals.

### OWASP ZAP

Primary authorized dynamic web/API scanner. Passive and active modes, target context, authentication state, rules/add-ons and HTTP evidence are retained. Raw alerts, review and release gates remain separate.

### Strix

Optional agentic validation workload. Model/provider/prompt/tools/sandbox are fixed per run. Its findings, proof material, scores and proposed changes remain agent-originated Claims requiring independent validation.

### ReproZip

Optional observed dependency capture/replay Facility. Trace, edited recipe, bundle and replay remain separate. Bundle creation does not prove reproduction.

### GUAC

Optional derived security/provenance graph. Original SBOMs, attestations, advisories and reports remain authoritative. Graph edges retain source/parser lineage, uncertainty and rebuildability.

### ClaimBound Evidence

Primary narrow evidence-card donor. Allowed claim sentence and explicit boundary are mandatory. Result, reproduction, verification and review remain separate. Public summaries do not replace restricted raw evidence.

### SparkDistill

Optional AI-training reproduction workload. Recipe, data, checkpoint, metric claim, attestation and recheck remain separate. Validation levels and rights/licences are explicit. No automatic promotion into a caller product is permitted.

## Authorization boundary

A Security Test Authorization is mandatory before any state-changing, credentialed, load-producing or autonomous validation work.

It fixes:

- requestor, approver and target owner;
- legal/policy basis;
- exact target/environment revision;
- included and excluded hosts, routes, accounts and assets;
- permitted and prohibited test classes;
- rate, time, cost and change budgets;
- credential/test-data references;
- required isolation and network boundaries;
- monitoring and emergency stop;
- backup, cleanup and read-back plan;
- incident contacts and expiry.

A URL, repository or reachable service is never authorization.

## Risk, adjudication and correlation

Risk retains distinct fields for scanner severity, standard scores, confidence, reachability, likelihood, known exploitation, business impact, exposure, criticality, remediation cost and uncertainty.

Adjudication remains a named decision such as unreviewed, confirmed, possible, false positive, not applicable, not affected, related, needs more evidence or accepted risk.

Every detector result remains a Finding Observation. Stable Finding correlation, split, merge and duplicate relationships are reviewable Claims. Fingerprints and external identifiers remain aliases. Independent agreement and disagreement remain visible.

## Exceptions and accepted risk

Suppressions never delete evidence. Each exception records issuer, rationale, exact scope, compensating controls, creation, expiry and review date. Expired exceptions return to review-required state.

## Remediation ownership and closure

- Code Ops owns code patches.
- The correct specialist department owns its configuration, infrastructure, device or other changes.
- Sergeant owns independent engineering review and proof where applicable.
- Organizational policy owns risk acceptance and release approval.
- Ptah records authority, execution and evidence but does not become the organizational approver.

Verified closure requires an approved change, relevant build/deployment evidence, targeted re-scan or reproduction, negative read-back for the original issue, no unacceptable regression and authorized reviewer acceptance.

## Reproduction model

A Reproduction Recipe retains source/input Objects, commands or Activity graph, environment/toolchain, Node capabilities, external services, credentials/fixtures, clock/randomness/locale, expected outputs/tolerances, cleanup and known uncaptured state.

A Reproduction Bundle is an immutable signed Artifact. Bundle assembly is not reproduction proof.

A Reproduction Run is a new Activity/attempt. Comparison retains exact hashes, semantic/tolerance results, logs, external read-back, variance and limitations.

Closed reproduction levels:

```text
manifest_only
artifact_integrity_verified
commands_replayed
outputs_semantically_compared
partial_independent_reproduction
full_independent_reproduction
failed_to_reproduce
blocked
```

Signature or attestation proves identity/integrity under a trust chain, not semantic correctness or reproduction.

## Public/private evidence boundary

Security evidence is restricted by default. Public-safe Evidence Cards may expose only approved narrow claims, boundaries, protocol/tool revisions, hashes, result/reproduction/review levels, limitations and non-sensitive closure summaries.

Visual status always travels with the claim boundary and limitations.

## Security graph

GUAC or a native graph may index packages, sources, Artifacts, SBOMs, attestations, advisories, Findings, remediations, scanners and reproduction relationships.

The graph remains a derived, permission-filtered, versioned Index Revision. Source documents are retained and the graph can be rebuilt or replaced.

## Accepted architecture

Saved as:

- `decisions/ADR-0015-SECURITY-FINDING-CLAIM-EVIDENCE-REPRODUCTION-BOUNDARY.md`

Key decisions:

1. Tool result, Finding, Claim, Evidence, risk, adjudication, reproduction, review and acceptance remain separate.
2. Every scan binds to an exact target and scanner/rule/database/policy/model revision.
3. Native reports remain immutable Artifacts.
4. No-findings is always bounded by coverage and limitations.
5. Finding correlation preserves every Observation and disagreement.
6. Risk is multidimensional.
7. State-changing and autonomous tests require external authorization and cleanup.
8. Tools cannot authorize their own scope.
9. Signed or attested reports do not become correct by signature alone.
10. Replay bundles do not become reproductions without rerun and comparison.
11. Suggested changes remain proposals routed to specialist owners and independent review.
12. Public Evidence Cards are Views over restricted raw records.
13. Security graphs are derived and rebuildable.
14. Every donor remains replaceable.

## Requirement closure verdict

Closed for Phase 0B contract design:

- `SECURITY-001` scanner execution, Finding Observation, Finding correlation, risk, adjudication, authorization, exceptions, remediation and closure;
- `REPRO-001` Reproduction Recipe, Bundle, Run, Comparison and reproduction levels;
- security-evidence completion portions of `PROV-001`;
- security search portions of `SEARCH-001`;
- security runtime portions of `PLUGIN-001` and `ISOLATION-001`;
- active-test evidence portions of Browser and Application requirements;
- evidence/review projections of `UI-002`;
- resource/telemetry portions of `OBS-001`;
- security-session/evidence retention portions of `SESSION-001`.

No scanner service, graph, validation agent, reproduction engine, Finding database, policy engine or security UI implementation is approved yet.

## Phase 0B contracts required

1. Security Test Authorization.
2. Scan Target and Target Revision.
3. Scanner/Engine/Ruleset/Database/Policy/Model Revision.
4. Scan Activity and raw Scanner Report Artifact.
5. Finding Observation and stable Finding.
6. Claim and allowed claim boundary.
7. Evidence and relationships.
8. Risk Assessment and Adjudication.
9. Suppression, Exception and Accepted Risk.
10. Remediation Proposal/Change and closure.
11. Reproduction Recipe/Bundle/Run/Comparison.
12. Evidence Card/public View.
13. Security Graph Revision.
14. proof/reproduction/review levels.
15. coverage, negative, blocked and drift records.
16. sensitive-evidence, redaction, retention and audience policy.
17. backend replacement and historical migration.

## Validation set

- exact target and scanner revision pinning;
- no-findings with explicit skipped/unsupported/error coverage;
- changed rule/database/policy/model revisions against unchanged target bytes;
- multi-scanner disagreement retained;
- Finding split/merge/correlation review;
- false-positive/not-affected/accepted-risk with scope and expiry;
- sensitive result redaction and revocation evidence;
- authorized tests blocked outside scope;
- emergency stop, cleanup and read-back;
- agent-originated claim independently validated or rejected;
- suggested change routed through Code Ops/specialist owner and Sergeant review;
- trace-versus-pack drift detection;
- exact/semantic/tolerance reproduction comparisons;
- failed and blocked reproduction retained;
- signed/attested evidence kept separate from semantic proof;
- pass/negative/blocked/drift Evidence Card Views;
- security graph rebuilt from source Objects;
- donor replacement without Ptah identity loss.

## Next Phase 0A group

Proceed with:

1. research/documentation-source and unresolved-profile cleanup;
2. cross-requirement Phase 0A review;
3. explicit parked/rejected-gap audit;
4. Phase 0A freeze/readiness decision for Phase 0B.

No runtime implementation is approved yet.
