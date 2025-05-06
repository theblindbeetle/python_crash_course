"""
8-3. T-Shirt:

• Write a function called make_shirt()

• that function accepts a size and the text of a message that should be printed
    on the shirt.

• The function should print a sentence summarizing the size of the shirt and the
    message printed on it.

• Call the function once using positional arguments to make a shirt.

• Call the function a second time using keyword arguments.
"""

def make_shirt(size, text):
    message = f"\nT-shirt size:{str(size)}"
    message += f"\nText desired: {text}"
    print(message)


# Using positional arguments:
make_shirt('M', 'The best party in history!')

# Using keyword arguments:
make_shirt(text='Making shirts is awesome.', size='XL')
