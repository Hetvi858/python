# Write a program to implement single multilevel and multiple inheritance.

# Single
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"employee: {self.name}, id: {self.emp_id}"


class Manager(Employee):
    def assign_task(self, task):
        return f"manager: {self.name}, task: {task}"


# Multilevel (Employee -> Manager -> Executive)
class Executive(Manager):
    def approve_budget(self, amount):
        return f"executive: {self.name}, amount: ${amount}"


# Multiple Inheritance support classes
class Coder:
    def write_code(self, subject):
        return f"write a code in {subject}"


# TechLead combining Manager and Coder (Multiple Inheritance)
class TechLead(Manager, Coder):
    def lead_project(self, project_name):
        return f"Tech Lead {self.name} is steering the project '{project_name}'"


if __name__ == "__main__":
    print("1. Single Inheritance")
    mgr = Manager("raj", 101)
    print(mgr.get_details())         
    print(mgr.assign_task("Database Migration"))  

    print("\n2. Multilevel Inheritance")
    exec_officer = Executive("yug", 102)
    print(exec_officer.get_details())         
    print(exec_officer.assign_task("Quarterly Review"))  
    print(exec_officer.approve_budget(50000))  

    print("\n3. Multiple Inheritance")
    lead = TechLead("Charmi", 103)
    print(lead.get_details())        
    print(lead.assign_task("Architecture Setup"))
    print(lead.write_code("Python"))  
    print(lead.lead_project("Cloud Migration"))
