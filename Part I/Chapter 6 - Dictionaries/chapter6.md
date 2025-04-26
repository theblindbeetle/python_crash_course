
# Chapter 6: Dictionaries
### In this chapter you’ll learn how to use Python’s dictionaries, which allow you to connect pieces of related information.Additionally, you’ll learn to nest dictionaries inside lists, lists inside dictionaries, and even dictionaries inside other dictionaries.

---
## 6.1 A Simple Dictionary
Consider a game featuring aliens that can have different colors and point 
values, This simple dictionary stores information about a particular alien:
```python
# REFER: ../6.1.../alien.py
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
```
The dictionary `alien_0` stores the alien's color and point value. The last two
lines access and display the information, as shown here:
```commandline
green
5
```

---
## 6.2 Working with Dictionaries
A dictionary in python is a collection of <i>key-value pairs</i>. Each key is
connected to a value, and you can use that key to access the associated value.
A value can be a number, a string, a list, or even another dictionary.
In deed, you can use any object that Python can create as value in a dictionary.
In Python a dictionary is wrapped in braces, {}, with a series of key-values
pairs inside the braces, as shown in the earlier example:
```python
alien_0 = {'color': 'green', 'points': 5}
```
A <i>key-value pair</i> is a set of values associated with each other. When you
provide a key, Python returns the value associated with that key. The key
connects with the value by using a colon (`:`), and individual key-value pairs
are separated by commas.
The simples dictionary has only one key-value pair:
```python
alien_0 = {'color': 'green'}
```
This is a single piece of information, about `alien_0`, where namely the alien's
color. The string 'color' is a key in this dictionary, and its associated value
is 'green'.

### 6.2.1 Accessing Values in a Dictionary
To get the value associated with a key, give the name of the dictionary and
then place the key inside a set of square brackets, as shown here:
```python
# REFER: ../6.2.../6.2.1.accessing_values_in_a_dictionary.../alien.py
aline_0 = {'color': 'green'}
print(aline_0['color'])
```
This returns the value associated with the key `color` from the dictionary 
`alien_0`:
```commandline
green
```
You can have unlimited number of key-values pairs in a dictionary.
For example, here's the one we used previously:
```python
aline_0 = {'color': 'green', 'points': 5}
```
You can check on either of the elements in the dictionary, if a player shoots
down the `aline_0` you can check how many player earns:
```python
aline_0 = {'color': 'green', 'points': 5}

new_points = aline_0['points']
print(f"You just earned {new_points} points!")
```
First you set the dictionary, then you access the points; the output:
```commandline
You just earned 5 points!
```
if you run this code every time an alien is shut down, the alien's point value
will be retrieved.

### 6.2.2 Adding New Key-Value Pairs
Dictionaries are dynamic structures, and you can add new key-value pairs to it
at any time. Let's add two new pieces of information to `alien_0` dictionary:
the alien's x- and y-coordinates, which will hellp us display the alien in a
particular position on the screen.
Let's place the alien on the left edge of the screen. 25 pixels from the top.
Because screen coordinates usually starts  from the upper-left corner on the
screen. We will use x=0, y25:
```python
# REFER: ../6.2.../6.2.2.adding_new_key_value_pairs.../alien.py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```
Please, observe in the output, how data is printed before and after update the
dictionary:
```json lines
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```
The final version of the dictionary contains 4 key-value paris, while the
original two specify 'color' and 'points', the second one 'x-' and
'y-coordinates'.

> As of Python 3.7, dictionaries retain the order in which they were defined. 
When you print a dictionary or loop through its elements, you will see the
elements in the same order in which they were added to the dictionary.


### 6.2.3 Starting with a New-Empty Dictionary
You can create an empty dictionary, and then when it's necessary add  the
required key-value pairs, as follows:
```python
# REFER: ../6.2.../6.2.3.starting_with_an_empty_dictionary.../alien.py
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
```
This simple example results in the same output: 
```json lines
{'color': 'green', 'points': 5}
```

