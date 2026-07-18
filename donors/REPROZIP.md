# Donor Record — ReproZip

**Phase:** 0A / Security and reproduction completion  
**Status:** FIRST-PASS COMPLETE — PRIMARY EXECUTION-DEPENDENCY CAPTURE AND REPLAY DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/VIDA-NYU/reprozip
- Default branch: `1.x`
- Pinned commit: `44687ce73efe7a889bf7a1ea982258e2d965c766`
- Release line observed: `1.3.2`
- Licence: BSD-3-Clause
- Activity: maintenance/legacy-active rather than rapidly evolving platform
- Classification: Linux process-trace, dependency/environment capture, reproducible-experiment package and replay donor
- Ptah targets: reproducible workload capture, environment/dependency inventories, replay recipes, comparison Activities and negative reproduction evidence

## Files/components inspected

- `README.md`
- `LICENSE.txt`
- `docs/packing.rst`
- `reprozip/common.py`
- trace, configuration, packing and unpacker concepts documented by the repository

## Verified capabilities and patterns

### Trace and capture

- ReproZip traces a Linux command and child processes through system-call observation.
- Trace data is retained in a SQLite database before packing.
- The generated configuration records runs, commands, arguments, working directories, environment variables, machine/distribution information, package dependencies, other files and candidate inputs/outputs.
- Multiple traced runs can be combined into one experiment description.
- The operator can edit run commands, environment, inputs/outputs and which packages/files are included before packing.
- Trace and pack are separate stages; files are collected later from the current filesystem state.

### Package and replay

- Packing produces an `.rpz` bundle containing the configuration and selected files.
- Replays can use directory, chroot, Docker or Vagrant unpacker paths depending on plugins and host capabilities.
- Inputs may be replaced and outputs collected during replay.
- Package manager metadata can be used to reinstall some dependencies instead of embedding every file.
- The package format is useful as a portable execution capture, but replay behavior depends on the chosen unpacker, host, kernel and dependency resolution.

### Reproducibility lessons

- Capturing observed file access is stronger than relying only on a handwritten dependency list.
- Editable configuration allows an operator to remove irrelevant inputs and mark expected outputs.
- Capturing command, working directory and environment alongside files is necessary for meaningful replay.
- A reproduction package and a successful replay are distinct records.
- Reproduction should compare exact outputs, exit state and declared acceptance conditions rather than merely proving the command launched.

## What ReproZip contributes

- A concrete observed-dependency capture workflow.
- Separation of trace, editable recipe, package and replay.
- Environment, arguments, working-directory, package and file inventories.
- Explicit input/output concepts.
- Several replay backends.
- A useful donor for creating bounded reproduction bundles from legacy or poorly documented workloads.
- Strong evidence that reproducibility requires preserving execution context, not only source code.

## Important limitations for Ptah

- Packing is Linux-specific and depends on `ptrace`/kernel-observable system calls.
- It observes dependencies used during the traced runs, not every possible branch or future execution path.
- Remote APIs, databases, network services, clocks, randomness, hardware state, devices and human interactions may remain uncaptured.
- A file can change between trace and pack, causing a bundle to contain bytes different from those actually observed.
- Package-manager reconstruction may resolve different versions or repositories later.
- Kernel, architecture, CPU features, drivers and external runtime behavior are not fully reproduced by copying files.
- Sensitive files, credentials, personal data and proprietary/licensed dependencies can be captured unintentionally.
- The configuration is operator-editable; removal or alteration can weaken fidelity while still producing a valid package.
- Replay through directory/chroot/Docker/Vagrant provides different isolation and compatibility properties.
- A replay may succeed while outputs differ or hidden side effects remain unverified.
- `.rpz` identity and paths are not canonical Ptah Recipe, Object or Activity identity.
- Maintenance pace and Python/plugin dependencies require compatibility review before adoption.

## Must not be inherited

- `.rpz` creation reported as successful reproduction;
- traced dependency presence treated as a complete software bill or full execution truth;
- current file bytes packed without comparing them to the traced revision;
- remote services, randomness or device state assumed captured;
- package-manager reinstallation treated as exact dependency reproduction;
- secrets, credentials or restricted files bundled automatically;
- operator-edited configuration accepted without provenance and review;
- one unpacker/backend treated as semantically equivalent to another;
- ReproZip run IDs or paths used as Ptah identities;
- replay exit code alone treated as proof of equivalent output or side effects;
- legacy bundles executed outside an approved Isolation Class.

## Integration decision

**ADAPT REPROZIP'S OBSERVED-DEPENDENCY TRACE/PACK/REPLAY PATTERN AS AN OPTIONAL REPRODUCTION FACILITY; KEEP PTAH-NATIVE RECIPE, OBJECT, ACTIVITY, SECURITY AND PROOF CONTRACTS.**

Recommended Ptah role:

1. a Capture Activity observes one exact command/workload revision in a scoped Linux Workspace;
2. source Objects, environment, arguments, packages, files, network observations, devices and Node capability are retained as separate records;
3. captured file bytes are hashed at observation and rechecked at packaging;
4. a Reproduction Recipe remains human-readable and reviewable;
5. a Reproduction Bundle is an immutable signed Artifact assembled from approved Objects;
6. sensitive or restricted content is classified before inclusion/export;
7. replay occurs in an approved target Isolation Class with explicit network/device/credential policy;
8. replay produces a new Activity/attempt and Output Comparison, not a mutation of the original run;
9. unsupported external state is listed as an explicit limitation or supplied through separately versioned Facilities;
10. ReproZip can be replaced by native capture, ReproZip-compatible import or another reproducibility backend without identity loss.

## Native Ptah gap

Ptah must define:

- Reproduction Recipe and Recipe Revision;
- Capture Activity and observed dependency records;
- source/process/environment/package/file/network/device snapshots;
- observation-time and packaging-time content hashes;
- Reproduction Bundle Artifact and manifest;
- sensitive/licensed-content classification and export policy;
- replay backend and Isolation Class identity;
- external service fixture/reference records;
- randomness, clock, locale and hardware controls;
- Reproduction Run and attempt;
- output/side-effect Comparison and acceptance policy;
- partial/blocked/drifted/not-reproduced statuses;
- provenance, signature, SBOM and reviewer records;
- migration/import from `.rpz` without adopting ReproZip IDs.

## Exit strategy

Ptah's reproduction contracts remain backend-neutral. Native Linux tracing, BuildKit/Dagger captures, ReproZip, Nix/Guix-like environments, VM snapshots or future systems can produce Reproduction Bundles without changing Recipe, Object, Activity or Comparison identity.

## Validation required

1. Trace a workload with files, environment, subprocesses and declared inputs/outputs.
2. Change one dependency between trace and pack and detect the drift.
3. Replay the same bundle through two approved backends and compare outputs and limitations.
4. Exercise remote service, random, clock and hardware dependencies and record what remains uncaptured.
5. Detect and block a credential/private/licence-restricted file before bundle export.
6. Reinstall a package from a changed repository and prove it is not reported as exact reproduction.
7. Compare exit code, output hashes, logs and declared external side effects.
8. Retain a failed/partial replay as negative evidence.
9. Import an existing `.rpz` while assigning new Ptah identities.
10. Remove ReproZip and replay the retained Recipe/Objects through another backend.
