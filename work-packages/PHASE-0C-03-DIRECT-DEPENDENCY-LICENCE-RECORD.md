# Phase 0C-03 — Direct dependency and licence record

Status: candidate — runtime implementation remains unauthorized

## Purpose

Pin the first external implementations behind Ptah's neutral contracts, record their licence boundary and preserve a concrete exit path. This record does not authorize copying donor code or allowing dependency identity to become canonical Ptah identity.

## Selected direct toolchain and runtime candidates

| Role | Candidate version | Licence / distribution boundary | Ptah integration boundary |
|---|---:|---|---|
| Rust toolchain | `1.97.1` stable | Rust is primarily MIT OR Apache-2.0, with separately identified components | builds Ptah-owned Rust crates; compiler identity is Build evidence only |
| Node.js for Browser Provider | `24.18.0` LTS | Node.js project licence and bundled third-party notices retained | isolated Browser Provider service; Node process identity is an Alias |
| SQLite | `3.53.3` | SQLite upstream public-domain dedication; selected Rust driver retains its own licence | ledger backend behind `ptah-ledger`; database file/path is not canonical identity |
| containerd | `2.3.1` LTS line | Apache-2.0 code; upstream docs may carry separate CC terms | OCI Provider implementation; containerd IDs remain scoped Aliases |
| runc | `1.4.2` | Apache-2.0; distributed binary notices and linked-library notices retained | low-level OCI runtime used through containerd, never canonical Ptah identity |
| Playwright | `1.60.0` | Apache-2.0 | Browser Provider implementation |
| Playwright Chromium | `148.0.7778.96` | Chromium and bundled third-party licences/notices retained separately | Browser Process implementation; browser IDs remain Aliases |
| Git | `2.55.0` | GPL-2.0 family; executed as a separate process, no Git source copied into Apache Ptah Core | hardened Git Provider adapter |
| libarchive | `3.8.7` | BSD-licensed upstream library and notices retained | first archive decomposition adapter |

## Integrity pins already available

- Ubuntu server ISO SHA-256 is recorded in `PHASE-0C-02-HOST-BASELINE-PIN.md`.
- containerd `2.3.1` Linux amd64 release archive candidate SHA-256: `628448bd973610c656c1cbea8e88b32fafd85b23cc1aa4a3372eb7198478c054`.
- SQLite `3.53.3` source ID: `2026-06-26 20:14:12 d4c0e51e4aeb96955b99185ab9cde75c339e2c29c3f3f12428d364a10d782c62`.
- SQLite `3.53.3` amalgamation SHA3-256: `28e484abdaa43630e34040ef6ed92be973a1ad54107803d8af5145b889c23ed7`.

Every downloaded binary or source archive must additionally be locked by its authoritative checksum/signature in the implementation repository. Version text alone is insufficient.

## Public Ptah licence candidate

Recommendation remains Apache License 2.0 for Ptah-owned public source.

The public licence applies only to files for which THETECHGUY DIGITAL SOLUTIONS owns the necessary rights and intentionally publishes under that licence. It does not automatically relicense:

- Ubuntu or distribution packages;
- Rust toolchain components;
- Git;
- Chromium and browser codecs;
- Node.js or npm dependencies;
- containerd/runc;
- libarchive;
- donor code;
- private THETECHGUY Domain Packs and protocol knowledge;
- credentials, customer data, evidence bundles or restricted repair workflows.

Third-party components retain their own licences and notices.

## Required per-dependency lock record

Each selected dependency must receive a machine-readable lock entry with:

- canonical dependency name;
- exact version and release/tag identifier;
- source/release URL authority;
- source or binary digest;
- signature verification result when offered;
- SPDX licence expression;
- notice-file locations;
- whether it is linked, dynamically loaded, invoked as a process or used only at build time;
- Ptah adapter/crate owning the integration;
- expected capabilities;
- forbidden identity leakage;
- replacement candidate;
- migration and proof cases;
- known security limitations;
- review timestamp.

## Rust crate lock remains a blocker

No crate-level set is accepted by this record. Before implementation authorization, `Ptah-space` must contain:

1. a minimal `Cargo.toml` workspace;
2. an exact `Cargo.lock`;
3. licence/advisory policy such as `cargo-deny` configuration;
4. a generated dependency inventory and licence report;
5. an explicit review of SQLite driver, async runtime, serialization, identifier, hashing, tracing, HTTP/local RPC and PTY crates;
6. proof that no crate redefines frozen Ptah contracts.

A crate may not be selected merely because it is popular or already used by a donor.

## Browser dependency rule

Playwright's browser build is pinned as part of the Playwright package. A system Chromium substitution is a different backend revision and must not occur silently. Browser executable digest, Playwright version and launch policy must be retained in each Browser Provider generation.

## Git licence isolation rule

The Git adapter invokes the external Git executable with hardened configuration. Ptah does not copy or link Git implementation code into the Apache-licensed core. Command, version, environment policy, exit result and resulting repository Object identity are retained as Receipt evidence.

## Container integrity rule

The initial container path requires the selected containerd and runc releases plus a recorded OCI configuration. CNI networking is not required for the first isolated local proof unless explicitly enabled and pinned. A container start acknowledgement cannot become workload success.

## Exit strategy

- Rust implementation language may coexist with later language-specific Providers.
- SQLite may be replaced by PostgreSQL or another ledger backend.
- containerd/runc may be replaced by another OCI-conformant Provider.
- Playwright/Chromium may be replaced by another Browser Provider.
- Git CLI may be replaced by another hardened Git implementation.
- libarchive may be supplemented or replaced by Domain Pack-specific parsers.

Replacement must preserve canonical Ptah identities, migrations, Receipts and the frozen proof burden.

## Remaining blockers

- owner acceptance of the Apache-2.0 public/private boundary;
- authoritative hashes/signatures for every distributed artifact;
- the exact Rust crate lock and licence report;
- an exact implementation commit proving these versions are actually used.