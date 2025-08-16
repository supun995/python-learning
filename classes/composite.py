"""
Object inheritance is a core aspect of object oriented programming.
It's used inside the Python runtime by every object except for the root type named object.
Object composition is another aspect of object oriented programming.
Composition consists of accessing the functionality from other object types through attributes.
Where inherited objects have an is a relationship, composite object are more of a has a relationship.

The code in this lab step demonstrates composition by modeling a rudimentary company.
The model is composed of the following classes: Employee, Department, and Company.
The Company class is composed from the other two classes.

"""

class Employee:
    def __init__(self, name: str, manager=None):
        self.name = name
        self.manager = manager

    def __str__(self):
        if self.manager:
            return f'{self.name}: managed by: {self.manager.name}.'
        return f'{self.name}.'

    def __repr__(self):
        return str(self)


class Department:
    def __init__(self, name: str, head: Employee=None):
        self.name = name
        self.head = head
        self.team = []

    def with_team(self, *members):
        self.team += members
        return self

    def with_head(self, head):
        self.head = head
        return self

    def __str__(self):
        return f'{self.name}: headed by: {self.head}. Team: {self.team}'

    def __repr__(self):
        return str(self)

"""
The Company class is composed of the Employee and Department classes.
"""
class Company:
    def __init__(self):
        self.c_suite = [
            Employee('Q Q'),
            Employee('R R'),
            Employee('S S'),
        ]

        self.departments = [
            Department('HR').with_team(
                Employee('A A'),
                Employee('B B'),
            ).with_head(
                Employee('Y Y')
            ),
            Department('DEV').with_team(
                Employee('C C'),
                Employee('D D'),
            ).with_head(
                Employee('Z Z')
            ),
        ]

    def __str__(self):
        return f'C Suite: {self.c_suite} Departments: {self.departments}'

    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    company = Company()
    print(company)

"""
Composition consists of interacting with other object types through attributes. 
Composite classes leverage the functionality of the classes without augmentation. 
Unlike inherited classes which allow derived classes to augment the functionality of the base class.
"""