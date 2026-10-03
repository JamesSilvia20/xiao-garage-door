# Firmware

ESPHome configs for the Seeed XIAO ESP32-C6 on the XIAO Garage Door board (or the perfboard build).

| Config | Opener |
|---|---|
| [`garage-secplus2.yaml`](garage-secplus2.yaml) | Security+ 2.0, yellow learn button (myQ) |
| [`garage-secplus1.yaml`](garage-secplus1.yaml) | Security+ 1.0, purple / red / orange learn button |
| [`garage-dry-contact.yaml`](garage-dry-contact.yaml) | Simple 2-wire wall button, no sensor (assumed state) |
| [`garage-dry-contact-sensor.yaml`](garage-dry-contact-sensor.yaml) | Simple 2-wire wall button + reed switch (real state) |

No Wi-Fi passwords or keys are baked in. Set Wi-Fi with the browser installer (Improv) or the "Garage Door Setup" hotspot.

**Flash:** see [Flash the firmware](../docs/setup/flash.md). **Reference:** [Firmware reference](../docs/makers/firmware.md).
