# Donor Record — Firecracker

**Phase:** 0A / WP11  
**Status:** FIRST-PASS COMPLETE — PRIMARY STANDALONE MICROVM PROVIDER CANDIDATE  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/firecracker-microvm/firecracker
- Owner/organisation: `firecracker-microvm`
- Default branch: `main`
- Pinned commit: `5ac3f5ffdcd7a9660778df8b4c33fcad811d8fe2`
- Licence: Apache-2.0
- Activity: Active
- Primary language: Rust
- Classification: minimal KVM-based microVM monitor, host-jailer and snapshot Provider donor
- Ptah targets: `ISOLATION-001`, `DIST-001`, standalone high-isolation microVM Workspaces, serverless/batch Functions, rapid VM start/restore, one-workload-per-VM separation and resource-aware placement

## Files/components inspected

- `README.md`
- `LICENSE`
- `docs/design.md`
- `docs/prod-host-setup.md`
- `docs/snapshotting/snapshot-support.md`
- current repository/commit activity
- host API, Jailer, seccomp, cgroups, TAP networking, block devices, vsock, MMDS, rate limits and snapshot boundaries

## Verified capabilities and patterns

### MicroVM model

- Firecracker uses KVM to create lightweight virtual machines designed for secure multi-tenant container/function workloads.
- Each Firecracker process encapsulates exactly one microVM.
- The device model is intentionally minimal to reduce startup time, memory footprint and guest-facing attack surface.
- Guest-visible devices focus on virtio block, network and vsock plus minimal platform devices.
- It can be used directly as a standalone VMM or through integrations such as Kata Containers.
- Linux hosts and Linux guest operating systems are the primary execution environment.

### Host control API

- Each process exposes a host-facing HTTP API, normally through a Unix socket.
- The API configures vCPU count, memory, CPU template, kernel, root filesystem, boot arguments, network interfaces, file-backed block devices, vsock, entropy and selected hotplug features.
- Device rate limiters can bound operations and bandwidth.
- Logging and metrics endpoints are explicit.
- MMDS is optional and guest-visible only when configured.
- The API creates/configures the machine before `InstanceStart`; it is separate from guest workload execution.

### Threat containment and Jailer

- Guest vCPU threads are treated as malicious once started.
- KVM/virtualization forms the main isolation boundary.
- Firecracker installs restrictive per-thread seccomp filters before guest code executes.
- Production usage should start Firecracker through the Jailer or an equally restrictive wrapper.
- The Jailer configures chroot, namespaces, cgroups and resource limits, drops privileges and then executes Firecracker as an unprivileged user.
- Multiple microVMs should use unique UIDs/GIDs for stronger separation of host-owned resources.
- Jailer input paths are trusted and must not be writable by unprivileged users.
- Firecracker can access only resources deliberately made available inside the jail or passed through file descriptors.

### Resource and noisy-neighbour control

- vCPU and memory oversubscription are possible, but host operators own the safe degree of oversubscription.
- Firecracker supports block and network token-bucket rate limiting.
- Jailer/cgroup controls can bound CPU, RAM, file size, file descriptors and block I/O.
- CPU affinity/cpuset policy can reduce cross-node movement and contention.
- Guest-controlled serial/log output must be bounded to prevent host memory/storage exhaustion.
- A host overwatcher is recommended to terminate unresponsive processes.
- KVM helper threads, page cache, swap, logging, networking and storage can create host-level resource and data-remanence concerns outside the VMM itself.

### Networking and storage boundaries

- Guest network interfaces are backed by host TAP devices.
- Firecracker does not filter guest network traffic; host firewall/network policy must enforce egress and access restrictions.
- Guest disks are file-backed block devices managed by the host/operator.
- Rate limiting does not replace filesystem permissions, encryption, durability or Object-level access control.
- MMDS and host metadata endpoints require explicit isolation to avoid credential/metadata leakage.
- Block-device files, kernel images, root filesystems, snapshots and API sockets remain trusted host inputs.

### Snapshot and restore

