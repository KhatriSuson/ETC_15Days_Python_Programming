class Value:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # __add__(a + b)
        return Value(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


obj1 = Value(1, 3)
obj2 = Value(3, 5)

print(obj1 + obj2)
