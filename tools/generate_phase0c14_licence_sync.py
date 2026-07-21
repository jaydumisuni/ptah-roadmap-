#!/usr/bin/env python3
"""Generate the Phase 0C-14 licence-acceptance roadmap synchronization.

The generator reads the exact current control records, applies guarded literal
replacements, and writes proposed outputs under generated-sync. It never edits
canonical files directly and never authorizes runtime implementation.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated-sync"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def write(relative: str, text: str) -> dict[str, object]:
    path = OUT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    raw = text.encode("utf-8")
    path.write_bytes(raw)
    return {
        "path": relative,
        "size_bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }


def current_state() -> str:
    path = ROOT / "CURRENT_STATE.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "**Production dependency/backend selection:** EXACT RUST, DISTRIBUTED ARTIFACT, PROOF AND RETENTION TOOL LOCKS MERGED — PHYSICAL PINNED-HOST PROOF OPEN  ",
        "**Production dependency/backend selection:** EXACT RUST, DISTRIBUTED ARTIFACT, PROOF AND RETENTION TOOL LOCKS MERGED — APACHE-2.0 BOUNDARY ACCEPTED — PHYSICAL PINNED-HOST PROOF OPEN  ",
        "current state headline",
    )
    text = replace_once(
        text,
        "- `work-packages/PHASE-0C-13-DURABLE-PINNED-HOST-RETENTION-READINESS.md`;\n- proposed `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`.",
        "- `work-packages/PHASE-0C-13-DURABLE-PINNED-HOST-RETENTION-READINESS.md`;\n- `work-packages/PHASE-0C-14-APACHE-2.0-OWNER-ACCEPTANCE.md`;\n- proposed `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`.",
        "current state record list",
    )
    text = replace_once(
        text,
        "- Apache License 2.0 as the proposed public Ptah-owned source licence, pending owner acceptance.",
        "- Apache License 2.0 accepted for repository-owned public Ptah source, with private THETECHGUY systems, data, restricted adapters and trademarks excluded.",
        "current state licence baseline",
    )
    section = """## Merged Apache-2.0 public/private boundary acceptance

The non-operative boundary candidate was tested in `Ptah-space` PR `#12` at exact head:

```text
2a54093d0a7856d7b98c77ebaa78899e1626257b
```

and squash-merged at:

```text
bf846574df65061bd99d9c0e3d22a401bf9f27e2
```

The owner-acceptance change was then tested in PR `#13` at exact head:

```text
a47d418243af076b49367c4c4eccc8ef2090894c
```

and squash-merged at:

```text
3ce7d4251db0b6ba3f145385ad7ad8dc09276393
```

The accepted boundary records:

- rights holder `John Dumisuni trading as THETECHGUY DIGITAL SOLUTIONS`;
- exact official Apache License 2.0 bytes at root `LICENSE` and `LICENSES/Apache-2.0.txt`;
- licence size `11358` bytes and SHA-256 `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30`;
- operative `NOTICE`, `CONTRIBUTING.md`, `SECURITY.md` and repository-wide `REUSE.toml` annotations;
- explicit private-system, customer/device/payment, restricted-adapter, donor-source and trademark exclusions;
- a reviewed third-party NOTICE boundary and mandatory re-review triggers;
- historical candidate records preserved as non-operative evidence;
- `runtime_implementation_authorized: false` in the accepted machine record and exact-head evidence.

All nine exact-head workflows passed at the acceptance head, including the new licence-acceptance lane, Rust dependency/licence policy, source/no-build, host, backend, signer, frozen-contract and generated-binding gates.

This closes the Apache-2.0 owner decision and operative public repository governance files only. It does not close the physical-host, package, durable-retention, ADR or runtime-authorization gates.

---

"""
    text = replace_once(
        text,
        "---\n\n## Active Phase 0C blockers",
        "---\n\n" + section + "## Active Phase 0C blockers",
        "current state licence section insertion",
    )
    old_blockers = """Implementation remains unauthorized until all of the following are merged and reviewed:

