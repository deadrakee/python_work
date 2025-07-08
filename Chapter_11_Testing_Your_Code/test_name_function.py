from name_function import get_formatted_name

def test_first_last_name():
    """unit test"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_middle_last_name():
    """enter three names"""
    formatted_name = get_formatted_name("Johan", "bach", "sebastian")
    assert formatted_name == 'Johan Sebastian Bach'