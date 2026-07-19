# WP07 Consolidated Safety Net

**Status:** CANDIDATE TEST PLAN  
**Package:** `ptah.build` / provenance supplements `0.1.0`

## Structural gates

- Parse every WP07 schema as JSON Schema 2020-12.
- Require unique absolute Ptah URNs and exact registered entity kinds.
- Resolve all URNs from local catalogs without network access.
- Reject unknown top-level fields except through `extensions`.
- Prove no raw secret-value field exists in Recipe, Plan, Run, Step, Cache, Output, SBOM, Attestation, Signature or proof records.

## Positive cases

1. One accepted Recipe Revision compiles to two compatible backend plans without changing Recipe identity.
2. Parallel Step Runs preserve exact dependencies and Activity/Operation/Attempt bindings.
3. Cache reuse passes only when producer, inputs, toolchain, environment, integrity, policy and volatility match.
4. Each output binds an exact producer Attempt, immutable Object and digest; Artifact promotion remains optional.
5. Mutable OCI tag movement does not change digest-bound Artifact identity.
6. SBOM binds exact subject, generator revision and bounded coverage limitations.
7. Attestation and signature verification bind exact policy/trust inputs and remain separate from creation.
8. An allowed offline bundle verifies without transparency-network access.
9. Build success with later export or signing failure retains outputs and partial state.
10. Independent reproduction uses distinct accepted conditions and produces byte-identical, functional-equivalence or divergence comparison.
11. Backend replacement preserves public Recipe, Object, Artifact and provenance identity.

## Negative cases

Reject:

- backend path/job/result identifiers as canonical Recipe or Run identity;
- execution without an immutable accepted Recipe Revision;
- hidden unsupported capability, proof or isolation requirements;
- retry reusing Attempt identity;
- cache reuse with mutable/unknown input, changed toolchain/policy or missing integrity evidence;
- hidden output-affecting volatile input;
- raw credentials in logs, caches, outputs, SBOMs, attestations or public bundles;
- output registration without exact producer Attempt and immutable digest;
- mutable tags as exact Artifact subjects;
- SBOM completeness inferred from document existence or package count;
- attestation PASS inferred from creation or signature existence;
- release acceptance inferred from signature validity;
- public transparency publication violating privacy policy;
- same-cache rerun claimed as independent reproduction;
- deletion of negative or inconclusive history to manufacture success.

## Executable-harness requirement

The implementation repository must load every Phase 0B catalog, validate positive and negative fixtures, assert semantic invariants, and produce a receipted report. Until that harness exists and passes, WP07 is candidate-contract complete only—not implementation-frozen.
