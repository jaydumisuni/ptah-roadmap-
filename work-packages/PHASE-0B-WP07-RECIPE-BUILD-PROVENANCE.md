# Phase 0B WP07 — Recipe, Build, Provenance, SBOM, Signature and Verification

**Status:** CANDIDATE PACKAGE — REVIEW REQUIRED  
**Date:** 2026-07-19  
**Implementation authorization:** NONE

## Objective

Convert the frozen Phase 0A Build/Artifact/Provenance boundary and WP01–WP06 contracts into backend-neutral candidate contracts without selecting BuildKit, Dagger, ORAS, Syft, Witness, in-toto, Sigstore or a native build backend.

## Proposed accepted boundary

1. Recipe, immutable Recipe Revision, Proposal, Acceptance, Readiness, Compatibility and Compiled Plan remain separate.
2. Backend plans and job identifiers are implementation evidence, never canonical Recipe identity.
3. Build Run and Step Run map to exact WP02 Operations and Attempts.
4. Cache Record and Cache Use Decision remain separate; a cache hit is not newly executed-work proof.
5. Volatile output-affecting inputs lower reproducibility trust and cannot be hidden.
6. Secret references, grants, delivery and cleanup evidence are recorded without raw values.
7. Output declaration, Object creation, Artifact promotion, Location and Release remain separate.
8. SBOM document/revision, package observations and bounded coverage remain separate.
9. Attestation creation, verification, signature, transparency and release acceptance remain separate.
10. Online, private and offline verification are policy-controlled and privacy-aware.
11. Independent reproduction requires declared separation and a separate Comparison.
12. Build success may coexist honestly with export, proof, signing, review or reproduction failure.
13. Backend replacement preserves stable identity and creates new plans, runs, attempts and evidence.

## Candidate outputs

- normative Build/provenance conventions and entity-kind supplement;
- candidate schemas and local catalogs;
- namespaced lifecycle machines plus cross-machine invariants;
- migration/compatibility record;
- positive/negative fixtures and consolidated safety net;
- ADR-0024 candidate.

## Review gates

- every URN resolves locally and every entity kind is collision-free;
- schemas and lifecycle definitions pass structural validation;
- positive and negative fixtures pass the consolidated harness;
- no raw-secret field or donor-specific public dependency exists;
- partial-state, privacy and independent-reproduction semantics survive adversarial review;
- ADR-0024 is accepted before WP07 is marked candidate-complete.

Executable conformance, dependency selection and runtime implementation remain deferred.
