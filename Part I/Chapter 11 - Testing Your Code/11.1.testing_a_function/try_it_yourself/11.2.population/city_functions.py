"""
NOTE: This is activity is based on the already developed 11.1

11-2. Population:

√ • Modify your function so it requires a third parameter, population.

• It should now return a single string of the form
    • City,
    • Country – population xxx,
        such as Santiago, Chile – population 5000000.

√ • Run test_cities.py again.

√ • Make sure test_city_country() fails this time.

√ • Modify the function so the population parameter is optional.

√ • Run test_cities.py again, and make sure test_city_country() passes again.

√ • Write a second test called test_city_country_population()
    that verifies you can call your function with the values
    'santiago', 'chile', and 'population=5000000'.

√• Run test_cities.py again, and make sure this new test passes.
"""
# # Original version
# def place(city, country):
#     """Generates a formated "city, country" string."""
#     formatted_place = f"{city}, {country}"
#     return formatted_place.title()



# # Third parameter failing version:
# # TypeError: place() missing 1 required positional argument: 'population'
# def place(city, country, population):
#     """Generates a formated "city, country" string."""
#     formatted_place = f"{city}, {country} - population {population}"
#     return formatted_place.title()



# Third parameter passing version:
def place(city, country, population=''):
    """Generates a formated "city, country - population xxx" string."""
    if population:
        formatted_place = f"{city.title()}, {country.title()} - population {str(population)}"
    else:
        formatted_place = f"{city.title()}, {country.title()}"
    return formatted_place

'Santiago, Chile - Population 5000000'
'Santiago, Chile - population 5000000'