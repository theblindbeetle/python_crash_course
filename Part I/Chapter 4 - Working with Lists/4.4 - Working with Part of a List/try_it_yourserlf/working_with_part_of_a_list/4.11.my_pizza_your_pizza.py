"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
•   Make a copy of the list of pizzas, and call it friend_pizzas.
•   Add a new pizza to the original list.
•   Add a different pizza to the list friend_pizzas.
•   Prove that you have two separate lists.
    ·   Print the message 'c, {and then use a for loop to print the first list}'.
    ·   Print the message: 'My friend’s favorite pizzas are:, {and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list}'.
"""
pizzas = ['pepperoni', 'mushrooms', 'four cheese']
friend_pizzas = pizzas[:]

pizzas.append('Margherita')

friend_pizzas.append('Veggie')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My firends' favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)