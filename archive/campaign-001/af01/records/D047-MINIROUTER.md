# D047 — MiniRouter Archive Record

Outcome: BLOCKED FOR SOURCE REUSE — evidence retained; routing/evaluation study may continue without code adoption

Campaign: `CAMPAIGN-001`

Formation: `AF01`

Primary Archivist: `AF01-P08`

Independent Verifier: `AF01-V08`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `mini-router/minirouter`;
- owner: MiniRouter organization;
- visibility: public;
- archived: false;
- default branch: `main`;
- inspected commit: `6b283fed773556eb034f052a17dc0f3318f0a76b`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root `LICENSE`: not present at the inspected commit;
- `pyproject.toml` does not declare a licence field;
- README states the repository was adapted from `harrrshall/tinyrouter` and rebuilt around TRINITY-related routing work;
- source reuse remains blocked until the repository and adapted-source rights are explicitly resolved;
- model, benchmark, API-provider, generated result and competition-submission rights require separate review;
- activity state: active; inspected head merges current development work.

## Primary evidence packet — AF01-P08

Inspected:

- `README.md` blob `25413b9d0e4914dfc2a1c366c2d4a9dcf08d3c29`;
- `pyproject.toml` blob `396fb8fd0f3b979e21cc626b13b544c5c92a38af`;
- attempted root `LICENSE` retrieval at the exact commit: `404 Not Found`;
- exact current head.

Verified:

- MiniRouter is an SN74/Gittensor competition workspace for learning which model and role should answer each query;
- the documented implementation uses a frozen 0.6B encoder, a small routing head, derivative-free CMA-ES training, model-role selection and multi-turn verifier termination;
- repository includes training/evaluation/routing code, benchmarks, configs, experiments, submissions, a Postgres-backed validator and a web leaderboard;
- evaluation includes held-out comparisons, random/best-single baselines and an oracle-ceiling diagnostic;
- the README explicitly retains inconclusive/negative findings rather than claiming every routing modification wins;
- runtime depends on expensive GPU/API/model infrastructure and competition-specific state.

Primary conclusion:

MiniRouter is valuable as a routing/evaluation research donor and optional future workload. The repository cannot be used as a source dependency or copied/adapted while its root and adapted-source licensing remain unresolved.

## Independent verification packet — AF01-V08

Repeated checks:

- canonical repository identity and `main` branch;
- exact current head;
- root `LICENSE` absence;
- package metadata has dependencies and build configuration but no licence declaration;
- TinyRouter adaptation lineage is stated by the repository;
- current evidence contains measured limitations and inconclusive results.

Challenges retained:

- public visibility is not a licence grant;
- a missing root licence blocks copying, modification and distribution by default;
- model/API/benchmark result rights are separate from repository-code rights;
- competition reward/evaluation state is not Ptah routing truth;
- router performance is pool/task/distribution dependent and cannot justify global authority;
- verifier-agent naming does not give the model or component Ptah review authority.

Verifier conclusion: primary findings supported. Frozen donor register's source-reuse block remains correct and is now backed by exact-current evidence.

## Ptah relationship

- frozen donor group: Distributed placement / experimental routing;
- current classification: future routing/evaluation workload and research source only;
- requirements supported: model-pool evaluation, routing head experiments, oracle-ceiling diagnostics, baseline comparison and negative-result retention;
- prohibited inheritance: source code while unlicensed, competition identity as Ptah identity, router as global scheduler/reasoning/security authority, benchmark score as universal quality truth;
- replacement/exit strategy: reimplement only independently derived, rights-cleared ideas behind Ptah evaluation contracts, or wait for explicit compatible licensing.

## Reopening criteria

Source reuse may be reconsidered only when:

1. the repository adds an explicit compatible root licence;
2. adapted TinyRouter/TRINITY implementation lineage and rights are documented;
3. component/model/benchmark rights are reviewed;
4. exact pinned source passes security and reproducibility review;
5. the work remains a bounded optional workload rather than Ptah authority.

## Bounded outcome

`blocked for source reuse` is a completed archive outcome, not an unresolved archive record. The evidence may be studied and retained, but code reuse/dependency/adaptation is prohibited. This does not reopen Phase 0A, accept ADR-0033 or authorize Ptah runtime implementation.
