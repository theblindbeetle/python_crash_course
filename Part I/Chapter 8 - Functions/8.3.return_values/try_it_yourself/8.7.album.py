"""
8-7. Album:

• Write a function called make_album() that builds a dictionary
    describing a music album.

• The function should take in an artist name and an album title, and it should
    return a dictionary containing these two pieces of information.

• Use the function to make three dictionaries representing different albums.

• Print each return value to show that the dictionaries are storing the album
    information correctly.

• Use None to add an optional parameter to make_album() that allows you to
    store the number of songs on an album.

• If the calling line includes a value for the number of songs, add that value
    to the album’s dictionary.

• Make at least one new function call that includes the number of songs on an
    album.
"""

def make_album(artist, album, songs=None):
    description = {'name': artist.title(), 'album': album.title()}
    if songs:
        description['songs'] = songs
    return description

production = make_album('rudimental', 'home', 8)
print(production)
production = make_album('french kiwi juice', 'Just Piano')
print(production)
production = make_album('norah jones', 'the fall')
print(production)