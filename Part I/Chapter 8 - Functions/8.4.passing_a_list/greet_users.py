def greet_users(names):
    """Print a simple greeting to each usr in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hanna', 'ty', 'margo']
greet_users(usernames)