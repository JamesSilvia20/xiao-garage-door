"""Write JLCPCB assembly files (BOM + CPL) from garage_door.kicad_pcb.

Positions are pad centroids (what JLC expects as "Mid X/Y"). Rotation offsets follow the common
KiCad -> JLC corrections; always confirm part orientation in JLC's placement preview.
"""
import csv
import os
import re
from collections import defaultdict

import pcbnew

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'jlcpcb')
board = pcbnew.LoadBoard(os.path.join(HERE, 'garage_door.kicad_pcb'))
ROT_FIX = [(r'^SOT-23$', 180.0)]

bom = defaultdict(list)
rows = []
for fp in board.GetFootprints():
    lcsc = ''
    for f in fp.GetFields():
        if f.GetName() == 'LCSC':
            lcsc = f.GetText()
    if not lcsc:
        continue                      # mounting holes
    pads = list(fp.Pads())
    xs = [pcbnew.ToMM(p.GetPosition().x) for p in pads]
    ys = [pcbnew.ToMM(p.GetPosition().y) for p in pads]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    name = fp.GetFPID().GetLibItemName().wx_str()
    rot = fp.GetOrientationDegrees()
    for pat, off in ROT_FIX:
        if re.match(pat, name):
            rot = (rot + off) % 360
    ref = fp.GetReference()
    rows.append((ref, '%.3fmm' % cx, '%.3fmm' % -cy, 'Top', '%g' % rot))
    bom[(fp.GetValue(), name, lcsc)].append(ref)

key = lambda r: (re.sub(r'\d', '', r), int(re.sub(r'\D', '', r) or 0))
with open(os.path.join(OUT, 'garage_door_cpl.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Designator', 'Mid X', 'Mid Y', 'Layer', 'Rotation'])
    for r in sorted(rows, key=lambda r: key(r[0])):
        w.writerow(r)
with open(os.path.join(OUT, 'garage_door_bom.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Comment', 'Designator', 'Footprint', 'LCSC Part #'])
    for (val, name, lcsc), refs in sorted(bom.items(), key=lambda kv: key(sorted(kv[1], key=key)[0])):
        w.writerow([val, ','.join(sorted(refs, key=key)), name, lcsc])
print(open(os.path.join(OUT, 'garage_door_bom.csv')).read())
print(open(os.path.join(OUT, 'garage_door_cpl.csv')).read())
