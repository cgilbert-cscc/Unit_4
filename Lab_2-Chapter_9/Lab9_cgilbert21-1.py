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

    choice = input("\nDo you want to toss the coins? (y/n): ")

    while choice.lower() == "y":

        print("\nTossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        """Display the results"""
        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        """Determine the winner."""
        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()

            print("It's a Match! Player 1 wins a coin.")

        else:
            player2.win_coin()
            player1.lose_coin()

            print("No Match! Player 2 wins a coin.")

        print()
        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

        choice = input("\nDo you want to toss the coins? (y/n): ")
