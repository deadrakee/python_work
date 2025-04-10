# search for dictionary item in a list

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

friends = ["sarah","edward"]

for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        print(f"\t{name.title()} codes in {favorite_languages[name]}")