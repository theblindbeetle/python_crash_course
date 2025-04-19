# Chapter 4: Working with lists
### This chapter is dedicated for lists creation and manipulation, such as looping through them.

---
## Looping through an Entire List
You’ll often want to run through all entries in a list, performing the same
task with each item. For example, in a game you might want to move every
element on the screen by the same amount, or in a list of numbers you
might want to perform the same statistical operation on every element.
In these and other cases you can use a python's `for` loop.

If we have a list of magicians' names, and we want to print it, doing it one by one would be problematic.
Also, every time a new name is added, or deleted, we would need to update the code.
A better approach is us a `for` loop.
```python
# REFER: magicians.py
magicians = ['alice', 'david', 'calrolina']
for magician in magicians:
    print(magician)
```
The for loop goes one by one each position of the list, and the variable `magician` gets the value of tha position.
This code could be represented by:
```python
magicians = ['alice', 'david', 'calrolina']
magician0 = magicians[0]
magician1 = magicians[1]
magician2 = magicians[2]
print(magician0)
print(magician1)
print(magician2)
```
both chunks of code would give the same result:
```commandline
alice
david
carolina
```

### A Closer Look at Looping
In the previous loop of <<magicians.py>>, Python initially reads the first line of the loop:
```commandline
for magician in magicians:
```
This stablish the list `magicians` and associate it with the variable `magician`.<br>
The first value is 'alice'. Python then reads the next line:
```python
print(magician)
```
Python prints the current value 'alice'. Since the list contains more values, Python returns to the first line of the loop:
```python
for magician in magicians:
```
but this time, the value assigned to the variable `magician` is 'david':
```python
print(magician)
```
Python prints 'david' and goes back again the first line of the loop and finds 'carolina' and print it.<br>
Because there are no more values, python goes to the following line. For this program there are no more lines, so, the program simply ends.<br>
When you write down you own loops, consider the variable in the loop (`magician` in the previous example) can be anything, but it's preferable that it is a meaningful name that represents a single item of the list; for example:
```python
for cat in cats:
for dog in dogs:
for item in list_of_items:
```
This naming convention can be helpful with the following action being done on each item.<br>
Using singular and plural names can help to identify if a section of the code is working with a signle element froim the list or the entire list.

### Doing More Work Within a for Loop
You can do just about anything with each item in a `for` loop. let's print a message as example:
```python
# REFER: magicians2.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"That was an incredible trick, {magician.title()}")
```
the output:
```commandline
That was an incredible trick, Alice
That was an incredible trick, David
That was an incredible trick, Carolina
```
It is possible to write as many lines of code as you need in the `for` loop.
Every indented line following the `for` loop is <i>inside the loop</i>.
Let's add another line to the loop:
```python
# REFER: magicians3.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"That was an incredible trick, {magician.title()}")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
```
the output:
```commandline
That was an incredible trick, Alice
I can't wait to see your next trick, Alice.

That was an incredible trick, David
I can't wait to see your next trick, David.

That was an incredible trick, Carolina
I can't wait to see your next trick, Carolina.
```


### Doing Something After a for Loop
Any lines of code after the `for` loop that are not indented are executed after the loop, without repetition.<br>
Let's write a thanks message to the group:
```python
# REFER: magicians4.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"That was an incredible trick, {magician.title()}")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")
```
the output:
```commandline
That was an incredible trick, Alice
I can't wait to see your next trick, Alice.

That was an incredible trick, David
I can't wait to see your next trick, David.

That was an incredible trick, Carolina
I can't wait to see your next trick, Carolina.

Thank you, everyone. That was a great magic show!
```

---
## Avoiding Indentation Errors
Python uses indentation to determin how a line, or group of lines, is related to the rest of the program.<br>
Basically, it uses whitespace to force you to write neatly formatted code
with a clear visual structure. In longer Python programs, you’ll notice
blocks of code indented at a few different levels. These indentation levels
help you gain a general sense of the overall program’s organization.

### Forgetting to Indent
After a `for` statement in a loop you need to indent the lines related to the loop, not doing is an error in the syntax of Python.
```python
# REFER: magicians5.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```
if you try to run this it will cause an `IndentationError`:
```commandline
  File "magicians5.py", line 3
    print(magician)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 2
```

