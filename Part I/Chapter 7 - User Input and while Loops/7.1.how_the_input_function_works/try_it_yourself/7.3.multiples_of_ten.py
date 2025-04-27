"""
7-3. Multiples of Ten:

• Ask the user for a number,

• Then report whether the number is a multiple of 10 or not.
"""

multiple = input("Please, write a number:\n\t")

if int(multiple) % 10 == 0:
    print(f"Great! {multiple} is a multiple of 10.")
else:
    print(f"The number provided, '{multiple}', is not multiple of 10.")