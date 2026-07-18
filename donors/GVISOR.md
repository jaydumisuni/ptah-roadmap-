# Donor Record — gVisor

**Phase:** 0A / WP11  
**Status:** FIRST-PASS COMPLETE — PRIMARY USERSPACE APPLICATION-KERNEL SANDBOX CANDIDATE  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/google/gvisor
- Owner/organisation: `google`
- Default branch: `master`
- Pinned commit: `eb7b0b4c1a84b7e48e97d606e6a5e79e3eddbf01`
- Licence: Apache-2.0
- Activity: Active
- Primary language: Go
- Classification: OCI-compatible userspace application-kernel sandbox and stronger-container isolation donor
- Ptah targets: `ISOLATION-001`, risk-based runtime selection, OCI sandbox Provider, untrusted tool/plugin/workload execution, checkpoint evidence, GPU isolation and host-surface reduction

## Files/components inspected

- `README.md`
- `LICENSE`
- `g3doc/architecture_guide/intro_to_gvisor.md`
- `g3doc/architecture_guide/security.md`
- `g3doc/architecture_guide/performance.md`
- `g3doc/user_guide/gpu.md`
- `runsc/cmd/checkpoint.go`
- current repository/commit activity

## Verified capabilities and patterns

### Isolation architecture

- gVisor implements a Linux-like application kernel in memory-safe Go and runs it in userspace.
- The OCI-compatible `runsc` runtime integrates with Docker, containerd/Kubernetes and ordinary container images/tooling.
- It is neither a simple syscall filter nor an ordinary VM.
- Sandboxed workloads interact with the gVisor Sentry rather than issuing their system calls directly to the host kernel.
- Linux syscall, memory-management, filesystem, network, process, signal and namespace behavior is independently implemented in the Sentry.
- Unsupported Linux features are unavailable rather than transparently passed through.
- The Sentry itself runs with restricted host syscalls, namespaces, cgroups and minimal capabilities.
- A more privileged Gofer process mediates selected host-backed filesystem access.
- gVisor uses Linux security primitives as defense-in-depth rather than treating them as the primary isolation boundary.

### Platforms and execution modes

- Systrap is the default platform and uses seccomp-based interception without requiring host virtualization.
- KVM is an alternate platform using hardware virtualization for address-space isolation and page-fault interception.
- Platform choice changes compatibility, performance and security characteristics even though administrators can switch them behind the same runtime interface.
- `runsc` supports x86_64 and ARM64 hosts.
- Rootless operation is possible for restricted cases such as no-network one-off workloads, while ordinary sandbox setup can require privilege before dropping it prior to untrusted-code execution.

### Threat and policy boundary

- gVisor reduces direct exposure to host-kernel System APIs but does not replace secure higher-level architecture.
- It does not protect against vulnerabilities in services or orchestration layers that occur before the runtime is selected.
- It does not eliminate hardware side channels.
- A compromise inside one sandbox still exposes everything deliberately mounted, networked or otherwise granted to that sandbox.
- Separate untrusted tenants/workloads should use separate sandboxes.
- Host cgroups remain responsible for CPU/memory/resource-exhaustion controls.
- Container-level networking policy remains externally enforced.
- Host-backed file access and directfs choices change the host surface.

### Performance and compatibility

- CPU instructions execute natively, so CPU-bound workloads can have low direct compute overhead.
- System-call-heavy, network-heavy and metadata/filesystem-heavy workloads can incur significant overhead.
- The Sentry adds fixed and workload-dependent memory overhead.
- gVisor's independent Linux implementation creates compatibility gaps where syscalls, ioctls, filesystems or specialized features are not implemented.
- Systrap is recommended for best performance in most cases, while KVM and nested virtualization have different costs.
- gVisor is not automatically beneficial for every trusted workload, especially when all valuable data is already deliberately inside the sandbox.

### Checkpoint and recovery

- `runsc checkpoint` can save container state to an image path.
- Checkpoint behavior includes compression, optional leave-running/resume, direct I/O, zero-page exclusion and save/restore hooks.
- CUDA checkpoint support has explicit paths/options.
- The command labels checkpointing experimental.
- A successful checkpoint command is not proof that the state can restore on another Node, runtime version, platform or GPU/driver combination.

### GPU path

- `nvproxy` supports selected NVIDIA/CUDA, Vulkan and media workloads through a proxy to the host NVIDIA driver.
- `runsc` supports CDI integration and can operate with modern container runtimes/device plugins.
- GPU calls use a controlled but real host `ioctl` path rather than fully emulating the NVIDIA kernel driver.
- Supported GPUs, driver versions, capabilities, device files, ioctls and platforms are explicitly limited and version-sensitive.
- Unsupported known driver versions can only be attempted through an explicit warning flag; unknown drivers fail.
- Enabling additional NVIDIA capabilities broadens the exposed host-driver surface and must be conservative.

## What gVisor contributes

- A strong middle isolation class between ordinary OCI containers and VM/microVM backends.
- OCI compatibility without exposing the workload directly to the host Linux syscall implementation.
- A reusable `runsc` Provider path for untrusted scripts, plugins, builds, browser helpers and agent workloads.
- Explicit Systrap/KVM platform alternatives.
- Memory-safe application-kernel implementation and constrained host surface.
- Runtime checkpoint machinery useful for Ptah recovery research.
- GPU workload support with explicit model/driver/capability compatibility records.
- A clear threat-model lesson: sandbox, resource controls, network policy, data permissions and orchestrator trust remain separate.

## Important limitations for Ptah

