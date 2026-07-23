# D024 — Appium

Status: candidate record — paired evidence complete

Primary Archivist: `AF05-P10`

Independent Verifier: `AF05-V10`

Inspected: 2026-07-23

## Canonical source identity

- source: `appium/appium`;
- default branch: `master`;
- exact inspected commit: `e0c9018453ae605cc8df8f83317716a0694c34c5`;
- root licence: Apache-2.0;
- repository role: WebDriver-based cross-platform automation server and extension framework;
- archived: false.

## Primary evidence packet

Appium demonstrates protocol-based application automation, a core server separated from platform drivers and plugins, session lifecycle, capabilities and cross-platform client contracts.

## Independent verification packet

The verifier confirmed that drivers, plugins, platform SDKs, device services, WebDriver clients and applications are separately versioned trust surfaces. Session creation and command acknowledgement do not prove the intended device/application state. Driver-specific IDs and capabilities remain aliases and observations.

## Contradiction and supersession

Appium is a Device/Application Provider donor, not Ptah Core or canonical Device Session authority.

## Bounded outcome

`accepted_for_archive_apache_webdriver_automation_platform_with_driver_plugin_and_postcondition_boundaries`

Allowed reuse:

- run or adapt a pinned Appium server behind Ptah Device/Application Session boundaries;
- retain exact server, driver, plugin, client, platform and capability revisions.

Restrictions:

- preserve Apache notices and inspect every driver/plugin separately;
- require Device Lease/Fence and post-condition read-back for actions;
- do not expose Appium session/element IDs as canonical Ptah identities;
- do not infer iOS, Android, Windows or macOS support without exact driver/platform proof.

This outcome does not authorize implementation.