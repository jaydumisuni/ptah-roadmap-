# Ptah Progress Ledger

Tick only work backed by source inspection, pinned commits, accepted decisions, tests or live evidence.

- `[ ]` Not started
- `[-]` Active
- `[?]` Blocked/unresolved
- `[x]` Completed and evidenced

---

# Phase 0A — Donor recovery and requirement closure

**Status:** COMPLETE AND FROZEN AT `7d2dffee48f1400ba1cf88823343f09a3895ad33`

## Repository and method control

- [x] Private roadmap repository and public/private separation.
- [x] Master roadmap, Current State, progress and recovery rules.
- [x] Requirement Closure Matrix and donor/internal-record structure.
- [x] ADR-0001 through ADR-0017 accepted and indexed.
- [x] Remaining donor register and unresolved-profile cleanup.
- [x] Cross-requirement identity/authority/state/lifecycle review.
- [x] Parked/restricted gap audit.
- [x] Phase 0B schema, conformance and proof-corpus inputs enumerated.
- [x] Phase 0A freeze/readiness decision.

## Closed clusters

### WP01–WP02 — Core runtime

- [x] Node/Workspace boundary.
- [x] Workspace/provider execution composition.
- [x] Activities, Events, recovery and observability.
- [x] Internal runtime/evidence comparison.
- [x] Phase 0B design closure.

### WP03 — Build, Artifact and provenance

- [x] BuildKit/Dagger and internal Builder comparison.
- [x] ORAS, SBOM, attestation, signing and reproduction boundaries.
- [x] ADR-0005 and WP03.
- [x] Phase 0B design closure.

### WP04 — Storage, transfer, synchronization and backup

- [x] Lumi, aria2, tusd, rclone, Syncthing and restic.
- [x] local CAS/catalogue and revision/conflict direction.
- [x] distributed shared filesystems evaluated and parked.
- [x] ADR-0006 and WP04.
- [x] Phase 0B design closure.

### WP05 — Universal Object and decomposition

- [x] internal recovery/decomposition products.
- [x] archive/document/binary/Android/image/media/source donors.
- [x] ADR-0007 and WP05.
- [x] Phase 0B design closure.

### WP06 — Firmware, disks and filesystems

- [x] Apple, MTK, Qualcomm, Unisoc, Android OTA and Samsung composition.
- [x] libguestfs/libfdisk and isolated disk/filesystem boundary.
- [x] P5C parked with reopening criteria.
- [x] ADR-0008 and WP06.
- [x] Phase 0B design closure.

### WP07 — Device and Application Runtime

- [x] Android Device Provider, ADB/Fastboot, display/input and semantic UI.
- [x] Linux, Windows, macOS and iOS Application Providers.
- [x] remote display, VM, Window and Application Session boundaries.
- [x] Linux AT-SPI/libatspi semantic tree, actions, text, value, selection, event and GNOME-Wayland input completion.
- [x] semantic snapshot/target/selector/action/read-back and privacy boundary.
- [x] ADR-0009, ADR-0010, ADR-0015, WP07A/WP07B and Linux semantic completion work package.
- [x] Phase 0B design closure.

### WP08 — Browser and Live Research

- [x] Playwright, Playwright MCP, Browser-Use and TurboWebFetch.
- [x] Profile/Process/Context/Page/Download/Evidence model.
- [x] source/citation and challenge/human-completion model.
- [x] ADR-0011 and WP08.
- [x] Phase 0B design closure.

### WP09 — Human Workspace Shell and Operator Interface

- [x] Eclipse Theia, Dockview, xterm.js and optional coding Applications.
- [x] internal Hunter/Sergeant/MIBU/Device Manager/website UI patterns.
- [x] Ptah Home, Workspace switcher, Panel, Activity Centre and Evidence Explorer direction.
- [x] human/automation focus and fenced control handoff.
- [x] responsive desktop/tablet/phone and accessibility requirements.
- [x] ADR-0012 and WP09.
- [x] Phase 0B design closure.

### WP10 — Knowledge, Data, Search and Plugin Composition

- [x] Hunter knowledge/memory/search/provider foundations.
- [x] RAGFlow, LlamaIndex, Dify, Polars, DuckDB and Deno boundaries.
- [x] MCP and OpenClaw/ClawHub adapter/registry patterns.
- [x] Knowledge Source/Corpus/Document/Chunk/Index/Query/Result/Citation model.
- [x] Dataset/Table/Schema/Query/Transformation/Result model.
- [x] Package/Release/Installed Plugin/Activation lifecycle.
- [x] MiniRouter classified as optional future evaluation workload pending licence.
- [x] ADR-0013 and WP10.
- [x] Phase 0B design closure.

### WP11 — Strong Isolation and Distributed Placement/Scheduling

- [x] gVisor, Kata, Firecracker, youki, crun and Ray.
- [x] isolation-class and no-silent-weakening model.
- [x] Node/provider capability and resource snapshots.
- [x] Placement, Candidate/Decision, Reservation, Lease, Generation and Fence.
- [x] secure network/Object/device/credential grants.
- [x] interruption, checkpoint, restore and rescheduling behavior.
- [x] one-Node/multi-Node contract.
- [x] ADR-0014 and WP11.
- [x] Phase 0B design closure.

### Security Assessment and Reproduction Workloads

- [x] ReproZip, ClaimBound, SparkDistill, Syft, Grype, GUAC, Semgrep, Trivy, ZAP and Strix.
- [x] Security Authorization, Plan, exact Target, machinery revision and Coverage.
- [x] Finding Observation, Correlated Finding, risk/disposition/remediation/re-test model.
- [x] Protocol Revision, Reproduction Run and bounded Evidence Card model.
- [x] active/offensive isolation, network, credential, stop and cleanup boundary.
- [x] `SEC-001` and `REPRO-001` design closure.
- [x] ADR-0016 and security/reproduction work package.

