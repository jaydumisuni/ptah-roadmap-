# WP09 Migration and Compatibility Record

**Status:** CANDIDATE  
**Date:** 2026-07-19

WP09 migration imports or replaces desktop applications, browser profiles, automation backends, remote-display systems and human workspace shells without changing canonical Ptah identity or manufacturing recovery/action proof.

## Import boundary

Existing executables, packages, desktop entries, application registrations, browser binaries/profiles, cookies/storage exports, automation traces, screenshots, recordings, remote-display sessions, selectors, scripts and UI layouts enter Ptah as exact WP03 Objects/Object Revisions plus scoped Aliases, observations and proposals.

Import never grants:

- canonical Application, Browser, Page, semantic Target or Shell Panel identity from a path/handle/backend ID;
- exact compatibility or execution authority;
- functional recovery from profile/checkpoint bytes;
- successful UI action from backend acknowledgement;
- public export authority for cookies, credentials, clipboard, text, screenshots or traces.

## Directional migration sequence

1. Register exact binaries, packages, profile/checkpoint data, scripts and evidence as WP03 Objects with qualified digests, origin, audience and privacy.
2. Preserve executable paths, bundle/package IDs, PIDs, window handles, browser target/session IDs, element handles and panel IDs as scoped Aliases.
3. Create stable Application, Browser Binary/Profile, Shell Panel Type/Profile and other logical identities.
4. Create immutable Revisions and explicit Compatibility decisions.
5. Require new Installation, Session, Process, Context, Page, semantic Context and Shell Session records bound to exact Provider/generation and WP02 execution.
6. Convert legacy browser page/tab relationships to Page/Frame/Popup/Navigation records without using backend handle identity.
7. Convert legacy selectors/scripts to immutable Selector/Target/Action proposals; resolve fresh Target Results before any mutation.
8. Register screenshots, traces, logs, downloads and recordings as Objects/Artifacts and evidence records with privacy/redaction metadata.
9. Rebuild Shell layouts as immutable Layout Revisions plus responsive projections; client/window geometry never becomes runtime truth.
10. Preserve failed, blocked, ambiguous, stale, challenged and inconclusive history.

## Application migration

A legacy installed application migrates to:

- stable Application and immutable Application Revision;
- target-specific Compatibility;
- Installation with exact Provider/materialization/runtime context;
- optional Application Session/Window/Display only when live evidence exists.

A discovered executable or package does not imply installed or runnable state. A visible Window does not imply application readiness. Legacy “restored” sessions migrate no higher than the proven checkpoint, display or functional-recovery level.

## Browser migration

- Browser binary/version/install information becomes Binary and Binary Revision.
- Persistent profile bytes become Profile Revision under privacy/encryption/retention policy.
- Active browser instances become Process/Context/Page only with exact generation and execution correlation.
- Cookies/storage/authentication state are protected content; imported presence does not prove current authentication validity.
- Tab/window/popup backend IDs remain Aliases and relationships.
- Download bytes migrate through WP06 Transfer and WP03 Content/Object verification.
- Challenge/captcha/MFA/consent history remains separate from Page lifecycle and identity-provider authority.

## Semantic UI migration

Legacy selectors, element handles and recorded actions migrate as follows:

- selector text/queries → immutable `semantic.selector`;
- intended element/query → `semantic.target`;
- historical handle/match → expired or historical `semantic.target_result` bound to its original Snapshot/generation;
- requested effect → `semantic.action`;
- each provider invocation → `semantic.action_attempt` linked to exact WP02 Attempt;
- verified post-condition → `semantic.action_result`;
- screenshots/diffs → `semantic.visual_evidence`.

A backend “element found” or “click succeeded” log cannot migrate to current Target Result or verified Action Result without exact current context and post-condition evidence.

## Shell migration

Legacy saved UI/window layouts migrate to:

- stable Layout Profile;
- immutable Layout Revision;
- Panel Type, Panel Binding and View State;
- responsive projections generated per surface/viewport.

They do not migrate runtime state, Processes, Activities or control authority. Human/automation control state maps to canonical `runtime.lease` and `shell.control_transfer`; ambiguous ownership blocks mutation.

## Backend replacement

Replacing Playwright/CDP/WebDriver/Appium/accessibility/remote-desktop/editor/shell/UI framework or native application backend must:

- preserve stable Application, Browser Binary/Profile, Selector/Target, Panel Type/Layout and Object identity;
- create new Compatibility decisions, Provider instances/generations, Processes, Sessions, Contexts, Pages, semantic Contexts/Snapshots and Attempts;
- invalidate old backend handles, Target Results, connection epochs and fences;
- preserve checkpoint/evidence/history and run new Recovery Verification;
- never rewrite failed, challenged, stale or ambiguous outcomes.

## Schema and lifecycle evolution

Breaking changes require explicit:

- source/target schema versions and field mappings;
- lifecycle-state and transition mappings;
- authority, generation, privacy and proof preservation;
- unmapped behavior of reject, preserve-without-interpretation or manual review;
- fixture-backed migration tests;
- no silent promotion of installed→verified, visible→ready, ACK→action success, checkpoint→recovered or projection→runtime truth.

## Exit strategy

No public WP09 contract depends on one UI toolkit, browser protocol, remote-display stack or shell framework. Adapters may be replaced while Ptah retains stable identity, Revisions, Profile/Object content, layout history, evidence, Receipts and migration Aliases.
