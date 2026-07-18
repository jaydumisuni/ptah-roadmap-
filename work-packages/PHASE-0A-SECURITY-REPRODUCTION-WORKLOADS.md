# Phase 0A — Security Assessment, Findings and Reproduction Workloads

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Runtime code:** NOT STARTED

## Purpose

Close the final operational evidence gap between:

- source/static analysis;
- package, SBOM and vulnerability inventory;
- configuration, secret and licence scans;
- live web/API passive and active assessment;
- agentic offensive validation;
- supply-chain knowledge graphs;
- environment capture and replay;
- frozen protocols and narrow public evidence claims;
- AI model/dataset/training reproduction workloads;
- remediation, independent review and re-test.

This work package does not create one universal scanner or one universal `security passed` state. It defines Ptah-owned identities and proof boundaries so several detectors, scanners, human reviewers and reproduction systems can disagree without rewriting one another's evidence.

## Evidence recovered

### Existing Ptah foundations

- `decisions/ADR-0003-ACTIVITY-EVENT-OBSERVABILITY-BOUNDARY.md`
- `decisions/ADR-0004-OPERATION-RECEIPTS-PROOF-LEVELS.md`
- `decisions/ADR-0005-BUILD-ARTIFACT-PROVENANCE-BOUNDARY.md`
- `decisions/ADR-0007-OBJECT-GRAPH-DECOMPOSITION-DERIVATIVE-BOUNDARY.md`
- `decisions/ADR-0011-BROWSER-PROFILE-CONTEXT-PAGE-EVIDENCE-BOUNDARY.md`
- `decisions/ADR-0013-KNOWLEDGE-DATA-SEARCH-PLUGIN-BOUNDARY.md`
- `decisions/ADR-0014-ISOLATION-RUNTIME-PLACEMENT-SCHEDULING-BOUNDARY.md`
- internal Code Ops, Sergeant, Builder, MIBU and evidence-contract records

These already establish:

- source Objects and Artifacts are immutable/versioned;
- scanner output, Receipt, review and acceptance are separate authority levels;
- plural detector claims and disagreements are retained;
- Builds, SBOMs, attestations and signatures remain distinct;
- Browser traffic, source records and screenshots are evidence, not automatic claims;
- untrusted code/workloads use explicit isolation and permissions;
- fixes and release acceptance remain owned by caller departments and independent review.

### Reproduction and evidence donors

- `donors/REPROZIP.md`
- `donors/CLAIMBOUND.md`
- `donors/SPARKDISTILL.md`

### Supply-chain inventory and graph donors

- `donors/SYFT.md`
- `donors/GRYPE.md`
- `donors/GUAC.md`
- `donors/TRIVY.md`

### Source and dynamic-security donors

- `donors/SEMGREP.md`
- `donors/ZAPROXY.md`
- `donors/STRIX.md`

## Composite result

```text
Exact Ptah Target Revision
  source repository/Object
  Build Artifact/image/filesystem/SBOM
  deployed Service/API/Application
  dataset/model/checkpoint
  Workspace/environment snapshot

Assessment Authorization and Plan
  purpose and owner
  allowed target/scope
  scanner/test classes
  credentials/network/time/rate/destructive limits
  isolation and cleanup policy

Versioned Assessment Machinery
  Scanner/Workload Package Release
  engine/provider/model version
  rules/ruleset
  vulnerability/advisory database
  policy/check bundle
  protocol/harness/benchmark
  environment/runtime profile

Assessment Activity and Attempts
  exact target resolution
  coverage and skipped/failed scope
  raw restricted reports/traffic/logs
  resource/network/side-effect Receipts

Plural Finding Observations
  static match
  package/advisory match
  misconfiguration
  secret/licence observation
  passive web alert
  active/exploit observation
  agent-originated claim
  reproduction outcome

Finding Correlation and Adjudication
  independent observations preserved
  duplicate/correlation proposal
  severity/confidence/exploitability/impact separate
  false-positive/not-affected/accepted-risk/suppression separate
  reviewer and expiry

Remediation and Verification
  proposal/patch/config/data change
  Code Ops/department ownership
  tests/Build/re-scan/reproduction
  Sergeant/security review
  accepted or unresolved state

Evidence Card / Public View
  narrow allowed claim sentence
  protocol and boundary
  result, reproduction and verification levels
  limitations and negative/blocked/drift outcomes
  sanitized hashes to restricted raw evidence
```

