from pydoc import describe

# Chapter 8: Functions
### In this chapter you'll learn to create functions, which are blocks of code designed to do one, and only one, specify job.<br>Writing functions can make easy to write, read, test, and fix programs.


---
## 8.1 Defining a function
Here's a simple function named greet_user() that prints a greeting:
```python
# REFER: ../8.1.../greeter.py
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
```
This is a simple structure of a function, let's explain it line by line: <br>

<b><i>1st line: `def greet_user():`, let's brake it down:</b></i>
* `def` is a keyword that informs python that you're creating a function, which 
is called "<i>function definition</i>". it tells Python the name of the function
and what kind of information requires the function to do its job.
* `greet_user` is the name we assign to the function
* `()` inside the parentheses is the information required by the function to do
its job. In this case no information is required, but still, the parentheses
are required.
* `:` this completes the definition of the function,
> NOTE: Any indented line that follows the function definition make up the body
> of the function.

<b><i>2nd line: `"""Display a simple greeting."""`:</b></i>
* `"""docstrings""` it is a comment called <i>docstring</i> and describes what
the function does. Docstrings are enclosed in triple quotes, which Python looks
for when it creates documentation for the functions in your programs.

<b><i>3rd line: `print("Hello!")`:</b></i>
* This is the only line of actual code in the body of the function, so, 
`greet_user()` has one job: `print("Hello!")`.

<b><i>4th line: `greet_user()`:</b></i>
* This is a <i>function call</i>, which tells Python to execute the code in the
function.
> NOTE: To call a function you write the name of the function, followed by any
> necessary information in the parentheses. Beacuse no information is needed
> here, you can call the function just by the function name and parentheses,
> `greet_user()`.

The output is:
```commandline
Hello!
```

### 8.1.1 Passing Information to a Function
By modifying `greet_user()` we can say <i>Hello!</i> by their name. By adding
`username` in the parentheses you add the function can accept any value of
`username` you specify. the function now expects you to provide a value for
`userneame` each time you call it. When you call it, you can pass it a name
such as <i>'jesse'</i>, inside the parentheses:
```python
# REFER: ../8.1.../8.1.1.../greeter.py
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
```
The function accepts the name you passes to it. You can try with other names
like sarah or kevin, and you'll get `Hello, Sarah!` or `Hello, Kevin!
The output of our function:
```commandline
Hello, Jesse!
```

### 8.1.2 Arguments and Parentheses
The variable <i>username</i> in the definition of greet_user() is an example of
a <u><i>parameter</i></u>, a piece of information the function needs to do its
job.<br>
The value <i>'jesse'</i> in `greet_user('jesse')` is an example of an 
<u><i>argument</i></u>.
An argument is a piece of information that’s passed from a function call to a
function.

When we call the function and pass a value like `greet_uer('jesse')`, we are
passing an argument.<br> Therefore, the function receives the value 
<i>'jesse'</i> which is assigned to the parameter <i>'username'</i>.

---
## 8.2 Passing Arguments
You can pass arguments to your functions in several different ways. You can use:
* Positional arguments, which need to be in the same order as the parameters 
were written.
* Keyword arguments, where each argument consist of a variable name and a value.
* Lists and Dictionaries of values.

## 8.2.1 Positional Arguments
Whe you call a function, Python must match each argument in the function call 
with a parameter in the function definition.
"As you declare parameters, as you pass arguments"

Consider the following function that tell us the kind of pet and its name:
```python
# REFER: ../8.2.../8.2.1.../pets.py
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'peter pettigrew')
```
As you can see, the definition of 'describe_pet' a type of animal and the
animal's name. When you call the function `describe_pet()` you need to provide
the animal's type and name, in that order.<br>
In the function the parameters `animal_type` and `pet_name` are used to display
information about the pet. This is the output:
```commandline
I have a hamster.
My hamster's name is Peter Pettigrew.
```

#### 8.2.1.1 Multiple Function Calls
You can call a function as many times as needed. Let's try with other pet.

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'peter pettigrew')
describe_pet('dog', 'rocky')
```
The output:
```commandline
I have a hamster.
My hamster's name is Peter Pettigrew.

