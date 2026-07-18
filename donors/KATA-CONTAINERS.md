# Donor Record — Kata Containers

**Phase:** 0A / WP11  
**Status:** FIRST-PASS COMPLETE — PRIMARY VM-STRENGTH CONTAINER SANDBOX CANDIDATE  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/kata-containers/kata-containers
- Owner/organisation: `kata-containers`
- Default branch: `main`
- Pinned commit: `a2fbc64e27ecd3fc1b5992cf9a5fabba586c7911`
- Licence: Apache-2.0
- Activity: Active
- Primary languages: Rust and Go, with guest Linux/kernel/image and packaging components
- Classification: OCI/containerd-compatible lightweight-VM runtime and VM-strength container isolation donor
- Ptah targets: `ISOLATION-001`, `DIST-001` runtime classes, untrusted multi-tenant workloads, VM-backed Workspace Providers, accelerator/confidential-computing compatibility, runtime placement and stronger escalation from ordinary OCI/gVisor

## Files/components inspected

- `README.md`
- `LICENSE`
- `docs/design/architecture_4.0/architecture.md`
- `docs/threat-model/threat-model.md`
- `docs/hypervisors.md`
- `versions.yaml`
- current repository/commit activity
- runtime, runtime-rs, agent, Dragonball, QEMU, Cloud Hypervisor and Firecracker boundaries
- guest image/kernel, virtio/vsock, shared-filesystem, VFIO, GPU and confidential-computing component records

## Verified capabilities and patterns

### Isolation model

- Kata runs container workloads inside lightweight virtual machines rather than directly against the host kernel.
- The guest Linux kernel provides the container execution environment inside the VM.
- The additional isolation boundary is hardware virtualization layered over ordinary container controls.
- In Kubernetes/CRI usage, the sandbox boundary is normally the Pod; multi-container Pods can share one Kata VM.
- The stated security objective is to prevent an untrusted container user or workload from controlling, reading or tampering with host/cluster infrastructure.
- Kata remains OCI/containerd-compatible through a shim-v2 runtime, preserving ordinary container image and manager workflows.

### Runtime and guest architecture

- Core components include the containerd shim/runtime, an agent inside the guest VM, hypervisor/VMM integration, guest kernel/rootfs/initrd and host-side storage/network helpers.
- Kata 4.0 introduces a Rust runtime with asynchronous execution and a more unified control path.
- The runtime separates service/orchestration, sandbox/container management and infrastructure/hypervisor interfaces.
- Container abstractions include Linux, virtualization-backed and WebAssembly paths.
- Resource-manager interfaces cover shared filesystems, network, rootfs, volumes and cgroups.
- The guest agent receives commands over vsock/hybrid-vsock and configures container processes inside the VM.

### Built-in and external VMM modes

- Kata 4.0 supports an integrated built-in VMM and optional external VMMs.
- Dragonball can run as a library inside the Rust shim process, reducing IPC, startup latency and split-process cleanup complexity.
- External VMM mode supports QEMU, Cloud Hypervisor and Firecracker through separate processes and RPC/vsock paths.
- External VMM mode offers broader compatibility/modularity but adds process-boundary overhead and more complex abnormal-condition recovery.
- Hypervisor choice is explicit configuration, not an implementation detail that can be switched without compatibility/security evidence.

### Host and guest interface surface

- Container root filesystems, volumes, secrets and config maps can enter the guest through block devices or shared filesystems such as virtio-blk and virtio-fs.
- Networking commonly uses TAP/virtio-net; direct NIC/device assignment can use VFIO.
- Guest-agent control and container stdio use virtio-vsock/hybrid-vsock.
- CPU, memory and device hotplug can depend on ACPI or hypervisor-specific mechanisms.
- Each virtio backend may execute in the VMM, userspace helper or host kernel; this materially changes the host attack surface.
- `virtiofsd` uses namespace/seccomp hardening, but shared host filesystem access still creates a deliberate data/interface boundary.
- VFIO/device passthrough introduces DMA, firmware, isolation, resource-starvation and side-channel risks.

### Hypervisor and capability diversity

- Supported host architectures include x86_64/amd64, arm64, ppc64le and s390x with architecture-specific virtualization requirements.
- The repository provides host capability checking through `kata-runtime check`.
- Hypervisor options include QEMU, Cloud Hypervisor, Firecracker, Dragonball and StratoVirt.
- QEMU is the primary supported path for NVIDIA GPU and confidential-computing features such as Intel TDX and AMD SEV-SNP.
- Firecracker has a narrower device/hotplug feature set and no listed GPU/confidential-computing support in the inspected comparison.
- Dragonball integrates tightly with the Rust runtime and optimizes container workloads, but its supported device/host feature surface differs from QEMU.

