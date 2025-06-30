### 9-9. Battery Upgrade:

class Car:
    """Abstraction of a car"""
    def __init__(self, brand, model, year):
        """"Construct a car"""
        self.brand = brand
        self.model = model
        self.year = year
        

    def describe_car(self):
        """Print all details of a car"""
        print(f"\nDetails:\n\t{self.brand}\n\t{self.model}\n\t{self.year}")



class ElectricCar(Car):
    def __init__(self, brand, model, year):
        """Construc an electic car"""
        super().__init__(brand, model, year)
        self.battery = Battery()


    def describe_car(self):
        """"print Car + ElectricCar"""
        super().describe_car()
        print(f"\t{self.battery.battery_size}")



class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size


    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"\nThis car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")


    def upgrade_battery(self):
        """Increase battery_size attribute"""
        if(65 > self.battery_size):
            self.battery_size = 65



venko_car = ElectricCar("Ford", "Mondeo", 2022)
venko_car.describe_car()

venko_car.battery.get_range()
venko_car.battery.upgrade_battery()
venko_car.battery.get_range()

venko_car.describe_car()