# Phase 0C-13 — Durable pinned-host retention readiness

Status: retention tooling passed exact-head review — no physical-host bundle has been produced, retained or accepted

Reviewed: 2026-07-21

## Purpose

Record the repository-bound durable-retention tooling merged from `jaydumisuni/Ptah-space` PR `#11` without treating retention readiness as physical-host proof, package-boundary acceptance, ADR acceptance or runtime authorization.

## Accepted implementation evidence

Repository: `jaydumisuni/Ptah-space`

Pull request: `#11`

Exact tested head:

```text
f0c1aafb58b33fcc8338081244996ced9260ce5c
```

Squash merge commit:

```text
49f6035a93bf704d775dc437e8a8b25c95145ae1
```

Every generated source, durable and review record retains:

```json
"runtime_implementation_authorized": false
```

## Retention boundary implemented

The merged tooling provides two separate layers:

1. `tools/prepare_durable_pinned_host_evidence.py` independently verifies the exact six-file physical-host candidate bundle and encodes its exact bytes for durable retention;
2. `tools/retain_verified_pinned_host_evidence.py` binds that verified bundle to the current clean exact repository commit and reviewed proof-tool bytes before and after retention.

The operator entry point is:

```bash
python3 tools/retain_verified_pinned_host_evidence.py \
  --repo-root . \
  --bundle-dir evidence/phase0c/pinned-host-candidate \
  --output-dir evidence/phase0c/pinned-host-durable-candidate
```

## Independent source-bundle verification

Before retention, the tooling requires and re-verifies:

- exactly `apt-sources.json`, `bundle-manifest.json`, `host-capabilities.json`, `host-identity.json`, `installed-packages.json` and `package-artifacts.json`;
- every source file size and SHA-256;
- the aggregate source bundle digest;
- one clean unchanged implementation commit around collection;
- exact Ubuntu Server 24.04.4, `x86_64` and `6.8.0-136-generic` identity;
- hashed hostname, machine ID and boot ID, with no raw hostname retained;
- a proof-eligible capability report with zero required failures;
- exact installed package identities and aggregate package digest;
- one exact package-artifact SHA-256 identity per installed package;
- package-artifact and APT release/package-index aggregate digests;
- a non-empty APT source manifest and its aggregate digest;
- explicit non-authorization boundaries in every source record.

## Exact repository binding

The final entry point additionally requires:

- current `HEAD` equals the source bundle implementation commit;
- tracked worktree and Git index remain clean;
- only the source and durable evidence lanes may be untracked;
- canonical `host/scripts/collect_capabilities.py` bytes match the collector digest bound into the source bundle;
- canonical `tools/collect_apt_package_artifacts.py` bytes match the bound package collector digest;
- `tools/run_pinned_host_proof.py` exists at the same reviewed commit and its digest is recorded;
- source and output directories are inside the repository, are not symlinks, do not contain one another and do not overwrite an existing candidate;
- the repository commit and clean state remain unchanged after retention;
- the final durable directory contains exactly the expected four records.

## Durable candidate output

A passing retention run creates:

- `durable-pinned-host-bundle.json` — exact base64-encoded source bytes, individual file digests, aggregate retained-file digest and source-bundle bindings;
- `pinned-host-review-record.json` — `review_status: pending`, with physical host, installed package, package artifact, durable retention, ADR and runtime acceptance fields all `false`;
- `repository-binding.json` — exact commit, clean-state, collector, proof-runner and durable/source digest bindings;
- `README.md` — digest and claim-boundary summary.

Durable storage and acceptance remain deliberately separate. Committing these records preserves evidence; it does not accept the physical host or package boundary.

## Adversarial regression coverage

The exact-head host lane covers:

- source-byte tampering;
- non-proof-eligible or authorizing source records;
- missing package-artifact identity coverage;
- raw hostname leakage;
- wrong current Git commit;
- collector-byte mismatch;
- tracked, staged or unexpected untracked changes;
- source or output symlinks;
- nested source/output paths;
- an empty APT source manifest;
- a non-empty destination;
- separate empty-before and populated-after retention rules;
- exact final output-file and pending-review boundaries.

One automated review finding identified that post-retention validation initially reapplied the pre-retention empty-directory rule. The finding was corrected before merge by separating pre-retention and post-retention output conditions. The review thread was resolved.

## Exact-head workflow evidence

All eight workflows passed at exact head `f0c1aafb58b33fcc8338081244996ced9260ce5c`:

| Lane | Workflow run |
|---|---:|
| Frozen contract lock | `29813401646` |
| Generated contract bindings | `29813401632` |
| Host, package-artifact, retention and proof-runner evidence | `29813401728` |
| Rust dependency policy | `29813401773` |
| Backend artifact evidence | `29813401649` |
| Backend signature evidence | `29813401634` |
| Signer lock boundary | `29813401612` |
| Scaffold, source, Rust, Browser and WP13 | `29813401684` |

The hosted host report remains diagnostic rather than physical proof because the hosted runner is not the frozen `6.8.0-136-generic` machine.

## Conditions closed

This evidence closes, at tooling-readiness scope:

1. independent exact-byte verification before durable retention;
2. cross-record host, capability, package, package-artifact, APT-index and APT-source verification;
3. binding to one current clean exact repository commit;
4. binding to canonical collector and proof-runner bytes;
5. exact durable output format and aggregate digest preparation;
6. separation of durable storage from owner/reviewer acceptance;
7. a pending review record that cannot silently authorize runtime;
8. exact-head regression coverage for the complete retention path.

## Conditions still open

This evidence does not close:

- execution on the exact physical Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
- a resulting source bundle with `proof_eligible: true`;
- actual generation and durable commit of that host's retention candidate;
- owner/reviewer acceptance of the physical host identity;
- owner/reviewer acceptance of the installed package manifest;
- owner/reviewer acceptance of the package-artifact manifest;
- owner/reviewer acceptance of the durable retention record;
- owner acceptance of the Apache-2.0 public/private boundary;
- accepted public `LICENSE`, final `NOTICE`, contribution and security boundary;
- the final Phase 0C closure consistency review;
- ADR-0033 acceptance;
- explicit runtime implementation authorization;
- any WP14 runtime proof or implemented runtime behavior.

## Conclusion

The physical-host evidence can now be collected, independently verified, bound to exact reviewed repository bytes and prepared for durable retention without conflating storage with acceptance. The real host run and every governance acceptance remain open. ADR-0033 stays proposed and runtime implementation remains unauthorized.
