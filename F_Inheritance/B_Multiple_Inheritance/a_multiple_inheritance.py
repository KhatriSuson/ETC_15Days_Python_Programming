class Grandpa:  # super base
    def grand(self):
        print("I am your grandfather.")


class Father:  # super one base1
    def father(self):
        print("I am your father")


class Child(Grandpa, Father):
    pass


obj = Child()
obj.grand()
obj.father()
