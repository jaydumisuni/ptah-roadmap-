# D037 — Docker CLI

Status: candidate record — paired evidence complete

Primary Archivist: `AF03-P10`

Independent Verifier: `AF03-V10`

Inspected: 2026-07-23

## Canonical source identity

- source: `docker/cli`;
- default branch: `master`;
- exact inspected commit: `7a54334eb038871b45c2377baf8c12beaa14839c`;
- root licence: Apache License 2.0;
- repository role: Docker command-line client;
- archived: false.

## Primary evidence packet

The repository contains the Docker CLI, its commands, API client integrations, configuration handling, context selection, plugins, build/test tooling and cross-platform binaries.

Useful Ptah donor concepts include:

- a command-line projection over a replaceable backend API;
- explicit client contexts and endpoint configuration;
- separating user-facing commands from daemon/runtime implementation;
- cross-platform CLI build and test workflows;
- preserving command, argument, context, endpoint, output and exit evidence;
- extension through CLI plugins without merging plugin identity into Core.

## Independent verification packet

The verifier confirmed:

- the exact repository is Apache-2.0 and has a separate NOTICE file and export-control warning;
- this repository is the CLI, not Docker Engine, containerd, runc, BuildKit, Docker Desktop, registries or hosted services;
- Docker contexts and daemon object IDs are backend-specific and cannot replace Ptah canonical Provider, Node, Workspace, Activity, Object or Artifact identities;
- CLI exit success or daemon acknowledgement does not independently prove the requested container workload, transfer, build or cleanup succeeded;
- plugins, credential helpers, Compose, Buildx and daemon/API versions are separate dependency and trust surfaces;
- endpoint selection can redirect commands to remote infrastructure and therefore requires explicit authority and evidence.

## Contradiction and supersession

The donor pool classified Docker CLI under build, package and artifact machinery. Current evidence supports its client/UX and backend-adapter patterns, but not treating the CLI as a container runtime, build engine or canonical object model.

No frozen Ptah Provider or identity decision is superseded. A Docker-compatible CLI adapter would remain optional and must preserve exact daemon/API/provider identities and post-condition checks.

## Bounded outcome

`accepted_for_archive_apache_cli_adapter_with_daemon_and_context_boundaries`

Allowed reuse:

- study or potentially adapt Apache-2.0 CLI architecture and command/context patterns;
- retain exact CLI, plugin, context, endpoint, daemon/API, command, output and exit evidence;
- expose Docker-compatible operations only through explicitly configured Provider authority.

Restrictions:

- preserve Apache-2.0 notices, NOTICE obligations and separately review plugins, helpers and related repositories;
- do not claim the CLI contains Docker Engine, containerd, runc, BuildKit, Desktop or hosted services;
- do not map Docker context or object IDs directly onto canonical Ptah identities;
- require endpoint authority and post-condition verification for remote or consequential commands;
- do not treat CLI success as workload, build, transfer or cleanup success;
- do not make Docker CLI Ptah’s required interface or container authority.

This outcome does not authorize implementation.