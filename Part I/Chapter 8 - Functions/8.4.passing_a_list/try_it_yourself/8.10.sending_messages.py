"""
8-10. Sending Messages:

• Start with a copy of your program from Exercise 8-9.

• Write a function called send_messages()
    • that function prints each text message
    • and moves each message to a new list called sent_messages as it’s printed.

• After calling the function, print both of your lists to make sure the messages
    were moved correctly.
"""

def send_messages(messages, sent):
    """Print the messages received."""
    print("The messages received are:")
    while messages:
        message = messages.pop()
        print(f"\t{message}")
        sent.append(message)

def show_lists(unsent, sent):
    """Prints the lists to validate the messages are moved"""
    print(f"Unsent messages:\n\t{unsent_messages}")
    print(f"Sent messages:\n\t{sent_messages}")


unsent_messages = ['msg1', 'msg2', 'msg3', 'msg4']
sent_messages = []

send_messages(unsent_messages, sent_messages)
show_lists(unsent_messages, sent_messages)




