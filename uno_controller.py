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
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self.clicked = True
        elif event.type == MOUSEBUTTONUP:
            if event. button == 1:
                self.clicked = False

    def interact_with_card(self, model):
        """
            controls how player interacts with card objects
        """

        for i, _ in enumerate((model.player_hand)):
            if model.player_hand[i].image.get_rect().collidepoint(self.mouse_x, self.mouse_y) \
            and model.is_valid_move(model.player_hand[i]):
                model.human_players_turn(model.player_hand[i])
                break

    def interact_with_uno_button(self, model, uno_button):

        if uno_button.collidepoint(self.mouse_x, self.mouse_y):
            model.check_player_uno()
            model.call_uno()

    def interact_with_uno_out_button(self, model, uno_out_button):

        if uno_out_button.collidepoint(self.mouse_x, model, self.mouse_y):
            model.check_for_winner()
            model.call_uno_out()
            model.declare_winner()

    def interact_with_draw_button(self, model, draw_button):

        if draw_button.collidepoint(self.mouse_x, self.mouse_y):
            model._plus_card_effect()

