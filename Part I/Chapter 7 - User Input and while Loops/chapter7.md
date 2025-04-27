
# Chapter 7: User Input and while Loops
### In this chapter you’ll learn how to accept user input so your program can then work with it. When your program needs a name, you’ll be able to prompt the user for a name. When your program needs a list of names, you’ll be able to prompt the user for a series of names. To do this, you’ll use the input() function.
### You’ll use Python’s while loop to keep programs running as long as certain conditions remain true.

---
## 7.1 How the `input()` Function Works
The input() function pauses your program and waits for the user to enter
some text. Once Python receives the user’s input, it assigns that input to a
variable to make it convenient for you to work with.

Here's a simple example that receives the message from the user, and display it
back to the user.
```python
# REFER: ../7.1.../parrot.py
message = input("Tell me something, and I will repeat it back to you:")
print(message)
```
Let's break it down step by step:
1. The `input()` function takes the <i>prompt</i>, which is the message 
displayed,that message is instructions for the user, so they know what to do. 
2. When Python runs the first line, the user sees the prompt. 
3. The program waits for the user to respond.
4. The user inputs the response, and then needs to press <b>ENTER</b>.

The output:
```commandline
Tell me something, and I will repeat it back to you: Hello everyone!
Hello everyone!
```
> Sublime Text and many other editors don’t run programs that prompt the user
> for input. You can use these editors to write programs that prompt for input,
> but you’ll need to run these programs from a terminal. See “Running Python
> Programs from a Terminal” on page 12.

### 7.1.1 Writing Clear Prompts
A prompt must be clear, and easy-to-follow that request for the exact 
information needed. Telling the user what to enter should work. For example:
```python
# REFER: ../7.1.1.../greeter.py
name = input("Please, enter your name: ")
print(f"\n\tHello, {name}!")
```
Ad a space at the end of the prompt (after the colon) makes clearer the
interaction between prompt and the user's input. 
The output:
```commandline
Please, enter your name: Maximus

	Hello, Maximus!
```

Sometimes you'll need more than one line to explain the user something, as why
you ask for that information. <br>
<b><i>What can you do?</i></b> put the prompt into a variable and then pass the
variable into the `input()` function.
```python
# REFER: ../7.1.1.../greeter_2.py
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\n\tHello, {name}!")
```
The prompt now spans two lines.
> Don't forget the space after the last character in this case a question mark.
```commandline
If you tell us who you are, we can personalize the message you see.
What is your first name? Maximus

	Hello, Maximus!
```

### 7.1.2 Using `int()` to Accept Numerica Input
When you use the `input` function, Python interprets everything the user enters
as a string. Consider the following interpreter session, which asks for the 
users age.
```commandline
>>> age = input("How old are you? ")
How old are you? 21
>>> age
'21'
```
The user enters a number, 21, but when asking Python for the value it returns
'21' which is a string. We know it's a string because it is enclosed in quotes.
If you just want to print the input, it works well. But if you try using it as
a number, you'll get an error:
```commandline
>>> age = input("How old are you? ")
How old are you> 21
>>> age >= 18
Traceback (most reent call last):
  File "<stdin>", line 1, in <module>
 TypeError: unorderable types: str() >= int() 
```
The error occurs because the program tries to compare an integer and a string.
The string `'21'` can't be compared with a numerical value `18`.

To resolve this, you only need to say Python, to treat the variable `age` as an
integer with the function `int()`:
```commandline
>>> age = input("How old are you? ")
How old are you? 21
>>> age = int(age)
>>> age >= 18
True
```

How to use the `int()` function in an actual program? Consider that a program
determines if people is tall enough to ride a roller coaster:
```python
# REFER: ../7.1.2.../roaller_coaster.py
height = input("how tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```
The program compares correctly because `height = int(height)` converts the input
from a string to an integer. The output
```commandline
how tall are you, in inches? 50

You're tall enough to ride!
```

### 7.1.3 The Modulo Operator
A useful tool for working with numerical information is the modulo operator (%),
which divides one number by another number and returns the remainder:
```commandline
>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
```
The modulo operator doesn’t tell you how many times one number fits
into another; it just tells you what the remainder is.

When one number is divisible by another number, the remainder is 0,
so the modulo operator always returns 0. You can use this fact to determine
if a number is even or odd:
```python
# REFER: ../7.1.3.../even_or_odd.py
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
```
Even numbers are always divisible by two, so if the modulo of a number
and two is zero (here, if number % 2 == 0) the number is even. Otherwise,
it’s odd. Here's the output:
```commandline
Enter a number, and I'll tell you if it's even or odd: 42
The number 42 is even.
```
---
## 7.2 Introducing `while` Loops

### 7.2.1 The `while` Loop in Action
### 7.2.2 Letting the User Choose When to Quit
### 7.2.3 Using a Flag
### 7.2.4 Using `break` to Exit a Loop
### 7.2.5 Using `continue` in a Loop
### 7.2.6 Avoiding Infinite Loops

---
## 7.3 Using a while Loop with Lists and Dictionaries

### 7.3.1 Moving Items from One List to Another
### 7.3.2 Removing All Instances of Specific Values from a List
### 7.3.3 Filling a Dictionary with User Input

