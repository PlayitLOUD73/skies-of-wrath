import pygame

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 512, 720
screenColor = (0,0,0)

class View:

    def view_init(self):
        pygame.display.set_caption("Skies of Wrath")
        self.surface = pygame.display.set_mode(SCREEN_SIZE)
    
    def update_screen(self, player):

        self.surface.fill(screenColor)

        self.surface.blit(player.image, player.rect)

        pygame.display.update()