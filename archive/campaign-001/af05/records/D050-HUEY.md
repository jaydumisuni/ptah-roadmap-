# D050 — Huey

Status: candidate record — paired evidence complete

Primary Archivist: `AF05-P04`

Independent Verifier: `AF05-V04`

Inspected: 2026-07-23

## Canonical source identity

- source: `coleifer/huey`;
- default branch: `master`;
- exact inspected commit: `358bdc58b1ce671daa65d92a5194d3d153939d6d`;
- root licence: MIT;
- repository role: lightweight Python task queue;
- archived: false.

## Primary evidence packet

Huey demonstrates small-node task queues, delayed and periodic tasks, consumers, retries and simple Redis/file/in-memory storage patterns. It is useful as a compact local queue reference.

## Independent verification packet

The verifier confirmed that in-memory or lightweight storage modes have different durability and concurrency guarantees. Queue state, consumer acknowledgement and result storage are backend evidence only; they cannot replace Ptah Activity, Attempt, Receipt or acceptance.

## Contradiction and supersession

Huey remains an optional small-workload adapter reference rather than a global Ptah scheduler.

## Bounded outcome

`accepted_for_archive_mit_lightweight_task_queue_with_storage_durability_and_identity_boundaries`

Allowed reuse:

- study or adapt lightweight queue, scheduling and worker-consumer patterns;
- consider a Python workload Provider after canonical Ptah runtime substrates exist.

Restrictions:

- preserve MIT notices and review Redis/storage dependencies separately;
- do not infer durable exactly-once execution from queue acknowledgement;
- do not expose Huey IDs as Ptah identities or let worker completion accept results;
- do not make Huey mandatory or use it before runtime authorization.

This outcome does not authorize implementation.