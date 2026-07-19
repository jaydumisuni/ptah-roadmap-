# Phase 0B WP07 — Recipe, Build, Provenance, SBOM, Signature and Verification Conventions

**Status:** CANDIDATE DRAFT  
**Date:** 2026-07-19  
**Contract family target:** `ptah.build` / `ptah.provenance` `0.1.0`  
**Implementation authorization:** NONE

## Purpose

Define the exact identities, state boundaries and proof relationships required to describe intended Build work, compile it for replaceable backends, execute it through Ptah Activities, register outputs, inventory software, attest production facts, sign exact subjects, verify policy and perform independent reproduction.

This package composes WP01 common identity, WP02 Activity/Attempt/Receipt proof, WP03 Object/Artifact/Location, WP04 Node/Facility/Provider capability, WP05 Workspace/Session/recovery and WP06 Transfer/Backup contracts. It does not select BuildKit, Dagger, ORAS, Syft, Witness, in-toto, Sigstore or any native/platform backend.

---

# 1. Required separation

Ptah keeps the following distinct:

```text
Build Recipe
Build Recipe Revision
Recipe Proposal / Detection Observation
Recipe Acceptance or Configuration Decision
Compiled Plan
Backend Capability/Compatibility Decision
Build Run
Build Step / logical Operation
Physical Attempt
Cache Record
Cache Use Decision
Secret/Credential Access Record
Build Output Record
Object / Artifact / Artifact Release
SBOM
Package Observation
Attestation
Attestation Verification
Signature
Signature Verification
Transparency Evidence
Review / Verdict / caller acceptance
Reproduction Run
Comparison
```

None may be collapsed into one `build_status`, one backend job, one OCI manifest or one generic proof flag.

Backend graph IDs, job IDs, worker IDs, cache keys, image tags, registry references, package IDs, signature bundle IDs and transparency-log entry IDs remain scoped Aliases/evidence.

---

# 2. Build Recipe identity

## 2.1 Stable Recipe

`build.recipe` is the stable caller-visible identity of one intended Build/test/package/render/transform/release workflow family.

A Recipe is not:

- one detector result;
- one mutable project configuration file;
- one Dagger object/function ID;
- one BuildKit LLB digest;
- one Dockerfile path;
- one CI workflow/job;
- one Build Run;
- one output Artifact;
- one release approval.

## 2.2 Immutable Recipe Revision

Every executable configuration is an immutable Recipe Revision retaining at minimum:

```text
recipe_ref
recipe_revision_id
parent_revision_refs
canonical_revision_digest
recipe_type
source_and_input_bindings
requested_targets
platform_requirements
facility_and_capability_requirements
toolchain_and_environment_requirements
service_and_network_requirements
steps_and_dependencies
cache_policy
volatile_input_declarations
secret_and_credential_references
output_declarations
proof_requirements
sbom_requirements
attestation_requirements
signing_requirements
review_and_acceptance_requirements
caller_policy_refs
created_by
created_at
```

Executed Recipe Revisions are immutable. A change creates a new Revision and explicit compatibility/supersession relationship.

## 2.3 Recipe types

Initial neutral Recipe types include:

```text
source_build
container_or_image_build
test
package_or_installer
document_or_media_render
application_bundle
firmware_transform_or_rebuild
native_platform_build
composed_multi_stage_release
other_registered
```

Recipe type does not select one backend.

---

# 3. Detection, proposal and acceptance

Project/source scanners may create a Recipe Proposal containing:

- exact scanned Object/Revision/repository/commit references;
- detector/tool/configuration revision;
- evidence paths and observations;
- proposed project type, targets and entry points;
- confidence and ambiguity;
- missing tools/resources/configuration;
- warnings, skipped inputs and parse failures;
- suggested Recipe Revision content.

Rules:

1. detector output is an Observation/Proposal, not accepted Recipe truth;
2. hidden/suppressed scan failures are forbidden;
3. caller or authorized policy may accept, reject, correct or merge proposals;
4. acceptance creates or selects an immutable Recipe Revision;
5. a readiness or Build plan record is not a completed Build;
6. target-specific blocked reasons remain explicit and do not automatically block unrelated targets.

---

# 4. Backend compilation and compatibility

## 4.1 Compiled Plan

`build.compiled_plan` is one immutable backend-specific translation of one exact Recipe Revision.

It retains:

```text
recipe_revision_ref
backend_facility_revision_ref
provider_revision_ref
compiler_adapter_revision
compiled_graph_or_plan_digest
step_to_operation_mapping
backend_capability_requirements
resolved_platforms_workers_and_environments
resolved_input_digests
cache_and_export_mapping
secret_delivery_mapping
unsupported_capabilities
altered_or_weakened_semantics
known_limitations
created_activity_and_receipts
```

