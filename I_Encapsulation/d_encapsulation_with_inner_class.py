
class University:
    class Department:
        def __init__(self, name):
            self.name = name

    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, name):
        self.departments.append(self.Department(name))

    def display_departments(self):
        for department in self.departments:    # for i in range
            print(f"Departments: {department.name}")

obj = University("Sanothimi")
obj.add_department("ICT")
obj.add_department("Computer Science")
obj.display_departments()