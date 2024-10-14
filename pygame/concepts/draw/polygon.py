from enum import Enum
import pygame

class PolygonConstant(Enum):
    DEFAULT_WIDTH = 0
    COLOR = "COLOR"
    POINTS = "POINTS"
    WIDTH = "WIDTH"

def draw_polygon(surface, color, points, width=PolygonConstant.DEFAULT_WIDTH.value):
    return pygame.draw.polygon(surface, color, points, width)

def draw_polygons(surface, polygons):
    for polygon in polygons:
        draw_polygon(
            surface,
            polygon[PolygonConstant.COLOR.value],
            polygon[PolygonConstant.POINTS.value],
            polygon.get(PolygonConstant.WIDTH.value, PolygonConstant.DEFAULT_WIDTH.value),
        )
