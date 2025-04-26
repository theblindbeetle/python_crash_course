"""
6-9. Favorite Places:
• Make a dictionary called favorite_places.

• Think of three names to use as keys in the dictionary, and store one to three
    favorite places for each person.

• To make this exercise a bit more interesting, ask some friends to name a few
    of their favorite places.
• Loop through the dictionary, and print each person’s name and their favorite places.
"""

favorite_places = {
    'John': ['london', 'canberra'],
    'Jane': ['hawaii'],
    'S. Pepper': ['osaka', 'kathmandu', 'curitiba'],
    }
for name, places in favorite_places.items():
    message = 's are' if len(places) > 1 else ' is'
    print(f"The {name.title()}'s favorite place{message}:")
    for place in places:
        print("\t" + place.title())