- gVisor is Linux-host specific and supports only selected host architectures.
- It is not a VM-strength tenant boundary in every threat model and must be compared with Kata/Firecracker.
- Linux compatibility is intentionally incomplete; specialized syscalls, ioctls, devices, filesystems and kernel behavior may fail.
- Runtime selection before `runsc` is outside gVisor's protection.
- Host cgroups, networking, credentials, mounts and Object permissions remain Ptah/provider responsibilities.
- gVisor cannot prevent an application from reading data deliberately exposed inside the sandbox.
- Hardware side-channel mitigation remains a host/hardware concern.
- DirectFS, host networking, devices and GPU proxy paths can enlarge the host attack surface.
- GPU support depends on selected NVIDIA models, exact driver ABIs, permitted capabilities and supported ioctls.
- Checkpointing is explicitly experimental and portability/restore compatibility require proof.
- System-call-heavy, networking and filesystem-metadata workloads can perform materially worse than `runc`.
- `runsc`, sandbox, platform, container and checkpoint IDs are not canonical Ptah identities.
- gVisor does not own durable Activity scheduling, placement, retries, Object storage, proof or caller acceptance.
- Running one sandbox does not create safe multi-tenant separation inside that sandbox.

## Must not be inherited

- gVisor or `runsc` IDs as Ptah Workspace, Activity, Node, Provider or checkpoint identity;
- every OCI workload routed to gVisor regardless of trust, compatibility or performance needs;
- Systrap and KVM treated as equivalent without platform-specific evidence;
- checkpoint creation reported as proven portable recovery;
- host networking, directfs, broad mounts, devices or GPU capabilities enabled by default;
- `--nvproxy-allow-unsupported-driver` treated as supported or production-safe behavior;
- gVisor used as a substitute for cgroups, network policy, credential scoping or Object permissions;
- one sandbox used for mutually untrusted tenants;
- unsupported Linux behavior silently retried under weaker isolation without policy approval;
- gVisor described as complete VM isolation or as protection from hardware side channels;
- gVisor made mandatory for trusted high-performance databases or specialized device workloads.

## Integration decision

**ADOPT gVisor/runsc AS THE PRIMARY STRONGER-CONTAINER/USERSPACE-KERNEL ISOLATION CANDIDATE, BETWEEN ORDINARY OCI AND VM/MICROVM PROVIDERS.**

Recommended Ptah role:

1. ordinary trusted OCI remains available through the baseline container runtime;
2. approved untrusted or higher-risk OCI workloads can select a gVisor Provider;
3. platform selection (Systrap/KVM), network mode, filesystem mode and devices are explicit Provider configuration;
4. unsupported or incompatible workloads fail honestly or escalate to Kata/Firecracker/VM instead of silently weakening isolation;
5. checkpoint/restore is exposed only after version/platform/host conformance proof;
6. GPU access requires exact device/driver/capability compatibility and a separately approved host-surface record;
7. each mutually untrusted workload or tenant receives a separate sandbox;
8. Ptah retains cgroups, network, mount, credential, Object, Activity and evidence authority.

## Licence decision

Apache-2.0 is compatible with architecture study, wrapping and adoption, subject to retaining notices and reviewing container images, GPU/NVIDIA components and transitive dependencies separately.

## Native Ptah gap

Ptah must define:

- Isolation Class and Runtime Provider identities;
- threat/risk classification and escalation policy;
- ordinary OCI, gVisor Systrap, gVisor KVM, Kata, microVM and full-VM capability records;
- Node host-kernel, architecture, virtualization and platform compatibility snapshots;
- runtime version, config, seccomp/platform, filesystem, network and device records;
- cgroup/resource budgets and denial-of-service controls;
- Object/View mount and credential-delivery scopes;
- sandbox/tenant separation and generation/fencing identity;
- checkpoint Artifact, runtime/platform compatibility and restore proof;
- GPU model, driver ABI, CDI spec and allowed-capability records;
- unsupported-feature failure and stronger/weaker fallback policy;
- performance/compatibility profiles and workload placement hints;
- runtime health, vulnerability, upgrade and rollback behavior;
- cross-provider conformance tests.

## Exit strategy

Ptah's Isolation/Provider contracts remain independent. A workload can move among `runc`, gVisor, Kata, Firecracker, a full VM or a remote managed sandbox without changing Workspace, Activity, Object or Package identity.

## Validation required

1. Run the same OCI workload under baseline `runc`, gVisor Systrap and gVisor KVM and retain exact runtime/platform evidence.
2. Attempt unsupported syscalls/ioctls/features and fail without silently switching to weaker isolation.
3. Prove filesystem, network, credential and Object scopes remain enforced outside gVisor.
4. Run mutually untrusted workloads in separate sandboxes and reject cross-sandbox access.
5. Apply CPU, RAM, disk, process and network budgets through host controls and prove enforcement.
6. Compare CPU-bound, syscall-bound, network-heavy and filesystem-heavy golden workloads.
7. Checkpoint, restore and migrate across approved same-version/same-platform Nodes, retaining checkpoint Artifacts and read-back proof.
8. Reject restore across incompatible runtime/platform/host combinations unless explicitly proven.
9. Run a supported GPU workload with exact model/driver/CDI/capability identity.
10. Reject unknown or unsupported GPU drivers/capabilities without using break-glass flags.
11. Escalate an incompatible or higher-risk workload to Kata/Firecracker/VM without changing Ptah identities.
12. Upgrade/roll back `runsc` while preserving active-workload and checkpoint compatibility records.