No donor-specific report ID, alert ID, fingerprint, CVE match, package URL, evidence-card ID or agent report becomes canonical Ptah identity.

---

# 1. Native requirements

## `SEC-001` — Authorized security assessment and Finding lifecycle

Ptah must support:

- exact Target and target revision;
- Security Assessment Authorization;
- Assessment Plan and test class;
- versioned Scanner/Rule/DB/Policy machinery;
- Scan/Assessment Activity attempts;
- coverage, skip, error and incomplete states;
- raw restricted evidence;
- plural Finding Observations;
- Finding correlation/adjudication;
- severity, confidence, exploitability and impact separation;
- suppression, accepted risk and expiry;
- remediation proposal and ownership;
- independent re-test/review and closure;
- active-test emergency stop, cleanup and read-back.

## `REPRO-001` — Frozen protocol, rerun and bounded evidence claim

Ptah must support:

- Protocol and immutable Protocol Revision;
- source/target/input/output/environment boundaries;
- exact commands, dependencies, seeds and hardware/runtime profiles;
- capture/package/replay/retrain/re-score Activities;
- raw evidence and manifests;
- Result Status separate from Reproduction/Verification/Review level;
- negative, blocked, drifted, partial and non-reproduced outcomes;
- independent operator/reviewer records;
- allowed claim sentence and explicit claim boundary;
- public/sanitized Evidence Card Views;
- supersession without historical rewrite.

---

# 2. Security Assessment Authorization

Passive, static and active security work do not share one authority level.

A versioned authorization records:

```text
security_authorization_id
owner_and_approver
workspace_or_department
purpose
legal_or_customer_authority_reference
target_id_and_exact_revision
environment_class
allowed_hosts_services_paths_methods_accounts
excluded_hosts_services_paths_data
allowed_test_classes
forbidden_or_destructive_actions
credential_and_test_data_references
network_and_egress_scope
rate_concurrency_and_time_window
resource_budget
required_isolation_class
logging_redaction_and_retention_policy
emergency_stop_contact_and_condition
cleanup_and_read_back_plan
valid_from_and_expires_at
state
```

Test classes include at least:

```text
source_static
artifact_inventory
vulnerability_match
configuration_policy
secret_detection
licence_observation
passive_dynamic
active_dynamic
fuzz
exploit_validation
offensive_agentic
supply_chain_graph_analysis
reproduction_or_replay
```

A valid URL, repository, image or customer request is not sufficient authorization by itself.

## 2.1 Authorization rules

- static scans may run under source-read permissions;
- secret scanning requires stronger output/privacy controls;
- passive proxying requires traffic/TLS/session authorization;
- active/fuzz/exploit/agentic testing requires explicit target and destructive-action authorization;
- production/customer targets default to denied for active testing unless an exact approval exists;
- the scanner/workload cannot authorize or expand its own scope;
- newly discovered domains, services or credentials remain out of scope until approved;
- expired authorization blocks new operations while preserving existing evidence.

---

# 3. Assessment Plan and machinery identity

Every assessment runs under an immutable plan:

```text
assessment_plan_id
security_authorization_id
assessment_class
target_resolution_recipe
scanner_or_workload_package_release
engine_and_provider_revision
ruleset_or_policy_revision
advisory_database_revision_and_freshness
protocol_or_harness_revision
configuration_and_enabled_features
isolation_provider_profile
network_and_credential_grants
coverage_expectation
failure_and_stop_policy
output_artifact_schema
```

## 3.1 Scanner machinery

Ptah records separately:

- scanner name/version/build digest;
- community versus proprietary engine/tier;
- rules/ruleset source, hash, licence and trust;
- advisory/vulnerability DB source, version, update/download time and freshness;
- check/policy bundle digest;
- add-on/plugin versions;
- model/provider/prompt/tool versions for agentic workloads;
- container/VM/toolchain image and SBOM;
- exact configuration, disabled checks and thresholds.