### 6.2.4 Modifying Values in a Dictionary
To modify a dictionary you just need to do the same as you was adding a value,
but using a key that already exist
```python
# REFER: ../6.2.../6.2.3.starting_with_an_empty_dictionary.../alien.py
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")
```
We defined the dictionary with key-value pairs for `alien_0` where the color is 
green, then we updated the color to yellow, therefore the output is:
```commandline
The alien is green.
The alien is yellow.
```
Now we'll do it more complete by storing the alien speed, and determining how
far to the right the alien should move:
```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
```
Notice that other values (color and points) are avoided for simplicity.
We started by giving a position (x, y) and speed (medium) to `alien_0`.
At the `if-elif-else` chain is determined how much the alien is going to move to
the right, where move (units: 'u') depends on the speed:

| Speed  | Units |
|:-------|:------|
| slow   | 1     |
| medium | 2     |
| fast   | 3     |

Then line before the last line, the value is stored in `x_position`. Finally, the
output is:
```commandline
Original x-position: 0
New x-position: 2
```
By changing the one value in the alien's dictionary, you can change the overall
behavior of the alien. For example, to turn this medium-speed alien int a fast
alien, you would add the line:
```python
alien_0['speed'] = 'fast'
```
The if-elif-else block would then assign a larger value to x_increment
the next time the code runs.

### 6.2.5 Removing Key-Value Pairs
For example, let’s remove the key 'points' from the alien_0 dictionary
along with its value:
```python
# REFER: ../6.2.../6.2.5.../alien.py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
```
the <i>key-value pair</i> for `points` disappear; see the output:
```json lines
{'color': 'green', 'points': 5}
{'color': 'green'}
```
><i><b>NOTE</b></i>: Be aware that the deleted key-value pair is removed permanently.

### 6.2.6 A Dictionary of Similar Objects
The previous example shows how to store different kind of information about one
object, but what about storing the same kind of information about many objects?
<br>Here is an example about a dictionary being useful by storing the result of
a simple poll:
```python
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
```
Notice how this dictionary is broken into several lines. Each key is the name of
a person who responded to the poll, and each value a language of their 
preference.

Ok, how to do it? 
set variable equals to and add the opening brace, with this we indicate we are
creating a dictionary:<br>`favorit_language = {`<br>
Hit <i>ENTER</i>, and in the new line indent one level (four spaces),
add the key-value pair with a comma at the end: <br>
&emsp;`'jen': 'python',`<br>
Repeat until you finished adding key-value pairs.
Adding a comma in the last key-pair value, is a good practice, because makes you
ready for adding new lines.<br>
&emsp;`'phil': 'python',`<br>After adding the last new key-pair value, add a
closing brace on a new line. Also, indent it at one level, so it is at the level
of the key-pair values.<br>
&emsp;`}`<br>

>Most editors have some functionality that helps you format extended lists and 
dictionaries in a similar manner to this example. Other acceptable ways to 
format long dictionaries are available as well, so you may see slightly 
different formatting in your editor, or in other sources.

```python
# REFER: ../6.2.../6.2.6.../favorite_languages.py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
```
To see which language Sarah chose, we ask for the value at:
```python
favorite_languages['Sarah']
```
The output:
```commandline
Sarah's favorite language is C.
```

### 6.2.7 Using `get()` to Access Values
If the key you use square brackets to retrieve a key that doesn’t exist,  you’ll
get an error. 
```python
# REFER: ../6.2.../6.2.6.../aline_no_points.py
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])
```
the output is:
```commandline
Traceback (most recent call last):
File "alien_no_points.py", line 2, in <module>
print(alien_0['points'])
KeyError: 'points
```
For dictionaries, specifically, you can use the get() method to
set a default value that will be returned if the requested key doesn’t exist.
The get() method requires a key as a first argument. As a second
optional argument, you can pass the value to be returned if the key doesn’t
exist:
```python
alien_0 = {'color':'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
```
If the code has a key-value pair for you'd get the corresponding value.
Since no point key exists, ir returns:
```commandline
No point value assigned.
```
If there’s a chance the key you’re asking for might not exist, consider
using the get() method instead of the square bracket notation.

