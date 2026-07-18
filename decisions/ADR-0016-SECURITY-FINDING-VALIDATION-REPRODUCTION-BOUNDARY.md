# ADR-0016 — Security Finding, Validation and Reproduction Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Phase:** Phase 0A security/reproduction closure

## Context

Ptah will host source scanners, SBOM/package tools, vulnerability matchers, configuration/secret/licence scanners, live web/API testing, offensive-validation agents, supply-chain graph analysis, environment replay and model-training reproduction workloads.

These systems emit different kinds of evidence and authority. Collapsing them into one `security passed`, one scanner severity or one reproduction badge would create false claims:

- a static rule match described as an exploitable vulnerability;
- a package/advisory match described as runtime reachability;
- a passive no-findings report described as full dynamic coverage;
- an agent's own PoC counted as independent validation;
- a scanner ignore/filter treated as removal of evidence;
- an exit code treated as release acceptance;
- a replayable package treated as independent reproduction;
- a valid attestation or hash treated as semantic correctness;
- a narrow passing evidence card described as broad certification.

Full composition and proof plan: `work-packages/PHASE-0A-SECURITY-REPRODUCTION-WORKLOADS.md`.

## Decision

Ptah will own separate versioned contracts for:

1. **Security Assessment Authorization**;
2. **Assessment Plan and exact Target Revision**;
3. **Scanner/Engine/Ruleset/Database/Policy/Protocol Revision**;
4. **Assessment Activity, Attempt and Coverage Record**;
5. **Raw restricted Scanner/Workload Report Artifact**;
6. **Finding Observation**;
7. **Correlated Finding and Finding Revision**;
8. **severity, confidence, exploitability, impact and release-policy decisions**;
9. **suppression, false-positive, not-affected and accepted-risk disposition**;
10. **PoC/Exploit/Reproduction Evidence**;
11. **Remediation Proposal and Verification Run**;
12. **Protocol Revision and Reproduction Run**;
13. **Result, Reproduction, Verification, Review and Acceptance levels**;
14. **Claim, allowed claim sentence and explicit boundary**;
15. **public/sanitized Evidence Card Views**.

No scanner, report, CVE match, alert, agent, evidence-card or reproduction-workload ID becomes canonical Ptah identity.

---

# Requirement decisions

## `SEC-001`

Ptah supports authorized security assessments with exact scope, target revision, scanner machinery, coverage, Findings, dispositions, remediation and independent re-test/review.

## `REPRO-001`

Ptah supports frozen Protocol Revisions, exact source/target/environment boundaries, replay/re-execution evidence, negative/blocked/drift outcomes and narrow claim presentation without equating them to certification.

Both are closed for Phase 0B contract design, not implementation.

---

# Authorization and target boundary

Active, fuzz, exploit and agentic security operations require a durable Security Assessment Authorization defining:

- owner/approver and legal/customer authority;
- exact target and environment revision;
- included/excluded hosts, routes, accounts, files and data;
- permitted test classes and forbidden/destructive actions;
- network, credential, rate, concurrency, time and resource limits;
- required isolation class;
- emergency stop and cleanup/read-back plan;
- retention/redaction policy and expiry.

The scanner/workload cannot authorize or expand its own scope. A valid URL, repository or image does not prove permission to test it.

Mutable tags, branches, deployment names and URLs are resolution inputs only. Every Assessment records the exact resolved source/Object/image/service/dataset/model/environment revision.

---

# Coverage and report boundary

Every Assessment Attempt retains:

- expected and resolved scope;
- scanned files/packages/routes/roles/states;
- skipped, disabled, unsupported and ignored scope;
- parse, authentication, connection, tool and timeout errors;
- crawl/reachability and resource limits;
- exact scanner/workload configuration;
- raw native report/log/traffic/proof bundle as an immutable restricted Artifact.

A zero-findings result without coverage/error/skip context is not a complete security claim.

Normalization never replaces the native report.

---

# Finding boundary

## Finding Observation

