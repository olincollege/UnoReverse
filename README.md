# UnoReverse

## Set Up

This repository contains the files for the Digital UNO Reverse Game project for SoftDes. In this project we programmed a digital 1v1 uno game, where our player competes against the ‘computer’ who we programmed to play the game themselves. The game follows all standard UNO rules but we left out some special cards that are unusable in a 1v1 game and ignored some popular home rules to make the game play more accessible. Players have to click buttons to call UNO or UNO OUT. To play our game please download or clone a repository and run the file uno_game.py.


### Installing Libraries:
Using your Ubuntu terminal, please pip install the following libraries in order for our game to run
pip install pygame
pip install random
Pip install time

Once you have installed these libraries, you only need to run the uno_game.py file and follow the playing instructions of the game. 

Don’t forget to call UNO! 

## Playing Instructions
**Your goal is to get to 0 cards before your opponent ‘the computer’ does.**

You will be dealt a hand of 7 cards from the main draw deck. 

After cards are drawn one card from the draw deck will be left face up to start the played card deck. 

On your turn you need to pick a card from your hand that matches either the color, number, or symbol, of the top card in the played cards deck. You will only have _30_ seconds to pick what card to play.

If you have no cards in your hand that you can play you must use your turn to pick a card from the draw deck.

When you have one card left press the UNO button as fast as you can

When you are down to 0 cards press the UNO OUT button to win!

### Action Cards
**There are 2 action cards in the game which cause a special effect.**

The Plus Cards (which will have a +2 symbol) when played cause the opposite player to have to draw 2 cards from the deck at the start of their turn. If a +2 card is played on you, you can play another +2 and your opponent will have to draw 4 cards because plus cards add up over time. 

The Wild Cards allow the person who played that card to pick what color that card will be and cards played after the wild card will have to match that picked color. 
