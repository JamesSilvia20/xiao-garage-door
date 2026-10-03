# Add to Home Assistant

1. After flashing and setting Wi-Fi, Home Assistant usually finds it on its own. Go to **Settings → Devices & services**, look for **"Discovered: Garage Door"** under ESPHome, and click **Add**.
2. If it isn't discovered, click **Add integration → ESPHome** and enter `garage-door-xxxxxx.local` (the name shown in the installer) or the board's IP address.
3. Assign it to your **Garage** area.

## What you get

**Security+ firmware** (`garage-secplus2` / `garage-secplus1`):
- **Door** (cover): open / close / stop, with real position and opening/closing state
- **Light**, **Lock** (locks out remotes), **Obstruction**, **Motion**, **Button** presses, **Openings** count, and more

**Dry-contact firmware** (`garage-dry-contact`):
- **Door** (cover): open / close / stop. The position is **assumed** from the last command and the travel time.
- **Press Wall Button**: one press, exactly like the wall button.

**Dry-contact + sensor** (`garage-dry-contact-sensor`):
- **Door** (cover) with **real** open/closed status from the reed switch, and **Closed Sensor** / **Open Sensor**. Open/Close only press the button if the door isn't already there.

> [!WARNING]
> **Dry contact without a sensor:** single-button openers cycle **open → stop → close → stop**. If someone uses the wall button or a car remote, the door shown in HA can be wrong until the next command, and pressing "Close" could then actually open it. Add a reed switch (`garage-dry-contact-sensor`) to fix this for good.

## Set your door's travel time (dry contact only)

Time how long your door takes to open fully (for example 13 seconds). In ESPHome, adopt the device and change:

```yaml
substitutions:
  travel_time: 13s
```

## Example automation: notify if left open

```yaml
alias: Garage left open
triggers:
  - trigger: state
    entity_id: cover.garage_door_door
    to: open
    for: "00:15:00"
actions:
  - action: notify.notify
    data:
      message: "The garage door has been open for 15 minutes."
```

Next: [Add to Apple Home →](apple-home.md)