A Finding Observation is one detector/workload assertion tied to exact target location, scanner/rule/machinery revision and raw evidence.

Observation classes remain distinct, including:

```text
source_pattern_or_dataflow
package_or_advisory_match
misconfiguration
secret
licence
passive_web
active_or_exploit
agent_originated_claim
supply_chain_graph_result
reproduction_or_validation_result
```

## Correlated Finding

A Ptah Finding correlates one or more observations that may describe the same underlying issue. Correlation is a reviewable proposal with confidence/reasoning. It never deletes, merges away or rewrites the original observations or scanner disagreement.

## Evaluation dimensions

Ptah keeps separate:

- scanner severity;
- scanner confidence;
- exploitability/reachability;
- business/operational impact;
- affected/not-affected state;
- remediation priority;
- release policy;
- caller acceptance.

Each decision names its authority, evidence, scope and time.

## Dispositions

False positive, not affected, duplicate/correlated, accepted risk, suppressed and closed states are durable dispositions over immutable observations. They require issuer, reason, scope and optional expiry. Expiry returns the Finding to review; it does not erase history.

---

# Donor roles

## Semgrep

- primary source/static-analysis Facility;
- exact rule/source ranges, engine tier, dataflow and skipped/error evidence retained;
- Community/open analysis is not presented as equivalent to proprietary cross-file coverage;
- autofix remains a remediation proposal.

## Syft, Grype and Trivy

- Syft supplies SBOM/package/file/relationship observations;
- Grype supplies package/advisory matching;
- Trivy supplies broad vulnerability, configuration, secret and licence scanning;
- inventory, advisory DB, policy bundle, scanner class, modification/ignore state and release decision remain separate;
- secret values are redacted and separately revoked/remediated.

## GUAC

- optional supply-chain graph/enrichment/query Facility;
- graph facts are derived claims over source documents;
- GUAC does not replace Ptah Object, Package, Finding or provenance identity.

## ZAP

- primary authorized dynamic web/API scanning Facility;
- passive, active, manual and tool alerts remain distinct;
- HTTP traffic is restricted evidence;
- active work requires exact scope, rate, credentials, isolation, stop and cleanup.

## Strix

- optional agentic offensive-validation workload, never Core or security authority;
- the inspected default backend is Docker and does not itself provide sufficient target/network/credential isolation;
- agent claim, its own PoC, CVSS and remediation are not independent corroboration;
- generated fixes go through Code Ops and independent Sergeant/security review.

## ReproZip

- one environment-capture/replay donor;
- capture/replay does not prove complete external/kernel/hardware state, portability or independent reproduction.

## ClaimBound

- narrow Evidence Card/presentation donor;
- allowed claim sentence, frozen protocol, result, reproduction and verification remain separate;
- cards are Views over Ptah Claims, Activities and Artifacts, not certification or Activity truth.

## SparkDistill

- optional AI training/reproduction workload;
- recipe, dataset, checkpoint, metric claim, attestation, re-score and retrain remain separate;
- held-out re-score, partial retrain, full retrain and independent reproduction are distinct levels;
- model activation requires separate owner/department review.

---

# Offensive testing and isolation

Active/fuzz/exploit/agentic workloads:

- run only in an approved isolation Provider;
- receive exact target network grants, credentials, mounts and budgets;
- do not receive ambient host credentials or Docker-host authority;
- cannot reach excluded networks or metadata services;
- retain every request/command/payload and observed side effect;
- support emergency stop and independent cleanup/read-back;
- treat external LLM/model/provider data transfer as an explicit privacy decision.

A workload cannot declare its own exploit safe, target cleaned or authorization satisfied without external evidence/authority.

---

# Reproduction boundary

A neutral reproduction family represents at least:

```text
claim_only
artifact_manifest_verified
source_and_protocol_available
environment_captured
replayed_same_profile
replayed_compatible_profile
partial_reexecution_or_rescore
full_reexecution_or_retrain
independent_reproduction
independent_cross_implementation
```

