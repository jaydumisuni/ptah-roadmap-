# D031 — Kata Containers Archive Record

Outcome: ACCEPTED FOR ARCHIVE — optional VM-backed isolation backend; no default-backend or host-compatibility claim

Campaign: `CAMPAIGN-001`

Formation: `AF02`

Primary Archivist: `AF02-P07`

Independent Verifier: `AF02-V07`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `kata-containers/kata-containers`;
- owner: Kata Containers organization;
- visibility: public;
- archived: false;
- default branch: `main`;
- inspected commit: `809ab7d90f7dc8c10f51e5b0eef55b9bd33cdbc5`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root licence: Apache License 2.0;
- licence evidence: `LICENSE` blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`;
- guest kernels, root filesystems, hypervisors, firmware, packaged payloads and external components retain separate rights and supply-chain review obligations;
- activity state: active; inspected head merges dependency maintenance for documentation tooling and the repository publishes nightly/payload CI.

## Primary evidence packet — AF02-P07

Inspected:

- `README.md` blob `2e6c3ab5dc3d42e6934c724c5de99553a9091870`;
- root `LICENSE`;
- exact current head;
- source references for Go runtime, Rust runtime, guest agent, Dragonball VMM, hypervisor configurations, packaging and tests.

Verified:

- Kata Containers uses lightweight VMs designed to feel like containers while increasing workload isolation;
- the primary runtime integrates as a containerd shim v2, with a Rust runtime also present;
- a guest agent configures the container environment inside the VM/pod;
- optional hypervisors/VMMs include QEMU, Cloud Hypervisor, Firecracker and Dragonball-related paths;
- supported architectures depend on 64-bit hardware virtualization features;
- `kata-runtime check` validates host capability and may perform network/version checks unless disabled;
- configuration spans runtime, agent and hypervisor sections;
- packaging includes kernels, rootfs/initrd, hypervisors and deployment artifacts.

Primary conclusion:

Kata is a valid optional high-isolation backend donor for compatible container Activities. It is not a universal replacement for native containers or full VMs, and it cannot be selected without exact host virtualization, kernel, hypervisor, performance and workload compatibility evidence.

## Independent verification packet — AF02-V07

Repeated checks:

- canonical identity, `main` branch and exact current head;
- Apache-2.0 root licence;
- VM-backed isolation purpose;
- containerd shim/runtime, guest agent, runtime-rs and optional VMM components;
- architecture/hardware requirements and host-check command;
- packaging and release surface extends beyond repository source.

Challenges retained:

- host support depends on nested/physical virtualization and platform-specific kernel/hypervisor behavior;
- guest image/kernel/VMM provenance must be pinned independently;
- compatibility, startup overhead, resource use and device passthrough vary by workload;
- runtime success does not prove application correctness or policy compliance;
- configuration complexity and multiple backends increase testing and maintenance burden;
- isolation does not replace data minimization, network policy, secret control or Receipts.

Verifier conclusion: primary findings supported. Kata remains an optional isolation backend, not Ptah's execution identity or global default.

## Ptah relationship

- frozen donor group: runtime, builds and isolation;
- current classification: optional VM-backed OCI/containerd isolation provider;
- requirements supported: stronger tenant/workload isolation, runtime-class selection, guest agent lifecycle, hypervisor capability testing and VM-backed negative-path workloads;
- prohibited inheritance: Kata sandbox/container identity as Ptah Activity identity, host-check pass as universal compatibility proof, implicit trust in guest images/hypervisors, removal of runc/gVisor/VM alternatives;
- replacement/exit strategy: maintain provider-neutral execution contracts and select Kata per host/workload policy evidence.

## Contradiction and supersession

- no canonical-identity contradiction found;
- current source confirms Kata 2.x+ monorepo scope and multiple runtime/VMM implementations;
- current platform table supersedes generic “Linux VM isolation” shorthand by making hardware architecture prerequisites explicit;
- frozen Ptah isolation architecture remains unchanged.

## Bounded outcome

`accepted for archive` does not select Kata as default, authorize package/image deployment, prove the current Ptah host supports virtualization, reopen Phase 0A, start AF03, accept ADR-0033 or authorize Ptah runtime implementation.
