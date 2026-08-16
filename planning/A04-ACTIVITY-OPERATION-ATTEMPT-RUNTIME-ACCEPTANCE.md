# A04 — Activity, Operation, Attempt, Event and Receipt runtime acceptance

**Status:** ACCEPTED COMPLETE
**Recorded:** 2026-08-16
**Roadmap item:** A04 / P0C-I004

## Accepted implementation

A04 is frozen, independently reviewed, physically proven through the accepted Oracle MCP/RPC path, and merged into `jaydumisuni/Ptah-space`.

```text
Ptah-space PR: #26
candidate exact head: fad9029504258c773f5ab496c79cfceea17c0b5e
merge: a63eb8f2c73f961b8466b844c6f194f2381a8139
freeze manifest SHA-256: 6d69f74a209e95ab7faa9ab7a543b247dfc00d170e9d0af5be0f573d4eb5aa1f
Pass B proof manifest SHA-256: db3f3561b85de30c001ac405261d2507128cfd2a87687f955ac6a862f9ebfda1
SQLite supplement SHA-256: bd65b89e5cc1180b96612b18901c530892d5b753123c5b1ea237a0bd8a1fb734
Tenfold final-review packet SHA-256: 8f471eee95374fcad509aff88b80be08b95eae22dd719934978feac70ddb53d4
Tenfold private lanes: 190
transport: oracle.live.v1
githubInteractivePathUsed: false
Rust/Cargo toolchain: 1.97.1
SQLite static archive SHA-256: c1978ab409aa5195e1819e4fe9d3fc8634de3fc9a5a6fc2bfdde69acaa8fab10
```

GitHub Actions are **not** the A04 runtime execution or proof authority. A04 proof was executed on the accepted development host through Oracle Live MCP/RPC. GitHub carries source/review/merge history only.

## What A04 proves

A04 establishes the first durable orchestration runtime over the accepted A02 identity/Generation and A03 ledger substrate:

- Activity, Operation and Attempt remain separate canonical identities and lifecycle machines;
- bounded concurrent Activity admission does not collapse unrelated work;
- retry preserves logical Operation identity while creating a fresh physical Attempt identity and correlation nonce;
- idempotency and compensating-operation requirements fail closed;
- cancellation stays scoped and terminal work remains queryable;
- Event sequencing/replay is observable state, not execution proof;
- immutable Receipts bind proof to exact Activity/Operation/Attempt context, generations, authority class, proof claims, limitations and correction ancestry;
- Attempt completion or provider acknowledgement cannot silently become Operation or Activity success;
- caller-defined worker formations preserve primary/verifier independence, checkpoints, partial results and conflicts;
- repeated-failure correlation may advise but cannot self-authorize new work;
- Receipt visibility follows durable A03 journal persistence rather than preceding it.

## Review and proof

Final pre-freeze Review on exact candidate `fad9029504258c773f5ab496c79cfceea17c0b5e`:

- exact 10-file A04 diff against accepted A03 merge;
- no A04 GitHub Actions proof workflow changes;
- clean tree and `git diff --check`;
- Sergeant APPROVE / PASS;
- 10 permanent officers;
- 190 planned Tenfold private lanes;
- 0 admitted findings;
- 0 unresolved assurances.

Fresh detached Pass B on Kratos proved the frozen source hashes before execution, then passed:

- `cargo fmt --all -- --check`;
- scoped locked Clippy with `-D warnings`;
- A04 Runtime/Event/Receipt package tests;
- complete Ptah workspace regression;
- independent Sergeant Pass B;
- SHA-bound direct execution of generated A04 integration-test executables.

The A04 Runtime unit-test executables were additionally SHA-bound and directly executed. Their symbol tables contain statically linked SQLite execution symbols including `sqlite3_initialize`, `sqlite3_open_v2` and `sqlite3_prepare_v2`, binding the A03-backed journal tests to the retained SQLite implementation archive.

## Preserved boundaries

A04 does **not** claim:

- A05 native process, PTY or multi-terminal Provider implementation;
- A06 persistent Workspace/Session implementation;
- Prime-native integration qualification;
- production authorization;
- release acceptance;
- that Event delivery, acknowledgement, worker completion or Attempt completion alone proves accepted result success.

P01P remains **OPEN / DEFERRED** and does not block Programme A development.

## Authority decision

A04 is **FROZEN / PROVEN / COMPLETE**.

A05 — Native process, PTY and multi-terminal Provider — is **READY**.

## Next action

Begin A05 from P0C-I005 and frozen WP02, WP04, WP05, WP09 and WP11 contracts. Preserve A04 as the orchestration/proof substrate; do not widen A05 into A06 Workspace persistence, Object work, Prime-native integration, production or release claims.
