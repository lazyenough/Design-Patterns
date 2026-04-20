from abc import ABC, abstractmethod

#Component
class OrganizationMember(ABC):
    @abstractmethod
    def show_details(self, indent=0):
        pass

#Leaf
class Employee(OrganizationMember):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def show_details(self, indent=0):
        print(" "*indent + f"Name - {self.name}, Role - {self.role}.")

# Composite
class Manager(OrganizationMember):
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.subordinates = []

    def add(self, emp):
        self.subordinates.append(emp)

    def show_details(self, indent=0):
        print(" "*indent + f"Name - {self.name}, Role - {self.role}.")

        print(" "*indent + "Subordinates:")
        for emp in self.subordinates:
            emp.show_details(indent+4)


if __name__ == "__main__":
    manager1 = Manager("M1", "AI Manager")
    manager2 = Manager('M2', 'AI Lead')

    emp1 = Employee('E1', 'AI Developer')
    emp2 = Employee('E2', 'Backend Developer')
    emp3 = Employee('E3', 'Frontend Developer')

    manager2.add(emp2)
    manager2.add(emp3)

    manager1.add(emp1)
    manager1.add(manager2)

    manager1.show_details()