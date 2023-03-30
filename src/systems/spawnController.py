import pygame
import random
from src.enemies.ufo import UFO

class SpawnController:

    def __init__(self, parent):
        self.parent = parent


    def spawnEnemyWave(self, num):
        
        tiles = []

        for i in range(num):
            num = random.randrange(16)
            while num in tiles:
                num = random.randrange(16)
            tiles.append(num)

        for x in tiles:
            ufo = UFO(32 * x, -32)
            self.parent.enemyGroup.add(ufo)
    def update(self):
        if len(self.parent.enemyGroup.sprites()) == 0:
            self.spawnEnemyWave(random.randrange(8)+2)