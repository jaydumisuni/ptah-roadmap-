# Donor Record — ClawHub and OpenClaw Plugin Lifecycle

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — PRIMARY PUBLIC REGISTRY, PACKAGE VERIFICATION AND HOST-LIFECYCLE DONOR  
**Inspected:** 2026-07-18

## Identity

### ClawHub registry

- Canonical repository: `https://github.com/openclaw/clawhub`
- Default branch: `main`
- Pinned commit: `aaa73625ed4100b1006653f49089f2a2d969a427`
- Licence: MIT for registry code
- Activity: Active
- Classification: public skill/package registry, publication, moderation, verification and distribution donor

### OpenClaw plugin host lifecycle

- Canonical repository: `https://github.com/openclaw/openclaw`
- Default branch: `main`
- Pinned completion-pass commit: `e976e357ea5f26a27af1b4a0430fccb2f8e95032`
- Licence: MIT
- Activity: Active
- Classification: plugin discovery, install, activation, update, inspection and uninstall host donor

### Published skill licence rule

- ClawHub registry code is MIT.
- Skills published through ClawHub are released under MIT-0 and do not support per-skill licence overrides.
- Code-plugin and bundle-plugin packages require package/dependency-level licence review; registry publication is not a substitute for that review.

## Ptah relevance

Ptah targets:

- `PLUGIN-001` discovery, package, verification, installation and lifecycle completion;
- public, private and official registry channels;
- package/version/artifact identity;
- compatibility and host-target declarations;
- publication provenance and trusted publishing;
- scanning, moderation, quarantine, revocation and appeal;
- pinning, drift detection and update control;
- activation, runtime inspection and removal;
- skill/recipe and code-plugin separation;
- MCP-server and bundled-skill declarations.

## Files/components inspected

### ClawHub

- `README.md`
- `LICENSE`
- `docs/skill-format.md`
- `docs/cli.md`
- `packages/schema/src/packages.ts`
- `packages/schema/src/openclawContract.ts`
- `packages/clawhub/src/cli/commands/packages.ts`
- `convex/lib/packageRegistry.ts`
- `scripts/security/run-prepublication-worker.ts`

### OpenClaw plugin host

- `docs/plugins/manage-plugins.md`
- `src/plugins/install-provenance.ts`
- current plugin install/search/update/uninstall source locations

## Verified registry capabilities and patterns

### Package families and channels

- ClawHub distinguishes `skill`, `code-plugin` and `bundle-plugin` package families.
- Registry channels include official, community and private.
- Skills are text-oriented bundles centered on `SKILL.md` plus allowed supporting text files.
- Code plugins publish executable package artifacts.
- Bundle plugins can group plugin/skill material for multiple hosts.
- Package search can filter by family, official status, execution behavior, host target, OS, architecture, libc, browser/desktop/native dependencies, external services, binaries, OS permissions and artifact kind.

### Version and compatibility records

- Skills and packages publish explicit versions; skills use semver-like version/tag flows and code plugins require valid semver.
- Tags such as `latest` point to versions rather than replacing version identity.
- External code plugins must declare `openclaw.compat.pluginApi` and `openclaw.build.openclawVersion`.
- Optional compatibility fields include minimum Gateway version and plugin SDK version.
- Source repository, resolved commit, ref and subpath can be captured during publication.
- Package readiness exposes blockers for official status, artifact availability/digest, provenance, compatibility, host targets, environment metadata and scan state.

### Artifact identity and verification

- ClawPack code-plugin publication uses exact npm-pack tarball bytes.
- Artifact metadata can retain ClawHub SHA-256, npm SHA-512 integrity, npm shasum, tarball name, unpacked size and file count.
- Download verifies ClawHub SHA-256 for all artifacts.
- ClawPack downloads also verify npm integrity, npm shasum and `package.json` name/version.
- Local verification can compare a file against registry metadata or direct digest values.
- Package artifacts and bundled skills retain per-file SHA-256 and size metadata.
- Upload size limits are explicit.

### Verification tiers and source evidence

