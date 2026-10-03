#!/bin/bash
# Rebuild, autoroute, pour and check the garage door board.
set -eo pipefail
cd "$(dirname "$0")"
PY=~/Applications/KiCad/KiCad.app/Contents/Frameworks/Python.framework/Versions/3.9/bin/python3
K=~/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli
J=$(brew --prefix openjdk)/bin/java
$PY build_board.py 2>&1 | grep -v assert | head -1
$PY route.py export 2>&1 | grep -v assert
$J -Djava.awt.headless=true -jar ~/.cache/freerouting/freerouting.jar -de garage_door.dsn -do garage_door.ses -mp 20 --gui.enabled=false > fr.log 2>&1
grep -o "final score: .*violations)" fr.log | tail -1
$PY route.py import 2>&1 | grep -v assert
$K pcb drc --severity-all --refill-zones --save-board --format json -o drc.json garage_door.kicad_pcb | tail -2
