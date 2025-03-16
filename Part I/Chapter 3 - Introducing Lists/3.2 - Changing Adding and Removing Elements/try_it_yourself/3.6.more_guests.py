"""
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
•  Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger
dinner table.
•  Use insert() to add one new guest to the beginning of your list.
•  Use insert() to add one new guest to the middle of your list.
•  Use append() to add one new guest to the end of your list.
•  Print a new set of invitation messages, one for each person in your list
"""

guests =  ['Ticho', 'Hypatia', 'Cleo']

print(f"Dear {guests[0]}. \nWe're honored to invite you to dinner the following Thursday.")
print(f"Hey, {guests[1]}... whasssaaaa!!!!\nWe're having a dinner the following Thursday, please don't make excuses this time and come at least for a while, we enjoy a lot your company.")
print(f"Hi, {guests[2]}.\n how you doing? I already told you last week, but don't forget to come to the dinner following Thursday. Last time you didn't finish that story of that old Alex. I'll be waiting for it.")
print("\n\n")
print(f"Dear {guests[0]}.\nWe're sorry you'll can't make it. It will be next time.")
guests[0] = 'Clippy'
print("\n\n")
print(f"{guests[0].upper()}!!!!!!!!!!!!!!!! \nDon't tell Billy, I want you to be part of this small and selected group of friends. Come to dinner following Thursday. We're anxious to see you again.")
print(f"Hey, {guests[1]}... whasssaaaa!!!!\nWe're having a dinner the following Thursday, please don't make excuses this time and come at least for a while, we enjoy a lot your company.")
print(f"Hi, {guests[2]}.\n how you doing? I already told you last week, but don't forget to come to the dinner following Thursday. Last time you didn't finish that story of that old Alex. I'll be waiting for it.")

print("\n\n")
print("Hey people, Ticho is not coming, Clippy just confirmed, and good news found a bigger table... I'm going to invite 3 more guys.")

guests.insert(0, 'John Doe')
guests.insert(3, 'Jane Doe')
guests.append('Timothy')
print(f"Dear {guests[0]}.\tDon't forget to assist to our close circle dinner the following Thursday.")
print(f"Dear {guests[1]}.\tDon't forget to assist to our close circle dinner the following Thursday.")
print(f"Dear {guests[2]}.\tDon't forget to assist to our close circle dinner the following Thursday.")
print(f"Dear {guests[3]}.\tDon't forget to assist to our close circle dinner the following Thursday.")
print(f"Dear {guests[4]}.\tDon't forget to assist to our close circle dinner the following Thursday.")
print(f"Dear {guests[5]}.\t\tDon't forget to assist to our close circle dinner the following Thursday.")

