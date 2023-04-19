import pygame
import os

class Animation(pygame.sprite.Sprite):

    def __init__(self, x, y, name, frames, total, speed):

        pygame.sprite.Sprite.__init__(self)

        self.speed = speed

        self.anim = []
        self.frames = frames
        self.total = total * 2
        for i in range(frames):
            fileName = name + str(i+1) + '.png'
            self.anim.append(pygame.image.load(os.path.join('assets/animations/' + name, fileName)))

        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = x,y

        self.iteration = 0

    def update(self):
        self.iteration += 1
        if self.iteration >= self.total:
            self.kill()
        elif self.iteration % self.speed == 0: 
            self.image = self.anim[int(self.iteration / self.speed) % self.frames]