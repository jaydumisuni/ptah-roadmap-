# Donor Record — ClawHub

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — PRIMARY PLUGIN/SKILL REGISTRY, VERSIONING AND LIFECYCLE DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/openclaw/clawhub
- Owner/organisation: `openclaw`
- Default branch: `main`
- Pinned commit: `aaa73625ed4100b1006653f49089f2a2d969a427`
- Licence: MIT for ClawHub source; published skill content uses ClawHub's separate MIT-0 publication policy
- Activity: Active
- Classification: public registry, package catalogue, skill/plugin metadata, install/update/pin and security-review donor
- Ptah targets: `PLUGIN-001`, discovery, inspection, versioning, compatibility, trust/capability labels, install state, pinning, update, removal, quarantine and registry UX

## Files/components inspected

- `README.md`
- `LICENSE`
- `docs/cli.md`
- `specs/plans/plugins.md`
- skill/package/API/schema and security-analysis references
- current repository/commit activity

## Verified capabilities and patterns

### Registry and package identity

- ClawHub is the public skill registry for OpenClaw and now exposes a native package catalogue for code and bundle plugins.
- The registry supports text skills built around `SKILL.md` plus supporting files, while code plugins and bundle plugins retain different publish/install semantics.
- The planned package model uses one catalogue and canonical identity layer across skills, code plugins and bundle plugins, while keeping family-specific routes and install UX.
- Every package family must remain explicit, especially the executes-code distinction between code and bundle plugins.
- Supports canonical names, version history, tags, aliases, rename and merge workflows.
- Rename preserves redirect aliases; merge hides duplicate listings and redirects them to the canonical package.
- Mutable aliases/tags such as `latest` remain separate from exact release versions.

### Discovery and inspection

- Supports search, explore and inspect-without-installing.
- Search combines exact/name relevance, embeddings/vector search and a small popularity prior.
- Detail surfaces can expose owner, family, trust, capability, version and runtime-requirement metadata.
- Package browsing supports a unified catalogue while preserving family-specific nouns and filters.
- Inspection can target exact versions, list history/files and fetch bounded text files before installation.

### Publish, compatibility and provenance

- Publish creates versioned releases with changelogs/tags and supports dry-run and machine-readable output.
- Local fingerprints avoid redundant publishing and detect changed local installations.
- Code-plugin manifests require extension declarations and compatibility/build metadata.
- The long-term compatibility model separates stable semantic plugin API compatibility from exact daily OpenClaw application/build versions.
- A stable `pluginApiVersion` or compatible range is the main install/update gate; exact OpenClaw and SDK build versions remain provenance/diagnostic metadata.
- Code-plugin package versions use SemVer for package transport compatibility, while family-specific release-version rules may differ.
- The registry is intentionally not a general-purpose npm clone; npm-compatible access is only a possible restricted transport facade.

### Runtime requirements and capability visibility

- Skill metadata can declare required/optional environment variables, binaries, config files, operating-system restrictions, state directories and install specifications.
- Security analysis compares declared requirements with observed content behavior.
- Plugin capability summaries can include family, executes-code state, plugin ID, providers, channels, tools, hooks, services, commands, routes, config schema and dependency-materialization state.
- High-confidence reporting focuses on declared/registered surfaces rather than claiming arbitrary runtime behavior from static inspection.
- Prompt/model-affecting hooks can be disclosed as capabilities without claiming exact injected content unless explicitly declared.

### Install/update/remove lifecycle

- CLI writes a Workspace-level lockfile and per-install origin metadata.
- Install resolves a version, downloads an archive and records local origin/lock state.
- Pins may include reasons and block direct, batch and forced updates.
- Update fingerprints local files; unknown modifications cause refusal by default and require explicit override, while pins remain protected even from force.
- Uninstall removes the local install and lockfile entry.
- Local uninstall is distinct from registry deletion.
- Registry packages support soft delete/restore; hard delete is controlled and audited/admin-only.
- Version-specific permanent deletion is fail-closed and ownership-scoped.
- Install telemetry is minimal and can be disabled.

### Trust and security

- Supports moderation, verification labels, asynchronous scans and downloadable scan-report bundles.
- Scan bundles may include manifests, multiple static/security-analysis outputs and reports for blocked/hidden versions.
- Open publishing is paired with conservative code-plugin UX, provenance, scans, moderation and family labels rather than assumed safety.
- Security findings can remain visible without erasing package/version evidence.
- Current repository work includes organization-profile verification and audited hard-delete administration.

## What ClawHub completes

- A mature registry and lifecycle reference for skills, code plugins and bundle plugins.
- Inspect-before-install behavior.
- Family and executes-code distinction.
- Version, tag, fingerprint, origin, lockfile and reasoned pin patterns.
- Compatibility contracts separated from fast-moving application-release versions.
- Declared runtime requirements and capability summaries.
- Security scan/report, moderation, organization-verification and provenance UX.
- Rename, merge, soft delete, restore and controlled hard-delete lifecycle.
- Registry CLI and API patterns.
- Registry/package discovery separate from installed runtime truth.

## Important limitations for Ptah

