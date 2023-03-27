import pygame
from src.view import View
#from player import Player
from src.controller import Controller
from src.model import Model

clock = pygame.time.Clock()


ents = []

view = View()
view.view_init()

model = Model()
model.setup()

controller = Controller()

while True:
    
    
    clock.tick(60)

    events = controller.get_events()
    
    if not controller.pauseStatus:
        model.update(events)

    view.update_screen(model)
