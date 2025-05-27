"""
9-6. Ice Cream Stand:
An ice cream stand is a specific kind of restaurant.

• Write a class called IceCreamStand
    • that inherits from the Restaurant class you wrote in
        Exercise 9-1 (page 162) or Exercise 9-4 (page 167).
        Either version of the class will work;
        just pick the one you like better.

• Add an attribute called flavors that stores a list of ice cream flavors.

• Write a method that displays these flavors.

• Create an instance of IceCreamStand, and call this method.
"""

class Restaurant:
    """Describing a restaurant type and indicates if it is open."""

    def __init__(self, restaurant_name, restaurant_type):
        """
        Initialize restaurant_name and restaurant_type attributes.

        :param restaurant_name: (str) - the name of the restaurant.
        :param restaurant_type: (str) - the kind of restaurant (mexican, seafood,
                mediterranean, etc.)
        """
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe_restaurant(self):
        """Presents the restaurant."""
        print(f"This is the restaurant {self.restaurant_name}.")
        print(f"Try these tasty {self.restaurant_type} meals.")

    def open_restaurant(self):
        """Indicates that the restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is open.")

class IceCream(Restaurant):
    """Describing an Ice Cream Stand."""

    def __init__(self, restaurant_name, restaurant_type):
        """
        Initialize the attributes from Restaurant and from IceCream classes.
        """
        super().__init__(restaurant_name, restaurant_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberries', 'passion fruit']

    def get_flavors(self):
        """Display the flavors offered by Ice Cream restaurant."""
        message = f"The {self.restaurant_type}, "
        message += f"'{self.restaurant_name.title()}'"
        message += f" offers you the flavors:\n\t{self.flavors}"
        print(message)

ice_cream = IceCream('chilling summer',
                     'ice cream stand')
ice_cream.get_flavors()
