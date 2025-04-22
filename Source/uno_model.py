"""_summary_

Returns:
        _type_: _description_
"""

from random import shuffle
import time


class Card:
    """_summary_"""

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.function = None

    def _wild_effect(self, wild_card):
        """
        _summary_

        Args:
            wild_card (_type_): _description_
        """
        new_color = input(wild_card.function)
        wild_card.suit = new_color

    def _plus_card_effect(self, plus_cards):
        """_summary_

        Args:
            plus_cards (_type_): _description_
        """

    def _skip_effect(self, skip_cards):
        """_summary_

        Args:
            skip_cards (_type_): _description_
        """

    def special_card_effect(self, placed_card):
        """
        Calls of the functions of specially cards in the UNO deck

        Args:
            placed_card: A class instant representing a card played in the UNO game
        """
        match placed_card.function:
            case "wildcard":
                self._wild_effect(placed_card)

            case "pluscard":
                self._plus_card_effect(placed_card)

            case "skipeffect":
                self._skip_effect(placed_card)

    def __repr__(self):
        return f"You have a {self.suit} {self.value} with a function of {self.function}"


class PlayerDetails:
    """
    Saves the nessacry informtaion that players need for an UNO game
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
    """_summary_

    Returns:
        _type_: _description_
    """

    def __init__(self, personal_cards):
        """ """
        self.hand = personal_cards
        self.uno = False
        self.unoout = False
        self.my_turn = False

        self.deck = Deck([])

        self.rules = UNOGAMEMODEL()

    def computer_choice(self):
        """
        Performs the artificial player's (computer's) turn by having them choose
        what card they will play or if they will pick a card.

        Returns:
            The position number of the first eligiable card in the computer's
            hand to be played or the picked a card statement.
        """
        for card_pos in enumerate(self.hand):
            if self.rules.is_card_valid_move(self.hand[card_pos]):

                self.deck.played_cards.append(self.hand[card_pos])
                self.hand.pop(card_pos)
                break

            if card_pos == (len(self.hand) - 1) and not self.rules.is_card_valid_move(
                self.hand[card_pos]
            ):
                self.rules.pick_a_card(self.hand)

    def __repr__(self):
        pass


class Deck:
    """_summary_

    Returns:
        _type_: _description_
    """

    def __init__(self, original_deck):
        """_summary_

        Returns:
            _type_: _description_
        """
        self.main_deck = original_deck

        for color in ["red", "yellow", "green", "blue"]:
            self.main_deck.append(Card(color, i) for i in range(1, 10))

        wild1 = Card("wild", +4)
        wild1.function = "wildcard"
        self.main_deck.append(wild1)

        redplus2 = Card("red", +2)
        redplus2.function = "pluscard"
        self.main_deck.append(redplus2)

        yellowplus2 = Card("yellow", +2)
        yellowplus2.function = "pluscard"
        self.main_deck.append(yellowplus2)

        greenplus2 = Card("green", +2)
        greenplus2.function = "pluscard"
        self.main_deck.append(greenplus2)

        blueplus2 = Card("blue", +2)
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


class UNOGAMEMODEL:
    """
    Sets up the rules, game operation and winning conditions of a game of UNO
    """

    def __init__(self):
        """ """

        self.deck = Deck([])

        self.player = PlayerDetails([])

        self.computer = ComputerDetails([])

    def _flip_next_move(self):
        """
        Change the next player to move.
        """
        if self.player.my_turn is True:
            self.computer.my_turn = True
            self.player.my_turn = False

        else:
            self.computer.my_turn = False
            self.player.my_turn = True

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

    def players_turn(self, picked_card):
        """
        _summary_

        Args:
            picked_card: An integer or string type representing the position of
                the card in the players hand that they want to play in the game (if an integer)
                or the desire to pick a card for their turn (if a string)
            personal_hand:a list representing the player's hand who turn it is
        """
        if picked_card == "Pick":
            self.pick_a_card(self.player.hand)

        else:
            self.deck.played_cards.append(self.player.hand[picked_card])
            self.player.hand.pop(picked_card)

        self._flip_next_move()

    def countdown(self, seconds):
        """_summary_

        Args:
            seconds (_type_): _description_

        Returns:
            _type_: _description_
        """
        while seconds:
            time.sleep(1)
            seconds -= 1

        return "Time's up!"

    def call_uno(self):
        """
        _summary_
        """
        while self.countdown(60) != "Time's up!":
            call_uno = input("What do you say?")
            if call_uno == ("Uno"):
                return True
        return False

    def call_uno_out(self):
        """
        _summary_
        """
        while self.countdown(60) != "Time's up!":
            call_out = input("What do you say?")
            if call_out == ("Uno Out"):
                return True
        return False
