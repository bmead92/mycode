#!/usr/bin/env python3
"""Creating a simple dice program with classes."""

# standard lib
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    # a function defined within a class is a method
    def roll(self):
        self.dice = [] # clears current data
        for i in range(3):
            self.dice.append(randint(1,6))

    def get_dice(self):
        return self.dice
def main():
    """called at runtime"""

    # create players
    player1 = Player()
    player2 = Player()
        
    # have players roll
    player1.roll()
    player2.roll()

    # display results
    p1score = player1.get_dice()
    p2score = player2.get_dice()

    print(f"Player 1 rolled {p1score}")
    print(f"Player 2 rolled {p2score}")

    # determine winner
    if sum(p1score) == sum(p2score):
        print("Draw")
    elif sum(p1score) > sum(p2score):
        print("Player 1 wins!")
    else:
        print("Player 2 wins")
if __name__ == "__main__":
    main()