### Forgetting to Indent Additional Lines
Sometimes you may forget to indent additional lines, this is a context error, because the syntax is correct and the program will work, but not with the behavior expected:
```python
# REFER: magicians6.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
print(f"I can't wait to see your next trick, {magician.title()}.\n")
```
the output:
```commandline
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
```

### Indenting Unnecessarily
If a line is indented unnecessarily, Python will throw an error when trying to run, for example:
```python
# REFER: 4.2.3.hello_world.py
message = "Hello Python world!"
print(message)
```
the output:
```commandline
  File "4.2.3.hello_world.py", line 2
    print(message)
IndentationError: unexpected indent
```
Avoid using indentation unless it is necessary.

### Indenting Unnecessarily After the Loop
If you indent after the loop a line that should not be part of it, the loop will execute it with every item of the list:

```python
# REFER: magicians7.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
    print("Thank you everyone, that was a great magic show!")

```
the output:
```commandline
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

Thank you everyone, that was a great magic show!
David, that was a great trick!
I can't wait to see your next trick, David.

Thank you everyone, that was a great magic show!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you everyone, that was a great magic show!
```
As you can see, it does not matter the spaces, it is part of the loop just by the indentation.

This is another logical error, similar to the one in “Forgetting to Indent
Additional Lines” on page 54. Because Python doesn’t know what you’re
trying to accomplish with your code, it will run all code that is written in
valid syntax.

### Forgetting the Colon
The colon (:) at the end of a for statement tells Python to interpret the next  line as the start of a loop.
```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians
    print(magician)
```
If you accidentally forget the colon, you’ll get a syntax
error because Python doesn’t know what you’re trying to do. Although
this is an easy error to fix, it’s not always an easy error to find.

---
## Making Numerical Lists
Many reasons exist to store a set of numbers. For example, you’ll need to
keep track of the positions of each character in a game, and you might want
to keep track of a player’s high scores as well.<br>
Lists are ideal for storing sets of numbers, and Python provides a
variety of tools to help you work efficiently with lists of numbers. 

### Using the range() Function
Python’s range() function makes it easy to generate a series of numbers.
For example, you can use the range() function to print a series of numbers
like this:
```python
# REFER: first_numbers.py
for value in range(1, 5):
    print(value)
```
the output:
```commandline
1
2
3
4
```
in this example, `range()` prints only the numbers 1 through 4, which is a behavior <i>off-by-one</i> common in programming languages.
In Python the `range()` function starts with the first value provided, and stops on the second one. Then, to print 1-5 you would use `range(1,6)

You can also pass one argument to `range()`, and it will return a sequence of numbers at 0:
```python
for value in range(6):
    print(value)
```
The output
```commandline
0
1
2
3
4
5
```
### Using range() to Make a List of Numbers
If you want to make a list of numbers, you can convert the results of range()
directly into a list using the list() function.
```python
numbers = list(range(1, 6))
print(numbers)
```
the output:
```commandline
[1, 2, 3, 4, 5]
```
Also, if you pass a third argument to range(), Python uses that value
as a step size when generating numbers.
```python
# REFER: even_numbers.py
even_numbers = list(range(2, 11, 2))
print(even_numbers)
```
the output:
```commandline
[2, 4, 6, 8, 10]
```
You can create almost any set of numbers you want to using the range()
function. For example, consider how you might make a list of the first 10
square numbers (that is, the square of each integer from 1 through 10). In
Python, two asterisks (**) represent exponents. Here’s how you might put
the first 10 square numbers into a list:

```python
# REFER: squares.py
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
```
the output:
```commandline
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

You can write this core more efficiently by avoiding the temporary variable `square`:
```python
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)
```
Sometimes using a temporary variable makes your code easier to read; other times it makes the code unnecessarily long. Focus first on
writing code that you understand clearly, which does what you want it to do.
Then look for more efficient approaches as you review your code

### Simple Statistics with a List of Numbers
A few Python functions are helpful when working with lists of numbers.
For example, you can easily find the minimum, maximum, and sum of a list of numbers:
```commandline
>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
4
```

### List Comprehensions
The earlier example of squares used three or four lines of code. A <i>list comprehension</i> allows you to generate the same list in just one line of code:

