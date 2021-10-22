# Video 5 - Special (Magic/Dunder) Methods
# https://youtu.be/3ohzBxoFHAY?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        Employee.num_of_emps += 1

    def __repr__(self):
        """Convert to formal string, for rep()
        >>> Employee('First', 'Last', pay)
        """
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.full_name()} - {self.email}"

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1)
print(repr(emp_1))
print(str(emp_1))

# Dunder methods from int and str class
print(int.__add__(1, 2))
print(str.__add__('Pedro', ' Barcellos'))

test = 'test'
print(f"len of {test} = {len(test)}")
print(f"len of {test} = {test.__len__()}")

# This method works beacause of the dunder method created on the class
print(f"Length of employee full name = {len(emp_1)}")
print(f"Sum of emp_1 and emp_2 pay = {emp_1 + emp_2}")
