import pygame
import os
#from src.model import Model
from src.projectiles import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join('assets/player', 'player.png'))
        self.rect = self.image.get_rect()
        self.rect.centerx = 256
        self.rect.centery = 700

    def shootBullet(self, model):
        bullet = Bullet(self.rect.centerx, self.rect.centery - 16, True)
        model.projectileGroup.add(bullet)



    def update(self, velocity):

        # velocity = pygame.Vector2(velocity.x / 2.0, velocity.y / 2.0)

        self.rect.center = velocity
        
        
        pass