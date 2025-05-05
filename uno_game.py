import pygame
from Source.uno_model import UNOGAMEMODEL
from uno_controller import MouseController
from uno_view import View


# setup for the event
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()  # internal clock. May ve visualized in View
model = UNOGAMEMODEL
controller = MouseController(model)
view = View(model)
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

    # runs a single round of game
    # model.countdown(30)
    # model.human_players_turn()
    # model.computer_player_turn()
    # view # update view
    # model.check_computer_uno
    # model.check_computer_unoout
    # model.check_for_winner

    if (
        model.deck.computer_deck.is_winner is True
        or model.deck.player_deck.is_winner is True
    ):
        RUNNING = False
