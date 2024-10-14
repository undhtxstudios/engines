import pygame
import sys

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pygame Font Module Demo')

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    default_font_name = pygame.font.get_default_font()
    print(f"Default font: {default_font_name}")

    system_font = pygame.font.SysFont('arial', 30, bold=True, italic=True)
    custom_font = pygame.font.Font(None, 40)

    text_surface = system_font.render('System Font - Bold and Italic', True, WHITE)
    custom_text_surface = custom_font.render('Custom Font - Default', True, BLUE)

    metrics = system_font.metrics('A')
    print(f"Metrics for 'A': {metrics}")

    text_size = system_font.size('System Font - Bold and Italic')
    print(f"Text size: {text_size}")

    custom_font.set_underline(True)
    custom_font.set_strikethrough(True)
    underline_text_surface = custom_font.render('Underlined and Strikethrough Text', True, RED)

    ascent = custom_font.get_ascent()
    descent = custom_font.get_descent()
    height = custom_font.get_height()
    linesize = custom_font.get_linesize()
    print(f"Ascent: {ascent}, Descent: {descent}, Height: {height}, Linesize: {linesize}")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        screen.blit(text_surface, (50, 50))
        screen.blit(custom_text_surface, (50, 150))
        screen.blit(underline_text_surface, (50, 250))

        pygame.display.flip()

    pygame.font.quit()
    pygame.quit()
    sys.exit()
