"""
DirtySprite is used to optimize rendering by minimizing the area of the screen that is redrawn.
Rather than redrawing the entire screen each frame, only the "dirty" parts of the screen
where changes occurred (i.e., where sprites have moved or updated) are redrawn.

Usage: large number of sprites, especially when sprites don’t move often.

Methods and Attributes:
dirty: A flag that determines if the sprite should be redrawn. Set this to 1 when the sprite has changed and needs to be redrawn.
blendmode: Specifies a blending mode for drawing.
visible: A flag that determines if the sprite should be rendered.
"""

import pygame
import random
from constants import *

class MovingSprite(pygame.sprite.DirtySprite):
    def __init__(self, color, width, height, start_pos, speed):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = pygame.Vector2(speed)
        self.dirty = 2
        self.visible = 1

    def update(self):
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y

        # mark it as dirty (i.e., needs to be redrawn)
        self.dirty = 1

        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed.x *= -1
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed.y *= -1

class StaticSprite(pygame.sprite.DirtySprite):
    def __init__(self, color, width, height, pos):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self.dirty = False
        self.visible = 1

    def update(self):
        # static sprite, does not move or change, so it is not marked as dirty
        self.dirty = 1 # repaint, dont understand yet??? whats the point of not dirtying if repainted anyway

if __name__ == '__main__':
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("sprite.DirtySprite")

    clock = pygame.time.Clock()

    background = pygame.Surface(screen.get_size())
    background.fill(WHITE)

    static_sprites = pygame.sprite.LayeredDirty()
    moving_sprites = pygame.sprite.LayeredDirty()

    for i in range(5):
        static_sprite = StaticSprite(BLUE, 100, 100, (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100)))
        static_sprites.add(static_sprite)

        moving_sprite = MovingSprite(RED, 50, 50, (random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100)), speed=(random.choice([-5, 5]), random.choice([-5, 5])))
        moving_sprites.add(moving_sprite)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        moving_sprites.update()
        static_sprites.update()

        static_sprites.clear(screen, background)
        moving_sprites.clear(screen, background)

        dirty_rects = static_sprites.draw(screen) + moving_sprites.draw(screen)
        
        # only update dirty
        pygame.display.update(dirty_rects)

        clock.tick(60)

    pygame.quit()
