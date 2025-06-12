# Chapter 11: Testing Your Code
### When you write a function or a class, you can also write tests for that code.
Testing your code makes you confident that it will work correctly. Every
programmer must test their code often to catch problems before the user does.
You should test new code added to make sure it doesn't break the program.

What you'll learn here is:
* Test your code using Python's `unittest` module.
* Build a test case and check the inputs result in the expected output.
* What a passing test looks like.
* What a failing test looks like.
* How a failing test helps to improve your code.
* To test functions.
* To test classes.
* To start understanding how many tests to write for a project.

---
## 11.1 Testing a Function
To test something we need code. Try with this function that takes
first and last name, and returns a neatly formatted full name:
```python
# REFER: ../11.1.../name_function.py
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()
```
The function combines '*firstname* + *space* + *last name*', capitalize it
and returns the full name.<br>
&emsp;To check the `get_formatted_name()` function works, let's create the
program *names.py* that let the user enter first and last name, and see on
screen a neatly formatted full name:
```python
# REFER: ../11.1.../names.py
from name_function import get_formatted_name

divider = "-" * 25
print("Enter 'q' at any time to quit.")
while True:
    first = input(f"{divider}\nPlease give me a first name:\n\t")
    if first == 'q':
        break
    last = input("Please give me a last name:\n\t")
    if first == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
```
This program imports `get_formatted_name()` from *name_function.py*.
The user can input any amount of first and last names, and see the formatted
full names:
```commandline
Enter 'q' at any time to quit.
-------------------------
Please give me a first name:
	eleanor
Please give me a last name:
	rigbt
	Neatly formatted name: Eleanor Rigbt.
-------------------------
Please give me a first name:
	sgt.
Please give me a last name:
	pepper
	Neatly formatted name: Sgt. Pepper.
-------------------------
Please give me a first name:
	q
```
The neat formatted names are correct. But, what if we want the function
handles middle names. We want the program keeps working with a*First Last*
name structure. We can enter `Eleanor Rigby` every time we modify
`get_formatted_name()` to test the program, but there is a better way.

With Python, you can automate the testing of a function's output. However,
by automating the testing for `get_formatted_name()`, ensures the function
works with the kind of names we've written tests for, such as *First Last*
name, or *First Middle Last* name.

### 11.1.1 Unit Tests and Test Cases
The module `unittest` is a Python's standard library with the tools for
testing your code.
* A *unit test* verifies that a single aspect of a function is correct.
* A *test case* is a collection of *unit tests* proving a full range of
  situations you expect it to handle.
    * A good *test case*:
        * consider all the possible kinds of input a function could receive.
        * include tests to represent each of these situations.
* A test case with *full coverage* covers all the ways you can use a function.
* On large projects full coverage is not that common, and often is good enough
  to write tests for your code's critical behaviors. Although, you can aim
  for full coverage only if the project starts to see widespread use.

### 11.1.2 A Passing Test
The syntax for setting up a test case is a bit different, but once done,
it's easy to add more unit test for your functions.

To write a test case:
* import:
    * the module `unittest`
    * the function to test.
* create a class that inherits from `unittest.TestCase`
* write methods for testing aspects of the function's behavior.
```python
# REFER: ../11.1.../11.1.2.../test_name_function.py
import unittest
from name_function import get_formatted_name

class NamesTestCase(unit.TestCase):
    """Test for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Eleanor Rigby' work?"""
        formatted_name = get_formatted_name('eleanor', 'rigby')
        self.assertEqual(formatted_name, 'Eleanor Rigby')

if __name__ == '__main__':
    unittest.main()
```
Let's break this down:
* we import
    * the module `unittest`
    * the function to test `get_formatted_name()` from *name_function.py*
* We create the class `NamesTestCase`. <i>It will contain</i> unit tests for
  `get_formatted_name()`.
    * The class must inherit from `unittest.TestCase` so Python knows how to
    * > The class name can be any, but it's better call it something related
      > to the function you're about to test and to use the word *Test* in
      > the class name.
      run the test.
* The method `test_first_last_name()` is the only one in the class
  `NamesTestCase`. it verifies names with first and last name.
    * We assign to `formatted_name` the result of `get_formatted_name()` while
      we send the values `eleanor` and`rigby`.
    * We use an *assert* method, that verifies the result you received is the
      one you expected to receive.
    * > Any method with the prefix *test_* runs when we execute
      > *test_name_function.py*.
    * As we know `get_formatted_name()` returns a capitalized, spaced full name,
      we expect the value to be *Eleanor Rigby*. So, we use the method
      `assertEqual()` and pass it '*Eleanor Rigby*'

    * The line
      ```python
      self.assertEqual(formatted_name, 'Eleanor Rigby')
      ```
      compares the value in `formatted_name` to the string 'Eleanor Rigby'.
      If they are equal, it's ok. But if they are not, warn me.

