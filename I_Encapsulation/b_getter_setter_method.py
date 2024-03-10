class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balnace += amount  # self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount  # balance = balance - amount
        else:
            print("Insufficient funds")


obj = BankAccount(1000)
print("The total amount =", obj.get_balance())  # output 1000
obj.withdraw(100)
print("The amount after withdraw = ", obj.get_balance())  # output  900