These levels state exactly what was reused, rebuilt, rerun and independently operated. They are not one automatic quality score.

A Protocol Revision freezes:

- claim/question and allowed claim sentence;
- explicit boundary;
- source, target, period and inputs;
- commands, environment, dependencies and hardware;
- rules, harnesses, datasets, benchmarks and tolerances;
- seeds/stochastic policy;
- failure, blocked and drift rules;
- required Artifacts and operator independence.

Changing the protocol creates a new revision and never rewrites prior evidence.

Result Status, Reproduction Level, Verification Level, Review and Acceptance remain separate. Pass, fail, blocked source, drift, timeout, inconclusive and not-independently-reproduced outcomes all remain visible.

---

# Remediation and closure

Scanner/agent/human remediation is a proposal until implemented by the correct owner.

- Code Ops owns source patches;
- specialist departments own relevant configuration/data/business changes;
- security/quality owners authorize testing and adjudicate risk;
- Sergeant or another approved independent reviewer verifies engineering claims;
- caller/owner accepts release or residual risk.

Closure requires a new Verification Run under exact target and machinery revisions. The original report remains intact. A Finding may later become `regressed` through a new immutable observation.

Removal from one scanner after a rule/database change is not by itself remediation proof.

---

# Evidence privacy and public claims

Ptah separates:

```text
raw_restricted_evidence
redacted_internal_summary
reviewer_package
public_sanitized_evidence_card
```

Public cards include exact protocol, allowed claim sentence, boundary, result/reproduction/verification levels, limitations and hashes/references without exposing source, credentials, customer data, exploit details or private topology.

Hashes prove byte identity, not correctness, permission, safety or semantic truth.

---

# Consequences

## Positive

- scanners can disagree without evidence loss;
- no-findings and pass badges gain honest coverage boundaries;
- static, inventory, dynamic and offensive results remain distinguishable;
- active tests gain legal/technical authorization, containment and cleanup;
- remediation and release decisions retain the correct owners;
- reproduction claims become bounded and independently interpretable;
- negative, blocked and drift results remain first-class;
- public evidence can be useful without leaking restricted material;
- scanner/workload replacement preserves Ptah identities.

## Costs

- Finding correlation, dispositions and review schemas are substantial;
- scanner/rule/DB/policy freshness must be maintained;
- raw security evidence requires strict storage, redaction and access controls;
- offensive workloads require stronger isolation and operational safeguards;
- independent reproduction can be expensive and hardware/provider sensitive;
- public card generation requires careful claim wording and sanitization.

## Do-not-break rules

> Never collapse scanner Observation, correlated Finding, severity, exploitability, impact, disposition, remediation, verification, review and release acceptance into one status.

> Never describe no findings, exit code zero, a clean scan, a PoC, a hash, attestation, replay or narrow passing card as broad proof of security or correctness.

> Never permit a scanner/agent to authorize its own target, expand scope, waive isolation, accept its own fix or erase negative/contradictory evidence.

> Never publish raw source, credentials, traffic, exploits, customer data or sensitive model/dataset evidence merely to make a public proof card look complete.

---

# Required proof before freeze

1. Run static, inventory, vulnerability, secret, passive and active assessments against exact frozen targets.
2. Preserve scanner engines, rules, DBs, policies, coverage, skips and errors.
3. Correlate multiple observations without deleting disagreement.
4. apply false-positive/not-affected/accepted-risk dispositions with authority and expiry.
5. run ZAP/Strix only under exact Authorization, isolation and network/credential budgets.
6. stop/clean an unsafe active test and prove read-back.
7. route generated remediation through Code Ops and independent review.
8. capture/replay with ReproZip and retain missing-state limitations.
9. produce ClaimBound-style pass/fail/blocked/drift/non-independent cards.
10. perform manifest, re-score, partial/full re-execution and independent reproduction as separate levels.
11. retain failed/inconclusive/regressed results without historical rewrite.
12. replace scanners and Evidence Card renderers without changing Ptah identities.
