# I017 — USB and serial engine

Status: candidate record — paired evidence complete

Primary Archivist: `AF09-P09`
Independent Verifier: `AF09-V09`
Inspected: 2026-07-23

## Canonical source identity
- supporting sources: `jaydumisuni/android-drivers` at `ca582dcdb3058ed4086f717d61fae57de6ef469a` and `jaydumisuni/TTG-usb-redirect-` at `bb877636d76f85d5718d23f8da68d0169ac34432`;
- standalone engine repository: not established;
- role: USB/serial discovery, driver, port and transport requirements.

## Evidence and boundary
The sources establish driver inventory, USB endpoint and redirect/serial transport requirements. The verifier confirmed VID/PID/COM/port names are observations/aliases, hotplug creates new epochs, and only one centralized device-state manager may own USB access.

## Bounded outcome
`accepted_for_archive_usb_serial_engine_requirements_with_driver_endpoint_epoch_exclusive_ownership_and_source_boundaries`

Restrictions: exact driver/device/interface evidence; centralized exclusive access, Lease/Fence and hotplug reconciliation; port IDs remain aliases; command transport never supplies protected-action authority; no standalone source reuse claim.

This outcome does not authorize implementation.