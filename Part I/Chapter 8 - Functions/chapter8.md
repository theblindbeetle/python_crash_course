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
> necessary information in the parentheses. Because no information is needed
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

### 8.2.1 Positional Arguments
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
You can pass to a function simple lists, containing, numbers or names, or maybe
more complex objects, such as dictionaries.<br>
&emsp;Here's an example, with a list of users we're going to greet.
```python
# REFER: ../8.4.../greet_users.py
def greet_users(names):
    """Print a simple greeting to each usr in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hanna', 'ty', 'margo']
greet_users(usernames)
```
We create a function that receives the argument `names`, which is a list.  In
the for loop, we go through it, create a string with current name and print it.
<br>We create a list with as many names we need, in this case, three.
<br>We call the function, and pass the list of names ot it.
<br>The output:
```commandline
Hello, Hanna!
Hello, Ty!
Hello, Margo!
```

### 8.4.1 Modifying a List in a Function
When you pass a list to a function, the function can modify the list.<br>
<i>Any changes made to the list inside the function's body are permanent.</i>

&emsp;Consider a company that creates 3D printed models of designs that 
users submit. Designs that need to be printed are stored in a list, and after
being printed they're moved to a separated list. The following code does this
without using functions:
```python
# REFER: ../8.4.../8.4.1.../printing_models.py
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until non are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Pringin model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```
Le's put this process into steps abd simple words:
1. We create a list with the models to print (`unprinted_designs`).
2. And another empty list (`completed_models`).
3. The `while` loop goes through all the items in `unprinted_designs`.
   * assign the last value of the list to `current_design` and deletes it from 
   the list.
   * prints a message of the current printing model
   * adds the printed value to `completed_models`
4. Prints all the items added to `completed_models`.

The output:
```commandline
Pringin model: dodecahedron
Pringin model: robot pendant
Pringin model: phone case

The following models have been printed:
dodecahedron
robot pendant
phone case
```
This code can be reorganized in two functions. While the code remains almost the
same, it can be considered more carefully structured.<br>
&emsp;The first function prints the designs, and the second, summarize the
prints made.
```python
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until non are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following modelos have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
```
Let's brake it down:
1. We define `printing_model` with two parameters: a list of the designs
required to print, and a list of completed models.
   1. in the loop, each model being printed is deleted from first list and
   moved to the second list. from `unprinted_designs` to `completed_models`
2. We define `show_completed_models`, where prints each element of the list
`completed_models`.

Both programs have the same output, but this is more organized. Look how easier
to understand is the main part of this program:
```python
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
```
Let's break it down one more time:
1. We create a list with unprinted designs.
2. We create an empty list.
3. We call the function that prints the models.
4. We call the function that prints a list of the printed models.

This program is easier to extend and maintain than the version without
functions. If we need to print more designs, we can simply call `print_models`
again. If the printing code needs to be modified, we can change it once, and
those changes will take place everywhere the function is called.

This example also demonstrate the idea that every function should have one 
specific job. The first function prints each design, and the second displays the
completed models. This is more beneficial than using one function to do both 
jobs.

If you are writing a function and notice it has many tasks, try to split it up,
and remember you can call a function from another function, which can be helpful
when splitting a complex task into a series of steps.

### 8.4.2 Preventing a Function from Modifying a List
If you want to prevent a function from modifying a list, not as the previous
example, where we have list_a and the function moves all the elements to list_b.
<br>Then, you can address this issue by passing to the function a copy of the
list, not the original. The changes will affect the copy, living the original
list intact.

You can send a copy of a list to a function like this:
```python
function_name(list_name[:])
```
&emsp; The slice notation `[:]` makes a copy of the list ti send to the function.
If we didn't want to empty the list of `unprinted_designs` in 
<i>printing_models.py</i> we could call `print_models()` like this:
```python
print_models(unprinted_designs[:], completed_models)
```
The function can work because it still receives the information in the list 
`unprinted_designs`. The difference is that the list is not the original one, 
but a copy.

Even though you can preserve the contents of a list by passing a copy of it to
your functions, you should pass the original list to functions unless you have a
specific reason to pass a copy.<br> 
&emsp;It’s more efficient for a function to work with an existing list to avoid
using the time and memory needed to make a separate copy, especially when you’re
working with large lists.

