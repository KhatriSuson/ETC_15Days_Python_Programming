class Grandpa:
    def grand(self):
        print("I am your grandfather.")


class Father:
    def father(self):
        print("I am your father")


class Child(Grandpa, Father):
    pass


obj = Child()
obj.grand()
obj.father()