A Compiled Plan is not the Recipe and cannot silently change Recipe intent.

## 4.2 Compatibility result

Compilation/compatibility decisions are directional and target-specific:

```text
compatible
compatible_with_declared_conversion
compatible_with_reduced_scope
incompatible
unknown
stale
```

Rules:

- unsupported required capability blocks the affected target;
- optional capability loss is explicit and operation-scoped;
- silent isolation, proof, platform or output weakening is forbidden;
- backend/provider/adapter revision changes expire prior compatibility where policy requires;
- BuildKit, Dagger and native plans may coexist under one Recipe Revision.

---

# 5. Build execution

## 5.1 Build Run

`build.run` is one execution of one exact Recipe Revision through one exact Compiled Plan.

A Build Run binds:

```text
workspace_ref
recipe_revision_ref
compiled_plan_ref
facility_revision_ref
provider_instance_and_generation
node_or_remote_service_locality
materialization_generation
activity_ref
resolved_input_and_material_refs
resolved_environment_and_tool_refs
cache_policy_snapshot
proof_policy_snapshot
started_at
```

## 5.2 Steps and Ptah work identity

Each logical Build step maps to one or more WP02 Operations. Every physical execution is a new Attempt with exact Node/Provider/workload/materialization generations, connection epoch, nonce and backend aliases.

A backend job retry cannot reuse Ptah Attempt identity.

Parallel branches retain explicit dependency edges. A global Build Run must not block unrelated Activities or unrelated branches without a declared dependency/resource constraint.

## 5.3 Outcome dimensions

Build execution retains separate dimensions for:

```text
recipe_acceptance
plan_compilation
readiness
execution
output_registration
export_or_transfer
sbom
attestation
signature
verification
review
reproduction
release_acceptance
```

A successful compile/process exit does not imply any later dimension passed.

---

# 6. Inputs, materials and environment truth

Every Build Run freezes exact references for:

- source Object/Revisions and repository commit/tree/tag resolution;
- declared external materials and automatically observed materials;
- base images by digest/platform rather than mutable tag alone;
- toolchain binaries/packages and versions;
- environment/image/Workspace Revision and Materialization generation;
- service dependencies and endpoints as scoped references;
- platform/architecture/ABI/SDK/runtime constraints;
- network mode and approved external sources;
- Node/Provider capability evidence and freshness;
- caller/policy/permission refs.

Mutable aliases may be recorded for usability but never replace exact digests/revisions.

Declared materials and observed materials remain distinguishable. Missing observation coverage is explicit.

---

# 7. Cache boundary

## 7.1 Cache Record

`build.cache_record` is reusable derived state and retains:

```text
producer_recipe_revision_ref
producer_run_and_operation_refs
producer_attempt_ref
input_and_environment_digests
cache_key_scheme_and_version
output_object_digests
backend_and_location_refs
cache_class
created_at
last_verified_at
integrity_and_compatibility_evidence
retention_and_eviction_policy
limitations
```

Cache is not source truth, Artifact identity, independent proof or release acceptance.

## 7.2 Cache Use Decision

Every reuse decision names:

- exact requested Operation/target;
- candidate Cache Record;
- input/toolchain/environment/policy comparison;
- backend compatibility;
- freshness/integrity result;
- accepted/rejected reason;
- resulting Receipt and output correlation.

A cache hit must remain visible as reused work rather than falsely reported as newly executed.

## 7.3 Volatile inputs

An input configured not to affect cache identity is explicitly `volatile`.

If a volatile input can affect observable output:

- the output is marked non-reproducible or trust-reduced;
- the reason and affected outputs are recorded;
- independent validation may raise confidence but cannot erase the original volatile-input fact.

Cache eviction may remove reusable bytes but never deletes canonical Objects, Artifacts, Receipts or provenance records.

---

# 8. Secrets and credentials

Recipes and plans contain opaque Credential References only.

A Secret/Credential Access Record binds:

```text
credential_reference
provider_or_trust_domain
recipient_operation_and_attempt
provider_materialization_generation
destination_and_access_mode
issued_at
expires_at
revocation_or_cleanup_result
may_affect_output_identity
redaction_and_privacy_policy
receipts_and_limitations
```

Rules:

