"""
9-2. Three Restaurants:

• Start with your class from Exercise 9-1.

• Create three different instances from the class

• Call describe_restaurant() for each instance.
"""

class Restaurant:
    """Describing a restaurant type and indicates if it is open."""

    def __init__(self, restaurant_name, restaurant_type):
        """Initialize restaurant_name and restaurant_type attributes."""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe_restaurant(self):
        """Presents the restaurant."""
        print(f"This is the restaurant '{self.restaurant_name}'.")
        print(f"Try these tasty '{self.restaurant_type}' meals.")

    def open_restaurant(self):
        """Indicates that the restaurant is open."""
        print(f"The restaurant '{self.restaurant_name}' is open.")


r1 = Restaurant("The Bratwurst Plate", "German")
r2 = Restaurant("2 Big Bowls of Pho", "Vietnamese")
r3 = Restaurant("La Bandeja Paisa", "Colombian")

r1.describe_restaurant()
print()
r2.describe_restaurant()
print()
r3.describe_restaurant()