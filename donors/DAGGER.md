# Donor Record — Dagger

**Phase:** 0A / WP03  
**Status:** FIRST-PASS COMPLETE — TYPED RECIPE AND MODULE DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/dagger/dagger
- Default branch: `main`
- Pinned commit: `dc12c3ab1f7fda6b938f81d0f23d853e1a9392c8`
- Licence: Apache-2.0
- Activity: Active
- Classification: Typed programmable delivery graph, module and observability donor
- Ptah targets: Build Recipe ergonomics, typed inputs/outputs, reusable execution modules, content-addressed artifacts, secrets, services/tunnels, local/CI portability and OpenTelemetry traces

## Files/components inspected

- `README.md`
- `LICENSE`
- `core/service.go`
- `core/schema/container.go`
- BuildKit/containerd/OCI integration imports and persisted service-object model

## Verified capabilities and patterns

- Dagger runs programmable delivery workflows locally, in CI or in cloud infrastructure.
- It exposes a typed System API over containers, filesystems, secrets, Git repositories, services and tunnels.
- SDKs exist across several languages and are generated from the shared API schema.
- Custom typed objects can cross module and SDK-language boundaries.
- Operations are incremental and content-addressed by inputs.
- Every operation emits OpenTelemetry traces.
- Dagger depends on container runtime/BuildKit machinery rather than replacing low-level execution.
- Services are represented as content-addressed/persisted objects with container, arguments, execution metadata, module context, upstream tunnels, ports and host sockets.
- Persisted service references retain dependencies by result identity.
- Container schema includes platform selection, OCI image pull, Dockerfile build, files/directories, user/workdir/environment operations and explicit secret variables.
- Secrets are represented separately from ordinary environment values.
- Volatile values that intentionally do not invalidate cache are marked as an expert escape hatch with stale-result warning.
- OCI labels, image metadata, healthcheck-related state and service tunnels are represented through typed schema operations.

## What Dagger completes

- A higher-level typed and composable layer above BuildKit/containers.
- Reusable modules and cross-language SDK ergonomics.
- Explicit inputs, outputs, filesystems, services, tunnels and secrets.
- Content-addressed typed intermediate objects.
- Local/CI portability and built-in OTel traces.
- A strong reference for Ptah Build Recipe and Facility-module APIs.

## Important limitations for Ptah

- Dagger is primarily software-delivery/container oriented, not Ptah's universal Activity or Domain Pack system.
- Its typed objects/result IDs are Dagger-engine identities, not Ptah Objects/Artifacts.
- It requires container runtime machinery and does not cover all native Windows/macOS/device/firmware operations.
- A Dagger function completing does not prove independent reproduction, signing or external acceptance.
- Content-addressed cache/object behavior is engine-specific and cannot become Ptah's only durable storage catalogue.
- Volatile inputs can intentionally bypass cache invalidation and therefore require explicit provenance warnings.
- Service tunnels and sockets are runtime resources, not durable Ptah Session truth by themselves.
- Dagger modules/functions may execute arbitrary code and require caller/provider permission and secret boundaries.
- Its GraphQL/API/module model is richer and more complex than the first Ptah vertical slice requires.

## Must not be inherited

- Dagger's engine object/result IDs as public Ptah Object identity.
- Every Ptah Activity forced into a Dagger function or container.
- Container-only assumptions for all Build/Facility work.
- Cache hits interpreted as independent verification.
- Volatile variables used without explicit non-reproducibility receipts.
- Secret references copied into logs, outputs or public recipes.
- Dagger module registry/product identity as Ptah's universal plugin lifecycle.
- Build/test/deploy success automatically promoted to release acceptance.

## Integration decision

**ADAPT AS THE PRIMARY TYPED BUILD-RECIPE/MODULE DONOR; OPTIONAL EXECUTION BACKEND.**

BuildKit is the low-level engine candidate. Dagger informs or may implement the typed recipe/module layer for suitable workloads. Ptah still owns the neutral Build Recipe, Activity, Object, Artifact, Facility and receipt contracts.

Dagger may run as a Ptah Facility backend or host reusable build/test modules, but must remain replaceable.

## Internal Software Builder comparison

Dagger fills several missing parts of the internal Builder:

- actual typed executable graph rather than only scan/plan output;
- local/CI portability;
- content-addressed incremental execution;
- polyglot SDKs;
- explicit secret inputs;
- built-in traces;
- reusable modules and typed intermediate results.

The internal Builder still contributes requirements Dagger does not own:

- Project scanning and framework/target readiness;
- human correction of detected project type;
- shared tool/cache versus Project-source separation;
- private signing, branding and release-control adapters;
- platform-specific target planning and blocked reasons;
- user-facing Builder/Installer design.

## Native Ptah gap

Ptah must define:

- backend-neutral Build Recipe and module manifest;
- recipe version, source hashes, exact tool/image/environment identity;
- typed inputs/outputs mapped to Ptah Objects and Artifacts;
- secret/credential references and redaction;
- reproducibility classification including volatile/non-cache-affecting inputs;
- durable Activity and cancellation/recovery integration;
- Facility permissions/resources/platform requirements;
- cache provenance and eviction rules;
- review, attestation, SBOM and signing references;
- non-container/native execution path;
- private adapter separation for branding/signing/release policies.

## Exit strategy

Build Recipes remain portable Ptah records. They may compile to Dagger, BuildKit/LLB, native commands, platform workers or other engines. Dagger modules can be hosted without making Dagger mandatory.

## Validation required

1. Express one build/test pipeline through a typed recipe with explicit source, secret, service and Artifact outputs.
2. Run it locally and on a remote/CI worker with identical input identities.
3. Demonstrate content-addressed cache reuse and invalidate only affected operations.
4. Prove a volatile input is marked non-reproducible and cannot silently influence a trusted Artifact.
5. Trace every operation through OpenTelemetry and link it to Ptah Activities/Artifacts.
6. Replace the Dagger backend with direct BuildKit/native execution for one representative recipe without changing public Ptah records.
7. Keep private signing/branding steps outside the public recipe while retaining proof references.
8. Demonstrate a non-container platform build through a separate backend under the same Build Facility contract.
