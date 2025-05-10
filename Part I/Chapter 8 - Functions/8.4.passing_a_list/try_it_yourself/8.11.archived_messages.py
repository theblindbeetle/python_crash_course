"""
8-11. Archived Messages:

• Start with your work from Exercise 8-10.

• Call the function send_messages() with a copy of the list of messages.

• After calling the function, print both of your lists to show that
    the original list has retained its messages
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

send_messages(unsent_messages[:], sent_messages)
show_lists(unsent_messages, sent_messages)
