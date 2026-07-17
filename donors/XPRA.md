# Donor Record — Xpra and Xpra HTML5

**Phase:** 0A / WP07B  
**Status:** FIRST-PASS COMPLETE — RECONNECTABLE LINUX APPLICATION/WINDOW DISPLAY BACKEND CANDIDATE  
**Inspected:** 2026-07-17

## Identity

### Xpra server/client

- Canonical URL: https://github.com/Xpra-org/xpra
- Default branch: `master`
- Pinned commit: `333839b098007816006c00e4c2049d480a21249d`
- Licence: GPL-2.0-or-later

### Xpra HTML5 client

- Canonical URL: https://github.com/Xpra-org/xpra-html5
- Default branch: `master`
- Pinned commit: `41af47a87818d75d4ce74a9f5b525bc908280e9b`
- Licence: repository/package licence must be tracked with the Xpra distribution and bundled dependencies

- Classification: reconnectable Linux graphical application, seamless-window and browser-display donor
- Ptah targets: `APP-002`, Application Session, individual windows, full desktops, reconnect, audio, clipboard, recording/evidence and browser access

## Files/components inspected

- Xpra `README.md`
- Xpra `COPYING`
- documented seamless, desktop, shadow, network, authentication and proxy paths
- Xpra HTML5 `README.md`
- HTML5 client connection and proxy configuration model

## Verified capabilities and patterns

- Seamless mode runs individual remote X11 applications and forwards their windows to another machine.
- Clients may disconnect and later reconnect without terminating the applications.
- Desktop mode starts remote desktop sessions; shadow mode accesses an existing desktop.
- The server can expose a built-in HTML5 client through its web server.
- Windows, macOS and Linux native clients are available.
- Xpra forwards audio input/output, clipboard, printers, system tray, notifications, webcams and file/URL actions.
- Network options include SSH, SSL/TLS, HTTP/WebSocket, RFB and other transports.
- Authentication and proxy-server patterns are built in.
- One proxy may front several sessions.
- HTML5 access can expose seamless application windows in a browser rather than only a full framebuffer desktop.
- Display DPI, image depth and network-condition adaptation are first-class concerns.

## What Xpra completes

- A strong Linux-native Application Display backend for individual applications, not merely full desktops.
- Reconnectable graphical sessions with application state preserved by the server.
- Browser delivery without requiring a native client.
- Audio, clipboard, notification, tray and file-transfer requirements that a simple video stream misses.
- A mature distinction among seamless application mode, virtual desktop and shadow-existing-session mode.
- A practical remote-display path for native Linux applications running inside local or OCI Workspace Providers.

## Important limitations for Ptah

- Xpra is primarily built around X11 application/session forwarding; Wayland-native support and exact compositor behavior require current-version proof.
- It provides graphical-session transport, not Ptah Workspace, Application Object, Activity, Window or Session truth.
- A connected Xpra session does not prove that an application launched correctly or reached the intended state.
- Its broad desktop integration exposes sensitive clipboard, files, notifications, webcams, audio and printing surfaces.
- Reconnectable display state is not equivalent to a provider snapshot or complete Ptah Session checkpoint.
- Individual-window metadata is Xpra-specific and may not map perfectly across native/browser clients.
- GPL-2.0-or-later creates a strong source/distribution boundary; running Xpra as a separate service is safer than copying code into Ptah Core.
- The feature and dependency surface is large.
- Authentication/proxy configuration is deployment machinery, not Ptah identity or permission policy.
- Browser URL parameters and connection endpoints can leak credentials or session information if designed poorly.

## Must not be inherited

- Xpra session/window IDs as canonical Ptah Application Session or Window identity.
- GPL source copied into Ptah Core without explicit licence approval.
- clipboard, file, audio, webcam, notification or printing enabled as one unrestricted display permission.
- display reconnect interpreted as complete Workspace/Application checkpoint recovery.
- public unauthenticated TCP/HTTP/WebSocket listeners.
- X11-only assumptions embedded in the public Application Provider contract.
- a remote window being visible treated as semantic readiness or functional acceptance.
- Xpra proxy/auth schemas exposed as Ptah's public API.

## Integration decision

**WRAP XPRA AS THE PRIMARY INDIVIDUAL-LINUX-APPLICATION DISPLAY BACKEND CANDIDATE.**

Ptah should launch and supervise Xpra as a separate Application Display Facility attached to a Linux Workspace/Application Provider.

Recommended roles:

1. seamless individual-window mode for native applications;
2. desktop mode for full Linux graphical workspaces;
3. shadow mode only for explicitly approved existing sessions;
4. HTML5 client as one browser presentation path;
5. native clients as optional operator paths.

Ptah owns Application Session, Window, Stream, capability, privacy, Activity and Receipt records.

## Native Ptah gap

Ptah must define:

- Application Provider and Application Session lifecycle;
- stable Window identity and backend-window aliases;
- process/window/stream correlation;
- display mode and compositor/X11/Wayland capability declarations;
- per-capability permissions for video, audio, input, clipboard, files, notifications, printing and devices;
- browser connection tokens and short-lived scoped credentials;
- stream/recording Artifact references;
- reconnect, provider restart and stale-session rules;
- application launch, first-window, visible-frame and semantic-readiness receipts;
- resource accounting and session cleanup;
- GPL packaging/service boundary and replacement path.

## Exit strategy

Ptah's Linux Application Display contract remains implementable through Xpra, VNC/noVNC, Guacamole, RDP, compositor-native remoting or future Wayland protocols. Xpra-specific session/window IDs remain adapter metadata.

## Validation required

1. Launch two independent Linux applications and expose separate reconnectable windows.
2. Disconnect/reconnect the browser without terminating the application processes.
3. Restart the Xpra display backend and preserve or explicitly fail Application Session recovery without false continuity.
4. Verify clipboard, audio, file transfer and input are independently permissioned.
5. Record a session and link the recording to exact Application Session/Window/Activity IDs.
6. Test full desktop, seamless and shadow modes as distinct capabilities.
7. Prove browser access uses short-lived scoped credentials and no session secret in retained URLs/logs.
8. Test X11 and an approved Wayland/compositor path and record compatibility limits.
9. Replace Xpra with another display backend without changing public Application Session identity.
