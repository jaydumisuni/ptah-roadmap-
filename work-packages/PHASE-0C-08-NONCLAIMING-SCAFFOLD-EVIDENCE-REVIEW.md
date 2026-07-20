# Phase 0C-08 — Non-claiming scaffold evidence review

Status: passed for scaffold scope — runtime implementation remains unauthorized

## Reviewed implementation repository

- Repository: `jaydumisuni/Ptah-space`
- Initial scaffold head tested: `2f1fcedaa398254e5fa4b82583675a08755fa953`
- Initial scaffold pull request: `jaydumisuni/Ptah-space#2`
- Initial scaffold merge: `ff26fa93d1b60781b49f33f5d1758680e1282d5f`
- Initial exact-head workflow run: `29717770393`
- Evidence-hardening head tested: `900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc`
- Evidence-hardening pull request: `jaydumisuni/Ptah-space#3`
- Evidence-hardening merge: `23fc97ff0acd2b219990411ec4fb84d8a8c0a567`
- Hardened exact-head workflow run: `29717942201`

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
- immutable-pinned exact-head Rust, Browser, source-policy and frozen-conformance CI.

No Node, Workspace, Activity runtime, Provider, transfer engine, decomposition engine, Browser runtime or UI is claimed as implemented.

## Initial exact-head result

Workflow run `29717770393` passed all initial scaffold jobs against head `2f1fcedaa398254e5fa4b82583675a08755fa953`:

1. `no-build-boundary` — passed;
2. `rust-scaffold` — Rust `1.97.1` install, formatting, Clippy and all workspace tests passed under the committed lock;
3. `browser-scaffold` — exact npm install, syntax check and tests passed.

The first workflow attempt correctly found a self-matching leak-scanner defect. The second isolated a Clippy test-target policy mismatch. Both were corrected without suppressing the no-build boundary or production-target warnings. The third exact-head run passed.

## Hardened exact-head result

Workflow run `29717942201` passed all hardened jobs against exact head `900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc`:

1. `no-build-boundary` — passed and retained a source-policy report;
2. `rust-scaffold` — formatting, Clippy, tests and locked metadata passed and were retained;
3. `browser-scaffold` — locked npm installation, syntax, tests and dependency inventory passed and were retained;
4. `frozen-conformance` — the WP13 harness unit tests, structural conformance and semantic fixtures passed from local files at roadmap checkpoint `dc2db457f1705d0cba80f17ab76e5e93f808aee0`.

The workflow:

- checked out the actual pull-request head rather than GitHub's synthetic merge ref;
- pinned every third-party Action to an immutable commit;
- retained reports under `if: always()` semantics;
- bound every report to the tested commit;
- preserved `runtime_implementation_authorized: false`.

Exact Action commits, artifact IDs and report digests are recorded in `work-packages/PHASE-0C-09-IMMUTABLE-ACTION-AND-FROZEN-CONFORMANCE-EVIDENCE.md`.

## Closed Phase 0C conditions

This evidence closes the following candidate conditions:

- `Ptah-space` contains the accepted non-claiming top-level workspace structure;
- Rust and Node toolchain manifests are pinned;
- the Browser Provider candidate has an exact npm dependency lock;
- the empty Rust scaffold has an exact lock;
- scaffold code can be formatted, linted and tested;
- the repository itself prevents the scaffold from claiming runtime authorization;
- the public tree contains no internal package-gateway reference;
- GitHub Actions used by the acceptance workflow are immutable-pinned;
- the frozen WP13 harness runs from `Ptah-space` against local contract files;
- source-policy, Rust, Browser, structural and semantic evidence is retained at the exact tested head.

## Conditions still open

This evidence does not close:

- owner acceptance of Apache License 2.0;
- a public `LICENSE` and final `NOTICE`;
- external Rust crate selection, exact transitive licence/advisory review and final runtime `Cargo.lock`;
- complete frozen-catalog inventory in `contracts/upstream-lock.json`;
- generated Rust bindings and reproducibility digest;
- dependency-policy and contract-generation execution in the hardened workflow;
- host capability collector implementation and a real pinned-host report;
- direct binary/source artifact signatures and hashes beyond recorded candidates;
- durable retention of final acceptance reports beyond temporary CI artifacts;
- first-slice runtime implementation or WP14 execution;
- implementation authorization.

## Review conclusion

The scaffold and its hardened CI are valid Phase 0C artifacts and may remain on `Ptah-space/main`. They close the repository-layout, basic lock, exact-head and frozen-WP13 scaffold gates. They do not justify accepting ADR-0033 or changing `CURRENT_STATE.md` to authorized. The next technical closure work is complete frozen-contract locking/generation, runtime dependency inventory and real host capability evidence, while the public-licence boundary remains an owner decision.