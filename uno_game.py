import pygame
from Source.uno_model import UNOGAMEMODEL
from uno_controller import MouseController
from uno_view import View


# setup for the event
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()  # internal clock. May ve visualized in View
Model = UNOGAMEMODEL([])
controller = MouseController(Model)
view = View(Model)
RUNNING = True  # is the game running?
DT = 0  # start time
pygame.QUIT = RUNNING is False


# everything should be in the "running" loop
while RUNNING:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        controller.handle_mouse_event(event)

    # runs frame by frame, so you don't see cards in the background
    screen.fill("blue")

    # runs a single round of game, should be the layout of event
    Model.countdown(30)
    Model.human_players_turn()  # need to know what card is clicked as input
    Model.check_for_winner()

    if Model.deck.human_deck.is_winner is True:
        RUNNING = False
        continue

    Model.computer_player_turn()
    view.screen  # update view
    Model.check_computer_uno()
    Model.check_computer_uno_out()
    Model.check_for_winner()

    if Model.deck.computer_deck.is_winner is True:
        RUNNING = False

if Model.deck.computer_deck.is_winner is True:
    view.display_win_message("the computer")

elif Model.deck.human_deck.is_winner is True:
    view.display_win_message("you")
