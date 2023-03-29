import pygame
from src.player import Player
from src.controller import MouseEvent
from src.textures.ocean import Ocean
from src.enemies.ufo import UFO

class Model:

    def setup(self):
        player = Player()

        self.playerGroup = pygame.sprite.GroupSingle()
        self.playerGroup.add(player)
        
        self.enemyGroup = pygame.sprite.Group()
        
        self.spawnUFO()

        self.projectileGroup = pygame.sprite.Group()
        #pygame.mouse.set_pos((256,256))
        #print(pygame.mouse.get_pos())
        #print(pygame.mouse.get_visible())

        self.createBackground()

    def createBackground(self):
        
        self.backgroundGroup = pygame.sprite.Group()
        
        for i in range(8):
            for j in range(12):
                oceanTile = Ocean(i*64, j*64)
                self.backgroundGroup.add(oceanTile)
            for j in range(12):
                oceanTile = Ocean(i*64, j*-64)
                self.backgroundGroup.add(oceanTile)

    def spawnUFO(self):
        
        newUFO = UFO()

        self.enemyGroup.add(newUFO)


    def checkCollisions(self):

        # projectiles and enemies

        col = pygame.sprite.groupcollide(self.enemyGroup, self.projectileGroup, False, True)

        for x in col:
            x.damage(10)
            if x.hp <= 0:
                x.kill()

        # projectiles and player
        if self.playerGroup.sprite is not None:
            col = pygame.sprite.spritecollide(self.playerGroup.sprite, self.projectileGroup, True)

            for x in col:
                self.playerGroup.sprite.damage(10)
                if self.playerGroup.sprite.hp <= 0:
                    self.playerGroup.sprite.kill()


    def readInput(self, events):
        x = 0
        y = 0
        for event in events:
            if isinstance(event, MouseEvent):
                if event.lmb:
                    self.playerGroup.sprite.shootBullet(self)
                x = event.relX
                y = event.relY

        return pygame.Vector2(x, y)


    def update(self, events):

        velocity = self.readInput(events)
        mx, my = pygame.mouse.get_pos()

        self.playerGroup.update(velocity)
        self.projectileGroup.update()
        self.backgroundGroup.update()
        self.enemyGroup.update(self)
        self.checkCollisions()


        pass