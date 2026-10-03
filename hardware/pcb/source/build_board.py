"""Garage door carrier board for a Seeed XIAO ESP32-C6 (plugs into two 1x7 sockets).

One board for both doors:
  J1 OPENER  RED / WHITE / BLACK
     - Security+ 2.0 (MyQ LiftMaster): wire to the opener's red, white, black terminals.
     - Old "dumb" opener: RED -> wall-button +, WHITE -> wall-button common (BLACK unused).
  J2 SENSORS CLOSED / OPEN / GND  (reed switches to GND, optional)

XIAO pins (same as the hand-built boards):
  D2 GPIO2  -> Q1 AO3400A gate (send / press), R1 10k gate pull-down
  D3 GPIO21 <- Q2 2N7002 drain (receive, inverted), R2 10k pull-up; gate <- RED via R3 1k, R4 100k pull-down
  D5 GPIO23 <- BLACK via R5/R6 10k/10k divider (obstruction)
  D4 GPIO22 <- CLOSED via R9 1k, R7 10k pull-up, C1 100nF
  D1 GPIO1  <- OPEN   via R10 1k, R8 10k pull-up, C2 100nF

Run with KiCad's Python:  build_board.py  ->  garage_door.kicad_pcb (unrouted; see route.sh)
Coordinates in mm, KiCad frame (x right, y down). USB-C of the XIAO points to the top edge.
"""
import os
import pcbnew

HERE = os.path.dirname(os.path.abspath(__file__))
FP = os.path.expanduser('~/Applications/KiCad/KiCad.app/Contents/SharedSupport/footprints')
OUT = os.path.join(HERE, 'garage_door.kicad_pcb')

W, H = 56.0, 48.0           # board size
XL, XR = 13.0, 13.0 + 15.24  # XIAO socket columns
Y0 = 4.0                     # first XIAO pin (USB end)

board = pcbnew.CreateEmptyBoard()
board.SetCopperLayerCount(2)
mm = pcbnew.FromMM
nets = {}


def net(name):
    if name not in nets:
        n = pcbnew.NETINFO_ITEM(board, name)
        board.Add(n)
        nets[name] = n
    return nets[name]


def place(lib, name, ref, value, x, y, rot=0.0, lcsc=None, side_bottom=False):
    fp = pcbnew.FootprintLoad(os.path.join(FP, lib + '.pretty'), name)
    fp.SetReference(ref)
    fp.SetValue(value)
    fp.SetPosition(pcbnew.VECTOR2I(mm(x), mm(y)))
    fp.SetOrientationDegrees(rot)
    if lcsc:
        fp.SetField('LCSC', lcsc)
    board.Add(fp)
    return fp


def connect(fp, pad, netname):
    for p in fp.Pads():
        if p.GetNumber() == str(pad):
            p.SetNet(net(netname))
            return
    raise KeyError('%s pad %s' % (fp.GetReference(), pad))


def text(s, x, y, size=1.0, layer=pcbnew.F_SilkS, bold=False):
    t = pcbnew.PCB_TEXT(board)
    t.SetText(s)
    t.SetPosition(pcbnew.VECTOR2I(mm(x), mm(y)))
    t.SetLayer(layer)
    t.SetTextSize(pcbnew.VECTOR2I(mm(size), mm(size)))
    t.SetTextThickness(mm(size * (0.2 if bold else 0.15)))
    board.Add(t)


def line(x0, y0, x1, y1, layer=pcbnew.F_SilkS, w=0.15):
    s = pcbnew.PCB_SHAPE(board)
    s.SetShape(pcbnew.SHAPE_T_SEGMENT)
    s.SetStart(pcbnew.VECTOR2I(mm(x0), mm(y0)))
    s.SetEnd(pcbnew.VECTOR2I(mm(x1), mm(y1)))
    s.SetLayer(layer)
    s.SetWidth(mm(w))
    board.Add(s)


def rect(x0, y0, x1, y1, layer, w=0.15):
    for a, b, c, d in ((x0, y0, x1, y0), (x1, y0, x1, y1), (x1, y1, x0, y1), (x0, y1, x0, y0)):
        line(a, b, c, d, layer, w)


# ---------------------------------------------------------------- outline + holes
rect(0, 0, W, H, pcbnew.Edge_Cuts, 0.1)
for i, (x, y) in enumerate(((3.5, 3.5), (W - 3.5, 3.5), (3.5, H - 3.5), (W - 3.5, H - 3.5))):
    place('MountingHole', 'MountingHole_3.2mm_M3', 'H%d' % (i + 1), 'M3', x, y)

