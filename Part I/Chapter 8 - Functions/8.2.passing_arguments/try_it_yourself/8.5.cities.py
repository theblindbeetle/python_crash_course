"""
8-5. Cities:
• Write a function called describe_city()

• That function accepts the name of a city and its country.

• The function should print a simple sentence, such as Reykjavik is in Iceland.

• Give the parameter for the country a default value.

• Call your function for three different cities,
    • at least one of which is not in the default country.
"""

def describe_city(city, country='Brazil'):
    message = f"{city} is in {country}."
    print(message)

describe_city('San Carlos de Bariloche', 'Argentina')
describe_city(country='Austria', city='Vienna')
describe_city('Curitiba')

