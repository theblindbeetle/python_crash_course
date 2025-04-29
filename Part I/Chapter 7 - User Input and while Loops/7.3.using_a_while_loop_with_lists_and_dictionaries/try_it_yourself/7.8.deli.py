"""
7-8. Deli:

• Make a list called sandwich_orders and fill it with the names of various
    sandwiches.

• Then make an empty list called finished_sandwiches.

• Loop through the list of sandwich orders
    • print a message for each order, such as I made your tuna sandwich.

• As each sandwich is made, move it to the list of finished sandwiches.

• After all the sandwiches have been made, print a message listing each sandwich
    that was made.
"""

sandwich_orders = ['tuna sandwich', 'ham sandwich', 'turkey breast sandwich']

finished_sandwiches = []

while sandwich_orders:
    made = sandwich_orders.pop()

    print(f"The {made.title()} is ready to go.")
    finished_sandwiches.append(made)

print("\n------------\nSandwiches prepared today are:\n")
for sandwich in finished_sandwiches:
    print("\t",sandwich.title())
