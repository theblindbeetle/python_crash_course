"""
9-14. Lottery:

• Make a list or tuple containing a series of 10 numbers and five letters.

• Randomly select four numbers or letters from the list
    • and print a message saying that any ticket matching these four numbers
        or letters wins a prize.
"""
from random import choice, randint

lotto = []
while len(lotto) < 11:
    x = randint(1, 65)
    if x not in lotto:
        lotto.append(x)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
while len(lotto) < 16:
    x = choice(letters)
    if x not in lotto:
        lotto.append(x)

winner = []
for i in range(4):
    y = randint(0, len(lotto))
    winner.append(lotto.pop(y-1))

# winner = [choices(lottery_number, k=4)]
print(f"The new owner of the red velvet car have the number: {winner}")