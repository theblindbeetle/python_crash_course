"""
7-4. Pizza Toppings:

• Write a loop that prompts the user to enter a series of pizza toppings until
    they enter a 'quit' value.

• As they enter each topping, print a message saying you’ll add that topping to
    their pizza.
"""
import os
import subprocess

toppings = ['mushrooms', 'extra cheese', 'serrano ham']
available_toppings = toppings[:]


greetings = "Hi and welcome to Volcano Pizza!"
print(greetings)
instructions = "-----------------------"
instructions += "\nCommands:"
instructions += "\n\t'*topping*': adds the available topping to your pizza."
instructions += "\n\t'complete': starts the preparation of your pizza."
instructions += "\n\t'refresh': start over."
instructions += "\n\t'quit': exit the process."
instructions += "\n-----------------------"
print(instructions)
ordering = "What are your toppings? Please, add one at a time."
print(ordering)

opt_message = "Here are your available options:"
no_opt_message = "No more toppings available."
no_opt_message += "Please check for section 'Commands'."


ingredient_added = "\tYou just added: "

user_toppings = ''
while user_toppings != 'quit' or user_toppings != 'complete':
    options = ""
    for topping in available_toppings:
        options += f"\t|\t{topping}"

    message = f"{opt_message}\n\t{options}\n\t" if len(available_toppings)>0 else f"{no_opt_message}\n\t"
    user_toppings = input(message)

    if user_toppings  == 'quit':
        break

    elif user_toppings == 'refresh':
        clear = lambda: os.system('cls')
        clear()
        available_toppings = toppings[:]
        print(greetings)
        print(instructions)
        print(ordering)
        options = ""

    elif user_toppings == 'complete':
        if available_toppings == toppings:
            print("Your pure pizza is being prepared!")
        else:
            print("Your pizza is being prepared with:")
            for ingredient in toppings:
                if ingredient not in available_toppings:
                    print(f"\t{ingredient}")
        break

    elif user_toppings.lower() in available_toppings:
        print(ingredient_added, user_toppings)
        available_toppings.remove(user_toppings.lower())

    else:
        print(f"The ingredient '{user_toppings.upper()}', is not available.")