### Resource, denial-of-service and multi-tenant boundaries

- All Kata VMs still share host hardware and the host kernel/KVM implementation.
- VM isolation does not eliminate host-kernel, KVM, VMM, virtio backend, firmware or hardware vulnerabilities.
- CPU, RAM, I/O and network exhaustion remain host scheduler/cgroup/resource-policy concerns.
- Shared filesystems, network paths, device passthrough and deliberately mounted data remain visible to the guest according to configuration.
- Mutually untrusted workloads must not share one Pod/VM sandbox unless the caller explicitly accepts that shared boundary.
- Hypervisor/device configuration and resource control are as security-relevant as selecting Kata itself.

### Pinned component stack and confidential paths

- `versions.yaml` records exact or bounded versions for VMMs, guest kernels/images, confidential-computing components and supporting tools.
- The inspected pin records Cloud Hypervisor, Firecracker, QEMU, guest kernel/image/initrd and NVIDIA stack versions separately.
- Confidential paths include QEMU variants for TDX/SEV-SNP/CCA-related development and Confidential Containers guest/trustee components.
- Attestation/key-delivery components are separate dependencies and do not make every Kata workload confidential by default.
- GPU, confidential-computing, guest-image and driver combinations require exact compatibility and provenance records.

## What Kata Containers contributes

- A VM-strength isolation class that preserves container/OCI operational ergonomics.
- A clear escalation target above ordinary OCI and gVisor for stronger tenant/workload separation.
- Pod/Workspace sandboxing with a dedicated guest kernel.
- Containerd shim-v2 compatibility.
- Pluggable hypervisor/runtime architecture.
- Integrated Dragonball and external QEMU/Cloud Hypervisor/Firecracker modes.
- Explicit host-capability checking.
- Strong lessons for guest-agent control, shared filesystems, virtio, device passthrough and network boundaries.
- GPU and confidential-computing integration paths with version-sensitive component stacks.
- A practical provider candidate for high-risk Plugins, agents, builds, security workloads and customer-isolated Workspaces.

## Important limitations for Ptah

- Kata requires hardware virtualization and a compatible Linux host; it is not a universal desktop/mobile runtime.
- It has higher startup, memory and operational overhead than ordinary OCI or gVisor.
- A Kata VM is not automatically a separate tenant boundary when multiple mutually untrusted containers share one Pod/VM.
- The host KVM/kernel, VMM, virtio backends, filesystem helpers, device firmware and orchestration stack remain attack surfaces.
- QEMU, Cloud Hypervisor, Firecracker and Dragonball have different architectures, device models, performance and security properties.
- Built-in Dragonball and external VMM modes have different lifecycle/failure-domain behavior.
- Shared filesystems and host-backed volumes deliberately expose host data paths to the guest.
- VFIO and GPU passthrough materially broaden the trusted computing base and can introduce DMA/firmware risks.
- Confidential-computing support is hardware/VMM/firmware/attestation/image specific and cannot be inferred from using Kata alone.
- Runtime component versions span the shim, VMM, guest kernel, rootfs/initrd, agent, helpers and device stack; partial upgrades can break compatibility.
- No general, portable checkpoint/migration guarantee was established from the inspected sources.
- The runtime does not own Ptah Activity durability, placement, scheduling, Object permissions, credential policy, receipts or acceptance.
- `kata-runtime`, shim, VM, sandbox, Pod and guest-agent IDs are not canonical Ptah identities.
- Host capability checks establish prerequisites, not workload-level correctness or security proof.

## Must not be inherited

- Kata/VM/Pod/shim IDs as Ptah Workspace, Activity, Node, Provider or Session identity;
- every untrusted workload grouped into one shared Kata Pod/VM;
- all VMMs treated as equivalent behind one runtime name;
- Dragonball integrated mode assumed to have identical failure recovery to external VMM mode;
- shared filesystem, host networking, VFIO or broad device passthrough enabled by default;
- GPU/confidential-computing support claimed without exact hardware, firmware, VMM, guest, driver and attestation evidence;
- VM creation treated as proof of tenant isolation, resource control or successful workload completion;
- host capability-check success treated as deployment acceptance;
- host cgroups/network policy/object permissions replaced by the VM boundary;
- unsupported features silently retried under ordinary OCI/gVisor without policy approval;
- mutable or partially upgraded guest kernels/images/VMMs used without component-set identity;
- Kata made mandatory for trusted lightweight or latency-critical workloads where a lower class is sufficient;
- confidential or GPU paths made a v1 dependency.