1. raw values are absent from recipes, plans, logs, cache metadata, SBOMs, attestations, telemetry and public Artifacts;
2. minimum scope and lifetime are required;
3. stop, failure, lease loss, generation change or policy action revokes access;
4. secret mounts reduce accidental exposure but do not prove executed code did not copy secrets;
5. leak scanning/redaction evidence is required where policy demands;
6. private signing/release credentials remain outside public Ptah schemas and source.

---

# 9. Output and Artifact boundary

A Build Output Record declares what one Operation/Attempt produced before or while outputs become WP03 Objects/Artifacts.

It retains:

- output declaration/key and expected type;
- producing Activity/Operation/Attempt and exact generations;
- produced Content/Object/Revision refs and digests;
- Artifact promotion/release refs where applicable;
- Location and Transfer refs;
- completeness and finalization state;
- provenance, SBOM, attestation, signature and verification refs;
- partial/provisional/failed-export limitations.

Rules:

1. output bytes are registered as Objects before durable Artifact claims;
2. Artifact promotion does not imply verification, review, signature or release;
3. mutable tags/labels remain Aliases;
4. OCI/ORAS presence is one Location/relationship path, not canonical identity;
5. successful Build with failed export/signing/proof retains valid produced Objects and honest partial state;
6. failed/cancelled Runs retain any produced provisional outputs and cleanup state.

---

# 10. SBOM and package observations

`provenance.sbom` is one immutable software-inventory document over one exact subject digest/platform/revision.

It retains:

```text
subject_object_or_artifact_ref_and_digest
subject_platform_and_scope
generator_facility_provider_revision
scanner_configuration_and_cataloguer_set
native_raw_report_artifact_ref
interoperable_view_refs
package_observation_refs
coverage_skipped_unsupported_and_error_records
privacy_and_redaction_class
created_activity_attempt_receipts
freshness_and_supersession
```

Package Observations remain plural detector claims with locations, source method, confidence and aliases such as PURL/CPE/licence assertions.

Rules:

- SBOM generation is not proof of completeness;
- zero packages may mean unsupported/opaque input;
- static inventory does not prove runtime use, vulnerability, exploitability or licence approval;
- native Syft, SPDX and CycloneDX representations are related Views and conversion may be lossy;
- tool/configuration/cataloguer changes create a new SBOM revision/result;
- signatures/attestations prove document binding/identity, not inventory correctness.

---

# 11. Attestation and policy verification

## 11.1 Attestation

`provenance.attestation` is an immutable statement/envelope over exact subjects and predicates.

It retains:

- exact Activity/Operation/Attempt and generations;
- predicate type/schema/version;
- materials/products and whether each was declared or observed;
- producer/attestor identity and revision;
- collection stage such as pre-material, material, execute, product or post-product;
- DSSE/in-toto or other interoperable envelope refs;
- signature refs;
- privacy/redaction classification;
- limitations and missing facts.

Attestation creation is evidence production, not policy PASS.

## 11.2 Attestation Verification

Verification names:

- exact attestation bytes/digest;
- exact policy/layout/rules revision;
- authorized functionaries/identities;
- trusted roots and signature-verification refs;
- predicate/schema validation;
- material/product/step rule results;
- result, limitations, expiry and Receipts.

A valid signature with policy-failing facts is not accepted. Missing required attestation is explicit degraded/failed proof, never silent success.

Caller/project policy remains external authority; Ptah executes and records it.

---

# 12. Signature, trust and transparency

## 12.1 Signature

`provenance.signature` binds exact subject bytes/digest to one signing event.

It retains:

```text
subject_ref_and_digest
signature_artifact_ref
signing_method
signer_identity_or_key_reference
issuer_and_certificate_refs
trusted_root_family
transparency_or_timestamp_refs
portable_bundle_ref
signed_at
privacy_class
activity_operation_attempt_receipts
```

Signing methods may include public keyless, private Sigstore, KMS/HSM, hardware key, encrypted project keypair, caller PKI or offline-compatible methods.

## 12.2 Signature Verification

Verification records exact:

- subject digest;
- signature/certificate/bundle bytes;
- expected signer identity/issuer/key constraints;
- trusted-root revision and retrieval time;
- transparency inclusion/log-integrity evidence where required;
- offline/online mode;
- policy authorization result;
- verification result and limitations.

A valid signature proves binding and identity under the selected trust model. It does not prove functional correctness, SBOM completeness, attestation truth, review PASS or release acceptance.

## 12.3 Transparency privacy

Public transparency may permanently disclose signer identity. Use requires explicit policy and privacy acknowledgement. Public services are optional; private and offline paths remain valid contract implementations.

Transparency entry presence is not Artifact storage or Ptah Activity history.

---

# 13. Verification, review and reproduction

