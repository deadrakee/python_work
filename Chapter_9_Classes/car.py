# use inheritance

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
        self.battery = 20


    def describe_car(self):
        """"print Car + ElectricCar"""
        super().describe_car()
        print(f"\t{self.battery}")


my_car = Car("Reanult", "Megane", 2017)
my_car.describe_car()

venko_car = ElectricCar("Ford", "Mondeo", 2022)
venko_car.describe_car()

yavor_car = ElectricCar("BMW", "i3", 2024)
yavor_car.describe_car()

mom_car = Car("Seat", "Ibiza", 2008)
mom_car.describe_car()