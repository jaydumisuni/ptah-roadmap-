# ADR-0015 — Security Finding, Claim, Evidence, Authorization and Reproduction Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Phase:** 0A / Security, provenance and workload-proof completion

## Context

Ptah must execute and retain security/reproduction work without allowing a scanner result, agent statement, proof-of-concept, signed document, replay package or green dashboard to become universal truth.

The recovered donors solve complementary layers:

- Syft inventories packages/files and emits SBOMs;
- Grype matches package observations to vulnerability/advisory databases;
- Trivy scans vulnerability, misconfiguration, secret and licence classes across Artifacts and repositories;
- Semgrep performs source/configuration pattern and dataflow analysis;
- ZAP performs passive and active dynamic web/API testing;
- Strix is an optional autonomous offensive-validation workload that plans, executes, reports and proposes fixes;
- ReproZip captures observed Linux execution dependencies and builds replay bundles;
- ClaimBound renders narrow claims under frozen protocols while separating result, verification and reproduction level;
- SparkDistill demonstrates recipe/data/checkpoint/claim/attestation/recheck separation for AI-training workloads;
- GUAC aggregates SBOM, provenance, advisory and vulnerability relationships into a derived security graph;
- existing Ptah Build, Artifact, Object, Activity, Receipt, SBOM, attestation, signing, isolation, Browser, Application, Node and Sergeant boundaries already provide foundational identities and proof levels.

No donor defines Ptah's canonical Scan Target, Scanner Revision, Security Test Authorization, Finding Observation, stable Finding, Claim, Evidence, Adjudication, Exception, Remediation, Reproduction Recipe, Reproduction Run, Comparison or Closure identity.

## Decision

Ptah will own backend-neutral contracts for:

1. Security Test Authorization;
2. Scan Target and Target Revision;
3. Scanner, Engine, Ruleset, Database, Policy Bundle and Model Revision;
4. Scan Activity and attempt;
5. raw Scanner Report Artifact;
6. Finding Observation;
7. stable correlated Finding;
8. Claim and allowed claim boundary;
9. Evidence and Evidence Relationship;
10. Risk Assessment;
11. Adjudication;
12. Suppression, Exception and Accepted Risk;
13. Remediation Proposal and Remediation Change;
14. Verification/Re-scan and Finding Closure;
15. Reproduction Recipe and Recipe Revision;
16. Reproduction Bundle;
17. Reproduction Run and Comparison;
18. Evidence Card/public-safe View;
19. derived Security Graph revision;
20. independent review and release-gate decision.

Scanner, agent, repository, report, alert, check, rule, CVE, task, PoC, package, graph or card IDs remain aliases/references under Ptah identities.

---

# Core truth classes

## Target

The exact object or environment being assessed.

```text
scan_target_id
workspace_id
target_type
object_or_artifact_revision
git_repository_and_commit
image_digest_and_platform
deployment_or_service_revision
application_session_or_device_reference
source_paths_or_routes
created_at
```

A mutable branch, tag, URL or running environment is resolved to an exact revision/snapshot where possible. Where exact capture is impossible, the limitation and observation time are retained.

## Scanner Definition and Revision

```text
scanner_id
scanner_revision_id
tool_name
binary_or_image_digest
build_and_version
engine_or_feature_tier
configuration_digest
ruleset_revisions
vulnerability_database_revisions
policy_bundle_revisions
model_provider_and_model_revision
plugin_or_add_on_revisions
licence_and_provenance
capability_classes
known_limitations
```

A scanner name/version alone is insufficient. Results may depend on rules, databases, plugins, policies, models, remote services and target resolvers.

## Scan Activity

A Scan is a normal Ptah Activity with operation and attempt identity.

```text
scan_activity_id
security_authorization_id
scan_target_id
scanner_revision_id
started_at
completed_at
node_and_runtime_provider
isolation_class
network_and_credential_grants
resource_budget
status
coverage_summary
```

A completed Activity proves that the tool run reached its recorded terminal state. It does not prove complete coverage or correctness of findings.