---
## 8.5 Passing an Arbitrary Number of Arguments
If you don't know how many arguments the function will require, Python handles
functions with an arbitrary number of parameters.<br>
Let's consider building a pizza, It needs to accept a number of toppings, but
you can't know ahead of time how many toppings a person will want. The function
in the following example has one parameter, `*toppings`, but this time collects
as many arguments as the calling line provides:
```python
# REFER: ../8.5.../pizza.py
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```
Let's break down this function definition:
1. The parameter with an asterisk with the parameter name (`*toppins`) tells
Python to create an empty tuple.
2. Prints the parameter. Also, consider it handle different amount of
parameters, as we call the function each time with 1 and 3 values.

> Notice how python packs the arguments into a tuple, even if the function
> receives only one value:
```
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')
```
Now, let's create a more organized output by looping the list and printing 
values:
```python
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nPizza with toppings:")
    for topping in toppings:
       print(f"\t- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```
As you can see, the function adapts to the different amount of values:
```commandline

Pizza with toppings:
	- pepperoni

Pizza with toppings:
	- mushrooms
	- green peppers
	- extra cheese
```

### 8.5.1 Mixing Positional and Arbitrary Arguments
To mix up different kind of arguments, the parameter-arbitrary must be placed
last in the function definition. Positional and keyword arguments first, then,
any remaining arguments in the final parameter.<br>
&emsp;Let's try a pizza requiring size and toppings;
```python
def make_pizza(size, *toppings):
    """Print the size of the pizza and the required toppings"""
    print(f"\nLet's make a:\n\t{size}' pizza\nWith the toppings:")
    for topping in toppings:
        print(f"\t- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```
First we have a direct positional value on `size` everything after that is
stored in the tuple `toppings`, and the output is:
```commandline 

Let's make a:
	16' pizza
With the toppings:
	- pepperoni

Let's make a:
	12' pizza
With the toppings:
	- mushrooms
	- green peppers
	- extra cheese
```
> You’ll often see the generic parameter name `*args`, which collects arbitrary positional
> arguments like this.

### 8.5.2 Using Arbitrary Keyword Arguments
Python can also accept an arbitrary number of key-value paris as the calling
statement provides. For example, building user profiles where you know that the
function will get information about the user, but it doesn't know what kind of
information will be received.

The Function `build_profile()` takes in a first and last name, but it accepts an
arbitrary number of keyword arguments as well:
```python
# REFER: ../8.5.../8.5.2.../user_profile.py
def build_profile(first, last, **user_info):
   """Build a dictionary containing everything we know about a user."""
   user_info['first_name'] = first
   user_info['last_name'] = last
   return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='phyciscs')
print(user_profile)
```
Let's see in detail this code:
Summarizing, we created a function with two positional parameters and one
'arbitrary key-pair values argument', which is a dictionary (because of the 
`**`). Positional arguments are assigned to the dictionary, to return that
dictionary with all the values. the value is returned to a variable which is
printed.

If you want to see a more detailed explanation go through the following points
where it's break down point by point:

* The definition of  `build_profile()` expects a first and last name, then any
quantity of <i>name-value</i> paris as they want.
* With a double asterisk before a parameter Python creates an empty dictionary. 
* Within a function you can access the key-value pairs of <i>user_info</i> as
any dictionary.
* The body of `build_profile()` adds `first` and `last` to the dictionary 
`user_info`, why? because:
  * We always receive these two pieces of information.
  * They are not in the dictionary yet.
  * We return a dictionary with all the user's information to the call line.
* We call `build_prodile()`, passing `'albert'`, `'einstein'`, and two key-pair
values, `location='princeton'`,  and `field='phyciscs'`.
* The returned value is assigned to `user_profile`.
* We print the dictionary returned to `user_profile`.

* The output is:
```commandline
{'location': 'princeton', 'field': 'phyciscs', 
'first_name': 'albert', 'last_name': 'einstein'}
```
You can mix positional, keyword, and arbitrary values in many different ways
when writing your own functions.
> You’ll often see the parameter name **kwargs used to collect non-specific keyword
arguments.

---
## 8.6 Storing Your Functions in Modules
You can separate functions from your main program by putting the in a different
file. That file is called a <i>module</i>, which, by <i>importing</i> it, can be
used in your main program. The <i>import</i> statement tells Python to make
available in the main program the code in a module.

Advantages of separating functions in different files:
* Your code to be more focused on higher-level logic
* Functions ca be reused in different programs. 
* You can share those files with other programmers without sharing your entire
program.
* You can use libraries of functions that other programmers have written.

