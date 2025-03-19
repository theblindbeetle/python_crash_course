"""
3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.
"""
# --------------------------
message = "Creating a list"
print(f"\n{message.upper()}")

books = ['The Prince', 'Northern Lights', 'the green mile', 'Mobi Dick', 'The Dark Tower']
print(books)

# --------------------------
message = "Calling a list and its individual elements"
print(f"\n{message.upper()}")

print(f"create a list:\n{books}")

print(f"access with index an element of the list (index 2):\n{books[2]}")

print(f"index position starts with 0, not 1:\npos_0<<{books[0]}>> pos_1<<{books[1]}>>")

print(f"access the last element of the list(index -1):\n{books[-1]}")

print(f"using individual values as in a variable (index 2 with title()):\n{books[2].title()}")

# --------------------------
message = "Modifying a list"
print(f"\n{message.upper()}")

previous = books[2]
books[2] = "The Great Gatsby"
print(f"modify elements in the list (index 2 was{previous}):\n{books[2]}")

# --------------------------
message = "Adding elements ot a list"
print(f"\n{message.upper()}")

books.append("Twenty Thousand Leagues Under the Sea")
print(f"add elements at the end of the list:\n{books}")

books.insert(1, "the moons of Jupiter")
print(f"insert an item on the selected index (index 1 <<{books[1]}>>):\n{books}")

#--------------------------
message = "Removing items from the list"
print(f"\n{message.upper()}")

previous = books[1]
del books[1]
print(f"delete items on the selected index (index 1 <<{previous}>>):\n{books}")

popped_element = books.pop()
print(f"popping the last element of the list and using the value (index pop() <<{popped_element}>>):\n{books}")

popped_element = books.pop(3)
print(f"popping element from the list in a specific position (index pop(3) <<{popped_element}>>):\n{books}")

books.remove('Northern Lights')
print(f"removing an item by value (removes <<Northern Lights>>):\n{books}")

# --------------------------
message = "Sorting lists"
print(f"\n{message.upper()}")

print(f"sort list alphabetically and keep original:\n{sorted(books)}")

print(f"sort list alphabetically backwards and keep original:\n{sorted(books, reverse=True)}")

books.reverse()
print(f"reverse current order of the list permanent modification:\n{books}")

books.reverse()
print(f"reverse current order of the list permanent modification (to restore original):\n{books}")

books.sort()
print(f"sort the list permanently in alphabetical order:\n{books}")

books.sort(reverse=True)
print(f"sort the list permanently in backwards alphabetical order:\n{books}")

# --------------------------
message = "length of a list"
print(f"\n{message.upper()}")
print(f"The length is: {len(books)}")

