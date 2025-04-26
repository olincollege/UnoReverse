"""_summary_

Returns:
        _type_: _description_
"""

from random import shuffle
import time


class PlayerDetails:
    """
    Saves the neaaaccary information that the players need for an UNO game
    """

    def __init__(self, personal_cards):
        """ """
        self.hand = personal_cards
        self.uno = False
        self.unoout = False
        self.my_turn = True

    def __repr__(self):
        pass


class ComputerDetails:
    """
    Saves the details about the virtual 'computer' player for an UNO game
    """

    def __init__(self, personal_cards):
        """ """
        self.hand = personal_cards
        self.uno = False
        self.unoout = False
        self.my_turn = False

        self.rules = UNOGAMEMODEL()

    def computer_choice(self, maindeck, hand):
        """
        Performs the artificial player's (computer's) turn by having them choose
        what card they will play or if they will pick a card.

        Returns:
            The position number of the first eligiable card in the computer's
            hand to be played or the picked a card statement.
        """
        for card_pos in enumerate(hand):
            if self.rules.is_card_valid_move(hand[card_pos]):

                maindeck.played_cards.append(hand[card_pos])
                hand.pop(card_pos)
                break

            if card_pos == (len(hand) - 1) and not self.rules.is_card_valid_move(
                hand[card_pos]
            ):
                self.rules.pick_a_card(hand)

    def __repr__(self):
        pass


class Card:
    """
    Sets up the classifications and style of uno cards and assigns
    sub function to cards that have special effects
    """

    def __init__(self, suit, value, computer_class, player_class):
        self.suit = suit
        self.value = value
        self.function = None
        self.computer = computer_class
        self.human = player_class

    def _wild_effect(self, wild_card):
        """
        Has the players input in a new color for their card if they are playing a wild card

        Args:
            wild_card: An instance of the Card class where self.function is wildcardeffect,
                    representing a wild card from an UNO deck
        """
        new_color = input("Choose a new color base")
        wild_card.suit = new_color

    def _plus_card_effect(self, plus_card, current_deck):
        """
        Triggers the effects of a plus card in UNO by adding cards to the hand of the
        opposite player to place the plus card

        Args:
            plus_card: An instance of the Card class representing a plus UNO card
            current_deck: A list type representing the current state of the deck in the UNO game
        """
        plus_num = plus_card.value
        if self.computer.my_turn is False:
            self.computer.deck.append(current_deck[0:plus_num])
            del current_deck[0:plus_num]

        elif self.human.my_turn is False:
            self.human.deck.append(current_deck[0:plus_num])
            del current_deck[0:plus_num]

    def _skip_effect(self):
        """
        Skips the next player's turn, giving the current player another turn
        """

        if self.computer.my_turn is True:
            self.computer.computer_choice()

    def special_card_effect(self, placed_card, main_deck_instance):
        """
        Calls on the functions of special action cards in the UNO deck

        Args:
            placed_card: A class instant representing a card played in the UNO game
        """
        match placed_card.function:
            case "wildcard":
                self._wild_effect(placed_card)

            case "pluscard":
                self._plus_card_effect(placed_card, main_deck_instance)

            case "skipeffect":
                self._skip_effect()

    def __repr__(self):
        pass


class Deck:
    """
    _summary_

    """

    def __init__(self, original_deck):
        """
        Initilizes the main UNO deck with all the most standard UNO cards, the personal deck's
        for the human and computer players, and the deck for cards that have been played in the game

        """
        self.main_deck = original_deck

        for color in ["red", "yellow", "green", "blue"]:
            self.main_deck.append(
                Card(color, i, ComputerDetails, PlayerDetails) for i in range(1, 10)
            )

        wild1 = Card("wild", 0, ComputerDetails, PlayerDetails)
        wild1.function = "wildcard"
        self.main_deck.append(wild1)

        redplus2 = Card("red", 2, ComputerDetails, PlayerDetails)
        redplus2.function = "pluscard"
        self.main_deck.append(redplus2)

        yellowplus2 = Card("yellow", 2, ComputerDetails, PlayerDetails)
        yellowplus2.function = "pluscard"
        self.main_deck.append(yellowplus2)

        greenplus2 = Card("green", 2, ComputerDetails, PlayerDetails)
        greenplus2.function = "pluscard"
        self.main_deck.append(greenplus2)

        blueplus2 = Card("blue", 2, ComputerDetails, PlayerDetails)
        blueplus2.function = "pluscard"
        self.main_deck.append(blueplus2)

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

        self.human_deck.hand.append(self.main_deck[0:6])
        del self.main_deck[0:6]

        self.computer_deck.hand.append(self.main_deck[0:6])
        del self.main_deck[0:6]

        position = 0
        start_card = self.main_deck[position]

        while start_card.value in (0, +2) or start_card.suit == "wild":
            position += 1
            start_card = self.main_deck[position]

        self.played_cards.append(start_card)
        self.main_deck.pop(position)

    def __repr__(self):
        pass


