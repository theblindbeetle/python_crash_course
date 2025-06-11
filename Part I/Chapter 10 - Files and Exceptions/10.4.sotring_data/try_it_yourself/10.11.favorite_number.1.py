"""
10-11. Favorite Number:

• Write a program that prompts for the user’s favorite number.

• Use json.dump() to store this number in a file.

• Write a separate program that
    • reads in this value
    • and prints the message,
        “I know your favorite number! It’s _____.”
"""

import json

filename = 'favorite_number.json'
fav_number = input("What it your favorite number?\n\t")
with open(filename, 'w') as f:
    # noinspection PyTypeChecker
    json.dump(fav_number, f)

# NOTE: This is a tip for those who use the Pycharm IDE.
# Add the comment <<# noinspection PyTypeChecker>> to stop seeing the
# highlighted file object (f).