- Firecracker can pause, create full or differential snapshots, resume and load snapshots in a new process.
- Snapshot state includes guest memory and emulated/KVM device state; guest disk files are separate and operator-managed.
- Resumed memory is demand-paged from a private mapping and copied on write.
- Snapshot files are not packaged, authenticated, encrypted or lifecycle-managed by Firecracker.
- The state file uses only a CRC against accidental corruption; memory and disk files need independent integrity/security.
- Network and vsock connections may be lost or reset after restore.
- Logs/metrics configuration and MMDS data store are not fully preserved.
- Snapshot format compatibility is versioned and checked by the runtime.
- Differential snapshot support remains developer preview.
- Disk contents require external backup/flush/durability handling.
- Cloning one snapshot creates uniqueness/security risks unless guest identity, entropy, credentials, network state and VM generation are refreshed.

### Platform and compatibility boundaries

- Supported/tested paths are specific to host kernels, CPU families and architectures.
- Production security depends on patched host/guest kernels, KVM, CPU microcode and correct host configuration.
- CPU templates control exposed processor features and influence snapshot portability.
- Hardware vulnerabilities and side channels are not solved by Firecracker.
- Device hotplug and some stop/restore capabilities are architecture/version dependent.
- Firecracker provides a narrower device/feature surface than QEMU and is not the general answer for GPU or broad device passthrough workloads.

## What Firecracker contributes

- A clear standalone microVM isolation Provider above ordinary OCI and gVisor.
- One-process/one-microVM failure and lifecycle boundaries.
- Minimal device model and reduced guest-facing attack surface.
- Strong process-level defense in depth through Jailer, seccomp, namespaces, cgroups and privilege dropping.
- Explicit host API and machine configuration model.
- Fast microVM startup/density direction suitable for batch, function and disposable high-risk workloads.
- File-backed disk and TAP-network integration patterns.
- Per-device rate limiting and resource-accounting lessons.
- Versioned snapshot/restore mechanics with fast demand-paged resume.
- A reusable VMM both directly and behind Kata.

## Important limitations for Ptah

- Firecracker requires Linux/KVM and suitable CPU virtualization; it is not a universal local runtime.
- It provides a VMM, not a complete container/Workspace lifecycle, image manager, scheduler, network policy, credential manager or Activity runtime.
- Standalone usage requires Ptah to supply guest images/kernels, bootstrap/agent control, volume/object mounting and process/result collection.
- The API socket and every supplied kernel/rootfs/block/snapshot path are trusted host inputs.
- Firecracker performs no network filtering.
- Jailer/cgroup correctness and patched host/KVM/microcode are part of the security boundary.
- Guest serial/log output, network traffic, KVM helper threads, memory, page cache and storage can create denial-of-service risks.
- One process per microVM increases process/scheduling/monitoring volume at high density.
- Snapshot files can contain guest secrets, credentials and memory; Firecracker does not encrypt/authenticate/package them.
- Snapshot restore can lose network/vsock state and does not prove application-level recovery.
- Snapshot/disk consistency is operator/application responsibility.
- Differential snapshots are developer preview.
- Snapshot compatibility depends on Firecracker version, CPU template, architecture, guest/device state and host capabilities.
- The minimal device model limits GPU, VFIO, arbitrary PCI and broad hardware workloads.
- Firecracker process/microVM/snapshot/API IDs are not canonical Ptah identities.
- Standalone Firecracker does not provide Kata's containerd shim/guest-agent composition automatically.

## Must not be inherited

- Firecracker IDs as Ptah Workspace, Activity, Node, Provider, Session or checkpoint identity;
- API configuration success treated as workload execution proof;
- an unjailed or weakly jailed VMM used for production untrusted workloads;
- the API socket exposed across untrusted networks;
- TAP networking without host egress/ingress policy;
- host block/snapshot paths accepted from untrusted callers;
- snapshot creation reported as durable, portable or application-consistent recovery;
- snapshot CRC treated as cryptographic integrity;
- cloning snapshots without refreshing identity, entropy, credentials, network and generation state;
- CPU/memory oversubscription without admission control and pressure evidence;
- log/serial output left unbounded;
- swap/page-cache/data-remanence risks ignored;
- Firecracker used for GPU/device workloads it does not support;
- standalone Firecracker made mandatory when Kata or another Provider already supplies the required lifecycle;
- silent fallback to weaker OCI when KVM or compatibility is unavailable.

