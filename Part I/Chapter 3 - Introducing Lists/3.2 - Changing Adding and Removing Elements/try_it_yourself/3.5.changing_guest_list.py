"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
•  Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
•  Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
•  Print a second set of invitation messages, one for each person who is still in your list
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