Ptah keeps these bounded outcomes separate:

```text
planned
compiled
executed
build_completed
output_registered
artifact_hash_verified
sbom_generated
attestation_generated
attestation_policy_verified
signature_verified
functionally_tested
reviewed
independently_reproduced
byte_identical_reproduction
functionally_equivalent_reproduction
release_accepted
```

No stronger outcome is inferred from a weaker one.

## Independent reproduction

A Reproduction Run records:

- original Recipe Revision and exact inputs/materials;
- reproduction protocol and acceptance tolerances;
- independently selected Node/Provider/environment/toolchain;
- cache policy, including whether original cache was forbidden;
- produced Objects/Artifacts and digests;
- Comparison result;
- nondeterminism sources and differences;
- reviewer/verifier identity and Receipts.

A cache hit or rerun on the same original backend/environment is not independent reproduction.

Comparison types include exact bytes, normalized/semantic equivalence, functional test equivalence and declared tolerance. Functional equivalence never becomes byte-identical.

Release acceptance remains an explicit caller/authority decision over exact subjects and evidence.

---

# 14. Partial failure and lifecycle truth

A Build Run may finish execution while later dimensions fail.

Valid examples:

- Build completed; export failed;
- output registered; SBOM failed;
- Artifact valid; attestation missing;
- signature valid; signer unauthorized by release policy;
- all proof produced; review pending;
- reproduction functionally equivalent but not byte-identical.

Rules:

1. partial/provisional outputs and evidence are retained;
2. cleanup state is explicit;
3. failed proof does not rewrite successful earlier execution evidence;
4. successful execution does not hide failed proof/export/signing;
5. cancellation and retry follow WP02 idempotency/uncertainty rules;
6. stale backend/job events cannot change current-generation Run truth.

---

# 15. Migration and backend replacement

Migration must not:

- promote scanner proposal to accepted Recipe without authority;
- use Dockerfile/path/job ID/LLB digest as canonical Recipe or Run identity;
- omit exact source/material/tool/environment digests;
- treat process exit or backend success as universal completion;
- treat cache hit as independent execution or proof;
- hide volatile inputs;
- serialize raw secrets/keys/tokens;
- turn OCI tag/referrer presence into Artifact identity or verification;
- turn SBOM into complete composition truth;
- turn attestation/signature into correctness or release acceptance;
- delete partial outputs/evidence after later proof failure;
- claim independent reproduction from same-cache reuse;
- silently merge differing Recipe revisions or provenance graphs.

Backend replacement:

1. preserves Recipe and Artifact/Object identities;
2. creates a new Compiled Plan for the replacement backend;
3. re-evaluates compatibility/capabilities;
4. uses new Provider/Run/Attempt generations and aliases;
5. revalidates cache portability rather than assuming it;
6. preserves all earlier outputs, Receipts, attestations, signatures and failures;
7. compares outputs under an explicit reproduction/compatibility protocol.

---

# 16. Required conformance cases

1. scanner proposes a Recipe but cannot execute until accepted/configured;
2. one Recipe Revision compiles to BuildKit/Dagger and alternate/native plans;
3. unsupported backend capability remains explicit and blocks only affected target;
4. parallel steps retain exact dependency and Activity/Operation/Attempt mapping;
5. cache hit preserves producer provenance and is not reported as newly executed;
6. changed input invalidates only dependent cache entries;
7. volatile output-affecting input lowers reproducibility trust;
8. raw secrets are absent from logs, caches, SBOMs, attestations and outputs;
9. successful Build with failed export/signing/proof remains honest partial state;
10. every output becomes an exact Object before Artifact promotion;
11. mutable registry tag movement does not change Artifact identity;
12. SBOM retains generator/cataloguer/coverage/errors and does not claim completeness;
13. valid attestation signature with policy-failing facts is rejected;
14. valid Artifact signature from unauthorized signer is not release-accepted;
15. offline verification succeeds from local subject, bundle and trusted root where policy permits;
16. public transparency identity disclosure requires explicit privacy policy;
17. same-backend cache reuse is rejected as independent reproduction;
18. byte-identical and functional-equivalent outcomes remain distinct;
19. backend replacement preserves public Recipe/Artifact identity;
20. stale-generation backend evidence is retained but cannot prove current work.

## Do-not-break rule

> Never collapse Recipe intent, compiled backend plan, Build execution, cache reuse, output identity, SBOM inventory, attestation facts, signature binding, policy verification, review, reproduction and release acceptance. Each answers a different question and must remain bound to exact Objects, Activities, identities, generations and evidence.
