# D041 — Deno

Status: candidate record — paired evidence complete

Primary Archivist: `AF07-P01`

Independent Verifier: `AF07-V01`

Inspected: 2026-07-23

## Canonical source identity

- source: `denoland/deno`;
- default branch: `main`;
- exact inspected commit: `39c22a203a2b6d7cd3d9d5149c5348fe2268e4a6`;
- root licence: MIT;
- repository role: JavaScript/TypeScript runtime with permission controls and tooling;
- archived: false.

## Primary evidence packet

Deno can inform permission-scoped script execution, TypeScript tooling, package/module loading and lightweight automation runtimes.

## Independent verification packet

Permissions are runtime flags and configuration, not Ptah Policy. npm/JSR/network imports, subprocesses, FFI and unstable APIs create separate trust and reproducibility surfaces. Script completion does not prove external effects.

## Contradiction and supersession

Deno may be a script Provider, not Ptah Core or a replacement for frozen Activity/Policy contracts.

## Bounded outcome

`accepted_for_archive_mit_script_runtime_with_permission_module_network_ffi_and_identity_boundaries`

Allowed reuse:

- run pinned Deno scripts behind Ptah Activity and Policy boundaries;
- retain runtime, module graph, permissions, inputs and outputs.

Restrictions:

- preserve MIT notices and pin remote/npm/JSR dependencies;
- deny network, FFI, subprocess and filesystem access unless caller Policy grants them;
- do not equate Deno permission flags with Ptah authority or completion;
- keep runtime/module IDs as aliases.

This outcome does not authorize implementation.