# D048 — Ray Archive Record

Outcome: ACCEPTED FOR ARCHIVE WITH DISTRIBUTED-AUTHORITY RESTRICTIONS — optional compute/scheduling donor only

Campaign: `CAMPAIGN-001`

Formation: `AF02`

Primary Archivist: `AF02-P10`

Independent Verifier: `AF02-V10`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `ray-project/ray`;
- owner: Ray Project organization;
- visibility: public;
- archived: false;
- default branch: `master`;
- inspected commit: `eae2ad02ebdd1b9698e1613f4ef3f683e4e8ebbb`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root licence: Apache License 2.0;
- licence evidence: `LICENSE` blob `c247a8575b35eea321f584a57a67cfa93db6d654`;
- Python wheels, native libraries, dashboards, Kubernetes integrations, models/datasets, community integrations and cloud services retain separate dependencies and operational terms;
- Anyscale is a separate commercial service boundary;
- activity state: active; inspected head repairs a pinned xz/LZMA source download while retaining the exact SHA-256.

## Primary evidence packet — AF02-P10

Inspected:

- `README.rst` blob `978e713e61f916c19320022fcb318ecca216c064`;
- root `LICENSE`;
- exact current commit and Bazel dependency diff;
- current framework/library scope and cluster abstractions.

Verified:

- Ray provides a distributed runtime plus Data, Train, Tune, RLlib and Serve libraries;
- Ray Core exposes tasks, actors and immutable distributed objects;
- it scales Python/AI applications from one machine to clusters/cloud/Kubernetes;
- dashboard and distributed-debugging features exist as operational surfaces;
- nightly wheels and many community integrations expand the supply-chain boundary;
- the inspected head demonstrates real build reproducibility maintenance: dead pinned mirrors were replaced by a redirector/project fallback while the source archive SHA-256 remained unchanged;
- broad “general-purpose” claims do not remove workload-specific resource, failure, scheduling and determinism constraints.

Primary conclusion:

Ray is a valuable distributed execution, actor, object-store and evaluation workload donor. It must not become Ptah's global scheduler, canonical Object/Activity identity or proof authority. Any use requires a bounded provider adapter and explicit recovery, cancellation, quota, placement and evidence semantics.

## Independent verification packet — AF02-V10

Repeated checks:

- canonical identity, `master` branch and exact current head;
- Apache-2.0 root licence;
- tasks/actors/objects and AI-library scope;
- multi-machine/cloud/Kubernetes deployment claims;
- exact pinned dependency hash retained while mirrors changed;
- community/commercial boundaries.

Challenges retained:

- Ray object IDs and actor/task state are runtime implementation details, not canonical Ptah identities;
- cluster scheduling and retry semantics may duplicate or conflict with Ptah Activity authority;
- distributed execution increases network, credential, deserialization and multi-tenant risk;
- dashboard/cluster control surfaces require strict authentication and exposure policy;
- package/native dependency graph is large and exact wheel/build provenance matters;
- successful task completion does not prove semantic result correctness or durable recovery.

Verifier conclusion: primary findings supported. Ray is an optional compute backend/workload, never Ptah's command authority.

## Ptah relationship

- frozen donor group: routing, scheduling and evaluation donors;
- current classification: optional distributed compute provider and stress/evaluation workload;
- requirements supported: tasks, actors, distributed object movement, placement/scaling, ML workloads, serving and distributed-debugging patterns;
- prohibited inheritance: Ray task/actor/object IDs as Ptah identity, Ray scheduler as global authority, implicit retries as unreceipted truth, cluster dashboard as unrestricted control surface;
- replacement/exit strategy: preserve native Ptah Activity/Object/Receipt contracts and isolate Ray behind provider adapters with deterministic handoff/recovery rules.

## Contradiction and supersession

- no canonical-identity contradiction found;
- current source confirms Ray combines a core runtime with a broad and independently changing AI-library ecosystem;
- the inspected build fix demonstrates why mirror URLs and source digests must be recorded separately;
- frozen Ptah scheduling/placement architecture remains unchanged.

## Bounded outcome

`accepted for archive with distributed-authority restrictions` does not select Ray, authorize cluster deployment, accept its scheduler/object store as Ptah authority, reopen Phase 0A, start AF03, accept ADR-0033 or authorize Ptah runtime implementation.
