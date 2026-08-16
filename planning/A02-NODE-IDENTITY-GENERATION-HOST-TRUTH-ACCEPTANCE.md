# A02 — Node identity, Generation and host truth acceptance

**Status:** ACCEPTED COMPLETE  
**Recorded:** 2026-08-16  
**Dependencies:** A01 accepted complete; runtime implementation authorized

## Decision

A02 is accepted complete. A03 — Ledger, schema versions and crash-safe migrations — is READY.

A02 proves the Node identity/Generation/host-truth runtime slice only. It does not claim ledger persistence or migrations, Activity execution, Prime-native integration, production authorization, or release acceptance.

## Exact implementation evidence

- repository: `jaydumisuni/Ptah-space`;
- PR: `#24` — `A02: Node identity, Generation and host truth`;
- exact candidate head: `80adcd0aefe0053b2354b26676bfc9e28d9b8ec3`;
- merge: `1603ac80b5d2c5925fde62392ec0fff4b07a1219`;
- A02 exact-head workflow run: `31909732507`;
- all 13 repository workflows on the exact candidate head: PASS;
- retained A02 proof artifact: `9253318003`;
- retained A02 proof digest: `sha256:dbafc252ab2fb3e2eb9938de6648bca0105f698d27321be9eb2bdb1a3782ba0a`;
- external Cargo universe: 81 registry packages / 0 Git packages.

## Physical Kratos proof

The exact frozen A02 source was physically proven on Kratos through the existing private Oracle Live MCP/RPC evidence path (`oracle.live.v1`). The physical proof used checksum-bound static executables built from the exact frozen source and passed:

- `ptah-identifiers`: 9/9 tests;
- `ptah-node-agent`: 17/17 tests.

This physical proof is evidence for A02 behavior only. Oracle/MCP/RPC remains private control/evidence infrastructure and is not a Ptah Core dependency.

## Independent review

Independent Sergeant review at exact review commit `56961f12e5cc97cde447e5150e7a00ef3a8deba8` ran model-free at maximum depth and returned:

- status: PASS;
- blocking findings: 0;
- needs-work findings: 0.

## Proved A02 obligations

- canonical Ptah entity and Node identity uses validated lowercase UUIDv7 and is not substituted by host/process/boot aliases;
- entity kind and positive record revision boundaries are validated;
- Node Generation and connection epoch counters are bounded and overflow fails closed;
- restart seed semantics preserve Node identity without pulling A03 persistence forward;
- stale-generation commands fail closed and remain correlated to Event/Receipt evidence;
- Node observation, health, readiness, reachability, capability and resource projections are evidence-bound;
- worker-capacity baseline is tied to exact Node/Provider/resource evidence;
- missing-capability/degradation advisory output is bounded and cannot authorize, approve or execute its own upgrade;
- A01/Phase 0C dependency and contract boundaries remain intact;
- exact-head formatting, Clippy, runtime tests and all repository workflows passed;
- physical Kratos proof and independent Sergeant review passed against the frozen candidate.

## Claim boundary

```text
A01 scaffold: FROZEN / PROVEN / COMPLETE
A02 Node identity/Generation/host truth: FROZEN / PROVEN / COMPLETE
A03 ledger/schema/migrations: READY
A03 persistence implemented: NO
A04 Activity execution: NOT IMPLEMENTED
Prime-native integration: NOT QUALIFIED
P01P: OPEN / DEFERRED
Production: NOT AUTHORIZED
Release: NOT ACCEPTED
```

## Next action

Begin A03 from P0C-I003 and frozen WP01–WP06 contracts. Implement only the repository-owned `ptah-ledger` interfaces, SQLite WAL storage, schema/entity version registry, immutable numbered directional migrations, transactional write/checkpoint policy and repository-owned query boundaries. Prove restart durability, rollback under interrupted writes, deterministic migration replay, incompatible-version fail-closed behavior and canonical-identity isolation from backend row IDs before accepting A03.
