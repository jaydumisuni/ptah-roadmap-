# Donor Record — ClawHub

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — PLUGIN/SKILL REGISTRY, VERSIONING AND LIFECYCLE DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/openclaw/clawhub
- Default branch: `main`
- Pinned commit: `efa3dc7af7673d09d44625c28bbe106978110fbf`
- Licence: MIT
- Activity: Active
- Classification: public registry, package catalogue, skill/plugin metadata, install/update/pin and security-review donor
- Ptah targets: `PLUGIN-001`, discovery, inspection, versioning, compatibility, trust/capability labels, install state, pinning, update, removal and registry UX

## Files/components inspected

- `README.md`
- `LICENSE`
- `docs/skill-format.md`
- `docs/cli.md`
- `specs/plans/plugins.md`
- package/skill/API/schema and security-analysis references

## Verified capabilities and patterns

### Registry and identity

- Provides a public skill registry and an emerging package catalogue for code plugins and bundle plugins.
- Separates family identity: skill, code plugin and bundle plugin.
- Supports canonical names, version history, tags, aliases, rename and merge workflows.
- Treats package identity and public route/locator as related but not necessarily identical.
- Uses a unified catalogue/search direction while preserving family-specific publish/install semantics.

### Discovery and inspection

- Supports search, explore and inspect-without-installing.
- Search combines exact/name relevance, embeddings/vector search and a small popularity prior.
- Package/skill detail can expose owner, family, trust, capability and version metadata.
- Explicitly distinguishes code-executing plugins from content/bundle-only packages.

### Publish and versioning

- Skills use text bundles with a required `SKILL.md` and frontmatter metadata.
- Publish creates versions and tags; dry-run and machine-readable output are supported.
- Local fingerprints prevent redundant publish and detect changed installations.
- Native code-plugin direction requires manifests, extension entries and explicit compatibility/build metadata.
- Proposed plugin compatibility uses a stable semantic `pluginApiVersion`/range rather than daily application versions.
- Exact build-time application/SDK versions are retained as provenance/diagnostic metadata.

### Runtime requirements and capabilities

- Skill metadata can declare required/optional environment variables, binaries, config files, OS restrictions and install specs.
- Security analysis checks declared requirements against observed content behavior.
- Plugin planning requires visible family, code-execution status, plugin ID, providers/channels/tools/hooks/services/routes, config schema and dependency-materialization status.
- High-confidence capability reporting favors declared/registered surfaces over speculative behavior inference.

### Install/update/remove lifecycle

- CLI writes origin metadata and a workdir lockfile.
- Install downloads a versioned bundle and refuses to overwrite pinned installs.
- Pins may include reasons and block direct/forced updates.
- Update computes local fingerprints; locally modified files cause refusal unless explicitly overridden, while pinned installs remain protected.
- Uninstall removes the local install and lock entry.
- Registry deletion is soft/restore by default; hard delete is controlled.
- Rename and merge preserve redirects/canonicalization.

### Trust and security

- Supports asynchronous scans and downloadable scan-report bundles.
- Scan reports may remain available even for blocked/hidden versions.
- Open community publishing is paired with moderation, verification, scans, provenance and conservative code-plugin install UX.
- Trust is communicated through labels/channels rather than assuming every published package is safe.
- Install telemetry is minimal and can be disabled.

## What ClawHub completes

- A mature registry and lifecycle reference for skills, code plugins and bundle plugins.
- Inspect-before-install behavior.
- Family and executes-code distinction.
- Version, tag, fingerprint, origin, lockfile and pin patterns.
- Compatibility contract separated from application release version.
- Declared runtime requirements and capability summaries.
- Security scan/report, moderation and provenance UX.
- Rename, merge, soft delete and restore lifecycle.
- Registry CLI and API patterns.

## Important limitations for Ptah