>Note: If you leave out the second argument in the call to get() and the key
doesn’t exist, Python will return the value None. The special value None means
“no value exists.” This is not an error: it’s a special value meant to
indicate the absence of a value.

---
## 6.3 Looping Through a Dictionary
A dictionary (in Python) can contain large amount of data, because of it, Python
let you loop  through it. You can loop a dictionary through its keys or through
its values.

### 6.3.1 Looping Through All Key-Value Pairs
Let's consider a dictionary designed to store information about a user on a
website. The following dictionary would store one person's user's name, first
name, and last name:
```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
```
You can access a single value with the approach `user_0['username]`, or you can
use a for loop to go through all the dictionary:
```python
# REFER: ../6.3.../6.3.1.../user.py
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```
Notice that `key` and `value` are variables create to work with the for loop,
and you can name them as you need; for example `k` standing for 'key', and `v`
standing for 'value'; so that you have:
```python
for k, v, in user_0.items()
```
Also, look how the dictionary uses the method `items()`, which
returns a list of key-value paris .

As you can see the `\n` (newline) is printed every time a key is printed,and it
is printed before each 'Key':
```commandline

Key: username
Value: efermi

Key: first
Value: enrico

Key: last
Value: fermi
```
Looping through all key-value pairs works particularly well for dictionaries
which store the same kind of information for many different keys. Let's loop
through the dictionary created for 'favorite_languages.py' where the keys always
refer to a person, and the value to a language. Also, let's use `name` and
`language` instead of `key` and `value` to make it easier to understand what the
`print()` call is doing.

```python
# REFER: ../6.3.../6.3.1.../favorite_languages.py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
```
Python loops through each key-value pair in the dictionary, and assign the key
to `name`, as does with value to 'language'. 
The output:
```commandline
Jen's favorite language is Python
Sarah's favorite language is C
Edward's favorite language is Ruby
Phil's favorite language is Python
```

### 6.3.2 Looping Through All the Keys in a Dictionary
The <i>keys()</i> method is useful when you don't need to work with all the
values in a dictionary. Let's loop through the `favorite_languages` dictionary 
and print the name of everyone who took the poll:
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())
```
The output:
```commandline
Jen
Sarah
Edward
Phil
```
Since looping through the keys the default behavior it would do the same with:
```python
for name in favorite_languages:
    print(name.title())
```
In this case, adding the `keys()` method makes the code easier to read, but it
is up to you.

You can access the value of a key  inside the loop by using the current key.
We'll loop through the dictionary, but now, when we find a specific friend the
program will print a message for that friend.
```python
# REFER: ../6.3.../6.3.2.../favorite_languages.py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
```
We have created a list `friends = ['phil', 'sarah']`. In the conditional we
check whether the `name` we're working with is in the list `firends`. If it is,
we get the value based on that name and formatted with the method `title()`.
The output is:
```commandline
Jen
Sarah
	Sarah, I see you love C!
Edward
Phil
	Phil, I see you love Python!
```
Now let's find out if 'Erin' took the poll
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

if 'Erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
```
The `keys()` method is not just for looping, it returns a list of all the keys.
As you can see in previous code, the conditional line checks if 'Erin' is in the
list. And because she's not, the message is printed:
```commandline
Erin, please take our poll!
```

