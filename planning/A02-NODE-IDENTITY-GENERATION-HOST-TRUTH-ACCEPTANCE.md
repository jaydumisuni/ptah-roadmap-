# A02 — Node identity, Generation and host truth acceptance

**Status:** ACCEPTED COMPLETE  
**Recorded:** 2026-08-16  
**Dependency:** A01 accepted complete at merge `d33122c8cc625d38f2394d57fcbd2a3ef7027b08`

## Decision

A02 is accepted complete. A03 — Ledger, schema versions and crash-safe migrations — is READY.

A02 proves the canonical Node identity, Generation/connection-epoch fencing, restart-seed, evidence-bound host-truth projections and bounded advisory layer defined by the accepted implementation roadmap. It does not claim A03 persistence, A04 Activity execution, Prime-native integration, production qualification or release acceptance.

## Exact implementation evidence

- implementation repository: `jaydumisuni/Ptah-space`;
- PR: `#24` — `A02: Node identity, Generation and host truth`;
- exact frozen candidate head: `80adcd0aefe0053b2354b26676bfc9e28d9b8ec3`;
- frozen source tree: `9b477dc1bf9ab2dd466da9615dbbd0e881216ed6`;
- merge commit: `1603ac80b5d2c5925fde62392ec0fff4b07a1219`;
- exact-head A02 workflow run: `31909732507`;
- all 13 workflows on the exact candidate head: PASS;
- A02 exact-head artifact: `9253318003`;
- A02 exact-head artifact digest: `sha256:dbafc252ab2fb3e2eb9938de6648bca0105f698d27321be9eb2bdb1a3782ba0a`;
- merge tree equals the frozen candidate tree: `9b477dc1bf9ab2dd466da9615dbbd0e881216ed6`;
- retained post-merge Phase 0C scaffold push gate on merge `1603ac80...`: PASS.

## Dependency and lifecycle evidence

The accepted external Cargo universe remains frozen at:

```text
81 registry packages
0 Git packages
```

The A02 implementation adds only authorized workspace/path dependency metadata. The A01 and Phase 0C lifecycle validators were corrected to preserve the stronger invariant — the accepted external package/version/source/checksum universe — without falsely requiring the whole workspace lockfile bytes to remain identical forever.

Internal path dependencies introduced by A02 are pinned to the workspace package version `=0.0.0-phase0c` while retaining their paths.

## Proved A02 obligations

- canonical lowercase UUIDv7 entity and Node identity;
- canonical identity validation at parsing and Serde boundaries;
- validated EntityKind and positive RecordRevision types;
- Node Generation and connection-epoch constraints;
- counter advancement fails on overflow instead of saturating silently;
- restart seeds reject revision zero;
- worker-slot observations require exact non-negative integer values;
- stale-generation commands fail closed and remain correlated to Event/Receipt evidence;
- process ID, hostname and boot identity cannot substitute for canonical Node identity;
- Node health, reachability, capability, resource and worker-capacity projections remain evidence-bound;
- bounded missing-capability/degradation advisory records cannot authorize, approve or execute their own upgrade;
- A03 ledger persistence and A04 Activity execution were not pulled forward.

## Independent physical execution proof

Because Kratos's local Rust `1.97.1` installation was corrupted and Oracle Live intentionally bounds terminal RPC duration, the physical proof did not weaken or change the candidate. Instead, GitHub Actions compiled checksum-bound static MUSL x86_64 A02 test executables from the exact frozen source using Rust `1.97.1`, then Kratos independently downloaded, verified and executed those exact bytes through Oracle Live.

Immutable payload provenance:

```text
Oracle payload commit: 8522f104474f404a73c74fadc3bcf9c3e81664b3
bundle SHA-256: 04fa242442f916391c5cbc130c3ff32a6b98cde0b1149d81aa0ce9a479875671
source commit: 80adcd0aefe0053b2354b26676bfc9e28d9b8ec3
source tree: 9b477dc1bf9ab2dd466da9615dbbd0e881216ed6
Cargo.lock SHA-256: 73bfc13e9e73a465c8271a3a26a2a688b3abf2c3734a016307aba94c4a8c5c32
```

Kratos execution receipt:

```text
receipt: 0000-ptah-a02-kratos-physical-proof-20260816-013450z
transport: oracle.live.v1
githubInteractivePathUsed: false
machine: x86_64
node: kratos-HP-290-G4-Microtower-PC
ptah-identifiers: 9 passed / 0 failed
ptah-node-agent: 17 passed / 0 failed
command exit code: 0
```

The environment-repair failures remain retained as negative evidence and are not presented as Ptah defects or as successful toolchain installation.

## Independent Sergeant review

Exact reviewer:

```text
Sergeant commit: 56961f12e5cc97cde447e5150e7a00ef3a8deba8
review evidence commit: a6f2a3d216e7e4061771d76f1dead3f5c838409a
mode: model-free
review depth: maximum
```

Final reconciliation:

```text
verdict: PASS
consensus: PASS
blocking: 0
needs_work: 0
repository review: PASS — No action required
```

Sergeant challenged the remaining advisory/minor capability signals and retained them as non-blocking review-attention evidence rather than demonstrated defects. Static invariant and contract reviews reported no blocking defect.

## Claim boundary

```text
P01D: ACCEPTED / COMPLETE
Runtime implementation: AUTHORIZED
A01: FROZEN / PROVEN / COMPLETE
A02: FROZEN / PROVEN / COMPLETE
A03: READY
A03 persistence/migrations: NOT YET PROVEN
A04 Activity execution: NOT YET PROVEN
P01P Prime-native integration: OPEN / DEFERRED
Prime-native deployment qualification: NOT CLAIMED
Production: NOT AUTHORIZED
Release: NOT ACCEPTED
```

## Next action

Begin A03 only from the accepted A02 merge and frozen WP01–WP06 contracts. Implement the `ptah-ledger` interfaces, SQLite WAL implementation, entity/schema version registry, immutable numbered directional migrations, transactional write/checkpoint policy and repository-owned query boundaries required by the accepted implementation roadmap.
