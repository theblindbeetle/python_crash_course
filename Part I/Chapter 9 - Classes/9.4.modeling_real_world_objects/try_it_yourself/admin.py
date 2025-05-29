from privileges import User

class Privileges:
    """
    stores a list of strings like:
        • "can add post"
        • "can delete post"
        • "can ban user"
        • and so on.
    """
    def __init__(self):
        self.privileges = [
            "can post.",
            "can delete post",
            "can ban user",
            "can limit users",
        ]

    def show_privileges(self):
        """Display the administrator's set of privileges."""
        message = f"The admin has the following privileges:"
        message += f"\n\t{self.privileges}"
        print(message)

class Admin(User):
    """Modeling the type of user 'Admin'."""

    def __init__(self, first_name, last_name, age, country, height, weight):
        """Initialize attributes from classes User and Admin."""
        super().__init__(first_name, last_name, age, country, height, weight)
        self.privileges = Privileges()

    def admin_info(self):
        """Display the administrator's set of privileges."""
        message = f"{self.first_name.title()} {self.last_name.title()}, "
        message += f"with {self.age} y.o., {self.height}' tall, {self.weight} "
        message += f"pounds, from {self.country.title()}."
        print(message)
