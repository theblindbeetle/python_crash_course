import json

username = input("What is your name?\n\t")
filename = 'username.json'
with open(filename, 'w') as f:
    # noinspection PyTypeChecker
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

# NOTE: This is a tip for those who use the Pycharm IDE.
# Add the comment <<# noinspection PyTypeChecker>> to stop seeing the
# highlighted file object (f).