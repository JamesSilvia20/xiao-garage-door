# Build it on perfboard

No PCB order? You can build the same circuit by hand on a piece of perfboard. Never soldered? Read [Soldering 101](soldering-101.md) first. It takes 15 minutes and saves a lot of frustration.

> [!TIP]
> **Dry-contact openers** need only **one transistor and one resistor**, a great first soldering project. **Security+ openers** need the full circuit, including one tiny surface-mount part. If that sounds scary, the [ready-made PCB](order-pcb.md) is the easy way.

## Know your XIAO pins first

This is where most mistakes happen. Several pins sit right next to each other, and mixing up GND and 3V3 is very easy (we did it 😅).

Hold the XIAO **chips facing you, USB-C at the top**:

```
              USB-C
        ┌───────────────┐
   D0   │ ●           ● │  5V
   D1   │ ●           ● │  GND   ← 2nd pin from the USB end
   D2   │ ●           ● │  3V3   ← 3rd pin from the USB end (NOT ground!)
   D3   │ ●           ● │  D10
   D4   │ ●           ● │  D9
   D5   │ ●           ● │  D8
   D6   │ ●           ● │  D7
        └───────────────┘
```

**Golden rule: count from the USB-C end.** It works whichever way you're looking at the board, front or back.
- **D2** = 3rd pin from the USB end, in the **D0–D6** column.
- **GND** = 2nd pin from the USB end, in the **5V / GND / 3V3** column.

> [!WARNING]
> On the **back** of the board everything is mirrored left-right. Before you flip it over, put a marker dot next to the holes you'll solder.

**Foolproof GND check:** with the multimeter on continuity (beep), touch the **metal shell of the USB-C port** (that's ground) and then the pin. **GND beeps; 3V3 does not.**

## Dry-contact build (old / simple openers)

### Parts
1 × 2N7000, 1 × 10 kΩ resistor, perfboard, a 2- or 3-pin screw terminal (or two wires), and short pieces of solid wire.

### The 2N7000's legs

Hold it with the **flat side (the printing) facing you** and the **legs pointing down**:

```
   ┌─────────┐
   │  flat   │
   └─┬──┬──┬─┘
   LEFT MID RIGHT
   (S)  (G)  (D)
```

### Wiring: 5 connections

| From | To | Why |
|---|---|---|
| XIAO **D2** | 2N7000 **middle** leg | The "press" signal |
| 10 kΩ resistor | between 2N7000 **middle** leg and **GND** | Keeps it off while the XIAO boots |
| 2N7000 **left** leg | **GND** | |
| 2N7000 **right** leg | terminal **slot 1** | Goes to the opener's wall-button **+** |
| XIAO **GND** | terminal **slot 2** | Goes to the wall-button **common** |

Nothing connects to **3V3** or **5V**.

### Check before powering (USB unplugged, meter on continuity)

These should **beep**:
- [ ] D2 ↔ 2N7000 middle leg
- [ ] 2N7000 left leg ↔ terminal slot 2 ↔ **USB-C metal shell**
- [ ] 2N7000 right leg ↔ terminal slot 1

These must **not** beep:
- [ ] Any two legs of the 2N7000
- [ ] D2 ↔ GND
- [ ] GND ↔ 3V3, and GND ↔ 5V
- [ ] Any two neighbouring XIAO pins (solder bridges love to hide here)

### Check it switches (after flashing)

1. Meter on **DC volts**, black probe on the **USB-C shell**, red probe on the 2N7000 **middle leg**. Press the door button in Home Assistant: it should read about **0 V at rest** and **3.3 V during the press**.
2. Meter on **continuity**, across **slot 1 and slot 2**: **silent** at rest, **beeps** during a press.

> [!NOTE]
> At rest the meter may beep in **one** probe direction only. That's the transistor's built-in diode, and it's normal. It should be silent the other way round.

## Security+ build (LiftMaster / Chamberlain with a learn button)

This is the full circuit from [How the circuit works](circuit.md), the same as the PCB but with a 2N7000 instead of the 2N7002:

| Block | Connections |
|---|---|
| **Send** | D2 → AO3400A **gate**; 10 kΩ gate→GND; AO3400A **source**→GND; AO3400A **drain** → **RED** terminal |
| **Receive** | 2N7000 **drain** → D3; 10 kΩ from D3 → **3V3**; 2N7000 **source** → GND; 2N7000 **gate** → 1 kΩ → **RED**; 100 kΩ gate→GND |
| **Obstruction** | **BLACK** terminal → 10 kΩ → D5; 10 kΩ D5→GND |
| **Ground** | XIAO GND → **WHITE** terminal |

**AO3400A pins (SOT-23):** pin 1 = gate, pin 2 = source, pin 3 = drain (the single pin on its own side). Solder it onto a **SOT-23 to DIP adapter** first:
1. Tin one pad.
2. Hold the chip with tweezers and reheat that pad.
3. Solder the other two legs with a tiny bit of solder each.

Then check pin 1 against the adapter's marking.

## Next

[Flash the firmware →](../setup/flash.md)
