# What Really Happens When You Run hello_world.py
General explanation of how the interpreter works

---
## Variables:
Explanation of variable assignation.
```commandline
message = "test"
```

### Naming and Using Variables:
Naming rules and conventions.
```commandline
# Use letters, numers and underscore
# Do not use numbers at the beginning, whitespaces

# Correct naming:
_variable1 = 1
variable1_ = 1
_1variable_ = 1

# Incorrect naming:
_1 variable = 1
1variable = 1

```

### Avoiding Name Errors When Using Variables:
Talks about mistakes when naming, like creating the variable 'message' and call it as 'mesage'.
```commandline
>>> message = "test message 1"
>>> print(mesage)
test message 1
```
### Variables and Labels:
Describes that variables are not containers, but they can be seen as labels assigned to values.

---
## Strings:
General description of strings and combinations between single and double quotes like:
```commandline
>>> print('I like to say: "This is a greate day!".')
I like to say: "This is a greate day!".
>>> print("Lately I have been working with 'Python' for my personal projects.")
Lately I have been working with 'Python' for my personal projects.
```

### Changing Case in a String with Methods:
Samples of capitalization: title(), upper(), lower()

### Using Variables in Strings:
    
```commandline
# REFER TO: full_name.py
>>> first_name = "Alexander"
>>> last_name = "Magnum"
>>> full_name = f"{first_name} {last_name}"
>>> print (full_name)
Alexander Magnum
>>> print(f"Hello, {full_name.title()}!")
Hello, Alexander Magnum!

# an alternative is adding all to a variable and make a simpler call, like this:
>>> message = f"Hello, {full_name.title()}!"
>>> print(message)
Hello, Alexander Magnum!
```

### Adding Whitespace to Strings with Tabs or Newlines:
In the string you can add "\t" for adding a tab and \n for adding a new line, such as follows:
```commandline
# REFER TO: whitespace.py
>>> print("Languages:\n\tPython\n\tC\n\tJavaScript")
Languages:
    Python
    C
    JavaScript
```

### Stripping whitespace
functions for taking off trailing and leading whitespaces 
```commandline
# REFER TO: whitespace.py
>>> favorite_language = ' python '
>>> favorite_language               # No stripping sample
' python '
>>> favorite_language.rstrip()
' python'          # Stripping right sample
>>> favorite_language.lstrip()
'python '          # Stripping left sample
>>> favorite_language.strip()
'python'           # Stripping both sides sample
```

### Avoiding Syntax Errors with Strings
It's important to consider the text erquirements, for example if we need to use an apostrophe within the text it's better to use double quote.
if single quote is used, it will end the message where it finds the apostrophe.
```commandline
# REFER TO: apostrophe.py
>>> message = "One of Python's strengths is its diverse community."
>>> print(message)
One of Python's strengths is its diverse community.

# this following line have a syntax error, :
>>> message = 'One of Python's strengths is its diverse community.'
# the string would be consider 'One of Python' and the rest like unrequired elements that generates syntax error.
```

---
## Numbers
They are used to keep score in games, represent data in visualizations, stor information in web applications, and so on.

### Integers
<sup><small><i>No 'file.py' is created for this topic.</i></small></sup><br>
Add (+); Subtract (-); Multiply (*); Divide (/)
```commandline
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5
```
two multiplication symbol for exponent
```commandline
>>> 3 ** 2
9
>>> 3 ** 3
2
```
Python support the order of operations:
```commandline
>>> 2 + 3*4
14
>>> (2 + 3) * 4
2
```
The spacing in these examples has no effect on how Python evaluates
the expressions

### Floats
<sup><small><i>No 'file.py' is created for this topic.</i></small></sup><br>
For python a <i>float</i> is any number with a decimal point.<br>
For the most part, Python will handle decimals with no problem. Python most likely do what you expect:
```commandline
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
```
But be aware sometimes, computers calculations (at lower levels) are tricky, like when they get 0.3 by a calculation:
```commandline
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
```

### Integers and Floats
<sup><small><i>No 'file.py' is created for this topic.</i></small></sup><br>
When you divide integers you will always get a float, even if the result is a whole number.
```commandline
>>> 4/2
2.0
```
You will get a float when you mix an integer and a float:
```commandline
>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0
```
If you use a float, Python defaults the result as a float.

### Underscores in Numbers
<sup><small><i>No 'file.py' is created for this topic.</i></small></sup><br>
To make more readable numbers, you can use underscore to group digits.<br>
When you print the number, Python will show only the digits.
```commandline
>>> universe_age = 14_000_000_000
>>> print(universe_age)
14000000000
```
Python ignores the underscores, even if digits are not grouped in threes
```commandline
>>> universe_age = 14_00_000_00_25
>>> print(universe_age)
14000000025
```

### Multiple Assignment
<sup><small><i>No 'file.py' is created for this topic.</i></small></sup><br>
Multiple values can be assigned in one single line.<br>
Consider the variables need to be separated by a comma.
```commandline
>>> a, b, c = 1, 2, 3
>>> print(a, b, c)
1 2 3
```
This can shorten and make more readable your programs.

### Constants
<sup><small><i>No 'file.py' is created for this topic.</i></small></sup><br>
You distinguish a constant because it is declared with all capital letters.<br>
Python doesn't have a built-in constant types, even though, programmers use it all capital letters to indicate it should never change. 
```commandline
MAX_CONNECTIONS = 5000
```