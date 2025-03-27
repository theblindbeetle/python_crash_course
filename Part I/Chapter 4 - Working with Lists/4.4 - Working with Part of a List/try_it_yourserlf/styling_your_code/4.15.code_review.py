"""
4-15. Code Review: Choose three of the programs you’ve written in this chapter
and modify each one to comply with PEP 8:
    • Use four spaces for each indentation level. Set your text editor to insert
    four spaces every time you press tab, if you haven’t already done so (see
    Appendix B for instructions on how to do this).
    • Use less than 80 characters on each line, and set your editor to show a
    vertical guideline at the 80th character position.
    • Don’t use blank lines excessively in your program files.
"""

# in "4.7.threes.py": list creation did not have space after coma
threes = list(range(3, 31, 3))
for number in threes:
    print(number)

# in "3.8.seeing_the_world.py":
# Lines too long in the docstrings
# Also, there are many lines in a row, they should have separation and better
# comments.

"""
3-8. Seeing the World:
    Think of at least five places in the world you’d like to visit.
    √  Store the locations in a list. Make sure the list is not in alphabetical
        order.
    √  Print your list in its original order. Don’t worry about printing the 
        list neatly, just print it as a raw Python list.
    √  Use sorted() to print your list in alphabetical order without modifying 
        the actual list.
    √  Show that your list is still in its original order by printing it.
    √  Use sorted() to print your list in reverse alphabetical order without 
        changing the order of the original list.
    √  Show that your list is still in its original order by printing it again.
    √  Use reverse() to change the order of your list. Print the list to show 
        that its order has changed.
    √  Use reverse() to change the order of your list again. Print the list to 
        show it’s back to its original order.
    √  Use sort() to change your list so it’s stored in alphabetical order. 
        Print the list to show that its order has been changed.
    √  Use sort() to change your list so it’s stored in reverse alphabetical 
        order. Print the list to show that its order has changed.
"""
# Create list
places = ['Kilimanjaro', 'Toscana', 'Greenland', 'Antartica', 'Sahara']
print(places)

# Print sorted list (unmodified) and validate original
print(sorted(places))
print(places)

# Print alphabetically reverse with the method `sorted` and validate original
print(sorted(places, reverse=True))
print(places)

# Use reverse() to change the order of the list
places.reverse()
print(places)

# Use reverse() to change the order of the list again
places.reverse()
print(places)

# sort alphabetically with sort()
places.sort()
print(places)

# sort alphabetically backwards with sort()
places.sort(reverse=True)
print(places)

