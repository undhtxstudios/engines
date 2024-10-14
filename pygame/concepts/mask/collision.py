# All credits to https://www.youtube.com/watch?v=tJiKYMQJnYg

import pygame

if __name__ == '__main__':
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Masks")

    BG = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)

    class Soldier(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("soldier.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.mask = pygame.mask.from_surface(self.image)

    class Bullet(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((10, 10))
            self.rect = self.image.get_rect()
            self.image.fill(RED)
            self.mask = pygame.mask.from_surface(self.image)

        def update(self, colour):
            pos = pygame.mouse.get_pos()
            self.rect.center = (pos)
            self.image.fill(colour)

    pygame.mouse.set_visible(False)

    soldier = Soldier(350, 250)
    bullet = Bullet()

    soldier_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()

    soldier_group.add(soldier)
    bullet_group.add(bullet)

    run = True
    while run:

        screen.fill(BG)

        # use overlap for two
        col = GREEN
        if pygame.sprite.spritecollide(bullet, soldier_group, False):
            col = BLUE
            if pygame.sprite.spritecollide(bullet, soldier_group, False, pygame.sprite.collide_mask):
                col = RED
        else:
            col = GREEN

        bullet_group.update(col)

        soldier_group.draw(screen)
        bullet_group.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.draw.rect(screen, WHITE, soldier.rect, 1)
        pygame.display.flip()

    pygame.quit()