* We can run directly this file, but note that other testing frameworks
  import the test files before running them. And the interpreter executes
  the file as it’s being imported.
* The `if` block looks at a special variable `__name__`, the one is set when
  the program is executed. If this file is run as the main program, the value
  of `__name__` is set to `__main__`.
* We call `unittest.main()`, which runs the test case. But, when another
  testing framework imports this file, the value `__name__` won't be
  `__main__` and this block will bot be executed.
  By running *test_name_function.py* the output is:
```commandline
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
Let's read and understand this output:
* The dot tell us a single test passed.
* Python ran *one* test, and it took less than 0.001s to run.
* The `OK` tells that all unit tests in the test cases passed.

This means the function `get_formatted_name()` will always work for names
with firs and last name... unless we modify the function.<br>
If we modify `get_formatted_name()`, run this test, and it passes, we
know the function still works for names  with firs and last name.

### 11.1.3 A Failing Test
Let's modify `get_formatted_name()` so it also handles middle names, but in
a way it breaks when entering names with only first and last name:
```python
# REFER: ../11.1.../11.1.3.../name_function.py
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()
```
This version works for people with middle names, but the function breaks when
we introduce people with just first and last name. So that, by running
*test_name_function.py* the output is:
```commandline
E
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase.test_first_last_name)
Do names like 'Eleanor Rigby' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_name_function.py", line 9, in test_first_last_name
    formatted_name = get_formatted_name('eleanor', 'rigby')
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```
We got the error with much information, that's because we need as much
information as we can have to debug and correct errors.
Let's break it check what it says:
* The `E` in the first line tells one *unit test* in the *test case* resulted
  in an error.
* The `test_first_last_name()` method generated an error.
    * In the parentheses, separated by a dot there are three elements
      (\_\_main\_\_.NamesTestCase.test_first_last_name)
        * \_\_main\_\_ • The assigned name for the test.
        * NamesTestCase • The name (\_\_name\_\_) of the class.
        * test_first_last_name • the name of the method.
    * In the following line, it's displayed the docstring of the function.
* Then we have a standard `Traceback` reporting:<br>
  `TypeError: get_formatted_name() missing 1 required positional argument: 
  'last'`
* We see one unit test was run.
* The overall test case failed and one error occurred.


### 11.1.4 Responding to a Failed Test
* When a test fails, assume you're checking the right conditions.
* A passing test means the function behaves correctly.
* A failing test means there's an error in the code you wrote.
* When a test fails, fix the code, don't change the test.

The function `get_formatted_name()` used to require two parameters, the
first and last name, but now it requires first, middle, and last name.<br>
This means, that the addition of the *middle name* broke the behavior of
`get_formatted_name()`. The best option is to make middle name optional, so
that, `get_formatted_name()` handles names with or without middle name.

To make middle names optional, move the parameter `middle` to the end of the
parameters list in the function definition and give it an empty default value.
we also add an if statement to build properly the full name:
```python
# REFER: ../11.1.../11.1.4.../name_function.py
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        middle += ' '
    full_name = f"{first} {middle}{last}"
    return full_name.title()
```
In this new version the middle name is optional, so that if you pass a name
without middle name:
* the full name contains first and last name.
  and with middle name:
* the full name contains first, middle, and last name.

Now the function should work for both kind of names.
By executing our test with the name *Eleanor Rigby*, the output is:
```commandline
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
The test case passes now.
The failed test helped us to identify the new code that broke existing
behavior, making easy fixing the function.

### 11.1.5 Adding New Tests
As `get_formatted_name()` works for simple names, let's add a second test
for people with middle name by adding another method to the
class `NamesTestCase`:
```python
# REFER: ../11.1.../11.1.5.../test_name_function.py
--snip--

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        --snip--

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
```
The method's name must start with `test_` so it runs automatically when
the *main* program runs. And be clear to know what behavior we are testing, 
and, if the test fails we can detect what names are affected. 

Consider it's ok to have long/descriptive method names in your 
test case classes, to make sense of the output when your tests fail.

To test the function we call `get_formatted_name()` with a first, last, and
middle name. Then an `assertEqal()` checks the full name we expect
matches the returned value:
```commandline
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
Now we know the function works for people with and without middle name.

---
## 11.2 Testing a Class
### 11.2.1 A Variety of Assert Methods
### 11.2.2 A Class to Test
### 11.2.3 Testing the AnonymousSurvey Class
### 11.2.4 The setUp() Method