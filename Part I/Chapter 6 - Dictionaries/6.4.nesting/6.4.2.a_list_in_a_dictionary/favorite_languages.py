fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in fav_languages.items():
    print(f"{name.title()} favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")