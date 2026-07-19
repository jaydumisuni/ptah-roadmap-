# Phase 0B WP09 — Application, Browser, Semantic UI and Shell

**Status:** CANDIDATE BLUEPRINT
**Implementation authorization:** NONE

## Boundary

WP09 defines recoverable human/application interaction without selecting Playwright, Appium, scrcpy, a desktop shell or remote-display backend.

## Required entities

- Application, immutable Application Revision and compatibility;
- Application Installation, Instance and Session;
- Browser Profile, Context, Page/Tab and Browser Session;
- Display Stream, Input Stream, Clipboard Channel, Recording and Log Stream;
- Semantic UI Snapshot, Element Observation, Screen Context and Action Request/Result;
- Shell Workspace View, Panel, Attachment and layout revision;
- remote display endpoint and transport evidence;
- automation Protocol/Run separated from physical Actions/Attempts;
- recovery, reconnect, stale UI and uncertain input outcomes.

## Non-negotiable separations

1. Application identity is not process ID, package path or window handle.
2. Browser Profile, Context, Page and client panel remain separate.
3. Pixels, semantic hierarchy and caller interpretation are different evidence domains.
4. A requested click/type/scroll is not successful until exact target and post-condition evidence exist.
5. Display delivery is not application health or semantic correctness.
6. Closing a client attachment does not terminate the underlying Session.
7. Shell layout is a View, never canonical Workspace state.
8. Credentials/cookies remain referenced, scoped and redacted.
9. Browser/application backend replacement preserves public identities and history.

## Proof cases

- multiple browser contexts and application Sessions run concurrently;
- stale semantic snapshots cannot authorize state-changing input;
- ambiguous target selection is rejected or requires caller disambiguation;
- disconnect/reconnect preserves Session identity while advancing transport generation;
- input acknowledgement without observed post-condition is inconclusive;
- client closure does not destroy active work;
- private profile state is excluded from public exports;
- replacement backend produces new compatibility and transport evidence without identity loss.

## Outputs

Conventions, entity kinds, schemas/catalog, lifecycle machines, migration, fixtures, safety net, package record and ADR-0026.
