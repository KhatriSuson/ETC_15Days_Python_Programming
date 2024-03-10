class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

def make_sound(animal):
    return animal.sound()

d_obj = Dog()
c_obj = Cat()

print(make_sound(d_obj))  # Output: Woof!
print(make_sound(c_obj))  # Output: Meow!