### Research, documentation and source cleanup

- [x] research catalogue and discovery profiles resolved/classified.
- [x] Chris/Christiam Ipanaque identity resolved; prototype reuse parked pending licence/proof.
- [x] `amertoglu16.github.io` parked with reopening criteria.
- [x] Crisp Links, MkDocs Material, Docusaurus and Mermaid pinned/classified.
- [x] public/private documentation build boundary recorded.
- [x] cleanup work package committed.

### Cross-requirement consistency and freeze

- [x] Object versus Artifact normalized.
- [x] Activity/Operation/Attempt and Event/Telemetry/Receipt/Evidence normalized.
- [x] Provider/Session/Lease/Event/Revision/Snapshot typed-family rule accepted.
- [x] namespaced state-machine rule accepted.
- [x] Claim/Observation/Finding/Review/Acceptance relationships normalized.
- [x] Recipe/Plan/Protocol/Run relationships normalized.
- [x] lifecycle/deletion/tombstone rules enumerated.
- [x] parked/restricted gaps confirmed non-blocking.
- [x] public `Ptah-space` checked and confirmed no implementation conflict.
- [x] Phase 0B entry inputs/golden/negative corpus enumerated.
- [x] ADR-0017 accepted; Phase 0A frozen.

## Requirement closure

- [x] Core runtime.
- [x] Build/Artifact/Provenance.
- [x] Storage/Transfer/Sync/Backup.
- [x] Object/Decomposition.
- [x] Firmware/Disk/Filesystem.
- [x] Device/Application Runtime.
- [x] Browser/Live Research.
- [x] Human Workspace/UI.
- [x] Knowledge/Data/Search/Plugin.
- [x] Isolation/Distributed placement.
- [x] Security/reproduction workloads.
- [x] Phase 0A review and freeze.

Evidence:

- `work-packages/PHASE-0A-CROSS-REQUIREMENT-CONSISTENCY-REVIEW.md`
- `work-packages/PHASE-0B-ENTRY-CONTRACT-PROOF-INPUTS.md`
- `decisions/ADR-0017-PHASE-0A-FREEZE-PHASE-0B-ENTRY.md`

---

# Phase 0B — Contracts, migrations, conformance and proof design

**Status:** ACTIVE — IMPLEMENTATION STILL NOT AUTHORIZED

## Ordered work packages

- [-] 0B-WP01 — Common identity, versioning and typed-family conventions.
- [ ] 0B-WP02 — Activity, Operation, Attempt, Event, Receipt and proof.
- [ ] 0B-WP03 — Object, Revision, View, Artifact and storage relationships.
- [ ] 0B-WP04 — Node, Facility, Provider, capability and health.
- [ ] 0B-WP05 — Workspace, Session, checkpoint and recovery.
- [ ] 0B-WP06 — Transfer, sync, conflict and backup.
- [ ] 0B-WP07 — Recipe, Build, provenance, SBOM, signature and verification.
- [ ] 0B-WP08 — Domain Pack, firmware, disk and Device contracts.
- [ ] 0B-WP09 — Application, Browser, semantic UI and Shell contracts.
- [ ] 0B-WP10 — Knowledge, data, Package and Plugin contracts.
- [ ] 0B-WP11 — Isolation, placement, reservation, lease and secure grants.
- [ ] 0B-WP12 — Security, Finding, Claim, Evidence and reproduction contracts.
- [ ] 0B-WP13 — Cross-contract migrations and conformance harness.
- [ ] 0B-WP14 — Golden/negative corpus and proof-plan freeze.
- [ ] Phase 0B review/freeze and Phase 0C readiness decision.

## Cross-cutting Phase 0B gates

- [ ] every schema versioned and traceable to ADR/requirement;
- [ ] state machines/transitions explicit and namespaced;
- [ ] saved records/sessions have migration paths;
- [ ] permissions, audience and redaction represented;
- [ ] Provider/Facility conformance contracts defined;
- [ ] lawful golden and negative fixtures pinned;
- [ ] proof plans name exact Receipts/Evidence;
- [ ] backend replacement testable;
- [ ] online and later local Nodes use the same contracts;
- [ ] private consumer knowledge absent from public schemas;
- [ ] public licence/dependency strategy ready for Phase 0C;
- [ ] first vertical slice selectable without identity/proof ambiguity.

---

# Phase 0C — First vertical slice approval

- [ ] Select Linux host and exact components.
- [ ] Select public project licence and dependency/source layout.
- [ ] Approve implementation proof plan.
- [ ] Record implementation authorization in `CURRENT_STATE.md`.

# Implementation phases

- [ ] Phase 1 — Concurrent one-Node substrate.
- [ ] Phase 2 — Intake and transfer.
- [ ] Phase 3 — Universal decomposition.
- [ ] Phase 4 — Firmware, disks and filesystems.
- [ ] Phase 5 — Git, containers, environments and Builds.
- [ ] Phase 6 — Browser and live web.
- [ ] Phase 7 — Human Workspace shell.
- [ ] Phase 8 — Session Vault.
- [ ] Phase 9 — Applications and devices.
- [ ] Phase 10 — Knowledge, data, search, recipes and plugins.
- [ ] Phase 11 — Provenance and security workloads.
- [ ] Phase 12 — Distributed Ptah.
- [ ] Phase 13 — OS readiness.
