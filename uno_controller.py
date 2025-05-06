"""
Controller for our Final Project's version of UNO
"""

# import pygame
import pygame
from pygame.locals import *

from Source.uno_model import UNOGAMEMODEL

# setup pygame


class MouseController:
    """
    Tell when the mouse is clicking on a button or a carrd
    """

    def __init__(self, model):

        self._model = model
        self.clicked = False
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def mouse_controller_update(self, event):
        """
        Use this to help implement the mouse in an event
        """

        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        if event.type == MOUSEBUTTONDOWN:
            self.clicked = True
        if event.type == MOUSEBUTTONUP:
            self.clicked = False

    def interact_with_card(self, model):
        """
        Controls how player interacts with card objects
        """

        for i, _ in enumerate((model.player_hand)):

            if model.player_hand[i].rect.collidepoint(
                self.mouse_x, self.mouse_y
            ) and model.is_card_valid_move(model.player_hand[i]):
                model.human_players_turn(i)
                break

    def interact_with_uno_button(self, model, uno_button):
        """
        Sets up the UNO button

        Args:
            model: An instance of a class representing the model component of the program
            uno_button: _description_
        """
        if (
            uno_button.collidepoint(self.mouse_x, self.mouse_y)
            and model.check_player_uno()
        ):
            model.call_uno()

    def interact_with_uno_out_button(self, model, uno_out_button):
        """
        Sets up the UNO OUT button

        Args:
            model: An instance of a class representing the model component of the program
            uno_out_button: A button type
        """
        if uno_out_button.collidepoint(self.mouse_x, self.mouse_y):
            model.call_uno_out()
            model.check_for_winner()
            # model.declare_winner()

    def interact_with_draw_button(self, model, draw_button):
        """
        Sets up the draw button

        Args:
            model: An instance of a class representing the model component of the program
            draw_button: _description_
        """
        if draw_button.collidepoint(self.mouse_x, self.mouse_y):
            model.pick_a_card(model.deck.human_deck.hand)
