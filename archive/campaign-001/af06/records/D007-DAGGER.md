# D007 — Dagger

Status: candidate record — paired evidence complete

Primary Archivist: `AF06-P09`

Independent Verifier: `AF06-V09`

Inspected: 2026-07-23

## Canonical source identity

- source: `dagger/dagger`;
- default branch: `main`;
- exact inspected commit: `a2c8cbd50687bfc7466fd860ad0b0ea6e6a3fd12`;
- root licence: Apache-2.0;
- repository role: programmable containerized build and execution engine;
- archived: false.

## Primary evidence packet

Dagger demonstrates typed execution graphs, explicit filesystem/secret inputs, reusable modules, caching, containerized build/test functions and local/CI portability.

## Independent verification packet

Engine, SDK, module, container, cache and cloud surfaces are separately versioned. Cache hits and graph completion do not prove external effects or artifact correctness. Secrets and host sockets require explicit Policy.

## Contradiction and supersession

Dagger can inform Recipe/Build Provider patterns but cannot replace Ptah Activity, Recipe, Receipt or authority contracts.

## Bounded outcome

`accepted_for_archive_apache_typed_build_graph_donor_with_engine_sdk_cache_secret_and_receipt_boundaries`

Allowed reuse:

- study or integrate pinned Dagger execution behind Ptah Build/Recipe Providers;
- retain exact engine, SDK, module, container, cache, inputs, outputs and logs.

Restrictions:

- preserve Apache notices and review SDK/modules/cloud separately;
- never expose secrets or host sockets without caller Policy;
- do not equate cache/graph success with independent Artifact verification;
- do not make Dagger Ptah's canonical Activity or authority system.

This outcome does not authorize implementation.