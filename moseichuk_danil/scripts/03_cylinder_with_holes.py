import cadquery as cq
from cadquery import exporters
from pathlib import Path

# цилиндр с отверстиями по окружности
solid = (
    cq.Workplane("XY")
    .circle(30)         # основание цилиндра, диаметр 60 мм
    .extrude(20)        # высота 20 мм
    .faces(">Z").workplane()
    .polarArray(0, 0, 360, 6)  # 6 отверстий по окружности
    .hole(5)            # отверстия диаметром 5 мм
)

# экспорт
out_stl = Path("stl/03_cylinder_with_holes.stl")
out_step = Path("stl/03_cylinder_with_holes.step")
out_svg = Path("screenshots/03_cylinder_with_holes.svg")

exporters.export(solid, str(out_stl), exporters.ExportTypes.STL)
exporters.export(solid, str(out_step), exporters.ExportTypes.STEP)
exporters.export(solid, str(out_svg), exporters.ExportTypes.SVG)
