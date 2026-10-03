# Flash the firmware

You only do this once. After that, updates go over Wi-Fi.

**Pick your firmware** (see [Which opener do I have?](../start/which-opener.md)):

| Firmware | For |
|---|---|
| `garage-secplus2` | Security+ 2.0, **yellow** learn button (myQ) |
| `garage-secplus1` | Security+ 1.0, **purple / red / orange** learn button |
| `garage-dry-contact` | Simple 2-wire wall button, no sensor |
| `garage-dry-contact-sensor` | Simple 2-wire wall button **plus** a reed switch on SENSORS CLOSED |

Plug the XIAO into your computer with a USB-C **data** cable. It doesn't need to be connected to the garage door yet.

## Option A: one-click browser installer (easiest)

Open the **[browser installer](https://jamessilvia20.github.io/xiao-garage-door/install/)** in **Chrome or Edge** on a computer, click your firmware's **Install** button, pick the XIAO's port, and follow the prompts. At the end it asks for your **Wi-Fi name and password**, and you're done.

## Option B: from GitHub, using ESPHome Web

1. Download your firmware's `.factory.bin` from the [latest release](https://github.com/JamesSilvia20/xiao-garage-door/releases/latest), or from [`docs/install/firmware/`](https://github.com/JamesSilvia20/xiao-garage-door/tree/main/docs/install/firmware).
2. Go to **[web.esphome.io](https://web.esphome.io)** in Chrome or Edge → **Connect** → pick the XIAO → **Install** → choose the `.bin` file.
3. When it finishes, click **⋮ → Configure Wi-Fi** and enter your Wi-Fi.

## Option C: ESPHome Device Builder (if you already use ESPHome)

Use one of the YAML files in [`firmware/`](https://github.com/JamesSilvia20/xiao-garage-door/tree/main/firmware) as your device config, or flash with option A and then click **Adopt** when it appears in your ESPHome dashboard. Adopting lets you customise it, for example the door's travel time.

## Setting Wi-Fi later

If the board can't reach your Wi-Fi, it makes its own hotspot called **"Garage Door Setup"**. Join it from your phone, and a page pops up where you pick your network.

## Troubleshooting flashing

- **The computer doesn't see the board:**
  - Use a different cable; many USB-C cables only charge.
  - Plug straight into the computer, not through a hub.
  - **Mac:** newer Macs ask **"Allow accessory to connect?"**. Click **Allow**. If you missed it, unplug and replug with the Mac unlocked.
- **Still nothing? Force download mode.** Hold the tiny **B** (BOOT) button on the XIAO, plug in the cable, then let go after 2 seconds.
- **It worked before, now it's invisible even in download mode:** look for a **solder bridge**, especially between **3V3 and a neighbouring pin**. See [Troubleshooting](../help/troubleshooting.md).

Next: [Add to Home Assistant →](home-assistant.md)
