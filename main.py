import pygame
from src.view import View
#from player import Player
from src.controller import Controller
from src.model import Model

clock = pygame.time.Clock()


ents = []

model = Model()
model.setup()

model.state = 2

view = View()
view.view_init()

FPS = 60

controller = Controller()

while True:
    
    
    clock.tick(FPS)

    events = controller.get_events(model)
    
    if not controller.pauseStatus and model.state != 2:
        model.update(events)

        if model.state == -1:
            model.setup()

    view.update_screen(model)
