from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2  # math.pi = 3.14.......

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2

    def perimeter(self):
        return 4 * self.length


# Trying to instantiate Shape class will occur an erro

circle = Circle(5)
square = Square(3)

print("The area of circle: ", circle.area())
print("The perimeter of circle: ", circle.perimeter())
print("The area of square: ", square.area())
print("The perimeter of Square: ", square.perimeter())


# print(math.pi)

# try:
#     shape = Shape()
#     print(shape.area())

# except Exception as e:
#     print(e)