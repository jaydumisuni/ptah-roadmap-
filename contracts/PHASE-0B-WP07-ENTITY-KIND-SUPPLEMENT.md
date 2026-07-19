# Ptah Phase 0B WP07 — Recipe, Build and Provenance Entity-Kind Supplement

**Parent registry:** `ptah.entity-kind` `0.1.0`  
**Status:** CANDIDATE — normative supplement  
**Date:** 2026-07-19

## Purpose

Register stable entity kinds required by WP07 while preserving the existing Build, provenance, proof, Object, Activity, Facility, Provider, Workspace and identity families.

Registration does not authorize implementation or select a backend.

---

# Inherited kinds used directly

WP07 uses these existing registry kinds without changing their meaning:

| Token | WP07 use |
|---|---|
| `build.recipe` | stable caller-visible Build Recipe identity |
| `build.compiled_plan` | immutable backend-specific translation of a Recipe Revision |
| `build.run` | one Build execution root |
| `build.cache_record` | reusable derived cache entry with producer evidence |
| `provenance.sbom` | immutable SBOM/software-inventory document root |
| `provenance.package_observation` | one package/file inventory assertion |
| `provenance.attestation` | immutable attestation statement/envelope |
| `provenance.signature` | signature over an exact subject digest |
| `provenance.verification_run` | generic provenance verification execution where a more specific kind is not required |
| `provenance.graph_revision` | derived provenance relationship graph revision |
| `proof.reproduction_run` | independent/repeated execution under a frozen Protocol |
| `proof.comparison` | exact/semantic/tolerance comparison |
| `proof.review` | evaluator review over exact Build/provenance evidence |
| `proof.verdict` | versioned review conclusion |
| `proof.protocol` | frozen verification/reproduction method |
| `identity.approval` | explicit acceptance/rejection over an exact Recipe, Build or release subject |
| `identity.credential_reference` | opaque secret/key/token reference |
| `core.activity` | durable Build/proof work root |
| `core.operation` | logical Build/proof effect |
| `core.attempt` | one physical execution try |
| `proof.receipt` | immutable producer evidence |
| `object.object` | exact output/report/signature/bundle bytes |
| `object.artifact` | durable promoted result role |
| `object.artifact_release` | immutable released/published Artifact revision |
| `storage.location` | one backend materialization |
| `runtime.provider_revision` | exact Build/SBOM/signing/verifier implementation revision |
| `runtime.provider_instance` | one active Provider incarnation/generation |
| `core.facility` | stable Build/SBOM/signing/verification contract |

---

# New WP07 kinds

| Token | Meaning |
|---|---|
| `build.recipe_revision` | immutable executable/configured revision of one stable Build Recipe |
| `build.recipe_proposal` | scanner/planner proposal with evidence, confidence and limitations |
| `build.recipe_acceptance` | authority decision accepting/rejecting/correcting one proposed or configured Recipe Revision |
| `build.backend_compatibility` | target-specific directional compatibility result between Recipe Revision and backend/provider revision |
| `build.step_run` | one logical Build-step execution projection linked to WP02 Operations/Attempts |
| `build.cache_use` | immutable decision/result for accepting or rejecting one Cache Record for one requested step/Operation |
| `build.secret_access` | scoped secret/credential delivery/use/cleanup evidence for one exact Operation/Attempt |
| `build.output_record` | output declaration/result binding one producer Attempt to exact Objects/Artifacts/Locations |
| `provenance.sbom_revision` | immutable revision/result of an SBOM identity, generator configuration and subject scope |
| `provenance.attestation_verification` | policy/trust verification result over one exact attestation |
| `provenance.signature_verification` | trust/signature verification result over one exact subject/signature/bundle |
| `provenance.transparency_evidence` | immutable transparency/timestamp inclusion and log-integrity evidence |

---

# Identity rules

