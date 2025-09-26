import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import cadquery as cq
from main import build_plate

def test_build_plate_runs():
    part = build_plate(length=100, width=70, thickness=5, hole_d=5, offset=10, fillet_r=1)
    assert isinstance(part, cq.Workplane)
    assert part.val().Volume() > 0