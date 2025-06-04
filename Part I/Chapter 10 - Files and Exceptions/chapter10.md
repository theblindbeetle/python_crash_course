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
### 1.2.1 Writing to an Empty File
### 1.2.2 Writing Multiple lines
### 1.2.3 Appending to a File

---
## 10.3 Exceptions
### 1.3.1 Handling the ZeroDivisionError Exception
### 1.3.2 Using try-except Blocks
### 1.3.3 Using Exceptions to Prevent Crashes
### 1.3.4 The else Block
### 1.3.5 Handling the FileNotFoundError Exception
### 1.3.6 Analyzing Text
### 1.3.7 Working with Multiple Files
### 1.3.8 Failing Silently
### 1.3.9 Deciding Which Errors to Report

---
## 10.4 Storing Data
### 10.4.1 Using json.dump() and json.load()
### 10.4.2 Saving and Reading User-Generated Data
### 10.4.3 Refactoring