1. owner acceptance of the Apache-2.0 public/private boundary;
2. final public `LICENSE`, `NOTICE`, contribution and security boundary;
3. a proof-eligible capability report from the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
4. the exact installed Ubuntu package manifest and package-artifact digests from that pinned host, with reviewer acceptance;
5. generation, durable commit and explicit review acceptance of that physical-host evidence bundle;
6. a Phase 0C closure review proving no frozen contract was weakened;
7. acceptance of ADR-0033;
8. explicit `Runtime implementation: AUTHORIZED` in this file in the same reviewed closure change.

The frozen catalog, generated binding, exact Rust dependency graph, Cargo lock, cargo-deny policy, distributed backend artifact lock, Browser binary tree, signer lock, cryptographic signature, source-policy, Rust, Browser, host-collector, pinned-host proof-tool, package-artifact, durable-retention and frozen-WP13 lanes are complete. They do not close the physical pinned-host result, package acceptance, actual retained-bundle acceptance, governance acceptance or any WP14 runtime proof."""
    new_blockers = """Implementation remains unauthorized until all of the following are merged and reviewed:

1. a proof-eligible capability report from the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
2. the exact installed Ubuntu package manifest and package-artifact digests from that pinned host, with reviewer acceptance;
3. generation, durable commit and explicit review acceptance of that physical-host evidence bundle;
4. a Phase 0C closure review proving no frozen contract was weakened;
5. acceptance of ADR-0033;
6. explicit `Runtime implementation: AUTHORIZED` in this file in the same reviewed closure change.

The frozen catalog, generated binding, exact Rust dependency graph, Cargo lock, cargo-deny policy, distributed backend artifact lock, Browser binary tree, signer lock, cryptographic signature, source-policy, Rust, Browser, host-collector, pinned-host proof-tool, package-artifact, durable-retention, Apache-2.0 governance and frozen-WP13 lanes are complete. They do not close the physical pinned-host result, package acceptance, actual retained-bundle acceptance or any WP14 runtime proof."""
    text = replace_once(text, old_blockers, new_blockers, "current state blockers")
    text = replace_once(
        text,
        "- licence and contribution decisions;",
        "- accepted licence, contribution, security and third-party-notice boundary maintenance;",
        "current state allowed work",
    )
    text = replace_once(
        text,
        "6. Commit the durable candidate, repository binding and pending review record to a durable proof Location.\n7. Explicitly accept the host identity, installed packages, package artifacts and durable retention in reviewed evidence.\n8. Complete the Apache-2.0 owner decision and public/private notice boundary.\n9. Conduct the Phase 0C closure consistency review.\n10. Accept ADR-0033 and authorize runtime only if every blocker passes.",
        "6. Commit the durable candidate, repository binding and pending review record to a durable proof Location.\n7. Explicitly accept the host identity, installed packages, package artifacts and durable retention in reviewed evidence.\n8. Conduct the Phase 0C closure consistency review.\n9. Accept ADR-0033 and authorize runtime only if every blocker passes.",
        "current state continuation order",
    )
    return text


def progress() -> str:
    path = ROOT / "PROGRESS.md"
    text = path.read_text(encoding="utf-8")
    section = """## Apache-2.0 public/private boundary acceptance

- [x] non-operative boundary candidate exact-head tested and merged as `bf846574df65061bd99d9c0e3d22a401bf9f27e2`;
- [x] owner accepted `John Dumisuni trading as THETECHGUY DIGITAL SOLUTIONS` as the rights-holder wording;
- [x] exact official Apache-2.0 bytes installed at root `LICENSE` and `LICENSES/Apache-2.0.txt`;
- [x] root `NOTICE`, `CONTRIBUTING.md`, `SECURITY.md` and `REUSE.toml` made operative;
- [x] private THETECHGUY systems, data, restricted adapters, donor source and trademarks excluded;
- [x] third-party NOTICE review and future re-review triggers recorded;
- [x] seven positive/adversarial acceptance regressions passed;
- [x] all nine workflows passed at exact head `a47d418243af076b49367c4c4eccc8ef2090894c`;
- [x] owner-acceptance change squash-merged as `3ce7d4251db0b6ba3f145385ad7ad8dc09276393`;
- [x] runtime implementation remained unauthorized.

