"""
9-10. Imported Restaurant:

• Using your latest Restaurant class, store it in a module.

• Make a separate file that imports Restaurant.

• Make a
    • Restaurant instance,
    • and call one of Restaurant’s methods
        to show that the import statement is working properly.
"""
from restaurant import Restaurant

restaurant = Restaurant("Garam Masala", "Indian")

print(f"The {restaurant.restaurant_name} is my favourite restaurant.")
print(f"I like {restaurant.restaurant_type} food.")

restaurant.describe_restaurant()
restaurant.open_restaurant()
