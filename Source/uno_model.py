"""
The model portion of the UNO game which saves the rules, the game operations,
the player details, the card details
"""

from random import shuffle
import time
import pygame
import sprite_sheet


class Card(pygame.sprite.Sprite):
    """
    Sets up the classifications and style of uno cards and assigns
    sub function to cards that have special effects

    Args:
        self.suit: A string type representing the color of the card
        self.value: A integer type representing the number of the card
        self.image: A sprite that holds the visual image of the card for viewing
        self.function: A string type representing the kind of effect a card has, default set to None
        self.rect: A rectangle frame representing the positioning of the image of the card
    """

    def __init__(self, suit, value, image, function=None):
        super().__init__()
        self.suit = suit
        self.value = value
        self.image = image
        self.function = function
        self.rect = self.image.get_rect()

    def _wild_effect(self, wild_card):
        """
        Has the players input in a new color for their card if they are playing a wild card

        Args:
            wild_card: An instance of the Card class where self.function is wildcardeffect,
            representing a wild card from an UNO deck
        """
        new_color = input("Choose a new color base")
        wild_card.suit = new_color

    def plus_card_effect(
        self, plus_card, current_deck, computer_instance, player_instance
    ):
        """
        Triggers the effects of a plus card in UNO by adding cards to the hand of the
        opposite player to place the plus card

        Args:
            plus_card: An instance of the Card class representing a plus UNO card
            current_deck: A list type representing the current state of the deck in the UNO game
        """
        plus_num = plus_card.value
        if computer_instance.my_turn is False:
            computer_instance.hand.append(current_deck[0:plus_num])
            del current_deck[0:plus_num]

        elif player_instance.my_turn is False:
            player_instance.hand.append(current_deck[0:plus_num])
            del current_deck[0:plus_num]

    def special_card_effect(
        self, placed_card, main_deck_instance, computer_instance, player_instance
    ):
        """
        Calls on the functions of special action cards in the UNO deck

        Args:
            placed_card: A class instant representing a card played in the UNO game

            main_deck_instance: A class instant representing the current state of the
            main deck of the UNO game

            computer_instance: A class instant representing the current version of ComputerDetails

            player_instance: A class instant representing the current version of PlayerDetails
        """
        match placed_card.function:
            case "wildcard":
                self._wild_effect(placed_card)

            case "pluscard":
                self._plus_card_effect(
                    placed_card, main_deck_instance, computer_instance, player_instance
                )

    def draw(self, screen, x, y):
        """
        Allows the model to draw the sprite used in view

        Args:
            screen: a surface representing our game screen
            x: the x-cord of the top corner of where we want our sprite
            y: the x-cord of the top corner of where we want our sprite
        """
        self.rect = pygame.Rect(x, y, self.rect.width, self.rect.height)

        screen.blit(self.image, (x, y))


class PlayerDetails:
    """
    Saves the nessaccary information that the players need for an UNO game
    """

    def __init__(self, personal_cards):
        """
        Initiliazes all the relevent details a player in an UNO game needs, including their hand,
        if they called UNO or UNO OUT, and whether or not it is their turn

        Args:
            personal_cards: A list type representing the personal hand of cards for the
            human interactive player in the UNO game
        """
        self.hand = personal_cards
        self.uno = False
        self.unoout = False
        self.my_turn = True
        self.is_winner = False

    def draw_hand(self, screen, x, y):
        """
        Allows the model to draw the sprite used in view

        Args:
            screen: a surface representing our game screen
            x: the x-cord of the top corner of where we want our sprite
            y: the x-cord of the top corner of where we want our sprite
        """
        for i in range(len(self.hand)):
            self.hand[i].draw(screen, x + (i * self.hand[i].image.get_width()), y)


class ComputerDetails:
    """
    Saves the details about the virtual 'computer' player for an UNO game
    """

    def __init__(self, personal_cards):
        """
        Initiliazes all the relevent details a player in an UNO game needs, including their hand,
        if they called UNO or UNO OUT, and whether or not it is their turn

        Args:
            personal_cards: A list type representing the personal hand of cards for the
            virtual player in the UNO game

        """
        self.hand = personal_cards
        self.uno = False
        self.unoout = False
        self.my_turn = False
        self.is_winner = False