"""
    text = replace_once(
        text,
        "## Active Phase 0C closure work",
        section + "## Active Phase 0C closure work",
        "progress licence section insertion",
    )
    text = replace_once(
        text,
        "- [?] owner acceptance of Apache License 2.0 and the public/private contribution boundary;\n- [ ] add accepted public `LICENSE`, `NOTICE`, contribution and security files;",
        "- [x] owner acceptance of Apache License 2.0 and the public/private contribution boundary;\n- [x] add accepted public `LICENSE`, `NOTICE`, contribution and security files;",
        "progress licence completion",
    )
    text = replace_once(
        text,
        "- [x] no public licence is claimed before owner acceptance;",
        "- [x] accepted public Apache-2.0 governance does not authorize runtime implementation;",
        "progress no-build licence boundary",
    )
    return text


def adr() -> str:
    path = ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "Status: proposed — Rust dependencies, distributed backend artifacts, signers, host collector, physical-proof and durable-retention tooling complete; physical pinned-host result, package and retention acceptance, licence acceptance and closure review remain open",
        "Status: proposed — Rust dependencies, distributed backend artifacts, signers, host collector, physical-proof, durable-retention and Apache-2.0 governance complete; physical pinned-host result, package and retention acceptance and closure review remain open",
        "ADR status",
    )
    text = replace_once(
        text,
        "- `work-packages/PHASE-0C-13-DURABLE-PINNED-HOST-RETENTION-READINESS.md`.",
        "- `work-packages/PHASE-0C-13-DURABLE-PINNED-HOST-RETENTION-READINESS.md`;\n- `work-packages/PHASE-0C-14-APACHE-2.0-OWNER-ACCEPTANCE.md`.",
        "ADR record list",
    )
    text = replace_once(
        text,
        "- Apache License 2.0 recommendation for public Ptah-owned source, excluding private THETECHGUY knowledge, customer/device data and restricted workflows.",
        "- Apache License 2.0 accepted for public repository-owned Ptah source, excluding private THETECHGUY knowledge, customer/device data, restricted workflows and trademarks.",
        "ADR licence baseline",
    )
    section = """## Merged Apache-2.0 owner acceptance

The non-operative boundary candidate was tested in `Ptah-space` PR `#12` at exact head `2a54093d0a7856d7b98c77ebaa78899e1626257b` and squash-merged as `bf846574df65061bd99d9c0e3d22a401bf9f27e2`.

The operative owner-acceptance change was tested in PR `#13` at exact head `a47d418243af076b49367c4c4eccc8ef2090894c` and squash-merged as `3ce7d4251db0b6ba3f145385ad7ad8dc09276393`.

The accepted licence boundary provides:

- exact official Apache License 2.0 bytes, size `11358`, SHA-256 `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30`;
- rights-holder wording `John Dumisuni trading as THETECHGUY DIGITAL SOLUTIONS`;
- operative root `LICENSE`, `NOTICE`, `CONTRIBUTING.md` and `SECURITY.md`;
- `LICENSES/Apache-2.0.txt` and repository-wide `REUSE.toml` source annotations;
- explicit private THETECHGUY, customer/device/payment, restricted-adapter, donor-source and trademark exclusions;
- a third-party NOTICE review with mandatory re-review triggers;
- exact-head verification that licence acceptance cannot set runtime authorization true.

All nine exact-head workflows passed. This closes the licence/public-private governance conditions only and leaves the physical-host, package, retention, closure-review, ADR and explicit authorization conditions open.

