import pygame
import random

from src.systems.powerups.healthUp import HealthUp

def powerUpHandler(x, y):

    if random.randrange(20) < 4:
        return HealthUp(x, y)
    else:
        return None