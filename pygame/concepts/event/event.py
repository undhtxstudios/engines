import pygame
import sys

from centralized import CentralizedEventManager
from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT, FPS

def CentralizedEvent():
    pygame.init()
    pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()

    central_manager = CentralizedEventManager()
    central_manager.load_handlers()

    central_manager.block_events(pygame.MOUSEMOTION)
    central_manager.allow_events(pygame.MOUSEBUTTONDOWN)
    
    running = True
    while running:
        central_manager.handle_events()

        # custom_type = central_manager.create_custom_event()
        # central_manager.post_custom_event(custom_type, {"message": "Custom Event"})
        # usually add custom_type + CONSTANT to differentiate between custom events

        # events = central_manager.get_events(pump=True)
        # print("Events in queue:", events)
        clock.tick(FPS)

def SimpleEventHandling():
    pygame.init()
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        pygame.event.pump()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    print("Spacebar pressed!")

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    print(f"Mouse button {event.button} pressed at {event.pos}")

            # USEREVENT + CONSTANT
            elif event.type == pygame.USEREVENT:
                print(f"Custom event triggered with data: {event.dict}")

        screen.fill((0, 0, 0))
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    # CentralizedEvent()
    SimpleEventHandling()
    pass
