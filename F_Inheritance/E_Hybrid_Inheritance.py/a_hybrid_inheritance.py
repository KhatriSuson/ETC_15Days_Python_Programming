class A:  # super class
    def methodA(self):
        print("Method A")


class B(A):  
    def methodB(self):
        print("Method B")


class C(A):
    def methodC(self):
        print("Method C")


class D(B, C):
    def methodD(self):
        print("Method D")


d = D()
d.methodA()  # Output: Method A
d.methodB()  # Output: Method B
d.methodC()  # Output: Method C
d.methodD()  # Output: Method D


# OUTPUT
# Method A
# Method B
# Method C
# Method D