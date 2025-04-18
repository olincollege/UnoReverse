class UnoView:
    def __init__(self):
        self.player_name = input("🎮 Welcome to UNO! What's your name? ")
        print(f"Hi, {self.player_name}! Let's get started!")
    def display_hand(self, hand):
        """
        Display the player's current hand with numbered options and corresponding emojis.

        This method prints each card in the player's hand alongside a number (starting from 1)
        to help the user easily select a card by its index. Each card is displayed with a color-based
        emoji for better visual clarity.

        Parameters:
            hand (list of str): The list of cards currently in the player's hand.
        """
        print(f"\n🃏 {self.player_name}'s hand:\n")
        for idx, card in enumerate(hand, 1):
            emoji_card = self.format_card(card)
            print(f"{idx}: {emoji_card}")

    def format_card(self, card):
        """add emoji to cards"""
        if "Red" in card:
            return f"🔴 {card}"
        elif "Yellow" in card:
            return f"🟡 {card}"
        elif "Green" in card:
            return f"🟢 {card}"
        elif "Blue" in card:
            return f"🔵 {card}"
        elif "Wild" in card:
            return f"🃏 {card}"
        else:
            return card
        
    def display_top_card(self, card):
        """
        Display the current top card on the played pile with emoji formatting.

        This method shows the card that is currently on top of the discard pile.
        The player should match this card by color or number during their turn.

        Parameters:
            card (str): The card currently on top of the played pile.

        """
        emoji_card = self.format_card(card)
        print(f"\n🔺 Top card on the pile: {emoji_card}")

    def display_timer(self, time_left):
        """
        Display the remaining time for the player's turn.

        This method prints a countdown timer showing how many seconds the player
        has left to make a move. Intended for use within a time-limited turn system.

        Parameters:
            time_left (int): The number of seconds remaining in the turn.
        """
        print(f"⏳ Time left: {time_left} seconds")
    
    