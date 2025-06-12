# Chapter 10: Files and Exceptions
### In this chapter you'll learn to work with files and special objects Python creates to manage errors.

Learning to work with files and save data make your programs easier for people
to use.
Handling exceptions helps to deal with situations in which files don't exist
and deal with problems that can make your program to crash, making your
program more robust to handle bad-data, whether it comes from innocent
mistakes to malicious attempts to break your programs. With the skills
you'll learn in this chapter, your programs will be more applicable,
usable, and stable.

---
## 10.1 Reading from a File
Reading from a file is useful in data analysis applications, but it's also
applicable to any situation in which you want to analyze or modify
information stored in a file.

You can read the entire content of a file, or one line at a time.

### 10.1.1 Reading an Entire File
Let's create a file with pi with 30 decimal places, 10 decimals per line:
```text
# REFER: ../10.1.../10.1.1.../py_digits.txt
3.1415926535
8979323846
2643383279
```
Here's a program that opens the file, reads and prints its content:
```python
# REFER: ../10.1.../10.1.1.../file_reader.py
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
```
There's a lot to explain in this program, so, let's break it down into small
pieces:
* The `open()` function: gives access to the content of a file, it needs one
  argument, the name of the file to open.
* File to open: Python looks for the file <i>pi_digits.txt</i>  in the same
  directory where <i>file_reader.py</i> is stored.
* `open('pi_digits.txt')`: the open() functions returns an object representing
  the file <i>pi_digits.txt</i>.
* `file_object`: Python assigns the object to it.
* The keyword `with` closes the file once access to it is no longer needed.
> NOTE: <b>Python closes the file automatically</b>.<br>
> Notice how we call `open()` and never `close()`, which is used to close
> the opened file. But if a bug prevents the method from being executed, the
> program may never close. Incorrectly closing a file may cause data lost or
> file corruption.<br>If you close the file early, you may try to work with
> an inaccessible file, leading to errors. So, let Python do that for you, it
> will figure it out by itself when the `with` block finishes execution.
* The `read()` method reads the entire content from the `file_object`
  representing the <i>py_digits.txt</i>.
* `contents` (a variable) stores what was read in the file.
* Finally, we print that content:

```commandline
3.1415926535
8979323846
2643383279

```
There is a small difference between the file and the output at the end, where
the `read()` method returns an extra blank when reaches the end of the file.
That one can be removed with `rstrip()` in the print call:
```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
```
The method removes whitespaces from the right side of a string. Now, the output
matches the original file:
```commandline
3.1415926535
8979323846
2643383279
```

### 10.1.2 File Paths
When you pass just the name of the file to the `open()` method, you're saying
Python, the file is in the directory of the current execution. Sometimes
the file you need to open is not in the same directory as the
execution file (depending on the organization of your project).<br>
&emsp; Consider the following structure:
```text
python_work
├── text_files
│   └── filename.txt
└── program.py
```
Despite the program file is in <i>python_work</i> such as the folder
<i>text_files</i>, if you just pass to the program the name of
<i>text_content.txt</i>, Python won't look up further than <i>python_work</i>.
To go further than the current execution folder you need to specify a
<i>file path</i>, so Python looks in that location.
In this example <i>text_files</i> is inside <i>python_work</i>, you could use
a relative file path to open a file from <i>text_files</i>. A relative file
path tells Python to look  for a given location relative to the directory
where the currently running program file is stored. For example:
```python
with open('text_files/filename.txt') as file_object:
```
With this relative file path, Python assumes that <i>text_files</i> is inside
<i>python_work</i>, and <i>filename.txt</i> inside <i>text_files</i>.

> NOTE:<br>
> Windows OS use a backslash (\) when displaying file paths, but you can still
> use forward slashes in your code.

