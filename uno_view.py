import pygame
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
    # setup for regular cards:
    sprite_sheet_regular = pygame.image.load(
        "Assets/Uno_Cards_numbers.png"
    ).convert_alpha()
    regular_card_sheet = sprite_sheet.SpriteSheet(sprite_sheet_regular)

    # setup for special cards:
    sprite_sheet_special = pygame.image.load(
        "Assets/Uno_Cards_Special.png"
    ).convert_alpha()
    special_card_sheet = sprite_sheet.SpriteSheet(sprite_sheet_special)

    def __init__(self):
        self.screen_width = 1400
        self.screen_height = 800
        self.background_color = (211, 153, 242)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("UNO Game")
        self.red = (200, 50, 50)
        self.green = (50, 200, 50)
        self.blue = (50, 50, 200)
        self.yellow = (240, 240, 50)
        self.gray = (100, 100, 100)
        self.text = (255, 255, 255)
        self.font = pygame.font.Font(None, 36)
        self.buttons = {}

    def draw_background(self):
        """Fill the background with the determined color"""
        self.screen.fill(self.background_color)

    def draw_buttons(self):
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
        pygame.draw.rect(self.screen, self.gray, draw_button)
        text_draw = self.font.render("Draw", True, self.text)
        text_draw_rectangle = text_draw.get_rect(center=draw_button.center)
        self.screen.blit(text_draw, text_draw_rectangle)
        # UNO
        uno_button_position_x = horizontal_center - 50
        uno_button = pygame.Rect(
            uno_button_position_x, position_y, button_width, button_height
        )
        self.buttons["UNO"] = uno_button
        pygame.draw.rect(self.screen, self.gray, uno_button)
        text_uno = self.font.render("UNO", True, self.text)
        text_uno_rectangle = text_draw.get_rect(center=uno_button.center)
        self.screen.blit(text_uno, text_uno_rectangle)
        # uno_out
        uno_out_button_position_x = horizontal_center
        uno_out_button = pygame.Rect(
            uno_out_button_position_x, position_y, button_width, button_height
        )
        self.buttons["UNO OUT"] = uno_out_button
        pygame.draw.rect(self.screen, self.gray, uno_out_button)
        text_uno_out = self.font.render("UNO OUT", True, self.text)
        text_uno_out_rectangle = text_draw.get_rect(center=uno_out_button.center)
        self.screen.blit(text_uno_out, text_uno_out_rectangle)
        # Pass
        pass_button_position_x = horizontal_center + 70
        pass_button = pygame.Rect(
            pass_button_position_x, position_y, button_width, button_height
        )
        self.buttons["Pass"] = pass_button
        pygame.draw.rect(self.screen, self.gray, pass_button)
        text_pass = self.font.render("Pass", True, self.text)
        text_pass_rectangle = text_draw.get_rect(center=pass_button.center)
        self.screen.blit(text_pass, text_pass_rectangle)

    def draw_player_hand(self, player_hand):
        """Render the player's hand using images uploaded"""
        pass

    def draw_top_card(self, top_of_deck):
        """show the image of the last card played on the deck"""
        pass

    def display_win_message(self, winner):
        """
        Displays a message declaring the winner of an UNO game

        Args:
            winner: A string type representing the player who has won an UNO game
        """
        winner_text = self.font.render(
            f"The winner is {winner}!!!!!!!", True, (255, 255, 255)
        )
        self.screen.blit(winner_text, (550, 400))
