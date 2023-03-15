import pygame
from src.player import Player

class Model:

    def setup(self):
        player = Player()

        self.player = player
        self.playerGroup = pygame.sprite.Group()
        self.playerGroup.add(player)
        pygame.mouse.set_visible(False)

        self.projectileGroup = pygame.sprite.Group()
        #pygame.mouse.set_pos((256,256))
        #print(pygame.mouse.get_pos())
        #print(pygame.mouse.get_visible())
    def readInput(self, events):
        x = 0
        y = 0
        for event in events:
            if event == pygame.K_UP:
                y = -1
            if event == pygame.K_DOWN:
                y = 1
            if event == pygame.K_RIGHT:
                x = 1
            if event == pygame.K_LEFT:
                x = -1
            if event == "LMB":
                self.player.shootBullet(self)
        
        return pygame.Vector2(x, y)


    def update(self, events):

        velocity = self.readInput(events)
        mx, my = pygame.mouse.get_pos()

        self.playerGroup.update(pygame.Vector2(mx, my))
        self.projectileGroup.update()

        pass