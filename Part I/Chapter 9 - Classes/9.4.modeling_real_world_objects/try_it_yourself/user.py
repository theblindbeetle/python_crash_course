class User:
    """Modeling a user."""

    def __init__(self, first_name, last_name, age, country, height, weight):
        """Initialize the user characteristics."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.height = height
        self.weight = weight

    def describe_user(self):
        """User description."""
        message = f"Customer: {self.last_name}, {self.first_name}.\n"
        message += f"Age: {self.age} y.o.\n"
        message += f"Country: {self.country}."
        message += f"Height/Weight: {self.height}/{self.weight}.\n"
        print(message)

    def greet_user(self):
        """Greeting user."""
        if self.age<20:
            print(f"Look who it is! {self.first_name}! Welcome to the land of "
                  f"fun. Enjoy your visit!")
        elif self.age<40:
            print(f"Hiya! Come here every one! {self.first_name}'s here! "
                  f"Enjoy your visit!")
        else:
            print(f"Look what the cat dragged in! {self.first_name}! "
                  f"Enjoy your visit!")