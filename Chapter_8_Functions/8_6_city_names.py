### 8-6. City Names:

def city_country(city, country):
    """Prints formatted city - country pair"""
    formated_city_country = f"{city}, {country}"
    return formated_city_country.title()

print(city_country('sofia', 'bulgaria'))
print(city_country('lodnon', 'uk'))
print(city_country('hiroshima', 'japan'))