You can tell Python the <i>absolute file path</i>, which is where in the
computer the file is stored.<br>
&emsp;Suppose the folder <i>text_files</i> is not in <i>python_work</i>,
let's say that folder is <i>other_files</i>, then passing to the `open()`
method `'text_files/filename.txt'` won't work because Python looks for that
location inside the <i>python_work</i> folder.<br>
&emsp;Since absolute paths are commonly longer than relative ones, it helps
assign the to a variable and then pass it to the `open()` method:
```python
file_path = '/home/absolut/paht/other_files/text_files/filename.txt'
with open(file_path) as file_object:
    --snip--
```
> NOTE: backslashes<br>
> By using backslashes you get an error, because backslashes are used to
> escape characters in strings. So that in the path `'C:\paht\to\file.txt'`,
> the sequence `\t` is interpreted as a tab. If you need backslashes, you
> can escape each one in the path, like this `'C:\\paht\\to\\file.txt'`

### 10.1.3 Reading Line by Line
Reading line by line is helpful when you need to modify a line, look for
some specific information in a file, or extract some required data.<br>
&emsp;You can use a for loop on the file object to examine each line from
a file one at a time:
```python
# REFER: ../10.1.../10.1.3.../file_reader.py
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
```
Let's break this down:
* The variable `filename` gets the name of the file, just that as a plain
  string, not the value of the file or its content, just a string where you
  could assign whatever value, like replacing:
    * `filename = 'pi_digits.txt'`<br>
      by
    * `filename = 'name_of_a_file_that_does_not_exist.txt`<br>
      and this line it's ok because it's just assigning a string to the variable
      `filename`, which means it will be executed without a problem.

&emsp;&emsp;Assigning file names to variables is a common convention
when working with files.

* Then, we use the `with` syntax and call the `open()` method, to which we pass
  the variable `filename` (if we pass a file that doesn't exist this step will
  fail) and assign the object to the variable `file_object`.


* Finally, we go line by line through the file by looping over the
  file object and printing each line:

```commandline
3.1415926535

8979323846

2643383279
```
As you can see there are blanks between each line. It's because at the end of
each line there is an invisible newline character at the end of each line:
one from the file and one from the `print()`. Using `rstript()` in the
`print()` eliminates the extra blank:
```python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
```
The output will match the content of the file
```commandline
3.1415926535
8979323846
2643383279
```

### 10.1.4 Making a List of Lines from a File
The block of `with` gives you access to the file object returned by
the `open()` method just inside of that block.
To remain access to the file's content, store the file's lines in a list.
That assignation must happen inside the block so you can use it outside the
block.<br>
You can process some parts immediately and process some others later
in the program.<br>

Let's store the lines in a list inside the block and print them outside
the block:
```python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
```
The `readlines()` method reads each line and store it in a list.
Then we use a simple loop to print each item in the list, which corresponds
to each line in the file. The output matches the exact content of the file.

