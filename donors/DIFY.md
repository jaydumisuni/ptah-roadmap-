# Donor Record — Dify

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — WORKFLOW/APPLICATION/PLUGIN CONFIGURATION DONOR WITH MATERIAL LICENCE RESTRICTIONS  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/langgenius/dify
- Default branch: `main`
- Pinned commit: `2ec34b2cfbcf0ca1faabfff918b7e74d93aeffcf`
- Licence: modified Apache-2.0 with additional multi-tenant and frontend-branding restrictions
- Activity: Active
- Classification: AI application/workflow, model-provider, tool/plugin, data-source and knowledge-application platform donor
- Ptah targets: Recipe/workflow configuration, provider abstraction, typed node graphs, event streaming, plugin manifests, installation sources, permission/resource declarations, upgrade tasks and provider/plugin UX

## Files/components inspected

- `README.md`
- `LICENSE`
- `api/core/workflow/workflow_entry.py`
- `api/core/plugin/plugin_service.py`
- `api/core/plugin/entities/plugin.py`
- graph-engine, node-factory, command-channel, variable-pool, streaming-event and OTel boundaries
- plugin daemon, marketplace, package/GitHub installation and provider-cache boundaries
- latest commit/activity evidence

## Verified capabilities and patterns

### Workflow and graph execution

- Provides visual workflow orchestration with typed/versioned nodes and graph execution.
- Separates workflow graph definition, execution entry, node factory, variable pool, runtime state, command channel and streamed events.
- Child graphs use a fresh runtime state while retaining selected execution context and variable access.
- Graph construction validates child-root presence rather than silently fabricating a child graph.
- External command channels can control a run; in-memory channels are the default.
- Response-stream filtering preserves ordered public event behavior across engine changes.
- Execution limits bound maximum steps and runtime.
- Worker scaling parameters are explicit.
- LLM quota, debug and OpenTelemetry/observability behavior are applied as graph layers.
- Single-node debug execution resolves node type and version, preloads variables and returns node-level event streams.
- Exceptions become explicit failed events or node-run failures instead of being flattened into successful graph completion.

### Plugin manifest and installation model

- Plugin installation sources include GitHub, marketplace, local package and remote/debug sources.
- Manifests retain semantic version, author, name, description, category, creation time, repository, verification state, tags and minimum Dify version.
- Plugin categories include tool, model, extension, agent strategy, data source and trigger.
- Resource declarations include memory and scoped permissions for tools, model capabilities, nodes, endpoints and bounded storage.
- Installation records retain tenant, runtime type, source, plugin ID, unique package identifier, version, checksum and declaration.
- Dependency records distinguish GitHub, marketplace and package sources.
- Package/version strings are validated.

### Plugin lifecycle and trust controls

- Tenant-scoped plugin lists, provider discovery and endpoint counters are separated.
- Plugin provider metadata uses generation-based cache invalidation and tenant-specific Redis keys.
- Refresh locks reduce duplicate provider-cache rebuild work, with direct-daemon fallback when Redis or locking fails.
- Stale daemon endpoint counts are reconciled against live endpoint records before returning workspace metadata.
- Installation policy can restrict plugins to marketplace-only, official-only, official-plus-partners, none or all.
- Marketplace/package/GitHub upload paths can request signature verification and check returned verification category.
- Download size limits apply to GitHub release packages.
- Install operations produce queryable installation tasks with explicit success/failed terminal states.
- Marketplace and GitHub upgrade paths retain original and replacement unique identifiers and invalidate provider caches after change.
- Bundles can declare multiple plugin dependencies.
- Marketplace metadata exposes latest version, status, deprecation reason and replacement plugin.

## Licence boundary

Dify's licence is not ordinary Apache-2.0.

At the inspected pin:

- commercial use is generally allowed;
- operating Dify source as a multi-tenant environment requires a commercial licence unless explicitly authorized in writing;
- using Dify's frontend from source or its web image prevents removal or modification of Dify logo/copyright information;
- the interactive design is separately claimed as protected;
- the producer reserves the ability to adjust the agreement.

This materially limits direct source reuse for a public multi-tenant Ptah shell or a rebranded hosted service. Any deployment or code reuse beyond architecture study requires a formal licence review.

## What Dify completes

- A mature reference for visual Recipe/workflow/application composition.
- Typed/versioned node graphs, child graphs, variable pools and event streams.
- Model-provider, tool, data-source and plugin configuration UX.
- Explicit graph execution limits, command channels and observability layers.
- Tenant-scoped plugin/provider metadata and cache-invalidation patterns.
- Plugin manifests with versions, checksums, categories, resource declarations and permission families.
- Package, marketplace, GitHub and remote installation-source patterns.
- Install/upgrade tasks, verification categories, latest-version/deprecation metadata and bundle dependencies.
- Knowledge/application integration and application API/deployment concepts.
- A useful optional workload for users who want a Dify-compatible AI-app builder.

## Important limitations for Ptah

