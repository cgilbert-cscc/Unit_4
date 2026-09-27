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
