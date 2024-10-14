# surface.py

import pygame
from constants import *

def create_surface_example():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pygame Surface Example')

    surface = pygame.Surface((200, 200))
    surface.fill(RED)
    surface.set_colorkey(WHITE)
    surface.set_alpha(ALPHA_OPAQUE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        screen.blit(surface, (300, 200))
        pygame.display.flip()

    pygame.quit()

def blit_example():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Blit Example')

    surface1 = pygame.Surface((100, 100))
    surface1.fill(GREEN)

    surface2 = pygame.Surface((50, 50))
    surface2.fill(BLUE)

    surface1.blit(surface2, (25, 25))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        screen.blit(surface1, (350, 250))
        pygame.display.flip()

    pygame.quit()

def scroll_example():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Scroll Example')

    surface = pygame.Surface((200, 200))
    surface.fill(RED)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.scroll(1, 0)

        screen.fill(BLACK)
        screen.blit(surface, (300, 200))
        pygame.display.flip()

    pygame.quit()

def blits_example():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Blits Example')

    surface1 = pygame.Surface((200, 200))
    surface1.fill(RED)

    surface2 = pygame.Surface((50, 50))
    surface2.fill(BLUE)

    surfaces_to_blit = [(surface2, (10, 10)), (surface2, (100, 100))]
    surface1.blits(surfaces_to_blit)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        screen.blit(surface1, (300, 200))
        pygame.display.flip()

    pygame.quit()

def convert_example():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Convert Example')

    surface = pygame.Surface((200, 200))
    surface.fill(RED)
    converted_surface = surface.convert()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        screen.blit(converted_surface, (300, 200))
        pygame.display.flip()

    pygame.quit()

def convert_alpha_example():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Convert Alpha Example')

    surface = pygame.Surface((200, 200), pygame.SRCALPHA)
    surface.fill(RED)
    alpha_surface = surface.convert_alpha()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        screen.blit(alpha_surface, (300, 200))
        pygame.display.flip()

    pygame.quit()

def copy_example():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Copy Example')

    surface = pygame.Surface((200, 200))
    surface.fill(RED)
    copied_surface = surface.copy()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        screen.blit(copied_surface, (300, 200))
        pygame.display.flip()

    pygame.quit()

def fill_example():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Fill Example')

    surface = pygame.Surface((200, 200))
    surface.fill(BLUE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        screen.blit(surface, (300, 200))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    create_surface_example()
    blit_example()
    scroll_example()
    blits_example()
    convert_example()
    convert_alpha_example()
    copy_example()
    fill_example()
