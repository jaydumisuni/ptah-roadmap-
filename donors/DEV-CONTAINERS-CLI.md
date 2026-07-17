# Donor Record — Dev Container CLI

**Phase:** 0A  
**Status:** FIRST-PASS COMPLETE — REFERENCE IMPLEMENTATION DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/devcontainers/cli
- Default branch: `main`
- Pinned commit: `f683c29f64a20109b4453e5149807e390ff65133`
- Licence: MIT
- Activity: Active at the inspected pin
- Classification: Reference implementation for Dev Container compatibility
- Ptah targets: build, up, lifecycle commands, configuration reading, command execution and feature lockfiles

## Files/components inspected

- `README.md`
- CLI command surface
- lockfile behavior
- build/up/exec lifecycle
- relationship to Dev Container Specification

## Verified capabilities and patterns

- Builds or prebuilds Dev Container images.
- Starts and configures a container from `devcontainer.json`.
- Runs lifecycle commands such as `postCreateCommand`.
- Reads normalized workspace configuration.
- Executes commands with the configured user and environment.
- Supports Features and Templates.
- Generates `.devcontainer-lock.json` to pin feature versions and supports frozen lockfiles.
- Supports Docker Compose and simplified single-container environments.

## Important limitations

- `stop` and `down` remain explicitly incomplete in the inspected CLI status.
- It is a CLI/reference implementation, not a persistent control plane.
- It relies on Docker-oriented execution and does not provide Ptah activity recovery, provider placement or object/session state.
- It does not replace BuildKit, containerd or Ptah's Workspace Provider contract.

## Integration decision

**WRAP OR SELECTIVELY ADAPT FOR DEV CONTAINER COMPATIBILITY.**

The CLI may initially be invoked as a tool adapter while Ptah develops a stable native compatibility layer. MIT permits adaptation with notices.

## Must not be inherited

- CLI process lifetime as workspace truth.
- Docker command output as Ptah's canonical state.
- Incomplete stop/down behavior hidden from callers.
- Dev Container lifecycle commands executed without Ptah activity records.

## Native Ptah gap

- provider-neutral orchestration around the CLI;
- idempotent create/up and lifecycle tracking;
- explicit stop/delete support through Ptah providers;
- object, artifact and provenance capture;
- command cancellation and durable recovery;
- conformance across several providers.

## Exit strategy

Ptah can replace the CLI wrapper with native spec processing or another conforming implementation without changing public workspace contracts.

## Validation required

- Execute the same locked Dev Container using the CLI wrapper and a later native adapter.
- Verify lockfile and exact feature/image provenance.
- Record every lifecycle command as a separate Ptah activity.
- Report unsupported stop/down capabilities explicitly.
