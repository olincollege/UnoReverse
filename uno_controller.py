"""
Controller for our Final Project's version of UNO
"""
#import pygame
import pygame, sys
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


    def handle_mouse_event(self, event):
        """
            Use this to help implement the mouse in an event
        """

        while True:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN: #need to add when to play card?
                    if event.button == 1:
                        clicking = True
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        clicking = False

            pygame.display.update()
            mainClock.tick(60)
                         
