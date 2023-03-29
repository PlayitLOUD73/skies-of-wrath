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
        self.hp = 100

    def damage(self, x):
        self.hp -= x

    def shootBullet(self, model):
        bullet = Bullet(self.rect.centerx, self.rect.centery - 16, True)
        model.projectileGroup.add(bullet)


    def update(self, mousePos):

        # print(mousePos)

        # velocity = pygame.Vector2(velocity.x / 2.0, velocity.y / 2.0)
        velocity = pygame.math.Vector2()
        #difference = mousePos - pygame.math.Vector2(self.rect.centerx, self.rect.centery)

        difference = mousePos

        if difference.magnitude_squared() == 0:
            return

        if difference.magnitude_squared() > 100.0:
            difference.normalize()
            difference.scale_to_length(10.0)

        velocity = difference        
        #self.rect.center += velocity

        self.rect.centerx = self.rect.centerx + velocity.x
        self.rect.centery = self.rect.centery + velocity.y
        