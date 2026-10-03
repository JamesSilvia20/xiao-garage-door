# FAQ

**Does this replace my wall button and remotes?**
No. They all keep working. The board just adds a "virtual" wall button (and, on Security+, reads the opener's status).

**Does it need the internet or a cloud account?**
No. It runs locally on your Wi-Fi with Home Assistant. For Apple Home access from outside the house you need an Apple home hub (HomePod or Apple TV), like any HomeKit device.

**Can I use it without Home Assistant?**
The firmware is ESPHome, which is designed for Home Assistant. It also has a tiny built-in web page on Security+ builds. For native HomeKit with no Home Assistant, look at [homekit-ratgdo32](https://github.com/ratgdo/homekit-ratgdo32).

**Why a XIAO ESP32-C6?**
It's tiny, cheap (about $5), has Wi-Fi 6 and USB-C, and it **plugs into sockets**, so you can swap or reflash it easily.

**Can I open the door partway?**
Apple Home garage doors are open/closed only. Single-button (dry-contact) openers can't reliably stop at a position without a sensor, because each press cycles open → stop → close → stop.

**Is it safe?**
It's as safe as your wall button, as long as your **photo-eye sensors stay connected** and you follow [Safety first](../start/safety.md).

**How is this different from a ratgdo?**
It's the same idea and the same community circuit, adapted to a plug-in XIAO with fully open PCB files you can order yourself. If you want a finished, supported product, [buy a ratgdo](https://ratcloud.llc) and support the folks who made this possible.

**Can I change the PCB?**
Yes! The whole board is generated from a Python script. See [Edit the PCB](../makers/edit-pcb.md).
