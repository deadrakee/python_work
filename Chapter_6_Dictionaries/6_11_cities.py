### 6-11. Cities:

cities = {
    'sofia': {
        'country': 'bulgaria',
        'population': 2_000_000,
        'fact': "Izmislili sme kiseloto mlqko", 
    },

    'reykjavik': {
        'country': 'iceland',
        'population': 140_000,
        'fact': 'The word Reykjavík translates literally as “smoky bay”', 
    },

    'tokyo': {
        'country': 'japan',
        'population': 14_180_000,
        'fact': 'Tokyo has the second most Michelin-starred restaurants in the world', 
    },
}

for city, info_d in cities.items():
    print(f"\n{city.title()} information:")

    for info_category, info_value in info_d.items():
        print(f"\t{info_category} - {info_value}")