### 8.6.1 Importing an Entire Module
To start importing functions, we need to create a module. A <i>module</i> is a
file ending in <i>.py</i> that contains the code you want to import in your
program.<br>
&emsp;Let's make a module containing the function `make_pizza()`. To make this
module we'll remove everything from the file <i>pizza.py</i> except the function
`make_pizza()`:
```python
# REFER: ../8.6.../8.6.1.../pizza.py
def make_pizza(size, *toppings):
    """Summary the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")
```
Now we'll make a separated file called <i>making_pizzas.py</i> in the same 
directory as <i>pizzas.py</i>. This file imports the module we just created and
then makes two calls to `make_pizza()`:
```python
# REFER: ../8.6.../8.6.1.../making_pizzas.py
import pizza

pizza.make_pizza(16, '')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```
The line `import pizza` tells Python to copy all the functions from 
<i>pizza.py</i> into this program. The code is not visible in it, because all
this happens behind the scenes before the program runs. What you need to know is
that <i>pizza.py</i> is available in <i>making_pizzas.py</i>.<br>
&emsp;To call a function from an imported module, enter the name of the module
you imported followed by the name of the function, this, separated by  a dot.

This code produces the same output as the original that didn't import a module:
```commandline

Making a 16-inch pizza with the following toppings:
	- 

Making a 12-inch pizza with the following toppings:
	- mushrooms
	- green peppers
	- extra cheese
```

This way of importing, `import` followed by the <i>module name</i>, make every
function in the module available in your program by using the following syntax:
```python
module_name.function_name()
```

### 8.6.2 Importing Specific Functions
You can import just a specific function from a module:
```python
from module_name import function_name
```
By separating with a comma, you can add as many functions you want from a module:
```python
from module_name import function_0, function_1, function_2, function_3 
```
The <i>making_pizza.py</i> example with this approach, looks like this:
```python
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```
In this case the dot notation is not necessary, because you imported the
specific function `make_pizza()` in the import statement.<br>
Instead of `pizza.make_pizza()`, you use `make_pizza()`.

### 8.6.3 Using `as` to Give a Function an Alias
For any convenient situation, as shortening a long name, or conflict with your
current naming on you program, you can assign a nickname to a function when 
importing it.<br>
&emsp;You can call `make_pizza()` with the alias `mp()` by importing it as `mp`:
```python
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```
Instead of `make_pizza()`, you use `mp()`. The general
syntax:
```python
from module_name import function_name as fn
```

### 8.6.4 Using as to Give a Module an Alias
A module can also have an alias
```python
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```
Instead of `pizza.make_pizza()`, you use `p.make_pizza()`. The general syntax:
```python
import module_name as mn
```
Calling the function with `p.make_pizza()` is more concise than 
`pizza.make_pizza()` and redirects your attention from the module name and allows you
to focus on the descriptive names of its functions.

### 8.6.5 Importing All Functions in a Module
You can import every function in a module by using the asterisk operator `*`,
which is the same as importing each function by its name, so you don't need the
dot notation.<br>
It's better not using this approach when you're working with large modules you
didn't write; when a function matches a name you use you can have unexpected
results, because Python don't separate imported variables and functions, but 
overwrites them.
> The best approach is to import the function you want, or import the entire
> module and use the dot notation. This lead to clear code that's easy to read
> and understand.

However, you can recognize this by the syntax:
```python
from module_name import *
```

---
## 8.7 Styling Functions
For styling functions keep in mind:
* Naming:
  * Descriptive names.
  * Use lowercase.
  * Use underscores.
* Function description:
  * A comment describing concisely what the function does.
  * The comment appear immediately after the function definition.
  * Use docstring format.

> In a well-documented function, any programmer can use the function just by
> reading the description in the docstring.<br>
> As long as they know the name of the function, the arguments it needs, and the
> kind of value it returns, they should be able to use it in their programs.

If you specify a default value for a parameter, no space should be used on
either side of the equal sign:
```python
def function_name(parameter_0, parameter_1='default value')
```

The same convention should be used for keyword arguments in function calls:
```python
function_name(value_0, parameter_1='value')
```

* PEP 8 (https://www.python.org/dev/peps/pep-0008/) recommends that you limit
lines of code to 79 characters so every line is visible in a reasonably
sized editor window. If a set of parameters causes a function’s definition to
be longer than 79 characters, press enter after the opening parenthesis on
the definition line.
* On the next line, press tab twice to separate the list of
arguments from the body of the function, which will only be indented one
level.

Most editors automatically line up any additional lines of parameters to
match the indentation you have established on the first line:

```python
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...
)
```

If your program or module has more than one function, you can separate each by
two blank lines to make it easier to see where one function ends and the next
one begins.

All import statements should be written at the beginning of a file.
The only exception is if you use comments at the beginning of your file to
describe the overall program.



