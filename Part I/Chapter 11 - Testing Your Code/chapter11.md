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
It's useful validating a class works correctly. And a pass test for a class
makes you confident that an improvement won't break the current behavior.

### 11.2.1 A Variety of Assert Methods
Python provides assert methods in the `unittest.TestCase` class. Assert
methods test if a condition is indeed true. If so, no error exist. If not,
Python raises an exception.

The following table describe six common assert methods that inherits from 
`unittest.TestCase`:

| Method                  | Use                             |
|-------------------------|---------------------------------|
| assertEqual(a, b)       | Verify that a == b              |
| assertNotEqual(a, b)    | Verify that a != b              |
| assertTrue(x)           | Verify that x is True           |
| assertFalse(x)          | Verify that x is False          |
| assertIn(item, list)    | Verify that item is in list     |
| assertNotIn(item, list) | Verify that item is not in list |



### 11.2.2 A Class to Test
Testing a class is similar to testing a function. Much of your work
involves testing the behavior of the methods in the class. Let's write a class
that administer anonymous surveys:
```python
# REFER: ../11.2.../11.2.2.../survey.py
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
```
Let's see what this code does:
* The `__init__()` method prepares two elements:
    * the variable `question` to store the question of the survey.
    * the list `responses[]` to store the responses.
* The method `show_question()` prints the question.
* The method `store_response()` stores the response in the list.
* The method `show_results()` that print the responses.

Provide a `question` to create an instance of this class. When the 
instance for a survey is created you can use any of the methods.<br>
&emsp;To see the class `AnonymousSurvey` working let's create a program
that uses it:
```python
# REFER: ../11.2.../11.2.2.../language_survey.py
from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
```
The program do the following actions:
* Creates a question for the survey.
* Calls the class `AnonymousSurvey()` to create the object 
`my_survey`.
* Uses the object to call the methods from the class:
  * `show_question()` shows the question of the survey. 
    * and prints a message to quit the program
  * Enters to a `while` loop
  * prompts the user for a language
  * validates if response is 'q' to quit
    * if it is breaks the loop.
  * if the look continues, store the response
* prints a gratitude message for participate in the survey
* print the results:
```commandline
What language did you first learn to speak?
Enter 'q' at any time to quit.

Language: English
Language: Spanish
Language: English
Language: Mandarin
Language: q

Thank you to everyone who participated in the survey!
Survey results:
- English
- Spanish
- English
- Mandarin
```
The class works. But... what if we want to make some changes like:
* Allow a user to enter more than one response.
* write a method to list unique responses and report how many times
the that response was given (i.e. '3 English', '2 Spanish', '5 Mandarin')
* Add another class to manage non-anonymous surveys.

Implementing any of these could affect the behavior of the class
AnonymousSurvey. By allowing a user to enter multiple responses, we may change
the single response behavior. To ensure its behavior remains, we can write
tests for the class.

### 11.2.3 Testing the AnonymousSurvey Class
We'll write a test to verify a single response is stored properly by using
the `asserIn()` method. This let us know if the response is in the list
after it's been stored.
```python
# REFER: ../11.2.../11.2.3.../test_survey.py
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey."""
    
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

if __name__ == '__main__':
    unittest.main()
```

Let's check this code:
* we import `unittest` module and the class `AnonymousSurevey`
* We call our test case `TestAnonymousSurvey` that inherits 
from `unittest.TestCase`.
* The method `test_store_single_response` verifies a response to the survey
is correctly stored in the survey's list of responses. 
  * > NOTE:<br>As the method's name is descriptive, if it fails we'll know
  from the method's name shown in the output that there's a problem
  storing a single response to the survey's responses list.
  * the `question` variable is created with the question of the survey.
  * The method creates an instance of the class `my_survey` with `question`.
  * The method stores a single response `'English'`.
  * Then, verifies `'English'` is in the survey's list. 

When we run *test_survey.py*, the test passes:
```commandline
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
This is good, but a survey is only useful if it generates more than one 
response. Let's add another method to `TestAnonymousSurvey`:
```python
# REFER: ../11.2.../11.2.3.../test_survey_2.py
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey."""
    
    def test_store_single_response(self):
        --snip--
    
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)
        
if __name__ == '__main__':
    unittest.main()
```
Let's check this code:
* The name of the new method is clear and specific
`test_store_three_responses`. This method has:
  * the `question` variable.
  * the `my_survey` object with the `question` variable
  * a `responses` list with three elements
  * a loop to store th responses
  * a loop to asert all the responses are properly stored in the 
survey's list.

When we run *test_survey.py*, the tests pass:
```commandline
$ python test_survey.py 
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
This works great. But these tests are repetitive. Now, we'll use
another feature of `unittest` to make them more efficient.

### 11.2.4 The setUp() Method
In *test_survey.py*, each test method has an instance  the 
`AnonymousSurvey` class. Also, new responses in each method.<br>
The `unittest.TestCase` class has a `setUp()` method that allows you to
create these objects once then use them in each of your test methods.

When you include a `setUp()` method in a *TestCase* class, python runs that
method before running each method starting with *test_*. Any objects
created in the `setUp()` method are available in each test method.
Let's use `setUp()` to create a survey instance and used it in
`test_store_single_response()` and `test_store_three_responses()`

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """
        Create a survey and set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored proprely."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
```
Let's check our code:
* the `setUp()` method:
  * creates the `question` variable.
  * creates a survey instance
  * creates the list of responses
  * > notice how the variables `my_survey` and `responses` are prefixed by
    > `self` so they can be used anywhere in the class.<br>
    > This simplifies the test methods because they can use the self
    > variables, instead creating them on each method.
* the `test_store_single_response()` method verifies the first response in 
`self.responses` can be stored correctly
* the `test_store_three_responses()` method verifies all three responses in 
`self.responses` can be stored correctly

The execution of *test_survey.py* throw a pass for both tests.<br>
After modifying `AnonymousSurvey` to accept multiple responses for 
each person, these tests would be useful to verify that single responses
or series of individual responses are not affected.

* The `setUp()` method can make your test methods easier to write.
* The instances and attributes from the `setUp()` method can be used
in all the test methods.
* This is easier than making a new set of instances and attributes in each
test method.

> NOTE:<br>
> When you run a test case, in the first line of output, Python prints 
> different characters for test a test completed under different situations:
> * dot (.) - a test pass
> * *E* - an error in the test
> * *F* - a test that results in a failed assertion.
> 
> If the execution of the test is taking a while, you can take a look at the
> output and get sense of how many tests are passing.