A report on unchanged target bytes may legitimately change when rules, databases, policies, model/provider or scanner revisions change. Historical reports are not overwritten.

---

# 4. Target and coverage model

## 4.1 Exact Target Revision

A target can be:

- repository commit and path scope;
- immutable Object/View revision;
- Build Artifact/image digest and platform;
- filesystem snapshot;
- SBOM Artifact;
- deployed Service/API/Application revision;
- browser/site environment plus authentication state;
- dataset/model/checkpoint revision;
- Workspace/checkpoint/environment profile.

Mutable tags, branches, URLs and deployment names are resolution inputs only. The Assessment Activity records the exact resolved revision.

## 4.2 Coverage Record

```text
coverage_record_id
assessment_attempt_id
expected_scope
resolved_scope
scanned_objects_files_routes_roles_states_packages
skipped_disabled_unsupported_or_ignored_scope
parse_auth_connection_or_tool_errors
timeouts_and_resource_limits
crawl_or_reachability_state
partial_or_complete_claim
coverage_limitations
```

A zero-findings report without coverage/error/skip context is incomplete evidence.

---

# 5. Report and Finding model

## 5.1 Raw report

Every scanner/workload retains its native raw report/log/traffic/proof bundle as an immutable restricted Artifact. Normalization does not replace it.

## 5.2 Finding Observation

A Finding Observation is one detector/workload assertion:

```text
finding_observation_id
assessment_attempt_id
scanner_workload_and_rule_identity
observation_class
target_revision_and_location
source_range_or_http_exchange_or_package_path
raw_title_description_message
scanner_severity_and_confidence
scanner_fingerprint_or_alert_id
cwe_cve_wasc_or_external_references
matched_evidence_and_dataflow
attack_payload_or_poc_reference
coverage_and_assumptions
observed_at
raw_report_reference
```

Observation classes remain distinct:

- source pattern/dataflow;
- package/advisory match;
- configuration/misconfiguration;
- secret;
- licence;
- passive HTTP/web;
- active/fuzz/exploit;
- agent-originated claim;
- supply-chain graph query result;
- reproduction/validation result.

## 5.3 Finding

A Ptah Finding correlates one or more observations that may describe the same underlying issue:

```text
finding_id
finding_revision
canonical_target_and_location
finding_class
observation_relationships
correlation_basis_and_confidence
current_triage_state
impact_and_exploitability_assessment
owner
first_seen_last_seen
```

Correlation is a reviewable proposal. It never deletes source observations or scanner disagreement.

## 5.4 Separate evaluation dimensions

Ptah does not collapse:

- scanner severity;
- scanner confidence;
- exploitability/reachability;
- business/operational impact;
- affected/not-affected state;
- remediation priority;
- release policy;
- caller acceptance.

Each comes from a named authority with time, scope and evidence.

## 5.5 Triage states

At minimum:

```text
untriaged
needs_more_evidence
confirmed
likely
false_positive
not_affected
duplicate_correlated
accepted_risk
suppressed
remediation_planned
remediating
verification_pending
closed_verified
closed_unverified
regressed
expired_or_stale
```

The original observation remains immutable when triage changes.

## 5.6 Suppression and risk acceptance

```text
finding_disposition_id
finding_id
issuer_and_authority
state
reason
scope
evidence
created_at
expires_at
review_or_renewal_required
```

Ignored/false-positive/not-affected/accepted-risk observations are visible and reversible. Expired dispositions automatically return to review rather than silently remaining suppressed.

---

# 6. Donor composition

## 6.1 Semgrep

Primary source/static analysis Facility:

- syntax-aware rules and exact source ranges;
- rule metadata and dataflow traces;
- findings, errors, skipped targets/rules and engine tier retained;
- Community/open engine limits remain explicit;
- autofix remains a proposal for Code Ops and independent review.

## 6.2 Syft and Grype

Supply-chain inventory and vulnerability-matching composition:

- Syft produces package/file/relationship SBOM observations;
- Grype matches inventory against versioned vulnerability sources;
- inventory, vulnerability match, exploitability and release decision remain separate;
- one shared package lineage can support multiple scanner observations.

