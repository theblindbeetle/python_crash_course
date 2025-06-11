"""
10-9. Silent Cats and Dogs:

• Modify your except block in Exercise 10-8 to fail silently if either
    file is missing.
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
        pass

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