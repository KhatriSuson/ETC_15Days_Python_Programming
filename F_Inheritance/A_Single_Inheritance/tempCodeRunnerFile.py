# class Teacher:
#     def read(self):
#         print("Teacher is reading.")


# class Student(Teacher):  # Inheritance
#     # read() method is overriding

#     def read(self):
#         super().read()
#         print("Student is reading.")


# obj = Student()
# obj.read()


class Laptop:
    def facebook(self):
        print("I am using facebook in laptop")


class Mobile:
    def facebook(self):
        super().facebook()
        print("i am using facebook  in mobile")


class Child(Laptop, Mobile):  # Multiple inheritance
    pass


obj = Child()
obj.facebook()
