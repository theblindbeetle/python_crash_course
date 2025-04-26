"""
6-7. People:
Start with the program you wrote for Exercise 6-1 (page 99).
    • Make two new dictionaries representing different people
    • Store all three dictionaries in a list called people.
    • Loop through your list of people. As you loop through the list, print everything you know about each person.
"""

my_person_0 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'city': 'Mississippi',
    }
my_person_1 = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 25,
    'city': 'Queens',
    }
my_person_2 = {
    'first_name': 'Sargent',
    'last_name': 'Pepper',
    'age': 30,
    'city': 'Chicago',
    }

people = [my_person_0, my_person_1, my_person_2]

for person in people:
    print(f"\nMy dear fiend info is here:")
    for key, value in person.items():
        print(f"\t{key}: {value}")