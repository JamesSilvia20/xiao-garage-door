# Soldering 101 (for total beginners)

Never soldered before? Neither had the person who built the first one of these. Here's everything that tripped us up.

## Safety

- The iron tip is about **350 °C**. Always put it back in its stand.
- Work with some airflow; don't breathe the flux smoke.
- Wash your hands after handling solder.
- Wear glasses, because solder can flick.

## Your iron

- **A temperature-controlled iron** (for example a Pinecil, ~$30) heats up in seconds and makes life easy.
- **A basic plug-in iron** (for example a 25 W Weller) works for perfboard, but needs **3–5 minutes** to heat up.
- **"It takes forever to melt solder"** almost always means the tip isn't **tinned**. Melt solder straight onto the hot tip until the whole tip is shiny silver. Use the **side** of the tip, not the point.

**Flux-core solder is all you need.** Just add a little **fresh** solder to each joint, which brings fresh flux with it.

## Which side of the perfboard?

- **Parts go on the plain side.**
- **You solder on the side with the metal rings** around the holes.

If your board has metal rings on both sides, either side works.

## One joint, step by step

```
        leg (sticking up)
          |
   iron → |  ← solder
     _____|_____
    (  ring   )
```

1. Touch the iron so it touches **both the leg and the metal ring** at the same time. Hold 1–2 seconds.
2. Touch the solder to the **opposite side** of the leg, on the ring, not onto the iron.
3. Feed in about **3–5 mm** of solder. It flows around the leg.
4. Remove the solder, then the iron. **Don't move anything** for 3 seconds.
5. **A good joint is shiny and shaped like a small volcano.** A ball sitting on top means the ring wasn't hot enough; reheat with a touch of fresh solder.
6. Clip the extra leg.

## Connecting things on perfboard

Perfboard holes are **not connected to each other**. Every connection is either:
- a **bent leg** (bend a part's leg over to the next joint), or
- a **piece of solid wire** (the stiff breadboard jumper wires in most starter kits are perfect).

## Solder bridges (the #1 problem)

A **bridge** is solder accidentally joining two neighbouring pins. It causes very confusing symptoms; ours made a pin read 3.3 V all the time.

**Find them:** multimeter on continuity, test each pair of neighbouring pins. Neighbours should **not** beep (unless you connected them on purpose).

**Fix them:** wipe the tip clean, put it in the gap between the two pins, and **drag it away** from the part. The extra solder clings to the tip. If it won't let go, add a tiny bit of fresh solder (for the flux) and drag again.

## Cleaning the tip

- **While hot:** wipe on **brass wool** (best) or a **damp** sponge (damp, not wet), then re-tin immediately.
- **Black tip that won't take solder:** use **tip tinner** paste (~$8).
- **Don't use** sandpaper or files on the tip; it ruins the plating.
- Leave a blob of solder on the tip when you turn it off.

## The multimeter settings you'll use

| Setting | Symbol | Used for |
|---|---|---|
| **Continuity** | `)))` / 🔊 | Is it connected? A beep means yes. |
| **Ohms** | Ω | How connected? "OL" means open. |
| **DC volts** | V⎓ | Is the pin at 0 V or 3.3 V? |

The black probe goes in **COM**, the red probe in **VΩ** (not the 10 A jack). Touch the two probes together: continuity should beep.

Back to: [Build it on perfboard →](perfboard.md)
