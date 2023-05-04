import pygame
from src.player import Player
from src.controller import MouseEvent
from src.textures.ocean import Ocean
from src.enemies.ufo import UFO
from src.textures.bulletExplosion import BulletExplosion
from src.textures.shipExplosion import ShipExplosion
from src.systems.spawnController import SpawnController
#from src.systems.laser import Laser
from src.enemies.advancedUfo import AdvancedUFO

from src.systems.powerups import powerupController

from src.systems.soundEffects import Sounds

class Model:

    def setup(self):
        player = Player()

        self.playerGroup = pygame.sprite.GroupSingle()
        self.playerGroup.add(player)

        
        
        self.enemyGroup = pygame.sprite.Group()

        self.projectileGroup = pygame.sprite.Group()
        self.animationGroup = pygame.sprite.Group()

        self.powerupGroup = pygame.sprite.Group()

        self.spawnController = SpawnController(self)

        self.sound = Sounds()

        self.score = 0

        # 0 -> normal
        # 1 -> gameOver
        self.state = 0

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
        
        newUFO = UFO(100, 100)

        self.enemyGroup.add(newUFO)


    def checkCollisions(self):


        # projectiles and projectiles

        #col = pygame.sprite.groupcollide(self.projectileGroup, self.projectileGroup, True, True)

        # projectiles and enemies

        col = pygame.sprite.groupcollide(self.enemyGroup, self.projectileGroup, False, True)

        for x in col:
            for y in col[x]:
                explosion = BulletExplosion(y.rect.centerx, y.rect.centery)
                self.animationGroup.add(explosion)
            x.damage(10)
            if x.hp <= 0:
                explosion = ShipExplosion(x.rect.centerx, x.rect.centery)
                self.animationGroup.add(explosion)
                self.score += x.score
                newPowerup = powerupController.powerUpHandler(x.rect.centerx, x.rect.centery)
                if newPowerup is not None:
                    self.powerupGroup.add(newPowerup)
                self.sound.playExplosion()
                x.kill()

        # projectiles and player
        if self.playerGroup.sprite is not None:
            col = pygame.sprite.spritecollide(self.playerGroup.sprite, self.projectileGroup, True)

            for x in col:
                self.playerGroup.sprite.damage(10)
                if self.playerGroup.sprite.hp <= 0:
                    explosion = ShipExplosion(self.playerGroup.sprite.rect.centerx, self.playerGroup.sprite.rect.centery)
                    self.animationGroup.add(explosion)
                    self.state = 1
                    self.playerGroup.sprite.kill()
                    return

        # player and enemies
        if self.playerGroup.sprite is not None:
            col = pygame.sprite.spritecollide(self.playerGroup.sprite, self.enemyGroup, True)

            for x in col:
                explosion = ShipExplosion(self.playerGroup.sprite.rect.centerx, self.playerGroup.sprite.rect.centery)
                self.animationGroup.add(explosion)
                self.state = 1 # game over state
                self.playerGroup.sprite.kill()  
                explosion = ShipExplosion(x.rect.centerx, x.rect.centery)
                self.animationGroup.add(explosion)
                x.kill()

        # player and powerups
        if self.playerGroup.sprite is not None:
            col = pygame.sprite.spritecollide(self.playerGroup.sprite, self.powerupGroup, True)

            for x in col:
                x.powerup(self, self.playerGroup.sprite)



    def readInput(self, events):
        x = 0
        y = 0
        for event in events:
            if isinstance(event, MouseEvent):
                if event.lmb:
                    self.playerGroup.sprite.shootBullet(self)
                    self.sound.playLaser()
                x = event.relX
                y = event.relY

        return pygame.Vector2(x, y)


    def update(self, events):

        velocity = self.readInput(events)
        mx, my = pygame.mouse.get_pos()

        if self.state == 0:
            self.playerGroup.update(velocity)
            self.spawnController.update()
            self.checkCollisions()

        self.projectileGroup.update()
        self.powerupGroup.update()
        # self.backgroundGroup.update()
        self.enemyGroup.update(self)
        self.animationGroup.update()
        
        


        pass