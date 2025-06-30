### 9-6. Ice Cream Stand:

class Restaurant:
    """Abstraction of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Construct a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Prints dishes type"""
        print(f"\n{self.restaurant_name} serves {self.cuisine_type} dishes!")


    def open_restaurant(self):
        """Prints a statement"""
        print(f"\n{self.restaurant_name} is OPEN!")


    def increment_number_served(self, number_served):
        """Update how many customers were served today"""
        self.number_served = number_served


class IceCreamStand(Restaurant):
    """Abstraction of an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors


    def display_flavors(self):
        """Print all flavors"""
        print("\nIce cream flavors:")
        for flavor in self.flavors:
            print(f"\t{flavor}")


flavors = ["chocolate", "vanilla", "strawberry"]
my_ice_stand = IceCreamStand("Raffy", "Ice Creams", flavors)
my_ice_stand.describe_restaurant()
my_ice_stand.display_flavors()