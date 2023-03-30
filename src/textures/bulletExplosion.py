import pygame
import os

class BulletExplosion(pygame.sprite.Sprite):

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.anim = [0,1,2,3,4,5,6]

        for i in range(7):
            fileName = 'bulletExplosion' + str(i+1) + '.png'
            self.anim[i] = pygame.image.load(os.path.join('assets/animations/bulletExplosion', fileName))

        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = x,y
        self.iteration = 0

    def update(self):

        self.iteration += 1
        if self.iteration >= 14:
            self.kill()
        elif self.iteration % 2 == 0: 
            self.image = self.anim[int(self.iteration / 2)]



