"""
9-5. Login Attempts:

• Add an attribute called login_attempts to your User class from Exercise
    9-3 (page 162).

• Write a method called increment_login_attempts() that increments the
    value of login_attempts by 1.

• Write another method called reset_login_attempts() that resets the value
    of login_attempts to 0.

• Make an instance of the User class and call increment_login_attempts()
several times.

>• Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts().

• Print login_attempts again to make sure it was reset to 0.
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
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0."""
        self.login_attempts = 0

u1 = User('Barney', 'Stinson', 35, 'Ireland', 5.8, 132)

u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()

print(f"Login attempts by user 1: {u1.login_attempts}")
u1.reset_login_attempts()
print(f"Login attempts by user 1: {u1.login_attempts}")