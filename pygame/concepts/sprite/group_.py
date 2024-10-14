"""
A Group in Pygame is a container for Sprite objects.
It provides mechanisms for managing, updating, and drawing multiple sprites at once.

Group is used when you want to handle multiple sprites collectively.
Instead of updating or drawing each sprite individually, 
add them to a Group and update or draw the entire group in one call.

Methods and Attributes:
add(*sprites)       : Adds one or more sprites to the group.
remove(*sprites)    : Removes one or more sprites from the group.
empty()             : Removes all sprites from the group.
has(*sprites)       : Checks if one or more sprites are in the group.
update(*args)       : Calls the update() method for all sprites in the group.
draw(surface)       : Draws all sprites in the group on the given surface.
sprites()           : Returns a list of all sprites in the group.
copy()              : Returns a shallow copy of the group.
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
    pygame.display.set_caption("sprite.Group")

    clock = pygame.time.Clock()

    enemy_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    powerup_group = pygame.sprite.Group()

    # create enemies
    for i in range(5):
        enemy = GameSprite(RED, 50, 50, (random.choice([-3, 3]), random.choice([-3, 3])), start_pos=(random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100)))
        enemy_group.add(enemy)

    # create bullets
    for i in range(10):
        bullet = GameSprite(BLUE, 10, 10, (random.choice([-5, 5]), random.choice([-5, 5])), start_pos=(random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100)))
        bullet_group.add(bullet)

    # create power-ups
    for i in range(3):
        powerup = GameSprite(YELLOW, 30, 30, (random.choice([-2, 2]), random.choice([-2, 2])), start_pos=(random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100)))
        powerup_group.add(powerup)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        enemy_group.update()
        bullet_group.update()
        powerup_group.update()

        # detect collisions (bullets with enemies)
        bullet_hit_list = pygame.sprite.groupcollide(bullet_group, enemy_group, False, False)
        for bullet, enemies in bullet_hit_list.items():
            bullet.image.fill(BLACK)
            for enemy in enemies:
                enemy.image.fill(BLACK)

        # detect collisions (bullets with power-ups)
        bullet_power_up_list = pygame.sprite.groupcollide(bullet_group, powerup_group, False, True)
        for bullet, power_ups in bullet_hit_list.items():
            bullet.image.fill(YELLOW)
            bullet.speed += (0.2, 0.2)

        screen.fill(WHITE)

        enemy_group.draw(screen)
        bullet_group.draw(screen)
        powerup_group.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
