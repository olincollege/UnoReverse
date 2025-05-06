"""
This module defines the View class for the UNO game using the Pygame library,
including the background setup, buttons
and displaying the player's hand and the last card being played

"""

import pygame
from Source.uno_model import UNOGAMEMODEL
import sprite_sheet


class View:
    """
    View class for the UNO game using Pygame.

    This class is responsible for rendering the graphical interface of the game.
    It initializes the game window, sets colors and fonts, and draws elements such
    as the background and control buttons. It also provides getter methods to retrieve
    visual-related game state like the top card, player's hand, and computer's hand count.

    """

    pygame.init()

    def __init__(self, model):
        self.screen_width = 1400
        self.screen_height = 800
        self.background_color = (211, 153, 242)
        # setup for regular cards:
        sprite_sheet_regular = pygame.image.load(
            "Assets/Uno_Cards_numbers.png"
        ).convert_alpha()
        self.regular_card_sheet = sprite_sheet.SpriteSheet(sprite_sheet_regular)
        # setup for special cards:
        sprite_sheet_special = pygame.image.load(
            "Assets/Uno_Cards_Special.png"
        ).convert_alpha()
        self.special_card_sheet = sprite_sheet.SpriteSheet(sprite_sheet_special)
        # self.red = (200, 50, 50)
        # self.green = (50, 200, 50)
        # self.blue = (50, 50, 200)
        # self.yellow = (240, 240, 50)
        self.gray = (100, 100, 100)
        self.text = (255, 255, 255)
        self.font = pygame.font.Font(None, 36)
        self.buttons = {}
        self.model = model

    def draw_background(self, screen):
        """Fill the background with the determined color"""
        screen.fill(self.background_color)

    def draw_buttons(self, screen):
        """Draw needed buttons--Draw, UNO, and Pass at the right bottom of the screen"""
        button_width = 100
        button_height = 40
        position_y = self.screen_height - 80
        horizontal_center = self.screen_width // 2
        # Draw Card
        draw_button_position_x = horizontal_center - 170
        draw_button = pygame.Rect(
            draw_button_position_x, position_y, button_width, button_height
        )
        self.buttons["Draw"] = draw_button
        pygame.draw.rect(screen, self.gray, draw_button)
        text_draw = self.font.render("Draw", True, self.text)
        text_draw_rectangle = text_draw.get_rect(center=draw_button.center)
        screen.blit(text_draw, text_draw_rectangle)
        # UNO
        uno_button_position_x = horizontal_center - 50
        uno_button = pygame.Rect(
            uno_button_position_x, position_y, button_width, button_height
        )
        self.buttons["UNO"] = uno_button
        pygame.draw.rect(screen, self.gray, uno_button)
        text_uno = self.font.render("UNO", True, self.text)
        text_uno_rectangle = text_draw.get_rect(center=uno_button.center)
        screen.blit(text_uno, text_uno_rectangle)
        # uno_out
        uno_out_button_position_x = horizontal_center + 70
        uno_out_button = pygame.Rect(
            uno_out_button_position_x, position_y, button_width + 70, button_height
        )
        self.buttons["UNO OUT"] = uno_out_button
        pygame.draw.rect(screen, self.gray, uno_out_button)
        text_uno_out = self.font.render("UNO OUT", True, self.text)
        text_uno_out_rectangle = text_draw.get_rect(center=uno_out_button.center)
        screen.blit(text_uno_out, text_uno_out_rectangle)

    def draw_player_hand(self, screen):
        """
        Render the player's hand using images uploaded
        """
        x_position = 0
        for card in self.model.player_hand:
            screen.blit(card.image, (x_position, 150))
            x_position += 150

    def draw_top_card(self, screen):
        """
        Show the image of the last card played on the deck
        """
        screen.blit(
            self.model.deck.played_cards[-1].image,
            (self.screen_width // 2, self.screen_height // 2),
        )

    def display_win_message(self, screen, winner):
        """
        Displays a message declaring the winner of an UNO game

        Args:
            winner: A string type representing the player who has won an UNO game
        """
        winner_text = self.font.render(
            f"The winner is {winner}!!!!!!!", True, (225, 225, 225)
        )
        screen.blit(winner_text, (550, 340))


# if __name__ == "__main__":
#     import pygame

#     pygame.init()

#     clock = pygame.time.Clock()
#     screen = pygame.display.set_mode((1400, 800))
#     view = View(UNOGAMEMODEL([]))

#     # Create fake card surfaces for testing
#     red_card = pygame.Surface((100, 150))
#     red_card.fill((255, 0, 0))
#     blue_card = pygame.Surface((100, 150))
#     blue_card.fill((0, 0, 255))

#     player_hand = [red_card] * 5  # 5 red cards
#     top_card = blue_card  # blue top card

#     RUNNING = True
#     while RUNNING:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 RUNNING = False

#         view.draw_background(screen)
#         view.draw_buttons(screen)
#         # view.draw_player_hand(screen)
#         view.draw_top_card(screen)
#         view.display_win_message(screen, "YOU")
#         pygame.display.flip()
#         clock.tick(30)

#     pygame.quit()
