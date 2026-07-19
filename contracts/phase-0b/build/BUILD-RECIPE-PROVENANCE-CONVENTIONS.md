# Phase 0B WP07 — Recipe, Build, Provenance, SBOM, Signature and Verification Conventions

**Status:** CANDIDATE DRAFT  
**Date:** 2026-07-19  
**Contract family target:** `ptah.build` / `ptah.provenance` `0.1.0`  
**Implementation authorization:** NONE

## Purpose

Define backend-neutral Build Recipe, immutable Recipe Revision, proposal/readiness evidence, backend compilation, Build execution, output registration, cache use, secret access, SBOM, attestation, signature, verification and independent reproduction without selecting BuildKit, Dagger, ORAS, Syft, Witness, in-toto, Sigstore or one native platform backend.

This package composes:

- WP01 common identity/versioning and typed families;
- WP02 Activity, Operation, Attempt, Receipt, Review and Verdict;
- WP03 Content, Object Revision, Artifact, Location and release identity;
- WP04 Node, Facility, Provider, capability and generation evidence;
- WP05 Workspace Revision, Materialization, Session and checkpoint identity;
- WP06 Transfer, sync, backup and restore evidence;
- ADR-0005 Build/Artifact/Provenance boundary;
- ADR-0016 Security Finding/Validation/Reproduction boundary.

---

# 1. Required separation

Ptah keeps the following distinct:

```text
Build Recipe
Build Recipe Revision
Recipe Proposal / Detector Observation
Recipe Acceptance Decision
Build Readiness Assessment
Compiled Plan
Build Run
Build Step
Activity / Operation / Attempt
Cache Record
Cache Use Decision
Secret Access Grant / Observation / Cleanup
Output Declaration
Produced Object Revision
Artifact Promotion / Artifact Release
Package Observation
SBOM Document / Coverage
Attestation Statement
Attestation Verification
Signature
Signature Verification
Trust Policy
Review / Verdict
Reproduction Run / Comparison
Release Acceptance
```

No generic `build_status`, `verified`, `signed`, `reproducible` or `released` field may collapse these records.

---

# 2. Build Recipe identity

## 2.1 Build Recipe

`build.recipe` is the durable logical identity for one family of intended Build/test/package/render/transform work.

A Recipe is not:

- one YAML/TOML/JSON file;
- one Dockerfile;
- one Dagger module/function;
- one BuildKit LLB graph;
- one CI workflow;
- one Build Run;
- one backend or worker;
- one output Artifact;
- one release.

These remain source Objects, aliases, revisions, compiled plans, runs or relationships.

## 2.2 Recipe Revision

A Recipe Revision is immutable and content-hashed. It retains:

```text
recipe_ref
parent_revision_refs
recipe_type
workspace_revision_ref
source_material_bindings
requested_targets_and_platforms
step_graph
facility_and_capability_requirements
toolchain_and_environment_requirements
service_and_network_requirements
credential_reference_requirements
cache_policy
output_declarations
proof_requirements
SBOM requirements
attestation requirements
signing requirements
review requirements
caller policy references
limitations
```

After an accepted execution begins, the exact Recipe Revision is immutable. Changes create a new revision.

Recipe types include:

```text
source_build
container_image_build
test
package_or_installer
document_or_media_render
application_bundle
firmware_transform_or_rebuild
native_platform_build
composed_release
other_registered
```

## 2.3 Proposal and acceptance

Scanners, detectors, importers or callers may propose Recipe Revisions. A proposal records source evidence, confidence, inferred assumptions and unsupported areas.

A proposal is not accepted truth. Recipe Acceptance is an explicit decision by an authorized caller/policy over one exact proposal/revision.

---

# 3. Readiness

Build Readiness Assessment is immutable, time-bounded evidence over one exact Recipe Revision, Workspace Revision and candidate execution context.

It evaluates:

