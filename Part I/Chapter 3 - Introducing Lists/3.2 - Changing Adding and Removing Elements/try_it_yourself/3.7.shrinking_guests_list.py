"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
•  Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
•  Use pop() to remove guests from your list one at a time until only two names remain in your list.
   Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
•  Print a message to each of the two people still on your list, letting them
know they’re still invited.
•  Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
"""
guests =  ['Ticho', 'Hypatia', 'Cleo']

guests[0] = 'Clippy'

guests.insert(0, 'John Doe')
guests.insert(3, 'Jane Doe')
guests.append('Timothy')

message = ". Sorry, but I'm will re-schedule with you for the next week."
print("Hey, guys. There is a delay on the table, I'm going to change the date for the most of you, so we can get together the next week.")

popped_guest = guests.pop()
print(f"Hey, {popped_guest}{message}")
popped_guest = guests.pop(1)
print(f"Hey, {popped_guest}{message}")
popped_guest = guests.pop()
print(f"Hey, {popped_guest}{message}")
popped_guest = guests.pop(1)
print(f"Hey, {popped_guest}{message}")
print("\n\n")
print(f"Hey, {guests[0]}, I'll see you following Thursday")
print(f"Hey, {guests[1]}, I'll see you following Thursday")
