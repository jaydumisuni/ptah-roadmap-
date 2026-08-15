# ADR-0039 — P01D acceptance and A01 runtime authorization

**Status:** ACCEPTED ON MERGE  
**Recorded:** 2026-08-15  
**Depends on:** accepted ADR-0038 and the retained P01D evidence set  
**Amends:** proposed ADR-0033 host-acceptance condition and Phase 0C P01 closure status

## Context

ADR-0038 replaced the standalone exact-Ubuntu runtime-start prerequisite with two distinct obligations:

- P01D — physical development-host qualification on Kratos, which may authorize A01;
- P01P — later Prime-native integration qualification, which remains a deployment/integration gate.

P01D has now produced and independently reviewed the required evidence.

## Decision

Accept P01D and explicitly authorize A01 runtime implementation.

The first vertical-slice baseline recorded by ADR-0033 is accepted **as amended by ADR-0038**. The superseded exact-Ubuntu host requirement is not treated as passed and is not a remaining A01 prerequisite.

P01P remains open/deferred and must be completed before a Prime-native Ptah deployment is called qualified.

## Acceptance evidence

- Ptah-space merged proof commit: `f6064c98c58e369f621b1800632a0169d8fb0785`;
- corrected public report SHA-256: `598dbde9d5b3061ba9dfd29baf31ce2007718f0010db67ee96f2dc2b13e00083`;
- public probe result: all required portable capabilities PASS, all failure sets empty, exact clean repository binding before/after;
- Oracle Live physical receipt ID: `0000-ptah-p01d-final-kratos-proof-20260815-194730z`;
- Oracle Live receipt blob SHA: `bf81cc24f7fce84d777da3c668b8716b475e8002`;
- physical target: `kratos-hp-290-g4-microtower-pc`;
- control transport: `oracle.live.v1`;
- Git interactive fallback used: false;
- first-run negative report SHA-256: `cc1a91ac0e19bd3c108c4a85ccd2fa54fd688975398a90eb0da41c34e261a46d`;
- first-run defect: absolute local checkout path leaked into a public report;
- correction: Ptah-space PR #22, candidate `895d2cccb2d8208909da71f35213a9013a1ddc21`, merged as `f6064c98c58e369f621b1800632a0169d8fb0785`;
- independent Sergeant proof-implementation review: APPROVE, confidence `0.88`, required actions `[]`;
- independent combined P01D review: APPROVE / pass, confidence `0.88`, required actions `[]`.

Two Sergeant evidence-consensus heuristics are retained as non-blocking review notes: expected test callers of exported probe symbols and a nested-iteration scaling heuristic over fixed contract/failure-set lists. Neither produced a required action or admitted P01D defect.

## Authorization

```text
P01D: ACCEPTED / COMPLETE
ADR-0033 first-slice baseline: ACCEPTED AS AMENDED
Runtime implementation: AUTHORIZED
A01: READY
P01P: OPEN / DEFERRED
Prime-native deployment qualification: NOT CLAIMED
Production/release acceptance: NOT CLAIMED
```

## Non-effects

This decision does not:

- claim the historical Ubuntu 24.04.4 / `6.8.0-136-generic` proof passed;
- make the public probe self-authorizing;
- make Oracle a Ptah Core dependency;
- merge Ptah semantics into Prime Core;
- make `Prime Host ID` equal `Ptah Node ID`;
- satisfy P01P;
- pre-prove A01 implementation;
- authorize production or release acceptance.

## Consequences

A01 may now begin under the accepted roadmap, frozen WP01–WP14 contracts, exact dependency/licence/source boundaries and normal exact-head proof discipline.

Any A01 implementation change must still pass its own positive, negative, recovery and exact-head review gates before it can be frozen or proven.
