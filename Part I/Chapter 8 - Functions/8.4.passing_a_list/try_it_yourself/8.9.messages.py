"""
8-9. Messages:

• Make a list containing a series of short text messages.

• Pass the list to a function called show_messages(), which prints each text
    message.
"""

def show_messages(messages):
    print("The messages received are:")
    for message in messages:
        print(f"\t{message}")

messages = ['msg1', 'msg2', 'msg3', 'msg4']
show_messages(messages)