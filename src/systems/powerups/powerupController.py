import pygame
import random

from src.systems.powerups.healthUp import HealthUp

def powerUpHandler(x, y):

    if random.randrange(20) < 4:
        print("success")
        return HealthUp(x, y)
    else:
        print("fail")
        return None