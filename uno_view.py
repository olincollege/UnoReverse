import pygame


class View:
    """
    View class for the UNO game using Pygame.

    This class is responsible for rendering the graphical interface of the game.
    It initializes the game window, sets colors and fonts, and draws elements such
    as the background and control buttons. It also provides getter methods to retrieve
    visual-related game state like the top card, player's hand, and computer's hand count.

    """

    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 900
        self.background_color = (30, 120, 30)
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

    def load_card_images(self, spreadsheet_path):
        """Load all the card images listed in the spreadsheet and store them in a dictionary."""
        pass

    def draw_player_hand(self, player_hand):
        """Render the player's hand using images uploaded"""
        pass

    def draw_top_card(self, top_card):
        """show the image of the last card played on the deck"""
        pass
