"""
LayeredDirty is a subclass of LayeredUpdates that adds dirty flag functionality,
which allows sprites to be marked as "dirty" when they change. 


Methods and Attributes:
dirty attribute : Each sprite has a dirty attribute, which, when set to 1, means the sprite needs to be re-drawn. When set to 2, the sprite's area and background need to be redrawn.
clear()         : Clears dirty sprites.
draw()          : Draws only the dirty sprites to the screen.
*add(sprites, layer=None)   : Adds one or more sprites to the group. Optionally assign a layer.
"""

import pygame
from constants import *

class DirtySprite(pygame.sprite.DirtySprite):
    def __init__(self, color, width, height, start_pos):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=start_pos)
        self.dirty = 2

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.dirty = 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.dirty = 1

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("sprite.LayeredDirty")

    clock = pygame.time.Clock()

    layered_dirty_group = pygame.sprite.LayeredDirty()

    background = DirtySprite(BLUE, SCREEN_WIDTH, SCREEN_HEIGHT, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    player = DirtySprite(RED, 50, 50, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    layered_dirty_group.add(background, layer=0)
    layered_dirty_group.add(player, layer=1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        layered_dirty_group.update()

        layered_dirty_group.clear(screen, pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)))

        layered_dirty_group.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
