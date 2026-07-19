# Ptah Phase 0B — WP07 Entity Kind Registry Correction 0.1.1

**Status:** CANDIDATE CORRECTION  
**Date:** 2026-07-19  
**Supersedes:** only the conflicting active-kind interpretations in `ENTITY-KIND-REGISTRY-WP07-SUPPLEMENT.md` 0.1.0

## Purpose

Remove two overlapping draft identities and register the exact records added during WP07 consistency review without mutating the earlier candidate history.

## Corrected active kinds

| Token | Meaning |
|---|---|
| `build.recipe_revision` | Immutable Build Recipe revision |
| `build.recipe_proposal` | Proposal for one exact Recipe Revision |
| `build.recipe_acceptance` | Authorized decision over one exact Recipe Revision/proposal |
| `build.readiness` | Expiring readiness assessment over exact execution context |
| `build.backend_compatibility` | Directional backend/target compatibility decision |
| `build.step` | One run-scoped Step record mapping a Recipe `step_key` to Operations/Attempts |
| `build.output_declaration` | Expected output contract in a Recipe Revision |
| `build.output_record` | Exact producer-Attempt-to-produced-bytes/Object binding |
| `build.cache_use` | Cache-reuse decision for one consumer Step/Run |
| `build.secret_access` | Scoped credential access and cleanup evidence |
| `provenance.sbom_coverage` | SBOM scope/coverage/skips/errors record |
| `provenance.attestation_verification` | Verification of one attestation under exact policy |
| `provenance.signature_verification` | Verification of one signature under exact trust policy |
| `provenance.trust_policy` | Versioned trust and verification policy |
| `provenance.transparency_evidence` | Public/private/timestamp/offline transparency evidence |
| `provenance.proof_bundle` | Manifest of distinct proof-domain records |
| `provenance.reproduction_request` | Request for repeated/independent reproduction |

Existing canonical kinds remain active:

- `build.recipe`;
- `build.compiled_plan`;
- `build.run`;
- `build.cache_record`;
- `provenance.sbom`;
- `provenance.package_observation`;
- `provenance.attestation`;
- `provenance.signature`;
- `provenance.verification_run`;
- `provenance.graph_revision`;
- `proof.reproduction_run`;
- `proof.comparison`.

## Removed from the active WP07 vocabulary

### `build.step_run`

Removed as redundant for WP07 candidate contracts.

- Recipe Revision step definitions are embedded immutable definitions identified by `step_key`.
- `build.step` is already the separately addressable run-scoped projection linked to one Build Run, Operations and Attempts.
- A future reusable logical Step entity would require a separate ADR/schema rather than reusing this ambiguous token.

### `provenance.sbom_revision`

Removed as redundant for WP07 candidate contracts.

- `provenance.sbom` is already one immutable versioned SBOM document over one exact subject/generator/configuration.
- Re-generation creates a new `provenance.sbom` entity and related coverage/document Artifacts.
- A future stable logical SBOM family identity may be added separately if measured need requires it.

## Added during consistency review

- `build.backend_compatibility`;
- `build.output_record`;
- `provenance.transparency_evidence`.

## Do-not-break rule

> A Recipe step definition, run-scoped Build Step and WP02 Operation/Attempt remain different layers. An immutable SBOM document and its Coverage remain separately addressable without inventing a duplicate SBOM Revision identity.
