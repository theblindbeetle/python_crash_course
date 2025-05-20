# Chapter 9: Classes
### In OOP you create <i>classes</i> that represent real-world situations, and you create <i>objects</i> based on these classes.
Making an object from a class is called <i>instantiation</i>, and you work with
<i>instances</i> of that class.

Classes also make life easier for you and the other programmers you'll work 
with as you take on increasingly complex challenges. Your programs will make 
sense to many collaborators, allowing everyone to accomplish more.


---
## 9.1 Creating and using classes
You can model almost anything using classes. Let's create the class <i>dog</i>,
that represent any dog. What we know about dogs is they have name and age,
also, the roll-over and sit. We will add that information and behavior about 
the dog to our class: 
* name
* age
* sit
* roll over

This class tells Python how to make an object representing a dog.<br> One more
thing, we'll use the class to make individual instances, which represent one
specific dog.

### 9.1.1 Creating the Dog Class
Each instance created from the Dog class will store `name` and `age`, and the
ability to `sit()` and `roll_over()`:
```python
class Dog:
# REFER: ../9.1.../9.1.1.../dog.py
    """A simple attemp to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
```
Let's break this piece of code:
* `class Dog:` - is the definition of a class called 'Dog'. In Python, classes
are capitalized. The class has no parentheses because we're creating it from 
scratch. 
* Docstring - triple quotes that describes what the class does.
---
#### 9.1.1.1 The __init__() Method
Let's start with what is a method, what is the `__init__()` method, and why to
use the underscores:
* A function that is part of a class is a <i>method</i>, however, it's still a 
class. The only difference for now is how we'll call them.
* The <i>__init__()</i> method is a special method that Python runs
automatically whenever we create a new instance based on the Dog class.
* The two leading/trailing underscores are to prevent Python's default methods
from conflicting with you methods names.

> Be sure of adding two leading and trailing underscores, otherwise the method
> won't be called automatically.
---
Now let's go and break down the method `__init__(self, name, age):`: 
* It has three parameters: `self`, `name`, and `age`. 
  * The `self` parameter is required, and must come before the other 
