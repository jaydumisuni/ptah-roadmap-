# D044 — Dify

Status: candidate record — paired evidence complete

Primary Archivist: `AF04-P01`

Independent Verifier: `AF04-V01`

Inspected: 2026-07-23

## Canonical source identity

- source: `langgenius/dify`;
- default branch: `main`;
- exact inspected commit: `302b50c4fb84f7e7d4637cac278d0ae019dd5ea6`;
- root licence: modified Apache-2.0 with additional multi-tenant, branding and contribution conditions;
- repository role: LLM application-development, workflow, RAG, agent and model-provider platform;
- archived: false.

## Primary evidence packet

Dify exposes useful application-layer patterns for visual workflows, model-provider abstraction, RAG pipelines, tool configuration, APIs, observability and self-hosted deployment. It is not Ptah Core or Ptah's Activity runtime.

## Independent verification packet

The verifier confirmed that the current licence requires a commercial licence for source-based multi-tenant operation unless separately authorized, protects frontend logo/copyright presentation, and permits later licence adjustment. The repository combines public source, Dify Cloud and commercial edition surfaces. Provider integrations, models, external tools and hosted services are separate trust and licence surfaces.

## Contradiction and supersession

The donor pool correctly classified Dify as an application-platform donor, but ordinary Apache-2.0 reuse cannot be assumed. No frozen Ptah contract is superseded, and Dify workspace, workflow, tenant, agent or application identities cannot replace Ptah identities.

## Bounded outcome

`accepted_for_archive_application_platform_study_with_modified_apache_and_multitenancy_restrictions`

Allowed reuse:

- study workflow-design, model-provider, RAG, tool-configuration and application-deployment patterns;
- evaluate a separately reviewed adapter or workload behind Ptah-owned identities;
- reuse source only where the modified licence and every third-party dependency are satisfied.

Restrictions:

- do not use Dify source to operate an unauthorized multi-tenant Ptah service;
- do not remove protected frontend branding where the licence applies;
- do not treat Dify Cloud, paid editions, providers or external tools as rights granted by the public repository;
- do not make Dify Ptah Core, Ptah's scheduler, authority system or mandatory runtime.

This outcome does not authorize implementation.