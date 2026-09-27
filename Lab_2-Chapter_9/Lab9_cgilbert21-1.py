"""
Program: Match Coins
Author: Claude-henri Gilbert
Purpose: Produce coin game output. 
Starter code: None
Date: September 27, 2026
"""

from player import Player


def main():
    """Run the Coin Match game."""

    """Create two players."""
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")

    """Starting Coins."""
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")