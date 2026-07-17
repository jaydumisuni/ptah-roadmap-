# Donor Record — DevPod

**Phase:** 0A  
**Status:** FIRST-PASS COMPLETE — PROVIDER PORTABILITY DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/loft-sh/devpod
- Default branch: `main`
- Pinned commit: `5a0efcbff6610ab114b421f68a890739a452e66b`
- Licence: MPL-2.0
- Activity: Active at the inspected pin
- Classification: Provider and portable workspace completion donor
- Ptah targets: local/remote/cloud provider model, Dev Container portability, client-side workspace control and credential bridging

## Files/components inspected

- `README.md`
- `LICENSE`
- `pkg/provider/provider.go`
- provider-development documentation
- workspace client and machine-provider search results

## Verified capabilities and patterns

- Client-only workspace manager built around the Dev Container standard.
- Providers can target local computers, Kubernetes, reachable remote machines or cloud VMs.
- The same workspace is managed consistently across provider locations.
- Provider configuration includes version, source, options, binaries, agent behavior and command hooks.
- Agent configuration supports inactivity shutdown, container inactivity, Git credential injection and Docker credential injection.
- Docker, Kubernetes and custom drivers are represented separately.
- Custom drivers may define find, command, run, start, stop, delete, logs and reprovision capability.
- Provider binaries are selected by OS/architecture and carry checksums.

## What DevPod completes

- A stronger provider plug-in model than one fixed workspace service.
- Local-first and remote-machine parity.
- A practical separation between provider machine operations and Dev Container setup.
- Provider-delivered binaries and checksum-aware distribution.
- Credential synchronization and inactivity lifecycle patterns.

## Important limitations

- DevPod remains development-container centric.
- It is client-only rather than a durable multi-user Ptah control plane.
- Provider commands are command arrays and do not provide Ptah-level typed activity, object, session and provenance contracts.
- MPL-2.0 requires file-level licence compliance for modified source.
- It does not cover universal Ptah facilities, firmware, devices or non-container application environments.

## Must not be inherited

- Provider shell commands as Ptah's canonical internal protocol.
- Dev Container as the only environment type.
- Credential copying without Ptah credential-reference and audit semantics.
- Client-local state as the universal source of workspace truth.
- MPL-covered source copied into native Ptah files without licence review.

## Integration decision

**ADAPT PROVIDER CONTRACT PATTERNS; PROTOCOL-COMPATIBILITY POSSIBLE.**

DevPod is a major completion donor for `CORE-001`, `EXEC-002`, `SESSION-001` and provider portability. Ptah owns a richer provider contract and may later support DevPod providers through an adapter.

## Native Ptah gap

- typed provider capabilities and lifecycle responses;
- idempotency, cancellation, activity status and durable history;
- Node Protocol integration;
- object/storage/session identity independent of provider paths;
- graphical, VM, native, device and specialist provider families;
- centralized state with local/offline operation;
- credential references rather than uncontrolled secret copying.

## Exit strategy

The Ptah Workspace Provider contract must support direct native providers and optional DevPod-provider compatibility. DevPod cannot become required infrastructure.

## Validation required

- Map at least local, SSH/remote and cloud-style providers into one Ptah conformance suite.
- Prove provider capability discovery and unsupported-operation reporting.
- Prove credential use is reference-based and audited.
- Prove a provider can be replaced without changing workspace/object/session identity.
