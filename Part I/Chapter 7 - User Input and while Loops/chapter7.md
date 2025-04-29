
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
The for loop takes a collection of items and executes a block of code once
for each item in the collection. In contrast, the while loop runs as long as,
or <i>while</i>, a certain condition is true.

### 7.2.1 The `while` Loop in Action
You can use a while loop to count up through a series of numbers. For
example, the following while loop counts from 1 to 5:
```python
# REFER: ../7.2.1.../counting.py
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```
In the first line, we start counting from 1 by assigning `current_number`
the value `1`. The while loop will run if the condition is true:
<br>`while current_number <=5`.<br>
The code inside the loop prints the value of `current_number` and then adds 1 
to that value with:<br>`current_number += 1`.<br>
```commandline
1
2
3
4
5
```
every time the while loop finishes, Python asks if condition is true, something
like this:

| current_number | current_number <=5 | validation | print | current_number += 1  |
|:--------------:|:------------------:|:----------:|:-----:|:--------------------:|
|       1        |       1 <= 5       |    True    |   1   |  current_value = 2   |
|       2        |       2 <= 5       |    True    |   2   |  current_value = 3   |
|       3        |       3 <= 5       |    True    |   3   |  current_value = 4   |
|       4        |       4 <= 5       |    True    |   4   |  current_value = 5   |
|       5        |       5 <= 5       |    True    |   5   |  current_value = 6   |
|       6        |       6 <= 5       |   False    |   -   |          -           |
Since the condition is not true for the last `current_value` the loop breaks. If
there are more lines after the while loop, it will execute following lines, it
is not the case for this situation, so, the program finishes its execution.

The programs you use every day most likely contain while loops. For
example, a game needs a while loop to keep running as long as you want
to keep playing, and so it can stop running as soon as you ask it to quit.
Programs wouldn’t be fun to use if they stopped running before we told
them to or kept running even after we wanted to quit, so while loops are
quite useful.
> NOTE:
> The `+=` operator is shorthand for `current_number = current_number + 1`.

### 7.2.2 Letting the User Choose When to Quit
We can make the parrot.py program run as long as the user wants by putting
most of the program inside a while loop. We’ll define a quit value and then
keep the program running as long as the user has not entered the quit value:

```python
# REFER: ../7.2.../7.2.2.../parrot.py
prompt = "\mTell me something, and I will  repeat it back to you:"
prompt += "\nEnter `quit` to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
```
The first time through the loop, message is just an empty string, so Python
enters the loop. At message = input(prompt), Python displays the prompt
and waits for the user to enter their input. Whatever they enter is assigned
to message and printed; then, Python reevaluates the condition in the while
statement. As long as the user has not entered the word 'quit', the prompt
is displayed again and Python waits for more input. When the user finally
enters 'quit', Python stops executing the while loop and the program ends:
```commandline
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
quit
```
This program prints 'quit', as if it were an actual message, a simple way to fix
it is:
```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```
and the output is:
```commandline
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
```


### 7.2.3 Using a Flag
In the previous example, we had the program perform certain tasks while
a given condition was true. But what about more complicated programs in
which many different events could cause the program to stop running?

For example, in a game, several different events can end the game.
When the player runs out of ships, their time runs out, or the cities they
were supposed to protect are all destroyed, the game should end. It needs
to end if any one of these events happens. If many possible events might
occur to stop the program, trying to test all these conditions in one while
statement becomes complicated and difficult.

For a program that should run only as long as many conditions are true,
you can define one variable that determines whether or not the entire program
is active. This variable, called a flag, acts as a signal to the program. We can
write our programs so they run while the flag is set to True and stop running
when any of several events sets the value of the flag to False. As a result,
our overall while statement needs to check only one condition: whether or
not the flag is currently True. Then, all our other tests (to see if an event has
occurred that should set the flag to False) can be neatly organized in the rest
of the program.

Let’s add a flag to parrot.py from the previous section. This flag, which
we’ll call active (though you can call it anything), will monitor whether or
not the program should continue running
```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```

### 7.2.4 Using `break` to Exit a Loop
To exit a while loop immediately without running any remaining code in the
loop, regardless of the results of any conditional test, use the `break`
statement.

The break statement directs the flow of your program; you can use it to control which lines of code are executed and which aren’t, so the program only
executes code that you want it to, when you want it to

For example, consider a program that asks the user about places they’ve
visited. We can stop the while loop in this program by calling break as soon
as the user enters the 'quit' value:
```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
```
A loop that starts with `while True` will run forever, unless it reaches a
break statement. The loop in this program continues asking the user to enter
the names of cities they’ve been to until they enter 'quit'. When they enter
'quit', the break statement runs, causing Python to exit the loop:
```commandline
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) Bogota
I'd love to go to Bogota!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) Bariloche
I'd love to go to Bariloche!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) Brasilia
I'd love to go to Brasilia!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) quit
```
> You can use the break statement in any of Python’s loops. For example, you
> could use > break to quit a for loop that’s working through a list or a 
> dictionary.



### 7.2.5 Using `continue` in a Loop
Rather than breaking out of a loop entirely without executing the rest of its
code, you can use the continue statement to return to the beginning of the
loop based on the result of a conditional test. For example, consider a loop
that counts from 1 to 10 but prints only the odd numbers in that range:
```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```
First we set current_number to 0. Because it’s less than 10, Python enters the
while loop. Once inside the loop, we increment the count by 1, so current_number
is `1`. The if statement then checks the modulo of current_number and 2. If the
modulo is 0 (which means current_number is divisible by 2), the continue
statement tells Python to ignore the rest of the loop and return to the
beginning. If the current number is not divisible by 2, the rest of the loop is
executed and Python prints the current number:
```commandline
1
3
5
7
9
```

### 7.2.6 Avoiding Infinite Loops
Every while loop needs a way to stop running so it won’t continue to run 
forever. For example, this counting loop should count from 1 to 5:
```python
# REFER: ../7.2.../7.2.6.../counting.py
x = 1
while x <= 5:
    print(x)
    x += 1
```
But if you accidentally omit the line x += 1 (as shown next), the loop
will run forever:
```python
# This loop runs forever!
x = 1
while x <= 5:
    print(x)
```
The value of `x` never chane. So, the condition is always true `x <= 5`.
The output:
```commandline
1
1
1
1
--snip--
```
To avoid writing infinite loops, test every `while` loop and make sure the loop
stops when it is expected.


---
## 7.3 Using a while Loop with Lists and Dictionaries


### 7.3.1 Moving Items from One List to Another
### 7.3.2 Removing All Instances of Specific Values from a List
### 7.3.3 Filling a Dictionary with User Input

