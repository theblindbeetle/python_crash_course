import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompts for a new username."""
    username = input("What is your name?\n\t")
    filename = 'username.json'
    with open(filename, 'w') as f:
        # noinspection PyTypeChecker
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}")

greet_user()

# NOTE: This is a tip for those who use the Pycharm IDE.
# Add the comment <<# noinspection PyTypeChecker>> to stop seeing the
# highlighted file object (f).