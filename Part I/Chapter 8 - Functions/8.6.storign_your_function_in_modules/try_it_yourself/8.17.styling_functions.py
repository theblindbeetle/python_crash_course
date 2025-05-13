"""
8-17. Styling Functions:

• Choose any three programs you wrote for this chapter, and make sure they
    follow the styling guidelines described in this section.

--------------------------------
* Naming:
  * Descriptive names.
  * Use lowercase.
  * Use underscores.
* Function description:
  * A comment describing concisely what the function does.
  * The comment appear immediately after the function definition.
  * Use docstring format.
* Default values in parameters:
  * No space should be used on either side of the equal sign.
* Default values in arguments:
  * No space should be used on either side of the equal sign.
* Limit lines of code to 79 characters.
* On the next line, press tab twice to separate the list of arguments from the
    body of the function.
* If your program or module has more than one function, you can separate each by
    two blank lines.
* All import statements should be written at the beginning of a file.
    The only exception is if you use comments at the beginning of your file to
    describe the overall program.
"""
# ------------------------------------ user_profiler.py
import time

def build_profile(first, last, **user_info):
   """Build a dictionary containing everything we know about a user."""
   user_info['first_name'] = first
   user_info['last_name'] = last
   return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)


# ------------------------------------ person.py
def build_person(first_name='John', last_name='Doe'):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)


# ------------------------------------ greeter.py
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)




