"""
https://www.pygame.org/docs/ref/surface.html

pygame.surface.blit(source, dest, area=none, special_flags=0) -> rect
    draws the source surface onto this surface at the position given by dest
    if area is provided, only the portion of the source surface defined by the area rect will be blitted

pygame.surface.blits(blit_sequence, doreturn=false, special_flags=0) -> list of rect
    draws a sequence of images onto this surface. the blit_sequence is a list of tuples (source, dest)

pygame.surface.convert(surface=none) -> surface
    changes the pixel format of an image without per-pixel alphas to match the format of the display surface

pygame.surface.convert_alpha(surface=none) -> surface
    changes the pixel format of an image including per-pixel alphas

pygame.surface.copy() -> surface
    creates a new copy of a surface

pygame.surface.fill(color, rect=none, special_flags=0) -> rect
    fills the surface with a solid color if rect is provided, only that area of the surface is filled

pygame.surface.scroll(dx, dy) -> rect
    shifts the surface image in place by dx, dy pixels

pygame.surface.set_colorkey(color, flags=0) -> none
    sets the color key for the surface. pixels matching the color key will be transparent

pygame.surface.get_colorkey() -> color
    gets the current transparent colorkey

pygame.surface.set_alpha(value, flags=0) -> none
    sets the alpha value for the entire surface
    an alpha of 255 is fully opaque, and 0 is fully transparent

pygame.surface.get_alpha() -> int or none
    gets the current surface transparency value

pygame.surface.lock() -> none
    locks the surface memory for pixel access

pygame.surface.unlock() -> none
    unlocks the surface memory from pixel access

pygame.surface.mustlock() -> bool
    tests if the surface requires locking

pygame.surface.get_locked() -> bool
    tests if the surface is currently locked

pygame.surface.get_locks() -> tuple
    gets the locks for the surface

pygame.surface.get_at(pos) -> color
    gets the color value at a specific pixel on the surface

pygame.surface.set_at(pos, color) -> none
    sets the color value of a specific pixel on the surface

pygame.surface.get_at_mapped(pos) -> int
    gets the mapped color value at a specific pixel

pygame.surface.get_palette() -> list
    gets the color index palette for an 8-bit surface

pygame.surface.get_palette_at(index) -> color
    gets the color for a single entry in a palette

pygame.surface.set_palette(palette) -> none
    sets the color palette for an 8-bit surface

pygame.surface.set_palette_at(index, color) -> none
    sets the color for a single index in an 8-bit surface palette

pygame.surface.map_rgb(color) -> int
    converts a color into a mapped color value

pygame.surface.unmap_rgb(mapped_color) -> color
    converts a mapped integer color value into a color

pygame.surface.set_clip(rect) -> none
    sets the current clipping area of the surface

pygame.surface.get_clip() -> rect
    gets the current clipping area of the surface

pygame.surface.subsurface(rect) -> surface
    creates a new surface that references its parent

pygame.surface.get_parent() -> surface
    finds the parent of a subsurface

pygame.surface.get_abs_parent() -> surface
    finds the top-level parent of a subsurface

pygame.surface.get_offset() -> (x, y)
    finds the position of a child subsurface inside a parent

pygame.surface.get_abs_offset() -> (x, y)
    finds the absolute position of a child subsurface inside its top-level parent

pygame.surface.get_size() -> (width, height)
    gets the dimensions of the surface

pygame.surface.get_width() -> int
    gets the width of the surface

pygame.surface.get_height() -> int
    gets the height of the surface

pygame.surface.get_rect(**kwargs) -> rect
    gets the rectangular area of the surface

pygame.surface.get_bitsize() -> int
    gets the bit depth of the surface pixel format

pygame.surface.get_bytesize() -> int
    gets the bytes used per surface pixel

pygame.surface.get_flags() -> int
    gets the additional flags used for the surface

pygame.surface.get_pitch() -> int
    gets the number of bytes used per surface row

pygame.surface.get_masks() -> (rmask, gmask, bmask, amask)
    gets the bitmasks needed to convert between a color and a mapped integer

pygame.surface.set_masks(masks) -> none
    sets the bitmasks needed to convert between a color and a mapped integer

pygame.surface.get_shifts() -> (rshift, gshift, bshift, ashift)
    gets the bit shifts needed to convert between a color and a mapped integer

pygame.surface.set_shifts(shifts) -> none
    sets the bit shifts needed to convert between a color and a mapped integer

pygame.surface.get_losses() -> (rloss, gloss, bloss, aloss)
    gets the significant bits used to convert between a color and a mapped integer

pygame.surface.get_bounding_rect(min_alpha=1) -> rect
    finds the smallest rect containing data

pygame.surface.get_view() -> bufferproxy
    returns a buffer view of the surface's pixels

pygame.surface.get_buffer() -> bufferproxy
    acquires a buffer object for the pixels of the surface

pygame.surface._pixels_address -> int
    pixel buffer address

pygame.surface.premul_alpha() -> surface
    returns a copy of the surface with the rgb channels pre-multiplied by the alpha channel
"""