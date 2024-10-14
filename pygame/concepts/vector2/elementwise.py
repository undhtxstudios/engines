import pygame
from pygame.math import Vector2

if __name__ == '__main__':
    pygame.init()

    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BG_COLOR = (0, 0, 0)
    WHITE = (255, 255, 255)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Elementwise Operations Demo")
    clock = pygame.time.Clock()

    vector_a = Vector2(100, 200)
    vector_b = Vector2(2, 3)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        # perform elementwise multiplication
        result_vector = vector_a.elementwise() * vector_b

        pygame.draw.line(screen, WHITE, (0, 0), vector_a, 2)
        pygame.draw.line(screen, WHITE, (0, 0), result_vector, 2)

        font = pygame.font.Font(None, 36)
        text_a = font.render(f"Vector A: {vector_a}", True, WHITE)
        text_b = font.render(f"Vector B: {vector_b}", True, WHITE)
        text_result = font.render(f"Result: {result_vector}", True, WHITE)
        screen.blit(text_a, (10, 10))
        screen.blit(text_b, (10, 50))
        screen.blit(text_result, (10, 90))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
