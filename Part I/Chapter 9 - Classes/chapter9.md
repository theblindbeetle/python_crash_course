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

print(f"My dog's name is {my_dog.name}.")
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

my_new_car = Car('audi', 'a4', 2025)
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
        Reject the change if it attempts to roll the odometer back.
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
        """Adds the given amount to the odometer reading."""
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
## 9.3 Inheritance
Classes don't always need to be written from scratch. You can have different 
versions based on another class. The original one is the <i>parent class</i>,
and the one that <i>inherits</i> is the <i>child class</i>.<br>
The child class can inherit any or all the attributes and methods from the
parent class, and it's also free to define new ones if its own.

### 9.3.1 The __init__() Method for a Child Class
When you write a child class, and call the `__init__()` method, this will
initialize the attributes and methods from the parent class, making them
available on the child class.<br>
&emsp;Let's model an electric car, which is a specific kind of car, and we
can base the new `ElectricCar` class on the `Car` class we wrote earlier. So,
we only write specific code of attributes and behaviors for the electric cars.

Let's start with a simple version of the `ElectricCar` class, which does
everything the `Car` class does:
```python
# REFER: ../9.3.../9.3.1.../electric_car.py
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe the car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Gather descriptive characteristics of a car into a string"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Ad the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2025)
print(my_tesla.get_descriptive_name())
```

First we create the parent class `Car`. The parent class should:
* be part of the current file.
* appear before the child class.

We de fine the child class `ElectricCar` where:
* The name of the parent class must be in parentheses in the definition
of the child class</i>.

The `__init__()` method takes the information required to make a 
`Car` instance.

The `super()` function is a special function that allows you to call
the methods from the parent class. <b><i>This line tells Python to call
the `__init__()` method from Car, which give an `ElectricCar` all the
attributes defined in that method.</i></b>

<h6>The name `super` comes from a convention of calling the parent class a
<i>superclass</i> and the child a <i>subclass</i>.

Then, we create an instance of the `ElectricCar` class and assign it to
`my_tesla`. 

This line calls the `__init__()` method defined in `ElectricCar`,
which in turn tells Python to call the `__init__()` method from 
the parent class `Car`. We provide the arguments `tesla`, `model s`, and `2025`

Aside from `__init__()`, there are no attributes/methods that are particular
from `ElectricCar`. For now, we are just making sure the electric car has 
the appropriate `Car` behaviors:
```commandline
2025 Tesla Model S
```

### 9.3.2 Defining Attributes and Methods for the Child Class
A child class can inherit from a parent class by adding any new attributes
and methods as necessary.<br>
&emsp;Let's add an attribute to electric cars and a method to report it.<br>
We'll add the battery size and a method that prints its description:
```python
# REFER: ../9.3.../9.3.2.../electric_car.py
class Car:
    --snip--

class ElectricCar(Car):
    """Represent aspects of a car, specficit to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describt_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2025)
print(my_tesla.get_descriptive_name())
my_tesla.describt_battery()
```
We added a new attribute, `battery_size`, and its default value, `75`.
This value will be associated with all the instances `ElectricCar`, but none of
`Car`.<br>
Also, we added a method describing the battery of size, `describe_battery()`.
```commandline
2025 Tesla Model S
This car has a 75-kWh battery.
```
> Each subclass can be specialized as required by adding all the
> attributes/methods needed.<br>
> An attribute/method that belongs to any car, should be added 
> to the `Car` class instead of `ElectricCar`. 

### 9.3.3 Overriding Methods from the Parent Class
When Python disregards methods in the parent class and attend the ones
with the same name in the child class, it's called <i>overriding</i>.
You can override methods from the parent class that doesn't alight with
the needs of the child class.<br>
&emsp;Say the class `Car` has a method called `fill_gas_tank`. This isn't useful
for an electric car, and in that class you might want to override it.
Here's one way to do that:
```python
class ElectricCar(Car):
    --snip--

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
```
When you use inheritance you can make the child classes to retain/override
whatever is needed from the parent class.

### 9.3.4 Instances as Attributes
When modeling something from the real-world in code you may find you're
adding meny attributes and methods and that your files are becoming lengthy.
Then you may want break your large class into smaller classes that work
together.<br>
&emsp;For  example, the `ElectricCar` class may grow by much adding specific
information about the battery. We can move attributes and methods to a
separated class, `Battery`, and from it create an instance as an attribute in
the `ElectricCar` class:
```python
class Car:
    --snip--

class Battery:
    """A simple attemp to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2025)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
```
Let's explain this code:
* `class Battery` - a class that does not inherit from any other class.
  * The `__init__()` method - it has one parameter, which is optional (because
it has a default value, `75`).
  * The `describe_battery()` method - prints the battery size, and now it's
also in the `Battery` class.
* `class ElectricCar` - we add a new attribute.
  * The `self.battery` attribute - Python creates an instance of `Battery ()` 
