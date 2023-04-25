import pygame
import os

class Powerup(pygame.sprite.Sprite):

    def __init__(self, fileName, x, y):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets/powerups', fileName))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        
        self.rect.center = (self.rect.centerx, self.rect.centery + 1.0)

        if self.rect.centery > 800:
            self.kill()