import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your username?\n\t").lower().title()
    with open(filename, 'w') as f:
        # noinspection PyTypeChecker
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")

# NOTE: This is a tip for those who use the Pycharm IDE.
# Add the comment <<# noinspection PyTypeChecker>> to stop seeing the
# highlighted file object (f).