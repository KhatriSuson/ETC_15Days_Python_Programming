def area(shape):
    return shape.area()

class Rectangel:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Circle:
    def __init__(self, radius):
        self.redius = radius


    def area(self):
        return 3.14 * self.redius ** 2
    
rect_obj = Rectangel(5, 3)
print("Area of rectangle = ", area(rect_obj))

circle_obj = Circle(6)
print("Area of circle = ", area(circle_obj))