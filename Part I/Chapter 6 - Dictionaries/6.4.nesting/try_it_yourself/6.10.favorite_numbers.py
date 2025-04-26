"""
6-10. Favorite Numbers:
• Modify your program from Exercise 6-2 (page 99) so each person can have more
    than one favorite number.
• Then print each person’s name along with their favorite numbers.
"""

favorite_numbers = {
    'john': [5, 7],
    'jane': [97,23],
    'nat': [50],
    'pat': [77,66, 55],
    'matt': [110, 111, 112],
    }

for name, numbers in favorite_numbers.items():
    message = ' is' if len(numbers) < 2 else 's are'
    print(f"{name.title()}'s favorite number{message}:")
    for number in numbers:
        print(number)