## Integration decision

**ADOPT KATA CONTAINERS AS THE PRIMARY VM-STRENGTH CONTAINER/WORKSPACE ISOLATION CANDIDATE ABOVE gVisor, WITH EXPLICIT HYPERVISOR AND COMPONENT-SET PROFILES.**

Recommended Ptah role:

1. ordinary trusted workloads may use baseline OCI;
2. higher-risk but compatible workloads may use gVisor;
3. mutually untrusted tenants, high-risk Plugins/security workloads or stronger isolation requirements may select Kata;
4. each mutually untrusted tenant/workload receives a separate Kata sandbox/VM unless shared trust is explicitly declared;
5. runtime profiles name exact VMM, integrated/external mode, guest kernel/image, agent, shared-filesystem, network and device configuration;
6. unsupported workloads fail honestly or escalate to a different VM/full-VM Provider rather than silently weakening isolation;
7. GPU and confidential-computing profiles remain separate optional classes with exact compatibility/provenance records;
8. Ptah retains Node placement, cgroups, resource budgets, network policy, Object mounts, credential delivery, Activity and Receipt authority;
9. component-set upgrades are staged, tested and rollbackable;
10. migration/checkpoint support remains unavailable until separately proven for an exact runtime/VMM/guest profile.

## Licence decision

Apache-2.0 is compatible with architecture study, wrapping and adoption. Hypervisors, guest images/kernels, firmware, GPU drivers/toolkits, Confidential Containers components and transitive packages require separate licence and provenance review.

## Native Ptah gap

Ptah must define:

- Isolation Class and Runtime Provider identities;
- baseline OCI, gVisor, Kata, microVM and full-VM profiles;
- exact runtime/VMM/guest component-set identity;
- integrated versus external VMM lifecycle/failure-domain records;
- Node architecture, KVM/virtualization, firmware and capability snapshots;
- sandbox/VM/tenant generation and fencing identity;
- resource reservation, CPU/RAM/disk/I/O/network budgets and enforcement evidence;
- Object/View mount, shared-filesystem and secret/credential delivery scopes;
- network namespace, TAP/CNI and egress/ingress policy records;
- virtio/vsock/VFIO/device/GPU exposure records;
- confidential-computing measurement, attestation, policy and key-delivery records;
- workload compatibility and escalation/fallback policy;
- startup/teardown/health/upgrade/rollback Activities and Receipts;
- checkpoint/migration capability and compatibility records;
- cross-runtime and cross-hypervisor conformance tests;
- placement hints based on risk, architecture, accelerator, data locality, cost and latency.

## Exit strategy

Ptah's Isolation and Workspace Provider contracts remain independent. A workload can move among baseline OCI, gVisor, Kata with Dragonball/QEMU/Cloud Hypervisor/Firecracker, a standalone microVM or a full VM without changing Workspace, Activity, Object, Package or caller identity.

## Validation required

1. Run one golden OCI workload under baseline OCI, gVisor and Kata and retain exact runtime/component evidence.
2. Run Kata with built-in Dragonball and at least one external VMM and compare lifecycle, startup, resource and failure behavior.
3. Reject a Node lacking required virtualization/architecture capability before placement.
4. Place mutually untrusted workloads in separate VMs and prove no unintended shared filesystem, network, process or credential access.
5. Apply CPU, RAM, disk, I/O, process and network budgets through host controls and prove enforcement.
6. Validate virtio-fs/block-volume paths against traversal, symlink, stale-mount and unintended-host-data exposure.
7. Deny VFIO/device/GPU access unless exact IOMMU group, firmware, driver and capability policy is approved.
8. Boot the same Package Release under two hypervisors and compare declared compatibility and output evidence.
9. Fail an integrated and external VMM process and retain distinct cleanup/recovery evidence.
10. Upgrade one component of the runtime/VMM/guest stack and reject activation until the complete component-set conformance suite passes.
11. Attempt checkpoint/migration and label unsupported/unproven paths honestly rather than claiming recovery.
12. Run a confidential-computing profile only after measurement, attestation and key-delivery proof; reject ordinary Kata as equivalent.
13. Escalate an incompatible gVisor workload to Kata without changing Ptah Workspace, Activity or Object identity.
14. Replace Kata with another VM Provider for one workload without changing Ptah identities.
