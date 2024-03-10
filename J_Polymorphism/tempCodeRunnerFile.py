def area(shape):
    return shape.area()


class Rectangle:
    def __inti__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


rect_obj = Rectangle(5, 6)
circle_obj = Circle(2)
print("Area of rectangle is : ", area(rect_obj))
print("Area of circle is : ", area(circle_obj))