(sized `75`, because we didn't specify other value), and assigns it to
`self.battery`.
  > Putting this last point in other words; every time the `__init__()` method
  > from `ElectricCar` is called, an instance from `Battery` is created.

The way to use the attribute-instance through the `my_tesla` instance, is
through the car's battery attribute
```python
my_tesla.battery.describe_battery()
```
We go through the instance `my_tesla`, use the `battery` attribute (which is
an instance of the `Battery` class), and call the method `describe_battery().
<br>&emsp;The output is:
```commandline
2025 Tesla Model S
This car has a 75-kWh battery.
```
This helps to add attributes and methods to the battery without cluttering
the `ElectricCar` class. Let's add the method `get_range()` based on the 
battery size:
```python
class Car:
    --snip--

class Battery:
    --snip--
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        car_range = 0
        if slef.battery_size == 75:
            car_range = 260
        elif self.battery_size == 100:
            car_range = 315

        print(f"This car can go about {car_range} miles on a full charge.")

class ElectricCar(Car):
    --snip--

my_tesla = ElectricCar('tesla', 'model s', 2025)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```
The output:
```commandline
2025 Tesla Model S
This car has a 75-kWh battery.
This car can go about 260 miles on a full charge.
```

### 9.3.5 Modeling Real-World Objects
As the complexity of modeling the real-world things grows, as electric cars,
new interesting questions appear. Is the range of an electric car a property
of the battery or of the car? it depends on:
* we are manufacturing just one car; it stays on `Battery` class.
* we are manufacturing an entire line of cars; it should be moved to the
`ElectricCar` class.

If we are manufacturing different cars, the battery size and other car's
properties determine will determine each car's range. In this supposition,
if we keep the `get_range()` method in the `Battery` class, we need to pass
other attributes (the car's properties) so the range is determined in the
`Battery` class.

These kind of questions are not at a <i>syntax-level</i>, but a higher logical
level where you try to model the real world in code. At this point there are
often no right/wrong approaches to model real-world situations. Some approaches
are more efficient than others, but it takes practice to find the most
efficient representation.<br>
&emsp;Don't get discouraged if you need to rewrite your classes several times
trying different approaches. To write efficient code, everyone goes through
this process.

---
## 9.4 Importing Classes
Python let you store classes in modules and import them into your programs,
so you don't clutter your main files.

### 9.4.1 Importing a Single Class
Let's create a file `car.py` with the `Car` class as follows:
```python
# REFER: ../9.4.../9.4.1.../car.py
"""A class that can be used to represent a car."""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
  
    def read_odometer(self):
          """Print a statement showing the car's mileage."""
          print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
  
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
```
In the first docstring (the first line in the file), describes briefly
the module. You should write a docstring for each module you create.<br>
&emsp;Let's create a file called `my_car.py` that imports the class `Car`
and creates an instance from that class:
```python
# REFER: ../9.4.../9.4.1.../my_car.py
from car import Car

my_new_car = Car('audi', 'a4', 2025)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```
The import statement (at the top) tells Python to open the `car` module and
import the class `Car` to use it as it was defined in this file:
```commandline
2025 Audi A4
This car has 23 miles on it.
```
Importing classes is an effective way to program. When you move the class
to a module and import the module, you:
* still get the functionality
* keep clean and easy to read code
* store the logic in separate files
* don't touch the class file again when it works correctly.
* focus on a higher-leve logic of your main program.

### 9.4.2 Storing Multiple Classes in a Module
A module can contain as many classes as needed, just consider, they should
be related somehow. The class `Battery` and `ElectricCar` help to represent
cars, let's add the to the module `car.py`:
```python
# REFER: ../9.4.../9.4.2.../car.py
"""A set of classes used to represent gas and electric cars."""

class Car:
    --snip--

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        car_range = 0
        if self.battery_size == 75:
            car_range = 260
        elif self.battery_size == 100:
            car_range = 315
        print(f"This car can go about {car_range} miles on a full charge.")

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
```
Let's make the new file `my_electric_car.py`, import the `ElectricCar`
class, and make an electric car:

```python
# REFER: ../9.4.../9.4.2.../my_electric_car.py
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2025)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```
This is the same output saw earlier, but with the logic hidden in a module:
```commandline
2025 Tesla Model S
This car has a 75-kWh battery.
This car can go about 260 miles on a full charge.
```

### 9.4.3 Importing Multiple Classes from a Module
You can import as many classes as you needed. Let's create a <i>car</i>
and an <i>electric car</i>:
```python
# REFER: ../9.4.../9.4.3.../my_cars.py
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2025)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2025)
print(my_tesla.get_descriptive_name())
```
You can import multiple classes from a module by separating with a comma.
Once you import them, you can create instances as you need.<br>
&emsp;This example describe a couple of  2025 cars. 
The <i>Volkswagen Beetle</i> and an electric car <i>Tesla Roadster</i>:
```commandline
2025 Volkswagen Beetle
2025 Tesla Roadster
```

### 9.4.4 Importing an Entire Module
When importing an entire module, you use the <i>dot notation</i>.
This results in code easy to read, because every instance you create
from the class includes the module name. Let's try that approach:
```python
import car