I have a dog.
My dog's name is Rocky.
```
Calling a function is an efficient way to work. All the code describing a pet is
written just once and in just one line you can describe a new pet.
You can use all the positional arguments you need. Python will match each
argument you provide with the parameters in the function.

#### 8.2.1.2 Order Matters in Positional Arguments
You can get unexpected results if you mix up the order of the arguments in
a function call when using positional arguments:
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('peter pettigrew', 'hamster')
```
Since 'peter pettigrew' is assigned to `animal_type`, and 'hamster' 
to `pet_name`, the values are mixed up. because order matters. The output is:
```commandline
I have a peter pettigrew.
My peter pettigrew's name is Hamster.
```
If you have a result like this, check that the order of the arguments matches
with the function parameters.

### 8.2.2 Keyword Arguments
A <i>key argument</i> is a name-value pair that you pass to a function. Name and
value are associated.

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(animal_type='hamster', pet_name='peter pettigrew')
```
By using <i>keyword arguments</i> there's no worries about the ordering values.
You can type either
`describe_pet(animal_type='hamster', pet_name='peter pettigrew')`
or
`describe_pet(pet_name='peter pettigrew', animal_type='hamster')`, and the
result will be the same. If you type both you'll obtain:
```commandline
I have a hamster.
My hamster's name is Peter Pettigrew.

I have a hamster.
My hamster's name is Peter Pettigrew.
```
> When you use keyword arguments, be sure to use the exact names of the 
> parameters in the function’s definition.

### 8.2.3 Default Values
When you write a function, you can define <i>default values</i> for each 
parameter. If an argument is provided in the function call, it is used instead
of the default value. If not, the function uses the default value.

So, when you define a default value, you can exclude that argument. 
```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(pet_name='rocky')
```

Using default values can simplify your function calls. If you see, 'dog' is  the
most average pet, you can set 'dog' as default value.
```commandline
I have a dog.
My dog's name is Rocky.
```

Other way, is just pass the pet's name, and the result is the same:
```python
describe_pet('rocky')
```
You can describe other animal type, just call the function like this:
```python
describe_pet(pet_name='peter pettigrew', animal_type='hamster')
```
Because the `animal_type` is provided, Python ignores the default value.

> <h3>IMPORTANT</h3> Notice how the parameters order has changed in the function
> definition:<br>`def describe_pet(pet_name, animal_type='dog'):`
> * The previous order was `(animal_type, pet_name)`.
> * The default value makes unnecessary to specify a type of animal.
> * It is still a positional argument.
> * When you just pass argument `pet_name`, it match up with the function 
> definition.
>
> <h3>Summarizing</h3> In the function definition:
> <i><b>
> * Every <u>parameter with no default value</u> should be placed first.
> * Every <u>parameter with default value</u> should be placed after the
> <u>parameters with no default values</u>.
> </b></i>

### 8.2.4 Equivalent Function Calls
Because positional arguments, keyword arguments, and default values can all be
used together, often you'll have several equivalent ways to call a function.
Consider the following definition for 'describe_pet()' with one default value
provided:
```python
def describe_pet(pet_name, animal_type='dog')
```
With this definition, an argument for `pet_name` always needs to be provided
using either, positional or keyword format.<br>
If the `animal_type` is not a dog, this argument can be specified.

All the following calls would work for this function:
```python
# A dog named Rocky.
describe_pet('rocky')
describe_pet(pet_name='rocky')

