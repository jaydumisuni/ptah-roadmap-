# Ptah Accepted Decisions

This file is the compact index of decisions that must not be silently reversed. Full architecture, limitations, donor boundaries and proof requirements live in the referenced ADRs.

---

## D-001 — Ptah is independent

**Status:** ACCEPTED

Ptah is a neutral open-source working world. Private consumers integrate through public-safe contracts rather than defining Ptah's identity.

## D-002 — Ptah is the world, not the thinker

**Status:** ACCEPTED

Ptah supplies environments, Objects, Activities, tools, applications, devices, browsers, storage and evidence. Callers supply intent, reasoning, policy and acceptance.

## D-003 — Roadmap and implementation are separate

**Status:** ACCEPTED

`ptah-roadmap-` owns private planning/recovery. `Ptah-space` owns public implementation and earned public progress.

## D-004 — Online first, local later, same contracts

**Status:** ACCEPTED

Online, local mini-PC and future OS deployments reuse the same identities, contracts and data model.

## D-005 — Workspace and Activity are different

**Status:** ACCEPTED

A Workspace persists while many unrelated Activities run, pause, fail, recover and complete inside it.

## D-006 — Object-first architecture

**Status:** ACCEPTED

Original bytes remain immutable Objects with hashes, locations, provenance, relationships, Views and derivatives.

## D-007 — Domain Packs

**Status:** ACCEPTED

Specialist formats use versioned detect, inventory, decompose, preview, transform, validate, compare, rebuild and execute contracts.

## D-008 — Internet is normally available

**Status:** ACCEPTED

Internet access behaves like an operating-environment capability. Restrictions come from caller, Workspace, provider or deployment configuration.

## D-009 — Storage is layered

**Status:** ACCEPTED

Fast local storage performs active work; Object storage retains durable bytes; Git owns source history; SQL owns metadata; Drive is export/recovery.

## D-010 — Integration first, not greenfield pride

**Status:** ACCEPTED

Every subsystem begins with internal recovery, donor inspection, mature machinery and identification of the true native Ptah gap.

## D-011 — Polyglot operational chassis

**Status:** ACCEPTED

Rust is preferred where valuable, while mature tools in other languages remain behind stable adapters.

## D-012 — Evidence before completion

**Status:** ACCEPTED

Source presence and optimistic UI claims are not proof. Completion requires frozen records, live evidence, hashes, limitations and retained negative results.

## D-013 — No work before placement and approval

**Status:** ACCEPTED

Ideas are preserved, placed, dependency-ordered and approved before implementation.

## D-014 — Engineering cycle

**Status:** ACCEPTED

Understand → Build → Review → Freeze → Prove → Submit/Ship.

## D-015 — Public Ptah remains neutral

**Status:** ACCEPTED

Public source must not expose private consumers, workflows, credentials, topology, customer data or unpublished company decisions.

## D-016 — Operating-system assembly is a later private lane

**Status:** ACCEPTED

Ptah stays OS-neutral. The future distribution/boot/update/hardware layer is decided after the online and Node substrate is proven.

## D-017 — Composite donor closure

**Status:** ACCEPTED

No subsystem closes through one repository. Closure combines internal foundation, primary donor, completion donors, mature machinery, native contracts, exit strategy and proof.

Full decision: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

## D-018 — Activity, Event and observability remain separate

**Status:** ACCEPTED

Ptah owns the Activity Ledger. Temporal, NATS/JetStream, OpenTelemetry, large streams and proof receipts have different guarantees.

Full decision: `decisions/ADR-0003-ACTIVITY-EVENT-OBSERVABILITY-BOUNDARY.md`.

## D-019 — Operation state, evidence and authority levels remain separate

**Status:** ACCEPTED

Activity state, attempts, Events, telemetry, Receipts, Artifact proof, review and authoritative external results are distinct. Stale or unverified evidence never becomes PASS.

Full decision: `decisions/ADR-0004-OPERATION-RECEIPTS-PROOF-LEVELS.md`.

## D-020 — Build, Artifact and provenance remain separate

**Status:** ACCEPTED

Build Recipe, execution graph, Artifact graph, SBOM, attestation, signature, review, reproduction and release acceptance are separate layers.

Full decision: `decisions/ADR-0005-BUILD-ARTIFACT-PROVENANCE-BOUNDARY.md`.

## D-021 — Storage, transfer, synchronization and backup remain separate

**Status:** ACCEPTED

Hot Workspace bytes, immutable Objects, revisions, caches, partial transfers, replicas, backups and exports have different guarantees.

Full decision: `decisions/ADR-0006-STORAGE-TRANSFER-SYNC-BOUNDARY.md`.

