# Donor Record — Development Containers Specification

**Phase:** 0A  
**Status:** FIRST-PASS COMPLETE — STANDARD DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/devcontainers/spec
- Default branch: `main`
- Pinned commit: `c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421`
- Licence: CC-BY-4.0 for the specification repository
- Activity: Maintained specification
- Classification: Portable environment-description standard
- Ptah targets: reproducible container workspace definitions and compatibility

## Files/components inspected

- `README.md`
- specification layout under `docs/specs/`
- `devcontainer.json` object model
- image metadata relationship
- reference CLI and CI implementation links

## Verified capabilities and patterns

- `devcontainer.json` describes a full-featured development container.
- The format can express tools, settings, lifecycle commands and configuration for local or cloud use.
- Metadata can also be attached to container images.
- The same environment definition can be reused for development, build and test.
- The specification deliberately enriches existing container formats rather than replacing OCI/container machinery.

## What it completes

- A widely used portable environment description that OpenClaw, Daytona and Coder do not share natively.
- A compatibility path for repositories that already contain `.devcontainer` definitions.
- A reusable configuration source for local, remote and cloud providers.

## Missing capabilities for Ptah

- It is intentionally focused on development containers, not universal Ptah workspaces.
- It does not define Ptah objects, activities, sessions, artifacts, nodes, devices or graphical applications.
- It does not provide durable lifecycle, recovery, scheduling or multi-node control.
- It assumes a container-oriented environment and does not cover native, VM, device or firmware providers.

## Must not be inherited

- `devcontainer.json` as the universal Ptah workspace schema.
- Development-only assumptions imposed on media, firmware, device or application worlds.
- Lifecycle commands treated as durable Ptah activity history.

## Integration decision

**ADOPT AS A SUPPORTED IMPORT/COMPATIBILITY STANDARD.**

Ptah should read and execute Dev Container definitions through an adapter while retaining a richer native workspace manifest.

## Native Ptah gap

- map Dev Container properties to Ptah provider capabilities and activities;
- preserve lock, image and feature identity in provenance;
- represent unsupported or provider-specific properties honestly;
- combine the Dev Container definition with Ptah objects, sessions, storage and facilities.

## Exit strategy

Ptah workspaces remain describable without Dev Containers. The adapter can be replaced while native Ptah contracts remain stable.

## Validation required

- Import representative Dockerfile, image and Compose-based Dev Containers.
- Prove consistent behavior on local and remote providers.
- Prove lifecycle commands appear as Ptah activities with logs and artifacts.
- Prove a non-development Ptah workspace does not require `devcontainer.json`.
