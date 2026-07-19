# Phase 0B WP09 — Application, Browser, Semantic UI and Human Shell Conventions

**Status:** CANDIDATE DRAFT  
**Date:** 2026-07-19  
**Contract family target:** `ptah.application` / `ptah.browser` / `ptah.semantic` / `ptah.shell` `0.1.0`  
**Implementation authorization:** NONE

## Purpose

Define backend-neutral Application runtime, Browser runtime, semantic/visual automation and human Workspace shell contracts without selecting native/OCI/VM runtimes, remote-display gateways, browser services, platform accessibility frameworks, desktop UI frameworks or mobile presentation implementations.

This package composes WP01–WP08 with ADR-0010, ADR-0011, ADR-0012 and ADR-0015.

---

# 1. Required separation

Ptah keeps the following distinct:

```text
Application Object role
Application Revision
Application Installation
Application Compatibility
Application Session
runtime Process
Application Window
Display Session
Application Checkpoint
Application Recovery Verification
Browser Binary
Browser Profile
Browser Process
Browser Context
Browser Page
Browser Frame
Popup relationship
Download
Challenge/Auth state
Browser Checkpoint
Semantic Provider
Semantic Context
Semantic Snapshot
Semantic Node Snapshot
Semantic Target
Semantic Selector
Semantic Event
Semantic Action
Semantic Action Attempt
Semantic Action Result
Visual Evidence
Shell Client
Shell Session
Panel Type
Panel Instance
Panel Binding
Layout Profile
Layout Revision
View State
Activity/Evidence Projection
Control Lease
Control Transfer
```

No window handle, process ID, accessibility object path, browser target ID, tab title, DOM selector, client connection, panel ID, layout restoration or screenshot may collapse these records.

---

# 2. Application identity and installation

## 2.1 Application role

`application.application` is a durable logical role over exact Object/Application revisions. It is not one installation, process, window, package-manager entry, executable path or Provider runtime.

An Application Revision binds exact source/package/executable Objects, version/build/platform/architecture claims, signatures/provenance, dependencies, capabilities and privacy/security requirements.

## 2.2 Installation

An Installation is one exact deployment of one Application Revision into one Provider/environment/Device/Workspace scope.

It records:

- Application and exact Revision;
- Provider/Facility revision and target platform;
- installation root/package-manager/backend aliases;
- exact installed objects/digests;
- configuration and dependency references;
- install/upgrade/repair/uninstall Activities and Receipts;
- health/verification and limitations.

Paths, package names, bundle IDs, registry entries and platform installation IDs remain Aliases.

## 2.3 Compatibility

Application Compatibility is directional and operation-specific. It binds an exact Application Revision to Provider/Node/platform/architecture/isolation/display/input/semantic capability context.

Compatibility may differ for:

```text
install
launch_headless
launch_graphical
remote_display
semantic_inspection
semantic_control
visual_control
checkpoint
restore
```

A binary may launch while semantic automation or checkpoint support is unavailable.

---

# 3. Application Session, Process and Window

Application Session is one running relationship between an Installation/Application Revision and one Provider generation under one Workspace Materialization.

It binds:

- Workspace/Revision/Materialization generation;
- Application/Revision/Installation;
- Provider/Node or remote-service locality/generation;
- Activity/Operation/Attempt;
- Process refs;
- Window refs;
- Display Session refs;
- semantic Context refs;
- control Lease/fence refs;
- checkpoint/recovery refs;
- privacy and evidence policy.

A Session may be active with no visible Window, multiple Processes, multiple Windows or degraded semantic/display capability.

`runtime.process` remains the canonical supervised process entity. OS PID is an Alias under one Provider/Node generation.

A Window is a Provider-scoped incarnation under one Application Session and generation. Native window handles/titles/classes are observations/Aliases. Close/recreate/fullscreen/remote-display remapping can create a new Window generation without changing Application Session identity.

---

# 4. Display Session

Display Session is separate from Application Session and Window identity.

It records:

- display backend/provider revision;
- locality, Node/remote-service generation;
- Application Session and exposed Window/surface refs;
- codec/geometry/orientation/scale/colour-space/input capability;
- authentication/privacy/recording policy;
- stream and client attachments;
- health/quality observations;
- checkpoint/cleanup evidence.

Display availability does not prove Application readiness, semantic availability or input authority.

Remote-display reconnect can restore pixels while the Application remains crashed, restarted or stale.

---

# 5. Application checkpoint and recovery

Application checkpoint is a typed WP05 checkpoint component over one exact Application Session, process/window/display/semantic generation and Provider/runtime format.

Checkpoint creation, integrity, target compatibility, runtime restore and Application Recovery Verification remain separate.

Recovery Verification may include:

- process generation and executable identity;
- Window/surface recreation;
- application protocol/API readiness;
- file/database/network side-effect reconciliation;
- display and semantic reacquisition;
- exact user-visible/functional post-condition.

`restored_runtime`, `window_visible`, `panel_restored` and `application_recovered` are different results.

---

# 6. Browser identity hierarchy

## 6.1 Browser Binary

Browser Binary is exact executable/build identity with platform, architecture, channel, version, signature/provenance and capability evidence.

## 6.2 Browser Profile

Profile is persistent browser storage/policy identity, not a Process or Context. It may contain cookies, local/session storage, history, certificates, extensions, permissions and authentication state.

Profiles have audience/privacy/retention/encryption rules. Shared or concurrent use is explicit and fenced. Mutually untrusted Workspaces do not share one writable Profile.

## 6.3 Browser Process

Browser Process is one running provider incarnation of one Binary, optionally bound to one Profile, under exact Provider/Node generation.

Process crash/restart creates a new Process/generation. Profile identity may persist.

## 6.4 Browser Context

Context is an isolated browsing/storage/network/permission scope inside one Browser Process. Incognito/ephemeral/persistent-partition semantics are explicit.

## 6.5 Page, Frame and Popup

Page is one top-level tab/window identity under one Context and Process generation. Navigation creates Page navigation revisions/events, not necessarily a new Page identity.

Frame is one document frame incarnation under Page/navigation generation. Cross-origin boundaries and accessibility/DOM availability are explicit.

Popup is a relationship/result linking opener Page, opening event/action and new Page. Popup IDs are not Page identity.

---

# 7. Browser downloads, challenges and evidence

Download binds exact initiating Page/Frame/Context/Profile/Process/navigation/action and produced Content/Object/Artifact evidence.

Filename and temporary path are Aliases only. Completion requires bytes, digest, Location and source/provenance evidence.

Challenge/Auth state is explicit:

```text
none
login_required
mfa_required
captcha_or_anti_bot
consent_or_terms
certificate_or_device_approval
human_completion_required
blocked_by_policy
expired
resolved
```

A challenge can pause automation without failing the Browser Process or Page.

Browser evidence classes remain separate:

- source response/body;
- DOM snapshot;
- accessibility snapshot;
- screenshot/video;
- trace/network/console;
- download bytes;
- visible rendered state;
- user/manual completion Receipt.

Pixels, DOM and accessibility trees may disagree and are retained.

---

# 8. Browser checkpoint/recovery

Checkpoint may capture Profile storage, Browser Process/runtime state, Contexts, Pages, navigation state, downloads and challenge state subject to privacy and backend capability.

Profile backup does not imply Process/Page recovery. Page URL/title restoration does not prove DOM/app state or authentication remains valid.

Recovery creates new Process/Context/Page generations where required and reacquires evidence. Stale target IDs, DOM handles, frame IDs and semantic targets are rejected.

---

# 9. Semantic provider and Context

Semantic Provider is a Facility/Provider adapter for platform accessibility or automation APIs, including AT-SPI/libatspi, Windows UI Automation, macOS Accessibility, mobile accessibility/UI automation and browser accessibility trees.

Provider-local object paths, runtime IDs, child indices and handles remain Aliases.