## D-022 — Object identity, detector claims, Views and rebuilds remain separate

**Status:** ACCEPTED

Originals remain immutable; detector disagreements are retained; decomposition is bounded; children, Views, previews, transformations, decompilations and rebuilds carry explicit origin.

Full decision: `decisions/ADR-0007-OBJECT-GRAPH-DECOMPOSITION-DERIVATIVE-BOUNDARY.md`.

## D-023 — Firmware packages, disk images and physical operations remain separate

**Status:** ACCEPTED

Static analysis does not authorize physical mutation. Device presence, protocol stages, loaders/programmers, write acknowledgement and read-back are distinct proof levels.

Full decision: `decisions/ADR-0008-DISK-FIRMWARE-DEVICE-OPERATION-BOUNDARY.md`.

## D-024 — Device identity, lease, display, input and semantic UI remain separate

**Status:** ACCEPTED

Ptah owns stable Device identity, interface epochs, Provider generation, leases/fencing, Device Sessions, streams and semantic contexts. Backend IDs are aliases; cleanup is verified.

Full decision: `decisions/ADR-0009-DEVICE-SESSION-DISPLAY-INPUT-SEMANTIC-UI-BOUNDARY.md`.

## D-025 — Application Provider, Window, display gateway and semantic context remain separate

**Status:** ACCEPTED

Application Object, Provider, Installation, Session, Process, Window, display, semantics and checkpoint state are distinct across Linux, Windows, macOS and mobile runtimes.

Full decision: `decisions/ADR-0010-APPLICATION-PROVIDER-WINDOW-DISPLAY-BOUNDARY.md`.

## D-026 — Browser Profile, Process, Context, Page and evidence remain separate

**Status:** ACCEPTED

Playwright is the primary Browser foundation. Profiles, processes, Contexts, Pages, downloads, source Views, evidence and research claims retain separate identities and privacy/recovery rules.

Full decision: `decisions/ADR-0011-BROWSER-PROFILE-CONTEXT-PAGE-EVIDENCE-BOUNDARY.md`.

## D-027 — Human Workspace shell, Panels, Layout and control ownership remain separate

**Status:** ACCEPTED

Ptah owns Shell Client, Shell Session, Panel Type/Instance, Layout Profile/Revision and control-lease identities.

- Eclipse Theia is the primary full desktop/workbench foundation, not Ptah Core or the universal phone shell.
- Dockview is the primary lighter responsive layout candidate; phones use compact single-primary-panel navigation rather than free-form docking.
- OpenVSCode Server and code-server are optional coding Applications.
- xterm.js is a terminal renderer over Ptah PTY Sessions.
- UI state and layout restoration never imply runtime recovery.
- Activity Centre and Evidence Explorer project live records and exact proof levels.
- Settings and operational controls remain separate.
- Human/automation control uses scoped leases, fencing and receipted takeover/return.
- Specialist UIs remain valid products and are not replaced merely because Ptah gains a shared shell.
- Hunter Foreman is excluded from active shell composition unless explicitly reintroduced.

Full decision: `decisions/ADR-0012-HUMAN-WORKSPACE-SHELL-PANEL-CONTROL-BOUNDARY.md`.

## D-028 — Knowledge source, indexes, queries, data and plugins remain separate

**Status:** ACCEPTED

Ptah owns neutral Knowledge Source, Corpus, Document Revision, Chunk, Index Revision, Query, Result, Citation, Dataset, Table, Package Release, Installed Plugin and Activation identities.

- Conversation, source knowledge, derived indexes and caller-owned memory are different truth classes.
- Source Objects and exact revisions are authoritative; embeddings, indexes, summaries and caches are derived and rebuildable.
- Query, ranking Result and exact Citation remain separate.
- Permissions apply during source acquisition, retention, embedding, indexing, retrieval, citation, export and deletion.
- LlamaIndex is the primary modular local knowledge-foundation candidate; RAGFlow is an optional heavier Knowledge Facility.
- Polars and DuckDB are analytical engines behind Ptah Dataset/Query/Result contracts, not universal transactional stores.
- Package, immutable Package Release, Installed Plugin, Activation and Registry Entry remain separate.
- Registry presence, verification, scans and manifest claims are evidence inputs, not approval or runtime proof.
- Deno is the lightweight permission-scoped tool-runtime candidate; native, FFI, untrusted or broad-privilege code escalates to OCI or VM isolation.
- MCP is one external adapter protocol, not Ptah's internal Object or Activity model.
- Hunter, Hermes, Dify, OpenClaw and future systems remain external callers or Applications that own reasoning, memory and relationship policy.
- Dify requires separate licence treatment; MiniRouter remains study-only until its licence is resolved.

