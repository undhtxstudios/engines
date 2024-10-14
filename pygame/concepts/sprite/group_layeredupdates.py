"""
LayeredUpdates is a subclass of OrderedUpdates and allows for more granular control over the drawing order of sprites by organizing them into layers.
Each sprite can be assigned a specific layer, and sprites in lower layers are drawn before those in higher layers. 

Methods and Attributes:
change_layer(sprite, new_layer) : Changes the layer of the specified sprite to new_layer.
get_layer_of_sprite(sprite)     : Returns the layer of the specified sprite.
*add(sprites, layer=None)       : Adds one or more sprites to the group. If a layer argument is provided, the sprites are added to that layer.
*remove(sprites)                : Removes one or more sprites from the group.
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
    pygame.display.set_caption("sprite.LayeredUpdates")

    clock = pygame.time.Clock()

    layered_group = pygame.sprite.LayeredUpdates()

    background = GameSprite(BLUE, SCREEN_WIDTH, SCREEN_HEIGHT, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    midground = GameSprite(GREEN, 400, 200, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    player = GameSprite(RED, 50, 50, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    foreground = GameSprite(YELLOW, 200, 100, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

    # add sprites to specific layers
    layered_group.add(background, layer=0)
    layered_group.add(midground, layer=1)
    layered_group.add(player, layer=2)
    layered_group.add(foreground, layer=3)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # change players layer when a key is pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    layered_group.change_layer(player, 3)  # move player above foreground
                elif event.key == pygame.K_DOWN:
                    layered_group.change_layer(player, 1)  # move player below midground

        screen.fill(WHITE)

        layered_group.update()
        layered_group.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
