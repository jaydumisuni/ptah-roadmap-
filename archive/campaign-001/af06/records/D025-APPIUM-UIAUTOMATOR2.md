# D025 — Appium UiAutomator2 Driver

Status: candidate record — paired evidence complete

Primary Archivist: `AF06-P06`

Independent Verifier: `AF06-V06`

Inspected: 2026-07-23

## Canonical source identity

- source: `appium/appium-uiautomator2-driver`;
- default branch: `master`;
- exact inspected commit: `88e78711595807f3893e9dbed233549597a43a0f`;
- root licence: Apache-2.0;
- repository role: Appium Android automation driver using UiAutomator2;
- archived: false.

## Primary evidence packet

The driver provides Android application session, element discovery, hierarchy, action and device-command patterns behind Appium's WebDriver surface.

## Independent verification packet

Android server APKs, platform tools, SDK/device versions, Appium server/client and OEM behaviour are separate compatibility surfaces. Element IDs and cached hierarchy can become stale. Command acknowledgement requires post-condition read-back and reacquisition.

## Contradiction and supersession

This is a platform-specific Provider, not Ptah's semantic UI authority or generic Device identity.

## Bounded outcome

`accepted_for_archive_apache_android_webdriver_driver_with_server_sdk_stale_element_and_postcondition_limits`

Allowed reuse:

- run a pinned driver behind Ptah Application/Device Session boundaries;
- retain exact Appium, driver, server APK, platform-tools and device revisions.

Restrictions:

- preserve Apache notices and review transitive APK/tool dependencies separately;
- require Device Lease/Fence and reacquire stale UI targets;
- do not expose element/session IDs as canonical identities;
- do not claim action success without independent state read-back.

This outcome does not authorize implementation.