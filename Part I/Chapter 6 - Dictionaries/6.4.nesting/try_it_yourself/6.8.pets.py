"""
6-8. Pets:
• Make several dictionaries, where each dictionary represents a different pet.

• In each dictionary, include the kind of animal and the owner’s name.

• Store these dictionaries in a list called pets.

• Next, loop through your list and as you do, print everything you know about each pet.
"""

pet_0 = {
    'kind': 'fish',
    'owner': 'milo james thatch',
}
pet_1 = {
    'kind': 'tiger',
    'owner': 'richard parker',
}
pet_2 = {
    'kind': 'monkey',
    'owner': 'ross geller',
}
pet_3 = {
    'kind': 'whale',
    'owner': 'ismael',
}

pets = [pet_0, pet_1, pet_2, pet_3]

for pet in pets:
    print("\nHere the details of my friends:")
    for key, value in pet.items():
        message = f'The {key} of pet is a {value}.' if key == 'kind' else f'The {key}, {value} knows both are good fellows of mine.'
        print(f"\t{message}")
