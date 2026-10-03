# Safety first ⚠️

A garage door weighs 70–200 kg (150–400 lb). Please take these seriously.

- **Keep the photo-eye safety sensors connected and working.** Never bypass them. The opener reverses when the beam is broken. That's your main protection, and this project doesn't change it.
- **Remote closing is risky.** Don't make automations that close the door when nobody can see it, unless the opener flashes and beeps before moving (many newer openers do this by themselves).
- **Unplug the opener before connecting wires** to its terminals. The low-voltage terminals are safe, but the opener has 120/230 V inside. Don't open the motor cover.
- **Measure before you connect.** Check the wall-button / wall-control voltage with a multimeter first ([Install at the opener](../setup/install.md) shows how). Our board is designed for the low-voltage DC found on these terminals (about 5–24 V). If you see AC or anything higher, stop and ask.
- **Test the door's auto-reverse** once a month: put a 2×4 flat on the floor under the door and close it. The door must reverse when it touches the board.
- **Kids:** don't put a garage button where small children can reach it in an app or widget.

> [!CAUTION]
> This is a hobby project, provided as-is with no warranty (see the [license](https://github.com/JamesSilvia20/xiao-garage-door/blob/main/LICENSE)). You're responsible for installing it safely.

Next: get the hardware, either [order the ready-made PCB](../hardware/order-pcb.md) or [build it on perfboard](../hardware/perfboard.md).
