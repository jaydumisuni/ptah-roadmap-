# ADR-0024A — WP07 Final Catalog and Conventions Correction

**Status:** ACCEPTED CORRECTION TO ADR-0024  
**Date:** 2026-07-19  
**Implementation authorization:** NONE

## Context

ADR-0024 accepted the WP07 Recipe, Build and Provenance architecture and selected `schemas/phase-0b/build/schema-catalog.v0.1.1.json` as the active candidate catalog.

A final consistency review preserved that architecture but found four machine-readable candidate defects and several missing precision cases:

1. Recipe Revision `0.1.0` embedded mutable execution-acceptance state inside an immutable revision;
2. Build Readiness `0.1.0` evaluated a candidate set without binding one exact Provider/Materialization/locality/generation context;
3. Build Run `0.1.0` did not require Backend Compatibility, current Dispatch Eligibility and connection epoch for every execution context;
4. Secret Access lifecycle `0.1.0` marked `expired` terminal while also allowing a later transition to `cleanup_failed`;
5. offline/no-log transparency evidence and produced-output identity required explicit schema/fixture precision.

No accepted WP07 architectural boundary changed.

## Decision

The authoritative WP07 candidate catalog remains:

- `schemas/phase-0b/build/schema-catalog.v0.1.1.json`.

The final active catalog contains 30 schemas and selects these corrected versions:

- `build.build-recipe-revision` `0.1.1`;
- `build.build-readiness` `0.1.1`;
- `build.build-run` `0.1.1`;
- `build.build-backend-compatibility` `0.1.0`;
- `build.build-output-record` `0.1.0`;
- `build.transparency-evidence` `0.1.0`;
- all other active catalog schemas at the versions listed in catalog `0.1.1`.

The final active lifecycle selection includes:

- `build.secret_access.lifecycle` `0.1.1`;
- the other eight WP07 lifecycle machines at `0.1.0`.

The catalog records these superseded candidate records explicitly:

- Recipe Revision `0.1.0`;
- Build Readiness `0.1.0`;
- Build Run `0.1.0`;
- Secret Access lifecycle `0.1.0`.

Earlier files remain candidate history and are not selected by downstream work.

## Conventions correction

The active normative convention set is:

- `contracts/phase-0b/build/BUILD-RECIPE-PROVENANCE-CONVENTIONS.md`;
- `contracts/phase-0b/build/BUILD-RECIPE-PROVENANCE-CONVENTIONS.v0.1.1.md`.

The `0.1.1` correction adds exact rules for:

- Backend Compatibility as a separate expiring decision;
- run-scoped Build Step versus WP02 Operation/Attempt;
- Build Output Record as the producer-to-Object bridge;
- SBOM identity/generation/coverage interpretation;
- separately addressable Transparency Evidence;
- truthful Node-local versus remote-service Build locality;
- migration and backend replacement.

It does not replace or reverse the original convention draft except where it explicitly adds precision.

## Entity-kind correction

The active entity-kind records are:

- `contracts/phase-0b/common/ENTITY-KIND-REGISTRY-WP07-SUPPLEMENT.md`;
- `contracts/phase-0b/common/ENTITY-KIND-REGISTRY-WP07-CORRECTION-0.1.1.md`.

The correction removes redundant draft kinds `build.step_run` and `provenance.sbom_revision`, while retaining `build.step`, immutable `provenance.sbom`, `provenance.sbom_coverage`, Backend Compatibility, Build Output Record and Transparency Evidence.

## Conformance correction

The active fixture set is:

- base corpus: `conformance/fixtures/phase-0b/wp07/build-provenance-cases.v0.1.0.json`;
- final correction corpus: `conformance/fixtures/phase-0b/wp07/build-provenance-cases.v0.1.1.json`.

Fixture `0.1.1` adds mandatory cases for:

- acceptance state prohibited inside immutable Recipe Revision;
- exact Node-local Build Readiness and Run evidence;
- remote Build execution without a fictional Node;
- mixed/stale locality and generation rejection;
- Build Output Record requiring produced bytes;
- Secret Access expiry only after verified cleanup;
- public transparency disclosure acknowledgement;
- valid offline/no-log verification without fabricated log evidence.

The consolidated safety net remains:

- `conformance/PHASE-0B-WP07-BUILD-PROVENANCE-SAFETY-NET.md`.

## Effect on ADR-0024 and WP07

Where ADR-0024 or the WP07 work package lists the active WP07 package, interpret it with this correction:

- catalog `0.1.1` is the authoritative machine-readable selection after commit-level review;
- the conventions `0.1.1` correction is normative;
- Recipe Revision, Readiness and Build Run `0.1.0`, plus Secret Access lifecycle `0.1.0`, are superseded candidate history;
- both fixture `0.1.0` and correction fixture `0.1.1` form the active specification corpus.

WP07 remains candidate-complete for downstream Phase 0B contract design.

No Build backend, cache, registry, SBOM generator, attestation/signing infrastructure, trust root, transparency service, reproduction runner or Build UI implementation is authorized.

## Do-not-break rule

> Final catalog selection must preserve immutable Recipe intent, exact execution context, truthful locality, produced-output identity, verified secret cleanup and honest transparency policy. Correcting machine-readable records does not authorize implementation or collapse any WP07 proof domain.
