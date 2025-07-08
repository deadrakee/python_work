"""Module for methods which build city names"""

def name_city(city_name, country_name, population=''):
    """combine names in a single string"""
    if population:
        formatted_name = f"{city_name.title()}, {country_name.title()} - population {population}"
    else:
        formatted_name = f"{city_name.title()}, {country_name.title()}"
    return formatted_name