# Donor Record — crun

**Phase:** 0A / WP11  
**Status:** FIRST-PASS COMPLETE — LOW-MEMORY OCI RUNTIME AND EMBEDDABLE LIBRARY DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/containers/crun
- Owner/organisation: `containers`
- Default branch: `main`
- Pinned commit: `fb54bc00bf4a9139e74ba68e00da22b424b90912`
- Licence state: root runtime distribution uses GPL-2.0; `libcrun` source inspected carries LGPL-2.1-or-later notices; file/component-level review is mandatory
- Activity: Active
- Primary language: C
- Classification: fast low-memory OCI runtime, embeddable runtime library, live-resource update and CRIU checkpoint/restore donor
- Ptah targets: baseline OCI implementation alternatives, constrained/edge Nodes, library embedding analysis, rootless execution, live cgroup updates and checkpoint compatibility

## Files/components inspected

- `README.md`
- `COPYING`
- `crun.1.md`
- `src/libcrun/container.h`
- current repository/commit activity
- lifecycle, cgroup, rootless, seccomp/LSM, live-mount and CRIU command boundaries

## Verified capabilities and patterns

### OCI runtime and library role

- crun is a C implementation of the OCI runtime specification.
- It supports create, run, start, state, list, exec, kill, pause, resume, update, checkpoint, restore and delete operations.
- It is designed for low startup latency and memory overhead.
- `libcrun` exposes the runtime as an embeddable library rather than requiring every caller to shell out to a separate CLI process.
- It is commonly integrated through Podman/containers tooling and ordinary OCI managers.

### Linux runtime controls

- Supports rootful and rootless OCI configurations.
- Supports cgroupfs, systemd and disabled cgroup-manager modes.
- Resource updates can modify CPU, memory, swap, PIDs, cpusets and block-I/O controls on a running container.
- Exec supports AppArmor profiles, SELinux/process labels, no-new-privileges, cgroup placement, users, environment and additional capabilities.
- OCI extensions include mount-context handling and seccomp receiver integration.
- Experimental live mount add/remove commands demonstrate runtime mutation but are not stable contracts.
- `--no-pivot` is explicitly documented as unsafe and should be avoided.

### Checkpoint and restore

- Uses CRIU for checkpoint and restore.
- Checkpoint options include leave-running, established TCP, external Unix sockets, shell jobs, pre-dump and parent-layer paths.
- Restore supports cgroup-management modes and LSM profile/mount-context replacement.
- Pre-dumps are not independently restorable and require a final checkpoint.
- Open sockets, LSM labels, cgroups, mounts and parent image paths materially affect restore behavior.
- These controls are richer than a simple checkpoint command but still do not prove portable or application-consistent migration.

### Performance and footprint lessons

- The project targets lower latency and memory use than runc and publishes narrow benchmark examples.
- The README's example also shows crun faster than the older tested youki/runc versions, but the result is host/version/workload specific.
- C implementation and library embedding reduce process/runtime overhead but enlarge the memory-safety and in-process trust considerations compared with a memory-safe runtime.
- Static/reproducible builds are available through a Nix path for selected targets.

### State and lifecycle details

- Rootful state defaults under `/run/crun`; rootless state follows `XDG_RUNTIME_DIR`.
- State directories and container IDs are runtime-local.
- Force and regular-expression operations can affect running or multiple containers and require strong caller scoping.
- Recent source activity includes lifecycle/state cleanup fixes, underscoring that low-level runtime correctness continues to evolve.

## What crun contributes

- A mature, low-overhead baseline OCI runtime candidate.
- An embeddable library interface for controlled runtime integration.
- Rootless and systemd/cgroupfs behavior.
- Live resource-update controls.
- AppArmor, SELinux, no-new-privileges and seccomp-listener integration lessons.
- Detailed CRIU checkpoint/pre-dump/restore options.
- A useful independent implementation for cross-runtime conformance and performance testing.
- Reproducible static-build direction.

## Important limitations for Ptah

- crun remains ordinary Linux-container isolation and shares the host kernel.
- C implementation increases memory-safety risk in a security-critical low-level component.
- Embedding `libcrun` places runtime code inside the host process and can enlarge the failure/trust boundary.
- Rootless mode is not equivalent to gVisor, Kata or VM isolation.
- Experimental live mount mutation can bypass expected immutable mount assumptions if exposed carelessly.
- `--force`, regex operations, preserved file descriptors, extra capabilities and `--no-pivot` can materially broaden risk.
- CRIU restore depends on host kernel, CRIU, cgroups, LSM, mounts, sockets and workload behavior.
- OCI conformance does not guarantee identical behavior to runc/youki.
- Benchmark claims are narrow and must not drive runtime selection without current target-Node measurements.
- The runtime does not provide image, network policy, storage, scheduling, credentials, Activity durability, proof or Object permissions.
- `crun` IDs/state paths/PIDs are not Ptah identities.
- GPL/LGPL component boundaries require careful legal packaging and linking review.

