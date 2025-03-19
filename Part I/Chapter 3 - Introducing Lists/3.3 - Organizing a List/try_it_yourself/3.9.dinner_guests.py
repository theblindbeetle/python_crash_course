"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 42), use len() to print a message indicating the number
of people you are inviting to dinner.
"""
guests =  ['Ticho', 'Hypatia', 'Cleo']
print(f"Ex. 3.4 > {len(guests)}")
guests[0] = 'Clippy'
print(f"Ex. 3.5 > {len(guests)}")
guests.insert(0, 'John Doe')
guests.insert(3, 'Jane Doe')
guests.append('Timothy')
print(f"Ex. 3.6 > {len(guests)}")
guests.pop()
guests.pop(1)
guests.pop()
guests.pop(1)
print(f"Ex. 3.7 > {len(guests)}")