class Super:
    def super(self, args1):
        print("hello,", args1)

class Super1:
    def super1(self, args2):
        print("HI", args2)

class Child(Super, Super1):
    def child(self, args3):
        print("i am here,", args3)


obj = Child()
obj.super("i am super first class .")   # super method call
obj.super1("I am second super class")
obj.child("I am child class method.")


# hello, i am super first class .
# HI I am second super class
# i am here, I am child class method.