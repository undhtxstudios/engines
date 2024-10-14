import pygame
import sys

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pygame Mouse Module Demo')

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    # load a custom cursor
    # pygame includes some built-in cursors, but we can also load our own
    # custom_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)
    # pygame.mouse.set_cursor(custom_cursor)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Mouse button {event.button} pressed at {event.pos}")
            elif event.type == pygame.MOUSEBUTTONUP:
                print(f"Mouse button {event.button} released at {event.pos}")
            elif event.type == pygame.MOUSEMOTION:
                print(f"Mouse moved to {event.pos} with relative movement {event.rel}")
            elif event.type == pygame.MOUSEWHEEL:
                print(f"Mouse wheel scrolled {'up' if event.y > 0 else 'down'}")

        screen.fill(BLACK)

        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        pygame.draw.circle(screen, WHITE, mouse_pos, 15)
        button_text = f"Left: {'Pressed' if mouse_buttons[0] else 'Released'}, " \
                    f"Middle: {'Pressed' if mouse_buttons[1] else 'Released'}, " \
                    f"Right: {'Pressed' if mouse_buttons[2] else 'Released'}"
        font = pygame.font.Font(None, 30)
        text_surface = font.render(button_text, True, RED)
        screen.blit(text_surface, (20, 20))

        focused = pygame.mouse.get_focused()
        visible = pygame.mouse.get_visible()
        focus_text = f"Mouse Focus: {'Yes' if focused else 'No'}, " \
                    f"Mouse Visible: {'Yes' if visible else 'No'}"
        focus_surface = font.render(focus_text, True, BLUE)
        screen.blit(focus_surface, (20, 60))

        pygame.display.flip()

    pygame.quit()
    sys.exit()
