import cadquery as cq

# прямоугольная коробка со скруглением
solid = (
    cq.Workplane("XY")
    .box(60, 40, 20, centered=[True, True, False])  # лежит на плоскости Z=0
    .edges("|Z").fillet(5)                           # скругляем вертикальные рёбра
)

from cadquery import exporters

exporters.export(solid, "stl/01_basic_rounded_box.stl")
exporters.export(solid, "stl/01_basic_rounded_box.step")

from cadquery import exporters
exporters.export(solid, "screenshots/01_basic_rounded_box.svg", exportType='SVG')