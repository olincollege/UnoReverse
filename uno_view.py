import pygame
from Source.uno_model import PlayerDetails, ComputerDetails, Card, Deck, UNOGAMEMODEL

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
        self.font=pygame.font.Font(None, 36)
    def get_top_card(self, top_card):
        """Get the top card"""
        top_card=Deck.played_cards[-1]
        return top_card
    def get_player_hand(self, player_hand):
        """Get details of the player's cards on hand"""
        player_hand=Deck.human_deck()
        return player_hand
    def get_computer_hand(self, computer_hand_count):
        """Get the number of cards that the computer left on hand"""
        computer_hand_count=len(Deck.computer_deck())
        return computer_hand_count
    def draw_background(self):
        """Fill the background with the determined color"""
        self.screen.fill(self.background_color)
    #def draw_timer(self):
       # """Draw the timer"""
        #timer=pygame.Rect(self.screen_width-150, 10, 130, 40)
        #pygame.draw.rect(timer)
        #timer_time=self.font.render("Time: 0", True, self.text)
        #time_position=timer_time.get_rect(center=timer.center)
        #self.screen.blit(timer_time, time_position)
    def draw_buttons(self):
        """Draw needed buttons--Draw, UNO, and Pass at the right bottom of the screen"""
        self.buttons={}
        button_width=100
        button_height=40
        position_y = self.screen_height-80
        horizontal_center=self.screen_width//2
        #Draw Card
        draw_button_position_x=horizontal_center-170
        draw_button=pygame.Rect(draw_button_position_x,position_y,button_width,button_height)
        self.buttons["Draw"]=draw_button
        pygame.draw.rect(self.screen,self.gray,draw_button)
        text_draw=self.font.render("Draw", True, self.text)
        text_draw_rectangle=text_draw.get_rect(center=draw_button.center)
        self.screen.blit(text_draw,text_draw_rectangle)
        #UNO
        UNO_button_position_x=horizontal_center-50
        UNO_button=pygame.Rect(UNO_button_position_x,position_y,button_width,button_height)
        self.buttons["UNO"]=UNO_button
        pygame.draw.rect(self.screen,self.gray,UNO_button)
        text_UNO=self.font.render("UNO", True, self.text)
        text_UNO_rectangle=text_draw.get_rect(center=UNO_button.center)
        self.screen.blit(text_UNO,text_UNO_rectangle)
        #Pass
        Pass_button_position_x=horizontal_center+70
        Pass_button=pygame.Rect(Pass_button_position_x,position_y,button_width,button_height)
        self.buttons["Pass"]=Pass_button
        pygame.draw.rect(self.screen,self.gray,Pass_button)
        text_Pass=self.font.render("Pass", True, self.text)
        text_Pass_rectangle=text_draw.get_rect(center=Pass_button.center)
        self.screen.blit(text_Pass,text_Pass_rectangle)