## 6.3 Trivy

Primary broad Artifact/configuration scanner:

- vulnerability, misconfiguration, secret and licence classes remain separate;
- enabled scanners and DB/check-bundle freshness are mandatory evidence;
- original versus modified/ignored results remain visible;
- secrets are redacted and separately remediated/revoked.

## 6.4 GUAC

Supply-chain graph and enrichment Facility:

- ingests SBOM, provenance, vulnerability and package relationships;
- graph/enrichment/query results are derived claims over source documents;
- GUAC is not the canonical Object, Package or Finding graph;
- ingestion source, parser and collector revisions remain traceable.

## 6.5 ZAP

Primary authorized dynamic web/API Facility:

- passive, active, manual, tool and unknown alert sources remain distinct;
- HTTP requests/responses, attack, evidence, risk and confidence retained;
- authentication/crawl/route/role coverage explicit;
- active scans require exact scope, rate, credentials, emergency stop and cleanup;
- raw traffic/report evidence is restricted/redacted.

## 6.6 Strix

Optional agentic offensive-validation workload:

- runs only under explicit Security Test Authorization;
- Docker is its default registered backend at the inspected pin and is not sufficient isolation by itself;
- Ptah chooses gVisor/Kata/Firecracker/full VM based on tools/target risk;
- `NET_ADMIN`, `NET_RAW`, bind mounts, external LLMs and network destinations are tightly scoped;
- agent claim, its own PoC, CVSS and remediation are not independent evidence;
- PoCs require independent replay/review;
- generated patches go through Code Ops and Sergeant/security review.

## 6.7 ReproZip

Environment capture/replay donor:

- traces runtime dependencies and packages execution environments;
- useful for one reproduction level and debugging missing dependencies;
- ptrace/Linux coverage and packaging cannot prove all network, kernel, hardware or hidden external state;
- a replayable package is not automatically equivalent, safe or independently reproduced.

## 6.8 ClaimBound

Evidence Card/presentation donor:

- narrow allowed claim sentence and explicit claim boundary;
- frozen protocol and source boundary;
- Result Status, Reproduction Level, Verification Level and Review remain separate;
- negative, blocked and drift outcomes remain visible;
- cards are Views over Ptah Claims/Activities/Artifacts, not Activity truth or certification.

## 6.9 SparkDistill

Optional AI training/reproduction workload:

- recipe/dataset remain source inputs distinct from checkpoint and metric claims;
- self-reported metrics are Claims;
- manifest-only, re-score, partial retrain, full retrain and independent reproduction remain different levels;
- GPU/confidential-computing attestation binds environment/claim but does not prove semantic correctness;
- exact dataset/model/provider rights and revisions are mandatory;
- no trained model activates in Hunter or another caller without separate owner/department review.

---

# 7. Offensive and active testing boundary

Active/fuzz/exploit/agentic operations can modify targets and create legal/operational risk.

## 7.1 Runtime and network

- run in an approved isolated Provider;
- no host Docker socket or ambient host credentials;
- network egress limited to authorized targets and required approved providers;
- excluded networks and metadata services denied;
- target, method, rate, concurrency and duration budgets enforced outside the workload;
- external LLM/provider traffic follows approved privacy/data policy;
- source/target mounts default read-only where possible.

## 7.2 Operation receipts

Every active action records:

- operation and attempt;
- target resolution and authorization;
- exact request/command/payload;
- network/source/credential grant;
- response/effect evidence;
- observed side effects;
- cleanup/compensation state;
- emergency-stop reason where applicable.

A scanner/agent cannot report its own side effect as safely cleaned without independent read-back.

## 7.3 Stop and cleanup

The plan defines:

- automatic stop conditions;
- human emergency stop;
- credential revocation;
- created-account/data/resource inventory;
- rollback/cleanup recipe;
- post-test health/read-back;
- unresolved or irreversible side effects.

---

# 8. Reproduction and validation levels

A neutral level family must represent at least:

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

These are not an automatic linear quality score. Each record states:

- what was rerun;
- what was reused;
- what was independently rebuilt;
- environment/hardware/provider differences;
- tolerance and stochastic policy;
- drift and limitations;
- operator/reviewer independence.