## Integration decision

**ADOPT FIRECRACKER AS THE PRIMARY STANDALONE MICROVM PROVIDER CANDIDATE AND AS ONE OPTIONAL KATA VMM, WITH PTAH-OWNED GUEST, NETWORK, STORAGE, ACTIVITY AND SNAPSHOT CONTRACTS.**

Recommended Ptah role:

1. baseline OCI handles trusted lightweight workloads;
2. gVisor handles compatible higher-risk container workloads;
3. Kata handles VM-backed container/Pod Workspaces;
4. standalone Firecracker handles disposable, function-like, one-workload-per-microVM or specially controlled high-isolation workloads;
5. Ptah supplies a guest bootstrap/agent protocol for process execution, Objects, Events and Receipts;
6. every microVM receives a unique runtime UID/GID, jail, network namespace, cgroup, API socket and generation identity;
7. host firewall, Object mounts, credential delivery and metadata access are explicit policy;
8. snapshot Artifacts include memory, machine state, disks, component versions, CPU template, integrity/encryption and application-consistency records;
9. restore creates a new attempt/generation and requires application/read-back proof;
10. incompatible Nodes fail placement or choose another approved isolation Provider without changing Ptah identities.

## Licence decision

Apache-2.0 is compatible with architecture study, wrapping and adoption. Guest kernels/images, bootstrap agents, VMM integrations and packaged dependencies require separate licence/provenance records.

## Native Ptah gap

Ptah must define:

- standalone MicroVM Provider and Isolation Class identities;
- guest image/kernel/bootstrap/agent component-set identity;
- Node KVM, CPU-template, architecture, kernel and microcode capability snapshots;
- microVM generation, jail, UID/GID, API socket and fencing identity;
- vCPU/RAM/disk/network reservation and admission control;
- host cgroup, CPU affinity, I/O and network-rate policy;
- Object-backed block-image and read-only/read-write mount contracts;
- TAP/network namespace/firewall/metadata-service policy;
- credential/secret delivery and revocation;
- process/guest-agent Activity and Event mapping;
- log/metric/serial collection with bounded storage;
- snapshot bundle, encryption, signature, CAS and retention identity;
- disk/application-consistency, network-reset and clone-identity handling;
- version/CPU/host compatibility and restore conformance;
- VM create/start/stop/kill/snapshot/restore/cleanup Activities and Receipts;
- provider replacement and migration tests.

## Exit strategy

Ptah's MicroVM/Isolation/Workspace contracts remain independent. A workload can move between Firecracker, Kata, Cloud Hypervisor, QEMU, another microVM service or a full VM without changing Workspace, Activity, Object, Package or caller identity.

## Validation required

1. Start a microVM only through Jailer-equivalent constraints and prove unique UID/GID, chroot, namespace, cgroup and API-socket isolation.
2. Reject Nodes without compatible KVM, architecture, host kernel or CPU-template support.
3. Run mutually untrusted microVMs and prove filesystem, network, metadata, API and credential separation.
4. Apply and measure CPU, RAM, disk IOPS/bandwidth, network and log-output limits.
5. Deny guest access to host/Node metadata and restricted network destinations.
6. Boot exact signed kernel/rootfs/block Objects and retain component/digest evidence.
7. Execute one Ptah Activity through a guest agent and retain attempt, Event, output Object and Receipt identity.
8. Create a full snapshot bundle with encrypted/authenticated memory, state and disk Artifacts.
9. Restore on an approved compatible Node, create a new generation and prove application-level readiness/read-back.
10. Reject incompatible Firecracker, CPU-template, architecture or device-state restore.
11. Clone one snapshot and prove identity, entropy, credentials and network state are renewed.
12. Interrupt snapshot creation/restore and retain partial Artifacts without reporting success.
13. Compare standalone Firecracker with Kata-Firecracker for lifecycle, startup, resource and security behavior.
14. Replace Firecracker with another MicroVM Provider without changing Ptah identities.
