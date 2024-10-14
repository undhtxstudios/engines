"""
sprite.Sprite
- base for creating objects that can be controlled in games
- prites typically represent players, enemies, bullets, or any interactive object in a game

methods:
__init__    : initialize the sprite
add         : add the sprite to one or more group
remove      : remove the sprite from one or more group
kill        : remove the sprite from all group objects
groups      : returns a list of group objects this sprite is a member of
alive       : returns true if the sprite is in any groups
update      : a method meant to be overridden to define sprite behavior
"""

import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.health = 100
        self.energy = 50
        self.velocity = pygame.Vector2(0, 0)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -5
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = 5
        else:
            self.velocity.x = 0

        if keys[pygame.K_UP]:
            self.velocity.y = -5
        elif keys[pygame.K_DOWN]:
            self.velocity.y = 5
        else:
            self.velocity.y = 0

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.kill()  # remove sprite from all groups

class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = pygame.Vector2(-3, 0)

    def update(self):
        self.rect.x += self.velocity.x
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("sprite.Sprite")

    clock = pygame.time.Clock()

    player = Player(BLUE, 50, 50)
    enemy = Enemy(RED, 30, 30)

    # sprite groups
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # add player and enemy to groups
    all_sprites.add(player)
    all_sprites.add(enemy)
    enemies.add(enemy)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update all sprites
        all_sprites.update()

        # collision detection between player and enemies
        if pygame.sprite.spritecollideany(player, enemies):
            player.take_damage(1)

        screen.fill(WHITE)

        all_sprites.draw(screen)

        font = pygame.font.SysFont(None, 36)
        health_text = font.render(f"Health: {player.health}", True, BLACK)
        screen.blit(health_text, (10, 10))

        pygame.display.flip()
        print(player.alive())

        clock.tick(60)

    pygame.quit()