Semantic Context binds exact Application/Browser/Device Session, Window/Page/Screen surface, Provider generation and capability/privacy scope.

Observation permissions remain separate from mutation, clipboard, sensitive text, raw input and cross-application authority.

---

# 10. Semantic Snapshot and Node Snapshot

Snapshot is an immutable captured projection at one time/generation. It records:

- Context and source method;
- root and node count;
- roles, names, descriptions, states, relations, interfaces, attributes and geometry;
- text/value/selection summaries under privacy policy;
- completeness/truncation/errors;
- provider generation/event cursor;
- related screenshot/visual evidence.

Node Snapshot is valid only inside one Snapshot revision. Live provider aliases are not durable Node identity.

Semantic Events can invalidate or prompt targeted refresh, but never replace a fresh Snapshot or durable Activity/Event history.

---

# 11. Selector, Target and reacquisition

Selector is a versioned query/specification using role, name, text, state, relation, interface, attribute, application/window/page ancestry, geometry and optional stable application-provided IDs.

Selector Result/Target records:

- exact Context and Snapshot;
- matched Node refs;
- uniqueness/ambiguity score;
- fallback evidence;
- expiry/generation;
- required reacquisition policy.

Before mutation, Target is reacquired against the current Context/Snapshot/Window/Page/Provider generation. Stale or ambiguous targets are blocked unless policy explicitly requires human selection.

No coordinate, text label, object path, DOM selector or accessibility ID is permanent universal identity.

---

# 12. Semantic and input actions

Action Request states intended effect, preferred methods, target, precondition, authority and required post-condition.

Method classes remain separate:

```text
semantic_interface
application_api
browser_dom_or_protocol
keyboard_shortcut
raw_keyboard
raw_pointer
coordinate_visual
clipboard
mobile_input_bridge
human_completion
```

Action Attempt binds exact Session/Context/Target/generations, control Lease/fence, Provider and WP02 Attempt.

Provider call/ACK proves only method acceptance. Action Result requires post-condition evidence such as:

- fresh semantic Snapshot/state;
- visual screenshot/region comparison;
- application/browser API state;
- file/network/external authoritative result;
- human verification.

Semantic and visual evidence may disagree; both remain.

Fallback to lower-confidence methods is explicit and cannot claim equivalent semantic assurance.

---

# 13. Human Workspace Shell

## 13.1 Shell Client and Session

Shell Client is one presentation implementation/build. Shell Session is one authenticated human presentation relationship to one Workspace, independent of runtime Sessions.

Closing/disconnecting Shell Session does not stop Activities, Application/Browser/Device Sessions or Workspaces unless an explicit operation does so.

## 13.2 Panel Type and Instance

Panel Type is a versioned contribution contract declaring:

- supported entity bindings;
- required Facilities/permissions;
- commands/events;
- privacy/audience;
- desktop/tablet/phone capabilities;
- accessibility/keyboard/touch requirements;
- resource limits and failure behavior.

Panel Instance binds one Panel Type revision to exact entity refs and one Shell Session/layout. Panel state is presentation state, not canonical runtime truth.

Panels call scoped Ptah Facilities; they do not access host/browser/device resources directly.

## 13.3 Layout Profile and Revision

Layout Profile is logical presentation identity. Layout Revision is immutable and records panel placements, groups, sizes, active/hidden state and responsive projections.

Desktop may support docking/multi-panel; tablet uses constrained splits/drawers; phone uses one primary panel plus compact switching/drawers. A phone projection does not mutate desktop layout truth.

View State stores scroll/cursor/filter/selection/zoom and other client-local presentation state separately from Layout and runtime.

---

# 14. Activity Centre and Evidence Explorer

Activity/Evidence projections are permission-filtered Views over canonical Activities, Operations, Attempts, Events, Receipts, Objects, Artifacts, Reviews, Findings and limitations.

UI labels must name exact dimensions:

- lifecycle;
- connectivity/reachability;
- readiness/health;
- proof domain/level;
- review/acceptance;
- degraded/partial/unknown state.

