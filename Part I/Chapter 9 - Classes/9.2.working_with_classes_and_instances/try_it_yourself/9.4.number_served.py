"""
9-4. Number Served:

• Start with your program from Exercise 9-1 (page 162).

• Add an attribute called number_served with a default value of 0.

• Create an instance called `restaurant` from this class.

• Print the number of customers the restaurant has served,
    then change this value and print it again.

• Add a method called set_number_served() that lets you set the number
    of customers that have been served.

• Call this method with a new number and print the value again.

>• Add a method called increment_number_served() that lets you increment
    the number of customers who’ve been served.

• Call this method with any number you like that could represent how
    many customers were served in, say, a day of business.

"""

class Restaurant:
    """Describing a restaurant type and indicates if it is open."""

    def __init__(self, restaurant_name, restaurant_type):
        """Initialize restaurant_name and restaurant_type attributes."""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = 0

    def describe_restaurant(self):
        """Presents the restaurant."""
        print(f"This is the restaurant {self.restaurant_name}.")
        print(f"Try these tasty {self.restaurant_type} meals.")

    def open_restaurant(self):
        """Indicates that the restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is open.")

    def set_number_served(self, served):
        """Update the number of customers served to the receipt value."""
        self.number_served = served

    def increment_number_served(self, add_served):
        """Increment the value of the customers served"""
        self.number_served += add_served

restaurant = Restaurant("Garam Masala", "Indian")

print(f"Customers served: {restaurant.number_served}\n")
restaurant.number_served = 400
print(f"Customers served: {restaurant.number_served}\n")
restaurant.set_number_served(150)
print(f"Customers served: {restaurant.number_served}\n")
restaurant.increment_number_served(350)
print(f"Customers served: {restaurant.number_served}\n")