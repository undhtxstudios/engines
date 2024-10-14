import pygame
from pygame.math import Vector2

if __name__ == '__main__':
    pygame.init()

    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BG_COLOR = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Vector Reflection and Projection")
    clock = pygame.time.Clock()

    vector = Vector2(300, 150)
    surface_normal = Vector2(0, -1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        mouse_pos = Vector2(pygame.mouse.get_pos())

        reflection = vector.reflect(surface_normal)

        projection = mouse_pos.project(vector)

        pygame.draw.line(screen, WHITE, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), (SCREEN_WIDTH / 2 + vector.x, SCREEN_HEIGHT / 2 + vector.y), 2)

        pygame.draw.line(screen, RED, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), (SCREEN_WIDTH / 2 + surface_normal.x * 50, SCREEN_HEIGHT / 2 + surface_normal.y * 50), 2)

        pygame.draw.line(screen, GREEN, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), (SCREEN_WIDTH / 2 + reflection.x, SCREEN_HEIGHT / 2 + reflection.y), 2)

        pygame.draw.line(screen, BLUE, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), (SCREEN_WIDTH / 2 + projection.x, SCREEN_HEIGHT / 2 + projection.y), 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
