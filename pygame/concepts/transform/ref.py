"""
Transform / https://www.pygame.org/docs/ref/transform.html

flip(surface, flip_x, flip_y)
    flip the surface horizontally and/or vertically

scale(surface, size, dest_surface=none)
    resize the surface to a new width and height

scale_by(surface, factor, dest_surface=none)
    resize the surface by a scalar factor or a tuple of factors

rotate(surface, angle)
    rotate the surface counterclockwise by a specified angle

rotozoom(surface, angle, scale)
    scale and rotate the surface with filtering

scale2x(surface, dest_surface=none)
    double the size of the surface using the scale2x algorithm 

smoothscale(surface, size, dest_surface=none)
    smoothly scale the surface to a new size

smoothscale_by(surface, factor, dest_surface=none)
    smoothly scale the surface by a scalar factor or a tuple of factors

get_smoothscale_backend()
    return the smoothscale filter version in use

set_smoothscale_backend(backend)
    set the smoothscale filter version to a specific backend

chop(surface, rect)
    get a copy of the surface with an interior area removed

laplacian(surface, dest_surface=none)
    find and highlight the edges of the surface using the laplacian algorithm  

average_surfaces(surfaces, dest_surface=none, palette_colors=1)
    calculate the average surface from multiple surfaces

average_color(surface, rect=none, consider_alpha=false)
    find the average color of a surface or a region of a surface

grayscale(surface, dest_surface=none)
    convert the surface to grayscale

threshold(dest_surface, surface, search_color, threshold=(0,0,0,0), set_color=(0,0,0,0), set_behavior=1, search_surf=none, inverse_set=false)
    identify pixels within a threshold and optionally modify them  
"""