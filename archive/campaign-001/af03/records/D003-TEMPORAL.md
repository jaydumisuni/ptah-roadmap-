# D003 — Temporal

Status: candidate record — paired evidence complete

Primary Archivist: `AF03-P05`

Independent Verifier: `AF03-V05`

Inspected: 2026-07-23

## Canonical source identity

- source: `temporalio/temporal`;
- default branch: `main`;
- exact inspected commit: `a813c6193d24b91cce5b929d199e89340d63e2ac`;
- root licence: MIT;
- repository role: Temporal server implementation;
- archived: false.

## Primary evidence packet

Temporal is a durable execution platform whose server runs application Workflows and coordinates retryable operations across intermittent failures. The repository contains the server; language SDKs, CLI, Web UI and samples are separate repositories and products.

Useful Ptah donor concepts include:

- durable workflow state separated from transient client processes;
- retryable Activities with explicit histories;
- recovery from intermittent failures;
- visibility into running and completed workflows;
- separating server execution from language-specific worker code;
- deterministic history/replay concepts for long-running orchestration.

## Independent verification packet

The verifier confirmed:

- the exact repository and inspected commit are public and MIT licensed;
- the README identifies this repository as the Temporal server, while Workflows, Activities and Workers are implemented through separate SDKs;
- Temporal’s Workflow, Activity, task queue, namespace and history identities are backend-specific and cannot replace Ptah’s canonical Workspace, Activity, Operation, Attempt, Event or Receipt identities;
- automatic retries and durable acknowledgements do not independently prove external side effects occurred exactly once;
- Temporal Cloud, SDKs, UI, CLI, persistence stores and deployment charts are separate dependencies, services and trust surfaces.

## Contradiction and supersession

The donor pool treated Temporal as a Tier A runtime donor. Current evidence supports studying its durable-orchestration patterns, but not adopting Temporal’s world model as Ptah Core or assuming that backend durability satisfies Ptah’s independent post-condition and external-effect evidence requirements.

No frozen Ptah lifecycle or identity decision is superseded. Temporal could only appear as an optional Provider or orchestration adapter behind Ptah-owned identities and evidence.

## Bounded outcome

`accepted_for_archive_durable_execution_donor_with_identity_and_effect_boundaries`

Allowed reuse:

- study or potentially integrate MIT-licensed durable execution patterns behind a replaceable Provider boundary;
- retain exact server, SDK, worker, namespace, task-queue and persistence identities as backend evidence;
- use workflow history and retries as inputs to Ptah recovery and observability evidence.

Restrictions:

- preserve MIT notices and separately review every SDK, CLI, UI, persistence and deployment dependency;
- do not map Temporal Workflow or Activity IDs directly onto canonical Ptah identities;
- do not treat retry completion, workflow success or server acknowledgement as independent proof of external side effects;
- do not make Temporal Ptah’s global scheduler, approval system, authority model or mandatory runtime;
- do not infer Temporal Cloud rights or behavior from the public server repository.

This outcome does not authorize implementation.