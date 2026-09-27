"""
Program: Match Coins
Author: Claude-henri Gilbert
Purpose: Create a Coin class for the Coin Match game.
Starter code: None
Date: September 27, 2026
"""

import random

class Coin:
    """A class that represents a single coin."""

    def __init__(self):
        """Initialize the coin."""
        self.__sideup = "Heads"

    def toss(self):
        """Randomly toss the coin."""
        number = random.randint(0, 1)

        if number == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Return the current side of the coin."""
        return self.__sideup