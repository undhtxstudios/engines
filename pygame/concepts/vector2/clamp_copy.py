import pygame
from pygame.math import Vector2

if __name__ == '__main__':
    pygame.init()

    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BG_COLOR = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Clamping and Copying Demo")
    clock = pygame.time.Clock()

    vector = Vector2(500, 300)
    max_length = 200

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        pygame.draw.line(screen, WHITE, (100, 300), (100 + vector.x, 300 + vector.y), 2)

        clamped_vector = vector.clamp_magnitude(max_length)

        pygame.draw.line(screen, RED, (100, 200), (100 + clamped_vector.x, 200 + clamped_vector.y), 2)

        font = pygame.font.Font(None, 36)
        text_original = font.render(f"Original Vector: {vector}", True, WHITE)
        text_clamped = font.render(f"Clamped Vector: {clamped_vector}", True, RED)
        screen.blit(text_original, (10, 10))
        screen.blit(text_clamped, (10, 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