# A hamster named Peter Pettigrew 
describe_pet('peter pettigrew', 'hamster')
describe_pet(pet_name='peter pettigrew', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='peter pettigrew')
```
Each of these function calls should have the same output.

> As long as your function calls work as expected, it doesn't matter the style
> you use, just use the easiest to understand.

### 8.2.5 Avoiding Argument Errors
When you start to use functions, don’t be surprised if you encounter errors
about unmatched arguments. Unmatched arguments occur when you
provide fewer or more arguments than a function needs to do its work.

For example, here’s what happens if we try to call describe_pet() with no
arguments:
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()
```
Python recognizes that some information is missing from the function
call, and the traceback tells us that:
```commandline
Traceback (most recent call last):
File "pets.py", line 6, in <module>
describe_pet()
TypeError: describe_pet() missing 2 required positional arguments: 'animal_
type' and 'pet_name'
```
---
## 8.3 Return Values
A function doesn't have to display always its output. I can also return a value
or set of values.<br>
The <i>return</i> statement takes a value from inside the function and sends it
back to the line that called the function.
Return values allow you to move much of your program’s grunt work into
functions, which can simplify the body of your program.

### 8.3.1 Returning a Simple Value
Let’s look at a function that takes a first and last name, and returns a neatly
formatted full name:
```python
# REFER: ../8.3.../8.3.1.../formatted_name.py
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```
We declared a function taking first and last names.<br>
Then, documentation of the function.<br>
The name is gathered into one variable.<br>
The variable is returned as `title()`.<br>

As we are returning a value, we can receive that returned value into a variable,
as `musician`, so, when we call the function we can put the result in it.<br>
The variable is printed.<br>
The output:
```commandline
Jimi Hendrix
```
Consider this is a simple example, and we could just do `print("Jimi Hendirx")`,
but with a larger program, you may "need to get the neat name several times". 

### 8.3.2 Making an Argument Optional
You can use default values to make an argument optional. It makes sense
sometimes, so you should be able to choose if provide it or not, in those times.
<br>
&emsp; Let's consider that `get_formatted_name()` also, uses meddle name:
```python
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
```
In this case is forcing to use the middle name; the output is:
```commandline
John Lee Hooker
```
But, middle names are not always needed, so, we can make this optional:
```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
    

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
```
This modified version of our function works for people with just a first
and last name, and it works for people who have a middle name as well:
```commandline
Jimi Hendrix
John Lee Hooker
```
Optional values allow functions to handle a wide range of use cases
while letting function calls remain as simple as possible.

### 8.3.3 Returning a Dictionary
A function can return any kind of value, like lists or dictionaries.
```python
# REFER: ../8.3.../8.3.3.../person.py
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
```
`build_person` puts first name and last name into a dictionary and return that 
value.<br>
The variable `mucisian` receives the returned value, when calling the function.
<br>
The last line prints the dictionary.
```commandline
{'first': 'jimi', 'last': 'hendrix'}
```
This function creates more meaningful information, since it prints not just the
data, but the label of each element. You can add other elements ot the
dictionary, like age, occupation, or middle name.<br>
&emsp;Let's add the age of the person:
```python
def build_person(firsst_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```
We added `age` to the function and assigned it the special value `None`, used
when a variable has no specific value assigned to it.<br>
In conditional tests, `None` evaluates to `False`. If the call includes the age
it is stored in the dictionary.

### 8.3.4 Using a function with a while Loop
You can use a function with all the Python structures already mentioned so far.

Let's use the `get_formatted_name()` function with a `while` loop to greet users
more formally.
```python
# REFER: ../8.3.../8.3.4.../greeter.py
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```
This was the most basic way to execute the program into a while loop, but, it is
an infinite loop, the easiest way (also, a better experience for the user) to
terminate it is using the first inputs already there. We can do it by adding
three lines:
1. Print quitting information.
2. A conditional statement to know whether break or not.
3. The keyword `break`.
```python
# REFER: ../8.3.../8.3.4.../greeter.py
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
    break
    l_name = input("Last name: ")
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```
The output:
```commandline
Please tell me your name:
(enter 'q' at any time to quit)
First name: eric
Last name: matthes

Hello, Eric Matthes!

Please tell me your name:
(enter 'q' at any time to quit)
First name: q
```

---
## 8.4 Passing a List

---
## 8.5 Passing an Arbitrary Number of Arguments

---
## 8.6 Storing Your Functions in Modules

---
## 8.7 Styling Functions
