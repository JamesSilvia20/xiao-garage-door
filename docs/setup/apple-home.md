# Add to Apple Home

The board talks to Home Assistant. Home Assistant's **HomeKit Bridge** then shows it in Apple Home as a real **garage door** tile, with Siri ("Hey Siri, close the garage"), Control Center and automations.

## Easiest: from the HA screens

1. In Home Assistant: **Settings → Devices & services → Add integration → HomeKit Bridge**.
2. Choose **Accessory mode** and pick your garage door's **cover** entity (for example `cover.garage_door_door`).
   - Accessory mode gives the door its own Apple Home tile, just like a store-bought opener.
3. A **"HomeKit Pairing"** notification appears in HA with a QR code.
4. On your iPhone: **Home app → + → Add Accessory**, then scan that QR code. If it says "Uncertified Accessory", tap **Add Anyway**.
5. Pick a room.

## Or: YAML (if you already use `homekit:` in configuration.yaml)

```yaml
homekit:
  - name: Garage Door
    mode: accessory
    port: 21066            # any free port, different from your other HomeKit bridges
    filter:
      include_entities:
        - cover.garage_door_door
    entity_config:
      cover.garage_door_door:
        name: Garage Door
```

Restart Home Assistant, then pair from the notification as above.

## Notes

- Apple Home garage doors are **only open or closed**. There's no position slider, even on commercial openers.
- **Opening from outside the house** works through your Apple home hub (HomePod or Apple TV).
- Apple asks you to unlock your iPhone before opening a garage door. That's normal security.

Next: [Install it at the opener →](install.md)
