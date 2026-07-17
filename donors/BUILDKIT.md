# Donor Record — BuildKit

**Phase:** 0A / WP03  
**Status:** FIRST-PASS COMPLETE — LOW-LEVEL BUILD ENGINE CANDIDATE  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/moby/buildkit
- Default branch: `master`
- Pinned commit: `6dd06999d5d369a217c3f3259a420f507e2db2c7`
- Licence: Apache-2.0
- Activity: Active and widely used
- Classification: Mature low-level build graph, cache and worker machinery
- Ptah targets: reproducible builds, concurrent dependency graphs, cache import/export, distributed workers, secret mounts, multiple output formats and build evidence

## Files/components inspected

- `README.md`
- `LICENSE`
- `solver/pb/ops.proto`
- documented daemon/client, worker, cache, frontend, output and OpenTelemetry architecture

## Verified capabilities and patterns

- BuildKit converts source into build artifacts through an efficient and repeatable engine.
- Key features include garbage collection, pluggable frontends, concurrent dependency resolution, instruction caching, cache import/export, nested jobs, distributable workers, multiple outputs and rootless execution.
- `buildkitd` and `buildctl` are separate daemon/client components.
- OCI and containerd worker backends are supported.
- LLB is a Protobuf DAG rather than a sequential shell-script model.
- LLB operations include execution, source, file, nested build, merge, diff and passthrough vertices.
- Inputs are digest-addressed and operations may carry platform and worker constraints.
- Execution metadata includes arguments, environment, working directory, user, network, security mode, valid exit codes and resource constraints.
- Secret environment values, secret mounts and SSH mounts are explicit input types.
- Cache mounts support shared, private and locked writer modes.
- Sources can include local files, OCI images, Git and HTTPS resources.
- Per-operation metadata includes cache controls, capabilities, progress groups, source maps and Linux resource limits.
- Outputs include images/registries, local directories, OCI/Docker tarballs and containerd stores.
- Build cache can be exported/imported through several backends.
- BuildKit includes OpenTelemetry support and multi-platform build paths.

## What BuildKit completes

- The mature low-level graph solver and cache engine missing from the internal Software Builder.
- Concurrent execution based on explicit dependency edges.
- Content/digest-driven cache and worker selection.
- Securely declared secret/SSH inputs rather than ordinary logged environment values.
- Pluggable frontend and output boundaries.
- Shared cache and distributed worker foundations.
- A mature OCI/container connection to the selected Ptah execution substrate.

## Important limitations for Ptah

- BuildKit is a build engine, not Ptah's universal Activity runtime or Workspace model.
- LLB is too low-level to become the public Ptah Build Recipe format.
- Build success does not prove an Artifact is semantically correct, reproduced independently, signed or accepted.
- BuildKit does not own Ptah Object, Artifact, receipt, Session or caller-review identity.
- Cache hits must still preserve enough evidence to explain what was reused.
- Secret mounts reduce exposure but do not automatically guarantee user commands cannot copy secrets into outputs/logs.
- Some exporters/cache backends are experimental.
- Checkpoint/retry semantics belong to Ptah/Temporal rather than LLB alone.
- The daemon and worker topology add operational complexity.
- BuildKit is primarily Linux/Windows daemon machinery; macOS relies on a Linux VM or remote daemon.

## Must not be inherited

- LLB digests used as public Ptah Activity or Artifact identity.
- Every Ptah Facility forced through BuildKit.
- Build completion promoted to proof or release acceptance.
- Cache contents treated as durable source-of-truth Objects.
- Secret availability treated as permission to emit secret values.
- Experimental exporters/backends selected without explicit capability status.
- Dockerfile as Ptah's only Build Recipe language.
- One daemon/worker backend made an irreversible dependency.

## Integration decision

**ADOPT AS THE PRIMARY LOW-LEVEL BUILD ENGINE CANDIDATE, BEHIND A PTAH BUILD FACILITY.**

Ptah should use BuildKit/LLB for suitable reproducible containerized build graphs while owning a higher-level Build Recipe, Activity, Object, Artifact and receipt contract.

BuildKit remains one Facility backend. Native platform builds, Apple/Windows tooling, devices, firmware and non-containerized processes may use other backends through the same Ptah contract.

## Native Ptah gap

Ptah must define:

- Build Recipe and version schema;
- source Object/commit and immutable input references;
- Node/platform/toolchain requirements;
- secret and credential references;
- build-step Activity mapping;
- cache identity, provenance and eviction semantics;
- typed outputs and Artifact relationships;
- before/after hashes, SBOM and attestation references;
- cancellation, durable recovery and retry classification;
- verification/reproduction level separate from build status;
- public-safe logs and redaction;
- backend-neutral exit path.

## Exit strategy

The Ptah Build Facility remains implementable over BuildKit, Dagger, native toolchains, Nix, platform workers or other build engines. Public Build Recipes and Artifact records do not expose BuildKit-specific schemas as canonical truth.

## Validation required

1. Execute independent branches of one build graph concurrently.
2. Re-run with unchanged inputs and prove cache reuse by digest and retained evidence.
3. Change one input and prove only affected operations re-run.
4. Export/import cache across two workers without output identity collision.
5. Pass secrets without them appearing in logs, cache metadata or final Artifacts.
6. Produce several output types and register each as a Ptah Artifact/Object.
7. Cancel and recover a long build through the Ptah Activity layer.
8. Compare BuildKit output against an alternate backend or independent reproduction.
9. Prove Build success remains separate from Artifact verification, signing and acceptance.
10. Record exact frontend, worker, platform, image, source and tool identities.
