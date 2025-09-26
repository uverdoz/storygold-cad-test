import cadquery as cq
from cadquery import exporters
from pathlib import Path

# коробка с круглым отверстием в центре
solid = (
    cq.Workplane("XY")
    .box(60, 40, 20, centered=[True, True, False])
    .faces(">Z").workplane()
    .hole(10)  # отверстие диаметром 10 мм
)

# экспорт
out_stl = Path("stl/02_box_with_hole.stl")
out_step = Path("stl/02_box_with_hole.step")
out_svg = Path("screenshots/02_box_with_hole.svg")

exporters.export(solid, str(out_stl), exporters.ExportTypes.STL)
exporters.export(solid, str(out_step), exporters.ExportTypes.STEP)
exporters.export(solid, str(out_svg), exporters.ExportTypes.SVG)