- source/input Object availability and hashes;
- required Facility/capability support;
- target platform/architecture;
- toolchain/environment availability;
- Provider/Node eligibility and freshness;
- storage capacity and output destinations;
- service/network requirements;
- credential references and policy;
- privacy/licence constraints;
- proof, SBOM, signing and review requirements;
- unsupported or altered Recipe semantics.

Decisions:

```text
ready
ready_with_conditions
blocked
incompatible
unknown
stale
```

Readiness does not create a Build Run and expires when any required input, capability, policy, generation or environment changes.

---

# 4. Compiled Plan

A Compiled Plan is one backend-specific translation of one exact Recipe Revision.

It retains:

```text
recipe_revision_ref
backend Facility/Provider revisions
compiler/adapter revision
plan Object/Content digest
backend aliases
step-to-operation mapping
selected platforms/workers
capability coverage
unsupported_or_altered_semantics
cache strategy
secret injection strategy
network/service strategy
output/export strategy
proof hooks
created_at
```

Rules:

1. Recipe identity survives backend replacement.
2. Two Compiled Plans may implement the same Recipe Revision.
3. Compilation never mutates the Recipe Revision.
4. Unsupported or altered semantics remain explicit and require acceptance.
5. Backend-local graph/step IDs are Aliases only.
6. A valid Compiled Plan does not prove readiness or successful execution.

---

# 5. Build Run and execution mapping

A Build Run is one caller-visible execution of one exact accepted Recipe Revision through one exact Compiled Plan.

Build Run binds:

- Workspace and Materialization generation;
- exact Recipe Revision and acceptance/readiness records;
- Compiled Plan;
- Build Facility/Provider revisions and generation;
- Node generation or approved remote-service identity;
- Activity;
- Build Steps and their Operation/Attempt mappings;
- selected cache decisions;
- secret access records;
- produced Objects/Artifacts/Locations;
- proof-generation and verification results;
- partial/failed stages and limitations.

A Build Step is a stable Recipe-level step identity for one Run. Each step maps to one or more logical Operations; each physical retry receives a new Attempt.

Build Run lifecycle remains separate from:

- Activity lifecycle;
- step/operation lifecycle;
- output availability;
- export result;
- SBOM/attestation/signature creation;
- verification/review/reproduction;
- Artifact promotion or Release acceptance.

Build Run lifecycle:

```text
requested
validating
compiling
queued
running
cancelling
cancelled
partially_completed
build_completed
failed
uncertain
```

`build_completed` means declared Build steps completed under the recorded plan. It does not mean export, SBOM, attestation, signing, verification, review, reproduction or release acceptance succeeded.

---

# 6. Inputs and materials

Every input/material binding resolves mutable aliases to exact immutable references before execution where possible.

Examples:

- Git branch/tag → repository commit;
- OCI tag → manifest/index digest and platform;
- package range → exact package/version/content digest;
- URL → retained source Object/Content digest plus retrieval evidence;
- Workspace path → exact Object Revision or declared mutable snapshot;
- service dependency → versioned service reference and observation window.

Mutable/unresolved inputs are explicit and may lower reproducibility.

Material classifications:

```text
deterministic_bound
mutable_but_snapshotted
volatile_declared
external_service_observed
unresolved_or_unknown
secret_reference
```

---

# 7. Cache boundary

Cache is derived reusable state, not source truth or independent proof.

## 7.1 Cache Record

A Cache Record binds:

```text
producer_recipe_revision
producer_compiled_plan
producer_run_step_operation_attempt
exact input/material digests
backend/toolchain/environment identity
policy and platform
output Object/Content digest
created_at
verification evidence
visibility and retention
```

## 7.2 Cache Use Decision

Every reuse decision records:

- candidate Cache Record;
- exact consumer Recipe Revision/Plan/Step;
- input/toolchain/environment/policy comparison;
- volatility evaluation;
- authorization and visibility scope;
- validation/read-back;
- accepted/rejected decision and reason;
- resulting Operation/Receipt mapping.