- ClawHub is OpenClaw-specific and cannot define Ptah Facility, Domain Pack, Panel, Recipe or Plugin identity.
- Its skill model is optimized for text bundles and is not a universal executable-plugin format.
- The native code-plugin registry model is still evolving even though package catalogue/publish flows now exist.
- Capability declarations, static scans and registry verification do not prove actual runtime behavior or safety.
- Open publishing substantially increases supply-chain risk.
- A registry trust label, popularity, organization verification or moderation status does not equal Ptah approval.
- Skill instructions may influence external reasoning systems; Ptah must not treat them as trusted policy.
- Install specifications can invoke package managers or dependency materialization and therefore execute supply-chain code.
- Lockfiles and local fingerprints are local install state, not canonical Artifact, Activity or proof truth.
- Convex, GitHub OAuth and OpenAI embeddings are implementation choices rather than required Ptah infrastructure.
- ClawHub's MIT-0 publication rule for skills cannot be assumed suitable for all public/private Ptah registries.
- Tags such as `latest` are mutable aliases and cannot define immutable release identity.
- A plugin API compatibility range does not prove semantic compatibility with saved data, migration code or runtime policy.
- Scan reports can become stale when dependencies are materialized later or runtime configuration changes.
- Local uninstall does not inherently define retained data, orphan cleanup, credential revocation or rollback.

## Must not be inherited

- OpenClaw/ClawHub package, skill or plugin IDs as canonical Ptah identities;
- public registry presence treated as approval or safe installation;
- instructions/prompts inside skills treated as Ptah policy;
- code plugins and content bundles presented under one indistinguishable install action;
- mutable tags used as immutable release identity;
- arbitrary package-manager install scripts run inside Ptah Core;
- registry trust, scan, popularity or moderation labels promoted to proof of runtime safety;
- one registry, Convex deployment or embedding provider made mandatory;
- ClawHub's MIT-0 publication policy forced on private/public Ptah plugins;
- force update overwriting locally modified or pinned production plugins;
- application-release coupling used instead of explicit plugin API compatibility;
- plugin API range treated as approval to migrate or activate;
- hard delete used to erase historical security/provenance evidence required by Ptah policy.

## Integration decision

**ADAPT CLAWHUB AS THE PRIMARY REGISTRY/DISCOVERY/LIFECYCLE DONOR; BUILD PTAH-NATIVE PACKAGE, PLUGIN, TRUST, PERMISSION, INSTALLATION AND RUNTIME CONTRACTS.**

Recommended architecture:

1. one Ptah Package catalogue may index Facility plugins, Domain Packs, UI contributions, Recipes and content/bundle packages;
2. package family and executes-code status are mandatory and prominent;
3. immutable Package Release Artifacts are content-addressed, signed and linked to SBOM/provenance;
4. registry name, alias and tag identity remains separate from exact release identity;
5. inspect, scan, licence review, permission review and compatibility check precede installation;
6. Installed Plugin state records source registry, exact release, digest, permissions, runtime, origin and local modifications;
7. pins with reasons block automatic and forced upgrades;
8. upgrades stage, migrate, validate, health-check and support rollback before activation;
9. private and public registries share contracts but use independent publication/licence policies;
10. MCP servers, Deno tools, OCI/native services, UI contributions and content-only bundles remain distinct runtime/plugin classes;
11. registry trust and scans remain evidence inputs rather than final caller approval;
12. removal uses an explicit data/credential/orphan cleanup plan and retains required historical evidence.

## Licence decision

The ClawHub source MIT licence is compatible with architecture study and selective adaptation. Ptah must not inherit ClawHub's separate MIT-0 publication policy as a universal registry rule; each Ptah registry and Package Release retains its own licence record and acceptance policy.

## Native Ptah gap

Ptah must define:

- Package, Plugin, Package Release, Installed Plugin and Plugin Activation identities;
- plugin families and executes-code classification;
- manifest schema covering Facilities, Domain Packs, Panels, Recipes, Tools, Resources and services;
- stable plugin API/capability version ranges;
- exact source, build, runtime and SDK provenance;
- immutable digest, signature, SBOM and attestation relationships;
- Object, Workspace, permission, resource, network, filesystem and credential declarations;
- install plan and dependency/materialization Activities and Receipts;
- registry trust, reviewer, scan and caller-approval records;
- activation, health, degraded, disabled and quarantine states;
- staged upgrade, migration, rollback and pin semantics;
- local modification and fingerprint handling;
- removal, data retention, credential revocation and orphan-state cleanup;
- private/public registry and licence-policy separation;
- registry replacement, mirroring and offline installation;
- dependency graph re-scan and runtime conformance evidence.

## Exit strategy

Ptah's plugin/package contracts remain independent. ClawHub, OCI registries, Git repositories, local bundles, MCP registries or private catalogues can supply packages without changing Plugin, Package Release or Installed Plugin identity.

## Validation required

1. Publish and inspect content-only and code-executing packages with visibly different families and permission surfaces.
2. Resolve mutable aliases to immutable signed release digests before installation.
3. Refuse a package with incompatible plugin API range or undeclared critical capabilities.
4. Install into a scoped runtime, health-check and retain exact source, digest, dependency and Activity Receipts.
5. Pin an installed version with a reason and reject automatic, batch and forced updates.
6. Detect local modification and require an explicit preserve, fork or replace decision.
7. Stage an upgrade, run migration/conformance tests and roll back after failure.
8. Quarantine a Package Release after a security finding without deleting historical evidence.
9. Remove a Plugin and explicitly retain/delete its data, revoke credentials and clean orphan state through a plan.
10. Replace the registry or install offline without changing Plugin, Package Release or Installed identity.
11. Re-scan materialized dependencies and compare them with source-only scan claims.
12. Keep registry organization verification and popularity as advisory metadata rather than approval.