- Dify is an AI application platform, not Ptah's Activity Ledger, Object graph, Workspace Provider or plugin truth.
- Its graph engine cannot replace Temporal/Ptah durable Activity semantics, attempts, receipts, checkpoints or proof.
- Model, agent, prompt and reasoning features belong to caller products, not Ptah Core.
- Product workspace/tenant IDs are not Ptah Workspace identity.
- The modified licence conflicts with direct source reuse in a branded multi-tenant Ptah service unless commercially licensed.
- Dify frontend cannot be treated as a freely rebrandable Ptah shell.
- Workflow node success does not prove produced Objects, external side effects or acceptance.
- Plugin verification categories are Dify/marketplace policy, not a complete Ptah trust/provenance model.
- Signature verification is conditional on configured policy and does not replace SBOM, provenance, sandboxing or runtime permissions.
- Plugin permissions are broad capability families rather than Ptah Object/Workspace/credential/network scopes.
- Full deployment and separate plugin daemon are operationally heavy for the first Ptah slice.
- Knowledge-base IDs and indexes are derived product state, not canonical Knowledge identity.
- Cache fallback and stale-count reconciliation show that daemon/cache state can diverge from live state.
- Upgrade calls do not by themselves prove safe migration, rollback or compatibility with saved workflow/knowledge state.
- Marketplace availability and producer policy are external dependencies.

## Must not be inherited

- Dify as Ptah Core or the fundamental Activity runtime;
- Dify agent, reasoning, prompt or model policy inside Ptah;
- direct use of the Dify frontend as a rebranded Ptah shell under the inspected licence;
- source-based multi-tenant hosting without licence authorization;
- Dify workflow, app, tenant, plugin or provider IDs as canonical Ptah identities;
- provider credentials embedded in workflow exports or public configuration;
- graph-node completion promoted to verified operation outcome;
- every plugin/provider enabled by default;
- Dify knowledge-base schema used as Ptah's universal knowledge model;
- marketplace verification treated as complete supply-chain proof;
- broad plugin capability flags used without Ptah object/network/credential scopes;
- latest-version metadata treated as approval to upgrade;
- cache/daemon state used as canonical plugin installation truth.

## Integration decision

**STUDY AND INDEPENDENTLY ADAPT WORKFLOW/APPLICATION/PROVIDER/PLUGIN PATTERNS; HOST DIFY ONLY AS AN OPTIONAL EXTERNAL APPLICATION OR LICENSED SERVICE. DO NOT COPY ITS FRONTEND OR USE IT AS PTAH CORE.**

Useful patterns to adapt independently:

1. typed and versioned visual Recipe graphs;
2. graph execution limits, command channels and event streams;
3. subgraph, variable-pool and node-debug behavior;
4. model/provider/tool/data-source configuration;
5. plugin manifests with unique package identifiers, versions, checksums, resources and permissions;
6. install sources and install/upgrade task status;
7. marketplace deprecation/replacement metadata;
8. tenant-scoped cache invalidation and live-state reconciliation;
9. application API/deployment lifecycle;
10. workflow import/export and versioning concepts.

Any direct deployment must undergo licence review and remain a separate Application/Facility behind Ptah contracts.

## Native Ptah gap

Ptah must define:

- Recipe/Workflow Object independent of Dify;
- Recipe Revision, Node Type/Revision and graph migration identities;
- mapping from Recipe nodes to Ptah Activities and Facilities;
- durable retries, cancellation, checkpoints, compensation and attempts through the Activity runtime;
- model/provider/tool credential references and network scopes;
- node input/output Object and Artifact relationships;
- proof/receipt requirements per node and side effect;
- plugin Package, Manifest, Installation and Activation identities;
- package hash, signature, SBOM, provenance and licence records;
- plugin object, workspace, credential, network and resource permissions;
- install, health, migration, upgrade, rollback, removal and replacement Activities;
- public/private registry and contribution boundaries;
- safe workflow/plugin import and secret redaction;
- public-neutral visual editor and Panel contributions;
- optional Dify adapter plus licence-state record.

## Exit strategy

Ptah Recipes, Activities, Knowledge and Plugins remain independent. Dify may be removed, replaced, commercially licensed or hosted as a separate Application without changing Ptah identities or contracts.

## Validation required

1. Import a representative workflow and map every node/version to Ptah Recipe, Activity and Facility identities.
2. Preserve exact input/output Objects, Artifacts, attempts and receipts across graph execution.
3. Fail, retry, cancel and resume one node without treating Dify runtime state as canonical.
4. Keep credentials secret and scoped to exact nodes, providers, Objects and network destinations.
5. Run Dify as a separate Application without exposing private Ptah internals.
6. Demonstrate that removing Dify does not change Ptah Recipe, Activity, Plugin or Knowledge identities.
7. Complete formal licence review before any multi-tenant, branded or source-derived deployment.
8. Install a plugin from package, GitHub and marketplace sources and retain source, hash, signature, verification and task evidence.
9. Reject an unapproved plugin even when Dify policy would allow `ALL` installation scope.
10. Upgrade a plugin with incompatible saved state and prove Ptah can block, migrate or roll back.
11. Disable Redis/plugin-daemon cache and prove Ptah labels degraded discovery without changing canonical installation state.
12. Remove a plugin and prove dependent Recipes become explicitly unresolved rather than silently remapped.
