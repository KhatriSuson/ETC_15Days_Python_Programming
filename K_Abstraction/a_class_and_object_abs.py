from abc import ABC, abstractclassmethod 

class Animal(ABC):
    @abstractclassmethod   # abstract decorator is used to make abstract method
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "woof!"

class Cat(Animal):
    def sound(self):
        return "meow!"

dog = Dog()
print(dog.sound())
cat = Cat()
print(cat.sound())