A green badge cannot collapse `completed`, `verified`, `reviewed`, `reproduced` and `accepted`.

Projection lag/staleness is explicit. UI cache cannot update canonical state.

---

# 15. Human/automation control

Control uses a typed scoped `runtime.lease` plus fencing token. Scope can target Application Session, Window, Browser Context/Page, Device Session/Stream or Semantic Context.

Control states include automation-held, human-held, shared-observe-only, transfer-pending, suspended and released.

Control Transfer records requestor, current/new holder, scope, reason, pending operations, fence change, acknowledgement, cleanup and return conditions.

Human takeover fences automation before raw/semantic input. Automation cannot continue with stale target/fence. Return creates a new control generation and is receipted.

Observation may remain shared where policy permits; mutation authority is exclusive unless an explicit safe collaborative mode exists.

---

# 16. Recovery and presentation truth

The following are separate:

```text
Shell client reconnect
Shell Session restore
Layout Revision restore
Panel Instance/View State restore
Application Session restore
Browser Process/Context/Page restore
Display Session restore
Semantic Context reacquisition
Control Lease restoration or regrant
Application/browser functional Recovery Verification
```

A restored layout may show stale/placeholder Panels while runtime recovery continues. Panels display exact lifecycle/proof/limitation and never fabricate live state.

---

# 17. Accessibility and responsive requirements

All Shell/Panel contracts represent:

- keyboard navigation and focus order;
- screen-reader semantics;
- touch target sizing/gestures;
- safe-area/viewport behavior;
- text scaling/zoom;
- reduced motion;
- high contrast/colour-independent status;
- low-bandwidth/low-resource degradation;
- localization and right-to-left readiness;
- error/empty/loading/partial/offline states.

Accessibility support is tested as behavior, not inferred from framework choice.

---

# 18. Privacy and credentials

Browser Profiles, cookies/tokens/storage, Application configuration, clipboard, semantic text, screenshots/video, console/network traces, downloads, Shell history and evidence projections are restricted by default according to Workspace/caller policy.

Raw credentials never enter public schemas, layout state, logs or screenshots. Redaction/secret references and short-lived scoped grants are explicit.

Public export is allowlisted and cannot include authenticated Profiles, private page/session state, sensitive UI text or control credentials without explicit policy.

---

# 19. Provider and UI replacement

Replacing Application Provider, display gateway, Browser engine/service, semantic adapter or Shell framework:

- preserves Application/Browser/Profile/Workspace/Activity/Object identity;
- creates new Provider revisions/generations, Processes/Sessions/Contexts/Pages/Windows/Snapshots;
- fences stale handles/targets/control leases;
- retains old evidence, negative results and layout revisions;
- requires compatibility/conformance comparison before equivalent capability claims;
- never treats UI migration as runtime recovery.

---

# 20. Minimum conformance invariants

1. Application, Revision, Installation, Session, Process, Window and Display Session remain separate.
2. Browser Binary, Profile, Process, Context, Page, Frame and Download remain separate.
3. semantic Context, Snapshot, Node Snapshot, Selector, Target, Action Attempt and Result remain separate.
4. Shell Session, Panel Instance, Layout Revision and View State remain presentation-only.
5. stale Provider/Process/Window/Page/Context/semantic/control generations reject mutation.
6. client/panel/layout restoration cannot imply runtime recovery.
7. Provider ACK cannot complete semantic/input Action without post-condition evidence.
8. semantic/visual/API/external evidence retain disagreement and authority differences.
9. human takeover changes fence before input; stale automation stops.
10. Browser/Profile/Application credentials and sensitive evidence obey privacy/redaction.
11. phone responsive projection never rewrites canonical desktop layout.
12. Provider/framework replacement preserves canonical history and negative evidence.

## No-build boundary

These are candidate contracts only. No Application runtime, VM/native/OCI adapter, remote-display gateway, browser service, accessibility provider, automation backend, Shell framework, Panel implementation or UI asset is authorized by this document.
