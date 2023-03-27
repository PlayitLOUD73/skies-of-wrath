import pygame
from src.player import Player
from src.controller import MouseEvent

class Model:

    def setup(self):
        player = Player()

        self.player = player
        self.playerGroup = pygame.sprite.Group()
        self.playerGroup.add(player)
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)

        self.projectileGroup = pygame.sprite.Group()
        #pygame.mouse.set_pos((256,256))
        #print(pygame.mouse.get_pos())
        #print(pygame.mouse.get_visible())
    def readInput(self, events):
        x = 0
        y = 0
        for event in events:
            if isinstance(event, MouseEvent):
                if event.lmb:
                    self.player.shootBullet(self)
                x = event.relX
                y = event.relY
        
        return pygame.Vector2(x, y)


    def update(self, events):

        velocity = self.readInput(events)
        mx, my = pygame.mouse.get_pos()

        self.playerGroup.update(velocity)
        self.projectileGroup.update()

        pass