import pygame
#from model import Model

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 512, 720
screenColor = (0,0,0)

class View:

    def view_init(self):
        pygame.display.set_caption("Skies of Wrath")
        self.surface = pygame.display.set_mode(SCREEN_SIZE)
    
    def update_screen(self, model):

        self.surface.fill(screenColor)

        model.playerGroup.draw(self.surface)
        model.projectileGroup.draw(self.surface)

        # self.surface.blit(model.player.player.image, model.player.player.rect)

        pygame.display.update()