class Teacher:
    def read(self):
        print("Teacher is reading.")

class Student(Teacher):  # Inheritance
    # read() method is overriding
    def read(self):
        # call the read() method of the superclass using super()
        super().read()
        print("Student is reading.")

obj = Student()
obj.read()  # Output: Student is reading.
