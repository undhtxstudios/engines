"""
OrderedUpdates is a specialized Group subclass that maintains the order in which sprites are added.
This ensures that sprites are drawn in the order they were added to the group, 
which can be important for layered drawing.

Methods and Attributes:
update()        : Updates the state of all sprites in the group.
draw(surface)   : Draws all sprites in the group in the order they were added.
"""

import pygame
from constants import *

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, start_pos):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=start_pos)

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("sprite.OrderedUpdates")

    clock = pygame.time.Clock()

    ordered_group = pygame.sprite.OrderedUpdates()

    background = GameSprite(BLUE, SCREEN_WIDTH, SCREEN_HEIGHT, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    platform = GameSprite(GREEN, 250, 3000, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
    player = GameSprite(RED, 50, 50, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # order (background -> platform -> player)
    ordered_group.add(background)
    ordered_group.add(platform)
    ordered_group.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ordered_group.update()

        screen.fill(WHITE)
        ordered_group.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
