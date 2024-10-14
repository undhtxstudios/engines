import pygame
from listeners import quit_listener, mouse_down_listener_1, mouse_down_listener_2, key_down_listener

SUCCESS = True
FAIL = False

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600
FPS = 1

EVENT_HANDLERS = {
    pygame.QUIT: [quit_listener],
    pygame.KEYDOWN: [key_down_listener],
    pygame.MOUSEBUTTONDOWN: [mouse_down_listener_1, mouse_down_listener_2]
}
