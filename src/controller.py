import pygame, sys

class Controller:

    def get_events(self):
        exportKeys = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            exportKeys.append(pygame.K_UP)
        elif keys[pygame.K_DOWN]:
            exportKeys.append(pygame.K_DOWN)
        elif keys[pygame.K_LEFT]:
            exportKeys.append(pygame.K_LEFT)
        elif keys[pygame.K_RIGHT]:
            exportKeys.append(pygame.K_RIGHT)

        return exportKeys