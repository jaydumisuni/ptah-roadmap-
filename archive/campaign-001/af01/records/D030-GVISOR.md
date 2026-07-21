# D030 — gVisor Archive Record

Outcome: ACCEPTED FOR ARCHIVE — optional isolation backend; no default-backend or runtime-authorization claim

Campaign: `CAMPAIGN-001`

Formation: `AF01`

Primary Archivist: `AF01-P05`

Independent Verifier: `AF01-V05`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `google/gvisor`;
- owner: Google organization;
- visibility: public;
- archived: false;
- default branch: `master`;
- inspected commit: `9f653e577965df2ddd13875b5530cd2588661f1c`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root licence: Apache License 2.0;
- licence evidence: `LICENSE` blob `f7a006d10464cfe9724b5d687c0013bf982cc66a`;
- images, toolchains, dependencies and distributed artifacts require separate implementation-time review;
- activity state: active; inspected head changes and enables native syscall tests for runc/nftables behavior.

## Primary evidence packet — AF01-P05

Inspected:

- `README.md` blob `9df7b167df32de9eca3e64071ff36c097a2a7437`;
- `runsc/main.go` blob `01a4eb663b74425108ff8ba9bd0a1f6937d351e0`;
- root `LICENSE`;
- exact current head.

Verified:

- gVisor is a userspace application kernel written in Go;
- it exposes an OCI runtime named `runsc`;
- `runsc/main.go` delegates to the runtime CLI entry and explicitly implements the OCI runtime interface;
- gVisor integrates with Docker and Kubernetes/containerd tooling;
- supported source-build targets include x86_64 and ARM64;
- documented build/test paths use Bazel/Make and include unit and broader test suites;
- the project explicitly states that gVisor is neither a syscall filter nor a normal VM;
- its security model reduces the host-kernel surface available to workloads but does not eliminate the need to control data and external service exposure.

Primary conclusion:

gVisor remains a valid optional isolation backend donor. It can strengthen isolation for compatible container workloads, but it is not a scheduler, VM replacement in every case, policy authority, integrity proof system or universal compatibility layer.

## Independent verification packet — AF01-V05

Repeated checks:

- canonical identity, `master` branch and exact inspected head;
- Apache-2.0 licence;
- actual `runsc` OCI runtime entry point;
- build and test evidence;
- explicit “not VM / not syscall filter” limitation;
- architecture is a userspace application kernel that mediates Linux interfaces.

Challenges retained:

- syscall/application compatibility must be measured per workload;
- performance and architecture support require physical-host evidence;
- gVisor isolation does not replace secret/data minimization, network policy, VM fallback or Receipt generation;
- `runsc` process success is not proof of workload correctness;
- distributed binaries and host integration require pinned artifact/signature review.

Verifier conclusion: primary findings supported. No contradiction with the frozen isolation-backend placement.

## Ptah relationship

- frozen donor group: Runtime, builds and isolation;
- current classification: optional wrapped OCI isolation backend;
- requirements supported: stronger userspace-kernel isolation for compatible container Activities, Docker/Kubernetes/containerd integration and negative-path isolation testing;
- prohibited inheritance: gVisor identity as Ptah Workspace/Activity identity, backend success as final proof, removal of VM fallback, unmeasured default selection;
- replacement/exit strategy: preserve provider-neutral execution contracts and choose gVisor per capability/policy evidence with runc/Kata/VM alternatives.

## Contradiction and supersession

- no canonical-identity contradiction found;
- current `master` branch and exact head supersede generic branch assumptions;
- source confirms the frozen decision that gVisor is one backend option, not the whole isolation architecture.

## Bounded outcome

`accepted for archive` preserves the current gVisor account. It does not select gVisor as the default backend, authorize binary deployment/source reuse, reopen Phase 0A, accept ADR-0033 or authorize Ptah runtime implementation.
