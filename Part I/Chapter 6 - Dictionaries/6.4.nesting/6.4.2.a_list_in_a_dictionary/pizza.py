pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following ingredients:")

for topping in pizza['toppings']:
    print("\t" + topping)