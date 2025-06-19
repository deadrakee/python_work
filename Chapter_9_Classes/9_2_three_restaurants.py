### 9-2. Three Restaurants:

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

    def test_static():
        print("Static")


restaurant_1 = Restaurant("Frankos", "Pizza")
restaurant_2 = Restaurant("Namoos", "Greek")
restaurant_3 = Restaurant("Djumaq", "Bulgarian")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