### 10.1.5 Working with a File's Contents
Once you read a file into memory, you can do whatever you want with that data.
Let's build a single string containing all the digits in the file with no
whitespace in it:
```python
# REFER: ../10.1.../10.1.5.../pi_string.py
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
```
What we did here is:
* `filename` gets the name of the file.
* `with open()...` opens the file and assigns the object to `file_object`.
* `file_object.readlines()` assigns the content of the file to `lines.
* we declared `pi_string` as an empty string.
* the loop adds each line, and removing the newline character to the string.
  with no spaces.
    * if you print the list `lines` you can see the newline:
      `['3.1415926535\n', '8979323846\n', '2643383279']`
* we print the string `pi_string`.
* we print the length of the string `pi_string`.

The output is:
```commandline
3.1415926535  8979323846  2643383279
36
```
The whitespaces on the left of the second and third line remains. Let's try
replacing `rstrip()` by `strip()` to strip leading and trailing (left/right)
whitespaces of a string, instead of just the once at the right.
```python
--snip--
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
```
The <i>pi</i> with 30 decimal places has 32 characters because it includes
the leading `3` and the decimal point:
```commandline
3.141592653589793238462643383279
32
```
> NOTE: reading numbers<br>
> When Python reads a number from a file it interprets that as a string.
> You have to convert it to integer using the `int()` function or
> float using the `float()` function, to use it in a numerical context.

### 10.1.6 Large Files: One Million Digits
Our program should work as well with 1 million as it does with 30 decimal
places to create a string containing all these digits.
we don't need to change our program at all, just pass it a different file.
We'll just print 50 decimal places, so we don't need to watch a all the
million digits scrolling by in the terminal:
```python
# REFER: ../10.1.../10.1.6.../pi_string.py
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
```
The output show us how we have 1 million decimals in a string:
```commandline
3.14159265358979323846264338327950288419716939937510...
1000002
```

### 10.1.7 Is Your Birthday Contained in Pi?
Let's figure out if someone's birthday appears in the first million digits of
<i>pi</i>:
```python
--snip--
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
```
For someone who's born the 28th of June in 1962
```commandline
Enter your birthday, in the form mmddyy: 062862
Your birthday appears in the first million digits of pi!
```
Once you read from a file, you can analyze its content any way you can imagine.

---
## 10.2 Writing to a File
There are several reasons why you'd like to write into a file, like:
* It is one of the simplest ways to save data.
* When the terminal is closed the data is still available.
* You can examine the output after the program finishes.
* You can share the output with others.

### 10.2.1 Writing to an Empty File
To write text to a file, you need to call `open()` with a second argument.<br>
The second argument is to say Python the action to perform is <i>writing</i>.
```python
# REFER: ../10.2.../10.2.1.../write_message.py
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
```
Let's check what's different from reading:
* The `open()` method now has two arguments separated by a comma:
    * filename, which tells Python what file to write to
    * and the `'w'`, so Python opens the file in <i>write mote</i>

  The modes you can open a file with Python are:
    * 'r' - read mode
    * 'w' - write mode
    * 'a' - append mode
    * 'r+' - read and write

  By omitting the mode argument, Python uses <i>read-only mode</i> by default.
  <b><i>The `open()` function in write mode</i></b><br>
    * creates the file if it doesn't already exist.
    * if the file exist, erase the content before returning the file object.

* The `write()` method writes a string to the file. This program has no
  terminal output, but if you open the file <i>programming.txt</i> you can see:
```markdown
# REFER: ../10.2.../10.2.1.../programming.txt
I love programming.
```
This file is like any other txt file. You can open it, write new text in it,
copy from it, or paste ot it, etc.

> NOTE: Python only write strings to a text file. to store numerical data,
> convert it to string format by using the `str()` function.

### 10.2.2 Writing Multiple Lines
The write() function doesn't add any newlines to the text you write.
To add newlines without including the newline characters the argument `'w'`
is not be the solution:
```python
# REFER: ../10.2.../10.2.2.../write_message.py
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
```
When you execute this you'll find in the file <i>programming.txt</i> that
the lines are together:
```text
I love programming.I love creating new games.
```
Now, by including newlines (`\n`) in the call of the `write()` method:
```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
```
then you get:
```text
I love programming.
I love creating new games.

```
You can use all the resources you can use in the terminal-based output, as:
* spaces
* tab characters
* blank lines
  This, in order to have the desired output format.

### 10.2.3 Appending to a File
To append text instead overwriting the existing content (with the `'w'` mode),
you can use the <i>append-mode</i>.
Let's modify <i>write_message.py</i> and add more reasons for
love programming:
```python
# REFER: ../10.2.../10.2.3.../write_message.py
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
```
Now we are using the `'a'` argument for appending rather than writing over
the existing file. Therefore, when you open the file <i>programming.py</i>,
you'll find the previous lines plus the new ones:
```text
I love programming.
I love creating new games.
I also love finding meaning in large datasets.
I love creating apps that can run in a browser.
```

---
## 10.3 Exceptions
If you create code that handles an execution makes Python unsure
what to do next

* it's thrown an object called <i>exception</i> and the program can
  continue running.<br>

if you don't

* the program halt and show a <i>traceback</i>.

You can handle exceptions with `try-except` blocks, that tells Python
what to do when an exception raises. This ensures that the program continue
running even when something goes wrong, and instead of a traceback, you
can write a friendly message that a user can understand.

### 10.3.1 Handling the ZeroDivisionError Exception
Dividing a number by zero is an impossible operation, and it generates
an error in Python, let's see what happens

```python
# REFER: ../10.3.../10.3.1.../division_calculator.py
print(5/0)
```
This error generates the traceback:
```commandline
Traceback (most recent call last):
  File "division_calculator.py", line 1, in <module>
    print(5/0)
          ~^~
