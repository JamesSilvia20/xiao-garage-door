# Browser installer

Flash your XIAO ESP32-C6 straight from this page. Use **Chrome or Edge on a computer**; phones and Safari can't do it.

1. Plug the XIAO into your computer with a USB-C **data** cable.
2. Click the **Install** button for your opener type.
3. Pick the XIAO's serial port, then follow the prompts. At the end, enter your **Wi-Fi**.

Not sure which one? See [Which opener do I have?](../start/which-opener.md)

<script type="module" src="https://unpkg.com/esp-web-tools@10/dist/web/install-button.js?module"></script>

| Opener | Install |
|---|---|
| **Security+ 2.0**: yellow learn button (myQ) | <esp-web-install-button manifest="firmware/garage-secplus2.manifest.json"></esp-web-install-button> |
| **Security+ 1.0**: purple / red / orange learn button | <esp-web-install-button manifest="firmware/garage-secplus1.manifest.json"></esp-web-install-button> |
| **Dry contact**: simple 2-wire wall button | <esp-web-install-button manifest="firmware/garage-dry-contact.manifest.json"></esp-web-install-button> |
| **Dry contact + reed switch** | <esp-web-install-button manifest="firmware/garage-dry-contact-sensor.manifest.json"></esp-web-install-button> |

> [!NOTE]
> Reading this on GitHub? The Install buttons only work on the website: **https://jamessilvia20.github.io/xiao-garage-door/install/**. Or follow [Option B in the flashing guide](../setup/flash.md#option-b-from-github-using-esphome-web).

Problems? See [Flash the firmware → Troubleshooting](../setup/flash.md#troubleshooting-flashing).
