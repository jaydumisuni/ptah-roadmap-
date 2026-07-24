# Ptah Progress Ledger

Tick only work backed by source inspection, pinned commits, accepted decisions, tests or live evidence.

- `[ ]` Not started
- `[-]` Active
- `[?]` Blocked or unresolved
- `[x]` Completed and evidenced

---

# Phase 0A — Donor recovery and requirement closure

**Status:** COMPLETE AND FROZEN

- [x] donor, internal-workload and licence recovery;
- [x] requirement closure and consistency review;
- [x] public/private boundary recorded;
- [x] ADR-0017 accepted;
- [x] frozen at `7d2dffee48f1400ba1cf88823343f09a3895ad33`.

---

# Phase 0B — Contracts, migrations, conformance and proof design

**Status:** COMPLETE AND FROZEN

- [x] WP01 — Common identity, versioning and typed families;
- [x] WP02 — Activity, Operation, Attempt, Event, Receipt and proof;
- [x] WP03 — Object, Revision, View, Artifact and storage;
- [x] WP04 — Node, Facility, Provider, capability and health;
- [x] WP05 — Workspace, Session, checkpoint and recovery;
- [x] WP06 — Transfer, synchronization, conflict, backup and restore;
- [x] WP07 — Recipe, Build, provenance, SBOM, signature and verification;
- [x] WP08 — Domain Pack, firmware, disk, filesystem and Device;
- [x] WP09 — Application, Browser, semantic UI and Shell;
- [x] WP10 — Knowledge, Data, Package and Plugin;
- [x] WP11 — Isolation, placement, reservation, Lease and secure grants;
- [x] WP12 — Security, Finding, Claim, Evidence, remediation and reproduction;
- [x] WP13 — executable cross-contract conformance;
- [x] WP14 — golden/negative corpus and first-slice proof-plan freeze;
- [x] all active schemas versioned and locally traceable;
- [x] lifecycle machines explicit and namespaced;
- [x] directional migrations and backend-replacement rules defined;
- [x] lawful positive, negative and adversarial fixtures pinned;
- [x] privacy, audience, redaction and retention represented;
- [x] WP13 found and forced correction of real cross-package defects;
- [x] WP13 exact-head unit, structural and semantic gates passed;
- [x] WP14 exact-head conformance passed;
- [x] ADR-0032 accepted;
- [x] frozen at `dc2db457f1705d0cba80f17ab76e5e93f808aee0`.

Key implementation-proof checkpoints:

- WP13 merge: `261b3e4a71657898643271a1625e14560a5bc769`;
- WP14 merge: `fef387c4f074af7fcf86f2d99f7f9b7637e91f88`.

Phase 0B completion defines implementation laws. It does not prove a Ptah runtime exists.

---

# Phase 0C — First vertical-slice approval

**Status:** ACTIVE — RUNTIME IMPLEMENTATION NOT AUTHORIZED

## Candidate selections and architecture records

- [x] implementation repository selected: `jaydumisuni/Ptah-space`;
- [x] Ubuntu Server 24.04.4 amd64 image pinned by SHA-256;
- [x] Noble GA 6.8 kernel line and mandatory capability requirements recorded;
- [x] Rust `1.97.1` selected for Node/control implementation;
- [x] SQLite `3.53.3` candidate selected behind repository-owned ledger boundary;
- [x] containerd `2.3.1` and runc `1.4.2` candidates selected behind OCI Provider boundary;
- [x] Node.js `24.18.0`, Playwright `1.60.0` and candidate Chromium build selected;
- [x] hardened Git `2.55.0` process adapter candidate selected;
- [x] libarchive `3.8.7` decomposition candidate selected;
- [x] source layout and public/private boundary recorded;
- [x] T00–T13 mapped to WP14 proof obligations;
- [x] exact-head CI acceptance shape recorded;
- [x] real workload candidates registered without promoting them into Ptah Core;
- [-] ADR-0033 remains proposed.

