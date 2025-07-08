"""Module for employee creation"""

class Employee:
    """Abstraction of an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        """Construct an Employee object"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5_000):
        """increase the annual salary"""
        self.annual_salary += amount