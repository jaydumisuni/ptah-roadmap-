# Donor Record — xterm.js

**Phase:** 0A / WP09  
**Status:** FIRST-PASS COMPLETE — PRIMARY BROWSER TERMINAL-RENDERER CANDIDATE  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/xtermjs/xterm.js
- Default branch: `master`
- Pinned commit: `ce2169485677951c7701129516cbb68e01330d86`
- Licence: MIT
- Activity: Active
- Classification: browser terminal emulator and addon platform donor
- Ptah targets: multi-terminal panels, PTY stream rendering, search, links, WebGL/canvas rendering, fit/resize, accessibility and terminal reconnection views

## Files/components inspected

- `README.md`
- `LICENSE`
- documented terminal-core and official-addon boundaries
- security warning and data-transport separation

## Verified capabilities and patterns

- Implements a full browser terminal emulator used by VS Code and other major products.
- Renders terminal output but intentionally does not provide shell or PTY process execution itself.
- Applications connect it to a server-side PTY through their own transport, commonly WebSocket.
- Supports official addons for fit/resize, search, web links, Unicode, clipboard, image handling, WebGL and other capabilities.
- Can render through DOM/canvas/WebGL-related paths depending on configuration/addons.
- Supports themes, selection, input, resize and terminal buffer state.
- Warns that terminal input/output is effectively user-controlled and can create XSS or dangerous link behavior if an application does not sanitize surrounding integration.
- Treats links and optional features as separate addons rather than inseparable terminal authority.

## What xterm.js completes

- The mature browser terminal surface Ptah should not rebuild.
- Many simultaneous terminal panels over Ptah PTY streams.
- Search, selection, links, clipboard, fit/resize and accelerated rendering patterns.
- A clear separation between browser rendering and server-side PTY/process supervision.
- A widely tested terminal behavior baseline across modern browsers.
- Addon-based feature composition and graceful capability differences.

## Important limitations for Ptah

- xterm.js is a renderer, not a shell, process supervisor, terminal Session or Activity Ledger.
- Terminal buffer contents are not durable process state or complete audit evidence.
- Input acknowledgement does not prove the shell/process accepted or completed a command.
- Terminal output may contain secrets, personal data, control sequences and hostile content.
- Link handling can open untrusted URLs.
- Clipboard access is sensitive and browser-dependent.
- Search/render buffers may be truncated and cannot replace retained logs/Artifacts.
- WebGL/image addons increase resource use and browser compatibility requirements.
- One xterm instance is not automatically isolated from another if application transports or IDs are wrong.
- Terminal resize changes PTY geometry and can affect running full-screen programs.

## Must not be inherited

- xterm instance IDs as canonical Ptah terminal/PTY identities;
- browser buffer used as the only terminal log or replay store;
- terminal input exposed without PTY Session ownership/focus rules;
- automatic opening of untrusted terminal links;
- clipboard read/write enabled under generic terminal-view permission;
- UI reload interpreted as PTY/process restart or recovery;
- raw terminal HTML/escape content injected into surrounding DOM;
- unlimited scrollback retained without privacy/resource policy.

## Integration decision

**ADOPT XTERM.JS AS THE PRIMARY BROWSER TERMINAL RENDERER OVER PTAH'S PROCESS/PTY FACILITY.**

Ptah owns:

- PTY Activity and terminal Session identity;
- process lifecycle;
- byte-stream sequencing and replay cursor;
- input focus/control lease;
- resize operations;
- retained logs and evidence;
- privacy/redaction;
- reconnect and stale-stream handling.

xterm.js renders one subscribed terminal stream and sends scoped user input.

## Native Ptah gap

Ptah must define:

- terminal Panel to PTY Session mapping;
- stream ID, sequence, replay cursor and backend generation;
- input-owner/focus lease shared between human and automation;
- resize and geometry receipts;
- scrollback/log retention and redaction classes;
- link, clipboard, image and addon capability scopes;
- terminal closed/recovering/disconnected states;
- mobile keyboard and touch behavior;
- accessible screen-reader mode and reduced-motion settings;
- rendering/resource limits for many concurrent terminals;
- backend/renderer replacement path.

## Exit strategy

Ptah's PTY/terminal contracts remain independent. xterm.js may be replaced by a native terminal view or another browser renderer without changing terminal Session, Activity or stream identity.

## Validation required

1. Render many independent PTY Sessions concurrently without stream/input cross-talk.
2. Disconnect/reconnect a terminal panel and replay from a cursor without duplicating output.
3. Enforce human/automation input ownership and reject stale input tokens.
4. Resize a terminal and verify PTY geometry separately from UI pixel size.
5. Retain logs as protected Artifacts independently of browser scrollback.
6. Reject or confirm untrusted links and scope clipboard access.
7. Stress WebGL/canvas/DOM renderers under resource pressure and degrade honestly.
8. Use desktop and mobile keyboard/touch input without losing command/control identity.
9. Replace xterm.js for one client without changing PTY Session identity.