## Raw Scanner Report Artifact

The complete native tool output, logs, errors, skipped inputs and metadata are retained as immutable restricted Artifacts.

Interchange views such as SARIF, SPDX, CycloneDX, JSON summaries, HTML, Markdown and public cards remain derived Views.

## Finding Observation

One detector/tool/source assertion.

```text
finding_observation_id
scan_activity_and_attempt
scanner_revision
scan_target_revision
finding_class
external_rule_alert_or_advisory_id
location_or_route
message_and_raw_severity
raw_confidence
source_span_or_http_exchange
package_or_configuration_reference
dataflow_or_exploit_trace
evidence_references
fingerprint_aliases
first_observed_at
```

Observations are never deduplicated away. They can be grouped/correlated while original detector disagreement remains visible.

## Finding

A stable Ptah issue identity that can aggregate multiple observations across time, tools and target revisions.

```text
finding_id
finding_class
subject_reference
canonical_title
state
created_at
superseded_or_split_relationships
```

Finding correlation is a reviewable Claim, not a destructive merge. A Finding can split, merge or link to another while retaining all historical observations.

## Claim

A bounded proposition supported or challenged by Evidence.

```text
claim_id
claim_revision
allowed_claim_sentence
claim_boundary
subject_and_period_scope
protocol_revision
status
limitations
created_by
```

Examples:

- "Package X version Y in Artifact Z matches advisory A under database revision D."
- "The authenticated endpoint accepted the demonstrated IDOR request in environment E at time T."
- "The frozen reproduction protocol produced output digest O within tolerance P."

Claims never exceed their target, time, protocol, evidence or reproduction boundary.

## Evidence

An immutable Object/Artifact/Receipt supporting, contradicting or limiting a Claim.

Evidence can include:

- source ranges;
- package records and SBOMs;
- scanner reports;
- database/rule/policy metadata;
- HTTP exchanges;
- screenshots/video;
- terminal/process logs;
- PoC scripts and outputs;
- read-back results;
- attestations and signatures;
- reproduction bundles/runs/comparisons;
- reviewer reports;
- negative and blocked outcomes.

Evidence Relationship states:

```text
supports
contradicts
limits
supersedes
reproduces
fails_to_reproduce
is_source_for
is_derived_from
```

## Risk Assessment

Risk is not one number.

Ptah retains separately:

```text
scanner_severity
standard_score_and_vector
confidence
reachability
exploitability
known_exploitation
probability_or_EPSS
business_impact
asset_criticality
exposure
remediation_cost
uncertainty
assessor_and_protocol
```

No scanner field directly becomes caller acceptance or release policy.

## Adjudication

A named authorized reviewer decides whether an Observation/Finding is:

```text
unreviewed
confirmed
likely
possible
false_positive
not_applicable
not_affected
duplicate_or_related
needs_more_evidence
accepted_risk
```

Adjudication preserves the original observation and states reviewer, rationale, scope, expiry and evidence.

---

# Finding classes

Ptah does not flatten all security output into one list.

```text
software_inventory
known_vulnerability_match
source_static_analysis
configuration_or_IaC
secret_or_credential_exposure
licence_observation
dynamic_web_or_API
runtime_or_behavioral
supply_chain_or_provenance
binary_or_malware
privacy_or_data_exposure
manual_or_agentic_security_claim
```

Each class has class-specific evidence and coverage semantics.

Examples:

- Syft inventory is not a vulnerability verdict.
- Grype/Trivy advisory match is not exploitability proof.
- Semgrep dataflow is not runtime execution proof.
- ZAP active response is not automatically business impact.
- Strix PoC is an agent-originated validation claim until independently reviewed/reproduced.
- Licence observation is not legal approval.
- Secret detection is not proof that the credential is valid or unrevoked.

---

# Coverage and negative evidence

Every scan records:

```text
requested_scope
resolved_scope
successfully_scanned_scope
skipped_scope
unsupported_scope
errors_and_timeouts
disabled_scanner_classes
rules_or_databases_unavailable
coverage_confidence
```

