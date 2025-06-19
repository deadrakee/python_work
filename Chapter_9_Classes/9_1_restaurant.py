### 9-1. Restaurant:

class Restaurant:
    """Abstraction of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Construct a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """Prints bot attributes"""
        print(f"\n{self.restaurant_name} serves {self.cuisine_type} dishes!")


    def open_restaurant(self):
        """Prints a statement"""
        print(f"\n{self.restaurant_name} is OPEN!")


restaurant_1 = Restaurant("Lachoni", "Pizza")

print(restaurant_1.restaurant_name)
print(restaurant_1.cuisine_type)
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()