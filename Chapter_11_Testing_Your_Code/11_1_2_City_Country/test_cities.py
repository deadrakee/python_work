### 11-1. City, Country:

from city_functions import name_city

def test_city_country():
    """unit test for two names concatenation"""
    formatted_location = name_city("santiago", "chile")
    assert formatted_location == "Santiago, Chile"

### 11-2. Population:
def test_city_country_population():
    """UT concatenating three location params"""
    formatted_location = name_city('Santiago', 'chile', 5_000_000)
    assert formatted_location == 'Santiago, Chile - population 5000000'