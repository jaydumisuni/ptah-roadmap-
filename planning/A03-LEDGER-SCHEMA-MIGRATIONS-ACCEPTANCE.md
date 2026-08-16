# A03 — Ledger, schema versions and crash-safe migrations acceptance

**Status:** ACCEPTED COMPLETE  
**Recorded:** 2026-08-16  
**Roadmap item:** A03 / P0C-I003  
**Dependencies:** A01 and A02 accepted complete

## Accepted implementation

A03 is frozen, physically proven on the accepted Kratos development host, independently reviewed, and merged into `jaydumisuni/Ptah-space`.

Exact implementation evidence:

```text
Ptah-space PR: #25
candidate: 19d390e22807a8540c7c4c5c3a94a37b93f5e3be
merge: da35986327010cba575093d905875ee966e3d755
Oracle Pass B receipt: 0000-ptah-a03-pass-b-physical-proof-20260816-1528z
Oracle receipt blob: dd78ee595abfec5a96250f060505df8e5d19765b
transport: oracle.live.v1
githubInteractivePathUsed: false
Pass B proof manifest SHA-256: 26d684fb63e36b159e5a83c373bcd3a02dee04e893e00e282ae60b1cf400f861
Sergeant final net review packet SHA-256: 520f82f371e3a0b39183044ead54331542d82ea85c27ee2226496e23a8256ad5
```

The accepted runtime slice provides repository-owned `ptah-ledger` interfaces, SQLite WAL storage, the frozen schema registry, immutable numbered directional migrations, transactional writes and explicit checkpointing, canonical-identity-safe repository queries, revision/generation fencing, and crash-safe reopen/recovery behavior.

## Physical proof

Pass B used a fresh detached checkout of the exact frozen candidate and the pinned Rust `1.97.1` toolchain. It proved:

- pinned rustfmt: PASS;
- scoped `ptah-ledger` Clippy with `-D warnings`: PASS;
- `ptah-ledger` unit tests: 19/19 PASS;
- abrupt crash/recovery integration tests: 4/4 PASS;
- complete workspace test suite: PASS;
- exact checksum-bound `ptah_ledger` and `crash_recovery` test executables: direct execution PASS;
- both exact binaries dynamically bind to the recorded native `libsqlite3.so.0`;
- frozen source remained clean and unchanged throughout Pass B.

Native SQLite evidence:

```text
package: libsqlite3-0 3.46.1-9ubuntu0.2 amd64
runtime: /usr/lib/x86_64-linux-gnu/libsqlite3.so.0.8.6
runtime SHA-256: c43daabc6597cb20c84ae5b785d7c6072220966bd79dd12b961b98fb48ba224a
local development .deb SHA-256: 3a6cdcfa5352e6d2b5c4b158b20177dad71dce628624be1d7fca3817872f2ba8
sqlite3.h SHA-256: f319f664239fdd3154721a70b7cf37fa1475703c6a4deaf7605511851c1edb17
```

A03-specific GitHub Actions runtime-proof workflows were removed before freeze. Physical proof authority is the Oracle MCP/RPC receipt and checksum-bound Pass B evidence above.

## Independent review

The final net A03 candidate was reviewed by Sergeant after route cleanup. Outcome: `APPROVE`, officer verdict `PASS`, admitted findings `0`, unresolved assurances `0`.

## Claim boundary

- A03 ledger runtime: PROVEN.
- A04 Activity execution: NOT IMPLEMENTED / NOT PROVEN by A03.
- Prime-native integration: NOT QUALIFIED.
- Production: NOT AUTHORIZED.
- Release: NOT ACCEPTED.
- `Prime Host ID != Ptah Node ID` remains invariant.

## Decision

A03 — Ledger, schema versions and crash-safe migrations — is **FROZEN / PROVEN / COMPLETE**.

A04 — Activity, Operation, Attempt, Event and Receipt runtime — is **READY**.

P01P remains **OPEN / DEFERRED** and does not block Programme A development.

## Next action

Begin A04 from P0C-I004 and frozen WP02, WP04, WP11 and WP12 contracts. Preserve A03 as the repository-owned persistence substrate; do not widen A04 into PTY, Workspace, Object or Prime-native integration work.
