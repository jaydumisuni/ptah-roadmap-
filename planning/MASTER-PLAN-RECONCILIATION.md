# Ptah Master Plan reconciliation

Status: accepted reconciliation under Phase 0C-16 — runtime implementation remains unauthorized

Recorded: 2026-07-21

## Purpose

Prove that `MASTER_PLAN.md` and `IMPLEMENTATION_ROADMAP.md` recover and extend the accepted product programme without silently weakening frozen WP01–WP14 contracts, discarding Phase 0C evidence or introducing an unreviewed Core primitive.

## Reconciliation result

- Frozen WP01–WP14 contracts remain authoritative.
- The Master Plan introduces no new canonical Core entity family.
- The implementation roadmap consumes existing contracts through delivery packages and Providers.
- The AI Project Workspace remains a composition profile over existing primitives.
- The detailed roadmap adds product, operating, release and sequencing detail that was missing from the old architecture-level roadmap.
- No current plan item requires reopening WP01–WP14 before implementation authorization.
- Any implementation discovery that cannot be represented through the frozen contracts must stop and request a versioned reopening ADR, migration, fixtures and conformance evidence.

## WP01–WP14 mapping

| Frozen package | Master Plan responsibility | Primary roadmap packages | Reconciliation |
|---|---|---|---|
| WP01 — Common identity/versioning | canonical identity, typed families, versions, URNs, Aliases, retention and migrations | A01–A03; all X1 tracks | Preserved exactly; backend IDs remain non-canonical |
| WP02 — Activity/Operation/Attempt/Event/Receipt | concurrency, retry, cancellation, Events, Receipts and proof boundaries | A02, A04, A05, A08–A13; all programmes | Preserved; ACK, attempt and Activity truth remain separate |
| WP03 — Object/Revision/View/Artifact/storage | structured Object world, immutable bytes, Views, Artifacts, CAS and Locations | A07, A08, A12; B01–B07; C01–C07; D06 | Preserved; Content, Object and Artifact roles remain separate |
| WP04 — Node/Facility/Provider/capability/health | Node identity, Generation, Provider capability and replacement | A02, A05, A09–A13; E01–E07 | Preserved; health/readiness/reachability remain distinct |
| WP05 — Workspace/Session/checkpoint/recovery | persistent Workspace, Sessions, context, checkpoints and verified restore | A06, A13, A14; B06; D02; E04 | Preserved; checkpoint, restore and Recovery Verification remain separate |
| WP06 — Transfer/sync/conflict/backup | resumable transfer, sync, conflict, backup and restore | A08; B01; B06; E03, E06 | Preserved; sync/backup/recovery are not conflated |
| WP07 — Recipe/Build/provenance/SBOM/signature | build, recipes, deterministic execution and supply-chain proof | A09, A10, A15; D04, D06; F01–F05 | Preserved; build/signature do not equal release acceptance |
| WP08 — Domain/Firmware/Disk/Device | Domain Packs, progressive decomposition, firmware/disk/device boundaries | A12; B02–B05; C01–C11 | Preserved; static evidence never authorizes physical mutation |
| WP09 — Application/Browser/Semantic UI/Shell | Browser, Applications, semantic targets and human shell | A11, A14; C10; D01, D08; F06 | Preserved; UI projection never becomes runtime truth |
| WP10 — Knowledge/Data/Package/Plugin | search, indexes, datasets, packages and plugins | B07; D02–D05 | Preserved; indexes are derived and caller reasoning remains external |
| WP11 — Isolation/placement/reservation/lease/grants | explicit authority, isolation, Provider placement and distributed fencing | A02, A04–A13; D02, D05; E01–E07 | Preserved; no implicit global tools or silent isolation weakening |
| WP12 — Security/Finding/Claim/Evidence/reproduction | security authorization, bounded findings, remediation and reproduction | D07; X2/X3 in every programme | Preserved; scanner output and Claims remain bounded evidence |
| WP13 — executable conformance | structural, semantic, migration and exact-head validation | A01, A15; X1 in every package | Preserved as mandatory acceptance gate |
| WP14 — golden/negative corpus and proof freeze | positive, negative, adversarial and recovery proof | every work package; A15 release gate | Preserved; green summary without retained proof fails |

## Phase 0C work-package mapping

| Phase 0C record | Master Plan / roadmap use | State after reconciliation |
|---|---|---|
| 0C-01 first-slice proposal | baseline for Programme A and selected host/backends | Incorporated; superseded only in detail, not intent |
| 0C-02 host baseline pin | P01 physical-host closure and Alpha host identity | Retained exactly |
| 0C-03 direct dependency/licence record | A01 and provider source policy | Retained exactly |
| 0C-04 source layout/boundary | repository ownership, crate/service/adapter boundaries | Retained exactly |
| 0C-05 WP14 implementation/proof map | A01–A13 and A15 critical path | Incorporated as authoritative first-slice ordering |
| 0C-06 exact-head CI acceptance | universal work-package and release gate | Retained exactly |
| 0C-07 real workload registry | post-Alpha workload admission order | Incorporated in Programmes B/C |
| 0C-08 scaffold evidence | A01 starting evidence | Retained; does not claim runtime |
| 0C-09 immutable actions/frozen conformance | A01 and X1 supply-chain gate | Retained |
| 0C-10 frozen catalogs/generated bindings | A01 contract binding authority | Retained |
| 0C-11 dependencies/backends/signers/collector | selected first Providers and host collector | Retained |
| 0C-12 proof integrity/package artifacts | P01 physical proof eligibility | Retained |
| 0C-13 durable retention readiness | P01 durable host-bundle path | Retained |
| 0C-14 Apache-2.0 acceptance | public/private and contribution governance | Retained and operative |
| 0C-15 AI Project Workspace donor | D02 and A06 handoff/isolation requirements | Incorporated as non-Core composition profile |
| 0C-16 master-plan closure | plan, roadmap, reconciliation and recovery authority | This candidate package |

