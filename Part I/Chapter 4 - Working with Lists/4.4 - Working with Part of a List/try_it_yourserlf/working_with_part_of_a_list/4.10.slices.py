"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:

1.  Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.

2.  Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.

3.  Print the message The last three items in the list are:. Use a slice to print the last three items in the list.
"""

items = ['soccer ball', 'lamp', 'pen', 'wave', 'book']
print(f"The first three items are:\n\t{items[:3]}")
print(f"Three itmes from the middle of the list are:\n\t{items[1:4]}")
print(f"The last three itmes from the  list are:\n\t{items[-3:]}")