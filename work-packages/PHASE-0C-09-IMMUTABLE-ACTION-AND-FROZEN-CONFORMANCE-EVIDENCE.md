# Phase 0C-09 — Immutable Action and frozen-conformance evidence

Status: passed for scaffold CI scope — runtime implementation remains unauthorized

Reviewed: 2026-07-20

## Purpose

Harden the merged non-claiming `Ptah-space` scaffold so its CI evidence is bound to the exact pull-request head, third-party Actions are immutable-pinned, failure reports are retained and the frozen WP13 structural/semantic harness runs from local files.

## Accepted GitHub Action pins

| Action | Release label | Exact commit | Licence | Role |
|---|---:|---|---|---|
| `actions/checkout` | `v6.0.2` | `de0fac2e4500dabe0009e67214ff5f5447ce83dd` | MIT | Exact-head scaffold and frozen-roadmap checkout |
| `actions/setup-python` | `v6.2.0` | `a309ff8b426b58ec0e2a45f0f869d46889d02405` | MIT | Source-policy and WP13 Python environments |
| `actions/setup-node` | `v6.4.0` | `48b55a011bda9f5d6aeb4c2d9c7362e8dae4041e` | MIT | Node.js `24.18.0` Browser scaffold environment |
| `actions/upload-artifact` | `v7.0.1` | `043fb46d1a93c77aae656e7c1c64a875d1fc6a0a` | MIT | Retained per-lane reports |

Floating action tags are prohibited in the acceptance workflow.

## Implementation evidence

Repository: `jaydumisuni/Ptah-space`

Evidence-hardening pull request: `#3`

Exact tested head:

`900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc`

Workflow run:

`29717942201`

Merge commit:

`23fc97ff0acd2b219990411ec4fb84d8a8c0a567`

## Passed lanes

1. `no-build-boundary`
   - exact pull-request head checkout;
   - private/internal gateway leak guard;
   - incomplete contract-lock guard;
   - nonfunctional host-capability-collector guard;
   - source-policy report retained.
2. `rust-scaffold`
   - Rust `1.97.1` installed;
   - formatting, Clippy and workspace tests passed;
   - locked Cargo metadata retained;
   - exact-head report retained.
3. `browser-scaffold`
   - Node.js `24.18.0` installed;
   - `npm ci --ignore-scripts` used the committed Playwright `1.60.0` lock;
   - syntax and tests passed;
   - dependency inventory and exact-head report retained.
4. `frozen-conformance`
   - roadmap checkpoint `dc2db457f1705d0cba80f17ab76e5e93f808aee0` checked out locally;
   - frozen WP13 harness unit tests passed;
   - structural conformance passed;
   - semantic fixtures passed;
   - exact-head report retained.

All reports state `runtime_implementation_authorized: false`.

## Artifact evidence

| Evidence | Artifact ID | SHA-256 digest |
|---|---:|---|
| Source policy | `8451256102` | `2d1684b64e6c9c02cae7ca0983b33735cb0ea3b2a688d1783144e3c34dd89a28` |
| Rust scaffold | `8451258083` | `7fd85f969beb175ae60b97b88bcc807fff4e293b0efc7ad7a3bf8756a438fb9f` |
| Browser scaffold | `8451256217` | `6e40ddb84117eb82826f677434091be388e068835b9fd5011ff9b94b805e11ac` |
| Frozen conformance | `8451257268` | `07c0783ce0320ae1bb1e49cfb8b6fea000643525fc520be88d46c8935b74bd6e` |

The current GitHub artifact retention is finite. Final Phase 0C acceptance must copy accepted reports into a durable proof Location or extend retention.

## Conditions closed

This evidence closes, for the scaffold scope:

- immutable Action commit pins;
- exact pull-request-head checkout and report binding;
- retained source-policy, Rust and Browser reports;
- frozen WP13 harness execution from `Ptah-space`;
- local structural and semantic conformance execution;
- artifact upload even when a preceding check fails.

## Conditions still open

This evidence does not close:

- complete frozen catalog locking and offline generated bindings;
- final runtime Rust crate lock/licence/advisory report;
- real host capability evidence;
- installed backend/browser executable hashes and signatures;
- WP14 runtime proof execution;
- public licence acceptance;
- runtime implementation authorization.

## Update rule

Changing any Action commit, workflow permission, frozen roadmap ref or report format requires a new exact-head run and an amended evidence record.