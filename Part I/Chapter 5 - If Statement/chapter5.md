# Chapter 5: If Statements
### Python’s if statement allows you to examine the current state of a program and respond appropriately to that state.


---
## 5.1 A Simple Example
The following code loops through a list of car
names and looks for the value 'bmw'. Whenever the value is 'bmw', it’s printed
in uppercase instead of title case:
```commandline
# REFER: Chapter 5.../a_simple_example/cars.py
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```
The output:
```commandline
Audi
BMW
Subaru
Toyota
```

---
## 5.2 Conditional Tests
At the heart of every if statement is an expression that can be evaluated as
True or False and is called a conditional test.

If a conditional test evaluates to True, Python executes the code following the 
if statement. If the test evaluates to False, Python ignores the code following
the if statement.

### 5.2.1 Checking for Equality
Most conditional tests compare the value of a variable with the value of 
interest. The simplest test checks if the value of a variable is equal to the
value of interest:
```commandline
>>> car = 'bmw'
>>> car == 'bmw'
True
```
Explanation of previous code: <br>
The first is line of code, uses a single equal sign (=),
and it assigns the value (bmw) to the variable (car). You can read this as:<br>
`Set the value of car equal to 'bmw'`

The second line of code, with double equal sign (==), compares if the values 
( of variable and interest) are equal. You can read this as:<br>
`Is the value of 'car' equal to 'bmw'?`


Whether the value of interest is different:
```commandline
>>> car = 'bmw'
>>> car == 'audi'
False
```

### 5.2.2 Ignoring Case When Checking for Equality
Testing for equality is case-sensitive in python; e.g.:
```commandline
>>> car = 'Audi'
>>> car == 'audi'
False
```
If case matters this is helpful. But if it doesn't you can convert the value to lowercase:
```commandline
>>> car = 'Audi'
>>> car.lower() == 'audi'
True 
```

### 5.2.3 Checking for Inequality
You can verify when two values are not equal (!=). The exclamation point 
represents <i>not</i>, as it does in many languages.<br>
Let's check how it works:
```commandline
```commandline
# REFER: Chapter 5.../conditianl_test/toppings.py
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the ancovies!")
```
You can read the inequality as:<br>
`Is the value of 'requested_topping' not equal to 'anchovies'?`

### 5.2.4 Numerical Comparisons
It is pretty straightforward...
```commandline
>>> age = 18
>>> age == 18
True
```

You can test to see if two numbers are not equal.
```commandline
# REFER: "../5.2.4.numerical_comparisons/magic_number.py"
answer = 17

if answer != 42:
    print("That is not the correct answer. Please Try again!")
```
The conditional passes because the value of the answer (17) is not equal to 
<i>42</i>.
Once it passes the indented code is executed, in this case, prints the message:
```commandline
That is not the correct answer. Please try again!
```
Other comparisons can be used:<br>
less than `<`; less tha or equal to `<=`; greater than `>`; grreater than or equal to `>=`.

```commandline
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False
```
Each mathematical comparison can be used as part of an if statement,
which can help you detect the exact conditions of interest.

### 5.2.5 Checking Multiple Conditions
Sometimes one condition is enough to satisfy a situation, but others you need to
validate two or more to take an action. The keywords `and` and `or` can help you
in these situations.

#### 5.2.5.1 Using `and` to Check Multiple Conditions
If you are using `and` between conditions, that means that both conditions need
to be true to return true, if one is false it returns `False` 
(condition_false > 1 ~~ False).

To check whether two conditions are `True` simultaneously, use the keyword
`and`. You can check if two people's age are both over 21:
```commandline
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >=21
False
>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
```
Under the first condition it throws `False` because not both of the values are
over 21. Before executing the second condition, the value of `age_1` is updated
to `22`, then the condition is accomplished and returns `True`.<br>
In other words "<b><i>all the conditions need to be true, to return `True`.</i></b>".

To improve readability, you can use parentheses around the individual tests, 
but they are not required. If you use them looks like this:
```commandline
(age_0 >= 21) and (age_1 >= 21)
```

#### 5.2.5.2 Using `or` to Check Multiple Conditions
Using the keyword `or` between conditions means that one of the conditions needs
to be true to return `True` (conditions_true > 1 ~~ True).<br>
In other words "<b><i>all the conditions need to be false, to return `False`.</i></b>".

Let's consider two ages with only one person over 21:
```commandline
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >=21
True
>>> age_0 = 18
>>> age_0 >= 21 and age_1 >=21
False
```
When at least 1 is true, returns `Ture`. When all (two in this case) are false,
returns `False`.

### 5.2.6 Checking Whether a Value Is in a List
Sometimes it is necessary to verify if a list contains a value before taking an
action. For example, by validating if a new username already exists in a list of
current usernames before completing some user registration.<br>
To verify whether a particular value is already in a list, use the keyword `in`.

Consider the scenario where a customer of a pizzeria requests for some toppings.
And check whether toppings are in the list.
```commandline
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
Flase
```

### 5.2.7 Checking Whether a Value Is Not in a List
Sometimes it is necessary to verify whether a value is not in a list. You can
use the keyword `not` in this situation.

Consider a list of users banned for some comments in a forum. You can check
whether a user has been banned before allowing that person to submit a comment:
```commandline
# REFER: Chapter 5.../5.2.conditianl_test/toppings.py
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
```
The output:
```commandline
Marie, you can post a response if you wish.
```
The condition returns `True`, therefore, the line of code in the conditional is
executed.

### 5.2.7 Boolean Expression
A Boolean expression is just another name for a  conditional test. Boolean value
is either True or False, just like the value of a conditional expression after 
it has been evaluated.

Boolean values are often used to keep track of certain conditions, such
as whether a game is running or whether a user can edit certain content on
a website:

```commandline
game_active = True
can_edit = False
```
Boolean values provide an efficient way to track the state of a program or a
particular condition that is important in your program.

---
## 5.3 `if` Statement
Several different kinds of if statements exist, and your choice of which to
use depends on the number of conditions you need to test.

### 5.3.1 Simple `if` Statement
The simples kind of `if` statement has one test and one action:
```commandline
if conditional_test:
    do something
