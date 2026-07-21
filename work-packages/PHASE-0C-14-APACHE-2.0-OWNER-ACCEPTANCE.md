# Phase 0C-14 — Apache-2.0 owner acceptance

Status: accepted and operative for the public `jaydumisuni/Ptah-space` repository — runtime implementation remains unauthorized

Recorded: 2026-07-21

## Owner decision

The owner authorized proceeding with the reviewed Apache License 2.0 public/private boundary.

Accepted rights-holder wording:

```text
John Dumisuni trading as THETECHGUY DIGITAL SOLUTIONS
```

Accepted notice:

```text
Copyright 2026 John Dumisuni trading as THETECHGUY DIGITAL SOLUTIONS
```

This is an engineering and repository-governance record, not legal advice.

## Candidate evidence

`Ptah-space` PR `#12` prepared a deliberately non-operative boundary candidate.

Exact tested head:

```text
2a54093d0a7856d7b98c77ebaa78899e1626257b
```

Squash merge:

```text
bf846574df65061bd99d9c0e3d22a401bf9f27e2
```

The candidate locked the unchanged official licence bytes, proposed owner wording, public/private scope, contribution and security rules, trademark exclusions and a fail-closed acceptance gate without creating operative root files.

All nine exact-head workflows passed.

## Operative acceptance evidence

`Ptah-space` PR `#13` applied the owner decision.

Exact tested head:

```text
a47d418243af076b49367c4c4eccc8ef2090894c
```

Squash merge:

```text
3ce7d4251db0b6ba3f145385ad7ad8dc09276393
```

The exact official Apache License 2.0 binding is:

```text
Size:    11358 bytes
SHA-256: cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
```

The operative change adds:

- root `LICENSE`;
- `LICENSES/Apache-2.0.txt` with identical bytes;
- root `NOTICE`;
- operative `CONTRIBUTING.md`;
- operative `SECURITY.md` using `support@thetechguyds.com` and `[PTAH SECURITY]`;
- repository-wide `REUSE.toml` Apache-2.0 annotations;
- `legal/apache-2.0-boundary.json` with `apache_2_0_accepted: true`;
- `legal/APACHE-2.0-OWNER-ACCEPTANCE.md`;
- `legal/THIRD-PARTY-NOTICE-REVIEW.md`;
- a fail-closed acceptance checker and seven positive/adversarial regressions.

## Exact-head workflow evidence

All nine workflows passed at exact head `a47d418243af076b49367c4c4eccc8ef2090894c`:

| Lane | Workflow run |
|---|---:|
| Frozen contract lock | `29816645393` |
| Generated contract bindings | `29816645433` |
| Host capability, package-artifact and retention evidence | `29816645472` |
| Rust dependency and licence policy | `29816645480` |
| Backend artifact evidence | `29816645435` |
| Backend signature evidence | `29816645427` |
| Signer lock boundary | `29816645476` |
| Scaffold, source, Browser and WP13 | `29816645410` |
| Apache-2.0 owner acceptance | `29816645483` |

The acceptance lane checked out the exact head, ran all seven regressions, validated the operative boundary, bound the report to the exact commit and retained an evidence artifact.

## Public scope accepted

Apache-2.0 applies by default to repository-owned source, tests, documentation, configuration, schemas, generated metadata bindings, CI definitions and proof tooling intentionally published in `Ptah-space`, unless a more specific file or subtree notice applies.

## Boundaries retained

The public licence does not automatically license:

- private THETECHGUY repositories or Domain Packs;
- Hunter private memory, prompts, knowledge stores or model data;
- customer, device, payment, employee or production records;
- credentials, secrets, private keys or private configuration;
- restricted recovery, bypass, unlock or credential-handling adapters;
- unlicensed donor source or proprietary third-party material;
- THETECHGUY, Ptah, Hunter or related names, marks, logos and branding as trademarks.

Third-party source and binary artifacts retain their own licences and notices. The root NOTICE must be re-reviewed whenever copied or redistributed third-party material introduces an attribution obligation.

## Conditions closed

This evidence closes:

1. owner acceptance of the Apache-2.0 public/private boundary;
2. exact accepted public `LICENSE` bytes;
3. operative root `NOTICE`;
4. operative contribution and security boundaries;
5. repository-wide source-licence annotation;
6. owner identity wording;
7. current third-party NOTICE review;
8. exact-head licence acceptance and adversarial verification.

## Conditions still open

This evidence does not close:

- execution on the exact physical Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
- a resulting source bundle with `proof_eligible: true`;
- acceptance of the installed-package and package-artifact manifests;
- generation, durable commit and explicit acceptance of the physical-host retention candidate;
- the final Phase 0C closure consistency review;
- ADR-0033 acceptance;
- explicit runtime implementation authorization;
- any WP14 runtime proof or implemented runtime behavior.

## Conclusion

The public Ptah repository is now operatively licensed under Apache-2.0 with an explicit owner, private-system boundary, contribution policy, security route and source annotation. This governance decision cannot substitute for the physical-host proof or authorize implementation. `Runtime implementation` remains `NOT AUTHORIZED`.
