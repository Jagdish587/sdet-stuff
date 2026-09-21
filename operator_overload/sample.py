class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


def compare_employee(employee_1, employee_2):
    if employee_1 > employee_2:
        print("employee_1 is greater than employee_2")
    else:
        print("employee_2 is greater than employee_1")


employee_1 = Employee("Jagdish", 5000)
employee_2 = Employee("Saheed", 7000)

compare_employee(employee_1, employee_2)