parameters.

  > In a method call, Python passes automatically `self` as an argument.
  > Every method associated with an instance automatically passes `self`, which
  > is a reference to the instance itself, and gives to the individual instance 
  > access to the attributes and methods in the class.<br><br>
  > When we make an instance of  `Dog`, Python will call the `__init__()` 
  > method   > from the `Dog` class. We'll pass `Dog()` name and age as
  > arguments; `self` is passed automatically (we don't need to pass it). When 
  > we make an instance of `Dog` we just pass `name` and `age`.

* The variables within the method has the prefix `self`.
  * Every variable prefixed `self` is available for every method in the class.
  * We'll be able to access these variables through any instance crated from 
the class.
  * The line `self.name = name` takes the value associated with the parameter
`name` and assigns it to the variable `name` (the one with `.self`), which is
attached to the instance being created. The same process happens with 
`self.age = age`. Variables that are accessible through instances like this are 
called <i>attributes</i>.

* The other Two methods defined: `sit()` and `roll_over()` don't need more
information to run, so they remain only with the parameter `self`.

Instances created later will have access to these methods. In other words,
they'll be able to sit and roll over. <br>
These methods are not doing too much right now, but imagine a real situation,
where a robotic dog is actually sitting and rolling over, these methods would 
be written to actually move the dog.

### 9.1.2 Making an Instance from a Class
Think of a class as a set of instructions for how to make an instance.
The class <i>Dog</i> tells the <u>how</u> of representing a specific dog.
<br>&emsp;Let's do that in code:
```python
class Dog:
    --snip--

my_dog = Dog('Whillie', 6)

print(f"My dog's name is {my.dog.name}.")
print(f"My dog is {my_dog.age} years old.")
```
The class is the same as in the previous exampl, so, let's explain the new
three lines of code:
* We tell Python to create a dog named `'Winnie'` and whose age is `6`.
* Python calls the `__init__()` method in the class `Dog` with the arguments
  * `'Winnie'`
  * `6`
* The `__init__()` method creates an instance representing a dog with the
values provided.
* The instance is assigned to the variable we created `my_dog,`.
> Notice how the naming convention are helpful, and we can distinguish how 
> `Dog` refers to a class and `my_dog` to a particular instance.

#### 9.1.2.1 Accessing Attributes
Use the dot notation to access a value of <i>my_dog</i>'s attributes. Let's try
with `name`:
```python
my_dog.name
```
Python looks at the instance `my_dog` and finds the attribute name associated
with `my_dog`, which in the class `Dog` is the same attribute referred to as 
`self.name`. The same approach is used for `age`.
```commandline
My dog's name is Winnie.
My dog is 6 years old.
```

#### 9.1.2.2 Calling Methods
The created instance also will give as access to the methods in the class 
`Dog`. So, let's make to our pet to sit and roll over:
```python
Class Dog:
    --snip--
my_dog = Dog('Winnie', 6)
my_dog.sit()
my_dog.roll_over()
```
To call a method, put the name of the instance (<i>my_dog</i>) and the method
you want to call separated by a dot.<br>
&emsp;Pyton reads `my_dog.sit()` and runs the code in the method `sit()` in the
class `Dog`. The same happens whe Python reads `my_dog.roll_over()`.
```commandline
Winnie is now sitting.
Winnie rolled over!
```

> NOTE:<br>
> When attributes and methods are appropriately descriptive, names
> like `name`, `age`, `sit()`, and `roll_over()`, we can easily infer what a 
> block of code, even one we’ve never seen before, is supposed to do.

> NOTE:<br>
> We can infer what a block of code does, even one we've never seen before, 
> when attributes and methods are appropriately named like `name`, `age`, 
> `sit()`, and `roll_over()` 

#### 9.1.2.3 Creating Multiple Instances
You can create as many instances from a class as you need:
```python
class Dog:
    --snip--
my_dog = Dog('Winnie', 6)
your_dog = Dog('Lucky', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```
'Winnie' and 'Lucky' are separated instances (specific dogs) with thri own set
of attributes, capable of teh same actions:
```commandline
My dog's name is Winnie.
My dog is 6 years old.
Winnie is now sitting.

Your dog's name is Lucky.
Your dog is 3 years old.
Lucky is now sitting.
```
> Even if the first and second dog have tha same name and age, Python would 
> create a separate instance from the `Dog` class.<br>
> You can create as many instances as you need as long as you give them a
> unique name, or it occupies a unique spot in a list or dictionary.


---
## 9.2 Working with Classes and Instances
You can use classes to represent real-world situations. And you'll work mostly
with instances of that class.<br>
Sometimes you'll require to modify attributes of an instance. You can do it
directly or through methods to update those attributes.

### 9.2.1 The Car Class
Let's create a class that stores information about the car wi're working with,
and a method to summarize that information.
```python
# REFER: ../9.2.../9.2.1.../car.py
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe the car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2025)
print(my_new_car.get_descriptive())
```
Here we have nothing newer as the <i>Dog</i> class. But let's break it down:
* We create the class `Car`.
* Add the `__init__()` method, with the parameters `make`, `model`, and `year`.
  * The parameters are assigned to the attributes associated
  with the instance (i.e. `self.make = make`).
* Add `get_descriptive()` method. It puts the attributes in a string and 
returns that value.
* Create a new instance from the `Car` class and assigned it to `my_new_car`.
* Print the string returned into `my_new_car` variable.
```commandline
2025 Audi A4
```
Let's add an attribute that changes over time, the car's overall mileage.
``
### 9.2.2 Setting a Default Value for an Attitude
Attributes can be defined without being passed in as parameters in the 
`__init__()` method, where they are assigned a default as a value.<br>
Let's add an attribute `odometer_reading` that always starts on `0`. Also, 
let's add a method `read_odometer()`, to read each car's odometer.
```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe the car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
      """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2025)
print(my_new_car.get_descriptive())
my_new_car.read_odometer()
```
We have fwe new lines, let's check on them:
* `self.odometer_reading = 0` it's just a new attribute initialized in `0`.
* `read_odometer()` method prints what's in `self.odometer_reading`.
* the last line which calls the new method `read_odometer()`.
What it prints:
```commandline
2025 Audi A4
This car has 0 miles on it.
```
Few cars actually have 0 miles in the odometer, let's create a way to update 
the value of this attribute.

### 9.2.3 Modifying Attribute Values
There are three ways to modify an attribute's value:
1. Directly through the instance.
2. Set a value through a method.
3. Increment a value through a method.
Let's take a look to each one:

#### 9.2.3.1 Modifying an Attribute's Value Directly
Here's the easiest way, <i>directly</i>. Let's update the odometer value 
through the instance.
```python
class Car:
    --snip--

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```
Through the instance in this piece of code `my_new_car.odometer_reading = 23`,
we update the value of the attribute, `odometer_reading`. Python sets `23` to
it, and when we print it we have:
```commandline
2025 Audi A4
This car has 23 miles on it.
```
Now let's take a look how to update an attribute through a method.

#### 9.2.3.2 Modifying an Attribute's Value Through a Method
Sometimes is preferred to have a method that do this updates for you. When
you pass the new value to the method, it updates the attribute internally.<br>
&emsp;Let's create a method called `update_odometer()`:
```python
class Car:
    --snip--

    def updat_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odomoeter_reading = mileage

my_new_car = Car('audi', 'a4', 2025)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
```
The new method just updates the value of `odometer_reading`.
We use that function here, `my_new_car.update_odometer(23)`.
After that it prints:
```commandline
2025 Audi A4
This car has 23 miles on it.
```
We can extend the method `update_odometer()` so that no one tries to roll back
the odometer reading:

````python
class Car:
    --snip--
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attemps to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
````
Now `update_odometer()` checks if the new reading makes sense before modifying
the attribute. If mileage is greater or equal, you can modify the odometer's
value. If the mileage is less than the existing one, you'll get a warning that
you can't roll back an odometer.

#### 9.2.3.3 Incrementing an Attribute's Value Through a Method
Let's say we want to increment a value instead of setting a new one. Imagine we
buy a used car, and drive 100 miles on it before registering it.
Let's check a method that let us pass this incremental amount.

```python
class Car:
    --snip--

    def update_odometer(selfself, mileage):
        --snip--

    def increment_odometer(selfself, miles):
        """Ad the givenamount to the odometer reading."""
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
```
Let's break down these new things in the code:
* The method `increment_odometer()` takes the number of miles and adds this
value to the `self.odometer_reading`.
* We created a new instance and assigned it to the variable `my_used_car`.
* We set the odometer to <i>23,500</i> miles, by calling `update_odometer`.
* We call `increment_odometer()` and pass it `100` to add 100 miles.
So it prints:
```commandline
2015 Subaru Outback
This car has 23500 miles on it.
This car has 23600 miles on it.
```
You can easily modify this method to reject negative increments so no  one uses
this function to roll back an odometer.
```python
    def increment_odometer(selfself, miles):
        """Ad the givenamount to the odometer reading."""
        if miles > 0:
          self.odometer_reading += miles
        else:
          print("You can't add negative values and roll-back the odometer.")
```
> NOTE:<br>You can use methods like this to control how users of your program 
> update values such as an odometer reading, but anyone with access to the
> program can set the odometer reading to any value by accessing the attribute
> directly. Effective security takes extreme attention to detail in addition 
> to basic checks like those shown here.

---
## 9.3 Instances
### 9.3.1 The __init__() Method for a Child Class
### 9.3.2 Defining Attributes and Methods for the Child Class
### 9.3.3 Overriding Methods from the Parent Class
### 9.3.4 Instances as Attributes
### 9.3.5 Modeling Real-World Objects


---
## 9.4 Importing Classes
### 9.4.1 Importing a Single Class
### 9.4.2 Storing Multiple Classes in a Module
### 9.4.3 Importing an Entire Module
### 9.4.4 Importing All Classes from a Module
### 9.4.5 Importing a Module into a Module
### 9.4.6 Using Aliases
### 9.4.7 Finding Your Own Workflow

---
## 9.5 The Python Standard Library

---
## 9.6 Styling Classes