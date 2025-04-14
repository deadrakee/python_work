### 6-9. Favorite Places:

favorite_places = {
    'ivo': ['iceland', 'japan', 'egypt',],
    'gabi': ['madeira', 'iceland', 'peru',],
    'steven': ['deutschland',],
    'martin': ['greece', 'brazil', 'italy',],
}

for traveller, locations in favorite_places.items():
    print(f"\n{traveller.title()} likes ")

    for location in locations:
        print(f"\t{location.title()}")