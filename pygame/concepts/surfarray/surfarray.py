import pygame
import pygame.surfarray as surfarray
import numpy as np

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FPS = 30

image = pygame.image.load('example.png')
image = pygame.transform.scale(image, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Surfarray')

def display_image(img):
    screen.fill(WHITE)
    screen.blit(img, (0, 0))
    pygame.display.flip()

def apply_color_filter(surface):
    array = surfarray.array3d(surface)
    array[:, :, 1] = 0
    return surfarray.make_surface(array)

def apply_grayscale_filter(surface):
    array = surfarray.array2d(surface)
    gray_array = np.mean(array, axis=-1)
    return surfarray.make_surface(np.stack([gray_array] * 3, axis=-1))

def invert_colors(surface):
    array = surfarray.array3d(surface)
    inverted_array = 255 - array
    return surfarray.make_surface(inverted_array)

def extract_red_channel(surface):
    red_array = surfarray.array_red(surface)
    red_surface = np.zeros_like(surfarray.array3d(surface))
    red_surface[:, :, 0] = red_array
    return surfarray.make_surface(red_surface)

def apply_alpha_effect(surface):
    alpha_array = surfarray.array_alpha(surface)
    print('Alpha Array: ', alpha_array)
    surface_with_alpha = surfarray.make_surface(alpha_array)
    return surface_with_alpha

def map_colors(surface):
    array = surfarray.array3d(surface)
    mapped_array = np.full_like(array, (128, 128, 128))  # map to a gray color
    return surfarray.make_surface(mapped_array)

def blit_array_effect(surface):
    array = surfarray.array3d(surface)
    array[:, :, 0] = 255
    surfarray.blit_array(surface, array)
    return surface

def rotate_image(surface):
    return pygame.transform.rotate(surface, 45)

def main():
    clock = pygame.time.Clock()
    running = True
    current_surface = image.copy()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_surface = apply_color_filter(image)
                elif event.key == pygame.K_2:
                    current_surface = apply_grayscale_filter(image)
                elif event.key == pygame.K_3:
                    current_surface = invert_colors(image)
                elif event.key == pygame.K_4:
                    current_surface = extract_red_channel(image)
                elif event.key == pygame.K_5:
                    current_surface = apply_alpha_effect(image)
                elif event.key == pygame.K_6:
                    current_surface = map_colors(image)
                elif event.key == pygame.K_7:
                    current_surface = blit_array_effect(image)
                elif event.key == pygame.K_8:
                    current_surface = rotate_image(image)
                
                display_image(current_surface)

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
