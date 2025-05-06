"""
8-4. Large Shirts:

• Modify the make_shirt() function so that
    • shirts are large by default
    • with a message that reads I love Python.

• Make a large shirt and a medium shirt with the default message,
• and a shirt of any size with a different message.
"""

def make_shirt(size='L', text='I ♥ Python'):
    message = f"\nT-shirt size:{str(size)}"
    message += f"\nText desired: {text}"
    print(message)

# Default Shirt
make_shirt()

# Using keyword arguments:
make_shirt(text='Tiny message for small T-sh..', size='S')