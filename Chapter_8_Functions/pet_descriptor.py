def describe_pet(pet_type, pet_name):
    """" Describes each pet's name and type"""
    print(f"\n{pet_name.title()} is a {pet_type.title()}")

describe_pet(pet_type='dog', pet_name='alaska')
describe_pet(pet_name='malcho', pet_type='cat')