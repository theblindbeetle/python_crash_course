"""
7-9. No Pastrami:
Using the list sandwich_orders from Exercise 7-8:

•Make sure the sandwich 'pastrami' appears in the list at least three times.

• Add code near the beginning of your program to print a message saying
    • "the deli has run out of pastrami"
    • and then use a while loop to remove all occurrences of 'pastrami' from
        sandwich_orders.

• Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'ham', 'pastrami', 'turkey breast']
print("The deli sandwich house has run out of pastrami.")
finished_sandwiches = []

while 'pastrami' in sandwich_orders:

    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)


print("Here are the finished sandwiches:")
for sandwich in finished_sandwiches:
    print("\t", sandwich.title())