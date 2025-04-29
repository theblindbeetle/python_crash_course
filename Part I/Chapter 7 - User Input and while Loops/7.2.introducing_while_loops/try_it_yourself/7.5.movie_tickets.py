"""
7-5. Movie Tickets:

• A movie theater charges different ticket prices depending on a person’s age.
    • If a person is under the age of 3, the ticket is free;
    • if they are between 3 and 12, the ticket is $10;
    • and if they are over age 12, the ticket is $15.

• Write a loop in which you ask users their age, and then tell them the cost
    of their movie ticket.
"""

price = ['free', '$10', '$15']

while True:
    age = input("Introduce your age: ")
    if int(age) < 3:
        print(f"Ticket fair is: {price[0]}")
    elif int(age) < 12:
        print(f"Ticket fair is: {price[1]}")
    else:
        print(f"Ticket fair is: {price[2]}")


