class Shape:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__(w, h)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


square = Square(5)
rectangle = Rectangle(4, 5)

print("Area of Square is", square.area())
print("Area of reactange is", rectangle.area())


# Area of Square is 25
# Area of reactange is 20