1. A Recipe path, Dockerfile, project folder, CI workflow, Dagger function, BuildKit LLB digest or backend job ID is not `build.recipe` identity.
2. Every executed configuration uses an immutable `build.recipe_revision`.
3. A detector/scanner result is `build.recipe_proposal`; it does not become Recipe truth without `build.recipe_acceptance` or equivalent exact authority evidence.
4. `build.compiled_plan` belongs to one exact Recipe Revision and backend/provider revision.
5. `build.run` persists across its step graph but never across independent executions.
6. Physical retries remain WP02 `core.attempt` entities; a `build.step_run` does not replace Attempt identity.
7. Cache backend keys and Dagger/BuildKit result IDs remain Aliases inside `build.cache_record`/`build.cache_use`.
8. `build.output_record` does not replace WP03 Object/Artifact identity.
9. One SBOM generation creates a new `provenance.sbom_revision`; format Views may differ without changing the exact native report bytes.
10. Signature, attestation and their verification records are separate entities.
11. Transparency-log IDs are references in `provenance.transparency_evidence`, not Ptah signature or Artifact identity.
12. Independent reproduction remains `proof.reproduction_run`; comparison remains `proof.comparison`.
13. Release acceptance uses exact `identity.approval`, `proof.review` and/or `proof.verdict` rather than a Build lifecycle state.

---

# Typed-family rules

## Recipe family

```text
build.recipe
  stable identity

build.recipe_revision
  immutable configured/executable revision

build.recipe_proposal
  detector/planner evidence

build.recipe_acceptance
  authority decision over proposal/revision
```

## Execution family

```text
build.compiled_plan
  backend-specific translation

build.backend_compatibility
  directional compatibility result

build.run
  execution root

build.step_run
  logical step projection

core.operation / core.attempt
  exact Ptah work and physical tries
```

## Cache and secret family

```text
build.cache_record
  reusable derived bytes/state

build.cache_use
  decision to accept/reject reuse

build.secret_access
  scoped delivery/use/cleanup evidence
```

## Output and provenance family

```text
build.output_record
  producer-to-output binding

object.object / object.artifact / object.artifact_release
  canonical output/result/release identity

provenance.sbom / provenance.sbom_revision
  inventory document identity/results

provenance.package_observation
  plural package/file assertions

provenance.attestation
  asserted production facts

provenance.attestation_verification
  policy/trust evaluation

provenance.signature
  digest/identity binding

provenance.signature_verification
  trust verification

provenance.transparency_evidence
  inclusion/timestamp/log evidence
```

---

# Authority and proof rules

1. Recipe Proposal confidence is not execution authority.
2. Recipe Acceptance does not prove backend compatibility or Build success.
3. Compiled Plan existence does not prove readiness or execution.
4. Build completion does not prove output registration, SBOM, attestation, signature, review, reproduction or release acceptance.
5. Cache Use acceptance proves only policy-compatible reuse under the recorded comparison.
6. SBOM and Package Observations remain inventory claims with explicit coverage.
7. Attestation creation is not attestation-policy verification.
8. Signature creation is not signature verification.
9. Signature verification is not functional correctness or release acceptance.
10. Transparency inclusion is not signature authorization or Artifact storage.
11. Reproduction Run is not independent when it reuses the original backend/cache/environment contrary to protocol.
12. Every proof/result references exact subject bytes/digests, revisions, Activities, Attempts and Provider generations.

---

# Conformance requirements

- reject backend/path/job identifiers used as canonical Recipe or Build Run identity;
- reject executed Recipe without immutable Recipe Revision;
- reject Recipe Proposal promoted without authority evidence;
- reject Compiled Plan that silently weakens required capability/proof/isolation/output semantics;
- reject retry that reuses Attempt identity;
- reject Cache Use without producer/input/toolchain/environment/integrity comparison;
- reject volatile output-affecting input hidden from reproducibility state;
- reject raw credential material in ordinary entities/logs/SBOMs/attestations/public exports;
- reject output record that lacks exact producer Attempt and Object digest;
- reject mutable tag as exact Artifact subject;
- reject SBOM completeness claim without bounded protocol/evidence;
- reject attestation PASS inferred from creation/signature alone;
- reject release acceptance inferred from valid signature;
- reject public transparency identity disclosure without explicit privacy policy;
- reject same-cache rerun claimed as independent reproduction;
- preserve all partial outputs and failed proof/signing evidence.

## Do-not-break rule

> Entity identity follows the question being answered. Recipe, Revision, Proposal, Acceptance, Plan, Run, Step, Attempt, Cache, Output, SBOM, Attestation, Signature, Verification, Review, Reproduction and Release remain separately addressable and cannot be replaced by one backend job or one status.
