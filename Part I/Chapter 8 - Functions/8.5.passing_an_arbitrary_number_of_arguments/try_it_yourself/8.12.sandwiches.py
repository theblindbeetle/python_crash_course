"""
8-12. Sandwiches:

• Write a function that accepts a list of items a person wants on a sandwich.

• The function should have:
    • one parameter that collects as many items as the function call provides
    • it should print a summary of the sandwich that’s being ordered.

• Call the function three times, using a different number of arguments each
    time.
"""

def make_sandwich(**items):
    print("\nYour sandwich will have:")
    for item_type, ingredient in items.items():
        print(f"\t- {item_type}:\t{ingredient}")

make_sandwich(protein='chicken breast ham',
              vegetable_1='lettuce',
              vegetable_2='tomato',
              vegetable_3='pickles',
              dressing_1='mayonnaise')
make_sandwich(protein='tuna',
              vegetable_1='yellow corn',
              vegetable_2='onion',
              dressing_1='mustard')
make_sandwich(protein='beef',
              dressing_1='colander',
              cheese='american')
