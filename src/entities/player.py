import pygame
import os

class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join('assets/player', 'player.png'))
        self.rect = self.image.get_rect()