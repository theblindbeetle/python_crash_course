"""
7-2. Restaurant Seating:

• Write a program that asks the user how many people are in their dinner group.

• If the answer is more than eight:
    • print a message saying they’ll have to wait for a table.
• Otherwise:
    • Report that their table is ready.
"""
users = input("How many people are going to be on your table?\n\t")

if int(users) > 8:
    print(f"There is a waiting time for {int(users) * 2} minutes. If you desire"
          f"you can wait in the lobby.")
else:
    print(f"Excellent there is a table ready for you.")


