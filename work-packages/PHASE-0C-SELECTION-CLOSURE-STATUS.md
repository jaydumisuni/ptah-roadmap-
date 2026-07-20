# Phase 0C — Selection closure status

Status: active — scaffold and CI preparation complete; runtime implementation remains unauthorized

Updated: 2026-07-20

## Completed candidate and evidence records

- `work-packages/PHASE-0C-01-FIRST-SLICE-SELECTION-PROPOSAL.md`
- `work-packages/PHASE-0C-02-HOST-IMAGE-AND-CAPABILITY-PIN.md`
- `dependencies/PHASE-0C-FIRST-SLICE-EXTERNAL-DEPENDENCY-AND-LICENCE-MATRIX.md`
- `dependencies/PHASE-0C-GITHUB-ACTION-IMMUTABLE-PINS.md`
- `work-packages/PHASE-0C-03-FIRST-SLICE-TASK-GRAPH-TO-WP14-PROOFS.md`
- `conformance/phase-0c/FIRST-SLICE-EXACT-HEAD-CI-GATE.md`
- `work-packages/PHASE-0C-04-SCAFFOLD-AND-CI-EVIDENCE-REVIEW.md`

## ADR-0033 condition status

| Condition | Status | Evidence / remaining work |
|---|---|---|
| Owner accepts public licence and contribution boundary | OPEN | Apache-2.0 remains a recommendation only. No public licence file or package licence field may claim acceptance yet. |
| Exact host image and kernel capability profile | CANDIDATE COMPLETE | Ubuntu Server 24.04.4 amd64 ISO is digest-pinned; installed kernel/package identity is measured per Node generation; mandatory host capability profile is defined. |
| Implementation source layout and non-claiming scaffold | COMPLETE | `Ptah-space` scaffold merged at `ff26fa93d1b60781b49f33f5d1758680e1282d5f`; it contains 17 Rust package boundaries and a private Browser scaffold while explicitly keeping runtime unauthorized. |
| Exact dependency versions and licences | PARTIAL | External tool/backend candidates, zero-dependency Rust scaffold graph, Browser npm lock and action SHAs are pinned. Runtime Rust crates, installed host/backend digests and Chromium executable evidence remain open. |
| Task graph mapped to WP14 proof cases | CANDIDATE COMPLETE | T00–T13 map P01–P15 and N01–N12 to implementation tasks and required evidence. |
| CI includes Rust, Browser, source-policy and frozen WP13 conformance | COMPLETE FOR SCAFFOLD | Exact-head run `29717942201` passed all four jobs and retained four digest-addressed artifacts; hardening merged at `23fc97ff0acd2b219990411ec4fb84d8a8c0a567`. |
| Exact installed host/browser acceptance evidence | OPEN | Requires an admitted Ubuntu Node, package/kernel inventory, mandatory capability-probe result, installed backend digests and Chromium executable/notices. |
| Final Phase 0C review and ADR-0033 acceptance | BLOCKED | Awaiting owner licence decision and the remaining runtime dependency/installed-environment evidence. |
| Explicit runtime authorization in `CURRENT_STATE.md` | BLOCKED | May occur only after every prior condition is accepted and ADR-0033 changes to accepted. |

## Scaffold evidence summary

Implementation repository: `jaydumisuni/Ptah-space`

- broader non-claiming scaffold merge: `ff26fa93d1b60781b49f33f5d1758680e1282d5f`;
- evidence-hardening tested head: `900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc`;
- evidence-hardening merge: `23fc97ff0acd2b219990411ec4fb84d8a8c0a567`;
- exact-head workflow run: `29717942201`;
- source-policy, Rust scaffold, Browser scaffold and frozen-conformance jobs: passed;
- runtime implementation authorization in all evidence: false.

The passing scaffold does not satisfy the WP14 runtime proof plan. It proves only that the selected repository layout, locks, no-build boundary and contract-conformance gate are viable.

## Deferred workload candidates

The following repositories were reviewed as useful future workloads/donors but are not selected Phase 0C dependencies yet:

- `jaydumisuni/linux-0.11-rs` — candidate reproducible OS/image/QEMU workload and selective image-tool donor;
- `jaydumisuni/MIBU` — candidate internal Device/Application proof workload;
- `jaydumisuni/thetechguy-device-manager` — candidate Android Device Owner/policy workload;
- `jaydumisuni/TTG-Device-X-Ray` — candidate internal WP08 Detector/Evidence producer.

They may be added after their interfaces, licences, exact commits and proof roles are reviewed. Their application-specific identity must not enter Ptah Core.

## Immediate continuation

1. define the minimal runtime Rust dependency candidates and exact features per T01–T06 without writing runtime behaviour;
2. generate and review the amended `Cargo.lock`, licence and advisory reports;
3. prepare the Ubuntu Node admission/capability probe and exact package inventory procedure;
4. prepare installation/digest evidence for SQLite, containerd, runc, Git and libarchive;
5. prepare the controlled Playwright browser installation and executable/notice evidence;
6. obtain owner decision on Apache-2.0 or an amended public/private boundary;
7. conduct the final Phase 0C consistency and licence review;
8. accept or amend ADR-0033;
9. explicitly authorize implementation in `CURRENT_STATE.md`;
10. begin T01 only from the accepted authorization commit.

## No false closure

- external dependency pins do not mean the binaries were installed or tested;
- empty scaffold crates do not constitute runtime implementation;
- Browser package installation without Chromium does not prove Browser execution;
- a green scaffold CI run does not satisfy WP14 implementation proofs;
- retained artifacts currently have finite CI retention and final acceptance evidence needs a durable Location;
- Phase 0C remains active until owner and installed-environment/runtime-dependency gates are merged.