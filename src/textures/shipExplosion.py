import pygame
import os

from src.textures.animation import Animation

class ShipExplosion(Animation):

    def __init__(self, x, y):
        Animation.__init__(self, x, y, 'shipExplosion', 12)