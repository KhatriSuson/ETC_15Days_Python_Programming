class One:
    def one(self, name, position):
        self.name = name
        self.position = position
        print(f"My name is {self.name} and my position is {self.position}")

class Two(One):
    def two(self, company_name):
        self.c_name = company_name

        print(f"The name of company is  {self.c_name}.")  

class Three(Two):
    def three(self, age,  salary):
        self.age = age
        self.salary = salary
        print(f"The age of developer is {self.age} and salary of developer is {self.salary}")

obj = Three()
obj.one("John", "Developer")
obj.two("All it solution")
obj.three(23, "90k")


# OUTPUT

# My name is John and my position is Developer
# The name of company is  All it solution.
# The age of developer is 23 and salary of developer is 90k