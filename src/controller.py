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

    def get_events(self):
        
        sensitivity = 1

        exportKeys = []
        x, y = pygame.mouse.get_rel()
        #print(x, y)

        #x = x * sensitivity
        #y = y * sensitivity

        # if abs(x) > 40:
        #     x = 40
        # if abs(y) > 40:
        #     y = 40

        # print(x, y)

        mouse = MouseEvent(x, y, False, False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    #exportKeys.append("LMB")
                    mouse.lmb = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pause()

        exportKeys.append(mouse)
        return exportKeys