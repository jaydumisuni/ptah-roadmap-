# A06 — Persistent Workspace, Session and authority projection acceptance

**Status:** ACCEPTED COMPLETE
**Recorded:** 2026-08-17
**Roadmap item:** A06 / P0C-I006

## Accepted implementation

A06 is independently reviewed, frozen, proven through the accepted Oracle MCP/RPC development-host path, and merged into `jaydumisuni/Ptah-space`.

```text
Ptah-space PR: #28
candidate exact head: 28444aa2331c4c170df62f4de9499e93009f0f41
merge: 55cb08cffec10a2ee560014133d393be55f98d05
final Tenfold review receipt: 0000-ptah-a06-final-review-20260817-0428z
freeze-gate receipt: 0000-ptah-a06-freeze-gate-20260817-0429z
freeze manifest SHA-256: 6cb32c2210927fc4fe1449bb8ac40502666a55071259157c431c13d76c963494
Pass B receipt: 0000-ptah-a06-pass-b-proof-20260817-0430z
Pass B proof manifest SHA-256: 26e7d031f444c4943e5ffcd36b484bd3d1a9265f9132b58d9d2d8b420f8e8d01
Tenfold private lanes: 110
Sergeant verdict: APPROVE
transport: oracle.live.v1
githubInteractivePathUsed: false
Rust/Cargo toolchain: 1.97.1
Cargo.lock SHA-256: b7e2a30fc0660160fd330a9e1272ff195554b52b76f619c886826b933fb0c90e
ptah-workspace Cargo.toml SHA-256: 2c2dc997762f89d2fa7894f631fa42eae7fbcf599e1432694f78a0ae4aee6cbb
ptah-workspace source SHA-256: 8b3d6383011aaf9422050b3c4a6a8b777a28c366e7c167b2818099976b830667
A06 acceptance-test SHA-256: 4bd1bc24d5bf7cc493839e50f22bfd0c5b02bb242be280c817915eb5a4d4e97b
```

GitHub Actions are **not** the A06 runtime execution or proof authority. The accepted execution/proof path is Oracle MCP/RPC on the accepted development host. GitHub carries source, review and merge history.

## What A06 proves

A06 establishes durable Workspace/Session authority projection over the accepted A03 ledger and A04/A05 runtime foundations:

- Workspace identity persists across disconnect and process/runtime restart;
- Workspace revisions and Provider bindings are durable without replacing Workspace identity;
- Session creation, attachment and detach state are durable projections;
- exact Provider Generation and connection epoch fence Session attachment authority;
- stale Session authority fails closed;
- Workspace-scoped Object, Activity, terminal and Policy references survive restart without claiming A07 Object/CAS materialization;
- Workspace Membership provides scoped participant authority;
- cross-Workspace retrieval fails closed without an accepted Membership or exact Secure Grant;
- Secure Grant subject, grantee, lifecycle, scope and expiry are enforced;
- a Secure Grant that expires after issue is rejected after the clock advances;
- missing Session attachments remain explicit recovery evidence instead of disappearing;
- worker formation role, independence lane, checkpoint, partial-result and conflict references survive restart;
- handoff records preserve subject and authority references across agent replacement;
- recovery remains metadata projection only and does not falsely claim A13 checkpoint/restore execution.

## Review, repair, freeze and proof

Initial A06 review exposed one real authority defect: an otherwise valid Secure Grant could still authorize cross-Workspace retrieval after its frozen `expires_at` time. A06 was not frozen at that point.

The candidate was repaired to enforce expiry at grant issue/retrieval boundaries and to add an external regression that advances the injected clock beyond grant expiry. The same repair cycle also removed an unused development dependency, synchronized `Cargo.lock`, fixed the acceptance fixture ownership error exposed by Clippy, and retained owned write-command APIs with explicit lint expectations rather than changing their ownership semantics.

Final Review on exact candidate `28444aa2331c4c170df62f4de9499e93009f0f41` established:

- exact four-file net diff against accepted A05 merge `34bc4beed57517532a1d79ae64131835a395f7b2`;
- no GitHub workflow changes;
- clean tree and `git diff --check`;
- Sergeant APPROVE;
- 110 planned Tenfold private lanes;
- no required actions admitted by the final verdict.

Freeze on the same exact candidate passed:

- `cargo fmt --all -- --check`;
- locked scoped Clippy with `-D warnings`;
- full Rust workspace regression;
- unchanged external registry dependency set relative to A05;
- exact hashes for all four changed files.

Fresh detached Pass B through Oracle MCP/RPC then passed:

- source hashes equal to the frozen manifest;
- format and locked Clippy;
- the complete A06 acceptance suite;
- complete Rust workspace regression;
- direct execution of checksum-bound A06 acceptance executables;
- clean tracked checkout after proof.

## Preserved boundaries

A06 does **not** claim:

- A07 Content hashing, Object registration, immutable Revision, Artifact, Location or local CAS implementation;
- A13 checkpoint/restore execution;
- Prime-native integration qualification;
- production authorization;
- release acceptance;
- that a Session attachment, Membership, Secure Grant, recovery projection or provider acknowledgement alone proves accepted Activity result success.

The A05 acceptance record remains historical truth: at A05 acceptance, A06 was not yet implemented. A06 completion does not rewrite that earlier non-claim.

P01P remains **OPEN / DEFERRED** and does not block Programme A development.

## Authority decision

A06 is **FROZEN / PROVEN / COMPLETE**.

A07 — Object, Revision, Artifact, Location and local CAS — is **READY**.

## Next action

Begin A07 from P0C-I007 and frozen WP03, WP07 and WP10 contracts. Preserve A03 durability, A04 producing-Activity/Receipt provenance and A06 Workspace authority. Implement Content hashing, logical Object registration, immutable Revisions, Relationship/View foundations, digest-addressed local CAS, Artifact promotion, Location/provenance and integrity verification. Do not widen A07 into A08 transfer execution, P01P Prime-native integration, production or release claims.
