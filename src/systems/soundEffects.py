import pygame
import os

class Sounds():

    def __init__(self):

        pygame.mixer.init()
        self.explosion = pygame.mixer.Sound(os.path.join('assets/sounds', 'explosion.wav'))
        self.laser = pygame.mixer.Sound(os.path.join('assets/sounds', 'laser.wav'))
        self.heal = pygame.mixer.Sound(os.path.join('assets/sounds', 'heal.wav'))
    
    def playExplosion(self):
        self.explosion.play()

    def playLaser(self):
        self.laser.play()

    def playHeal(self):
        self.heal.play()

    def stopSounds(self):
        pygame.mixer.stop()