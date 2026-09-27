"""
Program: Match Coins
Author: Your Name
Purpose: Run the Coin Match game.
Starter code: None
Date: September 27, 2026
"""

from player import Player


def main():
    """Run the Coin Match game."""

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Display the title
    print("--- Coin Match Game ---")

    # Display starting coins
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    choice = input("\nDo you want to toss the coins? (y/n): ")

    while choice.lower() == "y":

        print("\nTossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")