### 6.3.2 Looping Through a Dictionary's Keys in  a Particular Order
Starting in Python 3.7, looping through a dictionary returns the items in
the same order they were inserted. Sometimes, though, you’ll want to loop
through a dictionary in a different order.
One way to do this is to sort the keys as they’re returned in the for loop.
You can use the sorted() function to get a copy of the keys in order:
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```
This is a normal `for` statement, except that the `dictionary.keys()` is
wrapped in the function `sorted()`. This tells python to sort the list before
looping through the dictionary. The output is:
```commandline
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll
```

### 6.3.2 Looping Through All Values in a Dictionary
If the values are the elements of your interest you can loop through the
dictionary using the `values()` method to return a list of them without keys.
For example, getting the list of languages in the poll:
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print('The following languages have been mentioned in the poll:')
for language in favorite_languages.values():
    print(language.title())
```
The output is:
```commandline
The following languages have been mentioned in the poll:
Python
C
Python
Ruby
```
This approach returns all the values without checking for repeats.
To see each language without repetition you can use `set`.
```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print('The following languages have been mentioned in the poll:')
for language in set(favorite_languages.values()):
    print(language.title())
```
We use set() to pull out the unique languages in favorite_languages.values().
The output:
```commandline
The following languages have been mentioned:
Python
C
Ruby
```
> You can build a set directly by using braces and separating the elements with
> commas: 
> ```pycon
> >>> languages = {'python', 'ruby', 'python', 'c'}
> >>> languages
> {'ruby', 'python', 'c'}
> ```

---
## 6.4 Nesting
Sometimes you’ll want to store multiple dictionaries in a list, or a list of
items as a value in a dictionary. This is called nesting. You can nest 
dictionaries inside a list, a list of items inside a dictionary, or even a 
dictionary inside another dictionary. Nesting is a powerful feature, as the 
following examples will demonstrate.

### 6.4.1 A List of Dictionaries
The alien_0 dictionary contains a variety of information about one alien,
but it has no room to store information about a second alien, much less a
screen full of aliens. How can you manage a fleet of aliens? One way is to
make a list of aliens in which each alien is a dictionary of information about
that alien. For example, the following code builds a list of three aliens:
```python
# REFER: ../6.4.../6.4.1.../aliens.1.py
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```
The output:
```commandline
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
```

A more realistic example would involve more than 3 aliens with code that
automatically generates each alien. In the following example we use `range()`
to create a fleet of 30 aliens:
```python
# REFER: ../6.4.../6.4.1.../aliens.2.py
# Make an empty list for storing aliens.
aliens[]

# Make a 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print(...)

# Show how many aliens have been created.
print(f"Total of aliens: {len(aliens)}")
```
It starts by creating an empty list. Then creates the aliens and appends them to
the list.
When showing the aliens stored, we use a slice to it print the first 5 aliens.
And in the last line it is printed the total of aliens created.
The output is:
```commandline
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
...
Total number of aliens:  30
```
All the aliens have the same characteristics, but Python consider each one a
different object, therefore, each one can be modified individually.

Imagine that while the game progress, aliens change their color and move faster.
When it's time to change colors, we can use a for loop and an `if` statement to
change the color of the aliens. Let's upgrade aliens from level 1 to level 2:

| Level | Color   | Speed  | Points |
|:------|:--------|:-------|:-------|
| 1     | green   | slow   | 5      |
| 2     | yellow  | medium | 10     |
| 3     | red     | fast   | 15     |

```python
# REFER: ../6.4.../6.4.1.../aliens.3.py
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow'}
    aliens.append(new_alien)

# Loop through a slice of the first three aliens and update the values.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
```
In the second for loop, we ensure the aliens are green, because they not always
will be, if they are, we modify them. Here's the output:
```commandline
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
...
```
An `elif` block could be added to modify from yellow to red.
```python
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
```
It's common to store dictionaries with information about one object in lists.
For example, a particular user information is stored in a dictionary (i.e. 
user.py in 6.3.1), but all the dictionaries of all users are stored in a list.
> NOTE: All the dictionaries in a list should have the same structure to be able
> to loop through the list and work with each dictionary object in the same way.

