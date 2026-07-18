# ADR-0016 — Security Finding, Claim, Evidence, Authorization and Reproduction Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Phase:** Phase 0A security and reproduction completion

## Context

Ptah must retain security and reproducibility evidence without allowing one scanner, agent, report, signature, evidence card, graph or replay bundle to become authority by itself.

The recovered composition includes Syft, Grype, Trivy, Semgrep, OWASP ZAP, Strix, ReproZip, GUAC, ClaimBound Evidence and SparkDistill, joined to the existing Ptah Object, Artifact, Activity, Receipt, Build, provenance, isolation and independent-review boundaries.

No donor defines Ptah's canonical Target, Scanner Revision, Security Test Authorization, Finding Observation, stable Finding, Claim, Evidence, Risk Assessment, Adjudication, Exception, Remediation, Reproduction Recipe, Run, Comparison or Closure identity.

## Decision

Ptah owns separate backend-neutral records for:

1. Security Test Authorization;
2. Scan Target and exact Target Revision;
3. Scanner, engine, ruleset, database, policy, add-on and model revision;
4. Scan Activity and attempt;
5. raw Scanner Report Artifact;
6. Finding Observation;
7. stable correlated Finding;
8. bounded Claim and allowed claim sentence;
9. Evidence and Evidence Relationships;
10. Risk Assessment;
11. Adjudication;
12. Suppression, Exception and Accepted Risk;
13. Remediation Proposal and Change;
14. verification, re-scan and closure;
15. Reproduction Recipe and Bundle;
16. Reproduction Run and Comparison;
17. Evidence Card/public-safe View;
18. derived Security Graph Revision;
19. independent review and release/acceptance decision.

Tool-local rule, alert, report, task, package, graph, proof and card identifiers remain adapter metadata.

## Required separation

The following never collapse into one status:

```text
Activity state
Finding Observation
stable Finding
Claim
Evidence
scanner severity/confidence
risk and business impact
Adjudication
reproduction level
independent review
release or caller acceptance
```

A completed scan proves only the recorded tool execution state. A signature proves identity/integrity under a trust chain. A replay bundle proves only that the bundle was assembled. None of these alone proves security, correctness or reproduction.

## Finding and coverage rules

Finding classes remain distinct, including inventory, advisory matches, source analysis, configuration, secrets, licences, dynamic testing, runtime behavior, supply chain, privacy and agent/manual claims.

Every scan records requested, resolved, successful, skipped, unsupported and failed scope, along with disabled classes and exact rule/database/policy revisions.

`No findings` means only that no observations were produced within the successful recorded scope and limitations. It never means universally safe, clean or secure.

Every detector output remains a Finding Observation. Correlation into a stable Finding is a reviewable Claim. Independent agreement, disagreement, split and merge history remain visible.

## Risk and adjudication

Ptah retains separately:

- scanner severity;
- standard score/vector;
- confidence;
- reachability;
- exploitability;
- known exploitation;
- probability;
- business impact;
- asset criticality and exposure;
- remediation cost;
- uncertainty.

Adjudication records a named reviewer, rationale, evidence, exact scope and expiry. False-positive, not-affected, accepted-risk and other exceptions never delete the underlying observation.

## Authorization

State-changing, credentialed, load-producing or autonomous security testing requires an externally approved Security Test Authorization.

Authorization fixes target ownership, legal/policy basis, exact environment, included/excluded scope, permitted/prohibited test classes, credentials, rate/time/change budgets, isolation, network boundaries, emergency stop, backup, cleanup, read-back, contacts and expiry.

A URL, repository or reachable service is never authorization. Tools and agents cannot authorize or expand their own scope.

## Donor roles

- **Syft:** primary package/SBOM inventory Facility.
- **Grype:** primary package/advisory matcher with exact database freshness.
- **Trivy:** primary broad Artifact/configuration scanner; finding classes and modified states remain separate.
- **Semgrep:** primary source-level static analysis; source spans, rules, engine tier, dataflow, errors and skipped scope retained.
- **OWASP ZAP:** primary authorized dynamic web/API scanner; raw alerts, review and gates remain separate.
- **Strix:** optional agentic validation workload; its findings, scores and changes remain claims requiring independent validation.
- **ReproZip:** optional observed dependency capture/replay Facility; trace, recipe, bundle and replay remain separate.
- **GUAC:** optional derived security/provenance graph; source documents remain authoritative and the graph is rebuildable.
- **ClaimBound Evidence:** narrow evidence-card donor; result, reproduction, verification and review remain separate.
- **SparkDistill:** optional AI-training reproduction workload; recipe, data, checkpoint, claim, attestation and recheck remain separate.

## Remediation ownership

Security tools may propose changes but do not own them.

- Code Ops owns code patches.
- The correct specialist department owns other changes.
- Sergeant owns independent engineering review and proof where applicable.
- Organizational policy owns risk acceptance and release approval.
- Ptah records authority, execution and evidence but is not the organizational approver.

Verified closure requires an approved change, relevant build/deployment evidence, a targeted verification run, negative read-back for the original issue, regression checks and authorized reviewer acceptance.

## Reproduction model

A Reproduction Recipe freezes sources, inputs, commands or Activity graph, environment, Node capabilities, external services, credentials/fixtures, clock/randomness/locale, expected outputs/tolerances, cleanup and known uncaptured state.

A Reproduction Bundle is an immutable signed Artifact. A Reproduction Run is a new Activity/attempt. Comparison records exact hashes, semantic/tolerance results, logs, external read-back, variance and limitations.

Reproduction levels remain distinct:

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

## Public/private boundary

Security evidence is restricted by default. Public-safe Evidence Cards are permission-filtered Views exposing only an approved narrow claim, boundary, protocol/tool revisions, hashes, result/reproduction/review levels, limitations and non-sensitive closure summary.

The visual result must remain attached to the claim boundary and limitations.

## Security graph

GUAC or a native graph may index package, Artifact, SBOM, attestation, advisory, Finding, remediation, scanner and reproduction relationships.

The graph is a versioned derived Index. Source documents remain retained and authoritative. Uncertain/conflicting joins remain visible. The graph can be rebuilt or replaced.

## Rejected alternatives

- one universal security score;
- scanner output as release authority;
- deleting observations during deduplication;
- no findings treated as secure;
- self-authorized active or agentic testing;
- signed report treated as correct;
- replay bundle treated as reproduced;
- generated change merged automatically;
- derived security graph treated as source truth.

## Phase 0B requirements

Phase 0B must define schemas and conformance for:

1. Security Test Authorization;
2. Scan Target and Scanner Revision;
3. raw Scanner Report Artifact;
4. Finding Observation and stable Finding;
5. Claim and Evidence;
6. Risk Assessment and Adjudication;
7. Exceptions and Accepted Risk;
8. Remediation and verified closure;
9. Reproduction Recipe, Bundle, Run and Comparison;
10. Evidence Card View;
11. Security Graph Revision;
12. coverage, negative, blocked and drift records;
13. sensitive-evidence and audience policy;
14. scanner/backend replacement and migration.

No implementation is authorized by this ADR.

## Related evidence

- `work-packages/PHASE-0A-WP12-SECURITY-REPRODUCTION-WORKLOADS.md`
- `donors/REPROZIP.md`
- `donors/GUAC.md`
- `donors/SYFT.md`
- `donors/GRYPE.md`
- `donors/SEMGREP.md`
- `donors/TRIVY.md`
- `donors/ZAPROXY.md`
- `donors/STRIX.md`
- `donors/CLAIMBOUND.md`
- `donors/SPARKDISTILL.md`
