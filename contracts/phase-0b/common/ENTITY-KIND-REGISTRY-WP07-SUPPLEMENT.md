# Ptah Phase 0B — Entity Kind Registry WP07 Supplement

**Registry:** `ptah.entity-kind`  
**Candidate version:** `0.1.0`  
**Status:** CANDIDATE  
**Date:** 2026-07-19

This supplement extends the common registry for WP07 without modifying previously published registry history.

| Token | Meaning |
|---|---|
| `build.recipe_revision` | Immutable accepted or proposed Build Recipe revision |
| `build.recipe_proposal` | Detector/importer/caller proposal for a Recipe Revision |
| `build.recipe_acceptance` | Authorized acceptance/rejection decision over one exact Recipe Revision |
| `build.readiness` | Time-bounded readiness assessment over Recipe, Workspace and execution evidence |
| `build.step` | Stable Recipe-level step identity within one Build Run |
| `build.output_declaration` | Expected output role/type/platform/privacy/proof declaration |
| `build.cache_use` | One immutable cache-reuse eligibility and acceptance decision |
| `build.secret_access` | Scoped secret/credential access and cleanup evidence |
| `provenance.sbom_coverage` | Coverage, skipped, unsupported and error record for one SBOM generation |
| `provenance.attestation_verification` | Verification decision over one exact attestation statement |
| `provenance.signature_verification` | Verification decision over one exact signature and trust policy |
| `provenance.trust_policy` | Versioned trust-root, identity, certificate, transparency and offline verification policy |
| `provenance.proof_bundle` | Immutable manifest collecting distinct proof-domain records without collapsing them |
| `provenance.reproduction_request` | Requested independent or repeated Build reproduction under a frozen Protocol |

Rules:

1. Existing `build.recipe`, `build.compiled_plan`, `build.run`, `build.cache_record`, `provenance.sbom`, `provenance.package_observation`, `provenance.attestation`, `provenance.signature`, `provenance.verification_run`, `proof.reproduction_run`, `proof.comparison` and `provenance.graph_revision` remain canonical registered kinds.
2. Proposal, acceptance, readiness, execution and verification remain separate entities.
3. Backend-local plan, step, cache, signature, attestation and registry identifiers remain scoped Aliases.
4. Registration does not authorize implementation or public visibility.
