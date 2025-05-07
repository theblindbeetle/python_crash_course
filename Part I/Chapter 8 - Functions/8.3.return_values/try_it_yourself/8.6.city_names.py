"""
8-6. City Names:
• Write a function called city_country()
    that takes in the name of a city and its country.

• The function should return a string formatted like this:
    • "Santiago, Chile"

• Call your function with at least three city-country pairs, and print the
    values that are returned.
"""

def city_names(city, country):
    return f"{city.title()}, {country.title()}"

pair = city_names('okinawa', 'japan')
print(pair)
pair = city_names('jakarta', 'indonesia')
print(pair)
pair = city_names('budapest', 'hungary')
print(pair)
