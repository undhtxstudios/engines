"""
Similar to Sprite but uses weak references when it is added to groups. 
Automatically removed from a Group when it is no longer used elsewhere in the program.
Helps with memory management when handling a large number of sprites or when sprites are dynamically created and destroyed.

Typically used in scenarios where you have many temporary objects (e.g., particles) that will be created and destroyed quickly. 
Weak references ensure that the sprite is removed from its groups when it is no longer needed, thus avoiding memory leaks.
"""

import pygame
from constants import *

class Projectile(pygame.sprite.WeakSprite):
    def __init__(self, color, width, height, start_pos, velocity):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=start_pos)
        self.velocity = pygame.Vector2(velocity)

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # # remove the projectile if it goes off-screen (DOES NOT WORK, WHY WE NEED TO DO MANUALLY BRUH?)
        # if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.top > SCREEN_HEIGHT or self.rect.bottom < 0:
        #     self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.shoot_delay = 50
        self.last_shot_time = 0

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

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > self.shoot_delay:
            self.last_shot_time = current_time
            new_projectile = Projectile(BLUE, 10, 10, self.rect.center, velocity=(5, 0))
            projectiles.add(new_projectile)

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("sprite.WeakSprite")

    clock = pygame.time.Clock()

    player = Player(RED, 50, 50)

    players = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()

    players.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        players.update()

        screen.fill(WHITE)

        players.draw(screen)

        print(projectiles.sprites())

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
