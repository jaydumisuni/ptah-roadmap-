# Donor Record — ClawHub

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — PRIMARY PLUGIN/SKILL REGISTRY, VERSIONING, VERIFICATION AND LIFECYCLE DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/openclaw/clawhub
- Owner/organisation: `openclaw`
- Default branch: `main`
- Pinned commit: `aaa73625ed4100b1006653f49089f2a2d969a427`
- Licence: MIT for ClawHub source; published skill content uses ClawHub's separate MIT-0 publication policy
- Activity: Active
- Classification: public Registry, package catalogue, skill/plugin metadata, publication, artifact verification, moderation, install/update/pin and security-review donor
- Ptah targets: `PLUGIN-001`, discovery, inspection, versioning, compatibility, trust/capability labels, source/provenance, install state, pinning, update, removal, quarantine and Registry UX

## Files/components inspected

- `README.md`
- `LICENSE`
- `docs/skill-format.md`
- `docs/cli.md`
- `specs/plans/plugins.md`
- `packages/schema/src/packages.ts`
- `packages/schema/src/openclawContract.ts`
- `packages/clawhub/src/cli/commands/packages.ts`
- `convex/lib/packageRegistry.ts`
- `scripts/security/run-prepublication-worker.ts`
- skill/package/API/schema, publication, trusted-publisher and security-analysis references
- current repository/commit activity

## Verified capabilities and patterns

### Registry and package identity

- ClawHub is the public skill Registry for OpenClaw and exposes a native package catalogue for code and bundle plugins.
- Package families distinguish `skill`, `code-plugin` and `bundle-plugin`.
- Registry channels include official, community and private.
- Text skills center on `SKILL.md` plus allowed supporting files, while code and bundle plugins retain distinct artifact and execution semantics.
- One catalogue can present all families while preserving family-specific routes, filters, compatibility and install UX.
- Family and executes-code state remain explicit.
- Supports canonical names, version history, tags, aliases, rename and merge workflows.
- Rename preserves redirect aliases; merge hides duplicate listings and redirects them to the canonical package.
- Mutable aliases/tags such as `latest` remain separate from exact release versions.
- Publisher ownership, organization scope and transfer are explicit.

### Discovery and inspection

- Supports search, explore and inspect without installing.
- Search combines exact/name relevance, embeddings/vector search and a small popularity prior.
- Package browsing can filter family, official status, executes-code state, target, OS, architecture, libc, browser/desktop/native dependencies, external services, binaries, OS permissions and artifact kind.
- Detail surfaces can expose owner, family, trust, capability, version, source and runtime-requirement metadata.
- Inspection can target exact versions/tags, list version history/files and fetch bounded text files before installation.
- Popularity, search rank, downloads and official badges remain discovery signals, not approval.

### Publish, source and compatibility

- Publish creates versioned releases with changelogs/tags and supports dry-run and machine-readable output.
- Publish sources can be a local folder, exact npm-pack tarball, GitHub repository/ref or GitHub URL.
- Source attribution can retain repository, resolved commit, ref and subpath.
- Local GitHub-origin checkouts can contribute source attribution.
- Code-plugin folders are packed into exact npm-pack artifacts before upload.
- External code plugins must declare `openclaw.compat.pluginApi` and `openclaw.build.openclawVersion` explicitly.
- Optional compatibility includes minimum Gateway version and plugin SDK version.
- Code-plugin versions require SemVer.
- The compatibility model separates stable plugin API range from exact application/SDK build versions used for provenance and diagnostics.
- Readiness reports can identify blockers for official status, artifact availability/digest, source provenance, compatibility, host targets, environment metadata and scan state.

### Exact artifact identity and verification

- Package releases can retain ClawHub SHA-256, npm SHA-512 integrity, npm shasum, tarball name/version, byte size and file count.
- Download verifies ClawHub SHA-256 for all artifacts.
- ClawPack npm artifacts additionally verify npm integrity, npm shasum and tarball `package.json` name/version.
- Local verification can compare one file against Registry metadata or direct digest arguments.
- Bundled skills retain path, SHA-256 and size metadata inside package summaries.
- Upload and fetched-text size limits are explicit.
- Artifact identity is stronger than a tag or package name but remains Registry evidence until mapped to immutable Ptah Package Release identity.

