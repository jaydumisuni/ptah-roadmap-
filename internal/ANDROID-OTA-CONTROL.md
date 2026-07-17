# Internal Recovery Record — Android OTA Device-Control Utility

**Phase:** 0A / WP06  
**Status:** FIRST-PASS COMPLETE — BRAND-SPECIFIC ADB UPDATE-SERVICE CONTROL, NOT AN OTA PACKAGE DOMAIN PACK  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/TechGuyTool-Android-OTA-IdiotProof`
- Visibility: Public
- Default branch: `main`
- Pinned commit: `a4fea0be1bf5ab042fa9e0f23bba985dc05f9e14`
- Licence: custom attribution/non-commercial terms. Commercial embedding/integration requires prior permission; this is not an open-source licence suitable for copying into public Ptah.
- Ptah relevance: brand-specific ADB OTA package/service controls, device authorization checks, operation reversibility claims and analysis-versus-device-operation separation.

## Files inspected

- `README.md`
- initial commit/diff
- `ota/Samsung_TGT_OTA_IdiotProof.cmd`
- `ota/Tecno_Infinix_TGT_OTA_IdiotProof.cmd`
- launcher/brand-menu behavior visible in the initial import

## Verified implemented behavior

- Windows batch launcher selects a brand-specific script.
- Documented brand coverage includes Samsung, Transsion/Tecno/Infinix, Xiaomi, Oppo/Realme, Vivo/iQOO, OnePlus, Pixel, Motorola, Nokia/HMD, Sony, Huawei/Honor and LG.
- Requires ADB, USB debugging and accepted RSA authorization.
- Scripts start/restart the ADB server, wait for a device and check that an authorized `device` row exists.
- Brand scripts issue `pm clear` and `pm disable-user --user 0` calls for known update/updater packages.
- Samsung profile targets packages including `com.wssyncmldm`, `com.sec.android.soagent` and Samsung update center.
- Transsion profile targets generic/Transsion/Tecno/Infinix updater package names.
- Scripts show best-effort on-device toast messages and reboot the device afterward.
- The README states the operation is reversible by factory reset, full firmware flash or manually re-enabling packages.
- The repository also documents the consequence that security patches, feature updates and OEM fixes will no longer arrive while update services remain disabled.

## Strong internal patterns for Ptah

1. Device-side update control is brand/profile dependent.
2. ADB transport, authorization and exact device selection must be proven before package-state operations.
3. Update-package names and component actions belong in versioned device/OEM profiles rather than hard-coded universal logic.
4. Device operation consequences and reversibility need explicit caller-facing descriptions.
5. Firmware package analysis/apply and device-side updater-service control are different Facilities.
6. A caller may intentionally block updates, but Ptah should record the exact operation and resulting observed state rather than impose a universal policy.
7. Brand helper codes and enablement paths are support metadata, not proof of ADB/device readiness.

## Important limitations

- This repository does **not** parse OTA ZIPs, `payload.bin`, sparse images, super/dynamic partitions, metadata, AVB/vbmeta or source/target build compatibility.
- It does not download, verify, compare, reconstruct or apply firmware packages.
- All ADB command stdout/stderr is redirected to `nul`, so package-manager failures are hidden.
- There is no per-command exit/result/receipt capture.
- The scripts do not read back `pm list packages -d`, component state or updater behavior after modification/reboot.
- They claim “permanently blocked” despite documenting reversibility and without verified post-reboot state.
- Device selection checks only that at least one authorized device row exists; multiple-device ambiguity is not rejected and no serial selector is used.
- Package existence/version/OEM build compatibility is not checked before clear/disable actions.
- Disabling `com.android.providers.downloads` in some profiles can affect broader device behavior beyond OTA.
- `pm clear` destroys application state and is a side effect separate from disabling a package.
- The operation reboots automatically without a separate confirmation/receipt.
- There is no backup of prior package/component enabled state and no generated restoration plan.
- No stable Activity/operation/attempt/nonce/connection-epoch identities exist.
- No cancellation, recovery, read-back verification, rollback receipt or exact device inventory is captured.
- A toast is best-effort UI feedback and not operation proof.
- Broad exception/failure handling is absent in batch scripts.
- Custom non-commercial licence prevents direct public Ptah integration.

## What Ptah should reuse or adapt

- OEM/profile-driven update-service package catalogue;
- exact ADB authorization/device-selection prerequisite;
- separate `clear_state`, `disable_component`, `enable_component` and `reboot` operation classes;
- caller-facing security/update consequences;
- reversible-operation and prior-state capture requirements;
- support/helper-code metadata kept separate from proof;
- product utility later calling a neutral Device Package-State Facility.

## What Ptah must not inherit

- “Idiot Proof” or product branding in public Ptah contracts.
- hidden command output and unconditional success claims.
- automatic reboot in the same opaque operation.
- multiple-device ambiguity.
- package clear/disable actions without inventory, prior-state backup and read-back.
- “permanently blocked” wording without authoritative post-reboot proof.
- update-security policy imposed by Ptah.
- device updater control confused with OTA firmware decomposition/application.
- custom-licensed source copied into public Ptah.
- automatic retry of package-state/reboot operations after uncertain connection loss.

## Classification

**ADAPT THE OEM PROFILE AND OPERATION-CONSEQUENCE REQUIREMENTS; REBUILD AS A RECEIPT-DRIVEN DEVICE PACKAGE-STATE FACILITY.**

This internal utility informs firmware-side `DEVICE-001`, `FW-005`, `CORE-004`, `RELAY-002`, `OBS-001` and ADR-0004 proof-level rules. It does not close Android OTA package analysis.

## Native Ptah completion required

- exact selected device/serial/build/OEM profile identity;
- package/component existence and current-state inventory;
- prior-state backup and restoration recipe;
- separate clear/disable/enable/reboot Activities and receipts;
- per-command exit/stdout/stderr plus post-operation read-back;
- nonce/operation/attempt/Node epoch correlation;
- multiple-device rejection unless caller selects one;
- caller confirmation for destructive state clearing and reboot;
- delayed post-reboot verification;
- OEM profile version/provenance and unsupported-package handling;
- strict separation from OTA package/payload analysis and flashing;
- public-neutral implementation independent of custom-licensed scripts.

## Validation inherited into Ptah

1. Inventory one selected device and reject multiple-device ambiguity.
2. Record every updater package's present/enabled/state-data status before mutation.
3. Disable only packages that exist and match the selected OEM/profile/build evidence.
4. Preserve stdout/stderr/exit and verify disabled state before and after reboot.
5. Distinguish package clear from package disable and require explicit caller approval for each destructive action.
6. Generate and execute a restoration recipe that returns packages to their observed prior states.
7. Disconnect during operation and reconcile from authoritative device status without blind retry.
8. Prove failure of one package action produces partial/degraded state rather than universal success.
9. Keep OTA package analysis available even when no device/ADB is connected.
10. Confirm public Ptah contains no custom-licensed batch implementation or private profile policy.
