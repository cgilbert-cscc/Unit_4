"""
Program: Match Coins
Author: Claude-henri Gilbert
Purpose: Create a Player class for the Match Coins game.
Starter code: None
Date: September 27, 2026
"""

from coin import Coin

class Player:
    """A class that represents a player."""

    def __init__(self, name):
        """Initialize the player."""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """Toss the player's coin."""
        self.__coin.toss()

    def get_coin_side(self):
        """Return the side showing on the player's coin."""
        return self.__coin.get_sideup()

    def win_coin(self):
        """Add one coin to the player's wallet."""
        self.__wallet += 1

    def lose_coin(self):
        """Remove one coin from the player's wallet."""
        self.__wallet -= 1

    def get_wallet(self):
        """Return the player's current number of coins."""
        return self.__wallet