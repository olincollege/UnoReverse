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


# everything should be in the "running" loop
while RUNNING:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        controller.mouse_controller_update(event)

        if controller.clicked:
            controller.interact_with_card(Model)
            controller.interact_with_uno_button(Model, view.buttons["UNO"])
            controller.interact_with_uno_out_button(Model, view.buttons["UNO OUT"])
            controller.interact_with_draw_button(Model, view.buttons["Draw"])

    # runs frame by frame, so you don't see cards in the background
    screen.fill("blue")

    if Model.deck.human_deck.is_winner is True:
        RUNNING = False
        continue

    Model.computer_player_turn()
    pygame.display.update()
    Model.check_computer_uno()
    Model.check_computer_uno_out()
    clock.tick(60)
    Model.check_for_winner()

    if Model.deck.computer_deck.is_winner is True:
        RUNNING = False

if Model.deck.computer_deck.is_winner is True:
    view.display_win_message(screen, "the computer")

elif Model.deck.human_deck.is_winner is True:
    view.display_win_message(screen, "you")