## Existing implementation task map reconciliation

The original fourteen Phase 0C tasks remain represented:

| Existing task | Detailed roadmap package |
|---|---|
| I001 repository/contract scaffold | A01 |
| I002 Node identity/Generation | A02 |
| I003 ledger/migrations | A03 |
| I004 Activity runtime | A04 |
| I005 PTY/multi-terminal | A05 |
| I006 persistent Workspace/Session | A06 |
| I007 Object/Revision/Artifact/CAS | A07 |
| I008 resumable transfer | A08 |
| I009 hardened Git | A09 |
| I010 OCI container | A10 |
| I011 Browser | A11 |
| I012 archive decomposition | A12 |
| I013 checkpoint/recovery | A13 |
| I014 exact-head acceptance | A15 |

A14 adds the direct human Alpha control surface required by the Master Plan and the existing Human Workspace law. It does not alter frozen identity or proof contracts.

## Product-scope additions supplied by the Master Plan

The previous roadmap already contained architecture and phase headings. The new plan makes the following previously implicit areas explicit:

- user and participant roles;
- Hunter, Sergeant, owner, operator and replaceable-agent responsibilities;
- complete product surfaces;
- online, local, hybrid, offline, distributed and private OS modes;
- service ownership and operational duties;
- API, SDK and integration surfaces;
- upgrade, rollback and security responsibilities;
- source-authority and context-compiler behavior;
- release milestones and promotion rules;
- measurable success criteria;
- exact product definition of done;
- detailed work-package dependencies and evidence gates.

These additions are planning and composition detail. They do not change canonical entity families.

## Conflict review

### Ptah versus Hunter

No conflict. Ptah owns durable world state and evidence. Hunter supplies intent interpretation and coordination through Grants and bounded context.

### Public versus private

No conflict. Public Ptah remains generic and Apache-2.0. Private Domain Packs, restricted adapters, customer/device/payment data and Hunter private memory remain outside public source.

### Online versus local

No conflict. The same contracts and identities apply. Deployment and Provider differences remain explicit.

### Human versus automation authority

No conflict. Human and software participants use the same Grant, Lease, Fence, Activity and Receipt boundaries. UI or model output cannot silently promote authority.

### Roadmap versus frozen first-slice proof

No conflict. Programme A preserves the fourteen-task critical path and adds a human control-surface package without reducing proof.

## Missing-contract review

Current planning found no required new Core primitive.

The following are implementation/composition concerns rather than new entity families:

- Workspace source-authority service;
- context packet compiler;
- Artifact Library views;
- human shell navigation and panels;
- operator dashboards;
- deployment profiles;
- release milestones;
- service ownership.

If implementation proves any of these cannot be represented by Workspace, Policy, Grant, Knowledge, View, Artifact, Session, Activity, Event, Recipe and Receipt contracts, the affected package must stop and open a versioned reopening ADR.

## Stale control records requiring repair

The Phase 0C-16 merge must update:

- root `README.md` current position and recovery order;
- `MEMORY_PROTOCOL.md` recovery order and save-as-you-go rules;
- `DECISIONS.md` with WP08–WP14, Phase 0B freeze, Phase 0C, licence and plan-authority decisions;
- `DONOR_RECOVERY.md` status from active review to frozen donor closure;
- `MASTER_ROADMAP.md` status and supersession relationship;
- `PROGRESS.md` with P00/P01 and Programme A–F ledger;
- `CURRENT_STATE.md` with the exact planning branch, completed checkpoints and next action.

## Remaining authorization blockers

This reconciliation does not close:

1. plan/roadmap review and merge;
2. physical pinned-host proof;
3. package and package-artifact review acceptance;
4. durable physical-host bundle acceptance;
5. final Phase 0C consistency review;
6. ADR-0033 acceptance;
7. explicit runtime authorization.

Runtime implementation remains **NOT AUTHORIZED**.

## Phase 0C-19 deep Workspace operations reconciliation

<!-- PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION -->

The deep study maps to frozen WP02–WP07, WP09–WP11, WP13 and WP14. No new canonical family is required.

| Deep requirement | Frozen authority | Roadmap load |
|---|---|---|
| typed operation/effect metadata | WP02, WP04, WP07, WP11 | A01, A04, D04, X1 |
| Provider access / Grant / approval separation | WP02, WP04, WP11 | A04, A14, D01, D02, X2 |
| reference / materialization truth | WP03, WP04, WP06 | A07, A08, A11, B01, X2 |
| progress, partial output and result states | WP02, WP03, WP05 | A04, A13, A14, X3 |
| stable large-result handles | WP03, WP05, WP10 | A06–A08, B06, B07, D03 |
| typed render-independent Views | WP03, WP09 | A14, D01, D02, X4 |
| schedule kind/timing and exact inputs | WP02, WP05, WP07, WP11 | A04, A06, A13, A14, D04 |
| exact revision/head preconditions | WP01–WP03, WP07, WP11 | A04, A09, A11, A13, X1 |
| permission-aware retrieval/freshness | WP04, WP05, WP10, WP11 | B07, D02, D03, E06 |
| cross-interface/Node continuity | WP03–WP06, WP11 | A06, A13, B06, E04–E07, X5 |

The profile's enumerations and operation metadata are composition/conformance requirements, not new entity families. Any contrary implementation discovery triggers the existing versioned reopening rule.

The earlier P01 candidate selection is provisional until this reconciliation is accepted.
