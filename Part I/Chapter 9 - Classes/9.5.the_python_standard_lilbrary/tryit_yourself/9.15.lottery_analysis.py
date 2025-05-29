"""
9-15. Lottery Analysis:

• You can use a loop to see how hard it might be to win
    the kind of lottery you just modeled.

• Make a list or tuple called my_ticket.

• Write a loop that keeps pulling numbers until your ticket wins.

• Print a message reporting how many times the loop had to run to give you a winning ticket.
"""

from random import choices, choice, randint

class Winner:
    """Models a lottery selected number"""

    def __init__(self, rand_numbers = 10, rand_letters = 5):
        """Initialize attributes for lottery number selection."""
        self.numbers = rand_numbers
        self.letters = rand_letters

    def generate_numbers(self):
        """Generate the defined amount of numbers."""
        numbers_list = []
        while len(numbers_list) < (self.numbers + 1):
            number = randint(1, 65)
            if number not in numbers_list:
                numbers_list.append(number)
        return numbers_list

    def generate_letters(self):
        """Generate the defined amount of letters."""
        selected_letters = []
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        while len(selected_letters) < (self.letters + 1):
            letter = choice(letters)
            if letter not in selected_letters:
                selected_letters.append(letter)
        return selected_letters


winner = Winner()
lotto = winner.generate_numbers()
lotto2 = winner.generate_letters()
lotto = lotto + lotto2

winner = [choices(lotto, k=4)]

counter = 0
while True:
    finder = [choices(lotto, k=4)]
    counter += 1
    if finder == winner:
        print(f"finder is equals to winner at {counter}.\n{finder}=={winner}")
        break