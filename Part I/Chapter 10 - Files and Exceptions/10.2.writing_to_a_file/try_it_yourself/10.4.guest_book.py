"""
10-4. Guest Book:

• Write a while loop that prompts users for their name.

• When they enter their name, print a greeting to the screen and
    • add a line recording their visit in a file called guest_book.txt.

• Make sure each entry appears on a new line in the file.
"""
from datetime import datetime

filename = "guest_book.txt"
while True:

    guest = input("Tell me the person's name's  reservation:\n\t")
    when = datetime.now().strftime("%Y/%m/%dTT%H:%M:%S")
    if guest == 'q':
        break

    with open(filename, 'a') as file_object:
        file_object.write(f"{when} - {guest}\n")

# NOTE:
# 1. Type 'q' when the program asks for the name to get out of the program.
# 2. I added the module `datetime`, it is not describe in the book yet
# (it will), but I found it useful for this particular situation.