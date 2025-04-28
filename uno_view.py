import pygame
import sys
from Source.uno_model import Card
from random import choice

class UnoPygameView:
    """
    UnoPygameView is a visual interface for a simplified UNO game using pygame.
    It only handles displaying elements and capturing user interactions.
    """

    def __init__(self, width=1000, height=650):
        """
        Initialize the game window, fonts, colors, buttons, and timer.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("✨ Fancy UNO Game ✨")
        self.font = pygame.font.SysFont("Arial Rounded MT Bold", 28)
        self.small_font = pygame.font.SysFont("Arial", 20)
        self.bg_color = (25, 25, 112)
        self.card_rects = []
        self.uno_button = pygame.Rect(850, 500, 100, 40)
        self.draw_button = pygame.Rect(850, 550, 100, 40)
        self.clock = pygame.time.Clock()
        self.timer = 30
        self.exit_button = pygame.Rect(850, 600, 100, 40)

    def draw_background(self):
        """
        Fill the screen with the background color.
        """
        self.screen.fill(self.bg_color)

    def draw_card(self, card, x, y):
        """
        Draw a single card at the given (x, y) position.

        Args:
            card (Card): The card object to draw.
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            pygame.Rect: The rectangle representing the drawn card.
        """
        card_color = self.get_color_from_suit(card.suit)
        rect = pygame.Rect(x, y, 90, 130)
        pygame.draw.rect(self.screen, (255, 255, 255), rect.inflate(6, 6), border_radius=12)
        pygame.draw.rect(self.screen, card_color, rect, border_radius=10)
        text_value = self.font.render(str(card.value), True, (255, 255, 255))
        text_rect = text_value.get_rect(center=(x + 45, y + 50))
        self.screen.blit(text_value, text_rect)
        text_suit = self.font.render(card.suit.title(), True, (255, 255, 255))
        text_suit_rect = text_suit.get_rect(center=(x + 45, y + 90))
        self.screen.blit(text_suit, text_suit_rect)
        return rect

    def get_color_from_suit(self, suit):
        """
        Get the RGB color for a given suit.

        Args:
            suit (str): The color suit name.

        Returns:
            tuple: RGB color value.
        """
        color_map = {
            "red": (220, 20, 60),
            "yellow": (255, 215, 0),
            "green": (50, 205, 50),
            "blue": (65, 105, 225),
            "wild": (100, 100, 100)
        }
        return color_map.get(suit, (200, 200, 200))

    def draw_hand(self, hand, y=440):
        """
        Draw all the cards in the player's hand.

        Args:
            hand (list of Card): List of card objects.
            y (int, optional): The y-coordinate to draw the hand. Defaults to 440.
        """
        self.card_rects = []
        for i, card in enumerate(hand):
            x = 110 + i * 100
            rect = self.draw_card(card, x, y)
            self.card_rects.append((rect, card))

    def draw_computer_hand(self, count):
        """
        Draw the computer's hand size as a number.

        Args:
            count (int): Number of cards in the computer's hand.
        """
        text = self.font.render(f"Computer Cards: {count}", True, (255, 255, 255))
        self.screen.blit(text, (50, 30))

    def draw_top_card(self, card):
        """
        Draw the top card of the discard pile.

        Args:
            card (Card): The top card object.
        """
        pygame.draw.rect(self.screen, (255, 255, 255), (400-3, 200-3, 96, 136), border_radius=12)
        self.draw_card(card, 400, 200)

    def draw_buttons(self):
        """
        Draw the 'UNO','Draw',and "Exit" action buttons.
        """
        pygame.draw.rect(self.screen, (255, 69, 0), self.uno_button, border_radius=8)
        uno_text = self.small_font.render("UNO!", True, (255, 255, 255))
        self.screen.blit(uno_text, self.uno_button.move(10, 8))
        pygame.draw.rect(self.screen, (0, 128, 0), self.draw_button, border_radius=8)
        draw_text = self.small_font.render("Draw", True, (255, 255, 255))
        self.screen.blit(draw_text, self.draw_button.move(10, 8))
        pygame.draw.rect(self.screen, (128, 0, 0), self.exit_button, border_radius=8)
        exit_text = self.small_font.render("Exit", True, (255, 255, 255))
        self.screen.blit(exit_text, self.exit_button.move(10, 8))

    def draw_timer(self):
        """
        Draw the countdown timer on the screen.
        """
        timer_text = self.small_font.render(f"Timer: {int(self.timer)}s", True, (255, 255, 255))
        self.screen.blit(timer_text, (850, 20))

    def update_display(self):
        """
        Update the full display surface to the screen.
        """
        pygame.display.flip()

    def wait_for_quit(self):
        """
        Handle the quit event to close the game window.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def get_clicked_card(self, pos):
        """
        Return the card clicked by the user, if any.

        Args:
            pos (tuple): Mouse position (x, y).

        Returns:
            Card or None: The clicked card object, or None if no card was clicked.
        """
        for rect, card in self.card_rects:
            if rect.collidepoint(pos):
                return card
        return None

    def reset_timer(self):
        """
        Reset the countdown timer back to 30 seconds.
        """
        self.timer = 30

if __name__ == "__main__":
    view = UnoPygameView()
    fake_hand = [Card(choice(["red", "green", "yellow", "blue"]), i, None, None) for i in range(1, 6)]
    for c in fake_hand:
        c.function = None

    top_card = Card("blue", 5, None, None)
    computer_hand_count = 5

    while True:
        # --- draw everything ---
        view.draw_background()
        view.draw_hand(fake_hand)
        view.draw_top_card(top_card)
        view.draw_computer_hand(computer_hand_count)
        view.draw_buttons()
        view.draw_timer()
        view.update_display()

        # --- update timer ---
        view.clock.tick(60)
        view.timer = max(0, view.timer - 1 / 60)

        # --- handle events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if view.exit_button.collidepoint(pos):
                    pygame.quit()
                    sys.exit()

                # let controller handle clicks:
                if view.uno_button.collidepoint(pos):
                    print("UNO called!")

                elif view.draw_button.collidepoint(pos):
                    # controller decides what happens when draw is clicked
                    new_card = Card(choice(["red", "green", "yellow", "blue"]), choice(range(1, 10)), None, None)
                    fake_hand.append(new_card)

                else:
                    clicked_card = view.get_clicked_card(pos)
                    if clicked_card:
                        # controller decides what happens when a card is clicked
                        print(f"Card {clicked_card.suit} {clicked_card.value} clicked")
                        # Example logic: remove and update top card
                        fake_hand.remove(clicked_card)
                        top_card = clicked_card
                        view.reset_timer()