import pygame
import os

from constant import *

# load image
def load_image():
    image_path = os.path.join(ASSET, EXAMPLE_PNG)
    try:
        surface = pygame.image.load(image_path)
        surface = surface.convert_alpha()  # convert to include per-pixel transparency
        print(f"image loaded successfully from {image_path}")
        return surface
    except pygame.error as e:
        print(f"cannot load image: {image_path} - {e}")
        return None

# save image / screenshot
def save_image(surface):
    save_path = os.path.join(ASSET, SAVED_PNG)
    try:
        pygame.image.save(surface, save_path)
        print(f"image saved successfully to {save_path}")
    except pygame.error as e:
        print(f"cannot save image: {save_path} - {e}")

def get_sdl_image_version():
    version = pygame.image.get_sdl_image_version()
    print(f"sdl_image library version: {version}")

def check_extended_formats():
    can_load_extended = pygame.image.get_extended()
    print(f"extended image formats supported: {can_load_extended}")

# convert surface to byte buffer and back
def surface_to_from_bytes(surface):
    image_bytes = pygame.image.tobytes(surface, 'RGBA')
    new_surface = pygame.image.frombytes(image_bytes, surface.get_size(), 'RGBA')
    print("converted surface to bytes and back successfully")
    return new_surface

# create a surface from a byte buffer (fromstring and frombuffer)
def create_surface_from_buffer():
    width, height = 100, 100
    buffer = bytes(bytearray([255, 0, 0, 255] * width * height))  # red color buffer
    surface_from_string = pygame.image.fromstring(buffer, (width, height), 'RGBA')
    surface_from_buffer = pygame.image.frombuffer(buffer, (width, height), 'RGBA')
    print("created surface from string and buffer successfully")
    return surface_from_string, surface_from_buffer

# load a bmp image (basic format)
def load_bmp_image():
    image_path = os.path.join(ASSET, EXAMPLE_BMP)
    try:
        surface = pygame.image.load_basic(image_path)
        print(f"bmp image loaded successfully from {image_path}")
        return surface
    except pygame.error as e:
        print(f"cannot load bmp image: {image_path} - {e}")
        return None

# load an extended image format
def load_extended_image():
    image_path = os.path.join(ASSET, EXAMPLE_PNG)
    try:
        surface = pygame.image.load_extended(image_path)
        print(f"extended image format loaded successfully from {image_path}")
        return surface
    except pygame.error as e:
        print(f"cannot load extended image format: {image_path} - {e}")
        return None

# save a surface to png/jpg using save_extended
def save_extended_image(surface):
    save_path = os.path.join(ASSET, SAVED_JPG)
    try:
        pygame.image.save_extended(surface, save_path)
        print(f"extended format image saved successfully to {save_path}")
    except pygame.error as e:
        print(f"cannot save extended format image: {save_path} - {e}")

def main():
    pygame.init()
    pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    surface = load_image()
    if surface:
        save_image(surface)
    
    get_sdl_image_version()

    check_extended_formats()

    # convert surface to bytes and back
    if surface:
        new_surface = surface_to_from_bytes(surface)
        save_image(new_surface)

    # create surface from buffer
    _, surface_from_buffer = create_surface_from_buffer()
    print(surface_from_buffer)

    load_bmp_image()

    extended_surface = load_extended_image()
    if extended_surface:
        save_extended_image(extended_surface)

    pygame.quit()

if __name__ == "__main__":
    main()
