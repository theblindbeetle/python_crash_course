"""
7-10. Dream Vacation:

• Write a program that polls users about their dream vacation.

• Write a prompt similar to
    "If you could visit one place in the world,where would you go?"

• Include a block of code that prints the results of the poll.
"""

places = {}

keep_polling = True
while keep_polling:

    name = input("\nHi, what's your name: ")
    place = input(f"{name.title()}, where would you be if you could just appear there? ")

    places[name] = place

    polling = input("Are there more people to respond the poll? (yes/ no) ")
    keep_polling = False if polling == 'no' else keep_polling

print("\n--------------------------------\nPoll of ideal places:")
for person, ideal in places.items():
    print(f"{person.title()} would love to visit {ideal}.")