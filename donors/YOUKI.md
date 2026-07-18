# Donor Record — youki

**Phase:** 0A / WP11  
**Status:** FIRST-PASS COMPLETE — BASELINE OCI RUNTIME ALTERNATIVE AND RUST IMPLEMENTATION DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/youki-dev/youki
- Owner/organisation: `youki-dev`
- Default branch: `main`
- Pinned commit: `8ed71767216cebb9436fba1da94785f1ddbe4d4d`
- Licence: Apache-2.0
- Activity: Active
- Primary language: Rust
- CNCF status: Sandbox project
- Classification: low-level OCI runtime-spec implementation, rootless/container lifecycle and CRIU checkpoint donor
- Ptah targets: baseline OCI Provider alternatives, runtime conformance, rootless execution, memory-safe runtime implementation, low-resource Nodes and checkpoint compatibility research

## Files/components inspected

- `README.md`
- `LICENSE`
- current repository/commit activity
- OCI lifecycle/tutorial and runtime integration evidence
- seccomp implementation/source locations
- CRIU checkpoint/restore source and test locations
- containerd, Docker, Podman and OCI conformance-test references

## Verified capabilities and patterns

### OCI runtime role

- youki is a Rust implementation of the OCI runtime specification, in the same low-level runtime class as runc and crun.
- It consumes an OCI bundle/configuration and implements create, state, start, list, run, kill and delete lifecycle operations.
- It integrates with Docker as an alternate runtime and is used with Podman/containerd-compatible workflows.
- It passes OCI/containerd-oriented integration and end-to-end tests and has reported production adopters.
- The project maintains a separate Rust OCI specification library.

### Linux isolation primitives

- The runtime config expresses process arguments, environment, namespaces, capabilities, mounts, cgroups, seccomp and other Linux container controls.
- Source locations show dedicated seccomp implementation and listener support.
- Rootful and rootless modes are supported.
- Rootless mode relies on Linux user namespaces and host configuration; it does not create a stronger kernel boundary than ordinary containers.
- The `info` command reports host kernel, architecture, cgroup mode, namespaces and capability availability.

### Implementation and resource profile

- Rust provides memory-safety advantages for a privileged low-level runtime implementation, while still requiring unsafe/system-call interfaces and correct Linux policy.
- youki targets lower startup/memory overhead and easier low-level namespace/fork handling than some Go implementations.
- Published repository benchmarks show youki outperforming the tested runc version but trailing the tested crun version; those numbers are narrow environment/version evidence, not a universal performance ranking.
- Local build/runtime support is Linux-specific and requires a modern kernel and native system dependencies.

### Checkpoint and restore

- Source and tests include OCI checkpoint operations using CRIU.
- CRIU remains a separate privileged/kernel-sensitive dependency.
- Checkpoint/restore compatibility depends on kernel, namespaces, cgroups, files, sockets, mounts, security modules and workload behavior.
- Presence of checkpoint commands/tests does not establish portable migration or application-consistent recovery.

### Conformance and compatibility lessons

- The current head includes a fix aligning generated OCI state output with runc expectations, demonstrating that nominal runtime-spec compatibility can still differ in observable state details.
- OCI conformance and containerd end-to-end success are necessary but not sufficient for identical behavior across runtimes.
- Feature support varies by kernel, build flags, libc/system libraries, cgroup mode and host security configuration.

## What youki contributes

- A memory-safe Rust low-level OCI runtime implementation.
- A plausible baseline-runtime alternative for selected Linux Nodes.
- Rootless/container lifecycle and runtime-info patterns.
- OCI conformance and cross-runtime comparison evidence.
- Seccomp, namespaces, capabilities and cgroup implementation references.
- CRIU checkpoint/restore integration evidence.
- A useful independent runtime for proving Ptah is not coupled to runc.

## Important limitations for Ptah

