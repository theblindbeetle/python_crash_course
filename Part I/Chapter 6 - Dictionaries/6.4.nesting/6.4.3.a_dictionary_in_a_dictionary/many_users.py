users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }

}

for username, info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{info['first'].title()} {info['last'].title()}"
    location = info['location'].title()
    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location}")