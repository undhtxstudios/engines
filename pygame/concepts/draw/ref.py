"""
Rectangle: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect

Rectangle / pygame.draw.rect() / draw a rectangle
    rect(surface, color, rect) -> Rect
    rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1) -> Rect

width (int) -- optional -- used for line thickness or to indicate that the rectangle is to be filled
    if width == 0, (default) fill the rectangle
    if width > 0, used for line thickness
    if width < 0, nothing will be drawn

if border_radius < 1 it will draw rectangle without rounded corners
if any of border radii has the value < 0 it will use value of the border_radius
If sum of radii on the same side of the rectangle is greater than the rect size the radii will get scaled

Returns
    a rect bounding the changed pixels, if nothing is drawn the bounding rect's position will be the position of the given rect parameter and its width and height will be 0

Return type
Rect
"""


"""
Polygon: https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon

Polygon / pygame.draw.polygon() / draw a polygon
    polygon(surface, color, points) -> Rect
    polygon(surface, color, points, width=0) -> Rect

points
    tuple/list/vector -- a sequence of 3 or more (x, y) coordinates

width (int)
    if width == 0, (default) fill the polygon
    if width > 0, used for line thickness
    if width < 0, nothing will be drawn

Returns
Rect, a rect bounding the changed pixels

Raises
ValueError -- if len(points) < 3 (must have at least 3 points)
TypeError -- if points is not a sequence or points does not contain number pairs
"""

