# Phase 0B WP07 — Recipe, Build and Provenance Migration Compatibility

**Status:** CANDIDATE  
**Contract catalogs:** common 0.1.0, activity 0.1.1, object 0.1.0, runtime 0.1.2, workspace 0.1.0, transfer 0.1.0, build 0.1.0  
**Date:** 2026-07-19

## Purpose

Define how legacy project detectors, build scripts, CI workflows, Dockerfiles, Dagger modules, BuildKit records, native build logs, package outputs, SBOMs, attestations, signatures and reproduction evidence enter Ptah without fabricating Recipe acceptance, exact materials, Build completion, output identity, inventory completeness, trust, reproducibility or release approval.

## Non-negotiable preservation rules

1. Recipe, immutable Recipe Revision, Proposal, Acceptance, Readiness, Compiled Plan and Build Run remain separate.
2. backend, CI, graph, job, step, cache, image-tag, registry and signing-tool IDs remain Aliases.
3. Build Run, Build Step, Activity, Operation and Attempt remain distinct.
4. mutable source/package/image aliases resolve to exact revisions/digests or remain explicitly unresolved.
5. cache presence/hit does not become executed work or independent reproduction.
6. credentials remain opaque references; raw values are never imported into canonical records.
7. produced files become Content/Object Revisions before Artifact promotion or release.
8. output existence does not imply export, SBOM, attestation, signature, verification, review or acceptance.
9. SBOM is a bounded inventory claim with coverage/errors.
10. attestation creation, signature creation, policy verification and caller acceptance remain separate.
11. cryptographic validity never becomes functional correctness.
12. historical negative, partial, stale, contradictory and failed evidence remains immutable.

## Legacy Recipe and project detection

A Dockerfile, package manifest, CI file, build script, internal Builder configuration or Dagger module may become a source Object and may produce a `build.recipe_proposal`.

It becomes an accepted `build.recipe_revision` only when:

- exact source/Object Revision is retained;
- requested targets, materials, steps, dependencies, outputs and proof requirements are represented;
- unsupported/implicit behavior is explicit;
- an authorized acceptance record exists.

A legacy `detected`, `configured`, `ready` or `supported` flag becomes proposal/readiness evidence only. It never becomes an accepted or completed Recipe.

## Legacy Build/CI run import

A legacy CI/build job may produce:

- one `build.run` for the caller-visible Build;
- one or more `build.step` records;
- WP02 Activities, Operations and Attempts where correlation exists;
- backend aliases for CI job IDs, BuildKit solve IDs or native process IDs;
- produced Object Revisions and Locations;
- stage-specific proof/report records.

Legacy global statuses split into:

- Build Run lifecycle;
- Step/Operation/Attempt state;
- output registration/export state;
- SBOM/attestation/signature production;
- verification/review/reproduction/acceptance.

A legacy `success` maps only to the scope actually proved. When the job built bytes but later packaging/signing failed, preserve Build completion and separate downstream failures.

## Input/material migration

Mutable branches, tags, package ranges, URLs and filesystem paths are imported as Aliases plus exact resolved revisions where evidence exists.

When exact bytes/revisions cannot be recovered:

- retain the alias and observation time;
- classify the material as mutable, external, volatile or unresolved;
- lower reproducibility confidence;
- do not invent a digest or immutable revision.

## Plan/backend migration

BuildKit LLB, Dagger call graphs, CI DAGs and native backend plans become `build.compiled_plan` only when linked to one exact Recipe Revision and compiler/adapter/backend revision.

Unsupported or altered semantics remain requirement results. A backend plan may not replace Recipe identity.

## Cache migration

Legacy cache keys/layers/artifacts become `build.cache_record` only when producer Recipe/Plan/Run/Step/Operation/Attempt, exact inputs/toolchain/environment and output digest can be correlated.

Unknown producer or input identity makes cache reference-only, stale or quarantined. A cache hit record becomes a `build.cache_use` decision with comparison evidence; it cannot create an executed Attempt or independent reproduction claim.

## Credential migration

Legacy environment variables, secret files, CI secret names and key aliases map to credential references only.