class Deck:
    """
    Builds all the decks used a UNO game

    """

    _NUM_CARD_WIDTH = 122
    _CARD_HEIGHT = 200
    _SPECIAL_CARD_WIDTH = 116.66

    def __init__(self, original_deck):
        """
        Initilizes the main UNO deck with all the most standard UNO cards, the personal deck's
        for the human and computer players, and the deck for cards that have been played in the game

        Args:
            original_deck: A list type that represents the main eck of cards from the UNO game
            containing all the UNO cards at the start before distribution and play
        """
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

        self.main_deck = original_deck
        colors = ["red", "yellow", "green", "blue"]
        special_cards = ["red", "yellow", "green", "blue"]
        special_values = [2, 2, 2, 2]
        functions = ["pluscard", "pluscard", "pluscard", "pluscard", "wildcard"]

        # setting up regular cards
        for i in range(len(colors)):
            self.main_deck.extend(
                [
                    Card(
                        colors[i],
                        num + 1,
                        regular_card_sheet.get_image(
                            (num + (i * 10)),
                            Deck._NUM_CARD_WIDTH,
                            Deck._CARD_HEIGHT,
                            0.75,
                        ),
                    )
                    for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                ]
            )
        # setting up special cards
        for i in range(len(special_cards)):
            self.main_deck.append(
                Card(
                    special_cards[i],
                    special_values[i],
                    special_card_sheet.get_image(
                        i, Deck._SPECIAL_CARD_WIDTH, Deck._CARD_HEIGHT, 0.75
                    ),
                    functions[i],
                )
            )

        self.played_cards = []

        self.human_deck = PlayerDetails([])

        self.computer_deck = ComputerDetails([])

    def shuffle_and_distribute(self):
        """
        Shuffles the main deck of cards randomly, distributes the 7 cards to each player,
        and picks a number based card from the top of the deck to act as the starting
        card for the game

        """

        shuffle(self.main_deck)

        self.human_deck.hand.extend(self.main_deck[0:7])
        self.main_deck = self.main_deck[7:]

        self.computer_deck.hand.extend(self.main_deck[0:7])
        del self.main_deck[0:6]
        self.main_deck = self.main_deck[7:]

        position = 0
        start_card = self.main_deck[position]

        while start_card.function is not None:
            position += 1
            start_card = self.main_deck[position]

        self.played_cards.append(start_card)
        self.main_deck.pop(position)

    def refill(self):
        """
        Refills and reshuffles the main deck when it runs out during an UNO game by taking all
        but the top played cards from the played card deck, shuffling them, and making them the
        new main deck

        """

        if len(self.main_deck) == 0:
            length_of_played_deck = len(self.played_cards)
            temp_list = self.played_cards[0 : length_of_played_deck - 2]
            self.played_cards = self.played_cards[-1]

            shuffle(temp_list)
            self.main_deck = temp_list