### Verification tiers and trusted publishing

- Verification tiers include structural, source-linked, provenance-verified and rebuild-verified.
- Verification scope can distinguish artifact-only from dependency-graph-aware evidence.
- Verification summaries can retain source repository, commit, tag/path, provenance presence, trusted-plugin state and scan status.
- Trusted-publisher records bind a GitHub repository, workflow filename and optional environment.
- GitHub Actions OIDC can replace long-lived Registry tokens for supported flows.
- Reusable publication workflows should be pinned to stable tags or full commit SHAs rather than `main`.
- Pull requests can run publication dry-runs, while real publication is limited to trusted manual/tag events.

### Runtime requirements and capability visibility

- Skill metadata can declare required/optional environment variables, binaries, config files, operating systems and install specifications.
- Install specification kinds include Brew, Node, Go and uv.
- Security analysis compares declared requirements with observed content behavior.
- Plugin summaries can expose identity, compatibility, required/sensitive config fields, MCP server names and bundled skills.
- Plugin capability summaries can include family, executes-code state, plugin ID, providers, channels, Tools, hooks, services, commands, routes, config schema and dependency-materialization state.
- High-confidence reporting focuses on declared/registered surfaces rather than claiming arbitrary runtime behavior from static inspection.
- Prompt/model-affecting hooks can be disclosed without claiming exact injected content unless explicitly declared.

### Install/update/remove lifecycle

- Skill CLI writes Workspace-level lock and per-install origin metadata.
- Install resolves a version, downloads an archive and records local origin/lock state.
- Pins may include reasons and block direct, batch and forced updates.
- Update fingerprints local files; unknown modifications cause refusal by default and require explicit override, while pins remain protected even from force.
- Uninstall removes the local install and lock entry.
- Local uninstall is distinct from Registry deletion.
- Package download/verify is separate from host activation.
- Registry packages support soft delete/restore; hard delete is controlled and audited/admin-only.
- Version-specific permanent deletion is fail-closed and ownership-scoped, cannot be restored or republished, and requires replacement of the latest release first.
- Rename, merge, ownership transfer and publisher transfer retain explicit workflows.
- Install telemetry is best-effort and can be disabled.

### Moderation and prepublication security

- Supports reports, moderation status, verification labels, asynchronous scans and downloadable scan-report bundles.
- Scan bundles may include manifests, static/security analysis, VirusTotal-style results, SkillSpector findings and LLM-assisted analysis.
- Release moderation states include approved, quarantined and revoked.
- Reports can be open, confirmed or dismissed; appeals can be accepted or rejected.
- Reports alone do not automatically hide packages; moderation remains explicit.
- Security findings can remain visible without erasing package/version evidence.
- A prepublication worker retains publish-attempt ID, claim ID, package/version, artifact fingerprint and per-file hash/size.
- Secret scanning uses a digest-pinned TruffleHog container image.
- Verified secret findings block publication; public summaries are bounded and redacted.
- Scan and moderation evidence is tied to exact versions, including blocked/hidden releases.
- Current work includes organization-profile verification and audited hard-delete administration.

## What ClawHub completes

- A mature Registry and lifecycle reference for skills, code plugins and bundle plugins.
- Inspect-before-install behavior and family-aware discovery.
- Version, tag, fingerprint, origin, lockfile and reasoned pin patterns.
- Exact package artifact digest/integrity verification.
- Compatibility contracts separated from fast-moving application-release versions.
- Declared runtime requirements, sensitive config and capability summaries.
- Source attribution, trusted publishing and verification tiers.
- Prepublication secret scanning and asynchronous security evidence.
- Moderation, report, quarantine, revocation and appeal states.
- Rename, merge, transfer, soft delete, restore and controlled hard-delete lifecycle.
- Registry CLI and API patterns.
- Registry/package discovery separate from installed/runtime truth.

## Important limitations for Ptah

