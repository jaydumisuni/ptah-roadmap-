# Donor Record — Dify

**Phase:** 0A / WP10  
**Status:** FIRST-PASS COMPLETE — WORKFLOW/APPLICATION CONFIGURATION DONOR WITH MATERIAL LICENCE RESTRICTIONS  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/langgenius/dify
- Default branch: `main`
- Pinned commit: `63ca2b94b5871d7fc338334e70930500006b99b3`
- Licence: modified Apache-2.0 with additional commercial and frontend-branding restrictions
- Activity: Active
- Classification: AI application/workflow, model-provider, tool/plugin and knowledge-application platform donor
- Ptah targets: workflow/application configuration, provider abstraction, node/tool graph patterns, application deployment, knowledge-base management and plugin/provider UX

## Files/components inspected

- `README.md`
- `LICENSE`
- `api/core/workflow/workflow_entry.py`
- graph-engine, node, command-channel, streaming-event, provider/tool/plugin and OTel source locations

## Verified capabilities and patterns

- Provides visual workflow orchestration with typed nodes and graph execution.
- Separates workflow graph definition, execution entry, node factories, variable pools and runtime events.
- Supports model providers, tools, plugins, knowledge retrieval and application APIs.
- Workflow execution has explicit limits, command channels, streaming events and tracing hooks.
- Child/subgraph and iteration-like execution patterns are present.
- Supports self-hosted deployment and a broad application-development surface.
- Treats application configuration, workflow graph, provider settings and runtime execution as distinct components.
- Provides useful operational UX for composing tools, models, data and workflows.

## Licence boundary

Dify's licence is not ordinary Apache-2.0.

At the inspected pin:

- operating Dify source as a multi-tenant service requires a commercial licence unless separately authorized;
- using the Dify frontend from source or its web image prevents removal/modification of its logo and copyright information;
- the interactive design is separately claimed as protected;
- the producer reserves the ability to change the open-source agreement.

This materially limits direct reuse for a public multi-tenant Ptah shell or branded hosted service.

## What Dify completes

- A mature reference for visual workflow/application composition.
- Model-provider and tool/plugin configuration UX.
- Node/graph execution and event-streaming patterns.
- Knowledge/application integration patterns.
- Application API and deployment concepts.
- A useful optional workload/application for users who want a Dify-compatible AI-app builder.

## Important limitations for Ptah

- Dify is an AI application platform, not Ptah's Activity Ledger, Object graph, Workspace Provider or plugin truth.
- Its workflow graph cannot replace Temporal/Ptah durable Activity semantics.
- Model, agent, prompt and reasoning features belong to caller products, not Ptah Core.
- Product workspace/tenant IDs are not Ptah Workspace identity.
- The modified licence conflicts with direct source reuse in a branded multi-tenant Ptah service unless commercially licensed.
- Dify frontend cannot be treated as a freely rebrandable Ptah shell.
- Workflow node success does not prove produced Objects, external side effects or acceptance.
- Provider/plugin ecosystems introduce supply-chain and credential risk.
- Full deployment is operationally heavy for the first Ptah slice.
- Knowledge-base IDs/indexes are derived product state, not canonical Knowledge identity.

## Must not be inherited

- Dify as Ptah Core or the fundamental Activity runtime;
- Dify agent/reasoning/prompt identity inside Ptah;
- direct use of the Dify frontend as a rebranded Ptah shell under the inspected licence;
- source-based multi-tenant hosting without licence authorization;
- Dify workflow/app/tenant IDs as canonical Ptah identities;
- provider credentials embedded in workflow exports or public configuration;
- graph-node completion promoted to verified operation outcome;
- every plugin/provider enabled by default;
- Dify knowledge-base schema used as Ptah's universal knowledge model.

## Integration decision

**STUDY WORKFLOW/APPLICATION/PROVIDER UX AND HOST DIFY ONLY AS AN OPTIONAL EXTERNAL APPLICATION OR LICENSED SERVICE. DO NOT COPY ITS FRONTEND OR USE IT AS PTAH CORE.**

Useful patterns to adapt independently:

- typed visual workflow graphs;
- model/provider/tool configuration;
- streaming node events;
- subgraph and variable-pool behavior;
- application API/deployment lifecycle;
- workflow import/export and versioning concepts.

Any direct deployment must undergo licence review and remain a separate Application/Facility.

## Native Ptah gap

Ptah must define:

- Recipe/Workflow Object independent of Dify;
- mapping from recipe nodes to Ptah Activities/Facilities;
- durable retries/cancellation/checkpoints through the Activity runtime;
- model/provider/tool credential references;
- node input/output Object and Artifact relationships;
- proof/receipt requirements per node;
- plugin trust and permission scopes;
- graph version/migration and replay rules;
- public-neutral visual editor/panel contributions;
- optional Dify adapter and licence-state record.

## Exit strategy

Ptah Recipes and Activities remain independent. Dify may be removed, replaced, commercially licensed or hosted as a separate Application without changing Ptah contracts.

## Validation required

1. Import a representative workflow and map each node to Ptah Activity/Facility identities.
2. Preserve exact input/output Objects and receipts across graph execution.
3. Fail/retry/cancel one node without treating Dify state as canonical.
4. Keep credentials secret and scoped to exact nodes/providers.
5. Run Dify as a separate Application without exposing private Ptah internals.
6. Demonstrate that removing Dify does not change Ptah Recipe, Activity or Knowledge identities.
7. Complete formal licence review before any multi-tenant or branded source deployment.
