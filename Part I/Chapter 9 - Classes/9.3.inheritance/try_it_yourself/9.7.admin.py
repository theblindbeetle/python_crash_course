"""
9-7. Admin:
An administrator is a special kind of user.

• Write a class called Admin
    that inherits from the User class you wrote in Exercise 9-3 (page 162)
    or Exercise 9-5 (page 167).

• Add an attribute, privileges, that stores a list of strings like:
    • "can add post"
    • "can delete post"
    • "can ban user"
    • and so on.

• Write a method called show_privileges() that lists the administrator’s
    set of privileges.

• Create an instance of Admin, and call your method.
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

class Admin(User):
    """Modeling the type of user 'Admin'."""

    def __init__(self, first_name, last_name, age, country, height, weight):
        """Initialize attributes from classes User and Admin."""
        super().__init__(first_name, last_name, age, country, height, weight)
        self.privileges = [
            "can post.",
            "can delete post",
            "can ban user",
            "can limit users",
        ]

    def show_privileges(self):
        """Display the administrator's set of privileges."""
        message = f"{self.first_name.title()} {self.last_name.title()}, "
        message += f"with {self.age} y.o., {self.height}' tall, {self.weight} "
        message += f"pounds, from {self.country.title()}, "
        message += f"has the following privileges:\n\t{self.privileges}"
        print(message)

admin = Admin('michael',
                   'jackson',
                   25,
                   'u.s.a.',
                   5.9,
                   136
                   )
admin.show_privileges()