Selection/evidence package merge:

`79e83be0c340e871521d574719cdf6d20d52f4c9`

## Non-claiming implementation scaffold

- [x] 17 non-publishable Rust package boundaries merged;
- [x] initial empty third-party Rust dependency lock committed as non-claiming scaffold evidence;
- [x] private Browser scaffold and npm lock committed;
- [x] candidate cargo-deny policy committed;
- [x] initial host capability collector placeholder recorded as deliberately nonfunctional;
- [x] no-build and no-private-gateway guards merged;
- [x] initial exact-head scaffold workflow passed;
- [x] scaffold merge `ff26fa93d1b60781b49f33f5d1758680e1282d5f`.

## Hardened exact-head scaffold evidence

- [x] checkout Action pinned to `de0fac2e4500dabe0009e67214ff5f5447ce83dd`;
- [x] setup-python Action pinned to `a309ff8b426b58ec0e2a45f0f869d46889d02405`;
- [x] setup-node Action pinned to `48b55a011bda9f5d6aeb4c2d9c7362e8dae4041e`;
- [x] upload-artifact Action pinned to `043fb46d1a93c77aae656e7c1c64a875d1fc6a0a`;
- [x] exact pull-request head checked out and verified in reports;
- [x] source-policy/no-build job passed;
- [x] Rust formatting, Clippy, tests and locked metadata passed;
- [x] Browser locked install, syntax, tests and dependency inventory passed;
- [x] frozen WP13 harness unit tests passed from `Ptah-space`;
- [x] frozen structural conformance passed from local files;
- [x] frozen semantic fixtures passed from local files;
- [x] four digest-addressed artifacts retained;
- [x] exact tested head `900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc`;
- [x] passing workflow run `29717942201`;
- [x] hardening merge `23fc97ff0acd2b219990411ec4fb84d8a8c0a567`.

## Frozen catalog and generated binding closure

- [x] all fourteen frozen public catalogs locked by path, canonical URN and original-byte SHA-256;
- [x] catalog-set SHA-256 recorded as `f0668a5f5d5c68cabf623176608c627a94482faa4f4460e4f0fe0f0969d7c64d`;
- [x] 346 canonical schema bindings generated offline;
- [x] 99 lifecycle-machine bindings generated offline;
- [x] legacy catalog identifiers retained only as aliases;
- [x] generated manifest SHA-256 recorded;
- [x] generated catalog-index SHA-256 recorded;
- [x] generated Rust-module SHA-256 recorded;
- [x] generated output-tree SHA-256 `8f3355e0eac19715ea34e06ea227a826ac727d2e5b9ebf231a672927350c8db2` recorded;
- [x] two independent generated trees proved byte-identical;
- [x] generated Rust formatting, Clippy, compilation and tests passed;
- [x] no-build guard accepts the binding-locked state and still rejects runtime claims;
- [x] exact tested head `33043eaadb0f074d8867cb8ce999f16ea4c06a8b`;
- [x] catalog-lock workflow run `29727701958` passed;
- [x] binding-generation workflow run `29727701960` passed;
- [x] source/Rust/Browser/frozen-WP13 workflow run `29727701999` passed;
- [x] binding package merge `f45c96e3f667b463042b6a8b714066236fde703d`.

## Runtime dependency, backend signer and host-collector evidence