## 8.1 Protocol Revision

```text
protocol_revision_id
claim_or_question
allowed_claim_sentence
explicit_claim_boundary
source_and_target_scope
inputs_and_expected_outputs
commands_steps_and_environment
rules_harness_benchmarks_and_tolerances
random_seeds_and_stochastic_policy
failure_blocked_and_drift_rules
required_artifacts_and_hashes
required_operator_independence
```

A changed protocol produces a new revision and cannot silently update prior evidence.

## 8.2 Reproduction Run

```text
reproduction_run_id
protocol_revision_id
source_target_and_input_revisions
operator_and_environment
activity_attempts
captured_or_reused_artifacts
result_status
reproduction_level
verification_level
raw_evidence
limitations_and_drift
```

## 8.3 Result status versus reproduction

A protocol may pass but remain single-operator/not independently reproduced. A reproduction may detect source-byte drift without changing the historical gate result. These states stay separate.

## 8.4 Negative and blocked evidence

Ptah retains:

- failed gate;
- negative result;
- source unavailable/blocked;
- environment incompatible;
- timed out/resource exhausted;
- irreproducible;
- drift detected;
- partial reproduction;
- inconclusive;
- not independently verified.

These do not disappear from dashboards or public cards.

---

# 9. Remediation, verification and closure

## 9.1 Remediation proposal

A scanner/agent/human may propose:

- source patch;
- dependency upgrade;
- configuration/policy change;
- credential revocation/rotation;
- data/model/dataset correction;
- environment/runtime change;
- risk acceptance/suppression.

A proposal is not applied or accepted automatically.

## 9.2 Ownership

- Code Ops owns code patch implementation;
- the relevant department owns specialist configuration/data/business changes;
- Security/quality owners authorize security testing and triage impact;
- Sergeant or another approved independent reviewer verifies engineering claims;
- the caller/owner accepts release or residual risk.

Ptah records these authorities but does not replace them.

## 9.3 Verification run

Closure requires a new Activity/report under exact target and machinery revisions. The original report remains intact.

A Finding closes as verified only when the defined closure protocol passes and required review/acceptance exists. Removal from one scanner after a rule/DB change is not by itself remediation proof.

## 9.4 Regression

A previously closed Finding can reappear as a new Observation and transition to `regressed` while retaining prior closure history.

---

# 10. Evidence privacy and public views

Security evidence can contain:

- proprietary source;
- credentials, cookies and tokens;
- exploit payloads;
- personal/customer data;
- internal hosts/topology;
- vulnerable endpoints;
- model/dataset/provider-restricted content.

Ptah separates:

```text
raw_restricted_evidence
redacted_internal_summary
reviewer_package
public_sanitized_evidence_card
```

Public views include hashes/references, boundary, limitations and allowed claim sentence without leaking raw restricted evidence. A hash does not prove correctness or give public access to the underlying Artifact.

---

# 11. Scanner disagreement and correlation

Different scanners may disagree because of:

- inventory differences;
- rules and databases;
- language/framework coverage;
- runtime reachability;
- source versus deployed state;
- authentication/crawl state;
- advisory/vendor severity;
- policy thresholds;
- model/agent stochasticity.

Ptah retains every Observation and records correlations such as:

```text
supports
contradicts
possible_duplicate
same_location_different_rule
same_package_different_advisory
source_and_runtime_related
not_comparable
supersedes_observation
```

Correlation does not erase independent provenance or shared assumptions.

---

# 12. Requirement closure verdict

## `SEC-001` — CLOSED FOR PHASE 0B CONTRACT DESIGN

Closed direction:

- security testing requires exact Target, Authorization, Plan and machinery revision;
- static, inventory, vulnerability, secret, passive, active and agentic findings remain distinct;
- coverage/errors/skips are mandatory;
- scanner Observation and correlated Finding are separate;
- severity, confidence, exploitability, impact, disposition and release policy are separate;
- active/offensive work uses strong isolation, exact network/credential grants, stop and cleanup;
- fixes remain proposals until implementation, re-test and independent review;
- no findings does not mean secure.

