"""
image
https://www.pygame.org/docs/ref/image.html

pygame.image.load
    load(filename) -> surface
    load(fileobj, namehint="") -> surface
    loads an image from a file or file-like object

pygame.image.save
    save(surface, filename) -> none
    save(surface, fileobj, namehint="") -> none
    saves a surface to a file or file-like object

pygame.image.get_sdl_image_version
    get_sdl_image_version(linked=true) -> (major, minor, patch)
    returns the version of the sdl_image library being used

pygame.image.get_extended
    get_extended() -> bool
    checks if extended image formats can be loaded

pygame.image.tostring
    tostring(surface, format, flipped=false) -> bytes
    converts a surface to a byte buffer

pygame.image.tobytes
    tobytes(surface, format, flipped=false) -> bytes
    converts a surface to a byte buffer (recommended)

pygame.image.fromstring
    fromstring(bytes, size, format, flipped=false) -> surface
    creates a surface from a byte buffer

pygame.image.frombytes
    frombytes(bytes, size, format, flipped=false) -> surface
    creates a surface from a byte buffer (recommended)

pygame.image.frombuffer
    frombuffer(buffer, size, format) -> surface
    creates a surface that shares data inside a bytes buffer

pygame.image.load_basic
    load_basic(file) -> surface
    loads a bmp image from a file or file-like object

pygame.image.load_extended
    load_extended(filename) -> surface
    load_extended(fileobj, namehint="") -> surface
    loads an image from a file (extended formats)

pygame.image.save_extended
    save_extended(surface, filename) -> none
    save_extended(surface, fileobj, namehint="") -> none
    saves a surface as a png/jpg image to a file or file-like object
"""