- [x] minimal exact Rust crate/features graph selected: ten direct crates;
- [x] final `Cargo.lock` committed with 99 resolved packages, 81 registry packages and zero Git dependencies;
- [x] crates.io sources and checksums recorded;
- [x] cargo-deny advisory, ban, licence and source policy passed at the exact candidate head;
- [x] nine selected distributed/source backend artifacts locked and verified against authoritative identities;
- [x] Playwright Chromium version `148.0.7778.96`, revision `1223` and installed-tree digest locked and reproduced;
- [x] Node.js, runc, Git and libarchive signing authorities pinned;
- [x] all four selected backend signatures cryptographically verified;
- [x] fail-closed host capability collector implemented for eighteen required capabilities;
- [x] realistic Ubuntu point-release and frozen-kernel identity finalizer implemented;
- [x] malformed contract-lock and malformed-blocker paths fail with controlled evidence diagnostics;
- [x] all eight workflows passed at exact head `bc12885ce41844b05481628543219c3a8d3574ba`;
- [x] negative HTTP `504` signature-attempt evidence retained and successful unchanged-lock retry passed;
- [x] implementation evidence squash-merged as `c2cd803b5e5c50787b3d8c2d24392d693afdbb3c`;
- [x] runtime authorization remained false in every accepted record.

## Apache-2.0 public/private boundary acceptance

- [x] non-operative boundary candidate exact-head tested and merged as `bf846574df65061bd99d9c0e3d22a401bf9f27e2`;
- [x] owner accepted `John Dumisuni trading as THETECHGUY DIGITAL SOLUTIONS` as the rights-holder wording;
- [x] exact official Apache-2.0 bytes installed at root `LICENSE` and `LICENSES/Apache-2.0.txt`;
- [x] root `NOTICE`, `CONTRIBUTING.md`, `SECURITY.md` and `REUSE.toml` made operative;
- [x] private THETECHGUY systems, data, restricted adapters, donor source and trademarks excluded;
- [x] third-party NOTICE review and future re-review triggers recorded;
- [x] seven positive/adversarial acceptance regressions passed;
- [x] all nine workflows passed at exact head `a47d418243af076b49367c4c4eccc8ef2090894c`;
- [x] owner-acceptance change squash-merged as `3ce7d4251db0b6ba3f145385ad7ad8dc09276393`;
- [x] runtime implementation remained unauthorized.

## AI Project Workspace behavioural donor — neutral substrate correction

- [x] ChatGPT Projects, Library, Work, Canvas and Scheduled Tasks retained as application-experience sources only;
- [x] code reuse fixed at none and OpenAI excluded as a runtime dependency;
- [x] `ptah.workspace.ai_project.v1` remains a composition of sixteen existing Ptah primitives with zero Core extensions;
- [x] drift assigning context, source authority, review, approval or promotion to Ptah identified and removed;
- [x] Hunter owns intelligence/context/coordination, Sergeant owns independent review, and humans/calling applications own acceptance;
- [x] ten corrected fixtures and 17 adversarial regressions enforce the neutral boundary;
- [x] all ten workflows passed at exact correction head `5a95c577edf366bad1d8949ee37c17b81f296254`;
- [x] retained artifact `8546091277` with digest `sha256:04472fd4fd546fcc2420d135cdfcb517381efbe5de8b3bc14f6971207fbde819`;
- [x] correction squash-merged as `8a8d620c5227a6508145cd4a30f4f45142bfabe9`;
- [x] no AF03 start, contract reopening or runtime authorization introduced.

## Master Plan and implementation roadmap closure

- [x] requirements, architecture laws, accepted decisions and known gaps recovered into one ledger;
- [x] complete product and operating Master Plan candidate written;
- [x] detailed dependency-ordered Programme P00/P01 and Programmes A–F roadmap candidate written;
- [x] WP01–WP14 and Phase 0C reconciliation completed with zero current Core extensions;
- [x] physical-host through ADR-0033 and authorization procedure recorded;
- [x] durable `AI_HANDOFF.md` and `master-plan-index.json` created;
- [x] proposed ADR-0034 and Phase 0C-16 evidence package created;
- [x] stale control-book records repaired and exact-head consistency validation passed;
- [x] Phase 0C-16 reviewed and merged as `2c24f9e6b0fc98d5e03605596db75d7495796353`;
- [x] ADR-0034 accepted; Master Plan and implementation roadmap version `1.0.0` are operative authorities.

## Tenfold archive formation — accepted

