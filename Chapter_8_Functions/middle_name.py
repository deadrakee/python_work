def get_formatted_name(first_name, last_name, middle_name="", spanish_name=""):
    """"Optional middle name"""
    if middle_name:
        middle_name += " "
    if spanish_name:
        spanish_name += " "
    return f"{first_name} {middle_name}{spanish_name}{last_name}".title()

my_name = get_formatted_name('boyan', 'sabchev', "garcia", 'Krasimirov')
print(my_name)