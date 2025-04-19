"""
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.

•  Make a list of five or more usernames called current_users.

•  Make another list of five usernames called new_users. Make sure one or
    two of the new usernames are also in the current_users list.

•  Loop through the new_users list to see if each new username has already
    been used. If it has, print a message that the person will need to enter a
    new username. If a username has not been used, print a message saying
    that the username is available.

•  Make sure your comparison is case-insensitive. If 'John' has been used,
    'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
    current_users containing the lowercase versions of all existing users.)
"""

current_users = ['US0', 'Us1', 'admin', 'us2', 'us3']
upper_user = [x.upper() for x in current_users]
# To avoid copying the list, you may create a for within the `if` as the
# commented line below
new_users = ['us4', 'us5', 'us6', 'us0', 'US1']

for new_user in new_users:
    # if new_user.upper() in [current.upper() for current in current_users]:
    if new_user.upper() in upper_user:
        print(f"The user '{new_user.lower()}' is already taken. Please,"
              "try again with a different username.")
    else:
        print(f"The user '{new_user.lower()}' has been correctly created.")