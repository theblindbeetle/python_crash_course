"""
10-8. Cats and Dogs:

• Make two files:
    * cats.txt
    * dogs.txt

• Store at least
    * three names of cats in the first file
    * and three names of dogs in the second file.

• Write a program that
    • tries to read these files
    • and print the contents of the file to the screen.

 • Wrap your code in a try-except block
    • to catch the FileNotFound error,
    • and print a friendly message if a file is missing.

• Move one of the files to a different location on your system,
    and make sure the code in the except block executes properly.
"""

DIVIDER = '-' * 15

def record_animals(filename, animal_list):
    """Add string items from a list into the txt file required."""
    print(f"{DIVIDER}\n\tAdding elements to file: {filename}")
    for animal_name in animal_list:
        with open(filename, 'a') as file_object:
            file_object.write(f"{animal_name}\n")

def read_file(filename):
    """Reads information from a file and print it on screen."""
    print(f"{DIVIDER}\n\tReading elements from file: {filename}")
    try:
        with open(filename) as f:
            for cat in f.readlines():
                print(f"\t{cat.strip()}")
    except FileNotFoundError:
        print(f"The file <<{filename}>>, is not available.")

cats_file = "cats.txt"
cats_list = ['cat_1', 'cat_2', 'cat_3']
dogs_file = "dogs.txt"
dogs_list = ['dog_1', 'dog_2', 'dog_3']
parrot_file = "parrot.txt"

record_animals(cats_file, cats_list)
record_animals(dogs_file, dogs_list)

read_file(cats_file)
read_file(dogs_file)
read_file(parrot_file)

# NOTE:
# 1. I added the `parrot.txt` file so you can watch the behavior of
#       the program without modifications.
# 2. Consider the line `30` of the code
#   `with open(filename, 'a') as file_object:`
#   will increase the content of the file on every execution, if you
#   execute it again, the list will be added again. Feel free to
#   modify the `*.txt` files if you want them empty to execute them again.