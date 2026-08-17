# A05 — Native process, PTY and multi-terminal Provider acceptance

**Status:** ACCEPTED COMPLETE
**Recorded:** 2026-08-17
**Roadmap item:** A05 / P0C-I005

## Accepted implementation

A05 is frozen, independently reviewed, proven through the accepted Oracle MCP/RPC development-host path, and merged into `jaydumisuni/Ptah-space`.

```text
Ptah-space PR: #27
candidate exact head: 4be4f170219701841aca367dd98c7b746fdd444c
merge: 34bc4beed57517532a1d79ae64131835a395f7b2
freeze-quality receipt: 0000-ptah-a05-freeze-quality-20260817-0155z
frozen exact-head proof receipt: 0000-ptah-a05-frozen-proof-fast-20260817-0204z
Tenfold final-review packet SHA-256: 627074b11c36014d8f8c391bdbcecbb5130a68e0fbbe8151d8af03aa700b9061
Tenfold private lanes: 150
transport: oracle.live.v1
githubInteractivePathUsed: false
Rust/Cargo toolchain: 1.97.1
Cargo.lock SHA-256: cbcec35bac0fb9c08782390e28398d0f451cbd97e35381ee418f66574c6e4f0e
portable-pty: 0.9.0
portable-pty crates.io checksum: b4a596a2b3d2752d94f51fac2d4a96737b8705dddd311a32b9af47211f08671e
native-process source SHA-256: 994d47d4db7c30973be12d5653e2e1bbe62e85b640e85fa05e6e43b81d06105b
A05 acceptance-test SHA-256: 1f5246af783d2f75413532778a347f280a903303e41f9cbeed4d22baa06d2530
Provider API source SHA-256: 8422c7cd6640615c3243483758c1241660a0c5979d3e09006014c0ea903e5a60
```

GitHub Actions are **not** the A05 runtime execution or proof authority. The accepted execution/proof path is Oracle MCP/RPC on the accepted development host. GitHub carries source, review and merge history.

## What A05 proves

A05 establishes the native process and terminal Provider over the accepted A04 orchestration/proof substrate:

- the logical Provider, Provider Revision, Provider Instance and Provider Generation remain Ptah-owned canonical context;
- backend operating-system PIDs are retained only as endpoint aliases/evidence and never become canonical Ptah identities;
- native pipe-mode processes expose independently observable stdout and stderr streams;
- PTY mode truthfully exposes one merged terminal stream and retains that limitation instead of falsely claiming stderr separation;
- process launch establishes only a running state; exit is independently observed before it can become exit evidence;
- PTY input and resize are mechanically controlled through a fenced terminal-control lease;
- terminal attachment is fenced by Provider Generation and connection epoch;
- replacement control leases invalidate stale leases;
- Provider Generation advancement fences old terminal-control handles;
- durable terminal detach/reconnect preserves work under Retain Policy;
- last-attachment disconnect terminates work when Terminate Policy explicitly requires it;
- several PTYs remain independent;
- bounded stream retention exposes sequence, total bytes, retained bytes and truncated bytes;
- A05 Provider execution can construct the exact accepted A04 `AttemptContext` rather than replacing the A04 runtime.

## Review, freeze and proof

Final Review on exact candidate `4be4f170219701841aca367dd98c7b746fdd444c` proved:

- exact 9-file net diff against accepted A04 merge `a63eb8f2c73f961b8466b844c6f194f2381a8139`;
- no GitHub workflow changes;
- clean tree and `git diff --check`;
- Sergeant APPROVE / PASS;
- 10 permanent officers;
- 150 planned Tenfold private lanes;
- 0 admitted findings;
- 0 unresolved assurances.

Freeze-quality proof on the same exact candidate passed:

- `cargo fmt --all -- --check`;
- locked scoped Clippy with `-D warnings`;
- the current direct-dependency lock verifier;
- source-hash checks matching the reviewed bytes.

Frozen exact-head proof through Oracle MCP/RPC then passed:

- A01 Apache-2.0 licence boundary acceptance;
- current dependency-lock authority;
- A02 identity and Node-agent tests;
- A03 ledger tests;
- A04 Event, Receipt and Activity-runtime tests;
- A05 Provider and native-process/PTY tests;
- complete Rust workspace integration;
- tracked-clean checkout after proof.

The proof also established that protected A01–A04 history/source surfaces were byte-unchanged from the accepted A04 base. Historical A01/A02 package-count validators remain provenance for their original acceptance snapshots and were not rewritten to misclassify later authorized dependency growth.

## Preserved boundaries

A05 does **not** claim:

- A06 persistent Workspace, Session or authority-projection implementation;
- Object/CAS work from A07;
- Prime-native integration qualification;
- production authorization;
- release acceptance;
- that a PID, spawn acknowledgement, PTY write, attachment or Provider acknowledgement alone proves accepted Activity result success.

The A04 acceptance record remains historical truth: at A04 acceptance, A05 was not yet implemented. Later A05 completion does not rewrite that earlier non-claim.

P01P remains **OPEN / DEFERRED** and does not block Programme A development.

## Authority decision

A05 is **FROZEN / PROVEN / COMPLETE**.

A06 — Persistent Workspace, Session and authority projection — is **READY**.

## Next action

Begin A06 from P0C-I006, frozen WP05, WP09 and WP11 contracts, and the AI Project Workspace profile. Preserve A03 ledger durability, A04 orchestration/proof semantics and A05 process/terminal Provider identity and fencing. Do not widen A06 into A07 Object/CAS work, P01P Prime-native integration, production or release claims.
