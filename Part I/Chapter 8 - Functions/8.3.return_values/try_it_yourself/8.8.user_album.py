"""
8-8. User Albums:

• Start with your program from Exercise 8-7.

• Write a while loop that allows users to enter an album’s artist and title.

• Once you have that information:
    • call make_album() with the user’s input
    • and print the dictionary that’s created.

• Be sure to include a quit value in the while loop.
"""

def make_album(artist, album):
    description = {'name': artist.title(), 'album': album.title()}
    return description

while True:
    print("Tell me the album's info:\n(to quit press 'q' and *ENTER*)")
    musician = input("Tell me the name of the artist:\n\t")
    if musician == 'q':
        break
    product = input("Tell me the name of the album:\n\t")

    info = make_album(musician, product)
    print(info)