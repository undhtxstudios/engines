import pygame
from pygame.math import Vector2

if __name__ == '__main__':
    pygame.init()

    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BG_COLOR = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Distance and Movement Demo")
    clock = pygame.time.Clock()

    start_vector = Vector2(100, 300)
    end_vector = Vector2(700, 300)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        distance = start_vector.distance_to(end_vector)
        movement_vector = start_vector.move_towards(end_vector, 2)

        pygame.draw.circle(screen, WHITE, start_vector, 5)
        pygame.draw.circle(screen, GREEN, end_vector, 5)
        pygame.draw.line(screen, WHITE, start_vector, end_vector, 1)

        start_vector = movement_vector

        font = pygame.font.Font(None, 36)
        text = font.render(f"Distance: {distance:.2f}", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
