"""
Controller for our Final Project's version of UNO
"""

from abc import ABC, abstractmethod


class UNOController(ABC):
    """
    Your docstring goes here.
    """

    # makes a version of UNOModel for us
    def __init__(self, model):
        self._model = model

    @property
    def deck(self):
        """
            Your docstring goes here. Fill in once more info written.
        """
        return self._model


class TextController(UNOController):
    """
    Your docstring goes here. Fill in once more info written.
    Acts as an instance of UNOcontroller
    """
    #kinda of runs through all the tests we need for UNOController
    def is_valid(self, card):
        if card[0] == top_of_deck[0]:
            return True
        if card[1] == top_of_deck[1]:
            return True
        if card[0] == "wild":
            return True
        return False


    def Play(self):
        """
        Your docstring goes here. Fill in once more info written.
        """
        user_input = input(f"Type in the card you want to play or 'D' to Draw a card:")

        #this will eventually raise error messages for wrong imputs.  
        while self.is_valid(user_input) == False:
            try:
                pass
            except:
                pass