ZeroDivisionError: division by zero
```
The error reported in the traceback is the exception object
<i>ZeroDivisionError</i>.<br>
When this happens Python stops the program and tell the kind of exception that
was raised. We can use this information to understand how to address the
situation and be prepared if it happens again.

### 10.3.2 Using try-except Blocks
A <i>try-except</i> block is used when an error can occur so you can handle
the exception.<br>
&emsp;Let's use a <i>try-except</i> block for handling the zero division:
```python
# REFER: ../10.3.../10.3.2.../division_calculator.py
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```
As you can see there are two sections:
* `try:` which is the operation we want to perform.
* `except ZeroDivisionError:` as you can see, the keyword <i>except</i> goes
  with a second part, which is the error we are anticipating that may occur.
  Which in this case is a division by zero, so we use `ZeroDivisionError`.

The output we have is
```commandline
You can't divide by zero!
```
If there were code after the <i>try-except</i> block, because of the
<i>try-except</i> block, the program would continue running.

> NOTE:<br>
> * If the `try` block works, the `except` block is not executed.<br>
> * If the `try` block fails, the `except` block is executed.

### 10.3.3 Using Exceptions to Prevent Crashes
Handling error is especially important when the program has more work after
the error occurs, which is very common after user inputs.<br>
&emsp;A program that responds appropriately to invalid inputs can prompt
for more inputs instead of crashing.
&emsp;Let's create a calculator that does only divisions:
```python
# REFER: ../10.3.../10.3.3.../division_calculator.py
print("Give me two numbers, and I'll diveide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
```
Let's see what's this program does:
* It asks the user to input two numbers or a 'q' to quit the program.
* in the loop:
    * ask for the first number.
    * if it is a 'q' exits the program, if not.
    * ask for the second number.
    * if it is a 'q' exits the program, if not.
    * does the division and stores the result in the variable `answer`.
    * prints whatever is stored in `answer`.

Notice there's no handling exception, if the user introduce a zero division,
the program crashes.

```commandline
Give me two numbers, and I'll diveide them.
Enter 'q' to quit.

First number: 5

Second number: 0
Traceback (most recent call last):
  File "division_calculator.py", line 11, in <module>
    answer = int(first_number) / int(second_number)
             ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
ZeroDivisionError: division by zero
```
It's bad a program crashing, such as bad as letting the user see tracebacks.
Nontechnical users will be confused, and in a malicious settings, attackers
will learn more than you want them to know from the traceback.

### 10.3.4 The else Block
We can make the program work more appropriately to invalid inputs by
wrapping the vulnerable line to produce errors in a
<i>try-except</i> block.<br>
&emsp;The error occurs in the line that performs the division.
Here we also include the <i>else</i> block. Any code depending on the
<i>try</i> block goes in the <i>else</i> block:
```python
# REFER: ../10.3.../10.3.4.../division_calculator.py
print("Give me two numbers, and I'll diveide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```
We replaced this:
```python
answer = int(first_number) / int(second_number)
print(answer)
```
for this:
```python
    try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print(answer)
```
let's break this down:
* `try` the division.
* `except` it is a zero-division, throw the specified message
  "You cant divide by 0!" instead of the traceback.
* `else` execute the no-exception code (print the answer).

```commandline
Give me two numbers, and I'll diveide them.
Enter 'q' to quit.

First number: 5

Second number: 0
You can't divide by 0!

First number: 5

Second number: 2
2.5

First number: q
```
By anticipating to errors, you can create more robust programs that can handle
invalid data and missing resources. Your code will be resistant to innocent
users and malicious attackers.

### 10.3.5 Handling the FileNotFoundError Exception
For different reasons, a file may be not found like misspelling, different
location, or not existing. You can handle them with a <i>try-except</i>
block.<br>
&emsp;Let's try to read the content of <i>Alice in Wonderland</i>,
but the file <i>alice.txt</i> is not in the same directory as
<i>alice.py</i>
```python
# REFER: ../10.3.../10.3.5.../alice.py
filename = 'alice.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read()
```
We have two changes:
* the file object, previously represented as `file_object` now is `f`,
  which is a common convention.
* we're using the `encoding` argument, which is needed when the default
  encoding of your system doesn't match the encoding of the reading file.

Python can't read from a missing file, so it raises an exception:
```commandline
Traceback (most recent call last):
  File "alice.py", line 3, in <module>
    with open(filename, encoding='utf-8') as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
```
The traceback reports the exception `FileNotFoundError`, which Python
creates when it can't find the file to open.

Let's add the exception to handle the error in the try block:
```python
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} doesn't exist")
```
* The code in the <i>try</i> block produces a <i>FileNotFoundError</i>.
* Python looks for a match in the <i>except</i> block (and it does).
* Python runs the <i>except</i> block, producing a friendly error message:
```commandline
Sorry, the file alice.txt doesn't exist
```
As the program ends with the <i>try-except</i> block, it doesn't add much.
Let's build an example with more than one file.

### 10.3.6 Analyzing Text
You can analyze from entire books. We're going to work with the text of the
book <i>Alice in Wonderland</i>, which is a public domain book. You can
find this and other public domain texts in <href>http://gutenberg.org</href>

Let's pull in the text of <i>Alice in Wonderland</i> and try to count the
number of words in the text.
We'll use the string method `split()`, which can build a list of words from
a string. Here's what the `split()` method does with the string
<i>"Alice in Wonderland"</i>/.
```pycon
>>> title = "Alice in Wonderland"
>>> title.split()
['Alice', 'in', 'Wonderland']
```
The `split()` method uses the spaces to separate the words and put the in
a list. We'll use the `split()` method on the alice.txt and measure the size
of the generated list to check have an idea of the number of words.
> NOTE: Some punctuation may appear with some of the words in the list.
```python
# REFER: ../10.3.../10.3.6.../alice.py
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file <<{filename}>> has about {num_words} words.")
```
Let's check on the last three lines of code, the action taken when the
`try` block works (which is this case)
* `words = contents.split()` - we split the content of the book, which creates
  a word by word list assigned to the variable `words`.
* `num_words = len(words)` - `len()` tells the number of items in the list
  `words`, and that value is assigned to `num_words`.
* `print(f"The file ...")` - throws the output into screen:
```commandline
The file <<alice.txt>> has about 30389 words.
```
This count is a bit higher because of extra information provided by the
publisher. Although is not exact, is a very good approximation.

### 10.3.7 Working with Multiple Files
Let's add more books, but first let's create the function `count_words()`
and move the related code there, so we have a reusable, and clean code.
```python
# REFER: ../10.3.../10.3.7.../word_count.py
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file <<{filename}>> has about {num_words} words.")

filename = 'alice.txt'
count_words(fielname)
```
The code remains almost the same, there are few changes.
* We defined the function `count_words()` and indented the code to be part
of that function.
* We changed the "<i>Count the approx...</i>" comment to a docstring
of the function. It's a good practice to keep comments up to date.

We can analyze more books in just one execution by creating a list
of books and using a loop:
```python
# REFER: ../10.3.../10.3.7.../word_count.2.py
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file <<{filename}>> has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
             'twenty_thousand_leagues_under_the_sea.txt']
for filename in filenames:
    count_words(filename)
```
The missing file <i>siddhartha.txt</i>, does not stop the execution
of the loop:
```commandline
The file <<alice.txt>> has about 30389 words.
Sorry, the file siddhartha.txt does not exist.
The file <<moby_dick.txt>> has about 215838 words.
The file <<twenty_thousand_leagues_under_the_sea.txt>> has about 107721 words.
```
Using the <i>try-except</i> block prevents users from seeing traceback and
lets the program t continue the execution.<br>
&emsp;If we don't use the <i>try-except</i> block the sees the traceback,
which ins undesirable, and the program stops, instead of throwing a result
on what actually works and send a friendly message, such as we are doing.

### 10.3.8 Failing Silently
You can tell Python to do nothing with the `pass` keyword. Which is exactly
what you need sometimes, and for example, you may want that if some file
is not found, nothing happens in the `except` block:
```python
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        --snip--
    except FileNotFoundError:
        pass
    else:
        --snip--
        
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
             'twenty_thousand_leagues_under_the_sea.txt']
for filename in filenames:
    count_words(filename)
```
Previously except block was sending a warning message on missing files.
Now it does nothing:
```commandline
The file <<alice.txt>> has about 30389 words.
The file <<moby_dick.txt>> has about 215838 words.
The file <<twenty_thousand_leagues_under_the_sea.txt>> has about 107721 words.
```
The `pass` statement acts as a placeholder, which reminds about the decision
of doing nothing at some specific point in the program, and you might want
to do something later. For example, in this program you probably would like
to write the missing files in a file called <i>missing_files.txt</i>.
So, our users wouldn't see the missing files during the execution, but
we'd be able to read the file and deal with any missing texts.


### 10.3.9 Deciding Which Errors to Report
When is better for your users to receive or not errors:
* If users know which texts are supposed to be analyzed, they might
appreciate knowing also why some texts were not analyzed.
* If users expect results but don't know which texts are supposed to be
analyzed, they might not need to know that some texts were unavailable.

Giving information the user is not requiring, may decrease the usability
of your program.<br>
Python provides vast error-handling structures, letting you control on
how much to share with users when an error happens.

Well-written, properly tested code is not prone to internal errors
(syntax or logical). But, depending on other factors such as user inputs,
network connection, file existence, you better be prepared for exceptions being
raised.

---
## 10.4 Storing Data
There are different reasons to store data like gaming, data visualization, or
even privacy settings. That data is stored in data structures (such as
lists or dictionaries). A simple way to do it is with the `json` module. 

With the `json` module you can move data <i>from</i> and <i>to</i> a file.
However, since the JSON data format is not specific to Python, you can share
data between Python's programs, such as programs with other programming 
languages.

> NOTE:<br> 
> The JSON (JavaScript Object Notation) was originally developed by JavaScript.
> However, it has since become a common format used by many languages,
> including Python.

### 10.4.1 Using json.dump() and json.load()
Let's create a program for storing a set of numbers using `json.dump()`,
which takes two arguments:
1. A piece of data to store.
2. A <i>file object</i> to store the data.

```python
# REFER: ../10.4.../10.4.1.../number_writer.py
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dum(numbers, f)
```
Let's break it down:
* we imported the json module.
* and created a list of numbers.
* `filename` gets the name of the file with <i>.json</i> extension.
* we open the file in write mode.
* we use the `json.dump()` function to store the list `numbers`
in the json file <i>numbers.json</i>.

This program has no output, but you can see the list in the file
<i>numbers.json</i>:
```text
[2, 3, 5, 7, 11, 13]
```
Now, we will create a program to read back into memory from the file 
<i>numbers.json</i>:
```python
# REFER: ../10.4.../10.4.1.../number_reader.py
import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)
```
Let's check what this program does:
* import the module `json`
* the `filename` variable gets the name of the json file `numbers.json`.
* we create the file object (f) to read from.
* the variable `numbers` gets the data using the function `json.load()` 
using the file object (f).
* we print the variable `numbers`:
```commandline
[2, 3, 5, 7, 11, 13]
```
This is a simple way to share data between two programs.

### 10.4.2 Saving and Reading User-Generated Data
Is useful to save user-generated data, because if you don't do it, data will
be lost when the program closes.<br>
&emsp;Let's create a program that:
* prompts the user for their name, the first time they run a program.
* remember their name when they run the program again.

Let's start by storing the name
```python
# REFER: ../10.4.../10.4.2.../remember_me.1.py
import json

username = input("What is your name?\n\t")
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")
```
Let's go step by step:
* import the json module.
* prompt the user to introduce their username.
* ensure the filename to write in.
* creates the file object in write mode.
* dumps the username into the file.
* print a message saying we store the user information:
```commandline
What is your name?
	Ismael
We'll remember you when you come back, Ismael!
```
Let's create a program that greets the user, with their name,
when they come back:
```python
# REFER: ../10.4.../10.4.2.../greet_user.py
import json

filename = "username.json"

with open(filename) as f:
    username = json.loads(f)
    print(f"Welcome back, {username}!")
```
What we did here is:
* import hte json module.
* select the file json file to read from.
* create the file object.
* use json to load (or read) from the file object.
* greet the user on screen using their username.
```commandline
Welcome back, Ismael!
```
Now, let's combine this into one file, and when someone opens
<i>remember_me.py</i> we retrieve their username from memory if the
<i>username.json</i> file exists, if not, we want to create that 
file and save the username:
```python
# REFER: ../10.4.../10.4.2.../remember_me.2.py
import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.loads(f)
except FileNotFoundError:
    username = imput("What is your username?\n\t")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
```
Here is the same code combined, excepting it is in a <i>try-except</i> block.
The possible outputs are:
1. if the json file does not exist:
    ```commandline
    What is your username?
        ismael
    We'll remember you when you come back, Ismael!
    ```
2. if the json file does exist:
    ```commandline
    Welcome back, Ismael!
    ```

### 10.4.3 Refactoring
When you think your code (despite it works) can be cleaner, easier to
understand, and easier to extend, you want to do some <i>refactoring</i> by
breaking down your code into smaller functions with more specific tasks.

We can refactor <i>remember_me.2.py</i> by moving the bulk of its code
into one or more functions. The focus of the program is to greet the user.
Let's move the code into a function called `greet_user()`:
```python
# REFER: ../10.4.../10.4.3.../remember_me.1.py
import json

def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your username?\n\t").lower().title()
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")

greet_user()
```
First of all we update the comments to docstring because we are using a 
function.<br>
This file is a little cleaner, but `greet_user()` does the following tasks:
* if user exists:
  * retrieves stored username.
  * greets the user.
* if not:
  * prompts a new username.
Let's refactor it so it does more specific functions:
```python
# REFER: ../10.4.../10.4.3.../remember_me.2.py
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name?\n\t")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}")

greet_user()
```
Let's break down `get_stored_username()` which now has a clear purpose:
* It has no comments but a well descriptive docstring.
* it retrieves a stored username (if it exists) 
* or return `None` if it does not.
  * > A function should return the value expected or `None`, which  is a
    > good practice. This allows as to perform a simple test with the return
    > value of a function.

Now let's see what's going on with `greet_user()`:
* it calls the function `get_stored_username()`
* it has two possible actions:
  * if the name exists prints the "Welcome back..." message.
  * if it does not, prompts the user for a username to store it.

We should refactor `greet_user()`, so that, when the username does not
exist, a dedicated function prompts for the new username:

```python
# REFER: ../10.4.../10.4.3.../remember_me.3.py
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
        username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompts for a new username."""
    username = input("What is your name?\n\t")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}")

greet_user()
```
Each function has a clear single, clear purpose.<br>

* `get_stored_username()` retrieves the stored username.
* `get_new_username()` prompts for a new username and stores it.
* `greet_user()` prints the appropriate message for each situation
  * username stored (Welcome back...).
  * username not stored (We'll remember you...).

