`no findings` means only:

> No finding observations were produced within the recorded successful scope, scanner revision and limitations.

It never means universally safe, clean, secure or vulnerability-free.

Negative, blocked, skipped, partial, drifted and failed-to-reproduce outcomes are retained as evidence.

---

# Active and offensive security authorization

Passive reading and active mutation have different authority.

## Security Test Authorization

Required before active scanning, fuzzing, exploit validation, credentialed testing, denial/stress behavior, post-exploitation or agentic pentesting.

```text
security_authorization_id
requestor
approver
owner_of_target
legal_and_policy_basis
target_environment_and_revision
included_hosts_routes_accounts_and_assets
excluded_hosts_routes_accounts_and_assets
test_classes
permitted_attack_and_destructive_actions
prohibited_actions
credential_and_test_data_references
network_and_rate_limits
time_window_and_expiry
isolation_class
monitoring_and_emergency_stop
backup_and_cleanup_plan
incident_contacts
```

A URL, repository or reachable host is never authorization.

## Execution rules

1. active security workloads run in an approved isolation class;
2. network egress is allowlisted to authorized targets/services;
3. credentials are short-lived and target-scoped;
4. destructive actions, load and data mutation have explicit classes/budgets;
5. production/customer targets require stronger approval and backup/rollback/read-back;
6. every tool/PoC action is logged as an operation/attempt where feasible;
7. emergency stop and cleanup are first-class Activities;
8. external LLM/provider transmission follows data/privacy policy;
9. unauthorized expansion of scope blocks the Activity;
10. active-test evidence is restricted by default.

---

# Scanner and donor composition

## Syft

Primary package/SBOM inventory Facility.

- native Syft JSON retained;
- SPDX/CycloneDX are derived Views;
- exact target digest/platform and cataloguers recorded;
- inventory completeness remains bounded.

## Grype

Primary package/advisory matching Facility.

- vulnerability database revision/freshness retained;
- CVSS, EPSS, KEV and reachability remain separate;
- VEX is a signed/scoped Claim, not deletion of the observation.

## Trivy

Primary broad Artifact/configuration scanner.

- vulnerability, misconfiguration, secret and licence classes remain separate;
- DB and policy-bundle revisions retained;
- original and ignored/not-affected/severity-adjusted states retained;
- secret values redacted while location/hash/revocation evidence remains.

## Semgrep

Primary source-level static analysis Facility.

- source span, rule/ruleset, engine tier, dataflow and errors/skips retained;
- community/local and advanced interfile capabilities are labelled honestly;
- autofix is a remediation proposal only.

## ZAP

Primary authorized web/API dynamic scanner.

- passive/active/manual/tool sources separated;
- target context, auth/session, rules/add-ons and HTTP evidence retained;
- alert filter/gate policy remains separate from raw alert;
- active tests require Security Test Authorization.

## Strix

Optional agentic offensive-validation workload.

- model/provider/prompt/tools/sandbox fixed per run;
- PoCs, CVSS and generated fixes are agent Claims;
- independent replay/review required;
- no autonomous scope/authorization or auto-merge authority.

## ReproZip

Optional observed execution-dependency capture/replay Facility.

- trace, editable recipe, bundle and replay remain separate;
- observation-time and packaging-time hashes compared;
- remote/external/nondeterministic state listed explicitly;
- bundle creation is not reproduction proof.

## GUAC

Optional derived security/provenance graph Facility.

- original documents remain source truth;
- graph edges retain source/parser lineage and uncertainty;
- graph vulnerability paths are derived Claims;
- graph is rebuildable and replaceable.

## ClaimBound

Evidence-card/export donor.

- allowed claim sentence and explicit claim boundary mandatory;
- result, reproduction, verification and review levels separate;
- negative/blocked/drift cards visible;
- public sanitized View never replaces restricted raw evidence.

## SparkDistill

Optional AI-training reproduction workload.

