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
    FPS = 60

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pygame Vector2 Basic")

    font = pygame.font.SysFont("Arial", 18)

    def draw_text(surface, text, pos, color=WHITE):
        text_surface = font.render(text, True, color)
        surface.blit(text_surface, pos)

    def draw_vector(surface, start_pos, vector, color=WHITE):
        end_pos = (start_pos[0] + vector.x, start_pos[1] + vector.y)
        pygame.draw.line(surface, color, start_pos, end_pos, 3)
        pygame.draw.circle(surface, color, end_pos, 5)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        vec1 = Vector2(150, 50)
        vec2 = Vector2(100, 200)
        
        origin = Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        draw_vector(screen, origin, vec1, RED)
        draw_vector(screen, origin, vec2, GREEN)

        draw_text(screen, f"vec1: {vec1}", (20, 20))
        draw_text(screen, f"vec2: {vec2}", (20, 50))

        dot_product = vec1.dot(vec2)
        draw_text(screen, f"Dot Product: {dot_product}", (20, 80))

        cross_product = vec1.cross(vec2)
        draw_text(screen, f"Cross Product: {cross_product}", (20, 110))

        magnitude_vec1 = vec1.magnitude()
        draw_text(screen, f"Magnitude of vec1: {magnitude_vec1}", (20, 140))

        magnitude_squared_vec1 = vec1.magnitude_squared()
        draw_text(screen, f"Magnitude Squared of vec1: {magnitude_squared_vec1}", (20, 170))

        normalized_vec1 = vec1.normalize() if magnitude_vec1 != 0 else Vector2(0, 0)
        draw_text(screen, f"Normalized vec1: {normalized_vec1}", (20, 200))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
