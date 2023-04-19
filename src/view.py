import pygame
#from model import Model

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 512, 768
screenColor = (0,0,0)
white = (255, 255, 255)

class View:

    def view_init(self):
        pygame.display.set_caption("Skies of Wrath")
        self.surface = pygame.display.set_mode(SCREEN_SIZE)
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 16)
        self.largeFont = pygame.font.Font(pygame.font.get_default_font(), 32)
    
    def fonts(self, score, state):
        testText = self.font.render(str(score), True, white, screenColor)

        gameOverText = self.largeFont.render("Game Over", True, white, screenColor)

        testRect = testText.get_rect()
        testRect.topleft = (24, 24)

        gameRect = gameOverText.get_rect()
        gameRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

        if state == 1:
            self.surface.blit(gameOverText, gameRect)

        self.surface.blit(testText, testRect)

    def update_screen(self, model):



        self.surface.fill(screenColor)

        # model.backgroundGroup.draw(self.surface)
        
        model.playerGroup.draw(self.surface)
        model.projectileGroup.draw(self.surface)

        model.enemyGroup.draw(self.surface)

        model.animationGroup.draw(self.surface)

        self.fonts(model.score, model.state)

        # self.surface.blit(model.player.player.image, model.player.player.rect)

        pygame.display.update()