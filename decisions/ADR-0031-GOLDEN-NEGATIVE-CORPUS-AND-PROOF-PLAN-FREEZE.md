# ADR-0031 — Golden/negative corpus and proof-plan freeze boundary

Status: accepted subject to exact-head conformance

## Decision

Ptah shall freeze implementation evidence through immutable Corpus Revisions and Proof Plan Revisions. Fixture bytes remain WP03 Content/Artifact records. Admission, expected proof and freeze authority are separate records.

A fixture is admissible only with exact digest, lawful source or permission, audience/privacy classification, target-contract scope and typed expected proof. Negative, failed and inconclusive fixtures are retained permanently under their declared retention policy.

The first vertical slice must satisfy the frozen backend-neutral Proof Plan. Phase 0C may choose implementations but may not remove required negative, recovery, offline or backend-replacement proofs.

## Consequences

- accidental green tests cannot silently redefine expected behavior;
- donor test assets require explicit licence review;
- CI summaries cannot replace immutable reports;
- implementation begins with a pre-agreed proof burden rather than architecture invention during coding.