- youki provides ordinary Linux container isolation and still shares the host kernel.
- Rust memory safety does not protect against Linux kernel vulnerabilities, incorrect namespace/capability/mount/seccomp configuration or unsafe host interfaces.
- Rootless mode reduces privileges but is not equivalent to gVisor, Kata or a VM.
- The runtime does not supply images, networking policy, storage, scheduling, Activity durability, credential management or Object permissions.
- OCI compatibility does not guarantee identical lifecycle, state, signal, cgroup, mount, device, seccomp or checkpoint behavior across runtimes.
- CRIU checkpointing is host/kernel/workload sensitive and can expose process memory and credentials.
- Published performance numbers are old/narrow and cannot drive runtime selection without Ptah workloads and current versions.
- Linux/kernel/system-library requirements limit portability.
- `youki` container IDs and state directories are not canonical Ptah identities.
- A low-level runtime process may require privilege during setup and is a security-critical component.

## Must not be inherited

- youki IDs/state paths as Ptah Workspace, Activity, Node, Provider or Session identity;
- Rust implementation described as a stronger isolation class than ordinary OCI;
- rootless execution described as tenant-grade containment;
- benchmark numbers generalized beyond the exact versions/host/workload;
- OCI conformance treated as proof of identical behavior to runc/crun;
- CRIU checkpoint creation reported as portable or application-consistent recovery;
- unsupported runtime behavior silently switched to another runtime without recording the Provider change;
- default generated OCI config used as Ptah security policy;
- host mounts/devices/capabilities or seccomp-notify paths exposed without explicit permission;
- youki made mandatory merely because it is Rust-based.

## Integration decision

**ADAPT YOUKI AS AN OPTIONAL BASELINE OCI RUNTIME PROVIDER AND CROSS-RUNTIME CONFORMANCE DONOR, NOT AS A STRONG ISOLATION LAYER.**

Recommended Ptah role:

1. containerd/OCI remains the stable Provider contract;
2. runc, youki and crun are replaceable low-level runtime implementations beneath that contract;
3. runtime selection records exact binary/version/build/kernel/cgroup/security configuration;
4. rootless is an explicit privilege mode, not a stronger isolation class;
5. higher-risk workloads escalate to gVisor, Kata, Firecracker or a full VM;
6. checkpoint/restore remains disabled until exact CRIU/runtime/kernel/workload conformance is proven;
7. runtime changes require golden lifecycle, filesystem, signal, resource, seccomp and checkpoint tests;
8. Ptah retains image, network, storage, credential, Activity, Receipt and Object authority.

## Licence decision

Apache-2.0 is compatible with architecture study, dependency use and selective adaptation. CRIU, libseccomp, system libraries and container-manager integrations require separate licence/provenance review.

## Native Ptah gap

Ptah must define:

- baseline OCI Runtime Provider and implementation identity;
- runtime binary/version/build/signature/SBOM records;
- Node kernel, architecture, cgroup, namespace, LSM and seccomp capability snapshots;
- rootful/rootless privilege mode and prerequisite checks;
- OCI config generation from Ptah permissions rather than donor defaults;
- runtime state/lifecycle mapping to Activity, attempt and Receipt identities;
- cross-runtime behavior/conformance corpus;
- CRIU checkpoint Artifact, secrecy, compatibility and restore proof;
- runtime vulnerability, upgrade, rollback and active-workload policy;
- escalation to stronger isolation without identity loss.

## Exit strategy

Ptah's OCI Provider contract remains independent of youki. A Node may use runc, crun, youki or another compliant runtime without changing Workspace, Activity, Object or Package identity.

## Validation required

1. Run one golden OCI workload through runc, youki and crun and compare lifecycle/state output.
2. Compare namespaces, mounts, capabilities, seccomp, devices, signals and cgroup enforcement.
3. Exercise rootful and rootless modes and report exact privilege/isolation differences.
4. Attempt hostile mount/device/capability requests and deny them before runtime invocation.
5. Measure current startup, memory and syscall-heavy behavior on target Nodes rather than relying on README benchmarks.
6. Checkpoint/restore selected workloads with CRIU and retain runtime/kernel/CRIU compatibility evidence.
7. Reject incompatible restore or application state rather than reporting recovery.
8. Upgrade/rollback youki and compare the golden conformance corpus.
9. Switch a Workspace from youki to another baseline OCI runtime without changing Ptah identities.
10. Escalate a workload from youki to gVisor/Kata/Firecracker when policy or compatibility requires it.