- recipe/data/checkpoint/metric claim/attestation/recheck separate;
- held-out re-score, partial retrain, full retrain and independent reproduction have different levels;
- model/data/provider licences and rights are mandatory;
- no automatic promotion into a caller product.

---

# Reproduction model

## Reproduction Recipe

A human-readable, versioned specification of what should be re-executed.

```text
reproduction_recipe_id
recipe_revision
source_and_input_objects
commands_or_activity_graph
environment_and_toolchain
node_architecture_and_capabilities
network_and_external_services
credentials_or_fixtures
clock_random_seed_locale
expected_outputs_and_tolerances
cleanup
known_uncaptured_state
```

## Reproduction Bundle

An immutable Artifact packaging the approved Recipe, Objects, manifests, hashes and required metadata.

Bundle creation proves only successful assembly.

## Reproduction Run

A new Activity on a selected Node/Provider/Isolation Class.

```text
reproduction_run_id
recipe_revision
bundle_revision
activity_and_attempt
target_environment
result_status
produced_outputs
limitations
```

## Comparison

```text
comparison_id
original_run_reference
reproduction_run_reference
exact_hash_comparisons
semantic_or_tolerance_comparisons
logs_and_side_effect_readback
variance_and_nondeterminism
status
reviewer
```

Reproduction levels:

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

Byte-identical output is not always required, but every tolerance/semantic comparison is frozen in the protocol.

Attestation/signature proves identity/integrity under a trust chain; it does not replace reproduction or semantic validation.

---

# Remediation and closure

## Remediation Proposal

May be produced by scanner, agent, human or caller but is not executable authority.

```text
remediation_proposal_id
finding_id
proposed_change
source_and_rationale
expected_effect
risk_and_compatibility
```

## Ownership

- caller/organization assigns the specialist security owner;
- Code Ops owns code patching and implementation changes;
- other departments own their specialist configuration/infrastructure changes;
- Sergeant owns independent engineering review/proof where applicable;
- Ptah records Activities, evidence and authority but does not become the organizational approver.

## Closure states

```text
open
triaged
in_remediation
mitigated
fixed_pending_verification
verified_closed
accepted_risk
not_applicable
false_positive
superseded
```

`verified_closed` requires:

1. approved remediation/change reference;
2. successful Build/test/deployment evidence as applicable;
3. targeted re-scan/reproduction;
4. negative read-back for the original vulnerability/claim;
5. no unacceptable regression under the frozen verification protocol;
6. authorized reviewer acceptance.

A scanner no longer reporting the issue is necessary evidence for some classes but not always sufficient proof.

---

# Suppression, exception and accepted risk

Suppressions never delete observations.

```text
exception_id
finding_or_observation
kind
issuer
rationale
scope
compensating_controls
created_at
expires_at
review_required_at
status
```

Kinds include:

```text
false_positive_suppression
not_affected_statement
temporary_exception
accepted_risk
policy_override
```

Expired exceptions automatically return the Finding to review-required/open policy state. VEX statements are mapped as scoped external Claims and do not rewrite scanner history.

---

# Evidence and public/private boundaries

Security evidence is restricted by default.

Sensitive classes include:

- source snippets and proprietary package inventory;
- secrets, credentials and tokens;
- HTTP requests/responses, cookies and personal data;
- exploit payloads and PoCs;
- network/topology and deployment details;
- vulnerability status before remediation;
- model/provider prompts and private datasets;
- internal risk decisions and accepted-risk rationale.

Public-safe evidence may expose:

- sanitized claim boundary;
- protocol/tool versions;
- signed hashes;
- high-level result/reproduction/review status;
- limitations;
- non-sensitive remediation/closure summary.

Evidence Cards are Views over underlying Claims/Artifacts and obey audience policy.

---

# Security graph and search

GUAC or a native Ptah graph may index:

- Packages, Sources and Artifacts;
- SBOMs and attestations;
- vulnerabilities/advisories/VEX;
- Findings and Observations;
- Builds and provenance;
- remediations and closure;
- scanners/rules/databases;
- reproduction/evidence relationships.