A cache hit does not equal executed work, independent reproduction or fresh proof.

## 7.3 Volatile inputs

Any input excluded from cache identity is explicitly marked volatile.

If a volatile input can affect observable output, the output is classified as reproducibility-limited until independently validated under a frozen protocol.

Cache eviction never deletes canonical Objects, Artifacts, Receipts or provenance history.

---

# 8. Secret and credential access

Recipes contain opaque credential references only.

Secret access records retain:

```text
credential_reference
trust_domain
recipient Activity/Operation/Attempt
access_scope_and_method
granted_at/expires_at
whether output identity may be affected
redaction policy
cleanup/revocation evidence
leak-scan evidence
limitations
```

Rules:

1. raw values never appear in Recipe, Plan, logs, cache metadata, SBOM, attestation, public Artifact, telemetry or schema fixtures;
2. Provider secret mounts/injection reduce exposure but do not prove executed code did not copy values;
3. output/cache/publication scans are required when policy demands;
4. expired/revoked credentials are not restored or reused silently;
5. cleanup/revocation is a separate receipted result;
6. secret-dependent output may require a restricted reproducibility/security classification.

---

# 9. Outputs and Artifact promotion

An Output Declaration states expected role, type, platform, path/selector, acceptance criteria, privacy/audience, retention and required proof.

Produced bytes become Content and Object Revisions under WP03. Export or registry push creates Storage Locations/Transfer evidence.

Artifact promotion is a separate decision over exact Object Revisions. Artifact Release remains a separate immutable allowlisted record.

Mutable tags, registry coordinates, filenames and URLs remain Aliases/Locations, never output identity.

A Build may produce valid Objects before a later export/proof/signing failure. Those Objects remain retained with honest partial state.

---

# 10. SBOM and package observations

## 10.1 Package Observation

One scanner/cataloguer assertion over an exact subject Object/Artifact Revision.

It retains:

- package/file identity and aliases;
- version and ecosystem;
- exact locations/evidence;
- detector/cataloguer and configuration;
- confidence and warnings;
- relationship to other observations.

## 10.2 SBOM Document

An SBOM is an immutable Artifact/View over one exact subject and one exact generator/configuration.

It records:

```text
subject Object/Artifact digest
scan source/scope
generator Facility/revision/configuration
format/schema version
package/file observations
relationships
coverage
skipped/unsupported/errors
privacy/redaction
storage/signature/attestation/verification refs
```

An SBOM is an inventory Claim. It does not prove completeness, vulnerability state, licence approval, runtime use or release acceptance.

Native scanner output and interoperable SPDX/CycloneDX Views remain related but distinct Artifacts.

---

# 11. Attestation

An Attestation Statement is an immutable signed or unsigned statement over exact subjects, predicate type/version, materials/products and producer identity.

Attestation creation is separate from:

- statement semantic validation;
- signature verification;
- policy verification;
- trust-root acceptance;
- subject/output correctness;
- caller/release acceptance.

Declared materials/products and automatically observed materials remain distinguishable.

Attestation Verification binds:

- exact statement/content digest;
- parser/schema revision;
- signature verification result where applicable;
- trust policy/root/version;
- expected predicate/layout/functionary policy;
- subject/material/product matching;
- freshness/transparency evidence;
- decision, limitations and Receipts.

---

# 12. Signature and trust

A Signature binds exact subject bytes/digest to one signer/key identity under one signing method.

Signature record retains:

```text
subject digest
signature Artifact/Content
signing method
signer identity or key reference
issuer/certificate
trusted-root candidate
transparency entry/proof or offline bundle
signed_at
privacy class
producer Activity/Receipt
```

Signature Verification is a new immutable record with:

- exact subject/signature;
- verifier revision;
- trust policy/root/version;
- certificate/identity/time validity;
- transparency inclusion or offline evidence;
- decision and limitations.

Decisions:

