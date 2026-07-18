# Donor Record — crun

**Phase:** 0A / WP11  
**Status:** FIRST-PASS COMPLETE — PRIMARY LOW-OVERHEAD OCI RUNTIME AND LIBRARY DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/containers/crun
- Owner/organisation: `containers`
- Default branch: `main`
- Pinned commit: `fb54bc00bf4a9139e74ba68e00da22b424b90912`
- Release line observed: `1.28`
- Licence: mixed component boundary — top-level `COPYING` is GPL-2.0; inspected `libcrun` source declares LGPL-2.1-or-later
- Activity: Active
- Primary language: C
- Classification: low-level OCI runtime, embeddable runtime library, rootless/cgroup/systemd and CRIU donor
- Ptah targets: baseline OCI Provider implementations, low-resource Nodes, embedded runtime control, rootless execution, cgroup/systemd behavior, OCI extensions and cross-runtime conformance

## Files/components inspected

- `README.md`
- `COPYING`
- `NEWS`
- `crun.1.md`
- `src/libcrun/container.c`
- checkpoint/restore source and test locations
- seccomp-listener/plugin, systemd/cgroup, idmapped-mount, krun and WASM extension documentation
- current repository/commit activity

## Verified capabilities and patterns

### OCI runtime and library role

- crun is a low-level OCI runtime in the same baseline isolation class as runc and youki.
- It implements create, start, run, exec, list, state, kill, delete, pause, resume, update, checkpoint and restore operations.
- Runtime state defaults to `/run/crun` for root and `$XDG_RUNTIME_DIR/crun` for unprivileged callers.
- It can use direct cgroupfs, systemd or disabled cgroup management.
- `libcrun` allows programs to embed the runtime rather than always invoking a separate CLI process.
- Shared and static build paths exist, but build composition and licences differ from simply consuming the executable.

### Resource and privilege controls

- Runtime resource updates cover CPU, memory, swap, PID, cpuset and block-I/O controls.
- Rootless OCI configuration generation and automatic user-namespace creation are supported.
- cgroup v2 is the forward path; cgroup v1 is deprecated.
- systemd subgroup and delegated-cgroup extensions support nested workload management, but delegation is limited to cgroup v2.
- AppArmor, SELinux, no-new-privileges, capabilities, mounts, namespaces, seccomp and devices remain OCI/host policy inputs.
- `--no-pivot` is explicitly documented as unsafe.

### Checkpoint and restore

- crun integrates with CRIU for checkpoint and restore.
- Options include leave-running, established TCP, external Unix sockets, shell jobs, pre-dumps, parent paths and cgroup-management modes.
- Restore can replace AppArmor/SELinux profile and mount-context information.
- CRIU configuration can be supplied through an annotation or compatibility config files.
- Pre-dumps are not independently restorable and require a final checkpoint.
- CRIU remains a separate privileged, kernel-sensitive dependency; command availability does not prove portable or application-consistent recovery.

### OCI extensions and alternative handlers

- seccomp listener descriptors can be sent to a Unix socket or handled through dynamically loaded plugins.
- Raw BPF seccomp data and fail-on-unknown-syscall behavior are supported through extensions.
- PID file-descriptor transfer, hook stdout/stderr routing, mount-context, recursive-mount and idmapped-mount extensions are available.
- Experimental handlers can route workloads through `libkrun` microVM execution or a native WASM handler.
- WASM and krun execution are alternative handlers under crun, not evidence that ordinary OCI isolation became a VM or WASM sandbox automatically.
- Dynamic seccomp plugins and custom handlers broaden the trusted runtime surface.

### Security and conformance lessons

- Current release notes include fixes for rootfs `/dev` symlink escape risk, delegated-cgroup path traversal, wrong-user execution, proc hardening and mount handling.
- These fixes show that a conformant low-level runtime remains a highly security-sensitive component.
- Container-ID validation is aligned with runc expectations, again showing observable compatibility details can differ across implementations.
- OCI conformance does not guarantee identical state, mount, signal, cgroup, rootless, seccomp, checkpoint or extension behavior.
- Published speed/memory examples are useful directional evidence only and must be remeasured on Ptah workloads and Nodes.

## What crun contributes

- A mature low-memory and low-startup-overhead baseline OCI runtime.
- An embeddable `libcrun` path for tightly controlled Provider implementations.
- Strong rootless, cgroup v2 and systemd integration evidence.
- CRIU checkpoint/pre-dump/restore machinery.
- Cross-runtime conformance and compatibility comparison against runc/youki.
- Advanced seccomp-notify, idmapped-mount and delegated-cgroup patterns.
- Optional krun microVM and WASM handler experiments.
- A useful runtime for low-resource Linux Nodes and container-heavy workloads.

## Important limitations for Ptah

