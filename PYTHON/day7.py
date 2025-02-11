'''


class Employee:
    def __init__(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary, department)
        self.department = department

class Engineer(Employee):
    def __init__(self, name, age, salary, department, skills):
        super().__init__(name, age, salary, department)
        self.skills = skills

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def find_manager(self, department):
        for employee in self.employees:
            if isinstance(employee, Manager) and employee.department == department:
                return employee
        return None

    def count_employees_by_department(self, department):
        return len([employee for employee in self.employees if employee.department == department])

    def find_engineers_by_skill(self, skill):
        return [engineer for engineer in self.employees if isinstance(engineer, Engineer) and skill in engineer.skills]

    def total_employees_by_department(self):
        dept_count = {}
        for employee in self.employees:
            if employee.department in dept_count:
                dept_count[employee.department] += 1
            else:
                dept_count[employee.department] = 1
        return dept_count

    def total_employees(self):
        return len(self.employees)

company = Company()
company.add_employee(Manager("Alice", 40, 80000, "HR"))
company.add_employee(Engineer("Bob", 30, 60000, "Engineering", ["Python", "Java"]))
company.add_employee(Engineer("Charlie", 35, 65000, "Engineering", ["C++", "Java"]))
company.add_employee(Engineer("Diana", 28, 62000, "Engineering", ["Python", "Go"]))
company.add_employee(Employee("Eve", 25, 50000, "HR"))

print(company.total_employees_by_department())
print(company.total_employees())



'''
# Polymorphism 
# ducktyping 
# operator overloading 
# method overloading 
# method ovreloading 

from abc import ABC , abstractmetod 
class Father():
    def display(self):
        print('i am display from father abstract class')
    @abstractmethod
    def myabstractmehtod(self):
        pass
class Child(Father):
    def myabstractmehtod(self):
        print('hello from child implementing abstract mehtod of father')

c=Child()
c.myabstractmehtod()
c.display()