## `REPRO-001` — CLOSED FOR PHASE 0B CONTRACT DESIGN

Closed direction:

- frozen Protocol Revision, source/target/environment boundaries and exact commands;
- result, reproduction, verification, review and acceptance remain separate;
- negative/blocked/drift/inconclusive outcomes retained;
- ReproZip is one environment-capture/replay donor, not universal reproduction;
- ClaimBound cards are bounded Views, not certification;
- SparkDistill is an optional specialist workload demonstrating recipe/data/checkpoint/claim/recheck separation;
- independent reproduction and cross-implementation evidence remain higher distinct levels.

## Existing requirements extended

- `PROV-001` raw evidence, SBOM, attestation and verification graph;
- `EXEC-003` reproducible Builds;
- `PLUGIN-001` package scanning and activation gates;
- `ISOLATION-001` scanner/offensive workload runtime class;
- `BROWSE-001–003` dynamic web target/evidence;
- `DATA-001/SEARCH-001` datasets, reports and evidence discovery;
- `UI-002` Finding/Evidence/review projections;
- `OBS-001` assessment events/resource/coverage accounting.

No scanner, offensive workload, security gate or reproduction runtime implementation is authorized by this closure.

---

# 13. Phase 0B contracts required

1. Security Assessment Authorization schema.
2. Assessment Plan and test-class schema.
3. exact Target Resolution and Coverage schema.
4. Scanner/Engine/Ruleset/Database/Policy Revision schema.
5. raw Scanner/Workload Report Artifact schema.
6. Finding Observation and Correlated Finding schema.
7. severity/confidence/exploitability/impact/disposition schema.
8. suppression/accepted-risk/expiry and authority schema.
9. HTTP exchange/PoC/exploit operation evidence schema.
10. emergency stop, cleanup and post-test read-back schema.
11. Protocol and Protocol Revision schema.
12. Reproduction Run and level/state schema.
13. Claim, allowed sentence, boundary and Evidence Card View schema.
14. remediation proposal, verification run, review and closure schema.
15. sensitive evidence/redaction/audience/retention schema.
16. multi-scanner correlation and replacement conformance corpus.

---

# 14. Required proof before freeze

1. Scan one exact source revision with Semgrep and retain rules, engine tier, coverage, skips and errors.
2. generate/ingest an SBOM through Syft and compare Grype/Trivy package findings while retaining inventory disagreement.
3. update vulnerability DB/policy rules with unchanged target bytes and retain new report revisions.
4. detect a secret, redact it and separately prove revocation/remediation.
5. mark one observation false positive/not affected/accepted risk with authority and expiry without deleting it.
6. correlate two scanners to one Finding while retaining both observations.
7. run ZAP passive and active tests against an intentionally vulnerable isolated target under explicit Authorization.
8. enforce target, rate, network, credential, time and destructive-action restrictions outside ZAP/Strix.
9. stop an unsafe active test, clean target state and prove read-back.
10. run Strix repeatedly, retain model/provider/prompt/tool/sandbox revisions and independently reject one unsupported claim.
11. route a generated patch through Code Ops tests and Sergeant/security review.
12. capture and replay one workload through ReproZip while retaining missing kernel/network/external-state limitations.
13. publish ClaimBound-style cards for pass, fail, blocked, drift and not-independently-reproduced outcomes.
14. prove a green/pass card cannot render without its boundary, limitations and allowed claim sentence.
15. run a SparkDistill-style manifest check, re-score and full/partial retrain as separate levels.
16. reject invalid/stale/mismatched attestation without treating valid attestation as semantic correctness.
17. preserve a failed or inconclusive reproduction without rewriting the original claim.
18. close and then regress one Finding through new immutable reports.
19. replace one scanner and one evidence-card renderer without changing Ptah Finding/Claim identity.
20. prove public evidence does not expose source, credentials, exploit details or customer data.

## Closure conclusion

Ptah now has a complete security and reproducibility design direction. Scanners, agents, replayers and validators produce bounded observations and evidence; Ptah retains exact target, scope, machinery, coverage, findings, review, reproduction and authority relationships. Security and reproduction become auditable workloads rather than one optimistic badge.
