# Parts and cost

## Everyone needs

| Part | Approx. cost | Notes |
|---|---|---|
| **Seeed Studio XIAO ESP32-C6** | $5–7 | Buy it **with pins** (headers), or solder them on yourself. One per door. |
| **USB-C cable + any 5 V USB charger** | (you probably have one) | Powers the board. Plug it into the outlet the opener uses. Some cables only charge, so use one that also carries **data** for flashing. |
| **2–3 wires** | (anything thin) | From the board to the opener's terminals. 22 AWG doorbell or thermostat wire is perfect. |
| **A multimeter** | $10–20 | Very helpful for checking voltages and your soldering. |

## Then pick ONE way to get the board

### Option A: ready-made PCB (no tiny soldering) ⭐ recommended

JLCPCB or PCBWay makes and assembles the board. You just plug in the XIAO.

| | Cost | Time |
|---|---|---|
| 5 assembled boards (JLCPCB, example quote) | about $25 + shipping (~$10–30) | about 1–2 weeks |
| 5 assembled boards (PCBWay, example quote) | about $40 shipped, final price after their review | about 1–2 weeks |

That's enough boards for you plus a few friends. See [Order the ready-made PCB](../hardware/order-pcb.md).

### Option B: build it on perfboard (cheapest, you solder)

**Dry-contact openers** only need:

| Part | Qty | Example |
|---|---|---|
| 2N7000 MOSFET (TO-92) | 1 | DigiKey 2N7000, or any electronics kit |
| 10 kΩ resistor | 1 | brown-black-orange |
| Perfboard (2.54 mm) | 1 small piece | |
| 2- or 3-pin 5.08 mm screw terminal (optional) | 1 | or solder wires directly |

**Security+ openers** also need:

| Part | Qty | Notes |
|---|---|---|
| AO3400A MOSFET (SOT-23) + SOT-23 to DIP adapter | 1 each | Tiny! The adapter makes it solderable. |
| 2N7000 | 1 | (instead of the 2N7002 on the PCB) |
| 10 kΩ resistors | 4 | |
| 1 kΩ resistor | 1 | |
| 100 kΩ resistor | 1 | |

See [Build it on perfboard](../hardware/perfboard.md).

## Optional: real open/closed status for dry-contact openers

| Part | Cost | Notes |
|---|---|---|
| **Wired magnetic reed switch** (garage-door type, normally open) | $5–12 | Mounts on the floor or track, and closes when the door is fully closed. Wires to SENSORS **CLOSED** + **GND**. |

Next: [Safety first →](safety.md)
