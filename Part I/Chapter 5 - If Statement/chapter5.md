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

---
## 5.4 Using `if` Statements with Lists

---
## 5.5 Styling Your `if` Statements