my_beetle = Car('volkswagen', 'beetle', 2025)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2025)
print(my_tesla.get_descriptive_name())
```
We imported the entire `car` module. We used the dot notation syntax to
access the class through the module name as: "<i>module_name.ClassName</i>".
<br>&emsp;We use again the car
<i>Volkswagen Beetle</i> and the electric car <i>Tesla Roadster</i>:
```commandline
2025 Volkswagen Beetle
2025 Tesla Roadster
```

### 9.4.5 Importing All Classes from a Module
You can import all the classes from a module by using:
```python
from module_name import *
```
This is not recommended for two reasons:
1. It's helpful to read wha classes are used from a module by using `import`
   (`from module import Class1, Class2, ClassN`).
2. Using this approach may lead to confusion with names in the file.
If you import two classes with the same name (from different modules),
you can create errors hard to diagnose.

### 9.4.6 Importing a Module into a Module
You may want to spread out unrelated classes in different modules, but
classes sometimes have dependency on other classes from other modules.
You can into the module the class that it requires.<br>
&emsp;Let's stor the `Car` class in one module and the classes `ElectricCar`
and `Battery` in a separated module:
```python
# REFER: ../9.4.../9.4.6.../electric_car.py
"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery:
    --snip--
    
class ElectricCar(Car):
    --snip--
```
The class `ElectricCar` needs access to its parent class `Car`, which we
import into the module in the firs line of code. Also, we added a description
for this module by adding the proper docstring.
We also updated the `car` module, so it contains only the `Car` class. 
```python
# REFER: ../9.4.../9.4.6.../car.py
"""A class that can be used to represent a car."""

class Car:
    --snip--
```
Now we can import from each module separately and create whatever kind of 
car we need:

```python
# REFER: ../9.4.../9.4.6.../my_cars.py
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
```
We import each class from its module, `Car` from `car` and `ElectricCar`
from `electric_car`, Both kinds are created correctly:
```commandline
2025 Volkswagen Beetle
2025 Tesla Roadster
```

### 9.4.7 Using Aliases
As when importing functions, you can use aliases when importing class too.<br>
&emsp;Consider making a lot of electric cars. It might get tedious typing
(and reading) `ElectricCar` over and over again. You can give an alias in 
the import statement:
```python
from electric_car import ElectricCar as EC
```
Now you can use the alias whenever you want to create an electric car:
```python
my_tesla = EC('tesla', 'roadster', 2025)
```

### 9.4.8 Finding Your Own Workflow
Python gives you many options to structure code in large projects. And it's
important to understand the options so you can organize your projects and
understand other's people projects.

If you're starting out, keep it simple. Create everything in one file. Once
everything is working, separate your classes into different modules.
Find an approach that lets you write code that works, and go from there.

---
## 9.5 The Python Standard Library
The <i>Python Standard Library</i> is a set of modules included in every
Python installation. You can use any function or class in the standard library
by including an `import` statement. Let's use the module `random`, which
can help modeling real-world situations.<br>
&emsp;An interesting function from random is `randint()`. which receives
two numbers and returns a random value between those numbers (including them).
```pycon
>>> from random import randint
>>> randint(1,6)
3
```
Another useful function is `choice()`. This function takes in a list or tuple
and retunrs a randomly chosen element:
```pycon
>>> from randome import choice
>>> players = ['charles', 'martina', 'michael', 'florence', 'eli']
>>> first_up choice(players)
'florence'
```
The random module shouldn't be used when building security applications, but
for other fun and interesting projects it's good.

>NOTE:<br>
> You can also download modules from external sources. You'll see a number of
> these examples in <i>Part II</i>, where we need external modules to 
> complete each project.



---
## 9.6 Styling Classes
#### Classes, Instances, Modules
* Class names should be written in CamelCase. To do this by capitalizing the
first letter of each word in the name, and don’t use underscores.
* Instance and module names should be written in lowercase with underscores 
between words.

#### Docstrings
* Every class should have a docstring immediately following the class 
definition. 
* The docstring should be a brief description of what the class does, and
you should follow the same formatting conventions you used for writing
docstrings in functions. Each module should also have a docstring 
describing what the classes in a module can be used for.

#### Blanks
* You can use blank lines to organize code, but don’t use them excessively.
* Within a class you can use one blank line between methods, and within 
a module you can use two blank lines to separate classes.
* If you need to import a module from the standard library and a module
that you wrote, place the import statement for the standard library module
first.
* Then add a blank line and the import statement for the module you
wrote.In programs with multiple import statements, this convention makes
it easier to see where the different modules used in the program come from.