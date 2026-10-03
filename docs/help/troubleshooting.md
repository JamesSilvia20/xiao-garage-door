# Troubleshooting

Real problems we hit while building these, and how we fixed them.

## The computer doesn't see the XIAO

| Cause | Fix |
|---|---|
| Charge-only USB-C cable | Use a cable that also carries data (the one from a phone or laptop). |
| Mac blocked the accessory | Click **Allow** on the "Allow accessory to connect?" popup. Replug with the Mac unlocked. |
| Firmware put the USB to sleep, or it's busy | Hold **B** (BOOT), plug in, release after 2 s. That's download mode, which always works on a healthy board. |
| **Solder bridge on the power pins** | If even download mode shows nothing, check for continuity between **3V3 and its neighbours** (GND, D10) and between **5V and GND**. Clear any bridge. |

## The switch is "on" all the time, or works backwards

Symptom: the opener terminals read as connected even when idle, or the transistor's gate reads 3.3 V while the button is off.

| Cause | How to check | Fix |
|---|---|---|
| **Wire on 3V3 instead of GND** (they're neighbours!) | Continuity from **terminal slot 2** to the **USB-C metal shell** must beep. | Move the wire one pin toward the USB end, to GND. |
| **D2 bridged to 3V3** | D2 ↔ 3V3 must not beep. | Clear the bridge. |
| **Wire on the wrong column** | D2 is the 3rd pin from the USB end in the **D0–D6** column. | Move it to the right column. |

## The meter beeps across the terminals at rest

If it beeps **only one way round**, that's the MOSFET's built-in body diode, and it's normal. Use the **Ω** setting: at rest it should read **OL** in at least one direction, and a low reading during a press.

## The door doesn't move when I press the button

1. Did the [dry-contact test](../start/which-opener.md#3-the-30-second-dry-contact-test) work (a wire across the wall-button terminals moves the door)? If not, your opener isn't dry-contact.
2. Is **RED** on the wall-button **+** terminal and **WHT** on the common? If they're swapped, the transistor can't switch.
3. Check the board's press with a meter (see [perfboard checks](../hardware/perfboard.md#check-it-switches-after-flashing)).

## Security+: "sync failed" notification, or no status

- Check the **RED / WHT / BLK** wiring matches the opener's terminals.
- Make sure you flashed the right protocol (yellow learn button = `secplus2`, purple/red/orange = `secplus1`).
- More help: the [esphome-ratgdo troubleshooting](https://github.com/ratgdo/esphome-ratgdo) docs apply directly.

## Apple Home shows the wrong state (dry contact, no sensor)

That's expected after someone uses the wall button or a remote: the board can only **assume** the position. Use **Press Wall Button** once to resync, or add a reed switch and switch to `garage-dry-contact-sensor`.

## Still stuck?

Open a [discussion](https://github.com/JamesSilvia20/xiao-garage-door/discussions) with:
- photos of **both sides** of your board;
- your opener's model;
- which firmware you flashed;
- what the multimeter shows.
