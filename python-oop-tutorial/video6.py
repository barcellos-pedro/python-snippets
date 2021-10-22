# Video 6 - Property Decorators - Getters, Setters, and Deleters
# https://youtu.be/jCzT9XFZ5bw?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleting employee name...')
        self.first = None
        self.last = None


emp_1 = Employee("Corey", "Schafer")

emp_1.first = 'Jim'  # The e-mail keeps with the initial value
emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

print(emp_1.__dict__)

del emp_1.fullname

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

print(__name__)