- crun remains ordinary host-kernel container isolation.
- C implementation and privileged setup create a high-value memory-safety and host-interface attack surface.
- Rootless reduces ambient privilege but is not equivalent to gVisor, Kata, Firecracker or a full VM.
- `libcrun` embedding can enlarge the blast radius if loaded into a privileged long-lived Ptah process.
- GPL/LGPL component boundaries require formal distribution/linking review.
- Dynamic seccomp plugins, hooks, custom handlers and preserved file descriptors can execute or expose host-authority paths.
- cgroup/systemd behavior varies by host configuration and versions.
- CRIU checkpointing is kernel, namespace, cgroup, LSM, filesystem, socket and workload sensitive.
- Alternative `krun` and WASM handlers have different isolation and compatibility properties and require separate Provider classes/evidence.
- Experimental mount and seccomp extensions may change and cannot define stable Ptah contracts.
- crun does not supply image management, network policy, scheduling, durable Activities, Object permissions or credential handling.
- crun IDs and state paths are not canonical Ptah identities.

## Must not be inherited

- crun/container IDs or state directories as Ptah Workspace, Activity, Provider or Session identities;
- low memory or startup time described as stronger security;
- rootless execution described as tenant-grade isolation;
- `libcrun` loaded inside Ptah Core without a narrow audited process boundary;
- CLI/runtime GPL and library LGPL obligations treated as interchangeable;
- `--no-pivot`, broad preserved FDs, arbitrary hooks, dynamic seccomp plugins or custom handlers enabled by default;
- experimental OCI annotations exposed as stable public Ptah contracts;
- CRIU checkpoint creation reported as portable, secure or application-consistent recovery;
- crun WASM/krun handlers treated as equivalent to a dedicated Deno/WASM or Firecracker/Kata Provider;
- README performance numbers generalized beyond their exact host/version/workload;
- silent runtime substitution when behavior differs.

## Integration decision

**ADAPT CRUN AS A PRIMARY LOW-OVERHEAD BASELINE OCI RUNTIME OPTION AND CROSS-RUNTIME CONFORMANCE DONOR; KEEP IT BELOW THE PTAH OCI PROVIDER CONTRACT AND OUTSIDE CORE.**

Recommended Ptah role:

1. containerd/OCI remains the stable Provider interface;
2. runc, crun and youki are replaceable baseline runtime implementations;
3. crun is preferred only where measured startup/memory, systemd or rootless characteristics justify it;
4. `libcrun` may be used only through a dedicated minimal Provider worker after licence and blast-radius review;
5. runtime identity records exact binary, build, licence, kernel, cgroup, LSM, seccomp and extension configuration;
6. hooks, seccomp listeners/plugins, FDs and custom handlers require explicit capability approval;
7. krun microVM and WASM modes are represented as separate runtime/handler capability variants;
8. higher-risk or incompatible workloads escalate to gVisor, Kata, Firecracker or full VM;
9. checkpoint/restore remains disabled until exact CRIU/runtime/kernel/workload conformance is proven;
10. Ptah retains image, network, storage, credential, Activity, Receipt, Object and proof authority.

## Licence decision

- Executable/source distribution must account for GPL-2.0 terms recorded at the repository root.
- Inspected `libcrun` code declares LGPL-2.1-or-later; linking and modification obligations require separate legal review.
- Dependencies such as libseccomp, systemd, json-c, CRIU, libkrun and WASM runtimes require independent licence/provenance records.
- Architecture study and subprocess use do not remove distribution obligations for packaged binaries or modified source.

## Native Ptah gap

Ptah must define:

- baseline OCI Provider and runtime-implementation identities;
- executable versus embedded-library deployment class;
- component licence/linking/provenance records;
- Node kernel, cgroup, namespace, LSM, seccomp, userns and systemd capability snapshots;
- OCI configuration generated from Ptah permission policy;
- hook, seccomp-notify/plugin, FD and handler capability grants;
- runtime state/lifecycle mapping to Activity, attempt and Receipt identities;
- cross-runtime golden conformance corpus;
- CRIU checkpoint Artifact, secrecy, compatibility and restore proof;
- krun/WASM handler capability and isolation records;
- vulnerability, upgrade, rollback and active-container policy;
- escalation to stronger isolation without identity loss.

## Exit strategy

Ptah's OCI Provider contract remains independent. A Node may use runc, crun, youki or another compatible implementation without changing Workspace, Activity, Object, Package or caller identity.

## Validation required

1. Run the same golden OCI workload through runc, crun and youki and compare lifecycle/state output.
2. Compare rootless/rootful, cgroupfs/systemd, namespace, mount, capability, seccomp, LSM, signal and resource behavior.
3. Measure current startup, RSS and high-container-density behavior on target Nodes.
4. Attempt hostile mount, device, capability, hook, preserved-FD, seccomp-plugin and handler requests and deny them before invocation.
5. Run crun CLI and a dedicated `libcrun` worker and compare blast radius, lifecycle and failure isolation.
6. Validate GPL/LGPL packaging and linking decisions before distribution.
7. Checkpoint/pre-dump/restore selected workloads with exact CRIU/runtime/kernel/LSM compatibility evidence.
8. Reject incompatible or application-inconsistent restore.
9. Test krun and WASM handlers as separately classified Providers, not as ordinary crun behavior.
10. Upgrade/rollback crun and rerun the golden conformance/security corpus.
11. Switch a Workspace between baseline runtimes without changing Ptah identities.
12. Escalate a workload to gVisor/Kata/Firecracker when risk or compatibility requires it.