The graph is derived, versioned and rebuildable. Original documents/Artifacts remain authoritative.

Search results expose exact source/revision and permission-filtered evidence. Correlation confidence and conflicting edges remain visible.

---

# Proof levels

Security/reproduction proof is cumulative and class-specific.

```text
P0 tool_present
P1 scan_or_capture_completed
P2 observation_with_source_evidence
P3 adjudicated_finding_or_bounded_claim
P4 dynamically_validated_or_output_compared
P5 independently_reproduced_or_reviewed
P6 remediation_applied_with_build/deploy_evidence
P7 verified_closed_or_release_accepted
```

These levels do not collapse:

- Activity state;
- scanner confidence;
- severity;
- cryptographic signature;
- reproduction level;
- independent review;
- caller acceptance.

UI must name the exact level and limitations rather than showing one ambiguous green badge.

---

# Consequences

## Positive

- Scanner results remain evidence, not authority.
- Finding correlation preserves independent disagreement.
- Active tests have explicit legal/operational scope.
- Rule, DB, policy and model drift are reproducible.
- Negative and no-findings results are bounded honestly.
- Remediation ownership and independent review remain intact.
- Reproduction captures output comparison rather than bundle presence.
- Public proof can be useful without exposing raw security data.
- Every donor remains replaceable.

## Costs

- Security records are more complex than one report list.
- Raw reports and evidence require secure storage/redaction.
- Rules/database/model versions must be tracked.
- Active tests require authorization and cleanup workflows.
- Finding correlation and adjudication require human review.
- Independent reproduction can be expensive.

## Risks retained

- false positives/negatives;
- scanner and rule vulnerabilities;
- stale/poisoned databases;
- active-test damage;
- credential or data leakage;
- agent/model hallucination and prompt injection;
- exploit side effects;
- nondeterministic reproduction;
- mistaken correlation or suppression;
- supply-chain compromise of scanner images/plugins/rules.

These are explicit risk/evidence records rather than hidden behind a `passed` state.

---

# Rejected alternatives

## One universal security score

Rejected. Severity, confidence, exploitability, likelihood, impact, exposure and acceptance differ.

## Scanner output as release authority

Rejected. Release policy and reviewer acceptance remain separate.

## Deduplicate by deleting duplicate observations

Rejected. Independent detector agreement/disagreement is evidence.

## No findings equals secure

Rejected. Coverage and limitations are mandatory.

## Active agent/scanner can authorize itself

Rejected. Target ownership and permitted actions require external authorization.

## Signed report equals correct report

Rejected. Signature/attestation proves integrity/identity under a trust chain.

## Replay bundle equals reproduced

Rejected. Re-execution and output/side-effect comparison are separate.

## Generated fix auto-merge

Rejected. Code Ops/department implementation and independent review remain required.

## GUAC graph as canonical truth

Rejected. It is derived from retained source documents and parser assertions.

---

# Phase 0B requirements

Phase 0B must define schemas and conformance for:

1. Security Test Authorization;
2. Scan Target and Target Revision;
3. Scanner/Engine/Ruleset/DB/Policy/Model Revision;
4. raw Scanner Report Artifact;
5. Finding Observation and stable Finding;
6. Claim and allowed claim boundary;
7. Evidence and relationships;
8. Risk Assessment and Adjudication;
9. Suppression/Exception/Accepted Risk;
10. Remediation Proposal/Change and closure;
11. Reproduction Recipe/Bundle/Run/Comparison;
12. Evidence Card/public View;
13. Security Graph revision;
14. proof/reproduction/review levels;
15. coverage/negative/blocked records;
16. sensitive-evidence/audience policy;
17. scanner replacement and historical migration.

No implementation is authorized by this ADR.

## Related evidence

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
- existing Build/Artifact/Provenance ADRs and donor records
- `work-packages/PHASE-0A-WP12-SECURITY-REPRODUCTION-WORKLOADS.md`
