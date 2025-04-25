import pygame
import sys
from Source.uno_model import Card
from random import choice

class UnoPygameView:
    def __init__(self, width=900, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("✨ Fancy UNO Game ✨")
        self.font = pygame.font.SysFont("Arial Rounded MT Bold", 28)
        self.bg_color = (25, 25, 112)  # dark blue
        self.card_rects = []

    def draw_background(self):
        self.screen.fill(self.bg_color)

    def draw_card(self, card, x, y):
        card_color = self.get_color_from_suit(card.suit)
        rect = pygame.Rect(x, y, 90, 130)
        pygame.draw.rect(self.screen, (255, 255, 255), rect.inflate(6, 6), border_radius=12)  # white border
        pygame.draw.rect(self.screen, card_color, rect, border_radius=10)

        # Draw value centered
        text_value = self.font.render(str(card.value), True, (255, 255, 255))
        text_rect = text_value.get_rect(center=(x + 45, y + 50))
        self.screen.blit(text_value, text_rect)

        # Draw suit label
        text_suit = self.font.render(card.suit.title(), True, (255, 255, 255))
        text_suit_rect = text_suit.get_rect(center=(x + 45, y + 90))
        self.screen.blit(text_suit, text_suit_rect)

        return rect  # return position

    def get_color_from_suit(self, suit):
        color_map = {
            "red": (220, 20, 60),
            "yellow": (255, 215, 0),
            "green": (50, 205, 50),
            "blue": (65, 105, 225),
            "wild": (100, 100, 100)
        }
        return color_map.get(suit, (200, 200, 200))

    def draw_hand(self, hand, y=440):
        self.card_rects = []
        for i, card in enumerate(hand):
            x = 110 + i * 100
            rect = self.draw_card(card, x, y)
            self.card_rects.append((rect, card))

    def draw_top_card(self, card):
        pygame.draw.rect(self.screen, (255, 255, 255), (400-3, 200-3, 96, 136), border_radius=12)
        self.draw_card(card, 400, 200)

    def update_display(self):
        pygame.display.flip()

    def wait_for_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def get_clicked_card(self, pos):
        for rect, card in self.card_rects:
            if rect.collidepoint(pos):
                return card
        return None


if __name__ == "__main__":
    view = UnoPygameView()
    fake_hand = [Card(choice(["red", "green", "yellow", "blue"]), i) for i in range(1, 6)]
    for c in fake_hand:
        c.function = None

    top_card = Card("blue", 5)

    while True:
        view.draw_background()
        view.draw_hand(fake_hand)
        view.draw_top_card(top_card)
        view.update_display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = view.get_clicked_card(pygame.mouse.get_pos())
                if clicked:
                    fake_hand.remove(clicked)
                    top_card = clicked