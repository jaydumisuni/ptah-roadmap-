# Donor Record — noVNC and websockify

**Phase:** 0A / WP07B  
**Status:** FIRST-PASS COMPLETE — LIGHTWEIGHT BROWSER VNC CLIENT/WEBSOCKET PROXY DONOR  
**Inspected:** 2026-07-17

## Identity

### noVNC

- Canonical URL: https://github.com/novnc/noVNC
- Default branch: `master`
- Pinned commit: `7c36fabe599e053c5a81e98e091ac636f6c1e174`
- Licence: primarily MPL-2.0; bundled components require their own notices

### websockify

- Canonical URL: https://github.com/novnc/websockify
- Default branch: `master`
- Pinned commit: `3dd228b81ade1ff76a27ad12eed6e78df8c6f8a6`
- Licence: LGPL-3.0

- Classification: browser VNC presentation and WebSocket-to-TCP translation donor
- Ptah targets: lightweight browser display, mobile-browser input, VNC compatibility, WebSocket stream proxy and simple VM/desktop console access

## Files/components inspected

- noVNC `README.md`
- noVNC server/client requirements and embedding/library paths
- websockify `README.md`
- websockify `COPYING`
- WebSocket proxy, TLS, token/auth plugin, recording and wrapped-program behavior

## Verified capabilities and patterns

### noVNC

- Runs as a browser VNC client on desktop and mobile browsers.
- Supports multiple VNC authentication methods and encodings, including JPEG, ZRLE and H.264-capable paths.
- Supports scaling, clipping, resizing, local cursor, Unicode clipboard and touch gestures.
- Can be embedded as a JavaScript library or deployed as an application.
- Requires a VNC server with WebSocket support or a WebSocket-to-TCP proxy.

### websockify

- Translates bidirectional WebSocket traffic to ordinary socket traffic.
- Supports WSS/TLS, authentication plugins and token-based target selection.
- Can serve static web content and proxy on one listener.
- Can record proxied traffic.
- Can launch/wrap a local program and proxy to its dynamically rebound port.
- Can run as a daemon or OCI container.
- Supports alternative implementations in other languages.

## What this donor set completes

- A small browser-display path for any existing VNC-capable provider.
- Mobile-browser mouse/touch and clipboard interaction.
- A clean separation between browser client, WebSocket proxy and VNC server.
- An embeddable client library useful for Ptah's own UI.
- A simple fallback for QEMU/VNC consoles, Linux desktops and other providers where richer gateways are unnecessary.
- Token-to-target routing and short-lived proxy concepts.

## Important limitations for Ptah

- noVNC is only a client; it does not create or manage the VNC server, VM, application or desktop.
- VNC is framebuffer-oriented and generally lacks individual application/window semantics.
- A connected framebuffer does not prove application launch or semantic readiness.
- Clipboard and input are sensitive side effects.
- websockify's token plugins and arbitrary TCP forwarding can become SSRF/internal-network gateways if exposed directly.
- Traffic recording may contain credentials and sensitive screen/input data.
- Self-signed certificate examples are development guidance, not a production trust model.
- noVNC and websockify licences impose file/library distribution obligations that must remain tracked.
- Target VNC security and encryption vary by server; WSS only protects the browser-to-proxy segment.
- WebSocket proxy process/session IDs are not Ptah Stream or Session identities.
- Full desktop pixels provide no semantic UI hierarchy.

## Must not be inherited

- arbitrary caller-selected TCP/VNC targets;
- persistent connection secrets in URL parameters or browser storage;
- self-signed certificates accepted silently in production;
- clipboard/input bundled with read-only display access;
- websockify token mapping as canonical Ptah authorization;
- VNC connection state used as application proof;
- recorded proxy bytes retained without privacy/retention metadata;
- noVNC UI adopted wholesale as Ptah's Application Centre;
- MPL/LGPL source mixed into Ptah Core without licence review.

## Integration decision

**SUPPORT AS A LIGHTWEIGHT VNC/BROWSER DISPLAY BACKEND, BELOW XPRA AND GUACAMOLE IN CAPABILITY.**

Recommended role:

- simple QEMU/VM console access;
- Linux desktop fallback;
- mobile-friendly browser access;
- local/development providers;
- compatibility when Xpra/Guacamole is unavailable or unnecessary.

Ptah owns provider lifecycle, target selection, short-lived stream tokens, input/clipboard permissions, Application Session and receipts.

## Native Ptah gap

Ptah must define:

- VNC provider/server capability and lifecycle record;
- browser display Stream identity;
- scoped one-time connection token and approved target mapping;
- separate display/input/clipboard capability scopes;
- TLS trust and proxy-network isolation;
- first-frame, reconnect and closure receipts;
- recording Artifact plus privacy/retention class;
- geometry/orientation/resolution-change handling;
- semantic automation fallback separate from framebuffer access;
- licence/bundling and backend replacement plan.

## Exit strategy

Ptah's browser-display API remains independent. noVNC/websockify can be replaced by Guacamole, Xpra HTML5, a WebRTC gateway or another VNC client/proxy without changing public Session/Stream identities.

## Validation required

1. Connect a browser and mobile browser to an approved VNC provider.
2. Reject arbitrary target hosts/ports and expired tokens.
3. Exercise resize, scaling, clipboard and touch input as separate capabilities.
4. Prove WSS terminates under a trusted deployment certificate and the target leg's security is recorded separately.
5. Restart websockify/VNC and reconcile stream state without claiming application continuity.
6. Record traffic only under explicit policy and hash/store it as a protected Artifact.
7. Replace noVNC with Guacamole/Xpra presentation without changing Application Session identity.