class UNOGAMEMODEL:
    """
    Sets up the rules, game operation and winning conditions of a game of UNO
    """

    def __init__(self, input_deck):
        """
        Sets up the initial decks of the UNO game by calling on the Deck class to get a
        main class, played cards class, and the individual hands of each player

        Args:
            input_deck: An instant of a class reprsenting the decks types for the start of the game

        """

        self.deck = Deck(input_deck)

        self.deck.shuffle_and_distribute()

        self.draw_deck = self.deck.main_deck

        self.player_hand = self.deck.human_deck.hand

        self.player_turn = self.deck.human_deck.my_turn

        self.computer_hand = self.deck.computer_deck.hand

        self.computer_turn = self.deck.computer_deck.my_turn

    def _flip_next_move(self):
        """
        Change which player's turn it is to make a move.
        """
        if self.player_turn:
            self.computer_turn = True
            self.player_turn = False

        else:
            self.computer_turn = False
            self.player_turn = True

    def is_card_valid_move(self, card):
        """
        Checks if a card played is valid based on if it matches either the color or
        the number of the last played card, with the expection of wild cards.

        Args:
            card: An intant of a class representing the card picked to be played next

        Returns:
            Returns true if the card picked to be played is wild, or matches the color
            or number of the last card played. Return False otherwsie
        """
        top_of_deck = self.deck.played_cards[-1]

        if (
            (card.suit == top_of_deck.suit)
            or (card.value == top_of_deck.value)
            or (card.suit == "wild")
        ):
            return True

        return False

    def pick_a_card(self, personal_hand):
        """
        Performs the game action of picking a card in the UNO game

        Args:
            personal_hand: a list within a class instance representing the player's
            hand who is currently picking a card
        """

        if len(self.draw_deck) == 0:
            print("refills")
            self.deck.refill()

        personal_hand.append(self.draw_deck[0])
        del self.draw_deck[0]

        self._flip_next_move()

    def check_for_winner(self):
        """
        Checks if a player has won the game
        """

        if (
            len(self.player_hand) == 0
            and self.deck.human_deck.uno
            and self.deck.human_deck.unoout
        ):
            self.deck.human_deck.is_winner = True

        if (
            len(self.computer_hand) == 0
            and self.deck.computer_deck.uno
            and self.deck.computer_deck.unoout
        ):
            self.deck.computer_deck.is_winner = True

    def human_players_turn(self, picked_card):
        """
        Runs a turn for the human player in an UNO game

        Args:
            picked_card: An integer representing the position of
                the card in the players hand that they want to play in the game (if an integer)
                or t+he desire to pick a card for their turn (if a string)
        """

        self.deck.played_cards.append(self.player_hand[picked_card])
        self.player_hand.pop(picked_card)

        self._flip_next_move()

    def computer_player_turn(self):
        """
        Runs the virtual 'computer' player's turn. Performs the artificial player's (computer's)
        turn by having them choose what card they will play or if they will pick a card, and then
        performing their chosen action in the game.
        """

        for card_position, card in enumerate(self.computer_hand):

            if self.is_card_valid_move(card):

                self.deck.played_cards.append(self.computer_hand[card_position])
                self.computer_hand.pop(card_position)
                self._flip_next_move()
                break

            if card_position == (
                len(self.computer_hand) - 1
            ) and not self.is_card_valid_move(card):
                self.pick_a_card(self.computer_hand)

        if self.computer_turn is True and len(self.computer_hand) == 1:
            self.deck.computer_deck.uno = True

        if self.computer_turn is True and len(self.computer_hand) == 0:
            self.deck.computer_deck.unoout = True

        self._flip_next_move()

    def countdown(self, seconds):
        """
        Counts down during a players turn for a designated amount of time

        Args:
            seconds: An integer type representing the amount of seconds in the countdown time

        Returns:
            Returns the string "Time's up!" once the countdown has ended to signify it has ended

        """

        while seconds:
            time.sleep(1)
            seconds -= 1

        return "Time's up!"

    def call_uno(self):
        """
        Declares the human player has called out UNO
        """

        self.deck.human_deck.uno = True

    def call_uno_out(self):
        """
        Declares the human player has called out UNO OUT
        """

        self.deck.human_deck.unoout = True

    def check_player_uno(self):
        """
        Checks if the player is currently at uno specifically for situations where they call uno
        then lose it, to reset their uno status.
        """

        if len(self.player_hand) != 1:
            self.deck.human_deck.uno = False

    def check_computer_uno(self):
        """
        Checks if the computer player has 1 card left and qualifies for uno status,
        declaring uno if it is true
        """

        if len(self.computer_hand) == 1 or len(self.computer_hand) == 0:
            self.deck.computer_deck.uno = True

        else:
            self.deck.computer_deck.uno = False

    def check_computer_uno_out(self):
        """
        Checks if the computer player has no cards left and qualifies for uno out status,
        declaring uno out if it is true
        """

        if len(self.computer_hand) == 0:
            self.deck.computer_deck.unoout = True

        else:
            self.deck.computer_deck.unoout = False
