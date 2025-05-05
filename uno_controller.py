"""
Controller for our Final Project's version of UNO
"""
#import pygame
import pygame
from pygame.locals import *

#setup pygame
mainClock = pygame.time.Clock()
pygame.init()

clicking = False

class MouseController:
    """
        Tell when the mouse is clicking on a button or a carrd
    """
    

    def __init__(self, model, rect):

        self._model = model
        self.clicked = False
        self.rect = rect
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()


    def mouse_controller_update(self, event):
        """
            Use this to help implement the mouse in an event
        """
            #track mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
        elif event.type == MOUSEBUTTONUP:
            if event. button == 1:
                clicking = False

    def interact_with_card(self, card):
        #if self.mouse_x within card_box and self.mouse_y within card box
            pygame.Rect.collidepoint
            card.image.get_rect().collidepoint
