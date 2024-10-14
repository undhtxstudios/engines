"""
GroupSingle is a specialized group for handling a single sprite.

Handles exactly one sprite.
Provides methods to manage and update the sprite like a group would.

Key Methods and Attributes:
Inherits from group.
"""

import pygame
import sys
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("sprite.GroupSingle")

    player = Player()
    player_group = pygame.sprite.GroupSingle(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player_group.update()

        screen.fill(WHITE)
        player_group.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(60)
