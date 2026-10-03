# XIAO Garage Door 🚗🏠

**Make your garage door opener smart for about $10 in parts.** This is a tiny open-source board that holds a [Seeed Studio XIAO ESP32-C6](https://www.seeedstudio.com/Seeed-Studio-XIAO-ESP32C6-p-5884.html) and wires to your opener's wall-button terminals. You can then open and close your garage from **Home Assistant**, **Apple Home** (with Siri and automations), or anything else that talks to [ESPHome](https://esphome.io).

No cloud, no subscription, no app from the opener company. Everything runs on your own network.

<p align="center">
  <img src="hardware/pcb/images/render_top.png" alt="XIAO Garage Door PCB" width="520">
</p>

## What it does

| Your opener | What you get |
|---|---|
| **Security+ 2.0** (LiftMaster / Chamberlain / Craftsman with a **yellow** learn button, the myQ kind) | Real open / closed / opening / closing status, light, lock, obstruction alerts and motion, read straight from the opener. |
| **Security+ 1.0** (same brands, **purple / red / orange** learn button) | Same as above. |
| **Any opener with a simple 2-wire wall button** (most other brands, older units) | Open / close / stop from your phone. Add a $5 magnetic reed switch for true open/closed status. |

One board does all of these. You pick the matching firmware.

## Start here 👇

New to this? Follow the guides in order. They're written for complete beginners, and we explain every step.

1. 🔍 [**Which opener do I have?**](docs/start/which-opener.md): pick your firmware in 2 minutes.
2. 🛒 [**Parts and cost**](docs/start/parts.md): everything you need, with links.
3. ⚠️ [**Safety first**](docs/start/safety.md): please read this one.
4. 🔧 Get the hardware, either way:
   - [**Order the ready-made PCB**](docs/hardware/order-pcb.md) from JLCPCB or PCBWay, all parts soldered for you, about $25–40 for 5 boards; **or**
   - [**Build it on perfboard**](docs/hardware/perfboard.md) with a few cheap parts (new to soldering? see [**Soldering 101**](docs/hardware/soldering-101.md)).
5. ⚡ [**Flash the firmware**](docs/setup/flash.md): straight from your web browser, no software to install.
6. 🏠 [**Add to Home Assistant**](docs/setup/home-assistant.md) and [**Apple Home**](docs/setup/apple-home.md).
7. 🪛 [**Install it at the opener**](docs/setup/install.md).

Stuck? See [**Troubleshooting**](docs/help/troubleshooting.md) and the [**FAQ**](docs/help/faq.md).

> [!TIP]
> Prefer a website? The same guides are at **https://jamessilvia20.github.io/xiao-garage-door/**, and that's where the one-click **browser installer** lives.

## What's in this repo

```
firmware/        ESPHome configs (one per opener type) - flash from the browser or adopt in ESPHome
hardware/pcb/    The PCB: KiCad board, scripts that build it, and ready-to-upload JLCPCB / PCBWay files
docs/            All the tutorials (this is also the website)
```

## Project status

Honest status, so you know what's been tested:

| Part | Status |
|---|---|
| Dry-contact firmware + hand-built perfboard | ✅ Built and bench-tested by the author (switches the wall-button contacts on command, shows up in HA and Apple Home). |
| Security+ 2.0 / 1.0 firmware | ✅ Compiles for the XIAO C6, using the proven [esphome-ratgdo](https://github.com/ratgdo/esphome-ratgdo) component and the community [rat-ratgdo](https://github.com/Kaldek/rat-ratgdo) circuit. 🧪 Not yet tested by the author on this exact board. Reports welcome! |
| PCB v1 | 🧪 Design passes KiCad DRC with 0 errors, and the JLCPCB/PCBWay files are generated. First boards are on order. |

Built one? Please open an issue or discussion with how it went (photos welcome!), so we can turn the 🧪s into ✅s.

## Credits

This stands on the shoulders of [**ratgdo**](https://github.com/ratgdo) (Paul Wieland and contributors), [**rat-ratgdo**](https://github.com/Kaldek/rat-ratgdo), [**esphome-ratgdo**](https://github.com/ratgdo/esphome-ratgdo), [**ESPHome**](https://esphome.io) and [**Home Assistant**](https://www.home-assistant.io). If you want a polished, ready-made product, buy an official [ratgdo](https://ratcloud.llc). It's great and supports the people who figured all this out.

See [Credits and license](docs/makers/credits.md).

## License

[MIT](LICENSE) for everything in this repo (firmware configs, PCB, docs). The Security+ firmware pulls in esphome-ratgdo, which is GPL-2.0.

> [!WARNING]
> Garage doors are heavy and can hurt people. Keep your photo-eye safety sensors connected and working. Never close the door remotely unless you can be sure nobody is under it. See [Safety first](docs/start/safety.md).
