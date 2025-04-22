
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

---
## 6.4 Nesting