class UNOGAMEMODEL:
    """
    Sets up the rules, game operation and winning conditions of a game of UNO
    """

    def __init__(self):
        """ """

        self.deck = Deck([])

        self.deck.shuffle_and_distribute()

        self.player_hand = self.deck.human_deck.hand

        self.player_turn = self.deck.human_deck.my_turn

        self.player_uno = self.deck.human_deck.uno

        self.player_unoout = self.deck.human_deck.unoout

        self.computer_hand = self.deck.computer_deck.hand

        self.computer_turn = self.deck.computer_deck.my_turn

        self.computer_uno = self.deck.computer_deck.uno

        self.computer_unoout = self.deck.computer_deck.unoout

    def _flip_next_move(self):
        """
        Change which player's turn it is to make a move.
        """
        if self.player_turn is True:
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
            card: A tuple type representing the card picked to be played next
            top_of_deck: A tuple type representing the last card played

        Returns:
            Returns true if the card picked to be played is wild, or matches the color
            or number of the last card played. Return False otherwsie
        """
        top_of_deck = self.deck.played_cards[(len(self.deck.played_cards) - 1)]

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
            personal_hand: a list representing the player's hand who is currently picking a card
        """

        personal_hand.append(self.deck.main_deck[0])
        del self.deck.main_deck[0]
        print("Picked A Card")

    def check_for_winner(self, player):
        """
        Checks if a player has won the game

        Args:
            player: A list type representing the hand of a player

        Returns:
            True if the specific player has won and False otherwise
        """

        if len(player) == 0 and self.call_uno_out:
            return True

        return False

    def human_players_turn(self, picked_card):
        """
        Runs a turn for the human player in an UNO game

        Args:
            picked_card: An integer or string type representing the position of
                the card in the players hand that they want to play in the game (if an integer)
                or the desire to pick a card for their turn (if a string)
            personal_hand:a list representing the player's hand who turn it is

        """

        if picked_card == "Pick":
            self.pick_a_card(self.player_hand)

        else:
            self.deck.played_cards.append(self.player_hand[picked_card])
            self.player_hand.pop(picked_card)

        self._flip_next_move()

    def computer_player_turn(self):
        """
        Runs the virtual 'computer' player's turn

        """

        self.deck.computer_deck.computer_choice(self.deck.main_deck, self.computer_hand)

        self._flip_next_move()

    def refill_deck(self):
        """
        Refills and reshuffles the main deck when it runs out during an UNO game by taking all
        but the top played cards from the played card deck, shuffling them, and making them the
        new main deck

        """

        if len(self.deck.main_deck) == 0:
            length_of_played_deck = len(self.deck.played_cards)
            temp_list = self.deck.played_cards[0 : length_of_played_deck - 1]
            self.deck.played_cards = self.deck.played_cards[-1]

            shuffle(temp_list)
            self.deck.main_deck = temp_list

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
        Checks that once the human player has only 1 card left, they type in Uno within a minute to
        claim UNO before their opponet does, and establishes that once the virtual player has only
        1 card left they claim UNO as well

        """
        if self.computer_turn is True and len(self.computer_hand) == 1:
            self.computer_uno = True

        else:
            self.computer_uno = False

        if self.player_turn is True and len(self.player_hand) == 1:
            while self.countdown(60) != "Time's up!":
                call_uno = input("What do you say?")
                if call_uno == ("Uno"):
                    self.player_uno = True
            self.player_uno = False

    def call_uno_out(self):
        """
        Checks that once the human player has no cards left, they type in Uno Out within a minute to
        claim UNO OUT before their opponet does, and establishes that once the virtual player has no
        cards left they claim UNO OUT as well

        """

        if self.computer_turn is True and len(self.computer_hand) == 0:
            self.computer_unoout = True

        else:
            self.computer_unoout = False

        if self.player_turn is True and len(self.player_hand) == 0:
            while self.countdown(60) != "Time's up!":
                call_uno = input("What do you say?")
                if call_uno == ("Uno Out"):
                    self.player_unoout = True
            self.player_unoout = False
