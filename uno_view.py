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
    

    def display_message(self, message):
        """
        Display a general-purpose system message to the player.

        This method is used to show notifications, instructions, or feedback during the game.
        It helps maintain a consistent format for all non-card-related messages.

        Parameters:
            message (str): The message text to display.
        """
        print(f"\n🔔 {message}")

    def display_winner(self, winner_name):
        """
        Display the game over message and announce the winner.

        This method is called at the end of the game to let the player(s) know who won.
        It uses emoji and formatting to emphasize the final result.

        Parameters:
            winner_name (str): The name of the winning player.
        """
        print(f"\n Game Over! 🏆Winner: {winner_name}")

    def prompt_for_move(self):
        """
        Prompt the player to make a move.

        This method asks the player to either:
        - enter the number corresponding to the card they want to play, or
        - enter 'P' to draw a card from the deck.

        Returns:
            str: The player's input, either a number as a string or 'P'.
        """
        return input("\n Enter the number of the card to play, or 'P' to pick a new card: ").strip()

    def prompt_uno(self):
        """
        Prompt the player to declare 'UNO' when they have one card left.

        This method is called when the player is about to play their second-to-last card.
        It asks them to type 'UNO' before continuing.

        Returns:
            str: The player's input, expected to be 'UNO' (case-insensitive).
        """
        return input("🚨 You have 1 card left! Type 'UNO' to continue: ").strip()

if __name__ == "__main__":
    view = UnoView()
    test_hand = ["Red 5", "Blue Skip", "Wild", "Yellow 3", "Green Reverse"]
    view.display_hand(test_hand)
    view.display_top_card("Yellow 3")
    view.display_message("You have drawn a card.")
    view.display_timer(5)
    view.display_winner(view.player_name)
    move = view.prompt_for_move()
    print(f"You selected: {move}")
    uno_call = view.prompt_uno()
    print(f"You said: {uno_call}")