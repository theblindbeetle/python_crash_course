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

