class MyClass:
    def __init__(self, value):
        self.__value = value # private attribute

    def __private_method(self):
        print("This is private method.")
        print(f"The value  of the private attribute = {self.__value}")

    def public_method(self):
        print("This is a public method.")
        self.__private_method()   # Access private method

obj = MyClass(10)
obj.public_method()