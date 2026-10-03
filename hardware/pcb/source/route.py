"""Autoroute garage_door.kicad_pcb with freerouting, then add GND pours on both layers.

Usage (KiCad's Python): route.py export   -> garage_door.dsn
                        (run freerouting on the .dsn -> garage_door.ses)
                        route.py import   -> routes + GND zones, saved in place
"""
import os
import sys
import pcbnew

HERE = os.path.dirname(os.path.abspath(__file__))
PCB = os.path.join(HERE, 'garage_door.kicad_pcb')
DSN = os.path.join(HERE, 'garage_door.dsn')
SES = os.path.join(HERE, 'garage_door.ses')
mm = pcbnew.FromMM

board = pcbnew.LoadBoard(PCB)

if sys.argv[1] == 'export':
    # GND is left to the pours, so the router only connects the signal nets
    ok = pcbnew.ExportSpecctraDSN(board, DSN)
    print('dsn', ok)
    sys.exit(0)

ok = pcbnew.ImportSpecctraSES(board, SES)
print('ses import', ok)

gnd = board.FindNet('GND')
bb = board.GetBoardEdgesBoundingBox()
for layer in (pcbnew.F_Cu, pcbnew.B_Cu):
    z = pcbnew.ZONE(board)
    z.SetLayer(layer)
    z.SetNet(gnd)
    z.SetLocalClearance(mm(0.3))
    z.SetMinThickness(mm(0.25))
    z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL)
    z.SetThermalReliefGap(mm(0.3))
    z.SetThermalReliefSpokeWidth(mm(0.4))
    o = z.Outline()
    o.NewOutline()
    for x, y in ((bb.GetLeft(), bb.GetTop()), (bb.GetRight(), bb.GetTop()),
                 (bb.GetRight(), bb.GetBottom()), (bb.GetLeft(), bb.GetBottom())):
        o.Append(x, y)
    board.Add(z)

filler = pcbnew.ZONE_FILLER(board)
filler.Fill(board.Zones())
board.BuildConnectivity()
pcbnew.SaveBoard(PCB, board)
tracks = [t for t in board.GetTracks() if t.GetClass() == 'PCB_TRACK']
vias = [t for t in board.GetTracks() if t.GetClass() == 'PCB_VIA']
print('tracks', len(tracks), 'vias', len(vias), 'unrouted', board.GetConnectivity().GetUnconnectedCount(True))
