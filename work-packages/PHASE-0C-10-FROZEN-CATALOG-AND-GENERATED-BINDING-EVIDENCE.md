# Phase 0C-10 — Frozen catalog and generated binding closure evidence

Status: passed for frozen-contract import and generated-binding scope — runtime implementation remains unauthorized

Reviewed: 2026-07-20

## Purpose

Close the Phase 0C frozen public catalog-lock and deterministic generated-binding conditions without implementing or authorizing Ptah runtime behavior.

## Accepted implementation evidence

Repository: `jaydumisuni/Ptah-space`

Pull request: `#5`

Exact tested head:

```text
33043eaadb0f074d8867cb8ce999f16ea4c06a8b
```

Merge commit:

```text
f45c96e3f667b463042b6a8b714066236fde703d
```

The accepted `contracts/upstream-lock.json` state is:

```text
frozen_catalogs_and_bindings_locked_runtime_dependencies_open
```

This state explicitly keeps runtime implementation unauthorized.

## Frozen catalog lock

- active catalog count: `14`;
- frozen roadmap checkpoint: `dc2db457f1705d0cba80f17ab76e5e93f808aee0`;
- WP14 merge: `fef387c4f074af7fcf86f2d99f7f9b7637e91f88`;
- aggregate catalog-set SHA-256:

```text
f0668a5f5d5c68cabf623176608c627a94482faa4f4460e4f0fe0f0969d7c64d
```

Every active catalog is recorded by exact repository path, canonical catalog URN, original-byte SHA-256, size, schema count and lifecycle-machine count. Network schema resolution remains disabled.

## Final generated binding lock

Generator:

- name: `ptah-phase0c-contract-bindings-final`;
- version: `0.3.0`;
- source: `tools/contract_binding_generator_final.py`;
- generator SHA-256: `17d62144dea2e2135f9e25a505d8cbc3132342d5691db4a9dae04dfbbc0280be`;
- formatting authority: `rustfmt 1.8.0-stable` from the Rust `1.97.1` toolchain.

The manifest records all three generator sources and their digests:

- final formatter/generator: `17d62144dea2e2135f9e25a505d8cbc3132342d5691db4a9dae04dfbbc0280be`;
- alias-aware identity normalizer: `13dab87ecf1aa1ac671273e2ae947a0dc7e1b5063529cde15108d86ff03c0077`;
- base catalog/schema/lifecycle generator: `8133d3315d93f096efe5adabc3e3eef62fb74a6988f7ced67ebe2986241120ce`.

Generated evidence:

| Output | SHA-256 | Size |
|---|---|---:|
| `contracts/generated/manifest.json` | `63fd0cb0fd4ef172271aa7a114e74bb24c0a9e70cc247faeff1db95f7a67d97d` | 1,790 bytes |
| `contracts/generated/catalog-index.json` | `0f97e222d9baf9f90721d2a30dd2b31920b53489ae343b0430cc9089c8fdaf9c` | 199,900 bytes |
| `crates/ptah-contracts/src/generated.rs` | `748e87f1a8cf2ed20d694aa716dd8f18b7ea4b3016372386202aeeaff687ae50` | 193,392 bytes |

Generated output-tree SHA-256:

```text
8f3355e0eac19715ea34e06ea227a826ac727d2e5b9ebf231a672927350c8db2
```

Bound identities:

- catalogs: `14`;
- canonical schemas: `346`;
- lifecycle machines: `99`.

Legacy catalog identifiers that differ from a referenced file's canonical identity are retained only as aliases. The file `$id` or lifecycle source remains canonical.

## Exact-head workflow results

### Frozen contract lock

Workflow run: `29727701958`

Passed:

- exact pull-request-head checkout;
- frozen catalog path/URN/digest regeneration;
- committed lock byte comparison;
- generated manifest and output digest verification;
- retained exact-head report.

Artifact:

- ID: `8454924392`;
- SHA-256: `94fe06c5943baf20858011ba288f77778ea96c82aac6cdf8889842a88e82f3d6`.

### Generated contract bindings

Workflow run: `29727701960`

Passed:

- candidate A generation from frozen local files;
- candidate-to-committed-tree byte comparison;
- independent candidate B generation;
- byte-identical candidate A/B comparison;
- exact-head binding report and artifact retention.

Artifact:

- ID: `8454924065`;
- SHA-256: `5f8d190e9bfb775a6f3182603d0120bbedd145a6ab04f42adff69084d405da1a`.

### Scaffold and frozen conformance

Workflow run: `29727701999`

All four jobs passed:

1. source-policy/no-build boundary;
2. Rust formatting, Clippy, workspace tests and locked metadata;
3. Browser locked installation, syntax, tests and dependency inventory;
4. frozen WP13 harness unit, structural and semantic conformance.

Artifacts:

| Lane | Artifact ID | SHA-256 |
|---|---:|---|
| Source policy | `8454924409` | `3c27c7fd2ec796321c859f80773c38d6dd6c72324c4f6b6609ec290ddc30cd4d` |
| Browser | `8454924718` | `2caf6178f8af7b631df06563eb416f3f78f82bec1bf2d9b113919fed507b90ac` |
| Frozen conformance | `8454926663` | `56069d6d2dd85d8ad5d44966fac91093f80d9769f8f73ab700fb6d66c6c1893e` |
| Rust | `8454926802` | `2dfb2bd34f2f2cacf067db8c40040511c0dec26136e79c5dc60a5aa478cfe8c0` |

## Conditions closed

This evidence closes:

1. complete frozen public catalog inventory by path, URN and original-byte digest;
2. deterministic offline metadata binding generation;
3. generated manifest, index, Rust-module and output-tree digest recording;
4. canonical schema/lifecycle identity and legacy-alias handling;
5. two independent byte-identical binding generations;
6. generated Rust compilation, formatting, Clippy and tests;
7. exact-head catalog-lock and binding-generation CI;
8. frozen WP13 conformance at the same exact head;
9. no-build policy recognition of the binding-locked state without runtime authorization.

## Conditions still open

This evidence does not close:

- owner acceptance of the Apache-2.0 public/private boundary;
- final public `LICENSE`, `NOTICE`, contribution and security files;
- the minimal external Rust runtime dependency graph;
- final runtime `Cargo.lock`, crate licence inventory and advisory review;
- authoritative installed/distributed backend hashes and signatures;
- real pinned-host capability evidence;
- dependency-policy CI;
- durable evidence retention beyond temporary GitHub artifact expiry;
- Phase 0C closure review;
- ADR-0033 acceptance;
- runtime implementation authorization;
- any WP14 runtime proof.

## Conclusion

The frozen-contract import and generated-binding sub-gate is complete. `Ptah-space` now has reproducible, compile-tested metadata bindings for the exact Phase 0B contract set. These bindings contain metadata and lookup functions only; they do not implement Node, Workspace, Activity, Provider, transfer, Browser or UI runtime behavior.