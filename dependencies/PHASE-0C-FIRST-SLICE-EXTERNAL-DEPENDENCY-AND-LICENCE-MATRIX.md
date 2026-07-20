# Phase 0C — First-slice external dependency and licence matrix

Status: candidate pin set — owner licence decision and Rust crate lock remain open

Verified on: 2026-07-20

## Rules

1. Versions in this record are the accepted starting candidates for the first vertical slice.
2. Exact installed binary/package digests and transitive notices must be captured by the implementation repository before authorization.
3. Backend names and backend IDs remain scoped Aliases and evidence; they do not become canonical Ptah identity.
4. Executing an external program does not transfer its licence to Ptah-owned source, but redistribution and linked-library obligations still apply.
5. No donor source is copied into Ptah merely because a compatible licence exists.
6. Every replacement must preserve stable Ptah identity, migration history, Receipts and WP14 proof results.

## Pin matrix

| Component | Candidate pin | First-slice role | Licence boundary | Integration boundary | Replacement path |
|---|---:|---|---|---|---|
| Ubuntu Server | 24.04.4 LTS amd64 ISO, SHA-256 `e907d92eeec9df64163a7e454cbc8d7755e8ddc7ed42f99dbc80c40f1a138433` | First Linux Node installation source | Distribution aggregate; retain package-specific copyright/licence records | Host OS only; Ptah contracts do not expose Ubuntu package identity | Another Linux host satisfying the same capability profile |
| Rust toolchain | 1.97.1 stable | Ptah-owned Node/control implementation toolchain | Rust is primarily MIT OR Apache-2.0, with separately identified portions | Pinned by `rust-toolchain.toml`; compiler identity retained as Build evidence | Later stable Rust after exact-head proof rerun |
| SQLite | 3.53.3 | One-Node durable ledger behind repository-owned storage interface | Core deliverable is public domain; build tooling may carry separate terms | Embedded through a Rust database adapter; SQLite row IDs never become Ptah IDs | PostgreSQL or another ledger implementation |
| containerd | 2.3.1 LTS | Local OCI container lifecycle Provider | Code Apache-2.0; repository documentation includes CC-BY-4.0 material | External daemon/API; containerd IDs remain Aliases | Another OCI-compatible runtime Provider |
| runc | 1.4.2 stable | Low-level OCI runtime used beneath containerd | Apache-2.0; official static binaries include separately noticed LGPL-2.1 libseccomp material | External runtime selected/configured by containerd; never called canonical identity | Another OCI runtime implementation |
| Node.js | 24.18.0 LTS | Supported runtime for the Playwright Browser adapter | MIT plus bundled third-party notices | Adapter runtime only; Node process IDs remain transient evidence | Later supported Node LTS or non-Node Browser Provider |
| Playwright | 1.60.0 | First interactive Browser Provider | Apache-2.0; downloaded browser artifacts retain their own notices | Adapter process/API; Browser/Profile/Page/Frame identity remains Ptah-owned | Another Browser Provider |
| Playwright Chromium | 148.0.7778.96 | Browser binary paired with Playwright 1.60.0 | Chromium and bundled components retain upstream licences/notices | Exact browser revision recorded as Provider generation evidence | Browser revision update or another browser engine |
| Git | 2.55.0 | Hardened clone/mirror adapter | GPL-2.0; execute as a separate program, retain source/offers when redistribution requires them | CLI subprocess with protocol, hook and submodule policy; Git object IDs are evidence, not Ptah Object IDs | libgit2 or another hardened Git Provider |
| libarchive | 3.8.8 | First archive decomposition backend | New BSD / BSD-2-Clause family; retain notices | Library or isolated adapter; parser output creates derived records and never replaces source truth | Format-specific Domain Pack adapters |
| Python | 3.11 for frozen WP13 workflow; 3.12 host candidate | Contract-conformance tooling only | Python Software Foundation licence plus bundled notices | Tooling boundary; not part of Ptah runtime identity | Later supported Python after harness verification |

## Official verification sources

- Ubuntu release and checksums: `https://releases.ubuntu.com/noble/`
- Rust release: `https://blog.rust-lang.org/releases/latest/`
- Rust licensing: `https://github.com/rust-lang/rust`
- SQLite releases: `https://www.sqlite.org/changes.html`
- SQLite public-domain statement: `https://www.sqlite.org/copyright.html`
- containerd releases and licensing: `https://github.com/containerd/containerd/releases`
- runc releases and licensing: `https://github.com/opencontainers/runc/releases`
- Node release schedule: `https://nodejs.org/en/about/previous-releases`
- Playwright releases: `https://github.com/microsoft/playwright/releases`
- Git source releases: `https://www.kernel.org/pub/software/scm/git/`
- libarchive stable releases and licence: `https://www.libarchive.org/`

## Selected boundaries and caveats

### Ubuntu

Ubuntu is a distribution of many independently licensed packages. The implementation must preserve package inventory and notices rather than describing the whole installed system as Apache-2.0 or any other single licence.

### Rust and crate graph

Rust 1.97.1 is the compiler/toolchain pin. The direct Rust crate graph is not accepted by this file. It must be generated in `Ptah-space`, committed through `Cargo.lock`, reviewed with licence/advisory tooling and recorded in a separate Phase 0C crate-lock decision before ADR-0033 acceptance.

### SQLite

SQLite owns no public Ptah schema or storage contract. The first implementation must use explicit repository methods for transaction boundaries, migrations, canonical IDs and Receipt persistence. SQL table names and integer row IDs are backend details.

### containerd and runc

The selected path is containerd 2.3.1 LTS with runc 1.4.2. The implementation must record:

- daemon/runtime versions and executable digests;
- configured snapshotter;
- runtime name;
- cgroup driver;
- namespace used by Ptah;
- image digest;
- container/task aliases;
- start/exit/cleanup observations.

A successful containerd/runc API acknowledgement is not proof that the workload reached or completed its required state.

### Playwright and Chromium

Playwright 1.60.0 identifies a tested browser set and reports Chromium 148.0.7778.96. The browser install directory and executable digest must be retained. Playwright IDs, CDP session IDs and OS process IDs remain transient Aliases/evidence.

### Git

Git is executed as a separate GPL-2.0 program. The adapter must disable or explicitly govern hooks, restrict protocols, control submodules, reject unsafe paths and retain exact command/exit/result evidence. Ptah must not copy Git source into the public core without a separate licence decision.

### libarchive

Archive parsing must be budgeted and guarded against path traversal, archive bombs, malformed entries, encrypted gaps and unsupported formats. Successful parser completion does not imply complete decomposition coverage.

## Version-change policy

A selected-version change requires:

1. a new dependency/tool Provider generation;
2. updated source and licence verification;
3. updated digest/package inventory;
4. targeted positive and negative proofs;
5. backend-replacement evidence where identity continuity is affected;
6. an amended lock record before release acceptance.

## Open items

This record does not yet close:

- the public Ptah licence choice;
- the direct Rust crate and feature lock;
- exact Ubuntu package versions after installation;
- exact downloaded browser executable digest;
- redistribution decisions for runtime binaries and browser assets.

Those remain Phase 0C blockers.