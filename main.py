from pathlib import Path
import cadquery as cq
from cadquery import exporters


def build_plate(
    length=80,      # длина
    width=50,       # ширина
    thickness=6,    # толщина
    hole_d=6,       # диаметр отверстий
    offset=8,       # отступ отверстий от краёв
    fillet_r=2      # скругление вертикальных рёбер
):
    # базовый параллелепипед, лежит на плоскости Z=0
    wp = (
        cq.Workplane("XY")
        .box(length, width, thickness, centered=[True, True, False])
        .faces(">Z").workplane()                             # верхняя грань
        .rect(length - 2*offset, width - 2*offset)           # прямоуг. контур
        .vertices().hole(hole_d)                             # отверстия в 4-х углах контура
    )
    if fillet_r > 0:
        wp = wp.edges("|Z").fillet(fillet_r)                 # скругляем вертикальные рёбра
    return wp


if __name__ == "__main__":
    part = build_plate()                                     # можно менять параметры здесь

    out = Path("out")
    out.mkdir(exist_ok=True)
    exporters.export(part, str(out / "plate.step"))
    exporters.export(part, str(out / "plate.stl"))

    print(f"OK, сохранено в: {out.resolve()}")

    print(f"OK, сохранено в: {out.resolve()}")

import argparse
from pathlib import Path
import cadquery as cq
from cadquery import exporters

def parse_args():
    p = argparse.ArgumentParser(description="Generate a parametric plate and export STEP/STL")
    p.add_argument("--length", type=float, default=80, help="Length (mm)")
    p.add_argument("--width", type=float, default=50, help="Width (mm)")
    p.add_argument("--thickness", type=float, default=6, help="Thickness (mm)")
    p.add_argument("--hole-d", type=float, default=6, help="Hole diameter (mm)")
    p.add_argument("--offset", type=float, default=8, help="Hole offset from edges (mm)")
    p.add_argument("--fillet-r", type=float, default=2, help="Vertical edge fillet radius (mm)")
    p.add_argument("--outdir", type=str, default="out", help="Output directory")
    return p.parse_args()

if __name__ == "__main__":
    args = parse_args()
    part = build_plate(
        length=args.length,
        width=args.width,
        thickness=args.thickness,
        hole_d=args.hole_d,
        offset=args.offset,
        fillet_r=args.fillet_r,
    )
    out = Path(args.outdir)
    out.mkdir(exist_ok=True)
    exporters.export(part, str(out / "plate.step"))
    exporters.export(part, str(out / "plate.stl"))
    print(f"Saved: {out.resolve()}/plate.step and plate.stl")