Raw values found in logs/configuration are handled as restricted security evidence and trigger redaction/revocation workflows; they are not copied into Recipe, Plan, SBOM, attestation or fixtures.

Unknown cleanup/leak state becomes a limitation or `cleanup_failed`, never assumed safe.

## Output and Artifact migration

Legacy build outputs are imported by hashing/retaining exact bytes as Content/Object Revisions and recording source Build evidence.

File names, paths, download URLs, registry tags and package coordinates remain Aliases/Locations.

Legacy release packages become Artifact Releases only with exact allowlisted Object Revisions, audience/privacy/retention and release authority. Output existence or upload does not imply promotion/release.

## SBOM migration

Legacy SBOMs remain immutable source Artifacts. Import retains:

- exact subject digest/revision;
- generator/version/configuration;
- format/version;
- package/file observations and locations;
- coverage, skipped, unsupported and error evidence;
- derived format conversions;
- signatures/attestations/verifications.

When subject or generator identity is unknown, retain the document with limitations and do not claim complete/current inventory.

## Attestation migration

Legacy in-toto, DSSE, SLSA, Witness or custom statements become `provenance.attestation` records only when statement bytes, subject, predicate, materials/products and producer identity are retained.

Declared and observed materials/products remain distinguishable. A signed statement still requires separate signature and attestation-policy verification.

## Signature/trust migration

Legacy signatures become `provenance.signature` with exact subject digest, signature bytes, method, signer/key/certificate/issuer/transparency or offline references.

A historical `verified` flag becomes a new `signature_verification` only when verifier, trust roots/policy, identity/time/revocation/transparency evidence and exact result can be recovered. Otherwise retain it as bounded legacy evidence.

Changing trust roots or policy creates new verification records and never rewrites earlier decisions.

## Reproduction migration

Legacy `reproducible`, `deterministic` or `same output` claims are imported only with original/reproduction runs, environment/independence evidence, cache policy, outputs and comparison protocol.

Classify separately:

- byte-identical;
- functionally equivalent under protocol;
- accepted variance;
- different/not equivalent;
- inconclusive/blocked.

A same-backend cache hit or repeated CI job is not independent reproduction unless the accepted protocol explicitly supports and proves the required independence.

## Backend replacement

Replacing Build, export, SBOM, attestation or signing machinery:

1. preserves Recipe/Object/Artifact/proof identities;
2. creates new Facility/Provider/adapter revisions;
3. compiles a new Plan rather than mutating the old one;
4. creates new Runs/Attempts/Receipts;
5. re-evaluates cache eligibility;
6. retains old outputs/reports/signatures/verifications;
7. performs explicit compatibility/conformance comparison;
8. does not claim semantic equivalence without proof.

## Breaking changes

Require versioned migration when changing:

- Recipe identity/revision/hash/step graph semantics;
- material resolution and volatility classification;
- Plan compilation/mapping semantics;
- Build/Step lifecycle and transition authority;
- cache identity/reuse/validation rules;
- credential access/cleanup classifications;
- output/Artifact promotion relationships;
- SBOM coverage or package-observation semantics;
- attestation predicate/material/product meanings;
- signature/trust/transparency/offline verification semantics;
- reproduction independence/comparison classes.

## Negative migration cases

Reject or require manual review when migration attempts to:

- use a Dockerfile/CI job/backend ID as canonical Recipe identity;
- accept a detected Recipe without authority;
- claim readiness from a stale tool check;
- collapse all retries/jobs into one Attempt;
- use mutable branch/tag/package range/image tag as immutable material or Artifact identity;
- promote cache hit to execution or independent reproduction;
- import raw secrets into canonical records;
- promote output presence to Artifact Release;
- claim SBOM complete with unknown/skipped scope;
- claim signed attestation verified without trust-policy evidence;
- claim valid signature means functionally correct or release accepted;
- overwrite negative verification after trust-policy change;
- discard partial outputs after downstream proof failure;
- call same-backend cached output independent reproduction.

WP13/WP14 must execute legacy-to-candidate fixtures, round trips, backend replacement and negative cases. Structural validation alone is insufficient.
