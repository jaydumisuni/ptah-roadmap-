# D014 — Coder

Status: candidate record — paired evidence complete

Primary Archivist: `AF03-P06`

Independent Verifier: `AF03-V06`

Inspected: 2026-07-23

## Canonical source identity

- source: `coder/coder`;
- default branch: `main`;
- exact inspected commit: `591edcb050f384a8ccfba3b04b78d061c7111b92`;
- root licence: GNU Affero General Public License version 3;
- archived: false.

## Primary evidence packet

Coder is a real self-hosted control plane for cloud development environments and coding-agent execution. Public source covers a server, CLI, workspace templates, identity/audit concepts and infrastructure provisioning through Terraform-backed templates.

Useful Ptah donor concepts include:

- durable remote development workspaces;
- separating workspace templates from provisioned workspace instances;
- automatic idle-resource shutdown;
- user identity and audit association for actions;
- connecting existing IDEs to remote environments;
- keeping provider-specific infrastructure behind templates and modules.

## Independent verification packet

The verifier confirmed:

- the exact repository is AGPL-3.0, creating network-use source obligations for modified deployments;
- the README distinguishes the public self-hosted platform from Premium features, registries, extensions, plugins and community templates;
- workspace infrastructure can span Docker, Kubernetes and cloud VMs, so each template/provider remains a separate trust, cost and rights surface;
- Coder workspace, template, agent and control-plane identities are backend-specific and cannot replace Ptah canonical Workspace, Node, Provider, Activity or authority identities;
- self-hosting does not eliminate external access, PostgreSQL, Terraform/provider, WireGuard, model-provider, extension or registry dependencies.

## Contradiction and supersession

The donor pool classified Coder as a workspace and sandbox donor. Current evidence supports studying its remote-development control-plane and template patterns, but not treating it as a neutral universal substrate or assuming all advertised enterprise/agent capabilities are available in the public AGPL repository.

No frozen Ptah Workspace, identity or authority decision is superseded. Coder could only be an optional workload/control-plane Provider behind Ptah-owned identities and explicit AGPL compliance.

## Bounded outcome

`accepted_for_archive_with_agpl_control_plane_and_premium_surface_restrictions`

Allowed reuse:

- study or potentially deploy the public AGPL control-plane patterns behind a replaceable Provider boundary;
- retain exact template, infrastructure, user, workspace, agent and audit evidence;
- use remote-development UX and lifecycle concepts as donor input.

Restrictions:

- comply with AGPL-3.0, including network-use obligations for modified deployments;
- separately review Premium features, registries, templates, modules, extensions, model providers and deployment dependencies;
- do not map Coder identities directly onto canonical Ptah identities;
- do not make Coder Ptah’s authority, required workspace backend or universal scheduler;
- do not expose credentials, private source or customer infrastructure through templates or hosted integrations without configured authority.

This outcome does not authorize implementation.