"""
10-3. Guest:
Write a program that prompts the user for their name.
When they respond, write their name to a file called guest.txt.
"""

filename = 'guest.txt'
username = input("Tell me your name:\n\t")

with open(filename, 'w') as file_object:
    file_object.write(username)
