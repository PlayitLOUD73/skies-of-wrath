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

    def healthBar(self, health):
        
        if health <= 70 and health >= 40:
            color = (255, 255, 0)
        elif health < 40:
            color = (255, 0, 0)
        else:
            color = (0, 255, 0)

        healthRect = pygame.rect.Rect(400, 10, health, 10)
        pygame.draw.rect(self.surface, color, healthRect)

    
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

        model.powerupGroup.draw(self.surface)

        model.animationGroup.draw(self.surface)

        self.fonts(model.score, model.state)

        if model.state == 0:
            self.healthBar(model.playerGroup.sprite.hp)

        # self.surface.blit(model.player.player.image, model.player.player.rect)

        pygame.display.update()