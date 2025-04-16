### 8-5. Cities:

def describe_city(city, country="iceland"):
    """"Match contry and city"""
    print(f"{city.title()} is in {country.title()}.")

describe_city(city="Husavik")
describe_city(country="Italy", city="Taormina")
describe_city("Syracuse", "Italy")