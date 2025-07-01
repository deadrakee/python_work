"""Contains a class representing a restaurant"""

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