# Video 4 - Inheritance
# https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4


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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"--> {emp.full_name()}")


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

dev_1 = Developer("Ana", "Luiza", 70000, "Java")
dev_2 = Developer("Lele", "Perez", 70000, "Python")

manager_1 = Manager("Jabs", "Barreto", 10000, [dev_1])

print(manager_1.full_name())
manager_1.print_emps()

print()

manager_1.add_emp(dev_2)
manager_1.print_emps()

manager_1.remove_emp(dev_1)

print()

manager_1.print_emps()

# print(dev_1.full_name())
# print(dev_2.full_name())

# print(help(Developer))  # Help to look up about the class

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

print(f"{dev_1.full_name()} = {dev_1.prog_lang}")
print(f"{dev_2.full_name()} = {dev_2.prog_lang}")

# print(dev_1.num_of_emps)
print(f"Number of Employees from Employee class = {Employee.num_of_emps}")
print(f"Nunber of Employees from Developer class = {Developer.num_of_emps}")
print(f"Nunber of Employees from Manager class = {Manager.num_of_emps}")

print(isinstance(dev_1, Developer))
print(isinstance(dev_1, Employee))
print(isinstance(dev_1, Manager))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))
