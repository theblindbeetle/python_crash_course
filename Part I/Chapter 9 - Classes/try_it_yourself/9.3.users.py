"""
9-3. Users:

• Make a class called User.

• Create two attributes:
    • first_name
    • last_name

• Create several other attributes that are typically stored in a user profile.

• Make a method called describe_user() that prints a summary of the user’s
    information.

• Make another method called greet_user() that prints a personalized greeting to
    the user.

• Create several instances representing different users, and call both methods
    for each user.
"""

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


u1 = User('Barney', 'Stinson', 35, 'Ireland', 5.8, 132)
u2 = User('Mulan', 'Fah', 17, 'China', 4.9,110)
u3 = User('Dolph', 'Lundgren', 68, 'Sweden', '6.5', 225)

u1.greet_user()
u1.describe_user()

u2.greet_user()
u2.describe_user()

u3.greet_user()
u3.describe_user()
