import pygame
import os

from src.textures.animation import Animation

class LaserBody(Animation):
    def __init__(self, x, y):
        
        Animation.__init__(self, x, y, 'laserBody', 2, 200, 8)

class Laser():

    def __init__(self, x, y, model):
        
        
        self.l = pygame.sprite.Group()
        i = 0

        while (i * 16 < 768):
            laserBody = LaserBody(x, y + (i * 16))
            model.animationGroup.add(laserBody)
            model.projectileGroup.add(laserBody)
            self.l.add(laserBody)
            i += 1

    def update(self):
        pass

        