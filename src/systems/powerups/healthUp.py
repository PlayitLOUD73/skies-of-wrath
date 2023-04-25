import pygame
import os

from src.systems.powerups.powerup import Powerup

class HealthUp(Powerup):

    def __init__(self, x, y):

        Powerup.__init__(self, 'heartPowerup.png', x, y)

    def powerup(self, player):
        player.hp = 100