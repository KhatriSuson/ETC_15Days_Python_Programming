class Engine:
    def __init__(self, fuel_name):
        self.__fuel_name = fuel_name

    def get_fuel_name(self):
        return self.__fuel_name


class Car:
    def __init__(self, brand, model, fuel_name):
        self.__brand = brand
        self.__model = model
        self.__engine = Engine(fuel_name)

    def get_info(self):
        return f"Brand: {self.__brand}\n Model: {self.__model}\n Fuel Name: {self.__engine.get_fuel_name()}"


obj = Car("Toyota", "2023", "Pretol")
print(obj.get_info())
