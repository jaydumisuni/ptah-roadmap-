# Phase 0C-12 — Pinned-host proof integrity and package-artifact readiness

Status: proof tooling passed exact-head review — physical pinned-host proof, package acceptance, durable retention, licence acceptance and runtime authorization remain open

Reviewed: 2026-07-21

## Purpose

Record the proof-integrity repairs and exact installed-package artifact evidence tooling merged from `jaydumisuni/Ptah-space` PRs `#9` and `#10` without treating tooling readiness, a hosted CI run or local APT metadata as proof that the frozen physical host has passed.

## Accepted implementation evidence

Repository: `jaydumisuni/Ptah-space`

### Proof-integrity repair

Pull request: `#9`

Exact tested head:

```text
4e871b2bad8c4054ef1e9a1245219fa231338458
```

Squash merge commit:

```text
b97c2defbba17d75e32cb0a02cda9bbb2b1c6649
```

### Installed-package artifact evidence

Pull request: `#10`

Exact tested head:

```text
74aef4b6a4ddebb7f2491fc0eb127d945ac05a14
```

Squash merge commit:

```text
50969c414b55460b6ff7a7d12fd7ae88f5ef5c0a
```

Every generated proof record retains:

```json
"runtime_implementation_authorized": false
```

## Proof-integrity defects corrected

The first merged proof runner was not safe to use as final evidence because:

1. it searched legacy tool-directory collector names although the accepted collector is `host/scripts/collect_capabilities.py`;
2. bundle eligibility did not require the accepted capability report itself to pass;
3. the documented in-repository output directory made the checkout appear dirty after generating its own evidence;
4. retained capability and boot records could expose raw hostname or boot identity;
5. the exact-head host workflow did not execute the proof-runner regression suite;
6. legacy collector fallbacks could silently replace the accepted collector.

PR `#9` corrected those defects by:

- accepting only `host/scripts/collect_capabilities.py`;
- requiring the capability report to record `required_capabilities_passed: true`, `pinned_host_match.all_match: true`, `proof_eligible: true` and zero required failures;
- proving repository cleanliness before and after collection while excluding only the fresh selected output directory;
- failing closed on tracked, staged or unexpected untracked changes, a non-empty output directory or a changing `HEAD`;
- retaining hashed hostname, machine ID and boot ID representations rather than raw identifiers;
- executing the pinned-host regressions in the exact-head host lane;
- rejecting legacy-only collector layouts.

## Exact installed-package artifact evidence

PR `#10` adds `tools/collect_apt_package_artifacts.py` and binds its result into `tools/run_pinned_host_proof.py`.

For every exact installed `dpkg` package/version/architecture record, the collector:

- validates strict string identity fields and rejects duplicate or malformed package identities;
- queries the existing local APT cache with exact version and architecture selectors in bounded batches;
- uses an exact-version architecture-neutral fallback only for unresolved identities;
- requires `Filename`, numeric `Size` and one 64-character `SHA256` record;
- fails closed on conflicting digest/size records;
- hashes the local `/var/lib/apt/lists` inventory;
- requires both release metadata and package-index files;
- records all missing artifact identities and attempted selectors;
- does not run `apt update`, contact mirrors or download package files.

The retained SHA-256 values are the binary-package artifact digests recorded in the local APT metadata for the exact installed version and architecture. They are not a claim that the original `.deb` remains cached locally, and they do not independently replace the final package-boundary review.

## Bundle eligibility after the repairs

`bundle-manifest.json` schema `0.3.0` can record `proof_eligible: true` only when all of the following pass together:

1. Ubuntu Server `24.04.4`, `x86_64` and kernel `6.8.0-136-generic` match exactly;
2. the accepted capability report passes every required capability and its own pinned-host identity gate;
3. every installed package has one exact version/architecture APT artifact SHA-256 record;
4. the APT release and package-index inventory is present and hashed;
5. the repository remains clean at one unchanged exact commit before and after collection;
6. no host, capability, package-artifact or repository failure is recorded.

The package-artifact collector remains local-only and records `network_used: false`.

## Exact-head workflow evidence

All eight workflows passed at PR `#9` exact head `4e871b2bad8c4054ef1e9a1245219fa231338458`:

| Lane | Workflow run |
|---|---:|
| Frozen contract lock | `29810141222` |
| Generated contract bindings | `29810141192` |
| Host capability and proof-runner evidence | `29810141195` |
| Rust dependency policy | `29810141189` |
| Backend artifact evidence | `29810141245` |
| Backend signature evidence | `29810141201` |
| Signer lock boundary | `29810141305` |
| Scaffold, source, Rust, Browser and WP13 | `29810141226` |

All eight workflows passed again at PR `#10` exact head `74aef4b6a4ddebb7f2491fc0eb127d945ac05a14`:

| Lane | Workflow run |
|---|---:|
| Frozen contract lock | `29811724517` |
| Generated contract bindings | `29811724529` |
| Host, package-artifact and proof-runner evidence | `29811724538` |
| Rust dependency policy | `29811724492` |
| Backend artifact evidence | `29811724572` |
| Backend signature evidence | `29811724594` |
| Signer lock boundary | `29811724499` |
| Scaffold, source, Rust, Browser and WP13 | `29811724520` |

The final host lane checked out the exact PR head and passed the host collector, identity finalizer, package-artifact and pinned-host proof regression suites. The hosted runner remains diagnostic because its kernel identity is not the accepted physical proof host.

## Operator command

On the exact frozen Ubuntu Server 24.04.4 / `6.8.0-136-generic` host, from a clean checkout of the reviewed candidate commit:

```bash
python3 tools/run_pinned_host_proof.py \
  --repo-root . \
  --output evidence/phase0c/pinned-host-candidate
```

The output directory must be absent or empty before collection.

## Conditions closed

This evidence closes, at proof-tooling readiness scope:

1. canonical host-capability collector discovery;
2. independent capability-report validation inside final bundle eligibility;
3. pre- and post-collection clean exact-commit binding;
4. privacy-preserving host, machine and boot identity retention;
5. exact installed package/version/architecture inventory generation;
6. exact local APT binary-artifact SHA-256 metadata collection;
7. fail-closed package-artifact completeness and APT index inventory validation;
8. exact-head regression coverage for the complete proof runner;
9. one command that produces the host, capability, installed-package, APT-source, package-artifact and aggregate bundle records.

## Conditions still open

This evidence does not close:

- execution on the exact physical Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
- a resulting bundle with `proof_eligible: true`;
- owner/reviewer acceptance of the installed package and package-artifact manifests;
- durable retention of that accepted physical-host bundle beyond temporary workflow expiry;
- owner acceptance of the Apache-2.0 public/private boundary;
- accepted public `LICENSE`, final `NOTICE`, contribution and security boundary;
- the final Phase 0C closure consistency review;
- ADR-0033 acceptance;
- explicit runtime implementation authorization;
- any WP14 runtime proof or implemented runtime behavior.

## Conclusion

The pinned-host proof command is now executable, privacy-preserving and fail-closed against host identity, capabilities, package artifacts and repository state. The remaining technical evidence must be produced on the real frozen host and reviewed durably. Governance and closure blockers remain unchanged. ADR-0033 stays proposed and runtime implementation remains unauthorized.
