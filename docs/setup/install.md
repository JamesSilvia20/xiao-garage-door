# Install it at the opener

Read [Safety first](../start/safety.md) before this.

## 1. Measure (2 minutes, opener plugged in)

Set your multimeter to **DC volts (V⎓)** and measure across the opener's terminals:

| Opener type | Measure | Expect |
|---|---|---|
| **Security+** | **RED to WHITE** | about **12 V**, often flickering (that's the data) |
| **Security+** | **BLACK to WHITE** | about **7 V or less** (the 10k/10k divider brings it to ≤ 3.5 V) |
| **Dry contact** | across the **2 wall-button terminals** | steady **5–24 V DC**. Note which terminal is **+**: when the reading is positive, that's the one under the **red** probe. |

> [!CAUTION]
> If you see **AC volts**, a reading **over 24 V**, or (Security+) BLACK above about 7 V, **stop** and ask in the [discussions](https://github.com/JamesSilvia20/xiao-garage-door/discussions) before connecting.

## 2. Connect

1. **Unplug the opener.**
2. Run short wires from the board's **OPENER** terminal to the opener's terminals. Put them **alongside** the existing wall-button wires; don't remove those.

| Board OPENER terminal | Security+ opener | Dry-contact opener |
|---|---|---|
| **RED** | Red terminal | Wall-button **+** terminal |
| **WHT** | White terminal | Wall-button **common** (the other one) |
| **BLK** | Black terminal (photo-eye) | not used |

3. **Optional reed switch (dry-contact + sensor firmware):** wire it from **SENSORS CLOSED** to **SENSORS GND**. Mount it so it **closes when the door is fully closed**.
4. Mount the board near the opener: zip-tie it, use the 4 × M3 holes, or put it in a small case. Keep it away from the motor's moving parts.
5. Plug the opener back in, and power the XIAO from a USB charger in the opener's ceiling outlet.

## 3. Test

- **Security+:** in Home Assistant the door should show its real state within a few seconds. Toggle the **Light**, then try **Open** and **Close** while watching the door.
- **Dry contact:** press **Press Wall Button**. The door should start moving. Press again to stop it.
- **Finally:** test the safety reverse with a 2×4 on the floor under the door.

🎉 You're done! Enjoy asking Siri to close the garage.

Problems? → [Troubleshooting](../help/troubleshooting.md)