- Verification tiers include structural, source-linked, provenance-verified and rebuild-verified.
- Verification scope can be artifact-only or dependency-graph-aware.
- Verification summaries can retain source repository, commit, tag, path, provenance presence, trusted-plugin status and scan state.
- Trusted publisher records can bind GitHub repository, repository owner, workflow filename and optional environment.
- GitHub Actions OIDC can replace a long-lived registry token for supported trusted publishing flows.
- Reusable publish workflows are expected to be pinned to stable tags or full commit SHAs rather than `main`.

### Manifest and declared requirements

- Plugin manifest summaries retain schema version, identity, compatibility, config fields, MCP server names and bundled skills.
- Config fields can be marked required and sensitive.
- Skills can declare required environment variables, binaries, alternative binaries, config paths, OS restrictions and dependency-install specifications.
- Install kinds include Brew, Node, Go and uv.
- Skill security analysis compares declared runtime requirements with observed content/behavior and reports mismatches.
- External TypeScript plugin packages must include compiled runtime output or explicitly declared runtime entries.

### Security inspection and moderation

- Package scan summaries can include static findings, SkillSpector findings, VirusTotal results, LLM-assisted analysis and general scan state.
- Release moderation states include approved, quarantined and revoked.
- Reports can be open, confirmed or dismissed and can lead to quarantine or revocation.
- Appeals can be accepted or rejected.
- A prepublication worker tracks publish-attempt ID, claim ID, package/version, artifact fingerprint and per-file hash/size.
- Secret scanning uses a digest-pinned TruffleHog container image.
- Verified secret findings block publication; public findings are bounded and redacted.
- Scan/download reports are tied to exact submitted versions, including blocked or hidden versions.
- A report alone does not automatically hide or block a package; moderation remains an explicit action.

### Rename, merge, transfer and deletion

- Owned skills can be renamed while preserving the old slug as a redirect alias.
- Duplicate owned skills can be merged into one canonical listing with redirect aliases.
- Ownership transfers have explicit request/accept/reject/cancel flows or controlled organization transfer.
- Whole skills/packages support soft delete and restore.
- Selected non-latest versions can be permanently deleted through fail-closed owner routes.
- Moderation reasons are recorded in audit logs.
- Hard deletion is restricted to administrative management/ban flows.

## Verified local skill lifecycle

- Skill install resolves a version, downloads an archive and writes origin plus workdir lock metadata.
- Installed skills can be pinned with an optional reason.
- Pinned skills reject direct update, bulk update and force reinstall until explicitly unpinned.
- Update fingerprints local files and refuses unknown local modifications by default.
- Force overwrite is available only for unpinned skills.
- Uninstall removes local files and the lock entry.
- Registry install telemetry is best-effort, applies only while logged in and can be disabled.
- Inspect and download operations can target exact versions/tags without installing.

## Verified OpenClaw code-plugin host lifecycle

### Discovery and authority

- The host distinguishes bundled, official external, ClawHub, npm, git, local path/archive, npm-pack and marketplace sources.
- Explicit prefixes select the desired source deterministically.
- ClawHub and selected bundled/official sources are treated as trusted by OpenClaw policy.
- Arbitrary npm, git, local, npm-pack or marketplace sources require explicit trust confirmation or `--force` in noninteractive use.
- Registry search and ordinary inventory are cold metadata checks; they do not prove a running Gateway loaded the module.

### Installation and activation

- Installation is separate from enablement.
- Restrictive allow lists can record explicit administrator trust when enabling an installed plugin.
- Deny-list entries remain authoritative.
- Installing/removing plugin code requires a Gateway restart; some enablement changes can reload live when supported.
- Runtime inspection imports the module and confirms registered tools, hooks, services, Gateway methods, routes and CLI commands.
- Plain list/inspect does not prove runtime registration.

### Update and removal

- Update reuses tracked install specifications, including exact versions and dist-tags.
- Bulk update can advance trusted official records to current catalog targets, while targeted updates preserve exact/tagged specs.
- Dry-run is supported.
- Uninstall removes config, persisted plugin-index state, allow/deny entries and linked load paths; files can optionally be retained.
- Managed Gateway restart follows source-changing install/update/uninstall operations.
- Nix mode disables mutable lifecycle commands and defers package choice to declarative source configuration.

### Install provenance limitations