# ---------------------------------------------------------------- XIAO sockets
left = ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6']          # USB end first
right = ['5V', 'GND', '3V3', 'D10', 'D9', 'D8', 'D7']
J3 = place('Connector_PinSocket_2.54mm', 'PinSocket_1x07_P2.54mm_Vertical', 'J3', 'XIAO L', XL, Y0, lcsc='C2932672')
J4 = place('Connector_PinSocket_2.54mm', 'PinSocket_1x07_P2.54mm_Vertical', 'J4', 'XIAO R', XR, Y0, lcsc='C2932672')
pin_net = {'D1': 'OPEN_IN', 'D2': 'TX', 'D3': 'RX', 'D4': 'CLOSED_IN', 'D5': 'OBST', 'GND': 'GND', '3V3': '+3V3'}
for i, n in enumerate(left):
    if n in pin_net:
        connect(J3, i + 1, pin_net[n])
for i, n in enumerate(right):
    if n in pin_net:
        connect(J4, i + 1, pin_net[n])

# ---------------------------------------------------------------- terminals (wire entry toward the bottom edge)
# Footprint body spans y -5.2..+4.6 around the pads, wire entry on +y: put the front flush with the edge.
TY = H - 4.9
J1X, J2X = 10.5, 30.0
J1 = place('TerminalBlock_Phoenix', 'TerminalBlock_Phoenix_MKDS-1,5-3-5.08_1x03_P5.08mm_Horizontal',
           'J1', 'OPENER', J1X, TY, lcsc='C474953')
J2 = place('TerminalBlock_Phoenix', 'TerminalBlock_Phoenix_MKDS-1,5-3-5.08_1x03_P5.08mm_Horizontal',
           'J2', 'SENSORS', J2X, TY, lcsc='C474953')
for p, n in ((1, 'RED'), (2, 'GND'), (3, 'BLACK')):
    connect(J1, p, n)
for p, n in ((1, 'CLOSED'), (2, 'OPEN'), (3, 'GND')):
    connect(J2, p, n)

# ---------------------------------------------------------------- send + receive (right of the XIAO)
SOT, R0603, C0603 = ('Package_TO_SOT_SMD', 'SOT-23'), ('Resistor_SMD', 'R_0603_1608Metric'), ('Capacitor_SMD', 'C_0603_1608Metric')
cx = 37.0
Q1 = place(*SOT, 'Q1', 'AO3400A', cx, 9.0, lcsc='C20917')
R1 = place(*R0603, 'R1', '10k', cx + 6.0, 9.0, 90, lcsc='C25804')
Q2 = place(*SOT, 'Q2', '2N7002', cx, 16.0, lcsc='C8545')
R2 = place(*R0603, 'R2', '10k', cx + 6.0, 16.0, 90, lcsc='C25804')
R3 = place(*R0603, 'R3', '1k', cx - 4.0, 19.5, 0, lcsc='C21190')
R4 = place(*R0603, 'R4', '100k', cx + 2.0, 19.5, 0, lcsc='C25803')
R5 = place(*R0603, 'R5', '10k', cx - 4.0, 24.0, 0, lcsc='C25804')
R6 = place(*R0603, 'R6', '10k', cx + 2.0, 24.0, 0, lcsc='C25804')
for fp, a, b in ((Q1, None, None),):
    pass
# AO3400A / 2N7002 SOT-23: 1 = G, 2 = S, 3 = D
connect(Q1, 1, 'TX'); connect(Q1, 2, 'GND'); connect(Q1, 3, 'RED')
connect(R1, 1, 'TX'); connect(R1, 2, 'GND')
connect(Q2, 1, 'RX_G'); connect(Q2, 2, 'GND'); connect(Q2, 3, 'RX')
connect(R2, 1, '+3V3'); connect(R2, 2, 'RX')
connect(R3, 1, 'RED'); connect(R3, 2, 'RX_G')
connect(R4, 1, 'RX_G'); connect(R4, 2, 'GND')
connect(R5, 1, 'BLACK'); connect(R5, 2, 'OBST')
connect(R6, 1, 'OBST'); connect(R6, 2, 'GND')

