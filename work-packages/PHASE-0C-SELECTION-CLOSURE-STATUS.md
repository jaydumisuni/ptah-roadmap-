# Phase 0C — Selection closure status

Status: active — runtime implementation remains unauthorized

Updated: 2026-07-20

## Completed candidate records

- `work-packages/PHASE-0C-01-FIRST-SLICE-SELECTION-PROPOSAL.md`
- `work-packages/PHASE-0C-02-HOST-IMAGE-AND-CAPABILITY-PIN.md`
- `dependencies/PHASE-0C-FIRST-SLICE-EXTERNAL-DEPENDENCY-AND-LICENCE-MATRIX.md`
- `work-packages/PHASE-0C-03-FIRST-SLICE-TASK-GRAPH-TO-WP14-PROOFS.md`
- `conformance/phase-0c/FIRST-SLICE-EXACT-HEAD-CI-GATE.md`

## ADR-0033 condition status

| Condition | Status | Evidence / remaining work |
|---|---|---|
| Owner accepts public licence and contribution boundary | OPEN | Apache-2.0 remains a recommendation only. No public licence file or package licence field may claim acceptance yet. |
| Exact host image and kernel capability profile | CANDIDATE COMPLETE | Ubuntu Server 24.04.4 amd64 ISO is digest-pinned; installed kernel/package identity is measured per Node generation; mandatory host capability profile is defined. |
| Exact dependency versions and licences | PARTIAL | External toolchain/backend candidates are pinned. Direct Rust crates, features, lockfile, action SHAs, exact installed Ubuntu package versions and browser executable digest remain open. |
| Task graph mapped to WP14 proof cases | CANDIDATE COMPLETE | T00–T13 map P01–P15 and N01–N12 to implementation tasks and required evidence. |
| CI includes Rust, WP13 and frozen proof-plan execution | DESIGN COMPLETE / IMPLEMENTATION OPEN | Exact-head CI contract is defined. It must be implemented and pass on a `Ptah-space` scaffold commit. |
| Explicit runtime authorization in `CURRENT_STATE.md` | BLOCKED | May occur only after every prior condition is accepted and ADR-0033 changes to accepted. |

## Deferred workload candidates

The following repositories were reviewed as useful future workloads/donors but are not selected Phase 0C dependencies yet:

- `jaydumisuni/linux-0.11-rs` — candidate reproducible OS/image/QEMU workload and selective image-tool donor;
- `jaydumisuni/MIBU` — candidate internal Device/Application proof workload;
- `jaydumisuni/thetechguy-device-manager` — candidate Android Device Owner/policy workload;
- `jaydumisuni/TTG-Device-X-Ray` — candidate internal WP08 Detector/Evidence producer.

They may be added after their interfaces, licences, exact commits and proof roles are reviewed. Their application-specific identity must not enter Ptah Core.

## Immediate continuation

1. create a non-runtime Phase 0C scaffold branch in `jaydumisuni/Ptah-space`;
2. pin Rust 1.97.1 and the accepted source layout;
3. generate the minimum direct crate graph and committed `Cargo.lock` without implementing runtime behaviour;
4. add dependency/licence/advisory policy;
5. implement exact-head CI with immutable action pins;
6. run the scaffold CI and retain reports;
7. review the resulting crate/action/package inventory;
8. obtain owner decision on Apache-2.0 or an amended public/private boundary;
9. accept or amend ADR-0033;
10. explicitly authorize implementation in `CURRENT_STATE.md`.

## No false closure

- external dependency pins do not mean the binaries were installed or tested;
- CI design does not mean CI exists in `Ptah-space`;
- a scaffold is not the Ptah runtime;
- a green scaffold CI run does not satisfy WP14 implementation proofs;
- Phase 0C remains active until the owner and evidence gates are merged.