"""
RenderUpdates: subclass of Group designed to efficiently manage redrawing sprites in games. 

Tracks areas that have changed and only updates those regions.

Methods and Attributes:
clear(surface, bg_color)    : Clears all the sprites by filling their previous positions with a background color or surface.
draw(surface)               : Draws the sprites to the given surface and returns the list of areas that were changed.
update()                    : Updates the state of all sprites in the group.
"""

import pygame
import random
from constants import *

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed, start_pos):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = pygame.Vector2(speed)

    def update(self):
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y

        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("sprite.RenderedUpdates")

    clock = pygame.time.Clock()

    render_group = pygame.sprite.RenderUpdates()

    # static
    for i in range(5):
        static_sprite = GameSprite(BLUE, 100, 100, (0, 0), start_pos=(random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100)))
        render_group.add(static_sprite)

    for i in range(3):
        moving_sprite = GameSprite(RED, 50, 50, (random.choice([-3, 3]), random.choice([-3, 3])), start_pos=(random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100)))
        render_group.add(moving_sprite)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)
        render_group.clear(screen, screen)

        render_group.update()

        dirty_rects = render_group.draw(screen)
        print(dirty_rects)

        pygame.display.update(dirty_rects)

        clock.tick(60)

    pygame.quit()
