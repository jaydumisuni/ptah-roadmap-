# ADR-0005 — Build Recipe, Artifact and Provenance Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Phase:** 0A deterministic build and provenance closure

## Context

Ptah needs to build, test, package, render and transform many kinds of outputs while preserving enough evidence to answer:

- what was requested;
- which exact inputs were used;
- which environment, tools and worker performed the work;
- which operations were cached or executed;
- which Objects were produced;
- whether the output was inventoried, attested, signed, verified, reviewed or independently reproduced;
- where the output and proof are stored;
- whether a different backend can reproduce the same result.

The inspected systems solve different parts:

- Software Builder records project detection/readiness and shared-environment requirements but does not yet provide the complete execution engine.
- BuildKit provides low-level LLB graphs, workers, caching, secrets and exports.
- Dagger provides typed programmable recipes/modules above container/BuildKit machinery.
- ORAS stores and relates content-addressed OCI Artifacts.
- Witness collects versioned facts and creates/verifies signed in-toto/DSSE attestations.
- in-toto models planned supply-chain steps, functionaries, materials, products and inspections.
- Cosign/Sigstore/Fulcio/Rekor signs exact digests, binds identity and supplies transparency/offline verification.
- Syft creates versioned package/file inventories and standard SBOMs.

None is Ptah's universal Build, Artifact or proof model.

## Decision

Ptah will own four separate but linked contracts:

1. **Build Recipe** — the portable caller-visible description of intended work.
2. **Build Activity Graph** — concrete Activities/operations produced for one execution backend.
3. **Artifact/Object Graph** — immutable outputs, relationships and storage locations.
4. **Provenance and Verification Graph** — receipts, SBOMs, attestations, signatures, transparency evidence, reviews and reproduction results.

Backend-specific IDs remain references, not canonical Ptah identities.

---

# Build Recipe contract

A Build Recipe is versioned, immutable once executed and backend-neutral.

It must be able to describe:

```text
recipe_id
recipe_version
recipe_type
source_object_ids
source_repository_and_commit
workspace_id
requested_targets
platform_requirements
facility_requirements
toolchain_requirements
environment_or_image_references
steps_and_dependencies
input_object_bindings
secret_or_credential_references
service_requirements
cache_policy
network_requirement
outputs
proof_requirements
sbom_requirements
attestation_requirements
signing_requirements
review_requirements
caller_policy_references
```

The recipe does not contain raw secret values.

## Recipe types

The initial contract should support more than container-image builds:

- source build;
- container/image build;
- test;
- package/installer;
- document/media render;
- application bundle;
- firmware transformation/rebuild;
- native platform build;
- composed multi-stage release.

Backends declare which recipe capabilities they support.

## Detection and planning

Project/source scanners may propose a recipe and retain evidence/confidence, but automatic detection never becomes immutable truth without acceptance or explicit caller configuration.

A plan/readiness record is not a completed build.

---

# Execution backend boundary

## BuildKit

BuildKit is the primary low-level graph/cache/worker candidate for suitable OCI/containerized builds.

Ptah may compile recipe steps into LLB or invoke a supported frontend. BuildKit owns low-level DAG solving, cache, worker and export behavior. Ptah owns Activity/operation identity, receipts and Artifacts.

## Dagger

Dagger is the primary typed recipe/module donor and an optional Build Facility backend.

Dagger modules may implement reusable typed functions and cross-language APIs, but Dagger object/result IDs remain backend references.

## Native/platform backends

Windows, macOS, Android, firmware, device and other native operations may require platform workers or specialist Facilities. They use the same Build Recipe and proof contracts without pretending they are BuildKit/Dagger operations.

## Backend compilation record

Every execution retains:

- recipe version/hash;
- backend and adapter version;
- compiled graph/plan reference;
- unsupported or altered capabilities;
- exact workers/platforms selected;
- backend-specific references;
- cache decisions;
- operation mapping.

---

# Cache boundary

Cache is reusable derived state, not source truth or proof by itself.

Every cache hit must retain:

```text
cache_backend
cache_key_or_digest
producer_recipe_hash
producer_operation
input_digests
output_digest
created_at
last_verified_at
reuse_receipt
```

