"""
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
    •  Use a loop to print a sentence about each river, such as The Nile runs
        through Egypt.

    •  Use a loop to print the name of each river included in the dictionary.

    •  Use a loop to print the name of each country included in the dictionary.
"""
rivers = {
    'nile': 'egypt',
    'sena': 'england',
    'bravo': 'mexico',
    }
for key, value in rivers.items():
    print(f"{key.title()} is an well known river in {value}.")

print("\n")
for key in rivers.keys():
    print(f"{key}")

print("\n")
for value in rivers.values():
    print(f"{value}")

