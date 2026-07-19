# Ptah Phase 0B — Entity Kind Registry WP07 Supplement

**Registry:** `ptah.entity-kind`  
**Candidate version:** `0.1.0`  
**Status:** CANDIDATE  
**Date:** 2026-07-19

This supplement extends the common registry for WP07 without modifying previously published registry history. Registration does not authorize implementation or public visibility.

## New WP07 kinds

| Token | Meaning |
|---|---|
| `build.recipe_revision` | Immutable configured/executable revision of one stable Build Recipe |
| `build.recipe_proposal` | Detector/importer/caller proposal for a Recipe Revision, with evidence and limitations |
| `build.recipe_acceptance` | Authorized acceptance/rejection/correction decision over one exact Recipe Proposal or Revision |
| `build.readiness` | Time-bounded readiness assessment over Recipe, Workspace and candidate execution evidence |
| `build.backend_compatibility` | Directional, target-specific compatibility decision between one Recipe Revision and backend/provider revision |
| `build.step` | Stable Recipe-level step identity within one Build Run |
| `build.step_run` | One execution projection of a Build Step linked to exact WP02 Operations and Attempts |
| `build.output_declaration` | Expected output role/type/platform/privacy/proof declaration |
| `build.output_record` | Exact producer-to-output binding for one Attempt and produced Object/Artifact/Location set |
| `build.cache_use` | Immutable decision accepting or rejecting one Cache Record for one requested Step/Operation |
| `build.secret_access` | Scoped secret/credential delivery, use, revocation and cleanup evidence |
| `provenance.sbom_revision` | Immutable SBOM generation/revision over one exact subject and generator configuration |
| `provenance.sbom_coverage` | Coverage, skipped, unsupported and error record for one SBOM generation |
| `provenance.attestation_verification` | Policy/trust verification decision over one exact attestation statement |
| `provenance.signature_verification` | Verification decision over one exact subject, signature and trust policy |
| `provenance.trust_policy` | Versioned trust-root, identity, certificate, transparency and offline-verification policy |
| `provenance.transparency_evidence` | Immutable transparency/timestamp inclusion and log-integrity evidence |
| `provenance.proof_bundle` | Immutable manifest collecting distinct proof-domain records without collapsing them |
| `provenance.reproduction_request` | Requested independent or repeated Build reproduction under a frozen Protocol |

## Existing kinds used directly

The following existing registry kinds remain canonical and unchanged:

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
- `proof.comparison`;
- `proof.protocol`;
- `proof.review`;
- `proof.verdict`;
- `identity.approval`;
- `identity.credential_reference`;
- WP02 Activity/Operation/Attempt/Receipt kinds;
- WP03 Object/Artifact/Release/Location kinds;
- WP04 Facility/Provider revision/instance kinds.

## Rules

1. A path, Dockerfile, CI workflow, Dagger function/result ID, BuildKit LLB digest or backend job ID is not canonical `build.recipe` or `build.run` identity.
2. Every executed configuration uses one immutable `build.recipe_revision`.
3. Proposal, acceptance, readiness, backend compatibility, compilation, execution and verification remain separate entities.
4. `build.step` is Recipe/Run-level identity; `build.step_run` projects execution; WP02 Operation and Attempt remain canonical logical/physical work identities.
5. `build.output_record` links producer evidence to outputs but never replaces WP03 Object, Artifact or Release identity.
6. Cache backend keys, plan IDs, registry tags, scanner package IDs, signature bundle IDs and transparency-log IDs remain scoped Aliases/evidence.
7. SBOM identity, SBOM generation revision and SBOM coverage remain separate where independently referenced.
8. Attestation creation, attestation verification, signature creation and signature verification remain separate.
9. Transparency evidence does not become signature, Artifact, Activity or release identity.
10. Independent reproduction remains `proof.reproduction_run`; comparison remains `proof.comparison`.
11. Release acceptance uses exact Approval/Review/Verdict records rather than Build lifecycle.
12. Every proof/result binds exact subjects, digests, revisions, Activities, Attempts, Provider generations and applicable policy/trust revisions.

## Conformance requirements

- reject backend/path/job identifiers used as canonical Recipe or Run identity;
- reject execution without an immutable accepted Recipe Revision;
- reject proposal promoted without authority evidence;
- reject backend compatibility that silently weakens required capability, proof, isolation or output semantics;
- reject retry that reuses Attempt identity;
- reject Cache Use without producer/input/toolchain/environment/integrity comparison;
- reject hidden volatile output-affecting inputs;
- reject raw credentials in ordinary entities, logs, SBOMs, attestations or public exports;
- reject output record lacking exact producer Attempt and immutable Object digest;
- reject mutable tag as exact Artifact subject;
- reject SBOM completeness inferred without bounded coverage evidence;
- reject attestation PASS inferred from creation/signature alone;
- reject release acceptance inferred from a valid signature;
- reject public transparency identity disclosure without explicit privacy policy;
- reject same-cache rerun claimed as independent reproduction;
- preserve partial outputs and negative/inconclusive proof history.

## Do-not-break rule

> Recipe, Revision, Proposal, Acceptance, Readiness, Compatibility, Plan, Run, Step, Attempt, Cache, Output, SBOM, Attestation, Signature, Verification, Review, Reproduction and Release remain separately addressable. No backend job or generic status may replace them.
