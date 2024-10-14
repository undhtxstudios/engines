import pygame
from math import atan2, degrees

if __name__ == '__main__':
    pygame.init()

    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BG_COLOR = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Vector Rotation Demo")
    clock = pygame.time.Clock()

    vector = pygame.Vector2(200, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        mouse_pos = pygame.mouse.get_pos()
        angle = degrees(atan2(mouse_pos[1] - SCREEN_HEIGHT / 2, mouse_pos[0] - SCREEN_WIDTH / 2))

        rotated_vector = vector.rotate(angle)

        pygame.draw.line(screen, WHITE, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), (SCREEN_WIDTH / 2 + vector.x, SCREEN_HEIGHT / 2 + vector.y), 2)
        pygame.draw.line(screen, RED, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), (SCREEN_WIDTH / 2 + rotated_vector.x, SCREEN_HEIGHT / 2 + rotated_vector.y), 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