### 6.4.2 A List in a Dictionary
Sometimes is useful to put a list inside a dictionary. For example, consider
describing a pizza being ordered. If you use only a list, you could only store 
a list of toppings. With a dictionary, the toppings, is just one aspect o the 
pizza to describe.

In the following example two kind of information are stored for each pizza:

1. Type of crust.
2. Toppings.

The <i>list of toppings</i> is a value associated with the key 'toppings'. To
use the items in the list give the name of the dictionary and the key.

```python
# REFER: ../6.4.../6.4.2.../pizza.py
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following ingredients:")

for topping in pizza['toppings']:
    print("\t" + topping)
```
We have 3 things to talk about: pizza dictionary; print() call; toppings list.

As you can see, the dictionary `pizza` contains two key-value pairs, the first
one, 'crust' is associated with a <i>string</i>, and the second one, 'toppings',
with a <i>list</i>.<br>

The print() call, has a long text, it was needed to brake it down. Take a look
in these things:
1. Parenthesis wraps both lines.
2. First and second lines starts and end with quotation marks.
3. At the end of the first line remains the space, like this 'pizza '.
4. Indent the second line so it is clear is part of the print function.

To access the list of toppings, we use the key 'toppings'. 

The output is:
```commandline
You ordered a thick pizza, with the following ingredients:
	mushrooms
	extra cheese
```

You can nest a list inside a dictionary anytime you want more than one value to
be associated with a single key in a dictionary.<br>
Suppose that in the example of favorite languages, people could choose more than
one favorite language. When we loop through the dictionary, the value
associated with a person would be a list of languages.
Inside the dictionary's `for` loop, we use another `for` loop to run through the
list of languages:
```python
# REFER: ../6.4.../6.4.2.../favorite_languages.py
fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in fav_languages.items():
    print(f"{name.title()} favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
```
As you can see each name is now associated with a list of languages. Even when
in the list is just one language we can loop through it because it remains the
same structure.<br>
The first `for` loop goes through each key-value pair. The second `for` loop
goes through each value, since is a list and not a single string, like this
example in previous chapters. Now each person can list as many favorite 
languages as they like:
```commandline
Jen favorite languages are:
	Python
	Ruby
Sarah favorite languages are:
	C
Edward favorite languages are:
	Ruby
	Go
Phil favorite languages are:
	Python
	Haskell
```

To refine the program you could include an `if` statement to validate whether
a person has more than one favorite language and adapt the output to that.
```python
fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in fav_languages.items():
    message = "s are" if  len(languages) > 1 else " is"
    print(f"{name.title()} favorite language{message}:")
    for language in languages:
        print(f"\t{language.title()}")
```
The output is:
```commandline
Jen favorite languages are:
	Python
	Ruby
Sarah favorite language is:
	C
Edward favorite languages are:
	Ruby
	Go
Phil favorite languages are:
	Python
	Haskell
```

> You should not nest lists and dictionaries too deeply. If you’re nesting items much
deeper than what you see in the preceding examples or you’re working with someone
else’s code with significant levels of nesting, most likely a simpler way to solve the
problem exists.

### 6.4.3 A Dictionary in a Dictionary
You can nest a dictionary inside another dictionary, but your code can get
complicated quickly when you do.
In the following example consider as a website that has multiple users, and it
requires to store the username as unique value, and also, other information
about the user (firs name, last name, and location).
In the first level of the dictionary is a key-value pair for:
<br>`'username': user_information`<br>
where `user_information` is a dictionary object containing 3 key-value pairs.
<br>`'first': 'user f_name', 'last': 'user l_name', 'location': 'user place',`<br>
```python
# REFER: ../6.4.../6.4.3.../many_users.py
users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        }
    
    }

for username, info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{info['first'].title()} {info['last'].title()}"
    lcation = info['location'].title()
    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location}")
```

The output is:
```commandline
Username: aeinstein
	Full name: Albert Einstein
	Location: Princeton

Username: mcurie
	Full name: Marie Curie
	Location: Paris
```

