# D058 — Strix Archive Record

Outcome: ACCEPTED FOR ARCHIVE WITH OFFENSIVE-SECURITY RESTRICTIONS — authorized isolated workload only

Campaign: `CAMPAIGN-001`

Formation: `AF01`

Primary Archivist: `AF01-P10`

Independent Verifier: `AF01-V10`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `usestrix/strix`;
- owner: Strix organization;
- visibility: public;
- archived: false;
- default branch: `main`;
- inspected commit: `48b4821f6960f38a289118a5c17b7e88e3a168b2`;
- inspected package/release state: `strix-agent` version `1.2.0`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root licence: Apache License 2.0;
- licence evidence: `LICENSE` blob `65c4e8f58a00552cc29f6bd1dcaf1c4ef10012b8`;
- package metadata declares Apache-2.0;
- scanners, exploit tools, browser/proxy/runtime images, generated reports/patches and external provider terms require separate review;
- activity state: active; inspected head releases version `1.2.0`.

## Primary evidence packet — AF01-P10

Inspected:

- `README.md` blob `2122d04b4ffb1ad519e4d846d7c0e6fd8b0ecc3d`;
- `pyproject.toml` blob `fb0257dd3a6c52ce12a3f6f89b13e556a7fefa7e`;
- root `LICENSE`;
- exact current head.

Verified:

- Strix is an agentic penetration-testing CLI/platform with reconnaissance, exploitation, proof-of-concept validation, reporting and proposed remediation/autofix features;
- local use requires Docker plus an LLM provider/API key;
- first run pulls a sandbox image and writes scan evidence to `strix_runs/`;
- package entry point is `strix.interface.main:main`;
- dependencies include OpenAI Agents/LiteLLM, Docker, Caido client, cryptography, PDF/report tooling and optional cloud-provider authentication;
- supported use includes source, repository, black-box web, authenticated/grey-box and multi-target testing;
- the tool intentionally exposes browser exploitation, shell/command execution and custom exploit runtime capabilities;
- local viewer binds to loopback with a tokened URL and reads retained run files.

Primary conclusion:

Strix is a useful optional security-stress workload and adversarial proof donor. Its offensive capabilities must run only against explicitly authorized targets in isolated Workspaces with declared scope, credentials, egress, evidence retention and human review. Strix findings and generated patches are evidence/recommendations, not automatic Ptah truth or deployment authority.

## Independent verification packet — AF01-V10

Repeated checks:

- canonical identity, `main` branch and exact inspected head;
- Apache-2.0 root/package licence;
- actual Python package entry point and dependency stack;
- Docker/provider-key requirements;
- offensive browser, shell, exploit and multi-target capabilities;
- local evidence/viewer behavior.

Challenges retained:

- only owned or explicitly authorized targets may be tested;
- credentials and target data are highly sensitive and require strict scope/retention controls;
- working PoCs can be dangerous artifacts and must be access-controlled;
- AI findings, severity scores and patches require independent validation;
- continuous/automated pentesting must not escape an approved target list or network boundary;
- provider APIs and pulled images expand the supply-chain and data-disclosure boundary.

Verifier conclusion: primary findings supported. Frozen classification as an optional workload remains correct with mandatory offensive-security controls.

## Ptah relationship

- frozen donor group: Provenance, artifact integrity and security evidence / security stress workloads;
- current classification: authorized optional workload only;
- requirements supported: adversarial testing, PoC/reproduction evidence, finding/report structure, multi-agent workload stress, CI security-gate ideas;
- prohibited inheritance: autonomous target selection, unrestricted egress/exploitation, findings as automatic truth, generated patches as auto-merge authority, stored credentials/PoCs without policy;
- replacement/exit strategy: preserve provider-neutral Security Assessment Activity/Receipt contracts and allow Strix only through an isolated, scope-enforced adapter/workload.

## Contradiction and supersession

- no canonical-identity contradiction found;
- current version `1.2.0` and active CLI/package source supersede earlier generic descriptions;
- source confirms that Strix is intentionally offensive, so authorization/isolation is a hard boundary rather than an optional recommendation.

## Bounded outcome

`accepted for archive with offensive-security restrictions` does not authorize scanning any target, storing credentials/PoCs, deploying Strix, accepting generated findings or patches, reopening Phase 0A, accepting ADR-0033 or authorizing Ptah runtime implementation.
