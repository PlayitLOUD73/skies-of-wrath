import pygame
import os

class Ocean(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join('assets/', 'ocean.png'))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self):
        self.rect.topleft = self.rect.topleft[0], self.rect.topleft[1] + 1
        