import pygame
from src.view import View
from src.entities.player import Player
from src.controller import Controller

clock = pygame.time.Clock()
clock.tick(60)

ents = []

view = View()
view.view_init()

controller = Controller()

player = Player()

while True:
    
    events = controller.get_events()
    
    # model.update(events)

    view.update_screen(player)
