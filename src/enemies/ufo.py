import pygame
import os

from src.projectiles import Bullet

class UFO(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join('assets/enemies', 'ufo.png'))
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 256
        self.hp = 30

    def shootBullet(self, model):
        bullet = Bullet(self.rect.centerx, self.rect.centery + 24, False)
        model.projectileGroup.add(bullet)

    def damage(self, x):
        self.hp -= x

    def update(self, model):
        #self.shootBullet(model)
        pass