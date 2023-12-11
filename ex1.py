class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.empCount -=1

    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in init)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
        
    def modify_task(self,task_name,status="New"):
        self.tasks[task_name]=status

    def display_task(self,status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    """Class representing a manager, inheriting from Employee"""
    mgrCount = 0

    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = "F08"
        Manager.mgrCount += 1

    def display_employee(self):
        print("Department: ",self.department)

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Manager.mgrCount}")    

m1=Manager("M1",5000,"Marketing")

m1.display_employee()

e1=Employee("Employee1",4000)
e2=Employee("Employee2",4500)



print(e1.empCount)
print(m1.mgrCount)

import pytest

from ex1 import Employee,Manager

def test_employee_creation():
    e=Employee("E1",5000)
    assert e.nam == "E1"
    assert e.salary == 5000

def test_manager_creation():
    m=Manager("M1",6000,"D1")
    assert m.name == "M1"
    assert m.salary == 6000
    assert m.department == "D1"

def test_display_employee():
    e=Employee("E1",5000)
    assert e.display_employee() == "Name: E1, Salary: 5000"

def test_display_manager():
    m=Manager("M1",6000,"D1")
    assert m.display_employee() == "Salary: 6000"
