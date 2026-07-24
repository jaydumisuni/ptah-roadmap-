# P01 / ADR-0033 physical-host proof candidate selection

Status: provisional, non-authorizing — P01 paused pending Phase 0C-19 / ADR-0037 planning-load acceptance

Recorded: 2026-07-24

## Purpose

Complete Step 2 of `planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md` by selecting one exact clean reviewed `Ptah-space` preparation commit before physical-host collection.

This record does not accept P01, accept ADR-0033 or authorize runtime implementation.

## Selected implementation-preparation commit

Repository:

```text
jaydumisuni/Ptah-space
```

Selected exact commit:

```text
23dc4b19a0189ba55e08dfa124761efa806bd68b
```

Commit purpose:

```text
Deepen the observable Workspace donor study
```

The selected commit contains the accepted Phase 0C preparation stack and non-operative Workspace donor supplements. It does not contain or claim a Node, Workspace, Activity, Provider, Browser, transfer, repair or user-interface runtime.

The immediately preceding PR candidate was exact head:

```text
bf4ae98b9d492ad688644fd6a330aaf435ac70c1
```

The complete PR matrix reached eleven passing exact-head workflows. The deep Workspace study run was `30087967851`, retained artifact `8594496859`, artifact digest `sha256:aea4fde3f600a6e4c3fc2f6ff3614918a5f714c6f8ebbf6ab3fb3cb29ccaf12b`, with 26 valid/adversarial cases passing. PR `#16` then merged as the selected commit above.

## Phase 0C-19 sequencing correction

The exact commit below was selected before the complete deep Workspace study was reconciled into the private Master Plan and roadmap. It remains technically suitable and non-runtime, but it is provisional.

Do not run physical-host collection until ADR-0037 accepts Phase 0C-19 and a reviewed change confirms this commit or selects a newer non-runtime preparation commit.

## Required proof-host identity

The collection machine must report exactly:

```text
Ubuntu Server 24.04.4 LTS
x86_64
6.8.0-136-generic
```

It must also satisfy every requirement in `Ptah-space/host/capability-profile.json`, preserve complete local APT metadata for every installed package and keep one clean unchanged checkout at the selected commit before and after collection and retention.

A generic CI runner, different point release, cloud kernel, dirty checkout or incomplete package-artifact evidence is diagnostic only.

## Exact collection procedure

On the physical proof host:

```bash
git clone https://github.com/jaydumisuni/Ptah-space.git
cd Ptah-space
git checkout 23dc4b19a0189ba55e08dfa124761efa806bd68b
test -z "$(git status --porcelain)"
rm -rf evidence/phase0c/pinned-host-candidate \
       evidence/phase0c/pinned-host-durable-candidate

python3 tools/run_pinned_host_proof.py \
  --repo-root . \
  --output evidence/phase0c/pinned-host-candidate
```

Collection may be considered proof-eligible only when `bundle-manifest.json` records:

- `proof_eligible: true`;
- empty `eligibility_failures`;
- empty `host_identity_failures`;
- empty `capability_failures`;
- empty `package_artifact_failures`;
- complete installed-package to package-artifact identity coverage;
- present APT release and package-index evidence;
- clean unchanged selected Git commit.

Then run, from the same exact checkout:

```bash
python3 tools/retain_verified_pinned_host_evidence.py \
  --repo-root . \
  --bundle-dir evidence/phase0c/pinned-host-candidate \
  --output-dir evidence/phase0c/pinned-host-durable-candidate
```

## Required returned evidence

Source candidate:

- `host-identity.json`;
- `host-capabilities.json`;
- `installed-packages.json`;
- `package-artifacts.json`;
- `apt-sources.json`;
- `bundle-manifest.json`.

Durable candidate:

- `durable-pinned-host-bundle.json`;
- `pinned-host-review-record.json`;
- `repository-binding.json`;
- `README.md`.

The generated review record must remain pending with all acceptance and authorization fields false until independent package, artifact, retention and Phase 0C closure review.

## Remaining P01 closure sequence

```text
run exact physical-host proof
→ independently verify and durably retain exact bytes
→ commit the durable candidate
→ review and accept host/package/artifact/retention evidence
→ complete Phase 0C consistency review
→ accept ADR-0033
→ set Runtime implementation: AUTHORIZED in the same reviewed closure merge
→ mark P01 complete and A01 ready
```

## Hard boundary

```text
P01: PAUSED / provisional proof candidate
ADR-0033: PROPOSED
Runtime implementation: NOT AUTHORIZED
```

Owner intent, donor completion, archive completion or CI success cannot replace the missing physical-host evidence.