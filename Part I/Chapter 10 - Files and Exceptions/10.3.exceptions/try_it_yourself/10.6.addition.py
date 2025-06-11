"""
10-6. Addition:

• One common problem when prompting for numerical input occurs when
    people provide text instead of numbers.
    When you try to convert the input to an int, you’ll get a ValueError.

• Write a program that prompts for two numbers.

• Add them together and print the result.

• Catch the ValueError if either input value is not a number,
    and print a friendly error message.

• Test your program by entering two numbers and then by entering
    some text instead of a number.
"""
DIVIDER = "_" * 25

def add_two_numbers(n1, n2):
    """Receive two numbers and print them as a String"""
    try:
        message = f"\n{DIVIDER}"
        message += f"\nThe sum is:"
        message += f"\t {n1}+{n2} = {int(n1)+int(n2)}"
        print(message)
    except ValueError:
        message = f"\n{DIVIDER}"
        message += f"\nWARNING!"
        message += f"\nEither the first value or the second value, "
        message += f"or both, are not numerical:"
        message += f"\n\tn1: {n1}\n\tn2: {n2}"
        print(message)


print(f"{DIVIDER}\nWelcome! Add two numbers to receive the sum of them.")
x = input("First number: ")
y = input("Second number: ")

add_two_numbers(n1 = x, n2= y)

# NOTE:
# 1. Notice how `DIVIDER` is uppercase, remember this represent a constant
# instead of a variable which would be lowercase.
