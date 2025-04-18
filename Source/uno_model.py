"""
Sets up the rules, game operation and winning conditions of a game of UNO
"""

from random import shuffle


class UNOGAMEMODEL:
    """
    The information used in a UNO game
    """

    def __init__(self):
        """ """

        self.deck = [
            ("wild", 0),
            ("wild", +4),
            ("yellow", 1),
            ("yellow", 2),
            ("yellow", 3),
            ("yellow", 4),
            ("yellow", 5),
            ("yellow", 6),
            ("yellow", 7),
            ("yellow", 8),
            ("yellow", 9),
            ("yellow", +2),
            ("yellow", "skip"),
            ("green", 1),
            ("green", 2),
            ("green", 3),
            ("green", 4),
            ("green", 5),
            ("green", 6),
            ("green", 7),
            ("green", 8),
            ("green", 9),
            ("green", +2),
            ("green", "skip"),
            ("blue", 1),
            ("blue", 2),
            ("blue", 3),
            ("blue", 4),
            ("blue", 5),
            ("blue", 6),
            ("blue", 7),
            ("blue", 8),
            ("blue", 9),
            ("blue", +2),
            ("blue", "skip"),
            ("red", 1),
            ("red", 2),
            ("red", 3),
            ("red", 4),
            ("red", 5),
            ("red", 6),
            ("red", 7),
            ("red", 8),
            ("red", 9),
            ("red", +2),
            ("red", "skip"),
        ]

        self.played_cards = []

        self.player_hand = []

        self.computer_hand = []

    def shuffle_and_distribute(self):
        """
        Shuffles the main deck of cards randomly, distributes the 7 cards to each player,
        and picks a number based card from the top of the deck to act as the starting
        card for the game

        """
        shuffle(self.deck)

        self.player_hand.append(self.deck[0:6])
        del self.deck[0:6]

        self.computer_hand.append(self.deck[0:6])
        del self.deck[0:6]

        position = 0
        start_card = self.deck[position]

        while start_card[1] == 0 or start_card[1] == +2 or start_card[1] == "skip":
            position += 1
            start_card = self.deck[position]

        self.played_cards.append(start_card)
        del self.deck[position]

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
        top_of_deck = self.played_cards[(len(self.played_cards) - 1)]

        if (
            (card[0] == top_of_deck[0])
            or (card[1] == top_of_deck[1])
            or (card[0] == "wild")
        ):
            return True

        return False

    def pick_a_card(self, personal_hand):
        """
        Performs the game action of picking a card in the UNO game

        Args:
            personal_hand: a list representing the player's hand who is currently picking a card
        """

        personal_hand.append(self.deck[0])
        del self.deck[0]
        print("Picked A Card")

    def computer_choice(self):
        """
        Performs the artificial player's (computer's) turn by having them choose
        what card they will play or if they will pick a card.

        Returns:
            The position number of the first eligiable card in the computer's
            hand to be played or the picked a card statement.
        """
        for card_pos in enumerate(self.computer_hand):
            if self.is_card_valid_move(self.computer_hand[card_pos]):
                return card_pos

        return self.pick_a_card(self.computer_hand)

    def check_for_winner(self, player):
        """
        Checks if a player has won the game

        Args:
            player: A list type representing the hand of a player

        Returns:
            True if the specific player has won and False otherwise
        """

        if len(player) == 0:
            return True

        return False

    def play_your_turn(self, pick_card):
        """
        _summary_

        Args:
            personal_hand (_type_): _description_
        """

    def call_uno(self):
        """
        _summary_
        """

    def call_uno_out(self):
        """
        _summary_
        """
