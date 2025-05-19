"""
9-1. Restaurant:

• Make a class called Restaurant.

•The __init__() method for Restaurant should store two attributes:
    • restaurant_name
    • cuisine_type

• Make a method called describe_restaurant() that:
    • prints these two pieces of information:
        • restaurant_name
        • cuisine_type

• Make a method called open_restaurant() that prints a message indicating that
    the restaurant is open.

• Make an instance called restaurant from your class.

• Print the two attributes individually, and then call both methods
"""
class Restaurant:
    """Describing a restaurant type and indicates if it is open."""

    def __init__(self, restaurant_name, restaurant_type):
        """Initialize restaurant_name and restaurant_type attributes."""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe_restaurant(self):
        """Presents the restaurant."""
        print(f"This is the restaurant {self.restaurant_name}.")
        print(f"Try these tasty {self.restaurant_type} meals.")

    def open_restaurant(self):
        """Indicates that the restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is open.")

restaurant = Restaurant("Garam Masala", "Indian")

print(f"The {restaurant.restaurant_name} is my favourite restaurant.")
print(f"I like {restaurant.restaurant_type} food.")

restaurant.describe_restaurant()
restaurant.open_restaurant()
