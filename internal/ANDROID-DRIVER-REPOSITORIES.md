# Internal Recovery Record — Android Driver Repositories

**Phase:** 0A / WP06  
**Status:** INSPECTED — NO AUDITABLE DRIVER PACK FOUNDATION RECOVERED  
**Inspected:** 2026-07-17

## Sources inspected

### `jaydumisuni/TechGuyDrivers`

- Pinned commit: `f575281a0682e921bdb1a593cb58757c77156b89`
- Repository contains only a README at the inspected pin.
- README claims Android and Arduino Windows drivers, but no driver files, manifests, hashes, licences, INF/provider identities or installation logic are present.

### `jaydumisuni/android-drivers`

- Pinned commit: `ca582dcdb3058ed4086f717d61fae57de6ef469a`
- README contains only the repository title.
- The inspected upload commit contains `java.apk`, not an auditable Android USB-driver package.
- A later commit deletes that APK.
- No Qualcomm, MediaTek, Unisoc, Google, Samsung, Apple or libusb driver manifest was recovered.

## Conclusion

Repository names and README claims do not establish a usable driver foundation.

These repositories cannot currently supply:

- driver inventory;
- supported VID/PID/interface modes;
- driver version/provider/signature identity;
- Windows INF/CAT/SYS relationships;
- libusb/WinUSB/filter-driver selection;
- install/uninstall/rollback logic;
- compatibility tests;
- redistribution rights;
- provenance or hashes.

## Strong lesson for Ptah

USB driver identity is part of the Node/Facility capability and operation proof. A driver pack must be treated as a signed, versioned Artifact with:

- provider/product/version;
- operating-system/architecture;
- supported device/interface IDs;
- INF/CAT/SYS component hashes;
- signature/trust evidence;
- install mode and rollback;
- reboot requirement;
- conflict/filter-driver risk;
- licence/redistribution rights;
- exact operation that required it.

A generic “drivers installed” flag is insufficient.

## Classification

**REJECT AS CURRENT FOUNDATIONS; RETAIN AS PLACEHOLDERS PENDING VERIFIED DRIVER ARTIFACTS.**

Do not copy, bundle or advertise driver coverage from these repositories.

## Recovery criteria

Re-open only when a repository or approved storage location contains:

1. exact driver packages or immutable download manifests;
2. SHA-256 or stronger hashes;
3. provider/version/OS/architecture metadata;
4. signed-driver verification;
5. supported VID/PID/interface-mode mappings;
6. install/uninstall/rollback scripts with receipts;
7. redistribution/licence records;
8. live proof on representative MTK, Qualcomm, Unisoc and generic ADB/Fastboot interfaces.