# ---------------------------------------------------------------- sensor inputs
R9 = place(*R0603, 'R9', '1k', cx - 4.0, 28.0, 0, lcsc='C21190')
R7 = place(*R0603, 'R7', '10k', cx + 2.0, 28.0, 0, lcsc='C25804')
C1 = place(*C0603, 'C1', '100nF', cx + 7.0, 28.0, 0, lcsc='C14663')
R10 = place(*R0603, 'R10', '1k', cx - 4.0, 31.5, 0, lcsc='C21190')
R8 = place(*R0603, 'R8', '10k', cx + 2.0, 31.5, 0, lcsc='C25804')
C2 = place(*C0603, 'C2', '100nF', cx + 7.0, 31.5, 0, lcsc='C14663')
C3 = place(*C0603, 'C3', '100nF', cx + 7.0, 22.0, 90, lcsc='C14663')
connect(R9, 1, 'CLOSED'); connect(R9, 2, 'CLOSED_IN')
connect(R7, 1, 'CLOSED_IN'); connect(R7, 2, '+3V3')
connect(C1, 1, 'CLOSED_IN'); connect(C1, 2, 'GND')
connect(R10, 1, 'OPEN'); connect(R10, 2, 'OPEN_IN')
connect(R8, 1, 'OPEN_IN'); connect(R8, 2, '+3V3')
connect(C2, 1, 'OPEN_IN'); connect(C2, 2, 'GND')
connect(C3, 1, '+3V3'); connect(C3, 2, 'GND')

# ---------------------------------------------------------------- silkscreen
xm = (XL + XR) / 2
rect(XL - 2.4, Y0 - 3.4, XR + 2.4, Y0 + 17.6, pcbnew.F_SilkS)       # XIAO outline (21 x 17.5)
rect(xm - 4.6, Y0 - 3.9, xm + 4.6, Y0 - 0.9, pcbnew.F_SilkS)        # USB-C marker
text('USB-C', xm, Y0 + 1.6, 0.9)
text('XIAO C6', xm, Y0 + 7.6, 1.0, bold=True)
text('CHIPS UP', xm, Y0 + 11.4, 0.8)
for i, n in enumerate(left):
    text(n, XL + 2.7, Y0 + i * 2.54, 0.8)
for i, n in enumerate(right):
    text(n, XR - 3.0, Y0 + i * 2.54, 0.8)
text('GARAGE DOOR v1', 15.0, 27.0, 1.2, bold=True)
text('Security+ 2.0 / dry contact', 15.0, 29.4, 0.8)
text('SEND', cx, 6.0, 0.8)
text('RECV', cx, 13.0, 0.8)
text('OBST', cx - 1.0, 25.8, 0.8)
text('OPENER', J1X + 5.08, TY - 8.2, 0.9, bold=True)
text('SENSORS', J2X + 5.08, TY - 8.2, 0.9, bold=True)
for i, n in enumerate(('RED', 'WHT', 'BLK')):
    text(n, J1X + i * 5.08, TY - 6.4, 0.9)
for i, n in enumerate(('CLOSED', 'OPEN', 'GND')):
    text(n, J2X + i * 5.08, TY - 6.4, 0.8)

# ---------------------------------------------------------------- design rules / net classes
ds = board.GetDesignSettings()
ds.m_TrackMinWidth = mm(0.2)
ds.m_MinClearance = mm(0.2)
ds.m_ViasMinSize = mm(0.6)
ds.m_MinThroughDrill = mm(0.3)
nc = ds.m_NetSettings.GetDefaultNetclass()
nc.SetTrackWidth(mm(0.3))
nc.SetClearance(mm(0.25))
nc.SetViaDiameter(mm(0.7))
nc.SetViaDrill(mm(0.35))

for fp in board.GetFootprints():
    fp.Reference().SetVisible(False)   # labels are printed explicitly; JLC assembles by position
    for f in fp.GetFields():
        if f.GetName() == 'LCSC':
            f.SetVisible(False)

board.BuildConnectivity()
pcbnew.SaveBoard(OUT, board)
print('saved', OUT, 'nets', len(nets))
for fp in board.GetFootprints():
    bb = fp.GetCourtyard(pcbnew.F_CrtYd).BBox() if fp.GetCourtyard(pcbnew.F_CrtYd).OutlineCount() else fp.GetBoundingBox()
    print('%-4s %-8s pos (%.2f, %.2f) bbox x %.2f..%.2f y %.2f..%.2f' % (
        fp.GetReference(), fp.GetValue(), pcbnew.ToMM(fp.GetPosition().x), pcbnew.ToMM(fp.GetPosition().y),
        pcbnew.ToMM(bb.GetLeft()), pcbnew.ToMM(bb.GetRight()), pcbnew.ToMM(bb.GetTop()), pcbnew.ToMM(bb.GetBottom())))
