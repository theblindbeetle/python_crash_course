"""
6-11. Cities:
• Make a dictionary called cities.

• Use the names of three cities as keys in your dictionary.

• Create a dictionary of information about each city and include the country
    that the city is in, its approximate population, and one fact about that
    city.

• The keys for each city’s dictionary should be something like country,
    population, and fact.

• Print the name of each city and all the information you have stored about it.
"""

cities = {
    'sydney': {
        'country': 'australia',
        'population': 5248790,
        'fact': 'it has one of the most popular theaters in the world.'
    },
    'Warsaw': {
        'country': 'poland',
        'population': 1800230,
        'fact': 'it is the city where Frederic Chopin was born.'
    },
    'San Salvador': {
        'country': 'bahamas',
        'population': 525990,
        'fact': 'it is the first place in America found by the expedition of'
                'Christopher Columbus and his crew.'
    }
}

for city, info in cities.items():
    print(f"\nWhat we know about {city.title} is:")
    for key, value in info.items():
        print(f"\t{key.title()}: {value}")