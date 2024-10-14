"""
Masks: used to represent the "solid" or "non-transparent" parts of a surface

Uses cases:
- Pixel perfect collision
- outlines
- silhouettes
- effects using setcolorkey, unset color key
- overlaps
- shadows & glows
- centroids (geometric center of an object's shape / average position of all the "solid" or non-transparent pixels in a mask / point where the object could be perfectly balanced if it were a physical object
"""