Cache classes may include shared, private, locked/exclusive and disposable.

## Volatile inputs

Any value configured not to affect cache identity must be explicitly marked as volatile.

If a volatile input can influence observable output, the resulting Artifact is marked non-reproducible or untrusted until independent validation proves otherwise.

## Cache eviction

Eviction may remove reusable bytes but never deletes canonical Artifact, receipt or provenance records.

---

# Secret and credential boundary

Recipes reference secrets/credentials by opaque reference.

Backends may mount or inject them for the minimum required operation. Ptah records:

- reference ID;
- providing trust domain;
- operation receiving access;
- access time and scope;
- whether the secret may affect output identity;
- redaction policy;
- cleanup/revocation result.

Raw values must not appear in recipes, logs, cache metadata, SBOMs, attestations, public Artifacts or telemetry.

A secret mount reduces accidental exposure but is not proof that executed code did not copy the secret. Proof plans must include leak scanning/redaction tests where appropriate.

---

# Artifact and Object graph

A Build Activity may produce several outputs. Each output becomes a Ptah Object and may be promoted to an Artifact.

Artifact records contain:

```text
artifact_id
artifact_type
artifact_version
object_ids
content_hashes
subject_or_parent_artifact_ids
recipe_id_and_hash
activity_id
operation_and_attempt_ids
source_material_ids
platform
producer_node_provider_facility
backend_references
storage_locations
created_at
verification_state
provenance_references
sbom_references
signature_references
review_references
reproduction_references
retention_and_visibility
```

Mutable tags/aliases are locations or labels, never immutable identity.

## Storage backends

Artifacts may live in:

- local content-addressed storage;
- R2/S3-compatible object storage;
- OCI registry/OCI layout through ORAS;
- Drive export/recovery bundles;
- other future backends.

No one backend is canonical truth. Content hash/Object identity remains stable across storage locations.

## Artifact relationships

Ptah defines versioned relationship types, including:

```text
built_from
contains
variant_of
supersedes
patch_for
sbom_for
attestation_for
signature_for
report_for
review_of
reproduction_of
checkpoint_of
export_of
cache_of
```

OCI subject/referrer relationships may carry these where suitable, but the Ptah catalogue remains richer and backend-neutral.

---

# SBOM boundary

Syft is the primary SBOM/package-inventory Facility candidate.

For each SBOM, Ptah records:

- exact subject Object/Artifact digest;
- scan scope/source type;
- Facility/version/configuration;
- schema/format version;
- package/file relationships;
- warnings and unsupported coverage;
- privacy/redaction class;
- storage locations;
- signature/attestation/verification links.

A generated SBOM is an inventory claim, not proof of completeness, vulnerability status, licence approval or runtime use.

Ptah may retain native Syft JSON plus interoperable SPDX/CycloneDX outputs.

---

# Attestation and in-toto boundary

## Ptah receipts

ADR-0004 receipts remain the broad native evidence format.

## Witness

Witness may collect versioned pre-material, material, execute, product and post-product facts and emit in-toto/DSSE attestations.

Witness attestors are evidence producers; their facts remain classified by authority and validation level.

## in-toto

Ptah may emit or verify in-toto-compatible Layout/Link/attestation records for declared Build/release chains.

Caller/project policy defines authorized functionaries, expected steps and rules. Ptah executes and records; it does not invent project-owner policy.

Declared materials/products and automatically observed dependencies must remain distinguishable. Missing observation coverage is surfaced explicitly.

---

# Signing and trust boundary

Cosign/sigstore-go are primary signing/verification Facility candidates.

Supported backend classes may include:

- public keyless Fulcio/Rekor;
- private Sigstore infrastructure;
- KMS/HSM/hardware keys;
- encrypted project keypairs;
- caller-provided PKI;
- offline bundle verification.

## Signing record

Every signature/verification receipt records:

```text
subject_digest
signature_artifact_id
signing_method
signer_identity_or_key_reference
issuer
certificate_reference
trusted_root_reference_and_version
transparency_entry_and_inclusion_proof
bundle_reference
signed_at
verified_at
verification_result
caller_authorization_policy_reference
privacy_class
limitations
```

