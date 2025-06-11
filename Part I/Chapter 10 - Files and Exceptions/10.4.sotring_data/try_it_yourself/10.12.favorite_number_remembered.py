"""
10-12. Favorite Number Remembered:

• Combine the two programs from Exercise 10-11 into one file.

• If the number is already stored, report the favorite number to the user.

• If not, prompt for the user’s favorite number and store it in a file.

• Run the program twice to see that it works.
"""

import json
try:
    filename = 'favorite_number.json'
    with open(filename) as f:
        number = json.load(f)
        print(f"I know your favorite number! It’s {number}.")
except FileNotFoundError:
    filename = 'favorite_number.json'
    fav_number = input("What it your favorite number?\n\t")
    with open(filename, 'w') as f:
        # noinspection PyTypeChecker
        json.dump(fav_number, f)

# NOTE: This is a tip for those who use the Pycharm IDE.
# Add the comment <<# noinspection PyTypeChecker>> to stop seeing the
# highlighted file object (f).
