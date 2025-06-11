"""
10-13. Verify User:

• The final listing for remember_me.py assumes either:
    • that the user has already entered their username
    • or that the program is running for the first time.

• We should modify it in case the current user is not the person who
    last used the program.

• Before printing a welcome back message in greet_user(),
    ask the user if this is the correct username:
    • If it’s not, call get_new_username() to get the correct username.
"""

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
        message = f"Are you {username}?\n press any key and enter to confirm, "
        message += "or just enter to deny: "
        current_user = input(message)
        if current_user:
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}")

greet_user()

# NOTE: This is a tip for those who use the Pycharm IDE.
# Add the comment <<# noinspection PyTypeChecker>> to stop seeing the
# highlighted file object (f).