"""
    text = replace_once(
        text,
        "## Conditions before acceptance",
        section + "## Conditions before acceptance",
        "ADR licence section insertion",
    )
    text = replace_once(
        text,
        "35. exact-head adversarial coverage for the full durable-retention path.\n\n### Still open",
        "35. exact-head adversarial coverage for the full durable-retention path;\n36. accepted Apache-2.0 owner and public/private boundary;\n37. exact official root licence and machine-readable copy;\n38. operative NOTICE, contribution, security and REUSE source-annotation boundary;\n39. third-party NOTICE review and private/trademark exclusions;\n40. exact-head adversarial coverage for the operative licence acceptance.\n\n### Still open",
        "ADR completed conditions",
    )
    old_open = """This ADR remains proposed until all of the following are complete:

1. the owner accepts the Apache-2.0 public/private boundary;
2. `Ptah-space` adds the accepted public `LICENSE`, final `NOTICE` and contribution/security boundary;
3. a proof-eligible capability report is produced on the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
4. the exact installed Ubuntu package manifest and package-artifact digests are recorded from that host and accepted by review;
5. that host's exact source bundle is independently verified, durably committed and explicitly accepted through its review record;
6. a Phase 0C closure review confirms no frozen contract was weakened;
7. this ADR is changed to accepted;
8. `CURRENT_STATE.md` is updated to `Runtime implementation: AUTHORIZED` in the same reviewed closure change."""
    new_open = """This ADR remains proposed until all of the following are complete:

1. a proof-eligible capability report is produced on the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
2. the exact installed Ubuntu package manifest and package-artifact digests are recorded from that host and accepted by review;
3. that host's exact source bundle is independently verified, durably committed and explicitly accepted through its review record;
4. a Phase 0C closure review confirms no frozen contract was weakened;
5. this ADR is changed to accepted;
6. `CURRENT_STATE.md` is updated to `Runtime implementation: AUTHORIZED` in the same reviewed closure change."""
    text = replace_once(text, old_open, new_open, "ADR open conditions")
    text = replace_once(
        text,
        "- the current scaffold, catalog lock, generated bindings, dependency graph, backend artifacts, signer proofs, host collector, physical-proof tooling and durable-retention tooling do not authorize T01 runtime work;",
        "- the current scaffold, catalog lock, generated bindings, dependency graph, backend artifacts, signer proofs, host collector, physical-proof tooling, durable-retention tooling and accepted public licence do not authorize T01 runtime work;\n- Apache-2.0 governs public repository-owned source but does not license private THETECHGUY systems, restricted adapters, customer/device data or trademarks;",
        "ADR consequences",
    )
    return text


def record() -> str:
    return """# Phase 0C-14 — Apache-2.0 owner acceptance

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
"""


def main() -> None:
    if OUT.exists():
        for path in sorted(OUT.rglob("*"), reverse=True):
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                path.rmdir()
    OUT.mkdir(parents=True, exist_ok=True)
    records = [
        write("CURRENT_STATE.md", current_state()),
        write("PROGRESS.md", progress()),
        write(
            "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md",
            adr(),
        ),
        write("work-packages/PHASE-0C-14-APACHE-2.0-OWNER-ACCEPTANCE.md", record()),
    ]
    manifest = {
        "schema_version": "0.1.0",
        "record_type": "ptah.phase0c.roadmap_licence_acceptance_sync",
        "source_commit": "d9f65fa5c56e3ec3fd608358c3146cac6ed9eaa5",
        "ptah_space_candidate_merge": "bf846574df65061bd99d9c0e3d22a401bf9f27e2",
        "ptah_space_acceptance_head": "a47d418243af076b49367c4c4eccc8ef2090894c",
        "ptah_space_acceptance_merge": "3ce7d4251db0b6ba3f145385ad7ad8dc09276393",
        "runtime_implementation_authorized": False,
        "files": records,
    }
    write("sync-manifest.json", json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