- [x] Sergeant tenfold private-force source pinned at `44c8f47f4bb50a73ef3b4d81d7b849a5aab37dfd`;
- [x] Ptah archive authority, pairing, promotion, privacy and save-point protocol accepted as version `1.0.0`;
- [x] 69 external and 29 internal obligations mapped into ten standard formations;
- [x] 200 private slots allocated with one primary and one independent verifier per obligation;
- [x] bounded archive-record template accepted;
- [x] candidate exact head `58b577b6793ec28de084e6d712c3c1e88bfe2d3a` passed 21 regression cases and exact-head validation in run `29853954659`;
- [x] retained artifact `8504497355` with digest `sha256:936740e8087e6f7f0a58b3d731117fcb9a4861edfd20c396fb1bb20a7d4f18f4`;
- [x] exact fifteen-file boundary directly reviewed and candidate merged as `c4973cbf4d02a34f14a7aefa85b8e2ea7b392752`;
- [x] ADR-0035 and Phase 0C-17 accepted;
- [x] AF01 completed ten paired source reviews with nine accepted archive records and one completed MiniRouter source-reuse block;
- [x] AF01 candidate exact head `f60e340cb856d50e88b4279147a933d838fce759` passed 24 regression cases in run `29862087745`;
- [x] AF01 retained artifact `8507695005` with digest `sha256:4ea6bf77131834b48b9e35ad5eb88538a87b6f376f2be4984f077eb3eeed1267`;
- [x] AF01 candidate merged as `0a35a8a904bdf235fa4989ea05b684443d5a879a` and accepted closure recorded;
- [x] AF02 completed ten paired source reviews with ten bounded archive acceptances and zero blocks;
- [x] AF02 candidate exact head `b710574b99269647cdd9029db5a2b217642aa344` passed 33 adversarial regressions in run `29875542752`;
- [x] AF02 retained artifact `8512821506` with digest `sha256:78c5b702aa6025f088e2c54002bbe84fead003c92e0bb98ec18fcd0220b1d81c`;
- [x] AF02 candidate merged as `58d89dfd1d5348cc8423222e3aff256ee041dce2` and accepted closure recorded;
- [x] AF03 accepted complete: ten paired records, ten accepted archive outcomes, zero blocks, independent Sergeant PASS WITH MANDATORY RETAINED RESTRICTIONS, candidate merge `d86218e1127c57bacfb4d88eff15b81d326995ba`.
- [ ] AF04 is READY / NOT STARTED; no AF04 source record is pre-accepted.


## Diagnostic advisory and efficient worker boundary — accepted

- [x] owner boundary recovered: diagnose platform condition without deciding caller work;
- [x] owner ten-for-two boundary recovered: spread a caller-given job across bounded workers for speed and efficiency;
- [x] frozen Node/Provider health, Recipe/Plan/Run/Step, Workspace/Activity/Attempt, Reservation/Grant/Lease/Fence, Event/Receipt, Claim/Evidence and View/Artifact primitives mapped;
- [x] diagnostic advisory, upgrade-request and worker-execution boundaries accepted as version `1.0.0`;
- [x] Programme A02/A04/A06/A14/A15 proof placement accepted;
- [x] exact head `d2608ba7c619c1c402091edd619a4b29813ee9a7` passed 41 regressions in run `29986975197`;
- [x] retained artifact `8555395796` with digest `sha256:72025fb0aa5a969ea73abe95d7352f7cf14f1c847943955bd768a46d964a4c61`;
- [x] candidate merged as `fbc4ee80284a2d7ea38a44fdbfa90f0348b875ae`;
- [x] ADR-0036 and Phase 0C-18 accepted;
- [x] implementation remains unauthorized;
- [x] AF03 used the accepted ten-for-two execution boundary and independent Sergeant review, then was accepted separately; AF04 remains READY / NOT STARTED.

## Active Phase 0C closure work