- ClawHub is OpenClaw-specific and cannot define Ptah Facility, Domain Pack, Panel, Recipe or Plugin identity.
- Its skill model is optimized for text bundles and is not a universal executable-plugin format.
- The code-plugin Registry model is still evolving.
- Capability declarations, static scans, LLM analyses and Registry verification do not prove runtime behavior or safety.
- Open publishing substantially increases supply-chain risk.
- A trust label, popularity score, organization verification, official badge or moderation state does not equal Ptah approval.
- Skill instructions may influence external reasoning systems and can contain dangerous actions, credential requests or social engineering even when text-only.
- Runtime declarations are publisher-authored and may be incomplete or misleading.
- Install specifications can invoke package managers and execute supply-chain code.
- Lockfiles and local fingerprints are local install state, not canonical Artifact, Activity or proof truth.
- Convex, GitHub OAuth and OpenAI embeddings are implementation choices rather than required Ptah infrastructure.
- ClawHub's MIT-0 publication rule for skills cannot be assumed suitable for all public/private/internal Ptah Registries.
- Tags such as `latest` are mutable aliases and cannot define immutable release identity.
- A plugin API compatibility range does not prove semantic compatibility with saved data, migration code or runtime policy.
- Scan reports can become stale when dependencies are materialized later or runtime configuration changes.
- A clean scan can miss delayed payloads, dependency substitution, runtime-only behavior and malicious remote services.
- LLM-assisted scan analysis is advisory evidence, not deterministic proof.
- Registry deletion cannot erase already downloaded bytes or historical evidence.
- ClawHub download/verification does not define staged activation, health checks, state migration or rollback in the consuming host.
- Local uninstall does not inherently define retained data, orphan cleanup, credential revocation or rollback.
- Registry telemetry still requires explicit Ptah privacy policy even when optional.

## Must not be inherited

- OpenClaw/ClawHub package, skill, plugin, slug, tag or publisher IDs as canonical Ptah identities;
- public Registry presence treated as approval or safe installation;
- instructions/prompts inside skills treated as Ptah policy or executable authority;
- code plugins and content bundles presented under one indistinguishable install action;
- mutable tags used as immutable release identity;
- arbitrary package-manager install scripts run inside Ptah Core or with ambient host privilege;
- Registry trust, scan, popularity, official or moderation labels promoted to proof of runtime safety;
- one Registry, Convex deployment or embedding provider made mandatory;
- ClawHub's MIT-0 publication policy forced on private/public Ptah Plugins;
- force update overwriting locally modified or pinned production Plugins;
- application-release coupling used instead of explicit plugin API compatibility;
- plugin API range treated as approval to migrate or activate;
- a clean scan used to bypass signature, provenance, licence, permission or sandbox policy;
- trusted-publisher OIDC treated as proof that package content is safe;
- hard delete used to erase historical security/provenance evidence required by Ptah policy;
- Registry soft deletion used as a substitute for revocation/tombstone propagation;
- install telemetry emitted without Workspace/user policy.

## Integration decision

**ADAPT CLAWHUB AS THE PRIMARY REGISTRY/DISCOVERY/PUBLICATION/VERIFICATION/LIFECYCLE DONOR; BUILD PTAH-NATIVE PACKAGE, PLUGIN, TRUST, PERMISSION, INSTALLATION, ACTIVATION AND ROLLBACK CONTRACTS.**

Recommended architecture:

1. One Ptah Package catalogue may index Facility Plugins, Domain Packs, UI Contributions, Recipes and content/bundle packages.
2. Package family and executes-code status are mandatory and prominent.
3. Registry name, alias and tag identity remains separate from immutable digest-based Package Release identity.
4. Immutable Package Release Artifacts are content-addressed, signed and linked to SBOM/provenance/licence records.
5. Structural, source-linked, provenance-verified and independently rebuilt evidence remain distinct proof levels.
6. Registry scans, reports and moderation become Claims/Evidence attached to exact Package Releases.
7. Inspect, scan, licence review, permission review and compatibility checks precede staging.
8. Install/stage is a receipted Activity that does not activate code.
9. Plugin Activation is a separate receipted Activity with permissions, configuration, migration and health checks.
10. Failed migration/health restores the previous Activation Revision.
11. Installed Plugin state records source Registry, exact release/digest, permissions, runtime, origin and local modifications.
12. Pins with reasons bind exact Package Revision/digest and block automatic or forced upgrades.
13. Updates stage proposed revisions, show compatibility/migration differences and require approval before activation.
14. Private, internal and public Registries share contracts but use independent publication/licence policies.
15. MCP servers, Deno Tools, OCI/native services, UI Contributions and content-only bundles remain distinct runtime/plugin classes.
16. Removal distinguishes disable, deactivate, uninstall, retained state, purge, revoke and tombstone.
17. Registry trust and scans remain evidence inputs rather than final caller approval.
18. ClawHub remains replaceable behind Ptah Registry adapters.

## Licence decision

The ClawHub source MIT licence is compatible with architecture study and selective adaptation. Ptah must not inherit ClawHub's separate MIT-0 publication policy as a universal Registry rule. Each Ptah Package Release, Registry channel, dependency, bundled binary and install mechanism retains its own licence record and acceptance policy.

## Native Ptah gap

Ptah must define:

- Package, Plugin, Package Release, Installed Plugin and Plugin Activation identities;
- immutable digest pins plus human names, aliases and tags;
- Plugin families and executes-code classification;
- Registry, Publisher and Publication records;
- manifest schema covering Facilities, Domain Packs, Panels, Recipes, Tools, Resources and services;
- stable plugin API/capability version ranges;
- exact source, build, runtime and SDK provenance;
- immutable digest, signature, SBOM, attestation and rebuild relationships;
- Object, Workspace, permission, resource, network, filesystem, Device and credential declarations;
- install/stage, dependency/materialization, configure, migrate, activate, health, rollback and removal Activities/Receipts;
- Activation Revision and previous-known-good state;
- Registry trust, reviewer, scan, report, moderation and caller-approval records;
- local modification and fingerprint handling;
- revocation/tombstone propagation to online and intermittently connected Nodes;
- removal, data retention, credential revocation and orphan-state cleanup;
- private/public/internal Registry and licence-policy separation;
- Registry replacement, mirroring and offline installation;
- dependency graph re-scan and runtime conformance evidence;
- telemetry/privacy policy.

## Exit strategy

Ptah's Plugin/package contracts remain independent. ClawHub, OCI/ORAS Registries, Git repositories, npm, local bundles, MCP Registries or private catalogues can supply packages without changing Plugin, Package Release, Installed Plugin or Activation identity.

## Validation required

1. Publish and inspect content-only and code-executing packages with visibly different families and permission surfaces.
2. Resolve mutable aliases to immutable signed release digests before installation.
3. Publish identical source through public and private Registries while preserving one Package Release identity and separate Publication records.
4. Verify package SHA-256/npm integrity and reject mismatched tarball identity.
5. Refuse a package with incompatible plugin API range or undeclared critical capabilities.
6. Install/stage without activating and prove it has no runtime authority.
7. Activate in a scoped runtime, health-check and retain exact source, digest, dependency and Activity Receipts.
8. Pin an installed revision with a reason and reject automatic, batch and forced updates.
9. Detect local modification and require an explicit preserve, fork or replace decision.
10. Stage an upgrade, run migration/conformance tests and roll back after failure.
11. Quarantine/revoke a Package Release after a security finding without deleting historical evidence.
12. Reject a clean-scanned package whose signature, provenance, licence or requested permissions are unacceptable.
13. Treat a text skill containing destructive instructions as untrusted content rather than authority.
14. Execute declared package-install steps only inside the approved Deno/OCI/VM isolation class.
15. Remove a Plugin and explicitly retain/delete its data, revoke credentials and clean orphan state through a plan.
16. Disable telemetry and prove installation still succeeds without hidden Registry calls.
17. Replace the Registry or install offline without changing Plugin, Package Release, Installed Plugin or Activation identity.
18. Re-scan materialized dependencies and compare them with source-only scan claims.
19. Keep organization verification, trusted publishing and popularity as advisory metadata rather than approval.