- ClawHub is OpenClaw-specific and cannot define Ptah Facility, Domain Pack, Panel or Recipe identity.
- The current skill model is optimized for text bundles and is not a universal executable plugin format.
- The first-class code-plugin registry model is still evolving in planning/implementation.
- Capability declarations and static scans do not prove actual runtime behavior or safety.
- Open publishing substantially increases supply-chain risk.
- A registry's trust label, popularity or moderation status does not equal Ptah approval.
- Skill instructions may influence external reasoning systems; Ptah must not treat them as trusted policy.
- Install specs can invoke ecosystem package managers and execute supply-chain code.
- Lockfiles and local fingerprints are local install state, not canonical Artifact/Activity truth.
- Convex, GitHub OAuth and OpenAI embeddings are implementation choices rather than required Ptah infrastructure.
- ClawHub's mandatory MIT-0 licence for published skills cannot be assumed suitable for all Ptah plugin registries or private plugins.
- Version tags such as `latest` are mutable aliases and cannot define immutable plugin identity.

## Must not be inherited

- OpenClaw/ClawHub package, skill or plugin IDs as canonical Ptah identities;
- public registry presence treated as approval or safe installation;
- instructions/prompts inside skills treated as Ptah policy;
- code plugins and content bundles presented under one indistinguishable install action;
- mutable tags used as immutable version identity;
- arbitrary package-manager install scripts run in Ptah Core;
- registry trust/moderation labels promoted to proof of runtime safety;
- one registry, Convex or embedding provider made mandatory;
- ClawHub's MIT-0 publication policy forced on private/public Ptah plugins;
- force update overwriting locally modified or pinned production plugins;
- plugin application-version coupling used instead of explicit API compatibility.

## Integration decision

**ADAPT CLAWHUB AS THE PRIMARY REGISTRY/DISCOVERY/LIFECYCLE DONOR; BUILD PTAH-NATIVE PLUGIN IDENTITY, TRUST, PERMISSION AND RUNTIME CONTRACTS.**

Recommended architecture:

1. one Ptah Package catalogue may index Facility plugins, Domain Packs, UI contributions, Recipes and bundle/content packages;
2. package family and executes-code status are mandatory and prominent;
3. immutable package/release Artifacts are content-addressed and signed;
4. registry/alias/tag identity remains separate from exact release identity;
5. inspect, scan, permission review and compatibility check precede installation;
6. installed state records source, exact version, digest, permissions, runtime and local modifications;
7. pins block automatic/forced upgrades;
8. updates stage, validate, health-check and support rollback;
9. private and public registries share contracts but may use different publication/licence policies;
10. MCP, Deno, OCI, native service and content-only bundles remain distinct plugin/runtime classes.

## Native Ptah gap

Ptah must define:

- Package, Plugin, Release and Installed Plugin identities;
- plugin families and executes-code classification;
- manifest schema covering Facilities, Domain Packs, panels, Recipes, tools and services;
- stable plugin API/capability version ranges;
- exact source/build/runtime/SDK provenance;
- immutable digest/signature/SBOM/attestation relationships;
- permission/resource/network/filesystem/credential declarations;
- install plan and dependency/materialization receipts;
- registry trust, reviewer, scan and caller-approval records;
- activation, health, degraded and quarantine states;
- staged upgrade, migration, rollback and pin semantics;
- local modification/fingerprint handling;
- removal, data-retention and orphaned-state cleanup;
- private/public registry and licence-policy separation;
- registry replacement/mirroring and offline install.

## Exit strategy

Ptah's plugin/package contracts remain independent. ClawHub, OCI registries, Git repositories, local bundles, MCP registries or private catalogues can supply packages without changing Plugin/Release/Installed identity.

## Validation required

1. Publish and inspect content-only and code-executing packages with visibly different families and permission surfaces.
2. Resolve mutable aliases to immutable signed release digests before installation.
3. Refuse a package with incompatible plugin API range or undeclared critical capabilities.
4. Install into a scoped runtime, health-check and retain exact source/digest/dependency receipts.
5. Pin an installed version and reject automatic/forced updates.
6. Detect local modification and require an explicit preserve/replace decision.
7. Stage an upgrade, run migration/conformance tests and rollback after failure.
8. Quarantine a package after a security finding without deleting historical evidence.
9. Remove a plugin and explicitly retain/delete its data through a cleanup plan.
10. Replace the registry or install offline without changing Plugin/Release identity.
