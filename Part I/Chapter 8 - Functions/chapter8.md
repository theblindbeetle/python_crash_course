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

---
## 8.4 Passing a List

---
## 8.5 Passing an Arbitrary Number of Arguments

---
## 8.6 Storing Your Functions in Modules

---
## 8.7 Styling Functions
