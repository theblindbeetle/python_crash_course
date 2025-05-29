"""
9-13. Dice:

• Make a class Die with one attribute called sides,
    which has a default value of 6.

• Write a method called roll_die() that prints a random number
    between 1 and the number of sides the die has.

• Make a 6-sided die and roll it.
"""

from random import randint

class Die:
    """Emulates a die."""

    def __init__(self, die_sides = 6):
        """Initialize the Die class attributes"""
        self.die_sides = die_sides

    def roll_die(self):
        """Simulates a die rolling."""
        rolled_die = randint(1, self.die_sides)
        print(f"Throwing result: {rolled_die}")

sides = 6
die = Die(sides)
for x in range(sides):
    die.roll_die()
