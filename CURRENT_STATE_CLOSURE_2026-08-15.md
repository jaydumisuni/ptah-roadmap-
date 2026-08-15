# Ptah P01D Closure — 2026-08-15

**Status:** OPERATIVE — P01D ACCEPTED — A01 AUTHORIZED  
**Scope:** Phase 0C P01D development-host qualification and transition into Programme A  
**Supersedes:** stale P01D/A01 status wording in `CURRENT_STATE_AMENDMENT_2026-08-15.md`, `CURRENT_STATE.md`, `AI_HANDOFF.md`, `IMPLEMENTATION_ROADMAP.md` and `master-plan-index.json`  
**Does not rewrite:** historical Ubuntu pinned-host evidence or claim that the superseded Ubuntu proof passed

## Decision

P01D is accepted on the selected physical Kratos development machine. Runtime implementation is explicitly **AUTHORIZED** and A01 is **READY**.

P01P remains **OPEN / DEFERRED**. It is the later Prime-native integration qualification and is not satisfied by this closure.

This closure does not qualify a Prime deployment, authorize production, accept a release, or collapse `Prime Host ID` into `Ptah Node ID`.

## Accepted evidence set

### Corrected merged public probe

- repository: `jaydumisuni/Ptah-space`;
- exact merged proof commit: `f6064c98c58e369f621b1800632a0169d8fb0785`;
- public report record type: `ptah.phase0c.development_host_probe`;
- public report schema: `0.3.1`;
- public report SHA-256: `598dbde9d5b3061ba9dfd29baf31ce2007718f0010db67ee96f2dc2b13e00083`;
- `portable_capabilities_passed: true`;
- capability failures: empty;
- observation failures: empty;
- repository-binding failures: empty;
- aggregate probe failures: empty;
- exact repository binding before/after: clean and unchanged;
- public repository root representation: `.`;
- absolute private checkout-path disclosure: absent.

The public report correctly keeps these fields false because the public probe cannot accept itself:

```text
physical_host_identity_verified: false
development_host_accepted: false
runtime_implementation_authorized: false
deployment_host_qualified: false
release_accepted: false
```

Those fields are claim-boundary protections inside the public report, not the final private acceptance state.

### Private physical execution binding

Oracle Live retained result:

- receipt ID: `0000-ptah-p01d-final-kratos-proof-20260815-194730z`;
- receipt blob SHA: `bf81cc24f7fce84d777da3c668b8716b475e8002`;
- target: `kratos-hp-290-g4-microtower-pc`;
- transport: `oracle.live.v1`;
- `githubInteractivePathUsed: false`;
- terminal exit code: `0`;
- exact Ptah-space commit: `f6064c98c58e369f621b1800632a0169d8fb0785`;
- report SHA-256 observed by the physical execution: `598dbde9d5b3061ba9dfd29baf31ce2007718f0010db67ee96f2dc2b13e00083`.

This private receipt supplies the physical-machine/control binding that the public report deliberately omits.

### Retained negative/correction evidence

The first mechanically passing Kratos report is retained but excluded from acceptance:

- report SHA-256: `cc1a91ac0e19bd3c108c4a85ccd2fa54fd688975398a90eb0da41c34e261a46d`;
- defect: public report disclosed the absolute local checkout path;
- correction: Ptah-space PR #22 redacted the local path and added regression/CI enforcement;
- corrected candidate exact head: `895d2cccb2d8208909da71f35213a9013a1ddc21`;
- corrected merge: `f6064c98c58e369f621b1800632a0169d8fb0785`.

The failed/defective first evidence remains part of the proof history and is not relabelled as accepted.

## Independent review

The corrected proof implementation received an independent Sergeant verdict:

```text
verdict: APPROVE
confidence: 0.88
required_actions: []
```

The final combined P01D evidence review included:

1. the corrected public report;
2. the Oracle Live physical-machine receipt;
3. the retained first-run negative/correction evidence;
4. the exact-head proof-tool assurance.

Sergeant's final review decision was:

```text
action: APPROVE
status: pass
confidence: 0.88
required_actions: []
```

The evidence-consensus diagnostic also emitted two non-blocking heuristics: an expected call-graph observation that exported probe symbols have test callers, and a nested-iteration scaling heuristic over fixed contract/failure-set lists. They are retained as review notes. They are not admitted P01D defects, required actions, capability failures, repository-binding failures, or physical-proof failures.

## P01D acceptance-condition closure

ADR-0038 conditions are closed as follows:

1. merged provider-neutral development-host probe — PASS;
2. clean exact checkout on Kratos — PASS;
3. Kratos-generated portable capability report — PASS;
4. public self-acceptance fields remain false — PASS;
5. retained private Oracle Live execution receipt — PASS;
6. exact clean repository binding before/after — PASS;
7. independent combined evidence review — PASS / APPROVE / no required actions;
8. this private closure explicitly accepts P01D and authorizes A01 while keeping P01P open — PASS when this reviewed closure change merges.

## Authorization state

```text
Phase 0C P01D: ACCEPTED / COMPLETE
Physical development host: ACCEPTED FOR PTAH DEVELOPMENT
ADR-0033 baseline: ACCEPTED AS AMENDED BY ADR-0038 AND ADR-0039
Runtime implementation: AUTHORIZED
A01: READY
P01P Prime-native integration proof: OPEN / DEFERRED
Prime deployment qualification: NOT CLAIMED
Production/release acceptance: NOT CLAIMED
```

## Exact next action

Begin **A01 — Repository, contracts and reproducible scaffold** under the accepted Master Plan/roadmap and frozen WP01–WP14 contracts.

A01 must still satisfy its own Build → Review → Freeze → Prove → Submit/Ship gates. P01D acceptance authorizes implementation; it does not pre-prove A01.

## Preserved architecture boundaries

- Ptah remains independent and OS-neutral.
- Prime remains machine/Host authority.
- `Prime Host ID != Ptah Node ID`.
- Oracle remains a private control/evidence provider, not a Ptah Core dependency.
- MCP/RPC remains the integration/control boundary.
- public Ptah source does not expose private machine/control topology.
- P01P remains a real later proof obligation.
- the superseded Ubuntu 24.04.4 / `6.8.0-136-generic` proof kit remains historical evidence and is **not** marked passed.
