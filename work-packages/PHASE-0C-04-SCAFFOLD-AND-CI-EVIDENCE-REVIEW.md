# Phase 0C-04 — Scaffold and exact-head CI evidence review

Status: passed for Phase 0C scaffold closure — runtime implementation remains unauthorized

Reviewed: 2026-07-20

## Scope

Review the non-claiming implementation scaffold in `jaydumisuni/Ptah-space` and determine whether it closes the Phase 0C source-layout and scaffold-CI preparation conditions without falsely starting the Ptah runtime.

## Canonical implementation history

The implementation repository first merged the broader non-claiming package layout at:

`ff26fa93d1b60781b49f33f5d1758680e1282d5f`

That scaffold established:

- 17 Rust workspace package boundaries at version `0.0.0-phase0c`;
- Rust `1.97.1`, edition 2024 and `publish = false`;
- no external Rust dependencies in `Cargo.lock`;
- Browser scaffold locked to Node.js `24.18.0` and Playwright `1.60.0`;
- host and contract-lock candidate records;
- explicit no-runtime/no-licence claims;
- placeholder packages that expose no runtime capability.

The exact-head evidence hardening was tested at:

`900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc`

and merged at:

`23fc97ff0acd2b219990411ec4fb84d8a8c0a567`

## Exact-head workflow evidence

Workflow: `Phase 0C scaffold`

Run ID: `29717942201`

Tested head: `900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc`

All required jobs passed:

1. `no-build-boundary`
   - exact head checkout;
   - private/internal leak check;
   - incomplete contract-lock enforcement;
   - runtime authorization remained false;
   - source-policy report retained.
2. `rust-scaffold`
   - Rust `1.97.1` installed;
   - formatting passed;
   - Clippy passed with warnings denied;
   - all workspace tests passed;
   - locked Cargo metadata retained;
   - exact-head report retained.
3. `browser-scaffold`
   - Node.js `24.18.0` installed;
   - `npm ci` used the committed lockfile;
   - syntax and tests passed;
   - dependency graph retained;
   - exact-head report retained.
4. `frozen-conformance`
   - roadmap checkpoint `dc2db457f1705d0cba80f17ab76e5e93f808aee0` checked out locally;
   - frozen WP13 harness unit tests passed;
   - repository-wide structural conformance passed;
   - semantic fixtures passed;
   - exact-head conformance report retained.

## Artifact evidence

| Evidence group | Artifact ID | SHA-256 digest |
|---|---:|---|
| Source policy | `8451256102` | `2d1684b64e6c9c02cae7ca0983b33735cb0ea3b2a688d1783144e3c34dd89a28` |
| Rust scaffold | `8451258083` | `7fd85f969beb175ae60b97b88bcc807fff4e293b0efc7ad7a3bf8756a438fb9f` |
| Browser scaffold | `8451256217` | `6e40ddb84117eb82826f677434091be388e068835b9fd5011ff9b94b805e11ac` |
| Frozen conformance | `8451257268` | `07c0783ce0320ae1bb1e49cfb8b6fea000643525fc520be88d46c8935b74bd6e` |

Artifacts expire under the current 30-day CI retention policy. Their IDs and digests remain retained governance evidence, but long-term Phase 0C acceptance should copy the final accepted reports into a durable proof Location or extend retention before authorization.

## Source-layout findings

The selected package boundaries align with the first-slice task graph:

- contract bindings and identifiers;
- ledger, events and Receipts;
- Node and Activity runtime boundaries;
- Workspace, Object store and transfer boundaries;
- Provider API and checkpoint boundaries;
- Node/control services;
- container, Git and decomposition adapters;
- separate Browser Provider package.

This is a package-layout selection only. Empty or constant-only crates are not implementation completion.

## Dependency findings

### Rust

The current `Cargo.lock` contains only the 17 Ptah-owned scaffold packages and no third-party crates. Therefore:

- the scaffold dependency graph is exact and reviewed;
- no runtime Rust crate has yet been selected;
- SQLite, async runtime, UUID, serialization, tracing, PTY, HTTP and container client crate choices remain open;
- introducing the first third-party Rust crate requires a new reviewed lock and licence/advisory evidence.

### Browser

The Browser scaffold commits an npm lock for Playwright `1.60.0` and its transitive package graph. It does not download or verify the Chromium executable in the scaffold job because install scripts are disabled. Exact Chromium bytes and digest remain an authorization blocker for the executable Browser Provider.

### GitHub Actions

The accepted workflow pins checkout, setup-python, setup-node and upload-artifact to immutable commits recorded in `dependencies/PHASE-0C-GITHUB-ACTION-IMMUTABLE-PINS.md`.

## Passed conditions

This review closes the following preparation conditions:

- implementation repository and source package layout exist;
- the scaffold is explicitly non-claiming and non-publishable;
- Rust and Browser scaffold locks are committed;
- immutable action pins are used;
- exact-head Rust, Browser and source-policy checks pass;
- frozen WP13 structural and semantic conformance passes from local files;
- failure evidence and successful reports are retained as artifacts.

## Conditions not closed

This review does not close:

- owner acceptance of Apache-2.0 or another public licence;
- runtime Rust crate and feature selection;
- exact SQLite/containerd/runc/Git/libarchive installed binaries and digests;
- exact installed Ubuntu kernel/package inventory;
- Playwright Chromium download, executable digest and notices;
- WP14 runtime positive/negative proofs;
- runtime implementation authorization.

## Decision

The Phase 0C scaffold and CI preparation are accepted as complete. ADR-0033 remains proposed because runtime dependency, installed-host/browser evidence and owner licence decisions are still open.