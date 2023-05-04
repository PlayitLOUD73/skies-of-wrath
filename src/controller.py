import pygame, sys

class MouseEvent:
    
    def __init__(self, relX, relY, lmb, rmb):
        self.relX = relX
        self.relY = relY
        self.lmb = lmb
        self.rmb = rmb


class Controller:

    def __init__(self):
        self.pauseStatus = True
        self.pause()

    def pause(self):
        self.pauseStatus = not self.pauseStatus

        if self.pauseStatus:
            pygame.mouse.set_visible(True)
            pygame.event.set_grab(False)
        else:
            pygame.mouse.set_visible(False)
            pygame.event.set_grab(True)

    def get_events(self, model):

        exportKeys = []
        x, y = pygame.mouse.get_rel()

        mouse = MouseEvent(x, y, False, False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0] and model.state == 0:
                    mouse.lmb = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if model.state == 0:
                        self.pause()
                    else:
                        pygame.quit()
                        sys.exit()
                if event.key == pygame.K_RETURN:
                    if model.state != 0:
                        model.state = -1

        exportKeys.append(mouse)
        return exportKeys