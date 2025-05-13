def make_pizza(size, *toppings):
    """Print the size of the pizza and the required toppings"""
    print(f"Let's make a:\n\t{size}' pizza\nWith the toppings:")
    for topping in toppings:
        print(f"\t- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')