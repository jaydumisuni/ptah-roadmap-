# D036 — Moby Archive Record

Outcome: ACCEPTED FOR ARCHIVE — modular container-engine donor; no stable-root-library or commercial-support claim

Campaign: `CAMPAIGN-001`

Formation: `AF02`

Primary Archivist: `AF02-P08`

Independent Verifier: `AF02-V08`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `moby/moby`;
- owner: Moby organization;
- visibility: public;
- archived: false;
- default branch: `master`;
- inspected commit: `722d76e76b5363691379ab6fe0ccbc8111f49b0e`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root licence: Apache License 2.0;
- licence evidence: `LICENSE` blob `6d8d58fb676bbbcc9b4432da4951e4b438478306`;
- repository includes a NOTICE and many bundled/external components requiring component-level review;
- engine distributions, containerd/runc/BuildKit integrations, images, registries, plugins and operating-system packages retain separate provenance and support boundaries;
- activity state: active; inspected head merges an engine/runtime panic fix.

## Primary evidence packet — AF02-P08

Inspected:

- `README.md` blob `fae3ea838fb6d1034d0e6ebf3ee39491d1812438`;
- root `LICENSE`;
- exact current head;
- source/test references covering daemon configuration, integration tests, rootless setup, APIs and platform-specific engine paths.

Verified:

- Moby is a modular toolkit/framework for assembling container-based systems rather than a single end-user product;
- principles explicitly favor modular, swappable components and developer-facing APIs;
- the project is upstream for Docker Engine but is not the commercial Docker product/support channel;
- the root `github.com/moby/moby/v2` module builds engine binaries and is not intended as an imported Go library;
- only the independently versioned `github.com/moby/moby/client` and `github.com/moby/moby/api` modules are supported public Go modules;
- the legacy `github.com/docker/docker` Go module is deprecated from Docker v29 onward;
- engine release tags and module tags have different consumption rules;
- releases are community/best-effort supported rather than commercial support guarantees.

Primary conclusion:

Moby remains a foundation-grade container-engine architecture and integration donor. Ptah should use stable public APIs/modules or process-level adapters, not import the root engine module as if it were a stable library or inherit Docker/Moby daemon identity as canonical Activity/Workspace truth.

## Independent verification packet — AF02-V08

Repeated checks:

- canonical identity, `master` branch and exact current head;
- Apache-2.0 root licence;
- modular/swappable component principles;
- relationship to Docker product and best-effort support boundary;
- root module binary-only/no API-stability warning;
- supported client/API modules and deprecated old import path.

Challenges retained:

- container-engine APIs are powerful host-control surfaces requiring policy and least privilege;
- daemon socket exposure can be equivalent to broad host authority;
- rootless mode reduces but does not eliminate kernel/filesystem/network risks;
- images, registries, plugins and build/runtime components require independent pins and trust evidence;
- engine success is not application or artifact correctness proof;
- large integration surface and release/module split increase upgrade risk.

Verifier conclusion: primary findings supported. Moby is a modular upstream donor, not a stable all-purpose library or Ptah authority.

## Ptah relationship

- frozen donor group: build/package/artifact and runtime machinery;
- current classification: optional container-engine provider and architecture study;
- requirements supported: engine API/client patterns, modular runtime/build/network/storage components, rootless/daemon operations and integration test ideas;
- prohibited inheritance: daemon socket reachability as authorization, root module as stable library, container/daemon IDs as canonical Ptah identity, commercial Docker claims as Moby source evidence;
- replacement/exit strategy: use provider-neutral execution contracts and independently versioned client/API modules or process adapters.

## Contradiction and supersession

- current documentation supersedes older `github.com/docker/docker` import guidance with `github.com/moby/moby/client` and `/api` modules;
- root module stability assumptions are explicitly rejected by current primary source;
- canonical repository identity remains `moby/moby` and frozen Ptah architecture is unchanged.

## Bounded outcome

`accepted for archive` does not authorize daemon exposure, engine deployment, image/plugin trust, root-module import, Phase 0A reopening, AF03 start, ADR-0033 acceptance or Ptah runtime implementation.