## Must not be inherited

- crun IDs/state directories as Ptah Workspace, Activity, Provider or Session identity;
- crun described as a stronger isolation class because it is small or fast;
- rootless mode described as tenant-grade containment;
- `libcrun` linked into Ptah Core without licence, failure-boundary and security review;
- README benchmark numbers generalized to current Ptah workloads;
- live mount add/remove exposed under ordinary process permission;
- `--no-pivot`, broad capabilities, preserved file descriptors or force/regex operations enabled by default;
- CRIU checkpoint success reported as portable/application-consistent recovery;
- LSM/cgroup restore changes applied without exact policy and evidence;
- GPL-covered source copied into incompatible proprietary/private components;
- runtime switching performed silently when behavior differs.

## Integration decision

**ADAPT CRUN AS AN OPTIONAL BASELINE OCI RUNTIME AND LOW-RESOURCE NODE CANDIDATE; PREFER PROCESS/CLI WRAPPING UNLESS A FORMAL LIBCRUN LICENCE AND FAILURE-BOUNDARY REVIEW APPROVES EMBEDDING.**

Recommended Ptah role:

1. containerd/OCI remains the stable baseline Provider contract;
2. runc, crun and youki are replaceable low-level runtime implementations;
3. crun is a strong candidate for low-memory/fast-start trusted workloads;
4. `libcrun` remains optional and separately reviewed;
5. rootless is recorded as a privilege mode, not a strong Isolation Class;
6. live mount/resource mutation requires dedicated high-risk Facility methods and Receipts;
7. CRIU checkpoint/restore is disabled until exact runtime/kernel/CRIU/LSM/workload conformance passes;
8. higher-risk workloads escalate to gVisor, Kata, Firecracker or full VMs;
9. Ptah owns all permission, Object, network, credential, Activity and proof contracts.

## Licence decision

- The root program is distributed under GPL-2.0.
- Inspected `libcrun` headers carry LGPL-2.1-or-later notices.
- Running or separately invoking crun is generally the cleanest integration boundary.
- Embedding/linking `libcrun`, modifying/distributing crun or packaging static binaries requires formal file/component-level licence review and corresponding source/notice obligations.
- Dependencies such as libseccomp, libcap, systemd, json-c and CRIU require separate review.

## Native Ptah gap

Ptah must define:

- baseline OCI Provider and implementation identity;
- process-wrapper versus embedded-library integration class;
- runtime binary/library version, build, signature, SBOM and licence records;
- Node kernel, architecture, cgroup, LSM, namespace and seccomp capabilities;
- rootful/rootless privilege mode;
- OCI config and extension policy generated from Ptah permissions;
- live resource/mount mutation Activities and rollback evidence;
- runtime state/lifecycle mapping to Activity/attempt/Receipt identities;
- CRIU image Artifact, secrecy, compatibility and restore proof;
- cross-runtime behavior/conformance corpus;
- runtime upgrade, vulnerability and active-workload policy;
- stronger-isolation escalation and fallback records.

## Exit strategy

Ptah's OCI Provider contract remains independent. A Node may use runc, crun, youki or another OCI runtime without changing Workspace, Activity, Object or Package identity.

## Validation required

1. Run one golden OCI workload through runc, crun and youki and compare lifecycle/state semantics.
2. Compare namespaces, mounts, devices, capabilities, seccomp, LSM, signals and cgroups.
3. Measure current startup/memory behavior on target Nodes.
4. Exercise rootful/rootless and systemd/cgroupfs modes.
5. Deny unsafe `no-pivot`, preserved-FD, capability, regex/force and live-mount requests through Ptah policy.
6. Apply live resource updates and retain before/after resource/Receipt evidence.
7. Checkpoint/pre-dump/restore selected workloads and retain CRIU/runtime/kernel/cgroup/LSM compatibility evidence.
8. Reject incompatible or application-broken restore.
9. Compare process-wrapped crun with an isolated libcrun prototype for licence, crash and privilege boundaries before any embedding decision.
10. Upgrade/rollback crun and compare the golden conformance corpus.
11. Replace crun with another OCI runtime without changing Ptah identities.
12. Escalate incompatible/high-risk workloads to gVisor/Kata/Firecracker without silent weakening.
