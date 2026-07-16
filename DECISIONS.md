# Ptah Accepted Decisions

This file records decisions that must not be silently reversed during implementation.

---

## D-001 — Ptah is independent

**Status:** ACCEPTED

Ptah Space is an independent open-source project. It is not publicly owned by or branded around any private system that uses it.

Private consumers may integrate through neutral APIs, SDKs, CLI, MCP adapters, event streams, files, and facility contracts.

---

## D-002 — Ptah is the world, not the thinker

**Status:** ACCEPTED

Ptah provides workspaces, tools, files, applications, storage, internet, execution, rendering, devices, and artifacts.

The user or calling system provides intent, reasoning, priorities, instructions, restrictions, and acceptance criteria.

Ptah does not contain a universal reasoning council, engineering authority, or product-approval system.

---

## D-003 — Roadmap and implementation are separate

**Status:** ACCEPTED

- `ptah-roadmap-` is the private canonical plan, progress ledger, donor register, decisions, and recovery memory.
- `Ptah-space` is the public implementation repository.

The public repository contains what is being built and public-safe earned progress. It must not contain the full private roadmap or private integration relationships.

---

## D-004 — Online first, local later, same contracts

**Status:** ACCEPTED

Ptah begins as an online workspace before the permanent mini-PC environment exists.

The future local node and larger operating environment must reuse the same objects, activities, sessions, facility contracts, storage identities, and APIs rather than replacing the online system.

---

## D-005 — Workspace and activity are different

**Status:** ACCEPTED

A workspace is persistent. Activities start, stop, fail, pause, recover, and complete inside it.

One workspace must support many simultaneous terminals, downloads, builds, browsers, media jobs, decomposition jobs, applications, and services.

---

## D-006 — Object-first architecture

**Status:** ACCEPTED

Files are registered objects with hashes, types, metadata, storage locations, provenance, parent/child relationships, derivatives, views, and producing activities.

Original objects remain preserved unless explicitly replaced.

---

## D-007 — Domain packs

**Status:** ACCEPTED

Decomposition and runtime support are extended through domain packs with a shared contract:

- detect;
- inventory;
- decompose;
- preview;
- open/mount;
- transform;
- validate;
- compare;
- rebuild where supported;
- execute through an appropriate runtime.

Firmware and disks/filesystems are first-class domain packs.

---

## D-008 — Internet is normally available

**Status:** ACCEPTED

Ptah behaves like a capable operating environment: Git, package registries, websites, APIs, downloads, browser sessions, and remote services work normally.

Restrictions originate from the user, caller, explicit workspace configuration, or hosting environment. Ptah does not autonomously decide what the programmer may access.

---

## D-009 — Storage is layered

**Status:** ACCEPTED

- Fast local storage performs active work.
- Object storage retains durable remotely available bytes.
- Git owns source history.
- SQL/metadata stores catalogue objects, activities, sessions, nodes, and artifacts.
- Google Drive is an export and readable recovery destination, not an active build filesystem.

---

## D-010 — Integration first, not greenfield pride

**Status:** ACCEPTED

Every facility begins with recovery of:

1. existing internal work;
2. external donor projects;
3. mature upstream machinery;
4. the remaining native Ptah gap.

Repositories are classified as adopt, adapt, wrap, fork, protocol-compatible, study-only, hosted workload, reject, or further inspection.

No donor is selected from README claims alone.

---

## D-011 — Polyglot operational chassis

**Status:** ACCEPTED

Rust is preferred for long-running Ptah core and node services where it improves performance, reliability, and portability.

Mature tools may remain in Go, Python, TypeScript, Java, C/C++, Kotlin, or other appropriate languages behind stable adapters.

---

## D-012 — Evidence before completion

**Status:** ACCEPTED

Source presence is not proof of capability.

Each phase has explicit gates, frozen checkpoints, live proof, artifacts, logs, hashes, and known limitations.

Negative, blocked, and partial outcomes remain recorded as evidence.

---

## D-013 — No work before placement and approval

**Status:** ACCEPTED

A useful idea is preserved, but it is not automatically active work.

Before implementation it must be:

- placed in the roadmap;
- assigned to a phase;
- checked against existing work;
- dependency-ordered;
- selected in `CURRENT_STATE.md`;
- approved for build.

---

## D-014 — Build cycle

**Status:** ACCEPTED

Every work item follows:

1. Understand
2. Build
3. Review
4. Freeze
5. Prove
6. Submit / Ship

Runtime experiments may confirm a design but must not replace understanding and architecture recovery.

---

## D-015 — Ptah public repo remains neutral

**Status:** ACCEPTED

Public documentation may describe humans, applications, agents, automation clients, IDEs, generic external systems, and execution nodes.

It must not expose private operation chains, private consumers, credentials, private deployment topology, customer data, or unpublished company decisions.

---

## D-016 — Operating-system assembly is a later private lane

**Status:** ACCEPTED

Ptah remains OS-neutral and independently useful.

A future local operating environment may package Ptah, but the distribution, boot, drivers, updates, hardware profiles, and private integrations are decided separately after the online and node services are proven.
