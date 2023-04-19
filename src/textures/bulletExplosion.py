import pygame
import os

from src.textures.animation import Animation

class BulletExplosion(Animation):

    def __init__(self, x, y):

        Animation.__init__(self, x, y, 'bulletExplosion', 7, 7, 2)



