import pygame
from pygame.locals import *

pygame.init()

image = pygame.image.load("image.png")

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Transform")

def flip():
    # flip the image horizontally
    flipped_image = pygame.transform.flip(image, True, False)
    screen.blit(flipped_image, (100, 100))

def scale():
    # scale the image to 200x200
    scaled_image = pygame.transform.scale(image, (200, 200))
    screen.blit(scaled_image, (100, 100))

def scale_by():
    # scale the image by 1.5 times
    scaled_image = pygame.transform.scale_by(image, 1.5)
    screen.blit(scaled_image, (100, 100))

def rotate():
    # rotate the image by 45 degrees
    rotated_image = pygame.transform.rotate(image, 45)
    screen.blit(rotated_image, (100, 100))

def rotozoom():
    # rotate by 45 degrees and scale by 0.5
    rotozoomed_image = pygame.transform.rotozoom(image, 45, 0.5)
    screen.blit(rotozoomed_image, (100, 100))

def scale2x():
    # double the size of the image
    scaled2x_image = pygame.transform.scale2x(image)
    screen.blit(scaled2x_image, (100, 100))

def smoothscale():
    # smoothly scale the image to 200x200
    smooth_scaled_image = pygame.transform.smoothscale(image, (200, 200))
    screen.blit(smooth_scaled_image, (100, 100))

def grayscale():
    grayscale_image = pygame.transform.grayscale(image)
    screen.blit(grayscale_image, (100, 100))

def threshold():
    dest_surface = pygame.Surface(image.get_size())
    search_color = (255, 0, 0)
    threshold = (30, 30, 30)
    set_color = (0, 255, 0)
    pygame.transform.threshold(dest_surface, image, search_color, threshold, set_color)
    screen.blit(dest_surface, (100, 100))

examples = {
    "flip": flip,
    "scale": scale,
    "scale_by": scale_by,
    "rotate": rotate,
    "rotozoom": rotozoom,
    "scale2x": scale2x,
    "smoothscale": smoothscale,
    "grayscale": grayscale,
    "threshold": threshold,
}

def main():
    clock = pygame.time.Clock()

    running = True
    current = "flip"

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_1:
                    current = "flip"
                elif event.key == K_2:
                    current = "scale"
                elif event.key == K_3:
                    current = "scale_by"
                elif event.key == K_4:
                    current = "rotate"
                elif event.key == K_5:
                    current = "rotozoom"
                elif event.key == K_6:
                    current = "scale2x"
                elif event.key == K_7:
                    current = "smoothscale"
                elif event.key == K_8:
                    current = "grayscale"
                elif event.key == K_9:
                    current = "threshold"

        screen.fill((255, 255, 255))

        examples[current]()

        pygame.display.flip()
        clock.tick(1)

    pygame.quit()

if __name__ == "__main__":
    main()
