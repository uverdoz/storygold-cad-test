import cadquery as cq
from cadquery import exporters

# Пирамида с плоской вершиной
solid = (
    cq.Workplane("XY")
    .polygon(4, 40)               # квадратное основание (4 стороны, радиус описанной окружности 40)
    .extrude(30)                   # высота 30
    .faces(">Z").workplane()       # верхняя грань
    .rect(20, 20)                  # плоская верхушка (20x20)
    .cutBlind(-10)                 # "срезаем" верхушку на глубину 10
)

# Пути к файлам
out_stl = "stl/02_pyramid_with_flat_top.stl"
out_step = "stl/02_pyramid_with_flat_top.step"
out_svg = "screenshots/02_pyramid_with_flat_top.png"

# Экспорт моделей
exporters.export(solid, out_stl, exporters.ExportTypes.STL)
exporters.export(solid, out_step, exporters.ExportTypes.STEP)
exporters.export(solid, out_svg, exporters.ExportTypes.SVG)

print("OK: pyramid STL, STEP и SVG сохранены!")
