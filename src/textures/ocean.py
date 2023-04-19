import pygame
import os

class Ocean(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.pos = x,y
        self.image = pygame.image.load(os.path.join('assets/', 'ocean.png'))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self):
        self.pos = self.pos[0], self.pos[1] + 0.5
        
        if self.pos[1] >= 768.0:
            self.pos = self.pos[0], -704.0

        self.rect.topleft = self.pos
