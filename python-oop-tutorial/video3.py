# Video 3 - Class methods and static methods
# https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4

import datetime


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        Employee.num_of_emps += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        """
        classmethod takes cls for class, and its passed automatically like self
        """
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        """
        Alternative constructor
        """
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        """
        staticmethod does not depend on class or instance

        5 for saturday, 6 for sunday
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return "No"
        return "Yes"


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)
emp_3 = Employee.from_string("Pedro-Barcellos-70000")

print(emp_3.full_name())

# Sets raise amount for the class and every instance
Employee.set_raise_amt(1.05)

# Sets raise amount for this instance
emp_2.raise_amount = 1.02

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


my_date = datetime.date(2021, 8, 30)
print(f"Is work day? {Employee.is_workday(my_date)}")
