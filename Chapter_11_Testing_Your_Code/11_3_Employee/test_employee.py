import pytest
from employee import Employee

@pytest.fixture
def employee_test():
    employee_test = Employee('john','doe', 0)
    return employee_test

def test_give_default_raise(employee_test):
    """UT to increase annual salary by default and expect default"""

    employee_test.give_raise()
    expected_salary = employee_test.annual_salary
    assert expected_salary == 5000

def test_give_custom_raise(employee_test):
    """increase annual salary by specific amount"""
    employee_test = Employee('john', 'doe', 1000)
    employee_test.give_raise(200)
    expected_salary = employee_test.annual_salary
    assert expected_salary == 1200

def test_give_default_raise_inceasing():
    """UT to increase annual salary by default and expect more than default"""
    test_employee = Employee('john','doe', 1000)
    test_employee.give_raise()
    expected_salary = test_employee.annual_salary
    assert expected_salary > 5000