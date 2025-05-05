"""
Controller for our Final Project's version of UNO
"""
import pygame
#from Source.uno_model import UNOGAMEMODEL

class MouseController:
    """
        Insert more finalized doctstring later
    """
    def __init__(self, model):

        self._model = model


    def handle_mouse_event(self, event):
        while True:
            for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        return
                    elif event.type == MOUSEWHEEL:
                        print(event)
                        print(event.x, event.y)
                        print(event.flipped)
                        print(event.which)
            clock.tick(60)
