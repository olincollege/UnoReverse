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
        _summary_
        """
        shuffle(self.deck)

        self.player_hand.append(self.deck[0:6])
        self.computer_hand.append(self.deck[0:6])

        position = 0
        start_card = self.deck[position]

        while start_card[1] == 0 or start_card[1] == +2 or start_card[1] == "skip":
            position += 1
            start_card = self.deck[position]

        self.played_cards.append(start_card)

    def is_card_valid_move(self, card, top_of_deck):
        """_summary_

        Args:
            card (_type_): _description_
        """
        if (
            (card[0] == top_of_deck[0])
            or (card[1] == top_of_deck[1])
            or (card[0] == "wild")
        ):
            return True

        return False

    def pick_a_card(self):
        """_summary_"""

    def player_turn(self, personal_hand):
        """_summary_

        Args:
            personal_hand (_type_): _description_
        """

    def computer_turn(self, personal_hand):
        """_summary_

        Args:
            personal_hand (_type_): _description_
        """

    def win_condition(self, player_cards, computer_cards):
        """_summary_

        Args:
            player_cards (_type_): _description_
            computer_cards (_type_): _description_
        """