A <i>list comprehension</i> combines the `for` loop and the creation of new elements into one line, and automatically appends each new element.<br>
The following example shows the same list of square numbers but uses a list comprehension:
```python
# REFER: squares2.py
squares = [value**2 for value in range(1,11)]
print(squares)
```
To use this syntax, begin with a descriptive name for the list, such as
squares. Next, open a set of square brackets and define the expression for
the values you want to store in the new list. In this example the expression is value**2, which raises the value to the second power. Then, write
a for loop to generate the numbers you want to feed into the expression,
and close the square brackets. The for loop in this example is for value
in range(1, 11), which feeds the values 1 through 10 into the expression
value**2. Notice that no colon is used at the end of the for statement.
The result is the same list of square numbers you saw earlier:
```commandline
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
It takes practice to write your own list comprehensions, but you’ll find
them worthwhile once you become comfortable creating ordinary lists.

---
## Working with Part of a List
In Chapter 3 you learned how to access single elements in a list, and in this
chapter you’ve been learning how to work through all the elements in a list.
You can also work with a specific group of items in a list, which Python calls
a slice.

### Slicing a List
To make a slice, you specify the index of the first and last elements you
want to work with. As with the range() function, Python stops one item
before the second index you specify.<br>
To output the first three elements  in a list, you would request indices 0 through 3, which would return elements 0, 1, and 2.<br>
The following example involves a list of players on a team:

```python
# REFF: players.py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
```
It indicates where to start and where to stop. The output:
```commandline
['charles', 'martina', 'michael']
```

<br>You can generate any subset of a list. for example starting on 1 and stopping on 4:
```python
# REFF: players2.py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
```
the output:
```commandline
['martina', 'michael', 'florence']
```

<br>By omitting the first index in the slice, Python starts at the beginning of the list (or index 0):
```python
# REFF: players3.py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
```
the output:
```commandline
['charles', 'martina', 'michael', 'florence']
```

<br>A similar syntax works if you want a slice that includes the end of a list:
```python
# REFF: players4.py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
```
the output:
```commandline
['michael', 'florence', 'eli']
```
<br>Recall that a negative index returns an element a certain distance from the end of a list;
therefore, you can output any slice from the end of a list:
```python
# REFF: players5.py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
```
the output:
```commandline
['michael', 'florence', 'eli']
```
<br>
Slicing accepts a third element `step` that indicates how many items to skip between items:
```commandline
# Start at index 1, stop at index 8, step of 2
print(numbers[1:8:2])  # Output: [1, 3, 5, 7]
```

### Looping Through a Slice
You can use a slice in a for loop.<br>
In the next example we loop through the first three
players and print their names as part of a simple roster:
```python
# REFFL players6.py
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
```
Instead of looping through the entire list of players, Python loops
through only the first three names:
```commandline
Here are the first three players on my team:
Charles
Martina
Michael
```

<br>Slices are very useful in a number of situations. For instance, when you’re
creating a game, you could add a player’s final score to a list every time thatWorking with Lists 63
player finishes playing.

### Coping a List
Often, you’ll want to start with an existing list and make an entirely new list
based on the first one. Let’s explore how copying a list works and examine
one situation in which copying a list is useful.

To copy a list, you can make a slice that includes the entire original list
by omitting the first index and the second index ([:]). This tells Python to
make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.

For example, imagine we have a list of your favorite foods and want to
make a separate list of foods that a friend likes. This friend likes everything
in our list so far, so we can create their list by copying yours:
```python
# REFF: fppds.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```
the output:
```commandline
My favorite foods are:
['pizza', 'falafel', 'carrot cake']
My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake']
```

To prove you're creating a new list, add a new food to each list.
```python
# REF Chapter4.../4.4.../foods2.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```
the output:
```commandline
My favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake', 'ice cream']
```
Probably it seems easier to just say to python `list_copy = list_original`, but 
what happens when you do this is that `list_copy` is just pointing to the other 
list, instead of copying the values. Let's try this out:
```python
# REF Chapter4.../4.4.../foods3.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```
The output:
```text
My favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
```
This syntax actually tells Python to associate
the new variable friend_foods with the list that is already associated with
my_foods, so now both variables point to the same list. As a result, when we
add 'cannoli' to my_foods, it will also appear in friend_foods.

---
## Tuples
Lists work well for storing collections of items that can change throughout
the life of a program. The ability to modify lists is particularly important
when you’re working with a list of users on a website or a list of characters in
a game. However, sometimes you’ll want to create a list of items that cannot
change. Tuples allow you to do just that. Python refers to values that cannot
change as immutable, and an immutable list is called a tuple.