Full decision: `decisions/ADR-0013-KNOWLEDGE-DATA-SEARCH-PLUGIN-BOUNDARY.md`.

## D-029 — Isolation Class, runtime, placement, reservation and proof remain separate

**Status:** ACCEPTED

Ptah owns the Isolation Class, Runtime Provider, Node Capability Snapshot, Placement Request/Decision, Reservation, Lease, Generation, Fence, secure grants and Checkpoint Bundle.

- Baseline OCI, gVisor, Kata, Firecracker and full VM are distinct runtime classes with explicit compatibility and threat boundaries.
- runc, crun and youki remain replaceable implementations below one OCI Provider contract.
- Rootless and memory-safe implementation are useful properties, not stronger containment classes.
- Incompatible work may escalate to an equal or stronger approved class or be blocked; Ptah never silently falls back to weaker isolation.
- Placement filters hard feasibility before scoring locality, pressure, accelerator fit, cost, failure domain and interruption risk.
- Placement selection, Reservation, Lease, workload Generation and fencing token are separate records.
- Network, Objects, devices and credentials require exact workload-generation grants.
- Checkpoint creation, restore compatibility and application recovery are separate proof levels.
- Ray is an optional trusted distributed Compute Facility behind Ptah Activities and placement, not the global scheduler or Object truth.
- Mutually untrusted Ray workloads use separate isolated clusters.
- MiniRouter remains an optional evaluation workload, not a Ptah routing authority.

Full decision: `decisions/ADR-0014-ISOLATION-RUNTIME-PLACEMENT-SCHEDULING-BOUNDARY.md`.

## D-030 — Linux semantic target, snapshot, actions, raw input and proof remain separate

**Status:** ACCEPTED

Ptah owns provider-neutral Semantic Provider, Snapshot, Target, Selector, Event, Action and proof identities for Linux Application Sessions.

- AT-SPI/libatspi is the primary Linux semantic tree/state/action provider foundation.
- D-Bus names, object paths, AccessibleIds and child indices remain provider-local observations rather than stable Ptah identities.
- targets are reacquired against current Application, Window and provider generations before mutation.
- bulk snapshots, events and reconciliation remain separate sources of semantic state.
- selector ambiguity and stale/defunct references are explicit.
- semantic inspection, semantic mutation, raw pointer/keyboard, clipboard and visual automation are separate permission classes.
- X11, GNOME Wayland/Ponytail and unsupported compositor input paths remain distinct.
- semantic action protocol success requires semantic and/or visual post-condition read-back.
- mutually untrusted Workspaces do not share one privileged accessibility session.
- opaque or incomplete UIs degrade explicitly to semantic-partial or visual-only behavior.
- Dogtail and Accerciser remain optional testing/inspection Applications; future accessibility providers remain replaceable.

Full decision: `decisions/ADR-0015-LINUX-APPLICATION-SEMANTIC-AUTOMATION-BOUNDARY.md`.

## D-031 — Security Observation, Finding, validation, reproduction and acceptance remain separate

**Status:** ACCEPTED

Ptah owns exact Security Assessment Authorization, Assessment Plan, Target Revision, Scanner/Rule/Database/Protocol Revision, Coverage, Finding Observation, Correlated Finding, disposition, remediation, Verification Run, Reproduction Run, Claim boundary and Evidence Card identities.

- static, inventory, vulnerability, configuration, secret, passive, active, exploit and agent-originated observations remain distinct.
- no-findings results require exact coverage, skipped scope and errors.
- scanner severity/confidence, exploitability, business impact, remediation priority, release policy and acceptance remain separate.
- false-positive, not-affected, accepted-risk and suppression dispositions never erase original evidence and may expire.
- active/fuzz/exploit/agentic work requires explicit target authority, isolation, network/credential budgets, stop and cleanup/read-back.
- Semgrep, Syft/Grype, Trivy, GUAC and ZAP are complementary Facilities rather than one universal scanner.
- Strix is an optional authorized offensive-validation workload, not a security authority or independent reviewer.
- ReproZip captures one environment/replay class and does not prove universal portability or independent reproduction.
- ClaimBound-style cards are bounded Views over Ptah Claims/Activities/Artifacts, not certification.
- SparkDistill is an optional specialist AI-reproduction workload; recipe, dataset, checkpoint, metric claim, attestation and recheck remain separate.
- remediation remains a proposal until correct ownership, re-test and independent review.
- Result, Reproduction, Verification, Review and Acceptance levels remain separate, including negative, blocked, drift and inconclusive outcomes.

Full decision: `decisions/ADR-0016-SECURITY-FINDING-VALIDATION-REPRODUCTION-BOUNDARY.md`.