```
You can put any conditional test in the first line and just about any
action in the indented block following the test.
If the conditional test
evaluates to True, Python executes the code following the if statement.
If the test evaluates to False, Python ignores the code following the if
statement.
Let's verify if a person is old enough to vote:
```commandline
# REFER: Chapter 5.../5.3.if_statement/voting.py
age = 19
if age >= 18:
    print("You are old enough to vote!")
```
The output:
```commandline
You are old enough to vote!
```
Indentation plays the same role in if statements as it did in for loops.
You can have as many lines of code as you want in the block following the if 
statement; e.g.:
```commandline
age = 19
if age >= 18:
print("You are old enough to vote!")
print("Have you registered to vote yet?")
```
The conditional test passes, and both print() calls are indented, so both
lines are printed:
```commandline
You are old enough to vote!
Have you registered to vote yet?
```

### 5.3.2 `if-else` Statement
If you want to take one action when a test passes and a different action in all
other cases. Python’s if-else syntax makes this possible.

We’ll display the same message we had previously if the person is old
enough to vote, but this time we’ll add a message for anyone who is not
old enough to vote:
```commandline
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registred to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please registre to vote as soon as you turn 18!")
```
the output:
```commandline
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
```
The if-else structure works well in situations in which you want Python to
always execute one of two possible actions. In a simple if-else chain like this,
one of the two actions will always be executed.

### 5.3.3 `if-else` Statement
Often, you’ll need to test more than two possible situations, and to evaluate
these you can use Python’s if-elif-else syntax. Python executes only one
block in an if-elif-else chain. It runs each conditional test in order until
one passes. When a test passes, the code following that test is executed and
Python skips the rest of the tests.

For example, consider an amusement park that charges different rates for
different age groups:
* Admission for anyone under age 4 is free.
* Admission for anyone between the ages of 4 and 18 is \$25.
* Admission for anyone age 18 or older is \$40.

How can we use an if statement to determine a person’s admission rate?
The following code tests for the age group of a person and then prints an
admission price message:
```commandline
# REFER: ../5.3.3.../amusement_park.py
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
```
Let's brake it:
consider age is 12; 
First conditional ask if age is under 4, and it is not. So, it goes to the 
following statement not indented.
<br>Second conditional ask if age is under 18, and it is. So, it goes into the 
block of code under this conditional, which, in this case is just one line.
<br>Ignore the rest of the conditions, sin one is already accomplished and there
is no need to go to any other linked condition.
<br>The output:
```commandline
Your admission cost is $25.
```
Any age greater than 17 would cause the first two tests to fail. In these
situations, the else block would be executed and the admission price would
be $40.

Rather than printing the admission price within the if-elif-else block,
it would be more concise to set just the price inside the if-elif-else chain
and then have a simple print() call that runs after the chain has been
evaluated:
```commandline
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.)
```

### 5.3.4 Using Multiple `elif` Blocks
It's the same principle, while more conditions is needed to link to the main if
the most `elif` you aggregate to the conditional blocks.
```commandline
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.)
```

### 5.3.5 Omitting the `else` block
Python does not require an else block at the end of an if-elif chain.
Just adapt to it, sometimes is better an `else` block, others an `elif`.
```commandline
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >=65:
    price = 20
    
print(f"Your admission cost is ${price}.)
```
The else block is a catchall statement. It matches any condition that
wasn’t matched by a specific if or elif test, and that can sometimes include
invalid or even malicious data. If you have a specific final condition you are
testing for, consider using a final elif block and omit the else block. 

### 5.3.6 Testing Multiple Conditions

The `if-elif-else` chain is appropriate to use for one test to pass. As soon as
Python finds one test that passes, it skips the rest of the tests.
Let's reconsider the pizzeria example. If someone requests for two-topping pizza,
you'll need to be sure to include both topping on their pizza:
```commandline
# REFER: ../5.3.6.../toppings.py
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra chees' in requested_toppings:
    print("Adding extra cheese")
    
    print("\nFinished making your pizza!")
```
All of these conditionals are separated tests, so if it goes into one, it also
executes the following condition. Such as the result is:
```commandline
Adding mushrooms.
Adding extra cheese

Finished making your pizza!
```

if we use the `if-elif-else` structure, that's just one condition, so, when it 
passes, it skips the rest of the steps in the chain:
```commandline
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    
print("\nFinished making your pizza!")
```
The output is:
```commandline
Adding mushrooms.

Finished making your pizza!
```




---
## 5.4 Using `if` Statements with Lists

---
## 5.5 Styling Your `if` Statements