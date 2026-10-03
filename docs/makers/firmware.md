# Firmware reference

All firmware is plain [ESPHome](https://esphome.io) YAML in [`firmware/`](https://github.com/JamesSilvia20/xiao-garage-door/tree/main/firmware).

| File | Notes |
|---|---|
| `garage-secplus2.yaml` | Pulls in [esphome-ratgdo](https://github.com/ratgdo/esphome-ratgdo) `base.yaml` with this board's pins |
| `garage-secplus1.yaml` | Same, with `base_secplusv1.yaml` |
| `garage-dry-contact.yaml` | `time_based` cover with assumed state, plus a "Press Wall Button" button |
| `garage-dry-contact-sensor.yaml` | `template` cover whose state comes from the CLOSED reed switch |

## Pin map

| XIAO | GPIO | Function |
|---|---|---|
| D2 | GPIO2 | Send / press (Q1 gate) |
| D3 | GPIO21 | Receive (Q2 drain, inverted) |
| D5 | GPIO23 | Obstruction (BLACK through a ÷2 divider) |
| D4 | GPIO22 | SENSORS CLOSED |
| D1 | GPIO1 | SENSORS OPEN |
| (internal) | GPIO3, GPIO14 | Antenna switch, both held low (built-in antenna) |

## Substitutions you might change

| Name | Default | |
|---|---|---|
| `name` | `garage-door` | The device hostname gets a MAC suffix added |
| `friendly_name` | `Garage Door` | |
| `travel_time` | `13s` | Dry contact only: your door's full open time |

## Building the binaries yourself

```bash
pip install esphome
esphome compile firmware/garage-dry-contact.yaml
```

The prebuilt `.factory.bin` files used by the browser installer are in `docs/install/firmware/`. The GitHub Action in `.github/workflows/firmware.yml` compiles every config on each push.