- OpenClaw's trust helper treats all `clawhub:` specs as trusted by host policy.
- Non-ClawHub sources display a warning explaining they are outside ClawHub review/trust metadata.
- Trusted source classification is useful host policy, but it is not equivalent to source provenance, independent rebuild or Ptah approval.

## What this donor composition completes

- Public package discovery with skill/code/bundle separation.
- Version, tag, source and compatibility metadata.
- Artifact digests and npm integrity verification.
- Verification tiers including provenance/rebuild language.
- Moderation, quarantine, revocation, reporting and appeal records.
- Trusted-publisher/OIDC patterns.
- Declaration of environment, binary, config, OS, host and capability requirements.
- Local lock/pin/drift behavior for installed skills.
- Host install-source selection, activation, runtime inspection, update and uninstall workflows.
- Clear distinction between cold inventory and live runtime registration.
- Registry aliases, transfer and soft-delete patterns.

## Important limitations for Ptah

- ClawHub is an OpenClaw-specific public registry, not Ptah's canonical Plugin, Facility or Recipe catalogue.
- Registry slugs, tags, publisher handles and IDs are mutable/local names rather than stable Ptah identities.
- Search popularity, stars, downloads, official labels and scan summaries are discovery signals, not trust proof.
- ClawHub's OpenAI/Convex implementation stack must not become mandatory Ptah infrastructure.
- Registry scans can miss malicious behavior, runtime side effects, dependency substitution and delayed payloads.
- LLM-assisted analysis is advisory evidence, not deterministic security proof.
- Text-only skills can still contain dangerous instructions, shell commands, credential requests or social-engineering content.
- Skill runtime declarations are self-authored and can be incomplete or misleading.
- Install specifications such as Brew/npm/Go/uv can execute supply-chain code and mutate the host.
- All ClawHub skills use MIT-0; Ptah needs private, internal, commercial and differently licensed package support.
- ClawHub package channels do not replace Ptah Workspace/department/tenant visibility and approval policy.
- Package deletion in a registry cannot erase already downloaded artifacts or historical evidence.
- OpenClaw's blanket trust for `clawhub:` sources is too broad for Ptah.
- Host enable/restart/runtime registration does not prove semantic correctness, health, acceptance or safe rollback.
- Tracked install specs and tags can drift unless resolved artifact digests are retained.
- Bulk update behavior can intentionally move official plugins, which is unsuitable for frozen or regulated Workspaces without explicit approval.
- The inspected host lifecycle does not establish transactional activation, state migration, automatic health rollback or dependency-aware rollback.
- Uninstall with retained files can leave executable bytes or state behind.
- Plugin config fields and environment variables do not express exact Object, credential, network or device permissions.
- Registry telemetry requires explicit Ptah privacy policy even when best-effort or optional.

## Must not be inherited

- ClawHub/OpenClaw package IDs, slugs, tags or publisher handles as canonical Ptah identities;
- all ClawHub packages trusted merely because they came from ClawHub;
- official/community labels treated as approval or proof;
- scan `clean` treated as safe execution authorization;
- skills automatically licensed MIT-0 in a general Ptah registry;
- skill text or package metadata activated without independent policy review;
- Brew/npm/Go/uv install instructions executed with ambient host privilege;
- version tags installed without resolving and pinning artifact digest;
- `--force` used as an ordinary unattended approval mechanism;
- update-all allowed to move frozen package versions silently;
- runtime import/registration treated as full health or acceptance proof;
- registry soft deletion used as a substitute for revocation/tombstone propagation;
- retained uninstall files left discoverable/executable without explicit state;
- telemetry emitted without Workspace/user policy;
- Convex, OpenAI embeddings or OpenClaw Gateway made mandatory Ptah foundations.

## Integration decision

**ADAPT CLAWHUB AS THE PRIMARY PUBLIC REGISTRY/PACKAGE-LIFECYCLE DONOR AND OPENCLAW AS A HOST-LIFECYCLE DONOR; BUILD PTAH-NATIVE PLUGIN IDENTITIES, TRUST, PERMISSIONS, ACTIVATION AND ROLLBACK.**

Recommended composition:

