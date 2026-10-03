# Which opener do I have?

This decides which firmware you flash. The board is the same for all of them.

## 1. Find the "learn" button

Get on a step ladder and look at the opener motor unit on the ceiling. There's usually a small square **LEARN** button near the antenna wire, often under the light cover, with a small LED next to it. **Note its color.**

| Learn button color | Protocol | Firmware |
|---|---|---|
| **Yellow** | Security+ 2.0 (most LiftMaster / Chamberlain / Craftsman from about 2011 on, anything "myQ") | `garage-secplus2` |
| **Purple**, **red/orange** | Security+ 1.0 | `garage-secplus1` |
| **Green** | Billion Code (very old Chamberlain). Uses a plain wall button. | `garage-dry-contact` |
| **No learn button**, or another brand (Genie, Overhead Door, Linear, Ryobi, Skylink…) | Usually a simple 2-wire wall button | `garage-dry-contact` |

## 2. Check the wall button

Look at the button on the wall by the door into the house.

- **A plain doorbell-style button** with 2 thin wires usually means a **dry-contact** opener. Our test is in step 3.
- **A wall panel with several buttons** (light, lock, motion) on a LiftMaster or Chamberlain is **Security+** (2.0 or 1.0, by the learn button color).

> [!IMPORTANT]
> Some brands use "smart" wall buttons that send data, not a simple contact. If you're unsure, do the test below **before** buying anything.

## 3. The 30-second dry-contact test

With the opener plugged in, **briefly touch a short wire across the two wall-button terminals** on the back of the opener.

- **The door moves:** it's a dry-contact opener. ✅ Use `garage-dry-contact`.
- **Nothing happens:** it's a data-type wall control. Check the learn button color again, or ask in the [discussions](https://github.com/JamesSilvia20/xiao-garage-door/discussions) with a photo of your opener's label.

> [!TIP]
> Never done this before? The terminals are the screws or push-in slots where the wall-button wires connect, usually labelled with colors or numbers. The voltage there is low (usually 5–24 V DC) and safe to touch, but keep your fingers off the 120 V wiring inside the opener.

## Not sure? Take a photo

Take a photo of the opener's **label** (model number) and the **wall button**, and open a [discussion](https://github.com/JamesSilvia20/xiao-garage-door/discussions). Someone can tell you.

Next: [Parts and cost →](parts.md)