- [x] select the minimal external Rust crate/features graph;
- [x] produce the final runtime-candidate `Cargo.lock`;
- [x] run crate licence, advisory, ban and source policy;
- [x] lock authoritative hashes for every selected distributed/source backend artifact;
- [x] pin and cryptographically verify Node.js, runc, Git and libarchive signing authorities;
- [x] implement the host capability collector and identity finalizer;
- [x] add dependency, backend, signer and host-collector evidence to exact-head CI;
- [ ] produce a proof-eligible report from the exact pinned Ubuntu image/kernel revision;
- [ ] record the exact installed package manifest and package-artifact digests from that host;
- [ ] persist final evidence beyond temporary CI artifact retention;
- [x] owner acceptance of Apache License 2.0 and the public/private contribution boundary;
- [x] add accepted public `LICENSE`, `NOTICE`, contribution and security files;
- [ ] conduct the Phase 0C closure consistency review;
- [ ] accept ADR-0033;
- [ ] change `CURRENT_STATE.md` to `Runtime implementation: AUTHORIZED`.

## No-build boundary

- [x] scaffold remains non-claiming;
- [x] generated bindings remain metadata-only;
- [x] dependency, backend, signer and host evidence remain non-authorizing;
- [x] no Node, Workspace, Activity, Provider or UI runtime is claimed;
- [x] accepted public Apache-2.0 governance does not authorize runtime implementation;
- [x] donor/workload identity remains outside Ptah Core;
- [x] AI Project Workspace donor/profile remains non-operative, provider-independent and mechanically neutral;
- [x] WP13 and WP14 proof burdens remain unchanged;
- [ ] runtime implementation authorized.

---

# Implementation programme

No runtime package may become READY or ACTIVE before Phase 0C authorization.

## Programme P00 — Planning and authorization

- [x] P00 — Master-plan authority closure.
- [?] P01 — Physical-host and ADR-0033 closure; paused pending Phase 0C-19 acceptance, then blocked on the exact external host.

## Programme A — Online Ptah Alpha

- [ ] A01 — Repository, contracts and reproducible scaffold.
- [ ] A02 — Node identity, Generation and host truth.
- [ ] A03 — Ledger, schema versions and crash-safe migrations.
- [ ] A04 — Activity, Operation, Attempt, Event and Receipt runtime.
- [ ] A05 — Native process, PTY and multi-terminal Provider.
- [ ] A06 — Persistent Workspace, Session and authority projection.
- [ ] A07 — Object, Revision, Artifact, Location and local CAS.
- [ ] A08 — Upload and resumable download engine.
- [ ] A09 — Hardened Git Provider.
- [ ] A10 — OCI container Provider.
- [ ] A11 — Browser Provider.
- [ ] A12 — Archive decomposition Provider.
- [ ] A13 — Checkpoint, restart and verified recovery.
- [ ] A14 — Human Alpha control surface.
- [ ] A15 — Exact-head Online Ptah Alpha acceptance.

## Later programmes

- [ ] Programme B — Object World Beta.
- [ ] Programme C — Firmware and Device Beta.
- [ ] Programme D — Full Workspace Release.
- [ ] Programme E — Distributed Ptah.
- [ ] Programme F — OS-ready foundation private lane.

Detailed package dependencies, deliverables and proof gates are authoritative in `IMPLEMENTATION_ROADMAP.md`.

## Deep Workspace operations planning-load reconciliation

<!-- PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION -->

- [x] deep observable Workspace study merged into `Ptah-space` as `23dc4b19a0189ba55e08dfa124761efa806bd68b`;
- [x] 22 capabilities, 28 mappings, 20 fixtures and 26 original cases recovered;
- [x] no new Core entity and no WP01–WP14 reopening identified;
- [-] Phase 0C-19 canonical planning synchronization in review;
- [-] ADR-0037 proposed;
- [?] P01 paused until the reconciliation is accepted;
- [ ] confirm or supersede the provisional proof commit after acceptance;
- [ ] runtime implementation authorized.
