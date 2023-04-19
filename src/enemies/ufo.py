import pygame
import os
import random

from src.projectiles import Bullet

class UFO(pygame.sprite.Sprite):

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join('assets/enemies', 'ufo.png'))
        self.rect = self.image.get_rect()
        self.rect.center = x,y
        self.hp = 20

        self.shoot = False

        self.bulletIter = -1

        self.bulletTimer = 0

        self.speed = random.randrange(3) + 2

        self.score = 100

    def shootBullet(self, model):
        bullet = Bullet(self.rect.centerx, self.rect.centery + 24, False)
        model.projectileGroup.add(bullet)

    def damage(self, x):
        self.hp -= x

    def move(self):
        self.rect.move_ip(0, self.speed)

    def update(self, model):
        
        # shooting logic

        self.bulletIter += 1
        if self.bulletIter % 60 == 0:
            if random.randrange(3) == 0:
                self.shootBullet(model)
        
        #     self.shoot = True
        # if self.shoot:
        #     if self.bulletIter % 4 == 0:
        #         self.bulletTimer += 1
        #         self.shootBullet(model)
        #     if self.bulletTimer % 3 == 0:
        #         self.shoot = False

        # move

        self.move()

        if self.rect.centery >= 820:
            self.kill()