# Ptah Current State

**Last updated:** 2026-07-16  
**Overall status:** ACTIVE PLANNING  
**Current phase:** Phase 0A — Internal and external donor recovery  
**Runtime implementation:** NOT STARTED  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

# Recovered position

The Ptah concept and full replacement architecture have been accepted in principle.

Ptah is:

- independent and open source;
- online first;
- a concurrent digital world rather than a reasoning system;
- built around persistent workspaces, objects, activities, facilities, nodes, sessions, and artifacts;
- capable of files, repositories, terminals, browsers, containers, applications, firmware, devices, media, documents, storage, transfer, rendering, and recovery;
- intended to reuse and improve proven internal and external machinery instead of rebuilding everything blindly.

The complete roadmap is stored in `MASTER_ROADMAP.md`.

---

# Active work

## Phase 0A — Donor recovery and requirement closure

Current objective:

> Produce the Ptah Requirement Closure Matrix and complete donor records before selecting implementation dependencies or writing runtime code.

Current donor pool includes:

- internal THETECHGUY repositories and unfinished work;
- OpenClaw organisation projects;
- Daytona, E2B, Coder, OpenHands;
- Temporal and NATS;
- containerd, OCI, BuildKit, Dagger;
- OpenTelemetry;
- Witness, in-toto, Cosign, ORAS;
- Playwright, Playwright MCP, Browser-Use, TurboWebFetch;
- STF, adbkit, Appium, scrcpy, Android platform tools, TouchPilot;
- decomposition, media, document, executable, firmware, filesystem, knowledge, security, and documentation donors listed in `DONOR_RECOVERY.md`.

---

# Accepted repository boundary

## `ptah-roadmap-`

Owns:

- master roadmap;
- current state;
- tickable progress;
- donor research;
- requirement closure;
- private decisions;
- sequencing;
- chat recovery memory;
- future local/OS integration notes.

## `Ptah-space`

Owns:

- public implementation;
- public-safe architecture and contracts needed by contributors;
- the build slice currently being implemented;
- tests, schemas, source, releases, and earned public progress.

The full private roadmap must not be copied into the public Ptah repository.

---

# No-build boundary

No Ptah runtime implementation is currently approved.

Allowed now:

- donor recovery;
- canonical URL and upstream verification;
- licence review;
- exact source-tree inspection;
- requirement closure matrix;
- internal existing-work recovery;
- donor adoption/wrap/adaptation/rejection decisions;
- schema and proof planning after Phase 0A review.

Not allowed yet:

- choosing dependencies from README claims alone;
- copying donor code;
- building a large UI;
- starting the runtime because a donor looks promising;
- replacing existing internal systems without evidence;
- exposing private consumers in the public repository.

---

# Immediate next actions

1. Populate `DONOR_RECOVERY.md` with canonical upstream and fork relationships.
2. Inspect foundation-grade donors in the approved order.
3. Inspect internal repositories against the same requirements.
4. Build the Requirement Closure Matrix.
5. Identify primary, secondary, and exit-strategy donors for every v1 subsystem.
6. Submit Phase 0A findings for review.
7. Only after approval, begin Phase 0B contract and schema design.

---

# Completion evidence for Phase 0A

Phase 0A can move to review only when:

- every v1 requirement has a recorded closure path;
- each selected donor has a pinned version and licence decision;
- exact files/components studied are recorded;
- limitations and non-inheritance boundaries are explicit;
- internal overlap is identified;
- native Ptah gaps are isolated;
- no selected foundation depends on an unresolved or abandoned source without an exit strategy.

---

# Chat continuation instruction

A future chat must read this file first, then `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `MEMORY_PROTOCOL.md`, and `DONOR_RECOVERY.md` before proposing next work.
