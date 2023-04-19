import pygame
import os
import random

from src.systems.laser import Laser

class AdvancedUFO(pygame.sprite.Sprite):

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join('assets/enemies', 'advancedUfo.png'))
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.hp = 50

        self.score = 500

        self.laserIter = -1

        self.firing = False
        self.laser = None

    def shootLaser(self, model):
        self.laser = Laser(self.rect.center[0], self.rect.center[1] + 24, model)
        self.firing = True

    def move(self):
        if self.rect.center[1] <= 64:
            self.rect.move_ip(0, 1)

    def damage(self, x):
        self.hp -= x

    def update(self, model):
        if self.laser is not None:
            if len(self.laser.l.sprites()) == 0:
                self.firing = False

        self.move()
        if self.rect.y >= 32:
            if self.firing == False:
                self.laserIter += 1
            if self.laserIter % 240 == 0 and not self.firing:
                self.shootLaser(model)