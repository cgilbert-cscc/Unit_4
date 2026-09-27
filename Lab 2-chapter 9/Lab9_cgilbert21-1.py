"""
Program: Match Coins
Author: Claude-henri Gilbert
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

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()

            print("...It's a Match! Player 1 wins a coin.")

        else:
            player2.win_coin()
            player1.lose_coin()

            print("...No Match! Player 2 wins a coin.")

        print()
        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

        choice = input("\nDo you want to toss the coins? (y/n): ")

    print("\n--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    # Determine final result
    if player1.get_wallet() > player2.get_wallet():
        print("Player 1 has more coins!")
    elif player2.get_wallet() > player1.get_wallet():
        print("Player 2 has more coins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()