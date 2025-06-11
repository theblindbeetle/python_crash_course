"""
10-7. Addition Calculator:

• Wrap your code from Exercise 10-6 in a while loop so the user
    can continue entering numbers even if they make a mistake and
    enter text instead of a number.
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
        message += f"\nEither of these values (or both) are not numerical"
        message += f"\n\tn1: {n1}\n\tn2: {n2}"
        print(message)


while True:
    print(f"{DIVIDER}\nWelcome! Add two numbers to receive the sum of them.")
    print("Note: to exit the program introduce 'q'.")
    x = input("First number: ")
    if x == 'q':
        break
    y = input("Second number: ")
    if y == 'q':
        break

    add_two_numbers(n1 = x, n2= y)


# Sample of output doing correct call, incorrect calls, and quit.

# Welcome! Add two numbers to receive the sum of them.
# Note: to exit the program introduce 'q'.
# First number: 10
# Second number: 11
#
# _________________________
# The sum is:	 10+11 = 21
# _________________________
# Welcome! Add two numbers to receive the sum of them.
# Note: to exit the program introduce 'q'.
# First number: 10
# Second number: eleven
#
# _________________________
# WARNING!
# Either of these values (or both) are not numerical
# 	n1: 10
# 	n2: eleven
# _________________________
# Welcome! Add two numbers to receive the sum of them.
# Note: to exit the program introduce 'q'.
# First number: q
#
# Process finished with exit code 0