A valid signature proves binding/identity under the selected trust root. It does not prove functional correctness or release acceptance.

Private signing identities, OIDC issuers, KMS/HSM details and company release policy remain outside public Ptah source.

## Transparency privacy

Public transparency logs may permanently retain signer identity information. Use requires explicit configuration and privacy acknowledgement. Private/offline signing paths remain available.

---

# Verification and reproducibility levels

Ptah distinguishes:

```text
planned
executed
build_completed
artifact_hash_verified
sbom_generated
attestation_generated
attestation_policy_verified
signature_verified
reviewed
functionally_tested
independently_reproduced
byte_identical_reproduction
functionally_equivalent_reproduction
release_accepted
```

A stronger level is never inferred from a weaker level.

## Independent reproduction

A reproduction must record:

- original recipe/source/input hashes;
- independently selected Node/worker/environment identity;
- cache-use policy;
- produced output hashes;
- byte-identical or functional-equivalence comparison;
- differences and known nondeterminism;
- reviewer/verifier identity.

A cache hit on the same backend is not independent reproduction.

---

# Build result and failure semantics

Build/recipe execution distinguishes:

```text
plan_created
readiness_blocked
queued
running
partially_completed
cancelled
failed
build_completed
artifact_export_failed
sbom_failed
attestation_failed
signing_failed
verification_failed
review_required
accepted
```

A successful compile with failed export/signing/proof remains partially complete, not universally failed or accepted.

Artifacts created before failure are retained with partial/provisional state and receipts.

---

# Donor decisions

- **Software Builder:** internal requirements and scanner/planner donor; not the execution engine.
- **BuildKit:** primary low-level build graph/cache/worker candidate.
- **Dagger:** primary typed recipe/module donor and optional backend.
- **ORAS:** OCI Artifact transport/referrer backend.
- **Witness:** attestor/policy Facility and proof donor.
- **in-toto:** supply-chain step/material/product interoperability model.
- **Cosign/Sigstore/Fulcio/Rekor:** signing, identity, trust and transparency backend set.
- **Syft:** primary SBOM/package-inventory candidate.

All remain behind Ptah-owned contracts and exit strategies.

---

# Consequences

## Positive

- Ptah reuses mature machinery without losing backend independence.
- Build planning, execution, output identity, inventory, attestation, signing, review and reproduction remain honest separate states.
- Container and native/platform builds can share one public contract.
- Private signing/release policy remains outside public Ptah.
- Artifacts can move among R2/S3, OCI and local stores without identity changes.
- Cache improves speed without becoming proof.

## Costs

- Several linked schemas and adapters are required.
- Provenance and reproduction increase storage/compute overhead.
- Secret and signing infrastructure require careful deployment.
- Some Artifacts will remain partially verified rather than receiving one simple success flag.
- Backend compilation and compatibility tests must be maintained.

## Do-not-break rule

> Never treat a Build plan, process exit code, cache hit, Artifact upload, SBOM, attestation, signature, transparency entry or review as universal completion. Each proves a different claim and must remain linked to exact Objects, operations, identities and verification levels.

---

# Required proof before freeze

1. Run one typed recipe through Dagger/BuildKit and one alternate/native backend under the same Ptah contract.
2. Prove parallel graph execution and deterministic cache invalidation.
3. Confirm secrets never enter logs, caches, SBOMs, attestations or outputs.
4. Register each output as an immutable Artifact with multiple storage locations.
5. Attach an SBOM, attestation, signature and report through ORAS relationships.
6. Verify in-toto/Witness policy and signer identity independently.
7. Move an OCI tag and prove Artifact identity remains digest-bound.
8. Verify offline using local Artifact, bundle and trusted root.
9. Perform an independent reproduction and classify byte-identical versus functional equivalence.
10. Fail signing or attestation after a successful build and preserve honest partial state.
11. Replace Dagger or the registry backend without changing public Recipe/Artifact identity.
12. Retain all recipe, tool, image, worker, cache and proof references required for audit.