### Defining a Tuple
A tuple looks like a list except you use parentheses instead of square brackets.<br>
If we have a rectangle that is always the same size, we can ensure it's size doesn't change by putting its dimensions into a tuple:
```python
# REF: "Chapter 4.../4.4.../dimensions.py"
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
```
the output:
```commandline
200
50
```
trying to change the value in a tuple:
```python
# REF: "Chapter 4.../4.4.../dimensions2.py"
dimensions = (200, 50)
dimensions[0] = 250

print(dimensions[0])
print(dimensions[1])
```
the output:
```commandline
Traceback (most recent call last):
  File "dimensions2.py", line 2, in <module>
    dimensions[0] = 250
    ~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
```
Python returns an error for trying to update a tuple.

> Tuples are technically defined by the presence of a comma;
> the parentheses make them look neater and more readable.
> If you want to define a tuple with one element, you need to include a trailing comma:
> `my_t = (3,)`
> It doesn’t often make sense to build a tuple with one element, but this can happen  when tuples are generated automatically.

### Looping Through All Values in a Tuple

```python
# REF: "Chapter 4.../4.4.../dimensions3.py"
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
```
Python returns all the elements in the tuple, just as it would for a list:
```commandline
200
50
```

### Writing over a Tuple
Although you can not modify a tuple, you can re-write the whole tuple:
```python
# REF: "Chapter 4.../4.4.../dimensions3.py"
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
print(dimension)
```
The output:
```commandline
Original dimensions:
200
50

Modified dimensions:
400
100
```

---
## Styling Your Code
Take the time to making easy-to-read code, that helps you keep track of what your programs are doing,
and helps others understand your code as well.
Python programmers have agreed on a number of styling conventions.<br>
You should begin following these guidelines as soon as possible to develop good habits.

### The Style Guide
When someone wants to make a change to the Python language, they write a Python
Enhancement Proposal (PEP).

One of the oldest PEPs is PEP 8, which is fairly lengthy, and instructs Python
programmers on how to style  their code. But much of it relates to more complex
coding structures than what you’ve seen so far.

The Python style guide was written with the understanding that code is read more
often than it is written. Given the choice between writing code that’s easier
to write or code  that’s easier to read. Python programmers will almost always
encourage you to write code that’s easier to read.

The following guidelines will help you write clear code from the start.

### Indentation
PEP 8 recommends that you use four spaces per indentation level. 
It improves readability while leaving room for multiple levels of indentation
on each line.<br>
In a word processing document, people often use tabs rather than spaces to 
indent. Python interpreter gets confused when tabs are mixed with spaces. Mixing
tabs and spaces in your file can cause problems that are very difficult to
diagnose.

### Line Length
Many Python programmers recommend that each line should be less than
80 characters. Historically, this guideline developed because most computers
could fit only 79 characters on a single line in a terminal window.
Currently, people can fit much longer lines on their screens, but other
reasons exist to adhere to the 79-character standard line length. Professional
programmers often have several files open on the same screen, and using
the standard line length allows them to see entire lines in two or three files
that are open side by side onscreen.

PEP 8 also recommends that you limit all of your comments to 72 characters per
line, because some of the tools that generate automatic documentation for larger 
projects add formatting characters at the beginning of each commented line.

Summarizing:
* Code: 79-characters
* Comments:  72-characters

> You can configure the line by going to the settings of your IDE, such as the
> spaces for the key 'TAB'.

### Blank Lines
To group parts of your program visually, use blank lines. You should use blank
lines to organize your files, but don’t do so excessively. By following the
examples provided in this book, you should strike the right balance.
For example, if you have five lines of code that build a list, and then another
three lines that do something with that list, it’s appropriate to place a blank
line between the two sections.

However, you should not place three or four blank lines between the two
sections. Blank lines won’t affect how your code runs, but they will affect the
readability of your code. The Python interpreter uses horizontal indentation to
interpret the meaning of your code, but it disregards vertical spacing.

### Other Style Guidelines
PEP 8 has many additional styling recommendations, but most of the guidelines
refer to more complex programs than what you’re writing at this point. As you
learn more complex Python structures, I’ll share the relevant parts of the PEP 8
guidelines.

