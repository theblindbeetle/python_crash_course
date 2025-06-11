"""
10-5. Programming Poll:

• Write a while loop that asks people why they like programming.

• Each time someone enters a reason, add their reason to a file that
    stores all the responses.
"""
from datetime import datetime

filename = 'poll.txt'
while True:
    name = input("Tell me who you are:\n\t")
    if name == 'q':
        break
    poll = input("Tell me what's the best part of programming:\n\t")

    with open(filename, 'a') as file_object:
        message = f"{name.title()} thinks the best of programing is {poll}.\n"
        file_object.write(message)

# NOTE:
# 1. Type 'q' when the program asks for the name to get out of the program.