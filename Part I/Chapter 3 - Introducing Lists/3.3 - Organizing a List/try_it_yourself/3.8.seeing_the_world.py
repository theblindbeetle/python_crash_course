"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
√  Store the locations in a list. Make sure the list is not in alphabetical order.
√  Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
√  Use sorted() to print your list in alphabetical order without modifying the actual list.
√  Show that your list is still in its original order by printing it.
√  Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
√  Show that your list is still in its original order by printing it again.
√  Use reverse() to change the order of your list. Print the list to show that its order has changed.
√  Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
√  Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
•  Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
"""
# Create list
places = ['Kilimanjaro', 'Toscana', 'Greenland', 'Antartica', 'Sahara']
# Print list created
print(places)
# Print sorted list (unmodified)
print(sorted(places))
# verify original
print(places)
# Print alphabetically reverse with the method `sorted`
print(sorted(places, reverse=True))
# verify original
print(places)
# Use reverse() to change the order of the list
places.reverse()
# Print the modified list
print(places)
# Use reverse() to change the order of the list again
places.reverse()
# Print the original list
print(places)
# sort alphabetically with sort()
places.sort()
# print sorted list
print(places)
# sort alphabetically backwards with sort()
places.sort(reverse=True)
print(places)