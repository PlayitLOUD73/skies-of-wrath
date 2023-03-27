import pygame, sys

class MouseEvent:
    
    def __init__(self, relX, relY, lmb, rmb):
        self.relX = relX
        self.relY = relY
        self.lmb = lmb
        self.rmb = rmb


class Controller:

    

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
        


        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            exportKeys.append(pygame.K_UP)
        elif keys[pygame.K_DOWN]:
            exportKeys.append(pygame.K_DOWN)
        elif keys[pygame.K_LEFT]:
            exportKeys.append(pygame.K_LEFT)
        elif keys[pygame.K_RIGHT]:
            exportKeys.append(pygame.K_RIGHT)

        exportKeys.append(mouse)
        return exportKeys