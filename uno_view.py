import pygame

class View:
    def __init__(self, model, controller):
        pygame.init()
        self.model=model
        self.controller=controller
        self.screen_width=1200
        self.screen_height=900
        self.background_color=(30, 120, 30)
        self.screen=pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("UNO Game")
        self.red=(200, 50,  50)
        self.green=(50,  200, 50)
        self.blue=(50,  50,  200)
        self.yellow=(240, 240, 50)
        self.gray=(100, 100, 100)
        self.text=(255, 255, 255)
    def draw_background(self):
        """Fill the background with the determined color"""
        self.screen.fill(self.background_color)
    def draw_timer(self):
        """Draw the timer"""
        timer= pygame.Rect(self.screen_width-150, 10, 130, 40)
        pygame.draw.rect(timer)
        font = pygame.font.Font(None, 36)
        timer_time=font.render("Time: 0", True, self.text)
        time_position = timer_time.get_rect(center=timer.center)
        self.screen.blit(timer_time, time_position)
    def draw_buttons(self):
        """Draw needed buttons--UNO, Draw, Pass at the right bottom of the screen"""
        self.buttons={}
        pass
    def draw_top_card(self, top_card):
        """Draw the top card"""
        pass
    def draw_deck(self):
        """Draw the deck with the recent played card in the center"""
        pass
    def draw_player_hand(self, player_hand):
        """Display to details of the player's cards on hand"""
        pass
    def draw_computer_hand(self, computer_hand_count):
        """Display the number of cards that the computer left on hand"""

