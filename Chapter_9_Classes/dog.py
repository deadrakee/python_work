# A simple class, creating dogs

class Dog:
    """Abstraction of a dog"""

    def __init__(self, name, age):
        """construct the new dog"""
        self.name = name
        self.age = age


    def sit(self):
        """Simulate sitting"""
        print(f"{self.name} is now sitting\n")


    def roll_over(self):
        """Simulate rolling over"""
        print(f"{self.name} is rolling on the lawn\n")

krasi_dog = Dog("Jorko", 4)
dariya_dog = Dog("Alyaska", 10)

print(f"{dariya_dog.name} is {dariya_dog.age} years old.\n")

krasi_dog.sit()
dariya_dog.roll_over()