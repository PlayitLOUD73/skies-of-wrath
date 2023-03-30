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

FPS = 60

controller = Controller()

while True:
    
    
    clock.tick(FPS)

    events = controller.get_events()
    
    if not controller.pauseStatus:
        model.update(events)

    view.update_screen(model)
