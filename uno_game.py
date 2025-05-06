"""
Combines elements of the uno_model.py, uno_controller.py, and uno_view.py
files together to run a fluid digital UNO game
"""

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
    # screen.fill("blue")
    view.draw_background(screen)
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("is running")
            RUNNING = False
        controller.mouse_controller_update(event)

        if controller.clicked:
            controller.interact_with_card(Model)
            controller.interact_with_uno_button(Model, view.buttons["UNO"])
            controller.interact_with_uno_out_button(Model, view.buttons["UNO OUT"])
            controller.interact_with_draw_button(Model, view.buttons["Draw"])

    if Model.deck.human_deck.is_winner:
        print("won and end")
        RUNNING = False
        continue

    if Model.deck.human_deck.is_winner:
        view.display_win_message(screen, "you")

    if Model.computer_turn:
        Model.computer_player_turn()
        Model.check_computer_uno()
        Model.check_computer_uno_out()

    view.draw_player_hand(screen)
    view.draw_top_card(screen)
    view.draw_buttons(screen)

    pygame.display.update()
    clock.tick(60)
    Model.check_for_winner()

    if Model.deck.computer_deck.is_winner:
        view.display_win_message(screen, "the computer")
        RUNNING = False

print("ends")
