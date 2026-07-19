# WP09 Cross-Machine Invariants

**Status:** CANDIDATE  
**Date:** 2026-07-19

These invariants compose the Application, Browser, semantic UI and human Shell records with WP01–WP08. No UI, process, backend handle or projection may replace canonical runtime or object truth.

1. Application, immutable Application Revision, Compatibility, Installation, Session, runtime Process, Window, Window Observation, Display Session, Display Observation, Checkpoint and Recovery Verification remain separately addressable.
2. A path, bundle/package ID, desktop entry, executable name, PID, window handle, display surface ID, browser target ID or backend session ID is a scoped Alias/evidence only.
3. `runtime.process` remains canonical Process identity. Application and Browser records reference it and never introduce a second process identity.
4. Application compatibility is exact, directional, Provider/generation/platform/isolation/permission specific and expiring. Installed presence does not prove launch, display, semantic or recovery readiness.
5. Installation acknowledgement does not create `installed_verified`; exact installed Revision, files/configuration and launch prerequisites require read-back.
6. Application Session survives Window and Display recreation but not silent Provider-generation replacement. A new runtime generation creates new Process/Window/Display bindings and new verification.
7. Window visible, pixels streaming and application functionally ready are three different claims.
8. Checkpoint bytes/integrity and target compatibility do not prove application recovery. Recovery Verification uses a new generation and functional post-condition read-back.
9. Optional display or semantic loss degrades only the affected capability; it does not automatically terminate a headless/otherwise functional Application Session.
10. Browser Binary, immutable Binary Revision, Profile, Profile Revision, Process, Context, Page, Frame, Popup, Navigation, Download, Challenge, Evidence, Checkpoint and Recovery Verification remain distinct.
11. Profile identity may survive Process/Context/Page generations. Writable sharing requires an exact current `runtime.lease` and fence; mutually untrusted Workspaces never share a writable Profile.
12. Browser Process restart creates a new Process generation and invalidates old Context/Page/Frame backend handles, semantic contexts and control authority.
13. Context isolation, storage mode, network and permission policies are explicit. Incognito/ephemeral/private is not inferred from a backend flag alone.
14. Popup records preserve opener/new-Page relationship; they never replace either Page identity.
15. Each Navigation is immutable and sequence-bound. Same-document and cross-document changes remain explicit; a URL string is not Page or Navigation identity.
16. Download initiation, byte transfer, finalize, Content/Object registration, digest verification, Location and optional Artifact promotion remain separate. Browser “download complete” cannot bypass WP06/WP03 truth.
17. Challenge identity/state pauses only affected Page/Navigation scope. Human completion fences automation input but does not expose secrets or collapse identity-provider authority into Ptah.
18. Browser checkpoint restoration creates new Process/Context/Page generations. Restored cookies/profile bytes do not prove authentication/session validity.
19. Browser Evidence Bundle collects source response, DOM, accessibility, screenshots, traces, network/console logs and downloads without treating any one class as universal truth.
20. Semantic Context, Snapshot, Node Snapshot, Event, Selector, Target, Target Result, Action, Action Attempt, Action Result and Visual Evidence remain distinct.
21. DOM, accessibility, platform UI, visual pixels and application API may disagree. Contradictions are retained and resolved by explicit policy/proof, never overwritten.
22. A Selector is a durable query; a Target Result is a fresh resolution against one exact Context/Snapshot/generation. Backend element handles are Aliases only.
23. Ambiguous, missing, stale, expired or wrong-generation Target Results cannot authorize mutation. Reacquisition is mandatory before action.
24. `runtime.lease` and fencing remain canonical human/automation control authority. No semantic or Shell lease duplicate is introduced.
25. Every Action Attempt binds exact current Context, Snapshot, Target Result, Provider generation, control Lease/fence and a new WP02 Attempt/nonce.
26. Provider/action acknowledgement proves only method dispatch/completion. Action success requires fresh post-condition verification through semantic, visual, application API or authoritative external evidence.
27. Fallback from semantic/API control to keyboard/raw input/coordinates lowers assurance explicitly. Hidden fallback is prohibited.
28. Uncertain action effects are reconciled before retry; retries always use new Target Result where freshness requires it and a new WP02 Attempt.
29. Shell Client, Shell Session, Panel Type, Panel, Panel Binding, Layout Profile, Layout Revision, View State, Projection, Responsive Projection, Client Observation and Control Transfer remain separate.
30. Shell projections, panel state, layout and client cache are presentation truth only. They cannot change Activity, Application, Browser, Device, Object or Workspace canonical state without an authorized operation.
31. Shell disconnect, mobile backgrounding or panel closure does not stop Workspace runtime, Browser Process, Application Session, Transfer or Device operation unless a separate authorized cancellation/stop occurs.
32. Responsive phone/tablet projections derive from immutable Layout Revision and never mutate the desktop/global layout merely because the viewport changed.
33. Control Transfer quiesces/fences the old holder before issuing a new Lease/fence. If control ownership is uncertain, all mutation is blocked.
34. Accessibility, keyboard, touch, text scaling, reduced motion, contrast, RTL, localization, safe areas and low-bandwidth behavior are contract requirements, not visual polish.
35. Profiles, cookies, credentials, clipboard, semantic text/value, screenshots, video, traces, network/console logs and client caches carry explicit audience/privacy/redaction/retention rules.
36. Backend replacement creates new Compatibility, Provider bindings, Processes, Sessions, generations, snapshots and Attempts while preserving stable Application, Browser Binary/Profile, Page relationship history and proof.
37. Negative, blocked, stale, ambiguous, partial, challenged, failed and inconclusive outcomes are immutable evidence and cannot be deleted or rewritten to manufacture success.