1. Ptah distinguishes Recipe/Skill, code Plugin, bundle Plugin, Domain Pack and UI Contribution packages.
2. Every package has immutable Package Revision and Artifact digest identity independent of slug/tag.
3. Public, private, internal and official registries are discovery locations, not trust authorities.
4. Registry publication retains source commit/path, package artifact, SBOM, signature, provenance and licence.
5. Verification tiers distinguish structural, source-linked, provenance-verified and independently rebuilt evidence.
6. Registry scans become Evidence/Claims attached to a Package Revision.
7. Install is a receipted Activity that stages bytes without activating them.
8. Activation is a separate receipted Activity with permissions, configuration, migration, health checks and control-plane reload/restart.
9. Failed health or migration triggers rollback to the previous Activation Revision.
10. Pinning records exact Package Revision and artifact digest, not only a version/tag.
11. Updates resolve proposed revisions, show compatibility and migration differences, and require policy approval before activation.
12. Removal distinguishes disable, deactivate, uninstall, retain-state, purge-state, revoke and tombstone.
13. MCP servers declared by packages remain MCP adapter contributions behind Ptah policy.
14. Skills/Recipes remain caller instructions, not executable authority or reasoning ownership.
15. ClawHub and OpenClaw can connect through adapters without becoming required infrastructure.

## Licence decision

- ClawHub and OpenClaw source are MIT-compatible for study and selective adaptation.
- ClawHub-published skills are MIT-0 by registry policy; Ptah must not impose this on all package classes.
- Each code/bundle plugin, dependency, bundled binary and install mechanism requires independent licence recording.
- Public registry metadata must expose licence state and block publication/activation when the package licence is absent or incompatible with its channel.

## Native Ptah gap

Ptah must define:

- Plugin/Recipe Package, Package Revision, Artifact and Source identities;
- immutable digest-based pins plus human names/tags/aliases;
- Registry, Publisher and Publication records;
- package family and contribution manifests;
- source, SBOM, signature, provenance, rebuild and licence evidence;
- object, workspace, credential, network, device, subprocess and resource permissions;
- install/stage, configure, migrate, activate, health, deactivate, rollback, uninstall and purge Activities;
- Activation Revision and previous-known-good state;
- dependency graph, compatibility, conflict and migration contracts;
- public/private/internal/department registry visibility;
- report, quarantine, revoke, appeal and tombstone propagation;
- exact update proposal and policy approval;
- offline registry mirror and cached-revocation behavior;
- telemetry/privacy policy;
- package replacement and registry-exit tests.

## Exit strategy

Ptah packages remain distributable through Ptah registries, OCI/ORAS, npm, Git, local bundles, ClawHub, MCP registry entries or other stores. Removing ClawHub or OpenClaw does not change Package, Plugin, Recipe, Facility or Activation identity.

## Validation required

1. Publish identical source through public and private registries while preserving one Package Revision identity and separate Publication records.
2. Resolve a tag to an immutable artifact digest and prove later tag movement does not alter a pinned installation.
3. Install a package without activating it and verify it has no runtime authority.
4. Activate with exact Object, network, credential and resource scopes and deny undeclared access.
5. Detect a local byte modification and refuse update/activation until explicitly reviewed.
6. Upgrade with configuration/state migration, fail the health check and automatically restore the previous Activation Revision.
7. Quarantine/revoke a published revision and propagate the state to online and intermittently connected Nodes without deleting historical evidence.
8. Run structural, source-linked, provenance and independent-rebuild verification as distinct proof levels.
9. Reject a package whose scan is clean but whose signature, provenance, licence or permissions are unacceptable.
10. Treat a text skill containing destructive instructions as untrusted content rather than executable authority.
11. Execute declared package-install steps only inside the approved Deno/OCI/VM isolation class.
12. Remove a plugin and prove code, configuration, credentials, state, dependencies and retained files have explicit final states.
13. Disable telemetry and prove installation still succeeds without hidden registry calls.
14. Switch from ClawHub to an ORAS/private registry without changing Package or Activation identity.
15. Import an OpenClaw plugin and expose it through a Ptah adapter without importing OpenClaw assistant identity or reasoning policy.
16. Compare cold manifest inventory with live runtime registration and retain both states honestly.
