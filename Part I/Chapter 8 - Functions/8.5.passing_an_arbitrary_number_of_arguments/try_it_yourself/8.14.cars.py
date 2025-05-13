"""
8-14. Cars:

• Write a function that stores information about a car in a dictionary.

• The function should always receive a manufacturer and a model name.

• It should then accept an arbitrary number of keyword arguments.

• Call the function with the required information and two other name-value
    pairs, such as a color or an optional feature.

• Your function should work for a call like this one:
---------------------------------------------------------------
car = make_car('subaru', 'outback', color='blue', tow_package=True)
---------------------------------------------------------------

• Print the dictionary that’s returned to make sure all the information was
    stored correctly.
"""

def make_car(manufacturer, model_name, **car_details):
    """summarize the information according to the car."""
    car_details['manufacturer'] = manufacturer
    car_details['model name'] = model_name
    return car_details

car_summary = make_car(
    'toyota',
    'corolla',
    rim_size = '20-inch',
    engine_type = 'Hybrid'
    )
print("Car details:")
for feature, description in car_summary.items():
    print(f"\t- {feature}: {description}")