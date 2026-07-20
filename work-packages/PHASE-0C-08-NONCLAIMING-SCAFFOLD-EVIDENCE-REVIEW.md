# Phase 0C-08 — Non-claiming scaffold evidence review

Status: passed for scaffold scope — runtime implementation remains unauthorized

## Reviewed implementation repository

- Repository: `jaydumisuni/Ptah-space`
- Scaffold branch head tested: `2f1fcedaa398254e5fa4b82583675a08755fa953`
- Pull request: `jaydumisuni/Ptah-space#2`
- Merge commit: `ff26fa93d1b60781b49f33f5d1758680e1282d5f`
- Exact-head workflow run: `29717770393`

## Scope merged

The merged scaffold contains:

- a Rust `1.97.1` workspace;
- seventeen compile-only crate/service/adapter boundaries;
- an exact candidate `Cargo.lock` with no external Rust crates yet;
- a Node `24.18.0` Browser Provider package boundary;
- Playwright `1.60.0` and transitive npm integrity lock;
- candidate `cargo-deny` policy;
- host image and capability requirement records;
- an explicitly incomplete upstream contract lock;
- a deliberately nonfunctional host capability collector placeholder;
- no-build-boundary checks;
- candidate Rust and Browser scaffold CI.

No Node, Workspace, Activity runtime, Provider, transfer engine, decomposition engine, Browser runtime or UI is claimed as implemented.

## Exact-head result

Workflow run `29717770393` passed all jobs against scaffold head `2f1fcedaa398254e5fa4b82583675a08755fa953`:

1. `no-build-boundary` — passed;
2. `rust-scaffold` — Rust `1.97.1` install, formatting, Clippy and all workspace tests passed under the committed lock;
3. `browser-scaffold` — exact npm install, syntax check and tests passed.

The first workflow attempt correctly found a self-matching leak-scanner defect. The second isolated a Clippy test-target policy mismatch. Both were corrected without suppressing the no-build boundary or production-target warnings. The third exact-head run passed.

## Closed Phase 0C conditions

This evidence closes the following candidate conditions:

- `Ptah-space` contains the accepted non-claiming top-level workspace structure;
- Rust and Node toolchain manifests are pinned;
- the Browser Provider candidate has an exact npm dependency lock;
- the empty Rust scaffold has an exact lock;
- scaffold code can be formatted, linted and tested;
- the repository itself prevents the scaffold from claiming runtime authorization;
- the public tree contains no internal package-gateway reference.

## Conditions still open

This evidence does not close:

- owner acceptance of Apache License 2.0;
- a public `LICENSE` and final `NOTICE`;
- external Rust crate selection, exact transitive licence/advisory review and final `Cargo.lock`;
- complete frozen-catalog inventory in `contracts/upstream-lock.json`;
- generated Rust bindings and reproducibility digest;
- WP13 conformance execution from the implementation repository;
- host capability collector implementation and a real pinned-host report;
- direct binary/source artifact signatures and hashes beyond recorded candidates;
- first-slice runtime implementation or WP14 execution;
- implementation authorization.

## Review conclusion

The scaffold is a valid Phase 0C artifact and may remain on `Ptah-space/main`. It does not justify accepting ADR-0033 or changing `CURRENT_STATE.md` to authorized. The next technical closure work is frozen-contract locking/generation, dependency inventory and host capability evidence, while the public-licence boundary remains an owner decision.