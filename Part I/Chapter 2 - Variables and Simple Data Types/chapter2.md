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
message = "test message 1"
print(mesage)
```
### Variables and Labels:
Describes that variables are not containers, but they can be seen as labels assigned to values.

---
## Strings:
General description of strings and combinations between single and double quotes like:
```commandline
print('I like to say: "This is a greate day!".')
print("Lately I have been working with 'Python' for my personal projects.")
```

### Changing Case in a String with Methods:
Samples of capitalization: title(), upper(), lower()

### Using Variables in Strings:
    
```commandline
# REFER TO: full_name.py
    first_name = "Alexander"
    last_name = "Magnum"
    full_name = f"{first_name} {last_name}"
    print (full_name)
    # output >>> Alexander Magnum
    print(f"Hello, {full_name.title()}!")
    # output >>> Hello, Alexander Magnum!
    
    # an alternative is adding all to a variable and make a simpler call, like this:
    message = f"Hello, {full_name.title()}!"
    print(message)
    # output >>> Hello, Alexander Magnum!
```

### Adding Whitespace to Strings with Tabs or Newlines:
In the string you can add "\t" for adding a tab and \n for adding a new line, such as follows:
```commandline
# REFER TO: whitespace.py
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# output
#   Languages:
#       Python
#       C
#       JavaScript
```

### Stripping whitespace
functions for taking off trailing and leading whitespaces 
```commandline
# REFER TO: whitespace.py
favorite_language = ' python '
favorite_language               # No stripping sample
# OUTPUT >>> ' python '
favorite_language.rstrip()
# OUTPUT >>> ' python'          # Stripping right sample
favorite_language.lstrip()
# OUTPUT >>> 'python '          # Stripping left sample
favorite_language.strip()
# OUTPUT >>> 'python'           # Stripping both sides sample
```

### Avoiding Syntax Errors with Strings
It's important to consider the text erquirements, for example if we need to use an apostrophe within the text it's better to use double quote.
if single quote is used, it will end the message where it finds the apostrophe.
```commandline
# REFER TO: apostrophe.py
message = "One of Python's strengths is its diverse community."
print(message)
# Output >>> One of Python's strengths is its diverse community.

# this following line have a syntax error, :
message = 'One of Python's strengths is its diverse community.'
# the string would be consider 'One of Python' and the rest unrequired elements generating syntax error.
```

---
## Numbers