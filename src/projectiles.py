import pygame
import os

class Bullet(pygame.sprite.Sprite):

    # need to implement direction
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join('assets/projectiles', 'bullet2.png'))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        if direction:
            self.speed = 15.0
        else:
            self.speed = -15.0
    
    def update(self):
        self.rect.centery -= self.speed