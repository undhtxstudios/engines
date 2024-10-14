"""
surfarray
   provides functions to manipulate surface pixel data using numpy arrays

array2d(surface)
   copy pixels into a 2d array

pixels2d(surface)
   reference pixels into a 2d array

array3d(surface)
   copy pixels into a 3d array

pixels3d(surface)
   reference pixels into a 3d array

array_alpha(surface)
   copy pixel alphas into a 2d array

pixels_alpha(surface)
   reference pixel alphas into a 2d array

array_red(surface)
   copy red pixels into a 2d array

pixels_red(surface)
   reference red pixels into a 2d array

array_green(surface)
   copy green pixels into a 2d array

pixels_green(surface)
   reference green pixels into a 2d array

array_blue(surface)
   copy blue pixels into a 2d array

pixels_blue(surface)
   reference blue pixels into a 2d array

array_colorkey(surface)
   copy the colorkey values into a 2d array

make_surface(array)
   copy an array to a new surface

blit_array(surface, array)
   blit directly from array values

map_array(array)
   map a 3d array into a 2d array

use_arraytype(type)
   set the array system to be used for surface arrays

get_arraytype()
   get the currently active array type

get_arraytypes()
   get the array system types currently supported
"""
