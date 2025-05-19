# Chapter 9: Classes
### In OOP you create <i>classes</i> that represent real-world situations, and you create <i>objects</i> based on these classes.
Making an object from a class is called <i>instantiation</i>, and you work with
<i>instances</i> of that class.

Classes also make life easier for you and the other programmers you'll work with
as you take on increasingly complex challenges. Your programs will make sense 
to many collaborators, allowing everyone to accomplish more.


---
## 9.1 Creating and using classes
You can model almost anything using classes. Let's create the class <i>dog</i>,
that represent any dog. What we know about dogs is they have name and age, also,
the roll-over and sit. We will add that information and behavior about the dog
to our class: 
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
  * The `self` parameter is required, and must come before the other parameters.

  > In a method call, Python passes automatically `self` as an argument.
  > Every method associated with an instance automatically passes `self`, which
  > is a reference to the instance itself, and gives to the individual instance 
  > access to the attributes and methods in the class.<br><br>
  > When we make an instance of  `Dog`, Python will call the `__init__()` method
  > from the `Dog` class. We'll pass `Dog()` name and age as arguments; `self`
  > is passed automatically (we don't need to pass it). When we make an instance
  > of `Dog` we just pass `name` and `age`.

* The variables within the method has the prefix `self`.
  * Every variable prefixed `self` is available for every method in the class.
  * We'll be able to access these variables through any instance crated from the
class.
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
* The `__init__()` method creates an instance representing a dog with the values
provided.
* The instance is assigned to the variable we created `my_dog,`.
> Notice how the naming convention are helpful, and we can distinguish how `Dog`
> refers to a class and `my_dog` to a particular instance.

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
The created instance also will give as access to the methods in the class `Dog`.
So, let's make to our pet to sit and roll over:
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
> We can infer what a block of code does, even one we've never seen before, when
> attributes and methods are appropriately named like `name`, `age`, `sit()`, 
> and `roll_over()` 

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
'Winnie' and 'Lucky' are separated instances (specific dogs) with thri own set of
attributes, capable of teh same actions:
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
> You can create as many instances as you need as long as you give them a unique
> name, or it occupies a unique spot in a list or dictionary.


---
## 9.2 Working with Classes and Instances
### 9.2.1 The Car Class
### 9.2.2 Setting a Default Value for an Attitude
### 9.2.3 Modifying Attribute Values


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