```text
valid_under_policy
invalid
untrusted_identity
expired_or_not_yet_valid
revoked
transparency_unavailable
incomplete
unknown
```

A valid signature proves digest binding and identity under the selected trust policy. It does not prove functionality, safety, reproducibility, review or release acceptance.

Public transparency may permanently disclose signer identity. Private/offline signing paths remain valid policy options.

---

# 13. Verification graph and proof domains

The following evidence domains remain separate:

```text
build_execution
output_integrity
export_availability
SBOM_inventory
attestation_creation
attestation_policy_verification
signature_verification
functional_test
independent_review
independent_reproduction
release_acceptance
```

No stronger domain is inferred from a weaker one.

A proof bundle may collect several records, but the bundle does not collapse their authority or limitations.

---

# 14. Independent reproduction

A Reproduction Run uses:

- the same accepted Recipe Revision or an explicit compatible migrated revision;
- independently selected Node/Provider/environment where required by protocol;
- declared cache-use policy;
- exact source/material/toolchain references;
- frozen comparison protocol;
- new Activities/Operations/Attempts/Receipts;
- new produced Object/Artifact identities.

A same-backend cache hit is not independent reproduction.

Comparison classes:

```text
byte_identical
functionally_equivalent_within_protocol
different_but_accepted_variance
not_equivalent
inconclusive
blocked
```

All differences and known nondeterminism remain evidence.

---

# 15. Failure and partial-state semantics

Ptah preserves stage-specific truth.

Examples:

- Build steps complete, export fails: Build Run may be `build_completed`; export Operation fails; local Objects remain.
- Build succeeds, SBOM fails: output remains; SBOM requirement is unsatisfied.
- Attestation created, verification fails: statement remains; verification record is negative.
- Signature created, transparency unavailable: signature remains; selected policy may classify verification incomplete.
- Review rejected after valid signature: signature remains valid under its trust policy; release is not accepted.
- Reproduction differs: original Build does not become failed; reproduction Comparison records divergence.
- final external effect is uncertain: Build/Operation remains uncertain and is not auto-retried without reconciliation.

No global success/failure state overwrites the underlying evidence.

---

# 16. Backend replacement

BuildKit, Dagger, native platform workers, CI systems, ORAS, SBOM generators, attestation tools and signing systems remain replaceable Facilities/Providers.

Replacement preserves:

- Recipe and Recipe Revision identity;
- Object/Artifact identity;
- public proof/verification contracts;
- Activities, Operations, Attempts and Receipts;
- source/material/output relationships;
- historical backend aliases and evidence.

Migration never rewrites old Plans, Runs, reports, signatures or verification records.

---

# 17. Minimum conformance invariants

1. Recipe, Revision, Proposal, Acceptance, Readiness, Plan and Run remain distinct.
2. every Run binds one exact accepted Recipe Revision and Compiled Plan.
3. mutable inputs are resolved or explicitly classified before execution.
4. Build Step/Operation/Attempt mappings preserve retry identity.
5. cache reuse is independently decided and cannot claim execution/reproduction.
6. secrets are references only and cleanup/leak evidence is explicit.
7. every produced output resolves to immutable Content/Object Revision before Artifact promotion.
8. mutable tags/paths/URLs never become Artifact identity.
9. SBOM coverage, skips and generator revision are mandatory.
10. attestation creation and verification are separate.
11. signature creation and verification are separate.
12. signature validity cannot imply functionality or release acceptance.
13. proof/signing/export failures after Build completion retain outputs and partial truth.
14. independent reproduction uses new execution evidence and explicit comparison.
15. backend replacement cannot change Recipe/Object/Artifact identity.
16. historical negative and inconclusive verification records remain immutable.

## No-build boundary

These are candidate contracts only. No BuildKit, Dagger, ORAS, Syft, Witness, in-toto, Sigstore, native compiler worker, signing infrastructure or Build UI implementation is authorized by this document.
