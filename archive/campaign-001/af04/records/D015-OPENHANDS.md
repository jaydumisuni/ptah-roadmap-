# D015 — OpenHands

Status: candidate record — paired evidence complete

Primary Archivist: `AF04-P08`

Independent Verifier: `AF04-V08`

Inspected: 2026-07-23

## Canonical source identity

- source: `OpenHands/OpenHands`;
- default branch: `main`;
- exact inspected commit: `e42220d0e2a8493fe78ccfb602ee6216347d737e`;
- root licence: MIT outside `enterprise/`; enterprise directory separately licensed;
- repository role: self-hosted developer control centre and transition repository for agent backends/automations;
- archived: false.

## Primary evidence packet

OpenHands demonstrates agent workspace, coding-session, repository, terminal, automation and backend-switching experiences. Its current repository directs agent/server implementation to `OpenHands/software-agent-sdk` and Agent Canvas to `OpenHands/agent-canvas`, making those separate source and licence surfaces.

## Independent verification packet

The verifier confirmed explicit warnings that non-sandboxed operation gives the agent full filesystem access. Local, Docker, VM, cloud and enterprise backends have different isolation and trust conditions. The enterprise directory is not covered by the root MIT grant.

## Contradiction and supersession

OpenHands remains an application/workspace experience donor, not Ptah Core. The repository's current transition means older architecture assumptions must not be treated as current implementation truth.

## Bounded outcome

`accepted_for_archive_agent_workspace_experience_with_repository_transition_enterprise_and_host_access_restrictions`

Allowed reuse:

- study agent-workspace, backend-switching, repository, terminal and automation UX patterns;
- inspect `software-agent-sdk` and `agent-canvas` separately before any integration;
- run a separately pinned OpenHands workload only behind Ptah isolation, Policy, Receipt and Artifact boundaries.

Restrictions:

- preserve MIT notices and exclude/review `enterprise/` under its own terms;
- do not run agents directly on a host or mount broad project paths without explicit caller Policy and isolation proof;
- do not infer cloud, enterprise, ACP backend or third-party agent rights from the public root repository;
- do not make OpenHands Ptah Core, Ptah's authority model or mandatory agent identity.

This outcome does not authorize implementation.