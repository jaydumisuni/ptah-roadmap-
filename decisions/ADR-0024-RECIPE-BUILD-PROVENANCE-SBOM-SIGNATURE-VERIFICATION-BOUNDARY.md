# ADR-0024 — Recipe, Build, Provenance, SBOM, Signature and Verification Boundary

**Status:** PROPOSED  
**Date:** 2026-07-19

## Context

Ptah must support multiple interchangeable build backends, deterministic and non-deterministic work, cache reuse, immutable outputs, supply-chain evidence, private/offline verification and independent reproduction. Donor systems expose useful mechanics but use incompatible identities and often collapse build success, cache hits, attestations, signatures and release trust.

## Decision

Adopt the WP07 candidate boundary:

- stable Build Recipe plus immutable Recipe Revision;
- separate Proposal, Acceptance, Readiness, Backend Compatibility and Compiled Plan;
- Build Run/Step Run projections linked to exact WP02 Operations and Attempts;
- separate Cache Record and Cache Use Decision;
- explicit volatile-input and secret-access/cleanup evidence;
- outputs registered through immutable WP03 Objects before Artifact promotion or release;
- separate SBOM revision and bounded coverage;
- separate attestation creation, attestation verification, signature, signature verification and transparency evidence;
- policy-controlled online, private and offline verification;
- immutable proof bundles that collect but do not collapse proof domains;
- separate independent Reproduction Request/Run and Comparison;
- honest partial state when build, export, proof, signing, review or release outcomes diverge.

## Consequences

Ptah gains backend portability, exact evidence boundaries and truthful failure reporting. Adapters require explicit mappings and cannot treat a backend job, cache hit, signed blob or generated SBOM as sufficient proof. More records exist, but each claim remains independently reviewable and migratable.

## Rejected alternatives

1. Canonicalize BuildKit, Dagger or CI workflow identity — backend coupling.
2. Treat cache hit as successful execution proof — reused output is not newly executed work.
3. Treat signature validity as correctness or release acceptance — signatures prove bounded identity/digest claims only.
4. Require public transparency for every verification — incompatible with private/offline policy.
5. Collapse reproduction into another Build Run — independence and comparison evidence would disappear.

## Constraint

Acceptance authorizes contract use only. It does not select dependencies or authorize runtime implementation.
